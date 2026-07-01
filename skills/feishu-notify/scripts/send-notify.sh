#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<EOF
用法：
  $(basename "$0") "标题" "正文" [--feishu] [--alert]

环境变量：
  ALIB_SOURCE       alib 根目录，默认自动从脚本路径向上推断
  ALIB_NOTIFY_PYTHON  覆盖 Python 解释器
  ALIB_NOTIFY_SCRIPT  覆盖 scholar-kit notify.py
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" || "${1:-}" == "help" ]]; then
  usage
  exit 0
fi

if [[ "$#" -lt 2 ]]; then
  usage >&2
  exit 2
fi

TITLE="$1"
MESSAGE="$2"
shift 2

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
GIT_ROOT="$(git -C "$SKILL_DIR" rev-parse --show-toplevel 2>/dev/null || true)"
DEFAULT_ALIB_ROOT=""
for candidate in \
  "$GIT_ROOT" \
  "$GIT_ROOT/../../.." \
  "$SKILL_DIR/../../../.." \
  "$SKILL_DIR/../../../../.."; do
  if [[ -n "$candidate" && -f "${candidate%/}/Writer/.pytools/scholar-kit/scripts/notify.py" ]]; then
    DEFAULT_ALIB_ROOT="$(cd "$candidate" && pwd)"
    break
  fi
done
ALIB_ROOT="${ALIB_SOURCE:-$DEFAULT_ALIB_ROOT}"

if [[ -z "$ALIB_ROOT" ]]; then
  printf '未找到 ALIB_SOURCE，也无法从脚本路径推断 alib 根目录。\n' >&2
  exit 1
fi

NOTIFY_PYTHON="${ALIB_NOTIFY_PYTHON:-${ALIB_ROOT%/}/Writer/.venv/bin/python}"
NOTIFY_SCRIPT="${ALIB_NOTIFY_SCRIPT:-${ALIB_ROOT%/}/Writer/.pytools/scholar-kit/scripts/notify.py}"

if [[ ! -x "$NOTIFY_PYTHON" ]]; then
  if command -v python3 >/dev/null 2>&1; then
    NOTIFY_PYTHON="$(command -v python3)"
  else
    printf '未找到可用 Python：%s\n' "$NOTIFY_PYTHON" >&2
    exit 1
  fi
fi

if [[ ! -f "$NOTIFY_SCRIPT" ]]; then
  printf '未找到通知脚本：%s\n' "$NOTIFY_SCRIPT" >&2
  exit 1
fi

ARGS=("$NOTIFY_PYTHON" "$NOTIFY_SCRIPT" "$MESSAGE" "--title" "$TITLE")
while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --feishu|--alert)
      ARGS+=("$1")
      ;;
    *)
      printf '未知参数：%s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

"${ARGS[@]}"
