#!/usr/bin/env bash
set -euo pipefail

ACTION="${1:-status}"
SERVER="${2:-/data/local/tmp/fs-16.0.19}"
ADB="${ADB_BIN:-$(command -v adb || true)}"

[[ -n "$ADB" ]] || {
  printf '未找到 adb。\n' >&2
  exit 1
}

device_count() {
  "$ADB" devices | awk 'NR > 1 && $2 == "device" {count++} END {print count+0}'
}

require_one_device() {
  local count
  count="$(device_count)"
  [[ "$count" -eq 1 ]] || {
    printf '需要且只能连接一台 Android 设备，当前为 %s 台。\n' "$count" >&2
    exit 1
  }
}

server_running() {
  "$ADB" shell su -c "pidof '$(basename "$SERVER")'" 2>/dev/null | tr -d '\r' | grep -Eq '[0-9]'
}

frida_running() {
  "$ADB" shell su -c "pidof frida-server || pidof '$(basename "$SERVER")' || true" 2>/dev/null | tr -d '\r' | grep -Eq '[0-9]'
}

frida_pids() {
  "$ADB" shell su -c "pidof frida-server || pidof '$(basename "$SERVER")' || true" 2>/dev/null | tr -d '\r'
}

start_server() {
  require_one_device
  if frida_running; then
    printf 'frida-server 已启动：%s\n' "$(frida_pids)"
    return 0
  fi
  "$ADB" shell su -c "test -x '$SERVER'" || {
    printf '手机端不存在可执行文件 %s，请先运行 make frida-install-device。\n' "$SERVER" >&2
    exit 1
  }
  if ! server_running; then
    "$ADB" shell su -c "nohup '$SERVER' >/data/local/tmp/frida-server.log 2>&1 &"
    sleep 2
  fi
  server_running || {
    printf 'frida-server 启动失败。\n' >&2
    exit 1
  }
  printf 'frida-server 已启动：%s\n' "$("$ADB" shell su -c "pidof '$(basename "$SERVER")'" | tr -d '\r')"
}

stop_server() {
  require_one_device
  "$ADB" shell su -c "pkill -f '$(basename "$SERVER")'" >/dev/null 2>&1 || true
  "$ADB" shell su -c "pkill -f frida-server" >/dev/null 2>&1 || true
  sleep 1
  if frida_running; then
    printf 'frida-server 未能停止。\n' >&2
    exit 1
  fi
  printf 'frida-server 已停止。\n'
}

show_status() {
  require_one_device
  printf '设备：'
  "$ADB" devices | awk 'NR > 1 && $2 == "device" {print $1}'
  printf 'ABI：'
  "$ADB" shell getprop ro.product.cpu.abilist | tr -d '\r'
  printf 'Root：'
  "$ADB" shell su -c id | tr -d '\r'
  if frida_running; then
    printf 'frida-server：运行中（PID %s）\n' "$(frida_pids)"
  else
    printf 'frida-server：未运行\n'
  fi
}

case "$ACTION" in
  start) start_server ;;
  stop) stop_server ;;
  status) show_status ;;
  *)
    printf '用法：%s start|stop|status [device-server-path]\n' "$0" >&2
    exit 2
    ;;
esac
