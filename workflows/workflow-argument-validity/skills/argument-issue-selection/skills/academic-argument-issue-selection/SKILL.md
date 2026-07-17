---
name: academic-argument-issue-selection
description: 学术论文审稿和写作自审的问题选择 Skill。用于在 academic-argument-arrow-audit 已经全量审计作者论证树、academic-arrow-repair-mapping 已给出补证据/补实验/补分析/降调路线之后，从 weak、broken、unclear、needs-qc 或 needs-external-evidence 箭头中选择 major concern、minor concern、revision action 或 evidence-needed issue，生成 review-issue-arrow-map 和 major-concern-candidates；对尚未完成外部证据增强的箭头不得写成已确认 major concern。
---

# Academic Argument Issue Selection

## 定位

这是学术论文场景的“选问题”子 Skill。它不重新抽作者树，也不重新全量验箭头，而是消费：

```text
academic-arrow-audit-table.md
paper-argument-tree.md
evidence-ledger.md
```

并输出：

```text
full-issue-candidate-pool.md
human-readable-issue-candidates.md
review-issue-arrow-map.md
major-concern-candidates.md
revision-action-map.md
```

重要：本 Skill 不应让 subAgent 直接替审稿人完成最终取舍。默认先生成全量候选池，把所有可写断点摊开；然后再生成建议选点方案。最终哪些问题进入 author-facing comments，由用户 / 主 Agent / 审稿人决定。

## 输入

- `academic-arrow-audit-table.md`；
- `arrow-repair-map.md`；
- `paper-argument-tree.md`；
- `evidence-ledger.md`；
- `X1/X2/Y` 顶层结构；
- `empirical-review-sensitivity-map.md`、`empirical-arrow-candidate-ledger.md`（经管/社科实证论文，如有）；
- `chinese-reviewer-sensitive-candidates.md`、`local-expression-and-format-qc.md`（中文经管/中文社科语境，如有）；
- 审稿任务边界或写作自审目标；
- 已有 review issue ledger 或前序 TASK 输出。

## 选问题规则

详见 `references/academic-issue-selection.md`。

优先选择：

- 影响 `X2：作者证明了核心发现` 或 `Y：贡献成立/值得发表` 的断点；
- 位于较高 claim 层级，或虽是低层 evidence-leaf 但构成上层 claim 的瓶颈证据；
- 使 causal claim、construct-measure fit、sample-mechanism fit、result-contribution link 不稳的断点；
- 有明确 evidence location 或明确 QC 缺口的问题；
- 多个箭头共同削弱同一贡献链时，可合并为一个 major concern；
- 能产生可执行修改建议的问题。
- 修复成本与影响程度匹配的问题：高影响高成本适合 major concern，低成本澄清适合 minor 或 revision action。

经管 / 社科实证论文还要消费 `empirical-social-science-review-adapter` 的输出。以下问题即使看起来位于低层，也不能自动丢掉：

- `construct-proxy fit` 影响核心 X 或 Y 的含义；
- `sample-scope fit` 影响机制、外推或目标总体；
- `control-variable role` 可能改变估计对象或构成 bad control；
- `inference-clustering fit` 可能改变核心结果显著性；
- `mechanism-evidence strength` 决定机制 claim 是否只是相关通道；
- `descriptive-validity` 导致构造变量方向、量纲或分布不可解释。

中文经管 / 中文社科语境下，还要消费 `chinese-management-econ-review-adapter` 的输出。指标方向、文本口径、中文文献谱系、本土制度语境、政策化表达和表格变量说明，只有在它们卡住 parent claim 时才升级；若只是表达或格式改进，放入 minor / revision action / linked hold。

谨慎选择：

- 只影响表达但不影响核心论证的问题；
- 只位于低层 evidence-leaf，且不是上层 claim 必要支撑或瓶颈的问题；
- 只影响表格报告透明度但未影响结论的问题；
- 需要大量外部文献才能确认的问题；
- 与其他 major concern 重复的问题。

## 全量候选池优先

在输出 `major-concern-candidates.md` 之前，必须先输出：

```text
full-issue-candidate-pool.md
human-readable-issue-candidates.md
```

