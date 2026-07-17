# Evidence-Gated Research Route Adjudication

> 状态：`structural-green / forward-test-pending`  
> 语义所有者：`workflow-research`  
> 适用对象：已经形成稳定经验事实、多个竞争解释和跨 TASK 证据的探索性研究项目

## 一句话

当研究已经有很多“讲得通”的故事时，不继续堆规格，而是先冻结共同事实和负证据，通过 seminar 选出一项信息增量最高的区分性 Gate；Gate 升格为独立实证任务，经过协议一致性检查和必要的独立审计后，再回写 route portfolio、claim boundary 与下一数据对象。

## 职责分层

| 层 | 负责什么 | 不负责什么 |
|---|---|---|
| `workflow-research` | route lifecycle、状态、证据门和研究对象变化 | 具体目录脚手架和单次回归实现 |
| `research-brainstorm` | 候选池、交叉批评、Chair 仲裁和 promotion contract | 把候选机制直接写成结果 |
| `task-driven-project-manager` | 升格 TASK、冻结协议、UAT、日志、证据台账、独立验收 | 决定学术路线本身是否值得研究 |
| `research-roadmap` | 把仲裁、升格、Gate、审计、收敛和下一数据请求画清楚 | 用图替代结果报告和识别说明 |
| TASK00 / portfolio governance | 比较路线、记录 append-only 决策、同步全局状态 | 改写 evidence-owning TASK 的历史结果 |

## 触发条件

满足以下多数信号时启用：

- 已有至少一个冻结 anchor 或稳定经验事实；
- 多条机制、DGP、异质性或测量路线竞争；
- 继续增加 interaction、文本标签或窗口的边际信息下降；
- 下一步应回答“哪项证据能改变路线排序”，而不是“还能跑什么”；
- 路线推进可能改变研究对象、数据请求或 claim boundary；
- 需要多个学术角色进行交叉批评，而不是独立并行写报告。

不要用于只有一个自然下一步的小型线性任务。

## Route Lifecycle

```text
F0 冻结 anchors 与 negative evidence
-> F1 outcome-aware seminar brief，但禁止读取未冻结的新候选结果
-> F2 多角色独立发散与共享候选池
-> F3 交叉批评、回应和重复路线合并
-> F4 Chair 按 information gain 仲裁
-> F5 promotion contract：唯一问题、数据、falsifier、停止规则
-> F6 升格 substantive TASK，先冻结协议再读取新 outcome
-> F7 protocol-conformance + implementation audit
-> F8 evidence owner 验收，再同步 portfolio / roadmap / next data object
```

## 路线状态

Chair 必须给每条稳定 ID 一个明确去向：

| 状态 | 含义 | 后续 |
|---|---|---|
| `promote-now` | 当前数据可执行，且一项结果能重排至少两条 DGP | 升格 TASK / subtask |
| `queue-data` | 命题有区分性，但关键对象、字段或频率尚不可得 | 进入 Data Gate，不运行 outcome |
| `theory-boundary` | 行为机制重要，但当前数据无法观察必要角色或路径 | 保留为解释边界，不制造 proxy |
| `diagnostic-only` | 能定位样本、尺度或统计构成，不能独立解释 why | 作为 anchor、robustness 或 appendix |
| `merge` | 与更上位路线共享同一 Gate | 合并 stable ID，保留来源 |
| `archive` | 重复、不可证伪、信息增量低或已被负证据关闭 | 保留原因，停止扩张 |

默认只允许 1 条 `promote-now`。只有 write scope、数据对象和 acceptance contract 真正独立时，才并行升格 2--3 条。

## High-Information Gate

一项 Gate 值得升格，至少满足：

1. 结果为正、负或混合时，都能改变路线排序；
2. 能区分至少两个竞争 DGP，而不只是再次确认主效应；
3. 构念、经济对象、样本、主 contrast 和 stop rule 可在读新 outcome 前冻结；
4. 数据可得性和 mapping 已通过 outcome-blind 预审；
5. 失败不会通过放宽标签、改窗口或追加交互被事后“修好”；
6. 结论层级明确：定位结果、解释机制和识别因果不能混为一谈。

## Promotion Contract

从 seminar 升格到 TASK 前写清：

```text
Research question / estimand
Frozen anchors and negative evidence
Competing DGPs
Economic object and unit of analysis
Primary data universe and mapping
One primary Gate and planned contrasts
Pass / mixed / fail / blocked consequences
Forbidden follow-up specifications
Claim ceiling
Independent audit trigger
Portfolio and roadmap sync owner
```

