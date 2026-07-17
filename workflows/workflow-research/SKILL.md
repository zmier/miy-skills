---
name: workflow-research
description: 学术研究项目总父 workflow 型 Skill。用于把选题孵化、研究问题、文献定位、数据可得性、识别/实验设计、论证链、论文写作、项目任务与反哺沉淀放在同一研究项目系统中路由；组合 workflow-paper、workflow-argument-validity、scholar-kit、workflow-task-driven-project 等底层能力，但不替代它们。
metadata:
  status: 0.1-beta / seed / structural-draft / forward-test-required
  topology: graph-like / hybrid graph-of-trees
---

# Research Workflow

状态：`0.1-beta / seed / structural-draft / forward-test-required`

拓扑：`graph-like / hybrid graph-of-trees`

> 重要提示：当前版本只适合作为研究项目诊断与路由草案，不应视为稳定可用的完整研究管理 workflow。当前父入口的暂定主模型是 `route portfolio / 探索性论证树`；R0-R7 仅作为诊断面板，不是线性阶段。关键构思日志见：`logs/2026-07-05-从线性阶段到探索性论证树.md`、`logs/2026-07-08-Node-Task双层结构.md`；拓扑来源见 `../workflow-tao/logs/2026-07-05-workflow拓扑-树形与图型.md`。

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

## 拓扑定位

`workflow-research` 默认不是 tree-like workflow，而是 graph-like / hybrid graph-of-trees workflow。

这意味着：

```text
项目有总体方向，但 paper 主干未必一开始就知道；
多个 candidate routes / candidate claims 会并行生长；
route 之间会互相影响、竞争、合并、降级、拆分或转为另一篇 paper；
每条 route 内部可以调用 tree-like 子 workflow，例如文献读取、数据清洗、实验执行或写作交付；
最终 paper 化通常是后验地重组 route portfolio，而不是顺序阶段的自然终点。
```

因此，本 workflow 的顶层基本单位不是固定 TASK，也不是 R0-R7 阶段，而是：

```text
research route / candidate claim / 子论证
```

执行层 TASK 只服务 route portfolio，不定义研究项目本身。

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
| 将初始发现、核心谜题、后续机制 / 样本 / 识别分支和文档入口组织成可点击路线图 | `skills/research-roadmap` | seed / forward-test-with-CASE-260521 |
| 对初始事实、核心谜题、候选机制、替代解释或 route 选择困境进行 seminar-style 多视角脑暴 | `skills/research-brainstorm` | seed / extracted-from-CASE-260521 |
| 将阶段进展写成知乎式同行稿，并用陌生同行视角审计隐含前提、过期结论、术语依赖和 claim 越级 | `skills/research-zhihu-post` | structural-green / source-case-tested / independent-forward-test-pending |
| 多条路线竞争后，冻结一项 high-information Gate，升格实证 TASK，并完成协议审计和 portfolio 回写 | `references/evidence-gated-route-adjudication.md` + `research-brainstorm` + `task-driven-project-manager` | structural-green / forward-test-pending |
| 拆研究问题、贡献链、机制、识别与证据 | `workflow-argument-validity` + 待建 research references | pending |
| 围绕 task / candidate route 读取文献，提取实验设计、变量、数据需求、识别、机制和写作范式 | `skills/research-literature-reader` + `scholar-pdf-markdown-restoration` | seed / forward-test |
| 学一篇或一组文献，提炼模板与 gap | `workflow-paper/subworkflows/workflow-paper-learning` | available |
| 写作、审稿、自审、返修、格式交付 | `workflow-paper` | available / partial |
| 数据可得性、采集、实验、代码任务 | `workflow-task-driven-project` / `task-driven-project-manager` | available |
| 文献检索、引用增强、参考文献治理 | `scholar-kit-*` | available |
| 文献启发的数据需求、外部数据库补数、研究侧/数据侧 scope-lock | `references/literature-data-design-handshake.md` + `miy-mail` + task-driven 执行层 | structural-green / forward-test-pending |
| 学术项目目录结构、顶层清爽、执行层收束 | `references/project-structure.md` + 项目清理审计 | draft |
| 项目产生可迁移规则 | `workflow-research/logs` -> `references` / `templates` | seed |

## Route Portfolio Model

当前暂定主模型：

```text
Research Project
→ Candidate Claims / Research Routes
→ 每条 route 内部维护：
   question / literature / data / design / evidence / threat / contribution
→ route 之间竞争、合并、降级、拆分
→ paper 化时重组为主干、机制、稳健性、附录、弃用路线或另一篇 paper
```

每条 route 至少应能回答：

```text
它想证明什么 claim？
它需要哪些文献来定位 gap 和机制？
它已有哪块数据，仍缺哪些数据？
它可能的变量、样本、窗口和识别设计是什么？
它的主要证据和替代解释是什么？
它可能成为 paper 主干、机制、稳健性、附录，还是应降级 / 放弃？
```

## Evidence-Gated Route Lifecycle

当 route portfolio 已有稳定经验事实、负证据和多个竞争解释时，默认使用：

```text
anchors / negative evidence
-> research seminar
-> Chair adjudication
-> promote-now / queue-data / theory-boundary / archive
-> substantive TASK with frozen protocol
-> protocol-conformance and independent audit when required
-> evidence-owner acceptance
-> portfolio / roadmap / next-data-object sync
```