`full-issue-candidate-pool.md` 是全量候选账本，覆盖所有可写的 weak / broken / unclear / needs-qc / needs-external-evidence 箭头；`human-readable-issue-candidates.md` 是面向用户/审稿人的自然语言候选说明。

不要只给机器代号。每个候选 issue 必须同时有：

```text
issue_id
target_arrow_id
target_proposition_form
valid_counterexample_shape
does_issue_match_counterexample_shape
claim_level
bottleneck_status
surface_issue: 表面问题，例如“Robot 变量构造不清”
deep_arrow_break: 深层箭头断点，例如“进口机器人/组件不等于企业实际采用并使用机器人”
human_readable_summary: 2-5 句接近 review-draft 语气的说明
evidence_basis: 原文/表格/证据账本位置或 QC 缺口
why_it_matters: 为什么影响 X1/X2/Y 或 parent claim
possible_revision: 作者可以如何补证据、补分析或降调
suggested_bucket: major-candidate / minor-candidate / revision-action / evidence-needed / hold-for-qc
merge_split_advice: 可与谁合并；合并时必须保留哪些子问题
```

`human_readable_summary` 必须让没有读过 arrow ledger 的人也能看懂。禁止只写：

```text
A6 weak, E-X1/E-X2, needs-proxy-qc
```

应写成：

```text
作者把 Robot 表述为 firm-level robot adoption，但操作化似乎来自机器人或机器人相关产品进口。进口行为不必然等于企业实际安装并使用机器人，因为可能存在组件进口、中间商进口、维修/库存/转售或进口后滞后投产。若作者不能验证这条测量桥梁，核心 X 应更谨慎地表述为 robot-related imports，而不是 firm-level robot adoption。
```

候选池不等于最终审稿正文。候选池可以偏全；最终正文再根据审稿策略、篇幅和读者接受度选择、合并或降级。

外部证据规则：

- `needs-external-evidence` 箭头若影响 `X1/X2/Y`，可进入 `evidence-needed issue` 或 `search-before-major`；
- 若外部证据增强尚未完成，不得把它写成 confirmed major concern；
- 若审稿任务必须立即成文，应写成“建议作者补充/澄清相关文献或方法依据”，而不是断言作者错误；
- 若后续 `external-evidence-ledger.md` 已回填为 `weak-confirmed` 或 `broken-confirmed`，才可升级为 major concern。

QC guardrail：

- `needs-qc`、`needs-source-figure-qc`、`needs-supplement-qc`、`needs-fulltext-pattern-check`、`needs-human-pdf` 可以进入候选池，但默认只能作为 `hold-for-qc`、`evidence-needed`、`search-before-major` 或 confirmed issue 的 linked hold；
- 不得把未核图、补充材料、source data 或全文模式直接写成 confirmed major 的 evidence basis；
- 若一个 major 同时包含 confirmed arrows 和未核 arrows，必须拆成 `primary_confirmed_arrows` 与 `linked_hold_arrows`，并写明 `evidence_guardrail`。

混合 issue：

```text
primary_confirmed_arrows = 已经可支持该 issue 的主要箭头
linked_hold_arrows = 与该 issue 高度相关、但还需 QC / 全文 / 补充材料才能定性的箭头
evidence_guardrail = 哪些判断已确认，哪些仍是条件性判断
```

混合 issue 可以被选为 major-candidate，但 major 的核心判断只能建立在 `primary_confirmed_arrows` 上；`linked_hold_arrows` 只能作为后续核验或补充要求。

## Claim Level 与瓶颈判断

选点不是只看“细不细”，而是看该断点在论证树中的层级，以及它是否卡住上层 claim。

每个候选 issue 必须标注：

```text
claim_level: root / major-claim / middle-claim / subclaim / evidence-leaf
bottleneck_status: root-blocking / major-claim-blocking / local-support / cosmetic / irrelevant
parent_claim_id:
parent_claim_text:
why_this_detail_matters:
```

判断规则：

