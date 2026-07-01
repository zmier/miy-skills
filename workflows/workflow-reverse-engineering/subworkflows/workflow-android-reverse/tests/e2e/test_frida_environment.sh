#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# GIVEN：共享环境已经初始化。
test -x "$ROOT/.venv/bin/frida-ps"

# WHEN：检查主机 Frida。
HOST_VERSION="$("$ROOT/.venv/bin/python" -c 'import frida; print(frida.__version__)')"

# THEN：主机版本和项目固定版本一致。
test "$HOST_VERSION" = "16.0.19"

# AND：如果 Node 依赖已经初始化，则通用 Agent 编译器可以独立运行。
if [[ -x "$ROOT/node_modules/.bin/frida-compile" ]]; then
  COMPILE_HELP="$("$ROOT/node_modules/.bin/frida-compile" --help)"
  grep -q 'Usage: frida-compile' <<<"$COMPILE_HELP"
else
  echo "SKIP e2e: frida-compile not installed; run make node-init when JS agent compilation is needed"
fi

echo "PASS e2e: frida host environment"