完整协议见 [`references/evidence-gated-route-adjudication.md`](references/evidence-gated-route-adjudication.md)，模板见 [`research-route-gate-review-template.md`](templates/research-route-gate-review-template.md)。

这里必须区分四层结论：

```text
pattern -> location -> mechanism compatibility -> causality
```

定位某个结果在哪个经济层级已出现，不等于解释为什么出现；机制相容性也不等于因果识别。新证据除了更新 claim，还可能更新下一步应匹配的数据对象、粒度或 external Data Gate。

在重大 phase boundary、核心解释修正、coauthor / seminar 沟通前，或项目成员已难以用陌生读者语言复述主线时，调用 `research-zhihu-post`。它不代替 route adjudication，而是在 Gate 前后执行 outside-view checkpoint：重建当前 anchor、负证据、被修正 claim 和 unresolved question；把暴露出的新困惑回写 route portfolio、`research-brainstorm` 与 `research-roadmap`。

## Node / Task 管理约定

对于 graph-like / hybrid graph-of-trees 的研究项目，应区分研究图层和执行层：

```text
nodes/ = 研究图层，管理长期存在的 research routes / candidate claims / designs
tasks/ = 执行层，管理一段时间内线性推进的具体工作
```

核心规则：

```text
Task 可以线性推进；
Task 的研究贡献不一定线性；
同一个 Task 可以同时更新多个 Node；
同一个 Node 可以被多个 Task 反复补充、修正、合并或降级。
```

因此，不能把 `tasks/` 当成研究主轴。`tasks/` 记录“为了什么目标做了什么”，`nodes/` 承接“这些工作怎样改变了研究图”。

每个 Node 至少应有一个 node card，用于记录：

```text
当前状态；
当前 claim / route 直觉；
已经明确的信息；
候选但未确认的信息；
未明确信息；
关联 tasks；
关联文献；
数据需求；
候选设计；
证据与识别威胁；
下一步问题。
```

每个 Task 至少应说明：

```text
本 task 的目标和输入；
本 task 影响了哪些 nodes；
分别更新了每个 node 的哪一类信息：claim / literature / data / design / evidence / threat / contribution；
哪些判断只是 task 内部观察，哪些应回挂到 node；
哪些洞见可能进一步反哺 workflow。
```

## R0-R7 诊断面板草案

注意：以下 R0-R7 是诊断面板 / 工作面，不是线性流程，也不是项目阶段。它们可以用于整个项目，也可以用于单条 route。关于为何需要从“线性阶段模型”改为“探索性论证树 / 候选路线组合模型”，见：

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
当前项目 / route portfolio 的状态，而不是线性阶段；
当前活跃或待判断的 candidate routes / candidate claims；
本次需要诊断哪些 panel：question / literature / data / design / evidence / threat / contribution / paperization；
本次应调用哪些底层 workflow / skill；
预期产物是什么；
本次 task / action 影响了哪些 nodes；
每个 node 被更新的是 claim、literature、data、design、evidence、threat 还是 contribution；
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

当前 forward-test 不应把“材料整理 -> 实验设计 -> 数据审计 -> 路线选择”误读成线性流程。更准确的观察对象是：

```text
材料如何生成 / 修正 route portfolio；
文献如何改变 route 的 claim、proxy、design 和 threat；
数据字段如何暴露 route 的可行性和缺口；
实验设计如何让 route 竞争、合并、降级或 paper 化。
```

2026-07-09 新增 field-discovery：

```text
强参考文献 + 核心数据之后，若需要外部数据库补数，应启动 literature-data-design handshake：
研究侧 data request -> 数据侧 inventory/dictionary/QC -> 研究侧 scope-lock -> 数据侧 processed panel -> 研究侧 acceptance -> research design v1。
该规则当前为 structural-green / forward-test-pending，不应写成已验证通用子 Skill。
```

该案例当前采用的项目载体约定是：

```text
nodes/：管理 RTE01-RTE05 等候选研究路线；
tasks/：管理 TASK01、后续文献阅读、数据审计、实验设计等线性工作包；
task 产物通过 node card 回挂到一个或多个 route nodes。
```

当前正在该案例中 forward-test 的子能力：

```text
skills/research-literature-reader：研究项目文献阅读编排；
skills/research-roadmap：将任务谱系、结果台账和 route portfolio 重组为可点击 Research Roadmap；
skills/research-brainstorm：将“发现 -> 谜题 -> 多机制脑暴 -> 交叉批评 -> route gate”组织成 seminar-style 多视角研究讨论；
references/evidence-gated-route-adjudication.md：将 route gate 延伸到 substantive TASK、协议一致性、独立审计和 portfolio/roadmap 回写；
logs/2026-07-05-研究项目文献阅读子skill.md：该子 Skill 的来源、边界与迁移状态。
```

## 禁止事项

- 不把学术项目硬套成 4-8 个固定 TASK。
- 不用工程目录结构替代研究问题结构。
- 不把 `tasks/` 当成 `nodes/`；执行任务不是研究图本身。
- 不把单篇 paper workflow 误当成整个研究项目 workflow。
- 不把个案失败路线直接提升为稳定规则。
- 不在未完成数据可得性与合规判断前承诺研究设计。
- 不把 R0-R7 当作顺序关卡；它们只是诊断面板。
- 不在 route portfolio 尚未竞争前过早固定 paper 主干。
