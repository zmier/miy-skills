# QC and Skill Feedback

## Blind-Run QC

| check | status | notes |
|---|---|---|
| eight-step main axis followed | pass | log explicitly records steps 1-8 plus sensitivity preparation. |
| author tree preserved | pass | No reviewer attack nodes were added to the author tree. |
| first round internal audit before search | pass | Internal audit table completed before external request/ledger. |
| external evidence centralized | pass | All external needs placed in `external-evidence-request.md`; no scattered lookup. |
| no web/database search | pass | `external-evidence-ledger.md` marks every request as not-searched/pending. |
| arrow-bound issues | pass | Every candidate is tied to one or more `arrow_id`s. |
| no final review opinion | pass | Only diagnostic tables and candidates produced. |
| forbidden files avoided | pass | Did not read TASK08, old audit/review outputs, Xinyuan review, or TASK07 xinyuan-coverage file. |

## Skill Feedback Points

1. **Status vocabulary needs one canonical list.**  
   The SKILL text uses `needs-qc`, the template mentions `needs-table-qc` and `needs-method-qc`, and the user asked for `needs-qc`. In this run, I used top-level `needs-qc` plus `qc_flags` such as `table-qc`, `method-qc`, `figure-qc`. The SKILL could specify whether subtype statuses are allowed or should always live in `qc_flags`.

2. **Evidence-set edges need an explicit audit policy.**  
   TASK07 includes A001-A043 author-claim arrows and E001-E034 evidence-set edges. The SKILL says every arrow_id should be audited, but in academic trees evidence-set edges may explode the table. A clear rule would help: e.g., audit claim arrows fully, bind evidence-set edges through `evidence_ids`, and only audit E edges separately when evidence itself is contested.

3. **Review-sensitivity map is useful but should define relation to step 1.**  
   The SKILL has a step 0 sensitivity map and an eight-step main axis. In practice, sensitivity mapping helps prioritize high-risk arrows before full audit. The main-axis reference could state whether `review-sensitivity-map.md` is optional preparation, required output, or only required when evidence supports it.

4. **External-evidence round needs a formal “not searched”回填 pattern.**  
   This task intentionally skipped retrieval. The SKILL says keep `needs-external-evidence`, but final ledger fields such as `what_it_changes` are designed for completed searches. The templates could include a standard not-searched row pattern to avoid awkward pseudo-ledger entries.

5. **Method-QC routing could expose minimal audit checklists without invoking subskills.**  
   A clean subagent can identify that DID clustering, pretrend, staggered treatment, Oster, and placebo need method QC, but the parent SKILL does not define lightweight acceptance points. A short reference for “mark needs-method-qc without hard judging” would improve consistency in no-search blind runs.

## Case-Derived Reference Candidates

| candidate | source arrows | why transferable | proposed target |
|---|---|---|---|
| Table-text conflict should force `weak` or `needs-qc` before mechanism upscaling. | A014; A030 | Common in empirical papers where prose overstates subgroup tables. | academic-fallacy-adapter or mechanism-claim reference |
| Heterogeneity with reverse significant subgroup should be treated as boundary complexity, not simple robustness. | A040 | Helps separate boundary condition from robustness support. | academic-arrow-types / robustness-threat notes |
| Not-significant exclusion tests should usually be phrased as “no evidence for channel” rather than “channel is not main mechanism.” | A032 | Common mechanism-exclusion overclaim. | mechanism-claim reference |
| In no-search runs, literature gap arrows should remain `needs-external-evidence`, not weak/broken. | A006; A041; A042 | Protects blind runs from overclaiming based on memory. | academic-arrow-audit-main-axis |