如果目标、产物和 acceptance contract 已经独立变化，开新的顶层 TASK；如果只是同一父目标下的一个实验或审计，开 subtask。seminar 本身不拥有升格后的实证结果。

## Protocol-Conformance Gate

冻结文档不等于实现合规。读取新结果前后都要核对：

- 代码是否显式筛选 frozen primary sample；
- 主键是否唯一，是否把 sensitivity panels 堆进 primary；
- missing、invalid 与 observed zero 是否区分；
- mapping snapshot、版本、hash 和有效期是否冻结；
- primary 与 sensitivity 是否分别估计；
- planned contrast、cluster、FE 和 multiple-testing 规则是否一致；
- 代码是否为迭代、收敛和异常样本设置显式失败；
- tests 是否断言协议，而不只断言脚本能运行。

若发现历史实现错误：

```text
保留旧记录
-> 写 protocol repair note
-> 修复主实现
-> 分开重估 primary / sensitivity
-> 追加 decision-log correction
-> 判断 Gate 是否翻转
```

不要静默覆盖旧台账，也不要因结论未翻转就省略协议错误。

## Independent Audit Trigger

满足任一情况时，父任务接受前应安排独立实现或强审计：

- 新 estimand 依赖复杂聚合恒等式或跨方程 covariance；
- 结果将关闭多条主要机制路线；
- 上游刚发生协议修复；
- 样本 transport、mapping、FE absorption 或 cluster convention 容易改变推断；
- 单一脚本同时构造数据、估计模型和生成结论。

独立审计应尽量换一条计算路线，并把 `completed` 与 `accepted` 分开。

## Claim Ladder

每次 Gate 后明确停在哪一层：

```text
L0 pattern：观察到什么形状？
L1 location：该形状在哪个经济层级已经出现？
L2 mechanism compatibility：哪些机制被削弱、仍相容或需要新数据？
L3 causal identification：是否有外生变化和可辩护反事实？
```

`L1 location` 显著不等于 `L2 why` 已解决；`L2 compatible` 也不等于 `L3 causal`。

## Sync Order

```text
evidence-owning TASK README / report / acceptance / log
-> independent audit and parent acceptance
-> TASK00 portfolio / dated review / decision log
-> project and task Research Roadmap
-> hypothesis incubator / next data object
-> external request artifact, if needed
```

新证据可能改变的不只是结论，还包括下一步的经济对象。例如聚合层级 Gate 可能要求后续舆情、文本或制度数据匹配到更细的 fund/product object，而不是继续使用粗粒度代理。

## 最小产物

- seminar brief；
- stable-ID possibility pool；
- cross-critique 与 response；
- Chair final adjudication；
- promotion contract / next Gate；
- substantive TASK frozen protocol；
- protocol-conformance report；
- parent acceptance 与必要的 independent audit；
- portfolio/roadmap sync 和 claim boundary。

需要可复制结构时，使用 `../templates/research-route-gate-review-template.md`。

## Common Failures

| 失败 | 修复 |
|---|---|
| 哪个显著就讲哪个故事 | 先冻结候选、方向与多重检验；优先 information gain |
| Brainstorm 只产出长清单 | Chair 必须给每条 ID 明确状态和唯一 next Gate |
| Data 不足却制造 proxy | 标为 `theory-boundary` 或 `queue-data` |
| 定位结果发生层级就声称解释 why | 使用 Claim Ladder 分层 |
| 协议写对但代码混样本 | 增加 primary filter、unique-key assertion 和 sensitivity separation |
| Subagent 完成即父任务验收 | 父级检查 UAT、证据、输出、边界和 integration fit |
| 新结果只更新局部报告 | 按 Sync Order 回写 portfolio、roadmap 和下一数据对象 |
| 一次来源案例就创建新 Skill | 先 reference-integrated，经过新案例 forward-test 再决定抽 Skill |

## UAT

- [ ] anchors、negative evidence 与禁止声称已冻结；
- [ ] 候选机制、识别威胁、测量问题和异质性已分开；
- [ ] 每条 stable ID 有最终去向；
- [ ] `promote-now` 有唯一 high-information Gate 和 stop rule；
- [ ] 新 outcome 在协议冻结后才读取；
- [ ] protocol-conformance tests 覆盖 primary sample 与 key uniqueness；
- [ ] 高风险结果完成独立审计或写明不做理由；
- [ ] evidence owner 先验收，治理层后同步；
- [ ] roadmap 区分 pattern、location、mechanism compatibility 与 causality；
- [ ] 来源案例与通用规则分开；
- [ ] 当前迁移状态没有超过真实 forward-test 证据。

