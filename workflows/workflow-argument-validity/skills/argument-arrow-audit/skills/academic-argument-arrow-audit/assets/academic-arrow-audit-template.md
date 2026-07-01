# Academic Arrow Audit Template

## Arrow Audit Table

| arrow_id | 作者用 A | 推出 B | A 是否足以推出 B | 隐含前提 H | evidence_ids | paper_type | status | break_type | fallacy_label | arrow_type | domain_expression | qc_flags | route_output | impact_on_X1_X2_Y | possible_revision | selection_hint |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 |  |  |  |  |  | empirical/theory-model/review-concept/mixed | strong/strong-with-qc/weak/broken/unclear/needs-qc/needs-external-evidence |  |  | construct-measure / treatment-definition / sample-mechanism-fit / construct-level-fit / timing-fit / baseline-fit / identification-causal / robustness-threat / ... |  | reporting-qc / table-cell-qc / sample-consistency-qc / citation-qc / figure-qc / method-qc / external-evidence-qc | parent / causal / statistical / literature-gap | X1/X2/Y |  | candidate-major/candidate-useful/minor/no-issue |

`arrow_type` 是标签，不是审查顺序。必须先完成“作者用 A 推出 B；A 是否足以推出 B”的判断。

`fallacy_label` 是可选辅助标签；审稿正文优先写清证据与结论为何不匹配。

`domain_expression` 来自 `references/academic-fallacy-adapter.md`，用于把通用断点翻译成实证、理论或综述/概念论文中的专业表达。

`status = strong-with-qc` 表示当前证据方向支持作者箭头，但仍需要表格、图、引用、方法或来源复核后才能写入正式审稿意见。

`status = needs-external-evidence` 表示稿件内部证据不足以定性，必须先进入 `external-evidence-request.md` 集中检索或方法核验，不能直接写成已确认问题。

一级 `status` 只使用：

```text
strong
strong-with-qc
weak
broken
unclear
needs-qc
needs-external-evidence
```

`needs-table-qc`、`needs-method-qc`、`needs-citation-qc` 不作为一级 status；写入 `qc_flags`。若 QC 缺口大到无法判断，一级 status 写 `needs-qc`。

`qc_flags` 用于显式保留质量复核需求。常见取值：

```text
reporting-qc
table-cell-qc
figure-qc
citation-qc
sample-consistency-qc
method-qc
external-evidence-qc
method-qc-if-used-as-major
```

`route_output` 记录该条箭头是父 Skill 直接审计，还是由因果、统计、文献 gap 等子 Skill 返回。

## Review Issue Arrow Map

| issue_id | issue | target_arrow | weakened_node | impact_on_Y | evidence_location | proposed_revision |
|---|---|---|---|---|---|---|
| R1 |  | A1 | X1/X2/Y |  |  |  |

## Major Concern Candidate

```text
Concern:
Target arrow:
作者用 A 推出 B:
A 为什么不足以推出 B:
Why it matters:
Evidence:
Suggested revision:
Domain expression:
QC flags:
Recommended severity:
```
