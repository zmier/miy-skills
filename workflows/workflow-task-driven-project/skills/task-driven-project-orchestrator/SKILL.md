---
name: task-driven-project-orchestrator
description: 编排分形任务驱动型项目工程。用于判断当前目标处于机会评估、执行交付、阶段复盘或能力沉淀哪个阶段，并选择场景 adaptor、TASK 拆分、ReAct 日志、证据台账、Obsidian 双链、TDD/UAT、Gate 和最终交付策略。
---

# Task-Driven Project Orchestrator

## Workflow

1. 读取用户目标、当前项目根、已有 README/TASK/final_outputs/logs。
2. 读取 `references/fractal-task-driven.md`，确认当前目标是否应作为独立 task-driven project。
3. 读取 `references/routing.md` 判断阶段：
   - opportunity-evaluation；
   - execution-delivery；
   - phase-review；
   - capability-generalization。
4. 读取 `references/project-type-adaptors.md` 判断是否需要 adaptor。
5. 若是外包/客户需求，读取 `skills/outsourcing-project-adaptor/SKILL.md`，默认先创建机会评估型 project。
6. 读取 `references/stage-gates.md`，为当前阶段定义 Green。
7. 读取 `references/break-taxonomy.md` 判断当前断点类型。
8. 若项目未成形，调用或复用 `task-driven-project-manager` 的脚手架规则。
9. 若项目已成形，优先维护现有 TASK 树，不随意重编号。
10. 对新问题判断：
   - 属于同一主轴：创建 `subtasks/TASKxx-yy-*`；
   - 目标/产物变化：创建新顶层 TASK；
   - 已经稳定可迁移：写入 `docs/` 或 `final_outputs/`，并列入 workflow feedback。
11. 每个重要动作写入 `logs/log.md` 的 ReAct 条目。
12. 将关键 raw 结果提升为 Markdown 证据摘要，放在 `outputs/` 或 `docs/`。
13. 阶段结束时创建 `final_outputs/*复盘.md`，使用 Obsidian 双链链接 TASK、证据、日志和反哺位置。
14. 如果发现可复用方法，写明：
    - 来源项目；
    - 支持证据；
    - 应反哺的 workflow/skill；
    - 哪些内容必须留在 TASK。

## Fractal Rule

不要把 `task-driven` 理解为“如何完成一个已经决定要做的项目”。任何阶段目标都可以 task-driven 化：

```text
判断要不要做
-> 是一个 task-driven project

实际完成交付
-> 是一个 task-driven project

复盘沉淀能力
-> 也是一个 task-driven project
```

orchestrator 的第一责任是确认当前目标，而不是直接 scaffold。

## Decision Rules

### 机会评估型 Project

用于：

- 客户刚来咨询；
- 需求还在变化；
- 技术可行性或授权边界未知；
- 需要报价前判断；
- 需要先设计 PoC。

Green：

- accept；
- reject；
- poc-first；
- rescope；
- pending-client。

### 新顶层 TASK

用于：

- 目标、交付物或验收标准变化；
- 新入口、新数据源、新系统或新路线成为主线；
- 后续读者无需父任务上下文也能理解。

### 子 TASK

用于：

- 仍服务于同一主目标；
- 共用同一个数据库、请求池、状态机或语料库；
- 只是某个失败分支、工程补强、风险排查或局部实验。

### final_outputs

用于：

- 阶段复盘；
- 项目级地图；
- 对外可读报告；
- 已审阅的最终交付。

不要把 raw 中间结果直接放进 `final_outputs/`。

## ReAct Discipline

每个 live 实验、重要判断、结构调整、长跑启动/停止都要写：

```text
Thought -> Action -> Observation -> Reflection
```

Reflection 必须回答：

```text
是否改变下一步？
是否改变完成标准？
是否需要反哺 workflow/skill？
```

## Output

编排输出应包含：

- 更新过的 TASK/README/final_outputs；
- 当前阶段类型和 Green 标准；
- 使用的 adaptor；
- 当前项目状态；
- 证据链链接；
- 下一个最小动作；
- 需要人类确认的 gate；
- 可复用经验候选。
