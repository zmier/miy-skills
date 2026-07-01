# Extraction QC

## Status

- mode: full-tree regression
- author_tree_only: yes
- forbidden_outputs_generated: no
- ready_for_academic_arrow_audit: yes, with QC caveats
- dag_ready: partial

## Contract Compliance

| check | status | notes |
|---|---|---|
| Must Read files read | pass | Skill, required references, manuscript, restoration QC, table visual QC were read. |
| Must Not Read avoided | pass | No old TASK01/TASK02/TASK04/TASK06 outputs, review text, sensitivity maps, issue selections, or current conversation logs were read. |
| Required outputs produced | pass | All 10 requested output/log files produced. |
| `review-sensitivity-map.md` avoided | pass | No review/audit output generated. |
| X2 concrete | pass | X2 is written as author-claimed X -> Y: active disclosure of violations improves peer firms' disclosure quality and industry self-discipline via reputation competition and market pressure. |
| Edge status limited | pass | Edge statuses are only `not-yet-audited` and `needs-qc`. |

## Full-Tree Completeness

| check | status | notes |
|---|---|---|
| canonical-node-ledger | pass | Claim hierarchy is recursive and not forced to five levels. |
| evidence-ledger | pass | Evidence leaves include text, variable definitions, design facts, table coefficients/statistics, citation uses, sample rules, FE, cluster, pretrend, placebo, robustness, mechanisms, heterogeneity, and policy implications. |
| canonical-edge-ledger | pass | Restores author-claimed support relations only. |
| recursive-tree-master | pass | Full text tree preserves full structure. |
| evidence-expanded-mermaid | partial | `mermaid-render-limit`: major tree and many minimal evidence leaves rendered; some lower-level citation/heterogeneity details preserved in master tree and evidence ledger. |
| obsidian-link-map | partial | Links use manuscript/table anchors where available; many literature notes marked `needs-literature-note`/`needs-citation-link`. |

## Identification Design Coverage

| item | evidence coverage |
|---|---|
| treatment/shock | `E-XDEF-1`, `E-XDEF-2`, `E-XDEF-3` |
| treated group | `E-DID-TREAT-1` |
| comparison/control group | implied by `Peerdumy = 0`; needs more explicit author text if later DAG audit requires it |
| timing | `E-DID-POST-1`, `E-DID-POST-2`, `E-SAMPLE-2` |
| model | `E-MODEL-1`, `E-MODEL-2` |
| FE | `E-MODEL-3`, `E-MODEL-5` |
| cluster | `E-MODEL-4` |
| pretrend | `E-PRETREND-1` to `E-PRETREND-4` |
| placebo | `E-ROB-PLACEBO-1`, `E-ROB-PLACEBO-2`; figure QC needed |
| robustness | `E-ROB-STACK-*`, `E-ROB-MATCH-*`, `E-ROB-COMMON-*`, `E-ROB-OSTER-*`, `E-ROB-ALT-*` |

## QC Flags

| flag | severity | evidence/node | reason |
|---|---|---|---|
| needs-table-visual-qc | medium | most table evidence | TASK05 did page-level visual QC, not cell-by-cell audit. |
| needs-figure-qc | medium | `E-ROB-BACON-1`, `E-ROB-PLACEBO-*` | Figure 1/2 were not precisely cropped; evidence comes from manuscript text. |
| table-text-conflict | high | `E-MECH-REP-3`, `P7a`, edge `E021` | Table 11 column(3) shows PosCAR[-10,10] not significant and NegCAR[-10,10] significant, conflicting with author prose. |
| needs-citation-link | low | citation evidence | Citation uses were extracted into evidence ledger, but many literature-note links are not verified. |
| mermaid-render-limit | low | evidence-expanded-mermaid | Full structure retained in recursive tree and ledgers; Mermaid omits some repeated low-level evidence leaves. |

## Abstract Evidence Leaf Audit

- No evidence row is merely “主结果”“稳健性”“机制检验” without a lower-level location/value.
- Some edges group multiple minimal evidence IDs into evidence sets for readability; the minimal leaves remain individually listed in `evidence-ledger.md`.

## Handoff to Academic Arrow Audit

Suggested handoff targets:

| handoff_type | suggested_evidence_ids | suggested_arrow_ids | reason |
|---|---|---|---|
| treatment-timing | `E-DID-POST-1`; `E-DID-POST-2`; `E-SAMPLE-2`; `E-ROB-ALT-2`; `E-ROB-ALT-3` | `A012`; `A027` | POST timing and alternative POST_Month are central to DID interpretation. |
| cluster-level-fit | `E-MODEL-4`; `E-MODEL-5`; `E-MAIN-1`; `E-MAIN-2` | `A025`; `A028` | Treatment varies at industry/event timing, while clustering is at firm level. Audit later, do not judge here. |
| mechanism-text-table-conflict | `E-MECH-REP-3` | `A030`; `E021` | Table 11 column(3) conflicts with author mechanism prose. |
| construct-measure-fit | `E-YDEF-1`; `E-YDEF-2`; `E-ROB-ALT-1` | `A010`; `A035` | KV and DA as reverse proxies for disclosure quality should be audited later. |
| robustness-threat-fit | `E-ROB-PLACEBO-*`; `E-ROB-COMMON-*`; `E-ROB-OSTER-*` | `A036`; `A034`; `A035` | Robustness tests should be matched to core threats in later arrow audit. |

## Final QC Conclusion

This is a complete author-tree regression output under the contract. It is suitable as input to `academic-argument-arrow-audit`, with explicit caveats for Table 11 conflict, figure QC, table cell-level QC, and citation-link completion.
