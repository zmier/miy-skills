PROJECT_ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
WRITER_ROOT := $(abspath $(PROJECT_ROOT)/../../../../../..)
PYTHON := $(PROJECT_ROOT)/.venv/bin/python
FRIDA_VERSION := 16.0.19
FRIDA_ARCH := android-arm64
FRIDA_ARCHIVE := $(PROJECT_ROOT)/tools/frida-server-$(FRIDA_VERSION)-$(FRIDA_ARCH).xz
FRIDA_SERVER := $(PROJECT_ROOT)/tools/frida-server-$(FRIDA_VERSION)-$(FRIDA_ARCH)
FRIDA_URL := https://github.com/frida/frida/releases/download/$(FRIDA_VERSION)/frida-server-$(FRIDA_VERSION)-$(FRIDA_ARCH).xz
DEVICE_SERVER := /data/local/tmp/fs-$(FRIDA_VERSION)
MIKU_ROOT ?= $(WRITER_ROOT)/00 信息/工具/alib-miku-sync
NATIVE_TOOLCHAIN_SKILL := $(PROJECT_ROOT)/skills/prepare-android-native-toolchain
MITM_SKILL := $(PROJECT_ROOT)/skills/process-android-traffic
IDA_APP ?= /Applications/ida.app
REPORT ?= /tmp/workflow-android-reverse/native-toolchain-status.md
MITM_TARGET_HOST ?=
MITM_TARGET_PATH ?= /

.PHONY: help init python-init node-init validate-mermaid native-status ida-open frida-download frida-install-device frida-start frida-stop frida-status frida-ps mitm-start mitm-stop mitm-status mitm-ca-status mitm-ca-install mitm-ca-remove socks-capture-start socks-capture-stop socks-capture-status install-tools miku-install test test-unit test-e2e clean

help:
	@echo "Android reverse workflow:"
	@echo "  make init                 创建 .venv 并锁定 Python/Node 依赖"
	@echo "  make frida-install-device 下载并安装同版本 arm64 frida-server"
	@echo "  make frida-start          在已 Root 的单台设备上启动 frida-server"
	@echo "  make frida-stop           停止手机端 frida-server"
	@echo "  make frida-status         检查版本、设备、进程和连通性"
	@echo "  make mitm-start           启动 USB mitmproxy 抓包，支持 MITM_TARGET_HOST/PATH"
	@echo "  make mitm-stop            停止 mitmproxy 并恢复先前代理"
	@echo "  make mitm-ca-status       检查 systemless CA 是否加载"
	@echo "  make mitm-ca-install      部署 Magisk CA 模块，需重启后生效"
	@echo "  make mitm-ca-remove       移除 Magisk CA 模块，需重启后生效"
	@echo "  make socks-capture-start  用 SocksDroid/VPN 强制转发目标 App"
	@echo "  make socks-capture-stop   停止 SocksDroid 与 SOCKS5 mitmproxy"
	@echo "  make validate-mermaid     校验通用请求构造账本模板"
	@echo "  make native-status        检查 JNI/NDK/IDA/Native 工具链，REPORT 可覆盖"
	@echo "  make ida-open SO=...      用已通过 Smoke 的 IDA 打开目标 so"
	@echo "  make miku-install         重新构建并安装 Miku 菜单栏应用"
	@echo "  make test                 运行 Workflow 自身 unit/e2e 测试"

init: python-init node-init

python-init:
	@uv sync --no-config --project "$(PROJECT_ROOT)" --python /Users/narra/.local/bin/python3.12

node-init:
	@cd "$(PROJECT_ROOT)" && npm install

validate-mermaid:
	@cd "$(PROJECT_ROOT)" && node scripts/validate-mermaid.mjs \
		"skills/android-request-reproduction/assets/request-construction-ledger-template.md"

native-status:
	@"$(NATIVE_TOOLCHAIN_SKILL)/scripts/check_native_toolchain.sh" "$(REPORT)"

ida-open:
	@test -n "$(SO)" || (echo "用法: make ida-open SO=/absolute/path/to/libtarget.so IDA_APP=/Applications/IDA.app"; exit 2)
	@test -d "$(IDA_APP)" || (echo "IDA_APP 不存在: $(IDA_APP)"; exit 2)
	@open -a "$(IDA_APP)" "$(SO)"

frida-download:
	@mkdir -p "$(PROJECT_ROOT)/tools"
	@test -f "$(FRIDA_ARCHIVE)" || curl -fL "$(FRIDA_URL)" -o "$(FRIDA_ARCHIVE)"
	@test -f "$(FRIDA_SERVER)" || xz -dk "$(FRIDA_ARCHIVE)"
	@chmod 755 "$(FRIDA_SERVER)"

frida-install-device: frida-download
	@adb push "$(FRIDA_SERVER)" "$(DEVICE_SERVER)"
	@adb shell su -c 'chmod 755 "$(DEVICE_SERVER)"'

frida-start:
	@"$(PROJECT_ROOT)/scripts/frida-device.sh" start "$(DEVICE_SERVER)"

frida-stop:
	@"$(PROJECT_ROOT)/scripts/frida-device.sh" stop "$(DEVICE_SERVER)"

frida-status:
	@"$(PROJECT_ROOT)/scripts/frida-device.sh" status "$(DEVICE_SERVER)"

frida-ps:
	@"$(PROJECT_ROOT)/.venv/bin/frida-ps" -Uai

mitm-start:
	@MITM_TARGET_HOST="$(MITM_TARGET_HOST)" \
		MITM_TARGET_PATH="$(MITM_TARGET_PATH)" \
		"$(MITM_SKILL)/scripts/mitmproxy-session.sh" start

mitm-stop:
	@"$(MITM_SKILL)/scripts/mitmproxy-session.sh" stop

mitm-status:
	@"$(MITM_SKILL)/scripts/mitmproxy-session.sh" status

mitm-ca-status:
	@"$(MITM_SKILL)/scripts/manage_android_ca.sh" status

mitm-ca-install:
	@"$(MITM_SKILL)/scripts/manage_android_ca.sh" install-magisk

mitm-ca-remove:
	@"$(MITM_SKILL)/scripts/manage_android_ca.sh" remove-magisk

socks-capture-start:
	@TARGET_PACKAGE="$(TARGET_PACKAGE)" \
		SOCKSDROID_APK="$(SOCKSDROID_APK)" \
		MITM_TARGET_HOST="$(MITM_TARGET_HOST)" \
		"$(PROJECT_ROOT)/skills/capture-android-traffic/scripts/socksdroid_capture.sh" start

socks-capture-stop:
	@"$(PROJECT_ROOT)/skills/capture-android-traffic/scripts/socksdroid_capture.sh" stop

socks-capture-status:
	@"$(PROJECT_ROOT)/skills/capture-android-traffic/scripts/socksdroid_capture.sh" status

install-tools: init frida-install-device
	@echo "Frida 是 CLI 与手机端服务，不创建伪 GUI；入口由项目 Makefile 和 Miku 菜单提供。"

miku-install:
	@$(MAKE) -C "$(MIKU_ROOT)" install

test: test-unit test-e2e

test-unit:
	@"$(PYTHON)" -m pytest tests/unit

test-e2e:
	@bash tests/e2e/test_frida_environment.sh

clean:
	@rm -rf "$(PROJECT_ROOT)/.pytest_cache" \
		"$(PROJECT_ROOT)/tests/__pycache__" \
		"$(PROJECT_ROOT)/tests/unit/__pycache__" \
		"$(PROJECT_ROOT)/src/android_reverse_workflow/__pycache__"
