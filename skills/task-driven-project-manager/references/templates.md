# Task-Driven Project Templates

Use these snippets when creating or updating a project. Adapt names and paths to the concrete project.

## README Sections

```markdown
# Project Name

## 1. Project Background

## 2. Key Paths

## 3. Task-Driven Architecture

## 4. Task Folder Rules

## 5. Notebook Dashboard

## 6. Environment and Makefile

## 7. TDD and Testing

## 8. Expected Final Outputs

## 9. Run Order

## 10. Notes and Risks

## 11. Phase Reviews and Evidence Maps
```

## TASKxx-说明.md Template

```markdown
# TASKxx：任务名称

## 1. 任务目的

## 2. 上游依赖

## 3. 输入文件

## 4. 执行方法

## 5. 输出文件

## 6. 完成标准

## 7. 测试要求

## 8. 注意事项

## 9. 证据与日志

- ReAct 日志：
- 关键 outputs：
- 关键 docs：
- 上游/下游双链：
```

## Large Exploratory TASK Template

```markdown
# TASKxx：大型探索任务

## 背景

## 目标

## 当前判断

## 子任务结构

```text
subtasks/
├── TASKxx-01-...
├── TASKxx-02-...
└── TASKxx-03-...
```

## 状态表

| 子任务 | 状态 | 证据 | 下一步 |
|---|---|---|---|

## 主证据链

- [[outputs/evidence-report|证据报告]]
- [[logs/log|ReAct 日志]]
- [[docs/decision-note|决策说明]]

## Done Criteria

## 反哺候选

| 经验 | 证据 | 目标 workflow/skill | 状态 |
|---|---|---|---|
```

## ReAct log Template

```markdown
## YYYY-MM-DD HH:mm ReAct：标题

### Thought

### Action

### Observation

### Reflection
```

## Project Phase Review Template

```markdown
# 项目阶段复盘：标题

## 定位

## 一句话总览

## 原始问题如何变化

## 阶段时间线

## 关键 Red -> Green

| Red | Green | 证据 |
|---|---|---|

## 证据地图

- [[tasks/TASK01-name/TASK01-说明|TASK01]]
- [[tasks/TASK02-name/outputs/report|关键报告]]

## 数据/覆盖率边界

## 工程坑与恢复策略

## 可迁移方法

## Workflow / Skill 反哺

| 经验 | 反哺位置 | 证据 |
|---|---|---|

## 下一步
```

## Makefile Template

```makefile
PROJECT_ROOT := $(shell pwd)
VENV := $(PROJECT_ROOT)/.venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
KERNEL_NAME := project-kernel
KERNEL_DISPLAY := Python (Project Name)
REQUIREMENTS := $(PROJECT_ROOT)/common/requirements.txt

.PHONY: help init venv install kernel notebook test test-unit test-e2e test-uat freeze clean-cache

help:
	@echo "Available targets:"
	@echo "  make init        Create folders and virtual environment"
	@echo "  make install     Install dependencies"
	@echo "  make kernel      Register .venv as a Jupyter kernel"
	@echo "  make notebook    Start Jupyter Notebook"
	@echo "  make test        Run all tests"

init:
	mkdir -p common tests/unit tests/e2e tests/uat tests/fixtures tasks final_outputs docs scripts/legacy_or_experimental
	python3 -m venv $(VENV)

venv:
	python3 -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQUIREMENTS)

kernel:
	$(PYTHON) -m ipykernel install --user --name "$(KERNEL_NAME)" --display-name "$(KERNEL_DISPLAY)"

notebook:
	$(PYTHON) -m notebook 00_project_dashboard.ipynb

test:
	$(PYTHON) -m pytest tests

test-unit:
	$(PYTHON) -m pytest tests/unit

test-e2e:
	$(PYTHON) -m pytest tests/e2e

test-uat:
	$(PYTHON) -m pytest tests/uat

freeze:
	$(PIP) freeze > common/requirements.lock.txt

clean-cache:
	find tasks -type d -name cache -maxdepth 3 -exec rm -rf {}/* \;
```

## requirements.txt Starter

```text
pandas
numpy
tqdm
ipykernel
notebook
pytest
openpyxl
```

Add domain packages such as `jieba`, `gensim`, `scikit-learn`, `pdfplumber`, or `python-docx` only when the project needs them.

## Test Style

```python
def test_expected_behavior():
    # GIVEN：明确的输入、fixture 或前置状态

    # WHEN：执行被测试的函数或流程

    # THEN：验证业务可见的输出或副作用
```

## Task Status Table

```markdown
| Task | 状态 | 输入 | 输出 | 是否需要人工 |
|---|---|---|---|---|
| TASK01 | 待运行 | 原始数据 | 数据盘点表 | 否 |
| TASK02 | 待运行 | 需求文档 | 基础配置/词典/规则 | 是，确认口径 |
| TASK03 | 待运行 | TASK01-02 输出 | 中间产物 | 否 |
| TASK04 | 待运行 | 中间产物 | 候选结果 | 否 |
| TASK05 | 待处理 | 候选结果 | 人工定稿结果 | 是，核心人工环节 |
| TASK06 | 待运行 | 定稿结果 | 最终交付 | 否 |
```
