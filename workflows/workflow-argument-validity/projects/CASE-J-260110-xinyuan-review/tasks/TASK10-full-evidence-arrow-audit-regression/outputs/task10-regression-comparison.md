# TASK10 Regression Comparison

Comparison was performed only after TASK10 audit outputs were frozen.

## Compared Materials

| prior task | files read for comparison | role |
|---|---|---|
| TASK08 | academic-arrow-audit-table.md; academic-arrow-break-summary.md | prior rerun, mainly internal audit with some unclear/external-pending statuses |
| TASK09 | academic-arrow-audit-table.md; academic-arrow-break-summary.md; external-evidence-request.md; external-evidence-ledger.md; issue-selection-candidates.md; qc-and-skill-feedback.md | clean subagent internal-blind style output with centralized requests but no search |

## Overall Difference

TASK10 keeps the same author-tree orientation as TASK08/TASK09, but it is materially different because it actually completes the `full-evidence-audit` loop:

1. Internal audit was frozen before search.
2. External evidence requests were centralized.
3. External sources were searched and recorded with request_id/target_arrow bindings.
4. Final audit statuses distinguish internal-only, externally confirmed, insufficient-result, and manual-verification-needed.

## What TASK10 Has More Than TASK08

| area | TASK08 | TASK10 difference |
|---|---|---|
| external evidence | TASK08 marks literature/method needs but does not produce a source-bound external ledger. | TASK10 records source URLs/metadata for R01-R14 and backfills findings into final statuses. |
| policy/regulatory evidence | TASK08 flags policy overclaim internally. | TASK10 verifies 2019 Securities Law, 2025 CSRC disclosure measures, CSRC penalty discretion, and enforcement context. |
| method evidence | TASK08 notes DID, clustering, Bacon, Oster and placebo as method/QC needs. | TASK10 links these to method sources and changes many from pending/unclear to weak-confirmed or still-unclear with reasons. |
| construct evidence | TASK08 flags KV and RZ/HHI issues internally. | TASK10 confirms KV proxy limits, RZ industry-level origin, and competition disclosure literature with source metadata. |
| status granularity | TASK08 uses `weak`, `unclear`, `strong-with-qc`, `broken/needs-table-qc`. | TASK10 adds `weak-confirmed`, `strong-after-search`, `still-unclear`, `broken-pending-manual-qc`, and separates external confirmation from manual QC. |
| full request coverage | TASK08 did not have a full evidence-request/ledger pair. | TASK10 has 14 requests and a coverage summary. |

## What TASK10 Has Less Or Different Than TASK08

| area | TASK08 emphasis | TASK10 difference |
|---|---|---|
| treatment timing | TASK08 treats A017 as weak due to annual POST timing. | TASK10 keeps A017 as strong-with-qc internally because coding is explicit, while timing concerns are folded into A012/A035 and sensitivity map. |
| sample design | TASK08 marks A011/A018 as candidate-major. | TASK10 keeps them weak but not externally escalated; they remain internal design/scope issues rather than source-resolvable problems. |
| A013 main result | TASK08 marks A013 weak because it depends on KV. | TASK10 marks final A013 weak-confirmed: coefficient supports KV decline, but broad disclosure-quality wording remains bounded by R03/R04. |
| A030 | TASK08 uses broken/needs-table-qc. | TASK10 uses broken-pending-manual-qc to make clear external theory search cannot resolve restored-table accuracy. |

## What TASK10 Has More Than TASK09

| area | TASK09 | TASK10 difference |
|---|---|---|
| execution mode | TASK09 final table says external evidence was not searched. | TASK10 performs full-evidence search and records sources. |
| external ledger | TASK09 external ledger is all `not searched / pending`. | TASK10 ledger has official, method, literature, and citation evidence, plus insufficient-result/manual-QC statuses. |
| treatment definition | TASK09 marks A008/A016 strong-with-qc. | TASK10 downgrades A008/A016 to weak-confirmed after official/regulatory search found no support for the operational rule equaling genuine proactive intent. |
| market pressure | TASK09 marks A021/A031 strong-with-qc/no-issue for market pressure. | TASK10 downgrades A021/A031 to weak-confirmed because attention proxies remain compatible with visibility/selection. |
| financing dependence | TASK09 marks A039 strong-with-qc. | TASK10 downgrades A039 to weak-confirmed after RZ external finance dependence was verified as originally industry-level. |
| contribution arrows | TASK09 leaves A001/A006/A007/A041/A042 as needs-external-evidence. | TASK10 converts them to weak-confirmed because prior peer-disclosure/negative-disclosure literature narrows the novelty claim. |
| policy arrow | TASK09 leaves A043 weak with external need. | TASK10 confirms policy overclaim: official sources support disclosure duties and calibrated discretion, not blanket active-disclosure exemption. |

