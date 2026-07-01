# Task Contract

## Run

- task_id: TASK07-latest-paper-tree-regression
- mode: full-tree regression
- case: CASE-J-260110-xinyuan-review
- paper_type: empirical / quasi-experimental / DID-style Chinese management paper
- output_dir: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs`

## Must Read

- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/SKILL.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/academic-paper-main-axis.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/canonical-recursive-tree.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/claim-vs-evidence-boundary.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/empirical-paper-adapter.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/identification-design-adapter.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/obsidian-evidence-linking.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK05-PDF手稿完整Markdown还原/outputs/manuscript_restored_with_tables.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK05-PDF手稿完整Markdown还原/logs/table-visual-qc.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK05-PDF手稿完整Markdown还原/logs/restoration-qc.md`

## Must Not Read

- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/inputs/xinyuan-review.txt`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/inputs/source-review-notes.md`
- any old outputs under `TASK01`, `TASK02`, `TASK04`, or `TASK06`;
- `review-sensitivity-map.md`, `sensitivity-expanded-mermaid.md`, `academic-arrow-audit-table*`, `academic-selected-issues*`;
- previous conversation or user expectations not written in this contract.

## Required Outputs

- `outputs/academic-argument-spine.md`
- `outputs/canonical-node-ledger.md`
- `outputs/evidence-ledger.md`
- `outputs/canonical-edge-ledger.md`
- `outputs/paper-argument-tree.md`
- `outputs/recursive-tree-master.md`
- `outputs/evidence-expanded-mermaid.md`
- `outputs/obsidian-link-map.md`
- `outputs/extraction-qc.md`
- `logs/log.md`

Do not output `review-sensitivity-map.md` or `sensitivity-expanded-mermaid.md`; those belong to `academic-argument-arrow-audit`.

## Quality Requirements

- X2 must be a concrete finding, not "作者做出来了".
- Claim hierarchy is recursive, not fixed five layers.
- Evidence leaves must be minimal and source-located.
- Identification design facts must be extracted: treatment/shock, comparison group, timing, model, FE, clustering, pretrend/placebo/robustness if present.
- Citation evidence must enter `evidence-ledger.md`, or QC must mark `missing-citation-evidence`.
- Table evidence must include table number, column, variable, coefficient/statistic, significance or QC status when available.
- Edge ledger only restores author-claimed support relations; edge status can only be `not-yet-audited` or `needs-qc`.
- `evidence-expanded-mermaid.md` should prioritize completeness over readability and should draw from minimal evidence recursively to root claim as far as feasible.
- If Mermaid render limits prevent a full graph, mark `mermaid-render-limit` / `incomplete-mermaid-evidence-view` in QC and keep full structure in `recursive-tree-master.md`.
- Author tree must not include review attacks, issue selection, or sensitivity conclusions.
