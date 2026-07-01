#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKFLOW_ROOT="$(cd "$SKILL_DIR/../.." && pwd)"
MITMDUMP="${MITMDUMP_BIN:-$WORKFLOW_ROOT/.venv/bin/mitmdump}"
ADB="${ADB_BIN:-$(command -v adb || true)}"
PORT="${MITM_PORT:-9080}"
MODE="${MITM_MODE:-regular}"
ANDROID_ROUTE="${MITM_ANDROID_ROUTE:-global-proxy}"
RUNTIME_DIR="${MITM_RUNTIME_DIR:-$HOME/Library/Application Support/workflow-android-reverse/mitmproxy}"
STATE_DIR="$RUNTIME_DIR/state"
CONF_DIR="$RUNTIME_DIR/config"
PID_FILE="$STATE_DIR/mitmdump.pid"
PLIST_FILE="$STATE_DIR/com.narra.workflow-android-reverse.mitmproxy.plist"
LAUNCH_LABEL="com.narra.workflow-android-reverse.mitmproxy"
PREVIOUS_PROXY_FILE="$STATE_DIR/previous-proxy"
LOG_FILE="${MITM_LOG_FILE:-$RUNTIME_DIR/mitmdump.log}"
FLOW_FILE="${MITM_FLOW_FILE:-$RUNTIME_DIR/capture.mitm}"
EVENT_FILE="${MITM_EVENT_FILE:-$RUNTIME_DIR/events.jsonl}"
ADDON="${MITM_ADDON:-$SKILL_DIR/scripts/target_capture_addon.py}"
SAVE_FLOWS="${MITM_SAVE_FLOWS:-0}"
HTTP2="${MITM_HTTP2:-1}"

mkdir -p "$STATE_DIR" "$CONF_DIR"

device_count() {
  "$ADB" devices | awk 'NR > 1 && $2 == "device" {count++} END {print count+0}'
}

require_device() {
  [[ -n "$ADB" ]] || { echo "未找到 adb" >&2; exit 1; }
  local count
  count="$(device_count)"
  [[ "$count" -eq 1 ]] || {
    echo "需要且只能连接一台 Android 设备，当前为 $count 台" >&2
    exit 1
  }
}

