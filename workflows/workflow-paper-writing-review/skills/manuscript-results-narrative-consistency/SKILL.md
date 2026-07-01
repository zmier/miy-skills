---
name: manuscript-results-narrative-consistency
description: 对学术手稿的结果叙事一致性做审查。用于外部审稿、投稿前自审和论文方法诊断中，在快速通读、文献定位、因果识别和变量数据审查之后，检查理论机制、模型公式、数据方法、主结果、机制、异质性、稳健性、拓展分析、结论和贡献表述是否闭环，识别结果堆叠、机制过度解释、公式与变量不一致、结论越过证据等问题。本 Skill 不生成最终审稿意见。
---

# Manuscript Results Narrative Consistency

## 定位

本 Skill 是 workflow-paper-writing-review 中的第 7 步：结果叙事一致性审查。

它负责回答一个朴素问题：

```text
作者讲的理论、写的模型、用的数据方法、报的结果和最后的结论，是不是同一条证据链？
```

它也负责做跨模块一致性检查：承接第 3-6 步已经形成的贡献链、文献定位、识别审查和变量测量判断，检查这些判断是否共同支持作者的结果叙事，是否存在重复、冲突、遗漏或过度声称。它不是重做第 4-6 步，而是把这些模块的结论放回同一条叙事链中校准。

输出应优先使用中文大白话，同时保留必要英文术语、变量名、表号、公式号和 evidence location。

## 触发条件

当用户提出以下需求时使用：

- “结果叙事一致性”
- “理论、模型、结果是否闭环”
- “结果是不是支撑机制”
- “异质性/稳健性是不是堆表”
- “结论有没有过度声称”
- “前面是不是已经讨论过这个问题”
- “为什么某个已记录 issue 没有被承接”
- “这个问题应该归到哪一步 / 是否进入审稿素材”
- “第 7 步”

## 输入

必须按顺序串读前置模块结果：

- `notes/quick-read-contribution-chain.md`
- `notes/literature-positioning-and-genealogy.md`
- `notes/causal-identification-audit.md`
- `notes/variable-data-measurement-audit.md`
- `notes/review-issue-ledger.md`

然后读取：

- 段落编号 manuscript Markdown
- 公式、主结果、机制、异质性、稳健性、拓展分析和结论相关表格

同时读取：

```text
../../references/empirical-paper-component-coverage.md
```

必要时读取：

```text
../../references/statistical-identification-table-audit.md
```

## 输出

默认输出到：

```text
notes/results-narrative-consistency-audit.md
```

建议使用模板：

```text
../../templates/results-narrative-consistency-template.md
```

同时更新：

```text
notes/review-issue-ledger.md
```

## 前置串读协议

第 7 步开始正式审查前，必须先把前面几个结果 md 串起来读，形成一份简短的 cross-module intake。这个动作是为了承接既有判断，不是重做第 3-6 步。

串读顺序和读取目的：

| 文件 | 读取目的 | 不做什么 |
|---|---|---|
| `notes/quick-read-contribution-chain.md` | 提取作者声称的核心发现、贡献链、X/Y/M、实际观测发现与作者上升发现。 | 不重新通读全文。 |
| `notes/literature-positioning-and-genealogy.md` | 提取文献定位、gap 状态、关键 benchmark、概念/变量层级边界。 | 不重新检索文献。 |
| `notes/causal-identification-audit.md` | 提取 DAG、后门/前门/IV/PSM/FE、实际识别强度和因果边界。 | 不重新审计所有识别表。 |
| `notes/variable-data-measurement-audit.md` | 提取 X/Y/数据/样本/量纲/操作化边界。 | 不重新做变量数据审查。 |
| `notes/review-issue-ledger.md` | 提取 issue id、severity、status、route 和 next action。 | 不机械复制全部 issue。 |

串读后先生成或更新以下内部工作表，再进入理论、模型、结果和结论审查：

| Intake Item | From | Boundary / Finding | Issue ID | TASK07 Use |
|---|---|---|---|---|

`TASK07 Use` 只能写以下几类：

- `check narrative uptake`：检查作者叙事是否承接该边界；
- `check overclaim`：检查是否从窄发现上升为宽结论；
- `check conflict`：检查模块之间是否冲突；
- `route to TASK08`：需要后续组装为审稿素材；
- `background only`：只作为背景，不进入 TASK07 主审查。

## Issue Lineage Check

第 7 步遇到一个跨模块问题时，必须先追踪 issue lineage，而不是把它当成新发现。尤其当问题涉及“作者声称的结论是否越过前面文献、变量或识别模块已经发现的边界”时，执行以下检查：

1. 在 `notes/review-issue-ledger.md` 中查找相关 issue id、route、status 和 severity。
2. 回到该 issue 的发现源模块读取最小必要上下文：
   - 文献/概念层级问题：第 4 步产物；
   - 识别/因果问题：第 5 步产物；
   - 变量/数据/操作化问题：第 6 步产物。
