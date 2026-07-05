---
name: workflow-research
description: 学术研究项目总父 workflow 型 Skill。用于把选题孵化、研究问题、文献定位、数据可得性、识别/实验设计、论证链、论文写作、项目任务与反哺沉淀放在同一研究项目系统中路由；组合 workflow-paper、workflow-argument-validity、scholar-kit、workflow-task-driven-project 等底层能力，但不替代它们。
status: 0.1-beta / seed / structural-draft / forward-test-required
---

# Research Workflow

状态：`0.1-beta / seed / structural-draft / forward-test-required`

> 重要提示：当前版本只适合作为研究项目诊断与路由草案，不应视为稳定可用的完整研究管理 workflow。当前 R0-R7 表述存在“线性阶段”暗示，已记录为待验证架构问题。关键构思日志见：`logs/2026-07-05-从线性阶段到探索性论证树.md`。

当前 forward-test 样本：

```text
projects/CASE-260521-基金经理研究/
```

只有在该案例完成“候选 research routes / 子论证组合模型”的真实试跑，并将有效规则反哺到 `references/`、`templates/` 和本入口后，`workflow-research` 才能从 0.1 beta 进入可稳定调用状态。

## 目标

`workflow-research` 管的是“学术项目”，不是单篇 paper，也不是单纯任务工程。

它回答：

```text
一个模糊研究 idea 如何逐步变成可论证、可取数、可识别、可写作、可投稿的研究项目？
```

## 三层关系

```text
workflow-research
  管：选题、研究问题、文献定位、数据可得性、识别设计、论证路线、项目阶段、产出组合

workflow-paper
  管：当某条研究路线收束成 paper 后，如何学习、写作、自审、返修、格式交付

workflow-task-driven-project / task-driven-project-manager
  管：执行层工程化，如何组织 TASK、代码、日志、输出、证据和复盘
```

本 workflow 的核心原则：

```text
研究问题和证据链坐在驾驶座；
TASK、Makefile、Notebook、目录结构坐在副驾驶。
```

## 为什么需要它

单个学术项目常常同时包含：

- 选题孵化与导师沟通；
- 文献地形图与研究 gap 判断；
- 数据可得性审计；
- 变量、样本、识别策略和实验设计；
- 论证链搭建与反向审计；
- 技术采集、数据工程或仿真实验；
- 一篇或多篇 paper 的写作路线；
- 失败路线、伦理边界、项目复盘和 workflow 反哺。

这些内容会调用多个底层 workflow，但任何一个底层 workflow 都不应该单独接管整个学术项目。

## 最小路由

| 用户意图 | 路由 | 当前状态 |
|---|---|---|
| 整理研究项目、判断项目阶段、重建顶层地图 | `skills/workflow-research-orchestrator` | seed |
| 拆研究问题、贡献链、机制、识别与证据 | `workflow-argument-validity` + 待建 research references | pending |
| 围绕 task / candidate route 读取文献，提取实验设计、变量、数据需求、识别、机制和写作范式 | `skills/research-literature-reader` + `scholar-pdf-markdown-restoration` | seed / forward-test |
| 学一篇或一组文献，提炼模板与 gap | `workflow-paper/subworkflows/workflow-paper-learning` | available |
| 写作、审稿、自审、返修、格式交付 | `workflow-paper` | available / partial |
| 数据可得性、采集、实验、代码任务 | `workflow-task-driven-project` / `task-driven-project-manager` | available |
| 文献检索、引用增强、参考文献治理 | `scholar-kit-*` | available |
| 学术项目目录结构、顶层清爽、执行层收束 | `references/project-structure.md` + 项目清理审计 | draft |
| 项目产生可迁移规则 | `workflow-research/logs` -> `references` / `templates` | seed |

## 研究项目主轴草案

注意：以下 R0-R7 目前只是诊断面板草案，不是线性流程。关于为何需要从“线性阶段模型”改为“探索性论证树 / 候选路线组合模型”，见：

```text
logs/2026-07-05-从线性阶段到探索性论证树.md
```

```text
R0 项目界定：这个项目到底研究什么现象、对象和场景？
R1 研究问题：有哪些候选问题？哪一个值得优先推进？
R2 文献定位：站在哪些 literature 上？gap 是真缺口还是表述缺口？
R3 数据可得性：数据源、权限、字段、粒度、覆盖、合规边界是否成立？
R4 研究设计：变量、样本、识别/实验/机制检验如何支撑问题？
R5 论证链：claim -> mechanism -> evidence -> contribution 是否闭合？
R6 paper 化：哪些路线收束成论文，哪些保留为项目资产？
R7 交付与反哺：论文、数据说明、复盘、workflow 规则分别落到哪里？
```

## 输出契约

每次调用本 workflow，至少说明：

```text
当前研究项目处在哪个阶段；
本次应调用哪些底层 workflow / skill；
预期产物是什么；
哪些材料属于项目个案证据；
哪些洞见可能反哺 workflow-research。
```

## 反哺样本

当前第一个反哺样本：

```text
projects/CASE-260521-基金经理研究/
```

该案例来自：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究
```

它用于观察一个真实学术项目如何在“选题孵化 + 数据可得性 + 技术路线 + 文献定位 + paper 化”之间来回摆动。

当前该案例还承担 `workflow-research` 的 0.1 beta forward-test：

```text
用“基金经理研究项目”试跑探索性论证树 / candidate research routes 模型；
检验 R0-R7 是否应从阶段改写为诊断面板；
形成 route card、research management、paper route selection 等可迁移模板；
完成后再决定哪些规则提升到 references/templates/SKILL.md。
```

当前正在该案例中 forward-test 的子能力：

```text
skills/research-literature-reader：研究项目文献阅读编排；
logs/2026-07-05-研究项目文献阅读子skill.md：该子 Skill 的来源、边界与迁移状态。
```

## 禁止事项

- 不把学术项目硬套成 4-8 个固定 TASK。
- 不用工程目录结构替代研究问题结构。
- 不把单篇 paper workflow 误当成整个研究项目 workflow。
- 不把个案失败路线直接提升为稳定规则。
- 不在未完成数据可得性与合规判断前承诺研究设计。
