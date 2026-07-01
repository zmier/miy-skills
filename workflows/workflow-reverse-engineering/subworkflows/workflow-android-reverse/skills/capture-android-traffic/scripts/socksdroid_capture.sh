#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKFLOW_ROOT="$(cd "$SKILL_DIR/../.." && pwd)"
SESSION="$WORKFLOW_ROOT/skills/process-android-traffic/scripts/mitmproxy-session.sh"
ADB="${ADB_BIN:-$(command -v adb || true)}"
PORT="${SOCKSDROID_PROXY_PORT:-9081}"
PACKAGE="${SOCKSDROID_PACKAGE:-net.typeblog.socks}"
SERVICE="${SOCKSDROID_SERVICE:-$PACKAGE/.SocksVpnService}"
APK="${SOCKSDROID_APK:-}"
TARGET_PACKAGE="${TARGET_PACKAGE:-}"

usage() {
  cat <<EOF
用法：
  SOCKSDROID_APK=/path/SocksDroid.apk $0 install
  TARGET_PACKAGE=com.example.app $0 configure
  TARGET_PACKAGE=com.example.app $0 start
  $0 status
  $0 stop

说明：
  start 会启动 mitmproxy SOCKS5、ADB reverse 和 SocksDroid VpnService。
  首次使用若系统仍要求 VPN 授权，脚本会打开 SocksDroid，由人类确认一次。
EOF
}

require_device() {
  [[ -n "$ADB" ]] || { echo "未找到 adb" >&2; exit 1; }
  local count
  count="$("$ADB" devices | awk 'NR > 1 && $2 == "device" {count++} END {print count+0}')"
  [[ "$count" -eq 1 ]] || {
    echo "需要且只能连接一台 Android 设备，当前为 $count 台" >&2
    exit 1
  }
}

root_shell() {
  "$ADB" shell "su -c '$1'"
}

installed() {
  "$ADB" shell pm path "$PACKAGE" >/dev/null 2>&1
}

vpn_active() {
  "$ADB" shell ip address show 2>/dev/null |
    grep -q '26\.26\.26\.1/24'
}

install_app() {
  require_device
  [[ -f "$APK" ]] || {
    echo "请通过 SOCKSDROID_APK 指定经过核验的 SocksDroid APK" >&2
    exit 2
  }
  "$ADB" install -r "$APK"
}

configure_app() {
  require_device
  installed || { echo "SocksDroid 尚未安装" >&2; exit 1; }

  local uid app_list=""
  uid="$("$ADB" shell dumpsys package "$PACKAGE" |
    awk -F= '/userId=/{gsub(/\r/, "", $2); print $2; exit}')"
  [[ -n "$uid" ]] || { echo "无法读取 SocksDroid UID" >&2; exit 1; }
  [[ -z "$TARGET_PACKAGE" ]] || app_list="$TARGET_PACKAGE"

  local xml encoded
  xml="<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
  <string name=\"Defaultserver\">127.0.0.1</string>
  <int name=\"Defaultport\" value=\"$PORT\" />
  <string name=\"Defaultroute\">all</string>
  <string name=\"Defaultdns\">8.8.8.8</string>
  <int name=\"Defaultdns_port\" value=\"53\" />
  <boolean name=\"Defaultperapp\" value=\"$([[ -n "$app_list" ]] && echo true || echo false)\" />
  <boolean name=\"Defaultappbypass\" value=\"false\" />
  <string name=\"Defaultapplist\">$app_list</string>
  <boolean name=\"Defaultipv6\" value=\"false\" />
  <boolean name=\"Defaultudp\" value=\"false\" />
</map>"
  encoded="$(printf '%s' "$xml" | base64 | tr -d '\n')"

  "$ADB" shell am force-stop "$PACKAGE" >/dev/null
  root_shell "mkdir -p /data/data/$PACKAGE/shared_prefs; echo $encoded | base64 -d > /data/data/$PACKAGE/shared_prefs/profile.xml; chown -R $uid:$uid /data/data/$PACKAGE/shared_prefs; chmod 700 /data/data/$PACKAGE/shared_prefs; chmod 600 /data/data/$PACKAGE/shared_prefs/profile.xml; restorecon -RF /data/data/$PACKAGE/shared_prefs"
  "$ADB" shell cmd appops set "$PACKAGE" ACTIVATE_VPN allow >/dev/null 2>&1 || true
  echo "SocksDroid 已配置：127.0.0.1:${PORT}，目标=${app_list:-全部应用}"
}

start_proxy() {
  MITM_MODE=socks5 \
  MITM_ANDROID_ROUTE=vpn-socks \
  MITM_PORT="$PORT" \
  MITM_TARGET_HOST="${MITM_TARGET_HOST:-}" \
  MITM_TARGET_PATH="${MITM_TARGET_PATH:-/}" \
    "$SESSION" start
}

start_vpn() {
  require_device
  installed || { echo "SocksDroid 尚未安装" >&2; exit 1; }
  local args=(
    am start-foreground-service
    -n "$SERVICE"
    --es SOCKSNAME Default
    --es SOCKSSERV 127.0.0.1
    --ei SOCKSPORT "$PORT"
    --es SOCKSROUTE all
    --es SOCKSDNS 8.8.8.8
    --ei SOCKSDNSPORT 53
    --ez SOCKSIPV6 false
  )
  if [[ -n "$TARGET_PACKAGE" ]]; then
    args+=(
      --ez SOCKSPERAPP true
      --ez SOCKSAPPBYPASS false
      --esa SOCKSAPPLIST "$TARGET_PACKAGE"
    )
  else
    args+=(--ez SOCKSPERAPP false)
  fi
  root_shell "${args[*]}" >/dev/null 2>&1 || true
  sleep 1
  if ! vpn_active; then
    "$ADB" shell monkey -p "$PACKAGE" -c android.intent.category.LAUNCHER 1 >/dev/null
    echo "SocksDroid 尚未建立 VPN。请在手机上确认一次系统 VPN 授权并开启开关。" >&2
    return 3
  fi
}

status_all() {
  require_device
  MITM_MODE=socks5 MITM_ANDROID_ROUTE=vpn-socks MITM_PORT="$PORT" "$SESSION" status
  if installed; then
    echo "socksdroid=installed"
  else
    echo "socksdroid=missing"
  fi
  if vpn_active; then
    echo "vpn=running"
  else
    echo "vpn=stopped"
  fi
}

stop_all() {
  require_device
  root_shell "am stopservice -n $SERVICE" >/dev/null 2>&1 || true
  "$ADB" shell am force-stop "$PACKAGE" >/dev/null 2>&1 || true
  MITM_MODE=socks5 MITM_ANDROID_ROUTE=vpn-socks MITM_PORT="$PORT" "$SESSION" stop
}

case "${1:-}" in
  install) install_app ;;
  configure) configure_app ;;
  start)
    configure_app
    start_proxy
    start_vpn
    status_all
    ;;
  status) status_all ;;
  stop) stop_all ;;
  *) usage; exit 2 ;;
esac
