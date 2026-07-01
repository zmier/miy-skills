#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf '用法：%s enable-usb <端口> | enable-lan <代理主机> <端口> | disable [端口] | status\n' "$0" >&2
  exit 2
}

[[ $# -ge 1 ]] || usage
action="$1"
device_count="$(adb devices | awk 'NR > 1 && $2 == "device" {count++} END {print count+0}')"
[[ "$device_count" -eq 1 ]] || {
  printf '需要且只能有一台在线 Android 设备，当前为 %s 台。\n' "$device_count" >&2
  exit 1
}

case "$action" in
  enable-usb)
    [[ $# -eq 2 ]] || usage
    port="$2"
    [[ "$port" =~ ^[0-9]+$ ]] || usage
    adb reverse "tcp:${port}" "tcp:${port}"
    adb shell settings put global http_proxy "127.0.0.1:${port}"
    ;;
  enable-lan)
    [[ $# -eq 3 ]] || usage
    host="$2"
    port="$3"
    [[ "$port" =~ ^[0-9]+$ ]] || usage
    adb shell settings put global http_proxy "${host}:${port}"
    ;;
  disable)
    [[ $# -le 2 ]] || usage
    port="${2:-9000}"
    adb shell settings put global http_proxy :0
    adb reverse --remove "tcp:${port}" >/dev/null 2>&1 || true
    ;;
  status)
    ;;
  *)
    usage
    ;;
esac

printf 'Android 全局代理：'
adb shell settings get global http_proxy | tr -d '\r'
printf 'ADB reverse：'
adb reverse --list
