#!/usr/bin/env bash
set -euo pipefail

REPORT="${1:?用法: check_native_toolchain.sh <报告路径>}"
mkdir -p "$(dirname "$REPORT")"

command_path() {
  command -v "$1" 2>/dev/null || true
}

status_mark() {
  if [[ -n "$1" ]]; then printf "可用"; else printf "缺失"; fi
}

HOST_ARCH="$(uname -m)"
MACOS_VERSION="$(sw_vers -productVersion 2>/dev/null || true)"
ROSETTA="不可用"
if /usr/bin/pgrep oahd >/dev/null 2>&1 || /usr/bin/arch -x86_64 /usr/bin/true >/dev/null 2>&1; then
  ROSETTA="可用"
fi

SDK_ROOT="${ANDROID_SDK_ROOT:-${ANDROID_HOME:-$HOME/Library/Android/sdk}}"
NDK_ROOT=""
if [[ -d "$SDK_ROOT/ndk" ]]; then
  NDK_ROOT="$(find "$SDK_ROOT/ndk" -mindepth 1 -maxdepth 1 -type d | sort | tail -1)"
fi

INSTALLED_IDA=""
for candidate in \
  "${IDA_APP:-}" \
  "/Applications/ida.app" \
  "/Applications/IDA Professional.app" \
  "/Applications/IDA Pro.app" \
  "/Applications/ida64.app" \
  "$HOME/Applications/IDA Professional.app" \
  "$HOME/Applications/IDA Pro.app"; do
  if [[ -n "$candidate" && -d "$candidate" ]]; then
    INSTALLED_IDA="$candidate"
    break
  fi
done

IDA_VERSION="未发现"
IDA_BINARY_INFO="未发现"
IDA_SIGNATURE="未发现"
if [[ -n "$INSTALLED_IDA" ]]; then
  INFO="$INSTALLED_IDA/Contents/Info.plist"
  BINARY="$(find "$INSTALLED_IDA/Contents/MacOS" -maxdepth 1 -type f 2>/dev/null | head -1)"
  if [[ -f "$INFO" ]]; then
    IDA_VERSION="$(/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' "$INFO" 2>/dev/null || true)"
    [[ -n "$IDA_VERSION" ]] || IDA_VERSION="$(/usr/libexec/PlistBuddy -c 'Print :CFBundleVersion' "$INFO" 2>/dev/null || echo 未知)"
  fi
  if [[ -n "$BINARY" && -f "$BINARY" ]]; then
    IDA_BINARY_INFO="$(file "$BINARY")"
    IDA_SIGNATURE="$(codesign -dv "$BINARY" 2>&1 | tail -1 || true)"
  fi
fi

IDA_RUNNING="否"
if pgrep -if '/IDA[^/]*/Contents/MacOS/|/ida\.app/Contents/MacOS/' >/dev/null 2>&1; then
  IDA_RUNNING="是"
fi

cat >"$REPORT" <<EOF
# Android Native 工具链状态

- 检查时间：$(date '+%Y-%m-%d %H:%M:%S %z')
- 主机：macOS $MACOS_VERSION / $HOST_ARCH
- Rosetta 2：$ROSETTA

## 基础命令

| 命令 | 状态 | 路径 |
|---|---|---|
| adb | $(status_mark "$(command_path adb)") | $(command_path adb) |
| file | $(status_mark "$(command_path file)") | $(command_path file) |
| nm | $(status_mark "$(command_path nm)") | $(command_path nm) |
| otool | $(status_mark "$(command_path otool)") | $(command_path otool) |
| strings | $(status_mark "$(command_path strings)") | $(command_path strings) |
| objdump | $(status_mark "$(command_path objdump)") | $(command_path objdump) |
| readelf | $(status_mark "$(command_path readelf)") | $(command_path readelf) |

## Android SDK / NDK

- SDK：${SDK_ROOT:-未定位}
- NDK：${NDK_ROOT:-未定位}
- 结论：$([[ -n "$NDK_ROOT" ]] && echo N2 候选 || echo 尚未达到 N2)

## IDA

- 已安装应用：${INSTALLED_IDA:-未发现}
- 版本：$IDA_VERSION
- 当前正在运行：$IDA_RUNNING
- 主程序：$IDA_BINARY_INFO
- 签名检查：$IDA_SIGNATURE
- MCP：需在调用方 TASK 中独立验证打开、查询、落盘与关闭

## 下一步

1. 对目标 so 执行 ABI、符号、依赖与注册方式检查。
2. GUI 分析器通过启动 Smoke 后，再验证目标 so 能否完成自动分析。
3. MCP 只作为可选效率层，必须独立验证生命周期与证据落盘。
EOF

printf '%s\n' "$REPORT"