running() {
  [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null
}

restore_proxy() {
  local previous=":0"
  [[ -f "$PREVIOUS_PROXY_FILE" ]] && previous="$(cat "$PREVIOUS_PROXY_FILE")"
  if [[ "$previous" == "null" || -z "$previous" || "$previous" == "127.0.0.1:${PORT}" ]]; then
    previous=":0"
  fi
  "$ADB" shell settings put global http_proxy "$previous" >/dev/null
  "$ADB" reverse --remove "tcp:${PORT}" >/dev/null 2>&1 || true
  if [[ "$previous" =~ ^127\.0\.0\.1:([0-9]+)$ ]]; then
    "$ADB" reverse "tcp:${BASH_REMATCH[1]}" "tcp:${BASH_REMATCH[1]}" >/dev/null
  fi
}

start_session() {
  require_device
  [[ "$MODE" == "regular" || "$MODE" == "socks5" ]] || {
    echo "MITM_MODE 仅支持 regular 或 socks5" >&2
    exit 2
  }
  [[ "$ANDROID_ROUTE" == "global-proxy" || "$ANDROID_ROUTE" == "vpn-socks" ]] || {
    echo "MITM_ANDROID_ROUTE 仅支持 global-proxy 或 vpn-socks" >&2
    exit 2
  }
  [[ -x "$MITMDUMP" ]] || { echo "未找到 mitmdump：$MITMDUMP" >&2; exit 1; }
  running && { echo "mitmdump 已运行：PID $(cat "$PID_FILE")"; return; }

  local current_proxy
  current_proxy="$("$ADB" shell settings get global http_proxy | tr -d '\r')"
  if [[ "$current_proxy" != "127.0.0.1:${PORT}" || ! -s "$PREVIOUS_PROXY_FILE" ]]; then
    printf '%s\n' "$current_proxy" >"$PREVIOUS_PROXY_FILE"
  fi
  : >"$LOG_FILE"
  : >"$EVENT_FILE"

  local args=(
    --listen-host 127.0.0.1
    --listen-port "$PORT"
    --set "confdir=$CONF_DIR"
    --set block_global=false
    --set connection_strategy=lazy
    --set "http2=$HTTP2"
    -s "$ADDON"
  )
  if [[ "$MODE" != "regular" ]]; then
    args+=(--mode "$MODE")
  fi
  if [[ "$SAVE_FLOWS" == "1" ]]; then
    args+=(--save-stream-file "$FLOW_FILE")
  fi

  launchctl bootout "gui/$(id -u)/$LAUNCH_LABEL" >/dev/null 2>&1 || true
  rm -f "$PLIST_FILE"

  MITM_PROGRAM="$MITMDUMP" \
  MITM_ARGS="$(printf '%s\n' "${args[@]}")" \
  MITM_EVENT_FILE="$EVENT_FILE" \
  MITM_TARGET_HOST="${MITM_TARGET_HOST:-}" \
  MITM_TARGET_PATH="${MITM_TARGET_PATH:-/}" \
  MITM_LOG_FILE="$LOG_FILE" \
  MITM_PID_FILE="$PID_FILE" \
  "$WORKFLOW_ROOT/.venv/bin/python" - <<'PY'
import os
import subprocess
from pathlib import Path

environment = os.environ.copy()
log_path = Path(os.environ["MITM_LOG_FILE"])
with log_path.open("ab", buffering=0) as log:
    process = subprocess.Popen(
        [os.environ["MITM_PROGRAM"], *os.environ["MITM_ARGS"].splitlines()],
        stdin=subprocess.DEVNULL,
        stdout=log,
        stderr=log,
        env=environment,
        start_new_session=True,
        close_fds=True,
    )
Path(os.environ["MITM_PID_FILE"]).write_text(str(process.pid))
PY

  for _ in {1..30}; do
    if lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
      "$ADB" reverse "tcp:${PORT}" "tcp:${PORT}" >/dev/null
      if [[ "$ANDROID_ROUTE" == "global-proxy" ]]; then
        "$ADB" shell settings put global http_proxy "127.0.0.1:${PORT}" >/dev/null
      else
        "$ADB" shell settings put global http_proxy :0 >/dev/null
      fi
      status_session
      return
    fi
    sleep 0.2
  done

  stop_session
  echo "mitmdump 未能监听端口 ${PORT}，见 ${LOG_FILE}" >&2
  exit 1
}

stop_session() {
  require_device
  if running; then
    local pid
    pid="$(cat "$PID_FILE")"
    kill -TERM "-$pid" >/dev/null 2>&1 || kill "$pid" >/dev/null 2>&1 || true
    for _ in {1..20}; do
      running || break
      sleep 0.1
    done
    running && kill -KILL "-$pid" >/dev/null 2>&1 || true
  fi
  rm -f "$PID_FILE"
  restore_proxy
  rm -f "$PREVIOUS_PROXY_FILE"
  status_session
}

status_session() {
  require_device
  local state="stopped"
  running && state="running"
  printf 'mitmdump=%s\n' "$state"
  printf 'mode=%s\n' "$MODE"
  printf 'android_route=%s\n' "$ANDROID_ROUTE"
  printf 'port=%s\n' "$PORT"
  printf 'http2=%s\n' "$HTTP2"
  printf 'proxy=%s\n' "$("$ADB" shell settings get global http_proxy | tr -d '\r')"
  printf 'reverse=%s\n' "$("$ADB" reverse --list | tr '\n' ';')"
  printf 'events=%s\n' "$EVENT_FILE"
  if [[ "$SAVE_FLOWS" == "1" ]]; then
    printf 'flows=%s\n' "$FLOW_FILE"
  else
    printf 'flows=disabled\n'
  fi
  printf 'log=%s\n' "$LOG_FILE"
}

case "${1:-status}" in
  start) start_session ;;
  stop) stop_session ;;
  status) status_session ;;
  *) echo "用法：$0 start|stop|status" >&2; exit 2 ;;
esac