3. 检查当前结果叙事是否已经承接该 issue：
   - 作者是否在结果解释、拓展分析、结论或政策含义中越过该 issue 的边界；
   - 当前 `notes/results-narrative-consistency-audit.md` 是否已经记录该承接；
   - 若没有记录，补入“从哪个 issue 来、如何影响叙事、是否需路由到第 8 步”。
4. 不新建重复 issue；若只是把已有 issue 放进结果叙事链，更新原 issue 的 route/status/addendum。
5. 若需要进入最终审稿素材，标记为 `route: review-material-assembly`，交给第 8 步合并和排序。

示例：`Y 的宏观-微观 mismatch` 不应在第 7 步重新发现。它的发现源通常是第 4 步文献定位和第 6 步变量测量，issue id 可能是 `VAR-001` / `LIT-001`；第 7 步只检查作者是否把 narrow EPS relation 叙述成 broad export upgrading claim，以及这个承接是否已经进入结果叙事和第 8 步素材。

## 分析顺序

### 1. 前置模块串读与 intake summary

先执行“前置串读协议”，输出 cross-module intake summary。没有完成 intake summary 时，不进入后面的叙事一致性判断。

重点提取：

- 作者声称的发现与实际观测发现；
- 文献 gap 和 benchmark 边界；
- 识别强度与因果边界；
- 核心 X/Y 操作化边界；
- 已有 major-candidate issue 及其 route。

### 2. 作者目录体系覆盖检查

先用 `../../references/empirical-paper-component-coverage.md` 建立 coverage matrix，确认作者的：

- research question / contribution；
- theory / mechanism；
- mathematical or empirical model；
- data and method；
- baseline results；
- mechanism results；
- heterogeneity / extensions；
- robustness；
- conclusion / implications；

分别已经被哪个 workflow 步骤审查，哪里还没有被吃掉。

同时进行跨模块结论对齐：

- 同一问题是否在多个模块中重复出现；
- 不同模块对同一 issue 的严重程度是否一致；
- 是否有某个模块的结论没有被结果叙事承接；
- 是否需要把 issue 路由到第 8 步合并成 major/minor material。

对每个关键 issue，优先生成 lineage row：

| Issue ID | Source Module | Current Narrative Link | Missing / Overclaim | Route to TASK08 |
|---|---|---|---|---|

### 3. 理论机制到假设

检查：

- 理论机制是否清楚说明 X 为什么影响 Y；
- 假设是否从理论机制自然推出；
- 机制变量是否真的对应理论中的机制；
- 是否出现概念跳跃、多个机制混在一起、或机制与贡献无关。

### 4. 模型公式到变量

检查：

- 公式中的 X、Y、controls、FE、error term 是否与变量定义和表格一致；
- 下标、时间、样本单位是否清楚；
- 控制变量是否可能是机制变量或后处理变量；
- 公式实际估计的 estimand 是否与作者叙事一致。

### 5. 主结果到核心发现

检查：

- 主结果是否直接对应核心发现句；
- 系数方向、显著性、经济意义和量纲是否可解释；
- OLS/FE/IV/PSM 等不同结果是否讲同一件事；
- 作者是否把 narrow observed relation 上升为 broad theoretical claim。

### 6. 机制、异质性、稳健性和拓展

检查：

- 机制结果是否只是 `X -> M`，还是同时支撑 `M -> Y`；
- 异质性是否有理论预期，是否直接检验组间差异；
- 稳健性是否对应真实威胁，还是堆表；
- 拓展分析是否服务主贡献，还是扩大结论边界。

### 7. 结论和贡献表述

检查：

- 结论是否回到实际观测发现；
- 是否承认变量、识别和样本边界；
- 政策或理论含义是否越过证据；
- 是否需要 downgrade / reframe。

### 8. 审稿出口

最后输出：

- narrative consistency strength：strong / moderate / weak / fragmented；
- theory-model-data-result alignment；
- overclaim points；
- concrete author requests；
- issue ledger updates。

## 输出结构

~~~markdown
# Results Narrative Consistency Audit

## Plain-Language Bottom Line

## Cross-Module Intake Summary

| Intake Item | From | Boundary / Finding | Issue ID | TASK07 Use |
|---|---|---|---|---|

## Empirical Paper Component Coverage

| Author-Facing Component | Workflow Coverage | Current Status | Gap / Concern |
|---|---|---|---|

## Cross-Module Issue Lineage

| Issue ID | Source Module | Current Narrative Link | Missing / Overclaim | Route to TASK08 |
|---|---|---|---|---|

## Theory Mechanism to Hypotheses

## Model Formula to Variables

## Main Results to Core Finding

## Mechanism, Heterogeneity, Robustness, and Extensions

## Conclusion and Contribution Boundaries

## Narrative Consistency Strength

## Concrete Author Requests

## Issue Ledger Updates
~~~

## 判断纪律

- 不把显著结果自动当成叙事闭环。
- 不把机制表自动当成机制证明。
- 不把稳健性数量当成稳健性质量。
- 不重复第 5 步和第 6 步的全部细节，只承接它们的结论，检查作者叙事是否越界。
- 不生成最终审稿意见，只生成可核验的审稿素材。
