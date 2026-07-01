#!/usr/bin/env bash
set -euo pipefail

serial=""
output=""

usage() {
  printf '用法: %s [--serial 设备序列号] [--output 报告路径]\n' "$0"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --serial)
      serial="${2:?缺少设备序列号}"
      shift 2
      ;;
    --output)
      output="${2:?缺少报告路径}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf '未知参数: %s\n' "$1" >&2
      usage >&2
      exit 64
      ;;
  esac
done

find_adb() {
  local candidate
  if command -v adb >/dev/null 2>&1; then
    command -v adb
    return
  fi
  for candidate in \
    "${ANDROID_SDK_ROOT:-}/platform-tools/adb" \
    "${ANDROID_HOME:-}/platform-tools/adb" \
    "$HOME/Library/Android/sdk/platform-tools/adb" \
    "$HOME/Android/Sdk/platform-tools/adb" \
    "/opt/homebrew/bin/adb" \
    "/usr/local/bin/adb"; do
    if [[ "$candidate" != "/platform-tools/adb" && -x "$candidate" ]]; then
      printf '%s\n' "$candidate"
      return
    fi
  done
  return 1
}

adb_bin="$(find_adb || true)"
if [[ -z "$adb_bin" ]]; then
  printf '未找到 adb。请安装 Android SDK Platform Tools。\n' >&2
  exit 3
fi

"$adb_bin" start-server >/dev/null

if [[ -z "$serial" ]]; then
  mapfile_supported=false
  if help mapfile >/dev/null 2>&1; then
    mapfile_supported=true
  fi
  device_lines="$("$adb_bin" devices | awk 'NR>1 && NF>=2 {print $1 "\t" $2}')"
  usable_count="$(printf '%s\n' "$device_lines" | awk '$2=="device"{n++} END{print n+0}')"
  if [[ "$usable_count" -eq 1 ]]; then
    serial="$(printf '%s\n' "$device_lines" | awk '$2=="device"{print $1; exit}')"
  elif [[ "$usable_count" -eq 0 ]]; then
    printf '没有处于 device 状态的设备：\n%s\n' "$device_lines" >&2
    exit 2
  else
    printf '检测到多台可用设备，请使用 --serial：\n%s\n' "$device_lines" >&2
    exit 2
  fi
fi

adb() {
  "$adb_bin" -s "$serial" "$@"
}

state="$(adb get-state 2>/dev/null || true)"
if [[ "$state" != "device" ]]; then
  printf '设备 %s 当前状态不是 device：%s\n' "$serial" "${state:-unknown}" >&2
  exit 2
fi

shell_value() {
  adb shell "$1" 2>/dev/null | tr -d '\r' | tail -n 1
}

model="$(shell_value 'getprop ro.product.model')"
device="$(shell_value 'getprop ro.product.device')"
manufacturer="$(shell_value 'getprop ro.product.manufacturer')"
android_version="$(shell_value 'getprop ro.build.version.release')"
sdk="$(shell_value 'getprop ro.build.version.sdk')"
abi="$(shell_value 'getprop ro.product.cpu.abi')"
abilist="$(shell_value 'getprop ro.product.cpu.abilist')"
build_type="$(shell_value 'getprop ro.build.type')"
verified_boot="$(shell_value 'getprop ro.boot.verifiedbootstate')"
selinux="$(shell_value 'getenforce')"
shell_id="$(shell_value 'id')"
current_user="$(shell_value 'am get-current-user')"

root_id="$(adb shell 'su -c id' 2>/dev/null | tr -d '\r' | tail -n 1 || true)"
if [[ "$root_id" == *"uid=0"* ]]; then
  root_status="可用"
  readiness="D3"
else
  root_status="不可用或未授权"
  readiness="D2"
fi

magisk_version="$(adb shell 'su -c "magisk -v"' 2>/dev/null | tr -d '\r' | tail -n 1 || true)"
magisk_code="$(adb shell 'su -c "magisk -V"' 2>/dev/null | tr -d '\r' | tail -n 1 || true)"

token="device-check-$(date +%s)-$$"
tmp_result="$(printf '%s' "$token" | adb shell 'cat > /data/local/tmp/android-device-check.txt && chmod 600 /data/local/tmp/android-device-check.txt && cat /data/local/tmp/android-device-check.txt && rm /data/local/tmp/android-device-check.txt' 2>/dev/null | tr -d '\r')"
if [[ "$tmp_result" == "$token" ]]; then
  tmp_status="通过"
else
  tmp_status="失败"
  readiness="D1"
fi

if adb shell 'pm list packages >/dev/null' >/dev/null 2>&1; then
  package_status="通过"
else
  package_status="失败"
  readiness="D1"
fi

adb_version="$("$adb_bin" version | tr '\n' ' ' | sed 's/[[:space:]]\+/ /g')"
report="$(cat <<EOF
# Android 实验设备能力报告

- 检查时间：$(date '+%Y-%m-%d %H:%M:%S %z')
- ADB 路径：\`$adb_bin\`
- ADB 版本：$adb_version
- 设备序列号：\`$serial\`
- 连接状态：\`$state\`
- 设备：${manufacturer} ${model}（${device}）
- Android：${android_version}（API ${sdk}）
- ABI：$abi
- ABI 列表：$abilist
- Build 类型：$build_type
- Verified Boot：$verified_boot
- SELinux：$selinux
- Shell 身份：\`$shell_id\`
- 当前用户：$current_user
- Root：$root_status
- Root 身份：\`${root_id:-未取得}\`
- Magisk 版本：${magisk_version:-未取得}
- Magisk 版本码：${magisk_code:-未取得}
- \`/data/local/tmp\` 临时文件测试：$tmp_status
- 包管理测试：$package_status
- 当前就绪等级：**$readiness**

## 下一步

$(if [[ "$readiness" == "D3" ]]; then
  printf '%s\n' '- 基础 ADB 与 Root 分析环境已就绪。'
  printf '%s\n' '- 后续单独检查 Frida 客户端、服务端版本与连通性，以提升到 D4。'
else
  printf '%s\n' '- 先处理报告中的失败项，再进入动态分析工具安装。'
fi)
EOF
)"

if [[ -n "$output" ]]; then
  mkdir -p "$(dirname "$output")"
  printf '%s\n' "$report" > "$output"
  printf '%s\n' "$output"
else
  printf '%s\n' "$report"
fi
