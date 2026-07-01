#!/usr/bin/env bash
set -u

output="${1:-}"
tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

command_status() {
  if command -v "$1" >/dev/null 2>&1; then
    printf '可用'
  else
    printf '缺失'
  fi
}

adb_count=0
device_serial="无"
device_model="无"
android_proxy="未知"
adb_reverse="未知"
if command -v adb >/dev/null 2>&1; then
  adb_count="$(adb devices | awk 'NR > 1 && $2 == "device" {count++} END {print count+0}')"
  if [[ "$adb_count" -eq 1 ]]; then
    device_serial="$(adb get-serialno 2>/dev/null || true)"
    device_model="$(adb shell getprop ro.product.model 2>/dev/null | tr -d '\r')"
    android_proxy="$(adb shell settings get global http_proxy 2>/dev/null | tr -d '\r')"
    adb_reverse="$(adb reverse --list 2>/dev/null | tr '\n' ';')"
  fi
fi

mac_ip="$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || true)"
[[ -n "$mac_ip" ]] || mac_ip="未发现"

reqable_pid="$(pgrep -x Reqable 2>/dev/null | head -1 || true)"
if [[ -n "$reqable_pid" ]]; then
  reqable_state="运行中（PID ${reqable_pid}）"
  reqable_ports="$(lsof -nP -a -p "$reqable_pid" -iTCP -sTCP:LISTEN 2>/dev/null | awk 'NR > 1 {print $9}' | paste -sd ', ' -)"
else
  reqable_state="未运行"
  reqable_ports="无"
fi

if curl -fsS --max-time 2 http://127.0.0.1:18765/health >"$tmp" 2>/dev/null; then
  collector_state="可用"
  collector_health="$(tr '\n' ' ' <"$tmp")"
else
  collector_state="不可用"
  collector_health="无"
fi

if command -v codex >/dev/null 2>&1 && codex mcp get reqable >/dev/null 2>&1; then
  mcp_state="已注册"
else
  mcp_state="未注册"
fi

report="$(cat <<EOF
# Android 抓包就绪报告

- 生成时间：$(date '+%Y-%m-%d %H:%M:%S %z')
- adb：$(command_status adb)
- 在线设备数：$adb_count
- 设备序列号：$device_serial
- 设备型号：$device_model
- Android 全局代理：$android_proxy
- ADB reverse：$adb_reverse
- Mac 局域网地址：$mac_ip
- Reqable：$reqable_state
- Reqable 监听端口：$reqable_ports
- reqable-mcp 注册：$mcp_state
- Report 接收端：$collector_state
- Health：\`$collector_health\`

## 判定

正式采集前应满足：恰好一台 Android 设备在线、Reqable 正在监听代理端口、Android 代理与传输拓扑一致、reqable-mcp 已注册且 Report 接收端健康。USB 模式应看到 `127.0.0.1:<端口>` 和对应的 `adb reverse`。
EOF
)"

if [[ -n "$output" ]]; then
  mkdir -p "$(dirname "$output")"
  printf '%s\n' "$report" >"$output"
  printf '已写入 %s\n' "$output"
else
  printf '%s\n' "$report"
fi
