# Standing Project Governance / TASK00

> 状态：`structural-green / forward-test-pending`
> 适用对象：已从线性执行进入多路线竞争的中大型探索项目
> 视觉语法：使用 `$roadmap`

## 核心问题

```text
当多个 TASK 都留下了有价值但强弱不同的证据时，
如何在不污染各 TASK 结果台账的前提下，
统一比较研究/产品/技术线头，并决定下一步？
```

答案是建立一个常驻治理控制面。编号型项目默认使用：

```text
tasks/TASK00-project-governance/
```

TASK00 不是“排在 TASK01 前面的普通任务”，而是跨 TASK 的 registry、portfolio、decision gate 和 review history。

## 导航

- [触发与停止条件](#触发与停止条件)
- [权威边界](#权威边界)
- [默认结构](#默认结构)
- [Artifact Contracts](#artifact-contracts)
- [Portfolio Review Procedure](#portfolio-review-procedure)
- [Roadmap And Navigation Contract](#roadmap-and-navigation-contract)
- [Numbering And History](#numbering-and-history)
- [UAT](#uat)
- [Common Failure Modes](#common-failure-modes)
- [Provenance And Transfer](#provenance-and-transfer)

## 触发与停止条件

### 创建信号

满足三个或更多信号时，优先建立 TASK00：

1. 已有多个顶层 TASK，并出现互相竞争的下一步；
2. 证据同时包含 `accepted`、`diagnostic`、`monitor`、`hold` 或 `archive`；
3. 根 README 已承担过多详细证据和决策历史；
4. 新发现很亮眼，但样本、识别、稳定性或成本风险尚未比较；
5. 下一步要回答“哪条路线更值得投入”，而不是“顺序执行哪一步”；
6. 合作者需要理解路线为什么继续、暂停或改写；
7. 新开普通 TASK 会把元决策伪装成实质交付。

### 不创建

- 小型线性项目；
- 单一父 TASK 内的普通 subtasks；
- 只需要一次周报或状态汇报；
- 尚无可比较证据，只是提前设计空治理结构；
- 纯排期问题。排期优先使用日程或 Gantt。

### 退出条件

TASK00 通常是 standing task，不以一次评审完成为结束。项目归档时冻结 registry、最后一份 review 和 decision log，不删除历史评审。

## 权威边界

| 层级 | Source of truth | 职责 |
|---|---|---|
| 项目根 README | 当前对外总览 | 精简 roadmap、当前状态、TASK00 入口 |
| TASK00 | 跨 TASK 决策 | 注册、比较、排序、状态同步、评审历史 |
| TASK01+ | 任务内证据 | 输入、方法、模型、结果、UAT、内部 roadmap |
| subtask | 单一实验/工作流闭环 | 脚本、日志、证据台账、验收 |

TASK00 可以改变某条路线的治理状态，但不能：

- 修改下级 TASK 的估计值、原始结论或验收记录；
- 把 `diagnostic` 结果写成 `accepted`；
- 为了总图整洁移动或重编号历史 TASK；
- 用评分表替代专业判断；
- 将高显著性自动等同于高优先级。

## 默认结构

```text
tasks/TASK00-project-governance/
├── README.md
├── TASK00-说明.md
├── task-registry.md
├── workstream-portfolio.md
├── decision-log.md
├── reviews/
│   ├── YYYY-MM-DD-portfolio-review.md
│   └── YYYY-MM-DD-portfolio-review.md
└── logs/
    └── log.md
```

领域适配允许改名：

```text
research-thread-portfolio.md
product-route-portfolio.md
technical-route-portfolio.md
claim-portfolio.md
```

不要改掉这些文件承担的功能。

## Artifact Contracts

### `README.md`

必须包含：

- 定位与非目标；
- Project/Portfolio Roadmap；
- Task Lineage / Navigation Map；
- 稳定入口表；
- 当前 portfolio gate；
- 状态同步规则。

Portfolio Roadmap 讲“为什么这样推进”；Lineage Map 讲“对象如何组织”。不要把两张图合成一个巨型目录图。

### `TASK00-说明.md`

必须说明：触发原因、输入、交付物、验收、长期更新条件和不拥有下级结果的边界。

### `task-registry.md`

最少字段：

```text
Task | Role | Governance Status | Stable Entry | Last Reviewed
```

治理状态是摘要。详细状态仍由下级 TASK 的 README/acceptance contract 决定。

### `workstream-portfolio.md`

最少字段：

```text
ID | Workstream | Existing Evidence | Missing Evidence | Status | Next Action
```

推荐状态：

| 状态 | 含义 |
|---|---|
| `anchor` | 已冻结的共同事实或产品约束 |
| `continue` | 当前值得继续投入 |
| `diagnostic` | 有边界/解释价值，但不能独立承担主结论 |
| `monitor` | 保留线索，暂不追加大量资源 |
| `hold` | 等待新设计、输入、理论或数据 |
| `archive` | 证据保留，但退出当前竞争集合 |

### `decision-log.md`

只记录改变路线、状态、资源顺位或解释边界的决定。每条至少包含：

```text
Decision ID / Date
Decision
Reason
Evidence
Boundary
Impact
Re-review Trigger
```

普通执行记录继续写在 TASK/log，不进入 decision log。

### `reviews/YYYY-MM-DD-portfolio-review.md`

每次评审新增文件，不覆盖旧版本。至少包含：

- 本次评审问题；
- 冻结的候选集合；
- 比较维度；
- 逐路线判断；
- 下一顺位；
- promote / hold / archive gate；
- 可审计链接。

### `logs/log.md`

记录 TASK00 自身的 ReAct：为什么触发评审、读取了什么、如何比较、哪些边界未解决。

## Portfolio Review Procedure

### 1. Freeze Candidate Set

先列出本轮参与比较的所有 workstreams。评审过程中发现的新点可以进入候选池，但不能悄悄替换比较集合。

### 2. Pull Evidence From Owners

从每个 TASK 的稳定入口提取：

- 已验收事实；
- 证据等级；
- 未解决威胁；
- 当前数据/工具/权限边界；
- 最小下一动作及停止规则。

不从聊天摘要或记忆替代证据文件。

### 3. Compare On Common Dimensions

默认维度：

| 维度 | 核心问题 |
|---|---|
| Goal value | 它对项目核心目标有多重要？ |
| Evidence maturity | 证据是单点探索，还是跨口径/冻结规格稳定？ |
| Input feasibility | 当前数据、材料、权限和工具能否执行？ |
| Information gain per cost | 下一动作能否以合理成本改变决策？ |
| Risk | 是否存在选择、泄漏、多重检验、高杠杆或合规风险？ |

可以使用 1--5 分帮助排序，但分数只是治理启发式，不是统计量，也不是自动决策器。

### 4. Assign Governance Status

为每条线写明 `continue / diagnostic / monitor / hold / archive`，并说明证据和边界。不能只写“优先级低”。

### 5. Define A Decision Gate

下一动作必须能导致明确变化，例如：

```text
pass -> promote to substantive TASK
mixed -> retain as diagnostic / appendix
fail -> archive as high-risk discovery
blocked -> hold until named input arrives
```

### 6. Sync Without Rewriting History

更新顺序：

```text
evidence-owning TASK
-> TASK00 registry/portfolio
-> dated portfolio review
-> decision log
-> compact root README snapshot
```

如果只是下级执行进度变化、没有改变项目路线，可只更新下级 TASK 与 registry，不必重写 portfolio review。

### 7. Evidence-Gated Route Promotion

当 portfolio review 或 research seminar 产生一条 `promote-now` 路线时，不要把它继续留在治理 subtask 内跑结果。先写 promotion contract，再按目标和 acceptance contract 判断开顶层 TASK 还是 subtask。

最小 promotion contract：

```text
frozen anchors / negative evidence
research question / estimand
economic object / unit
primary universe / mapping
one primary Gate / planned contrasts
pass / mixed / fail / blocked consequence
forbidden follow-up specifications
claim ceiling
independent-audit trigger
```

治理层只拥有“为什么升格”的决定；新 TASK 是数据、代码、结果和验收的 evidence owner。完整研究侧规则见：

```text
../../../workflows/workflow-research/references/evidence-gated-route-adjudication.md
```

### 8. Protocol-Conformance And Corrective History

冻结分析协议必须由实现级检查保护：

- primary sample filter 显式存在；
- primary key 唯一；
- sensitivity panels 不得堆入 primary；
- missing / invalid / observed zero 分开；
- mapping/version/hash 与文档一致；
- FE、cluster、planned contrast 和 multiple testing 与协议一致；
- tests 对协议偏离失败，而不只是检查脚本可运行。

若发现历史实现与协议不一致，使用 append-only repair：保留旧报告，新增 repair note，修复后分开重估 primary/sensitivity，在 decision log 追加纠错，并明确 Gate 是否翻转。结论未翻转不等于可以隐藏协议错误。

当 promoted result 依赖复杂聚合、跨方程 covariance、上游刚发生协议修复，或会关闭多条主路线时，parent acceptance 前应安排独立实现审计。Subagent `completed` 仍不是 parent `accepted`。

## Roadmap And Navigation Contract

使用 `$roadmap`：

1. TASK00 的 Portfolio Roadmap 只放主事实、竞争分支、当前 Gate 和下一候选；
2. TASK00 的 Lineage Map 链接所有顶层 TASK 稳定入口；
3. 每个被治理 TASK 在 README/说明顶部链接回 TASK00；
4. 未来未创建的 TASK 使用 planned 节点，不添加失效 `click`；
5. Mermaid 图下提供 Markdown fallback link table；
6. 下级 roadmap 保留执行细节，上层不复制整张子图。

## Numbering And History

- `TASK00` 预留给 standing governance，`TASK01+` 留给实质工作；
- 已运行项目后补 TASK00 时，不重编号历史任务；
- TASK00 不表示发生时间早于 TASK01，只表示控制面角色；
- 新的实质路线只有在 portfolio gate 通过后才取得下一顶层 TASK 编号；
- 被 hold/archive 的 TASK 不删除，保留稳定入口和解释边界。

## UAT

- [ ] TASK00 的职责与非目标清楚；
- [ ] 根 README 有精简入口，未复制全部 portfolio；
- [ ] registry 覆盖全部顶层 TASK；
- [ ] Portfolio Roadmap 与 Lineage Map 分开；
- [ ] 所有 Mermaid click 与 fallback links 指向存在的稳定文档；
- [ ] 每个顶层 TASK 可返回 TASK00；
- [ ] portfolio 中每条线有证据、缺口、状态和下一动作；
- [ ] decision log 只记录项目级决定；
- [ ] dated reviews 未覆盖历史版本；
- [ ] 下级证据文件未被 TASK00 移动或改写；
- [ ] 当前成熟度如实标记为 `structural-green / forward-test-pending` 或更高；
- [ ] promoted route 有独立 evidence owner、frozen promotion contract 和 protocol-conformance checks；
- [ ] 历史协议修复采用 append-only correction，未静默覆盖；
- [ ] 高风险 Gate 已独立审计或记录不审计理由；
- [ ] 至少一个未参与提炼的新项目通过后，才标记 `validated`。

## Common Failure Modes

| 失败 | 修复 |
|---|---|
| TASK00 变成所有文档的复制仓库 | 只保留摘要和稳定链接 |
| 把文件树当 roadmap | 分开 Portfolio Roadmap 与 Lineage Map |
| 每周覆盖同一份评审 | 使用带日期的 append-only reviews |
| 下级 TASK 与 TASK00 状态冲突 | 下级证据为 source of truth，TASK00 标明 review snapshot |
| 因单个显著结果立刻新开主线 | 先比较证据成熟度、高杠杆风险和信息增量 |
| Seminar 直接在治理目录继续跑实证 | 先写 promotion contract，再交给 evidence-owning TASK |
| 协议文档正确但代码混入其他样本 | 增加 primary filter、unique-key assertion 和 sensitivity separation |
| 发现历史实现偏差后覆盖旧报告 | 保留旧记录并追加 repair note / decision correction |
| 小项目也强制 TASK00 | 仅在跨 TASK 决策负担真实出现时启用 |

## Provenance And Transfer

该模式由真实探索项目中的跨 TASK 线头盘点与共同讨论提炼。个案业务结论、精确估计值和私有路径不进入本 reference；它们只保留在 `references/source-provenance.md`、dialogue note 和来源项目。

当前状态只证明结构在来源案例中自洽：

```text
structural-green
forward-test-pending
```

需要在一个未参与提炼、同样存在多路线竞争的新项目上通过 UAT，才能升级为 `validated`。
