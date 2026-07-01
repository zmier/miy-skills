#!/usr/bin/env bash
set -euo pipefail

ADB="${ADB_BIN:-$(command -v adb || true)}"
CONF_DIR="${MITM_CONF_DIR:-$HOME/Library/Application Support/workflow-android-reverse/mitmproxy/config}"
CA_CERT="${MITM_CA_CERT:-$CONF_DIR/mitmproxy-ca-cert.cer}"
MODULE_ID="${MITM_CA_MODULE_ID:-alib_mitmproxy_ca}"

root_shell() {
  local command="$1"
  "$ADB" shell "su -c '$command'"
}

require_device() {
  [[ -n "$ADB" ]] || { echo "未找到 adb" >&2; exit 1; }
  [[ "$("$ADB" devices | awk 'NR > 1 && $2 == "device" {count++} END {print count+0}')" -eq 1 ]] || {
    echo "需要且只能连接一台 Android 设备" >&2
    exit 1
  }
  root_shell "id" | grep -q 'uid=0' || {
    echo "设备 Root 不可用" >&2
    exit 1
  }
}

cert_name() {
  openssl x509 -inform PEM -subject_hash_old -in "$CA_CERT" -noout | head -1
}

status() {
  require_device
  [[ -f "$CA_CERT" ]] || {
    echo "host_ca=missing"
    echo "module=missing"
    exit 1
  }
  local name
  name="$(cert_name)"
  echo "host_ca=$CA_CERT"
  echo "cert_name=${name}.0"
  if root_shell "test -f /data/adb/modules/$MODULE_ID/system/etc/security/cacerts/${name}.0"; then
    echo "module=installed"
  else
    echo "module=missing"
  fi
  if root_shell "test -f /system/etc/security/cacerts/${name}.0"; then
    echo "system_store=loaded"
  else
    echo "system_store=not-loaded"
  fi
}

install_magisk() {
  require_device
  [[ -f "$CA_CERT" ]] || {
    echo "未找到 mitmproxy CA：$CA_CERT；先启动一次 mitmproxy 会话生成 CA" >&2
    exit 1
  }

  local tmp name module
  tmp="$(mktemp -d)"
  trap "rm -rf '$tmp'" EXIT
  name="$(cert_name)"
  module="$tmp/$MODULE_ID"
  mkdir -p "$module/system/etc/security/cacerts"
  cp "$CA_CERT" "$module/system/etc/security/cacerts/${name}.0"
  chmod 644 "$module/system/etc/security/cacerts/${name}.0"
  cat >"$module/module.prop" <<EOF
id=$MODULE_ID
name=Alib mitmproxy CA
version=1
versionCode=1
author=alib
description=Systemless mitmproxy CA for authorized Android traffic research
EOF

  tar -C "$tmp" -czf "$tmp/module.tgz" "$MODULE_ID"
  "$ADB" push "$tmp/module.tgz" /data/local/tmp/alib-mitmproxy-ca.tgz >/dev/null
  root_shell "rm -rf /data/adb/modules/$MODULE_ID && mkdir -p /data/adb/modules && tar -xzf /data/local/tmp/alib-mitmproxy-ca.tgz -C /data/adb/modules && rm /data/local/tmp/alib-mitmproxy-ca.tgz && touch /data/adb/modules/$MODULE_ID/update"
  echo "CA 模块已部署。执行 reboot 后由 Magisk 加载。"
}

remove_magisk() {
  require_device
  root_shell "rm -rf /data/adb/modules/$MODULE_ID"
  echo "CA 模块已移除；重启后生效。"
}

case "${1:-status}" in
  status) status ;;
  install-magisk) install_magisk ;;
  remove-magisk) remove_magisk ;;
  *) echo "用法：$0 status|install-magisk|remove-magisk" >&2; exit 2 ;;
esac
