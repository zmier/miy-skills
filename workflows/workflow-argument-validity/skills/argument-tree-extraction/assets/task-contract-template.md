# Task Contract Template

## Task

- task_id:
- project:
- mode: `quick-tree` / `full-tree`
- text_type: academic paper / exam argument / GRE argument / policy report / other
- output_dir:

## Inputs

- primary_text:
- restored_markdown:
- tables:
- figures:
- visual_qc:
- prior_outputs_allowed:
- prior_outputs_forbidden:

## Boundary

- author tree only: yes / no
- arrow-audit handoff hints allowed: yes / no
- review sensitivity allowed: no by default; only `academic-argument-arrow-audit` should generate `review-sensitivity-map.md`
- final review writing allowed: yes / no
- forbidden materials:

## Main Axis

- [ ] 0 `task-contract.md`
- [ ] 1 `argument-spine.md`
- [ ] 2 `canonical-node-ledger.md`
- [ ] 3 `evidence-ledger.md`
- [ ] 4 `canonical-edge-ledger.md`
- [ ] 5 `recursive-tree-master.md` / `evidence-expanded-mermaid.md`
- [ ] 6 handoff hints in `extraction-qc.md`
- [ ] 7 `extraction-qc.md`

## Evidence Requirements

- [ ] text evidence
- [ ] table-cell evidence
- [ ] figure evidence
- [ ] definition evidence
- [ ] sample-rule evidence
- [ ] model-spec evidence
- [ ] citation evidence

## Completion Rules

- Cannot claim full-tree if canonical ledgers are missing.
- Cannot claim recursive tree if abstract evidence leaves remain.
- Cannot claim table/figure verified if visual QC is missing.
- Cannot claim citation coverage if single-paper citation evidence is missing.
