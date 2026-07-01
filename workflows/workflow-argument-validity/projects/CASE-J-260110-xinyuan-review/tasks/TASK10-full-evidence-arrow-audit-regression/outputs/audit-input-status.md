# Audit Input Status

## Mode And Boundary

- mode: full-evidence-audit
- audit target: author-claimed support arrows from TASK07.
- write scope: TASK10 directory only.
- forbidden-before-freeze materials avoided: TASK08, TASK09, TASK02 xinyuan-comparison, 欣媛审稿意见, current conversation logs.

## Inputs Read Before Freeze

| input | status | use |
|---|---|---|
| academic-argument-spine.md | read | core X/M/Y/Y2 and design spine |
| canonical-node-ledger.md | read | node definitions and source links |
| canonical-edge-ledger.md | read | authoritative arrow list |
| evidence-ledger.md | read | evidence IDs and QC flags |
| extraction-qc.md | read | caveats and handoff targets |
| paper-argument-tree.md | read | top-level structure |
| recursive-tree-master.md | read | full recursive tree |
| evidence-expanded-mermaid.md | read | derived visual cross-check |
| obsidian-link-map.md | read | source-link status |

## Input Completeness

| area | status | notes |
|---|---|---|
| claim tree | complete | Y0, X1, X2, P9 and recursive children are present. |
| claim-to-claim arrows | complete | A001-A043 available; all restored as author-claimed support relations. |
| evidence-to-claim arrows | complete-enough | E001-E034 summarize evidence sets; minimal evidence leaves are in evidence-ledger. |
| evidence details | complete-enough-with-qc | Table evidence is page-level restored but not cell-by-cell audited. |
| citation links | partial | many citation evidence rows carry `needs-citation-link` or `needs-literature-note`. |
| figures | partial | Bacon and placebo figures need precise crop/manual visual QC. |

## QC Caveats Carried Into Audit

| qc_flag | target | audit treatment |
|---|---|---|
| table-cell-qc / needs-table-visual-qc | most regression tables | status can be `strong-with-qc`, `weak`, or `needs-qc` depending on whether cell uncertainty blocks the arrow. |
| figure-qc | A027/A036 and related evidence | keep figure-dependent conclusions as `needs-qc` or `strong-with-qc`. |
| table-text-conflict | A030/E021/P7a | treat as substantive mechanism-arrow weakness until manual table-cell verification resolves it. |
| citation-qc | gap, theory, contribution, heterogeneity citations | route to external evidence/citation verification. |

## Audit Readiness

The input is sufficient for full arrow audit. Main limitations are external literature/citation verification, method-standard verification for DID/cluster/Oster/placebo, official regulatory context, and manual table/figure QC.
