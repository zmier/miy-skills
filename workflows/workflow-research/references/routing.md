---
type: reference
status: draft
---

# Research Workflow Routing

## 核心路由问题

先问：

```text
用户现在要推进的是学术项目本身，还是项目内的某个子动作？
```

## 路由表

| 当前对象 | 优先路由 | 说明 |
|---|---|---|
| 模糊 idea / 选题孵化 | `workflow-research` | 先定研究现象、对象、可行性 |
| 已收束成一篇论文 | `workflow-paper` | 进入 paper 写作、学习、自审或返修 |
| 论证链、机制、gap、贡献 | `workflow-argument-validity` | 作为底层论证引擎 |
| 文献检索与引用治理 | `scholar-kit-*` | 作为文献工具层 |
| 数据采集、清洗、实验、脚本 | `workflow-task-driven-project` / `task-driven-project-manager` | 作为工程执行层 |
| 文献启发的数据需求、外部数据库补数、研究侧/数据侧协作 | `references/literature-data-design-handshake.md` + `miy-mail` + task-driven 执行层 | R2/R3/R4 交界处的握手机制：request -> delivery -> review -> scope-lock -> acceptance |
| 项目目录清理 | `workflow-research` + task-driven 执行规则 | 先保护研究主轴，再整理证据与产物 |
| 可迁移方法沉淀 | `workflow-tao` + `workflow-research/logs` | 先写构思日志，再提升稳定规则 |

## 当前待验证

- 学术项目阶段是否应固定为 R0-R7；
- “paper 化”应作为阶段，还是作为从研究项目分叉出去的路线；
- 数据可得性审计是否需要独立 subworkflow；
- 文献-数据-设计握手机制是否应在第二个案例后升级为正式子 Skill；
- 项目反哺 workflow 的最小模板需要多重。
