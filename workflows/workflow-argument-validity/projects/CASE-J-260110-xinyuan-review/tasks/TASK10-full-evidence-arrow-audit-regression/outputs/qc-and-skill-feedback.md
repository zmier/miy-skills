# QC And Skill Feedback

## Regression Findings About The Skill

| feedback_id | observation | implication | possible skill feedback |
|---|---|---|---|
| F01 | The full-evidence mode worked best when internal audit was frozen before search. | Prevents external sources from reshaping the initial arrow list. | Keep the explicit "internal freeze -> evidence request -> search -> backfill" discipline. |
| F02 | External evidence is not only literature; official law/regulation changed the policy arrow materially. | Policy arrows need official-source routing, not generic web search. | Add a policy/regulatory evidence sub-template with official-source priority and "policy overclaim" mapping. |
| F03 | Search failures and thin evidence must be typed. | R02/R07/R10 would otherwise be mistaken for true absence. | Keep statuses `insufficient-result`, `manual-verification-needed`, `technical-failure`; add examples. |
| F04 | Method evidence often changes strength without fully resolving the arrow. | DID/Oster/Bacon sources confirmed limits, not binary pass/fail. | In method-ledger template, include "what remains unresolved". |
| F05 | Table/figure manual QC cannot be solved by external search. | A030/A036 remain manual-verification-needed despite evidence search. | Skill should explicitly separate external evidence from source-table verification. |
| F06 | Literature gap searches need nearest-neighbor framing. | Seo 2021 weakens broad peer-disclosure novelty but not the exact active-violation niche. | Add `nearest_prior_work` and `remaining_novelty_niche` fields for gap arrows. |
| F07 | Construct-level mismatch appeared in heterogeneity analyses, not just variables. | RZ external finance dependence and HHI competition affect boundary claims. | Add "heterogeneity construct-level fit" to sensitivity map examples. |

## Process Problems Exposed

| problem | evidence | consequence |
|---|---|---|
| Source retrieval breadth is uneven without database access. | CNKI/WoS were not directly used; web/OpenAlex-like metadata and official pages carried search. | Some Chinese citation verification remains partial/insufficient. |
| Official regulatory pages are available but legal interpretation is delicate. | Securities Law/CSRC rules support disclosure duties and discretion, not automatic exemption. | Policy arrows should be cautious and may need legal expert review. |
| Current restored tables are not cell-by-cell audited. | TASK07 QC marks most table evidence as needs-table-visual-qc. | Final statuses relying on tables should retain QC caveats. |

## Reusable Reference Candidates

1. `policy-implication arrow`: empirical evidence of improved disclosure can support cautious compliance/discretion implications, but recommendations for exemption/leniency require official legal basis.
2. `staggered DID robustness arrow`: Bacon decomposition and stacked DID are diagnostic/supportive; they do not alone establish all parallel-trend, clustering, or treatment-effect assumptions.
3. `construct adaptation arrow`: when a classic construct is industry-level or long-run (for example RZ external finance dependence), firm-year adaptation needs explicit justification.
4. `mechanism null-result arrow`: nonsignificant tests should be written as "no evidence detected in this proxy", not as proof that a mechanism is absent.
