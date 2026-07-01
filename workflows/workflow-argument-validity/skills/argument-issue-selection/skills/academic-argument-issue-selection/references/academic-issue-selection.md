---
date: 2026-06-20
type: reference
status: seed
scope:
  - academic-argument-issue-selection
---

# Academic Issue Selection

## 核心判断

学术审稿不是把所有 weak arrows 都写进审稿意见，而是选择最影响贡献成立、最需要作者回应、最能形成可执行修改建议的问题。

选择时先问：

```text
这条断点削弱的是 X1、X2 还是 Y？
如果作者不回应，论文核心贡献是否仍成立？
它是否可以通过补证据、补模型、补解释或降调来修复？
它位于论证树第几层？
如果它是低层证据，它是否真的卡住了上层 claim？
```

## Claim Level 与 Bottleneck

选点要先看层级：

```text
claim_level:
  root
  major-claim
  middle-claim
  subclaim
  evidence-leaf

bottleneck_status:
  root-blocking
  major-claim-blocking
  local-support
  cosmetic
  irrelevant
```

一般规则：

- `root` / `major-claim` 断点默认重要；
- `middle-claim` 若支撑 X2/Y，通常可进入 major-candidate；
- `subclaim` 是否重要取决于它是不是上层 claim 的必要支撑；
- `evidence-leaf` 默认不是 major，除非它是上层 claim 的瓶颈证据；
- `cosmetic` / `irrelevant` 细节不应进入审稿意见，或只进入极低优先级 note。

低层细节是否值得写，必须问：

```text
这个细节支撑哪个 parent claim？
如果没有它，parent claim 是否还成立？
它是必要证据、关键反证，还是只是让报告更完整？
作者读到时能否理解它为什么不是无关细节？
```

例子：

```text
zeta / EIS / EDS 本身不是 major。
但如果作者声称 EDL / ion pump / charge collection 机制已被证明，
这些实验可能是 mechanism claim 的瓶颈证据，
因此可以进入 major 的 evidence package。
```

反例：

```text
供应商、厂家、产地、型号等信息若不影响机制、性能、识别、可复现性或安全边界，
通常是 cosmetic / irrelevant。
不要把“电饭锅厂家在哪生产”式细节写成 major。
```

## Major Concern 候选

优先选为 major concern：

- 直接削弱 `X2` 的关键链条；
- 直接削弱 `Y`，即结果不能回应 gap 或贡献上升过度；
- 识别策略不足以支撑因果语言；
- 核心构念和操作化指标错配；
- 样本规则削弱作者声称的机制；
- 结果、机制、稳健性不能闭环；
- 多个中等断点共同指向同一核心链条失败；
- 低层 evidence-leaf 虽然细，但它阻断了上层核心 claim。

经管 / 社科实证论文中，以下低层问题若阻断 parent claim，可作为 major-candidate，而不是自动归为细节：

- 构念与代理变量不匹配，导致核心 X 或 Y 的含义不清；
- 样本范围无法支持作者的机制、外推或目标总体；
- 控制变量角色不清，可能构成 bad control 或机制吸收；
- 标准误、聚类层级或检验统计影响核心显著性判断；
- 机制检验只能说明相关通道，无法支撑机制声称；
- 构造变量的方向、量纲、分布或描述统计不可解释。

中文经管 / 中文社科论文中，指标方向、文本口径、中文文献谱系、本土制度语境、政策化表达和报告规范问题，需要先判断它们是否卡住 parent claim。若只是写作或格式问题，通常是 minor / revision action；若导致核心变量、结果或贡献不可判断，则可升级为 major-candidate。

major 排序时同时看：

```text
impact_on_X1_X2_Y x repair_cost
```

- 高影响、高修复成本：优先作为 major concern；
- 高影响、低修复成本：可作为 framing major、major 中的低成本修复项，或放在 major 开头建立审稿语境；
- 中低影响、低修复成本：通常作为 minor concern / revision action；
- 中低影响、高修复成本：通常暂缓，除非它阻断核心结论。

## Minor Concern 或 Revision Action

更适合放入 minor concern / revision action：

- 变量量纲、表格说明、术语解释不清；
- 某个稳健性或附表需要补充但不改变主链条；
- 文献引用、机制措辞或贡献表述需要降调；
- evidence location 或 table value 需要 QC；
- 低层细节能增强透明度或可复现性，但不是上层 claim 的瓶颈。

## Evidence Guardrail

选点时要区分“已经足以成问题的箭头”和“还需要核验的箭头”：

```text
primary_confirmed_arrows
linked_hold_arrows
evidence_guardrail
```

- `primary_confirmed_arrows`：已经可以支持该 issue 的主要箭头；
- `linked_hold_arrows`：与该 issue 相关，但仍需图表、补充材料、source data、全文或外部资料核验；
- `evidence_guardrail`：明确哪些判断已经可写，哪些只能写成条件性要求。

`needs-qc`、`needs-source-figure-qc`、`needs-supplement-qc`、`needs-fulltext-pattern-check`、`needs-human-pdf` 不得直接作为 confirmed major 的证据基础。它们可以进入：

```text
hold-for-qc
evidence-needed
search-before-major
linked_hold_arrows
```

如果一个问题同时包含 confirmed arrows 与 hold arrows，可以选为 mixed issue，但必须写清：

```text
confirmed concern = 由 primary_confirmed_arrows 支撑
conditional extension = linked_hold_arrows 需后续 QC
```

## Review Issue Arrow Map

每条 issue 必须写成：

```text
review issue
-> target arrow
-> claim level / bottleneck status
-> primary confirmed arrows / linked hold arrows
-> weakened node
-> impact on X1/X2/Y
-> parent claim and why this detail matters
-> evidence guardrail
-> possible revision
```

不要写成：

```text
变量问题
方法问题
机制问题
```

除非同时说明它们削弱哪条 `A -> B` 箭头。

## 合并规则

- 多个 measurement mismatch 同时削弱同一个 Y，可合并；
- 多个 robustness 问题若只是重复说明同一威胁未回应，应合并；
- 理论前提、样本筛选和机制检验若共同削弱同一机制链，可组合成一个 major concern；
- 但不要把不同层级的问题硬合并，导致作者无法执行修改；
- 合并低层 evidence-leaf 时，必须写清它们共同卡住的 parent claim；否则作者会读成细节清单。

## Hold 与 Discard

重要但未核的问题不要丢掉：

- manuscript-specific 图、表、补充材料、source data 未核时，进入 `hold-for-qc`；
- 外部全文或方法标准未读时，进入 `search-before-major` 或 `needs-fulltext-pattern-check`；
- 已被更高层 issue 覆盖的问题，进入 `discarded-but-noted` 并说明 folded / merged / lower-priority / hold reason；
- 未入选不等于问题不存在，只表示当前不适合作为独立审稿点。
