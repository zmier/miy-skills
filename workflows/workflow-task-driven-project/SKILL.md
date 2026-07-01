---
name: workflow-task-driven-project
description: 分形任务驱动 workflow。别名 workflow-task-driven。用于把任何阶段目标组织成 task-driven project：机会评估、接单判断、项目执行、阶段复盘、能力反哺。可按场景 adaptor 路由外包项目、学术研究、论文研究、软件工具等，并在需要落地项目骨架时复用 task-driven-project-manager。
---

# Task-Driven Project Workflow

## Purpose

把复杂实践从“散着聊、凭感觉推进”升级成可持续演化的分形任务驱动系统：

```text
任意阶段目标/困惑
-> 创建该阶段的 task-driven project
-> TASK 树
-> 证据台账 / ReAct 日志 / Red-Green
-> Gate 判断
-> 下一阶段 task-driven project 或终止
-> 阶段复盘与 workflow / skill 反哺
```

本 workflow 的核心哲学是：

```text
task-driven 是分形结构。
每一层都围绕一个目标拆 TASK、留证据、设验收、做 gate、复盘沉淀。
```

因此，“评估要不要做一个项目”本身也是 task-driven；“完成一个已确认项目”也是 task-driven；“把项目经验沉淀为 workflow/skill”仍然是 task-driven。

本 workflow 不替代具体领域 workflow。它负责目标阶段路由、项目组织、证据治理、阶段 gate、复盘和能力反哺；具体领域方法仍由对应 workflow/skill 承担。

## When To Use

使用本 workflow，当任务出现任一信号：

- 需要判断一个机会、需求、客户单子或研究方向要不要做；
- 需要先做需求澄清、风险评估、PoC 设计或接单决策；
- 项目超过 3 个阶段，且每阶段有独立输入、输出、日志或验收；
- 需要拆成 `TASK01/TASK02/...` 或 `TASKxx-01` 子任务；
- 过程中会不断发现新问题，而不是一开始就知道完整路径；
- 需要区分 raw outputs、证据摘要、最终交付和复盘文档；
- 需要 TDD、UAT、Makefile、Notebook dashboard、SQLite/request pool 或长跑调度；
- 需要用 Obsidian 双链把项目复盘链接回过程证据；
- 项目经验要反哺到可复用 workflow/skill。

如果只是创建一个简单目录骨架，直接使用 `task-driven-project-manager` 即可。若需要判断目标阶段、选择项目类型、先做机会评估、保留 gate 或后续能力反哺，应使用本 workflow。

## Fractal Model

每个阶段都是一个独立目标驱动项目：

```text
阶段 0：机会评估 project
目标：判断要不要做、怎么做、是否先 PoC。

阶段 1：实际执行 project
目标：完成已确认范围内的交付。

阶段 2：交付复盘 project
目标：验收、复盘、沉淀可迁移规则。

阶段 3：能力工程 project
目标：把复用规则迁移到 workflow/skill/template，并做 forward test。
```

父 workflow 不直接把所有阶段塞进一个巨型项目。它先判断当前目标属于哪个阶段，再为该阶段创建或更新对应 task-driven project。

## Modes

```text
mode: diagnose-only
  只做目标澄清、阶段判断、路由、材料清单和建议 project 结构。

mode: scaffold
  创建该阶段 task-driven project 骨架，可复用 task-driven-project-manager。

mode: full-lifecycle
  从机会评估、执行、复盘到能力反哺连续编排多个 task-driven project。
```

默认 mode 为 `scaffold`，除非用户明确只要分析或已经要求完整生命周期管理。

## Structure

```text
workflow-task-driven-project/
├── SKILL.md
├── skills/
│   └── task-driven-project-orchestrator/
│       └── SKILL.md
├── references/
│   ├── routing.md
│   ├── break-taxonomy.md
│   ├── core-loop.md
│   ├── source-provenance.md
│   ├── fractal-task-driven.md
│   ├── stage-gates.md
│   └── project-type-adaptors.md
├── templates/
│   ├── project-review-template.md
│   ├── evidence-ledger-template.md
│   ├── react-log-template.md
│   └── opportunity-evaluation-project-template.md
├── logs/
├── projects/
└── tests/
```

## Routing

1. 判断当前目标阶段：机会评估、执行、复盘、能力沉淀。
2. 判断项目类型 adaptor：外包/客户需求、学术研究、论文研究、软件工具、通用探索。
3. 机会评估阶段优先创建“评估型 task-driven project”，Green 是接单/不接/先 PoC/改范围。
4. 执行阶段创建“执行型 task-driven project”，Green 是交付物验收。
5. 复盘阶段创建“复盘型 task-driven project”，Green 是证据地图、经验抽象和反哺候选。
6. 简单脚手架动作复用 `task-driven-project-manager`。
7. 领域方法路由到对应领域 workflow，例如 reverse、paper、argument、domain engineering。
8. 过程证据留在具体 Project/TASK，不复制进 workflow。
9. 可复用规则抽象进 references、templates 或子 skill。

详细规则读取 `references/routing.md`。

## Core Loop

```text
Frame Goal
-> Classify Stage
-> Select Adaptor
-> Scaffold
-> Execute
-> Log
-> Promote Evidence
-> Gate
-> Review Phase
-> Generalize
-> Forward Test
```

详细执行循环读取 `references/core-loop.md`。

## Required Project Artifacts

大型项目至少应有：

- `README.md`：人类入口；
- `TASK-总-*.md` 或 `PROJECT-*.md`：项目目标和总状态；
- `tasks/TASKxx-name/`：任务树；
- `logs/log.md` 或 `logs/LOG.md`：ReAct 过程；
- `outputs/*.md`：关键证据摘要；
- `final_outputs/*.md`：阶段复盘和最终交付；
- `docs/`：跨任务方法、Q&A、决策树；
- `tests/unit/e2e/uat`：可验证项目质量；
- Obsidian `[[...]]` 双链：复盘到证据。

机会评估型项目至少应有：

- `inputs/`：原始客户材料或研究想法；
- `outputs/需求澄清纪要.md`；
- `outputs/风险与可行性评估.md`；
- `outputs/追问清单.md`；
- `outputs/决策建议.md`；
- `final_outputs/是否进入执行阶段-评估报告.md`。

## Boundary

不要把具体项目的 raw data、敏感值、日志全文、数据库、课程材料复制到 workflow。本 workflow 保存可迁移结构和方法；案例证据留在 Project/TASK。

## Status

```text
status: structural-green
source: 由基金经理请回答 Android 业务网络研究项目反哺抽象
upgrade-source: 由 2026-06-22 飞源信息外包需求评估案例与用户关于“分形 task-driven”的讨论反哺
forward-test: partial
```

## References

- 路由：`references/routing.md`
- 断点分类：`references/break-taxonomy.md`
- 核心循环：`references/core-loop.md`
- 来源与迁移：`references/source-provenance.md`
- 分形哲学：`references/fractal-task-driven.md`
- 阶段 Gate：`references/stage-gates.md`
- 项目类型 Adaptor：`references/project-type-adaptors.md`
- 编排 Skill：`skills/task-driven-project-orchestrator/SKILL.md`
- 外包项目 Adaptor：`skills/outsourcing-project-adaptor/SKILL.md`
