PROJECT_ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
PYTHON ?= /Users/narra/.local/bin/python3.12
VENV_PYTHON := $(PROJECT_ROOT)/.venv/bin/python
FRIDA_PS := $(PROJECT_ROOT)/.venv/bin/frida-ps
FRIDA := $(PROJECT_ROOT)/.venv/bin/frida
FRIDA_TRACE := $(PROJECT_ROOT)/.venv/bin/frida-trace
MITMPROXY := $(PROJECT_ROOT)/.venv/bin/mitmproxy

.PHONY: help init shared-tool-status frida-version frida-ps-local mitm-version test clean

help:
	@echo "Reverse engineering workflow shared tools:"
	@echo "  make init                Create shared .venv with Frida/mitmproxy"
	@echo "  make shared-tool-status  Show shared host-side tool versions"
	@echo "  make frida-ps-local      List local processes through shared Frida"
	@echo "  make mitm-version        Show mitmproxy version"

init:
	@uv sync --no-config --project "$(PROJECT_ROOT)" --python "$(PYTHON)"

shared-tool-status: frida-version mitm-version

frida-version:
	@"$(VENV_PYTHON)" -c 'import frida; print("frida", frida.__version__)'
	@"$(FRIDA_PS)" --version

frida-ps-local:
	@"$(FRIDA_PS)"

mitm-version:
	@"$(MITMPROXY)" --version

test:
	@"$(VENV_PYTHON)" -m pytest tests

clean:
	@rm -rf "$(PROJECT_ROOT)/.pytest_cache"

