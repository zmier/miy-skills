# TASK07 Quality Acceptance

## Verdict

TASK07 passes as a `full-tree` author-tree extraction and is a clear improvement over the earlier weak blind runs.

Compared with TASK02/TASK04, it no longer collapses the paper into a simplified tree. It produces the required spine, node ledger, evidence ledger, edge ledger, recursive master tree, evidence-expanded Mermaid, Obsidian link map, QC, and log.

Compared with TASK06, it is not dramatically larger, but it is cleaner as a workflow artifact: it separates author-tree extraction from review sensitivity / arrow audit, concretizes X2, adds more explicit citation evidence, and records handoff targets for later arrow audit without judging the arrows in this step.

## Output Contract

| check | result | note |
|---|---|---|
| Required files | pass | All requested files are present. |
| Author tree only | pass | No `review-sensitivity-map.md`, `sensitivity-expanded-mermaid.md`, arrow-audit table, or issue-selection output was generated. |
| X2 concrete | pass | X2 is not “核心经验发现成立”; it is written as active violation disclosure improves peer disclosure quality via reputation competition and market pressure. |
| Canonical ledgers | pass | Node, edge, and evidence ledgers are all present. |
| Edge boundary | pass | Edge status is limited to `not-yet-audited` / `needs-qc`; no `strong/weak/broken` judgment is made. |
| Evidence granularity | pass with QC | Most leaves are concrete table cells, variable definitions, sample rules, model facts, citation uses, or policy claims. |
| Mermaid | partial | It is derived from ledgers and includes many evidence leaves, but marks `mermaid-render-limit`; full structure remains in `recursive-tree-master.md`. |
| Obsidian links | partial | Manuscript/table anchors are present; many literature notes still need citation-link verification. |

## Comparison With Earlier Runs

| run | evidence ledger size | main character | judgment |
|---|---:|---|---|
| TASK01 V5 | about 68 table rows | strong calibrated tree after user iteration | strong but case-calibrated, not blind |
| TASK02 blind/full-v2 | about 69 table rows | fixed some V5 requirements but still diagnosis showed contract weakness | improved over blind sketch, still not stable enough |
| TASK04 blind | about 42 table rows | too compressed | regression / insufficient |
| TASK06 clean rerun | about 108 table rows | strong full tree, but still included sensitivity outputs inside extraction task | content strong, boundary less clean |
| TASK07 latest | about 111 table rows | full author tree, cleaner stage boundary, richer citation evidence, explicit handoff | best workflow-compliant extraction so far |

## What Improved

1. X2 is now a real claim.

   TASK07 writes the concrete finding as: active disclosure of violations improves peer firms' disclosure quality and industry self-discipline through reputation competition and market pressure. This fixes the earlier risk of using “核心经验发现成立” as an empty placeholder.

2. The claim/evidence boundary is cleaner.

   The node ledger uses claims such as treatment definition, theory mechanism, outcome operationalization, sample structure, DID design, main result, mechanism, robustness, and contribution. The evidence ledger then drills into table values, model facts, variable definitions, sample rules, and citation uses.

3. Citation evidence entered the evidence ledger.

   TASK07 does not merely say “existing literature supports this”. It lists specific cited works and records how the author uses them for gap, mechanism, variable construction, heterogeneity, or contribution positioning. Many links remain unverified, but the extraction stage now exposes the work to be done.

4. Identification design is much more DAG-ready.

   It records treatment/shock, treated group, timing, model, fixed effects, clustering, pretrend, placebo, robustness, and an explicit note that the comparison/control group is only implied and may need more text for later DAG audit.

5. It no longer mixes extraction and attack.

   Table 11 conflict, cluster-level fit, timing, construct fit, and robustness-threat fit are captured as handoff targets, not turned into final review conclusions in the author tree.

## Remaining Weak Spots

1. Table values are not cell-by-cell visually audited.

   The task uses TASK05 table extraction and page-level visual QC. This is enough for extraction, but not enough for final review prose that quotes exact coefficients.

2. Figure evidence is still weak.

   Figure 1/2 evidence relies on manuscript prose and marked `needs-figure-qc`. Later arrow audit should not lean heavily on graph shape before figure crops are checked.

3. Mermaid is not the whole tree.

   The Mermaid view is useful and more complete than earlier compact views, but it still omits some repeated low-level leaves due to render limit. For serious audit, use `recursive-tree-master.md` and the ledgers as authority.

4. Some branch labels remain slightly generic.

   For example, “稳健性与边界条件” is acceptable as a branch label, but later issue selection should translate it back into concrete claims: which robustness test supports which threat, and whether that threat is actually the relevant one.

## Acceptance Score

| dimension | score | note |
|---|---:|---|
| Contract compliance | 9/10 | Correct files, correct boundaries, clean log. |
| Core claim clarity | 9/10 | X/M/Y/Y2 and X2 are concrete. |
| Evidence granularity | 8/10 | Strong table/design/citation coverage; figure and cell QC remain partial. |
| Workflow boundary discipline | 9/10 | Author tree is separated from sensitivity / arrow audit. |
| Readiness for arrow audit | 8/10 | Ready, but with table/figure/citation caveats. |

Overall: `8.5/10`.

TASK07 is good enough to become the current academic paper tree extraction regression baseline for this case. The next step should be `academic-argument-arrow-audit`, using TASK07 outputs as inputs.