- 越高层级的箭头，默认优先级越高；
- 低层 evidence-leaf 只有在它是上层 claim 的必要支撑或瓶颈时，才可进入 major；
- 如果低层细节只是让报告更完整，但不改变上层 claim，通常进入 minor / revision-action；
- 如果低层细节与主箭头无关，进入 discarded-but-noted 或不选；
- 对材料/器件论文，zeta、EIS、EDS、BET、load resistance、washing cycles 等实验名本身不是 major，只有当它们是 mechanism、performance、durability、application claim 的瓶颈证据时，才支撑 major。

推荐自问：

```text
如果作者不补这个低层证据，上层 claim 是否还能成立？
这个低层证据支撑的是哪一个 parent claim？
读者能否从 issue 写法中看出它不是“电饭锅厂家”式无关细节？
```

## 输出字段

`review-issue-arrow-map.md`：

```text
issue_id
issue_level: major / minor / revision-action / note
issue_status: confirmed / evidence-needed / search-before-major / hold-for-external-evidence
target_arrow_id
target_proposition_form
valid_counterexample_shape
does_issue_match_counterexample_shape
primary_confirmed_arrows
linked_hold_arrows
claim_level
bottleneck_status
parent_claim_id
parent_claim_text
weakened_node
impact_on_X1_X2_Y
evidence_location
evidence_guardrail
why_selected
why_this_detail_matters
possible_revision
repair_route
repair_cost
priority_basis: impact x repair_cost
```

`full-issue-candidate-pool.md`：

```text
issue_id
target_arrow_id
status
target_proposition_form
valid_counterexample_shape
does_issue_match_counterexample_shape
claim_level
bottleneck_status
surface_issue
deep_arrow_break
evidence_basis
why_it_matters
possible_revision
suggested_bucket
merge_split_advice
keep_in_pool_reason
```

`human-readable-issue-candidates.md`：

```text
# Human-readable Issue Candidates

## Candidate I1: short title

Suggested bucket:
Target arrows:
Affected claim:

Draft-style explanation:
...

Why this matters:
...

Possible revision:
...

Merge/split note:
...
```

## 完成标准

- 已先生成全量候选池，而不是只输出最终 selected issues；
- 全量候选池覆盖所有可写的 weak / broken / unclear / needs-qc / needs-external-evidence 箭头，未纳入者必须说明 irrelevant 或 duplicate；
- 每个候选 issue 都有人类可读说明，不能只有 arrow_id、evidence_id、qc_flags；
- 每个候选 issue 都说明表层问题和深层箭头断点，避免把关键断点压成泛泛标签；
- 每个候选 issue 都说明它如何有效削弱目标命题；若目标是假言命题，不能把单纯 `非A` 误写成对 `A -> B` 的反驳；
- 每个 selected issue 都绑定 target arrow；
- 每个 selected issue 尽量绑定 repair_route；若没有 `arrow-repair-map.md`，标记 `missing-repair-map`；
- 每个 major concern 都说明影响 `X1`、`X2` 或 `Y`；
- 每个 selected issue 都标注 `claim_level` 与 `bottleneck_status`；
- 低层 evidence-leaf 若被选为 major，必须说明它阻断哪个 `parent_claim`，以及为什么不是无关细节；
- 每个 major concern 都说明其 evidence basis 是否来自 confirmed arrows，若含未核箭头，已拆为 `primary_confirmed_arrows` 与 `linked_hold_arrows`；
- 每个 selected issue 都写明 `evidence_guardrail`，避免把 `needs-qc` 或 `needs-fulltext-pattern-check` 写成已确认问题；
- 经管/社科实证论文已检查是否有 adaptor 输出；若未调用但任务明显属于该类型，标记 `missing-empirical-adapter-review`；
- 中文经管/中文社科论文已检查是否有中文 adaptor 输出；若未调用但任务明显属于该语境，标记 `missing-chinese-local-adapter-review`；
- major 排序时考虑 `impact x repair_cost`：高影响高成本优先进入 major，低成本澄清通常进入 minor / revision action，低影响高成本通常暂缓；
- 未入选的重要断点进入 `discarded but noted`；
- 不把所有 weak arrows 都机械写成 major concern；
- 输出可交给 `academic-review-argument-audit` 写成审稿或自审段落。