## What TASK10 Has Less Or Different Than TASK09

| area | TASK09 emphasis | TASK10 difference |
|---|---|---|
| no-search discipline | TASK09 is cleaner as a pure blind-run fixture. | TASK10 is not blind after freeze; it is a full-evidence regression and therefore more judgment-bearing. |
| some strong-with-qc labels | TASK09 preserves many arrows as strong-with-qc where internal evidence is traceable. | TASK10 is stricter after external evidence: traceability is not enough when construct/method/source standards narrow the inference. |
| external request naming | TASK09 uses XR01-XR12. | TASK10 uses R01-R14 and expands requests to official data/policy and contribution-positioning. |

## Main Convergent Findings Across TASK08/09/10

| finding | tasks agreeing | note |
|---|---|---|
| KV-to-disclosure-quality needs bounded wording | TASK08; TASK09; TASK10 | TASK10 externally confirms proxy-bounded reading. |
| DID/identification remains weaker than causal wording | TASK08; TASK09; TASK10 | TASK10 adds method-source confirmation. |
| Table 11 reputation mechanism conflict is central | TASK08; TASK09; TASK10 | TASK10 keeps this as manual-verification-needed/broken-pending-manual-qc. |
| information-transmission exclusion is overstrong | TASK08; TASK09; TASK10 | TASK10 leaves this mostly internal; no external source needed to see null-result reversal. |
| robustness tests need threat-to-test mapping | TASK08; TASK09; TASK10 | TASK10 separates method-confirmed limits from figure/table QC. |
| policy implication is over-elevated | TASK08; TASK09; TASK10 | TASK10 confirms with official regulatory sources. |

## Main Divergent Judgments

| arrow | TASK08 | TASK09 | TASK10 | reason for TASK10 difference |
|---|---|---|---|---|
| A008/A016 | weak | strong-with-qc | weak-confirmed | Full evidence search did not validate operational rule as genuine active/proactive disclosure. |
| A010 | weak | needs-external-evidence | weak-confirmed | KV is externally supported as a proxy but not the full construct. |
| A021/A031 | A031 weak | A021/A031 strong-with-qc | weak-confirmed | External/proxy search leaves attention vs pressure unresolved. |
| A027 | unclear | strong-with-qc | still-unclear | Method evidence says Bacon/stacked DID help, but figure/estimator details remain unresolved. |
| A039 | weak | strong-with-qc | weak-confirmed | RZ construct-level mismatch confirmed by source metadata. |
| A043 | weak | weak | weak-confirmed | Official sources confirm cautious discretion, not exemption policy. |

## Process Lessons

1. TASK09 is a better fixture for testing blind-mode discipline; TASK10 is a better fixture for testing full-evidence mode.
2. Full-evidence mode materially changes statuses, especially where TASK09 used `strong-with-qc` for traceable but externally contestable arrows.
3. The skill needs a regression expectation that not all searches resolve arrows: insufficient-result and manual-verification-needed are valid non-terminal outputs.
4. Official/regulatory evidence must be first-class in academic arrow audit, because it can change policy arrows as much as literature changes gap arrows.
5. External evidence should not be allowed to override manual table QC: A030 and A036 remain unresolved despite successful source search.

## Backfeed Points

| target | point |
|---|---|
| academic-arrow-audit main axis | Add explicit full-evidence status transitions: `needs-external-evidence -> weak-confirmed / strong-after-search / still-unclear / insufficient-result`. |
| review-sensitivity mapping | Include heterogeneity construct-level mismatch and policy implication fit as high-sensitivity map types. |
| external evidence ledger template | Require `source_url_or_metadata`, `search_status`, `what_it_changes`, and `what_remains_unresolved`. |
| method knowledge feedback | Distinguish method-source confirmation of limitation from manual table/figure QC. |
| policy/regulatory route | Add official-source route for policy implication arrows and legal/institutional context arrows. |
