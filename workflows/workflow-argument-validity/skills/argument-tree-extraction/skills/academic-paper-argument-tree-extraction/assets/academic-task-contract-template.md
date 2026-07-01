# Academic Argument Tree Task Contract

## Task

- task_id:
- project:
- paper_title:
- mode: `quick-tree` / `full-tree`
- paper_type: empirical / theory-model / conceptual-review / unclear
- output_dir:

## Inputs

- restored_manuscript:
- table_dir:
- figure_dir:
- visual_qc_logs:
- prior_task_outputs_allowed:
- prior_task_outputs_forbidden:
- review_materials_forbidden_for_author_tree:

## Boundary

- 2A author tree only uses manuscript evidence: yes / no
- sensitivity mapping belongs to academic-arrow-audit: yes
- final review writing allowed: no by default
- forbidden materials:

## Academic Main Axis

- [ ] 0 `task-contract.md`
- [ ] 1 `academic-argument-spine.md`
- [ ] 2 `canonical-node-ledger.md`
- [ ] 3 `evidence-ledger.md`
- [ ] 4 citation / table / figure evidence completion
- [ ] 5 `canonical-edge-ledger.md`
- [ ] 6 `recursive-tree-master.md` / `evidence-expanded-mermaid.md` / `obsidian-link-map.md`
- [ ] 7 `extraction-qc.md`

## Required Evidence Classes

- [ ] text evidence
- [ ] variable / construct evidence
- [ ] sample-rule evidence
- [ ] model-spec evidence
- [ ] table-cell evidence
- [ ] figure evidence
- [ ] citation evidence
- [ ] policy / institutional evidence

## Red Lines

- Cannot claim full-tree if citation evidence is missing without QC flag.
- Cannot claim table evidence verified without visual QC.
- Cannot mix review sensitivity, arrow audit, or review attacks into author tree.
- Cannot generate Mermaid by inventing nodes outside ledger.
