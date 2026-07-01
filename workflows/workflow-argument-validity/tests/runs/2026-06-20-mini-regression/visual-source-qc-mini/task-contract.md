# Task Contract: Visual Source QC Mini

## Mode

```text
mode: smoke-regression
```

## Tested Skill

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-paper-writing-review/skills/scholar-pdf-markdown-restoration/SKILL.md
```

## Goal

Verify that the updated restoration Skill requires model-vision source QC for table/figure evidence.

## Inputs

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/fixtures/visual-source-qc-table11/page-19.png
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/fixtures/visual-source-qc-table11/page-20.png
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/fixtures/visual-source-qc-table11/table-11.restored.md
```

## Required Actions

1. Read the tested Skill and the fixture README.
2. Use model vision to inspect both page images.
3. Compare the visual table evidence with the restored Markdown.
4. Write `outputs/table-visual-qc.md`.
5. Write `outputs/pass-fail.md`.
6. Write `log.md`.

## Forbidden

- Do not read prior TASK05 `table-visual-qc.md`.
- Do not read TASK08/TASK09/TASK10 outputs.
- Do not use only text/OCR inference.
- Do not write `cell-level audited` unless you actually perform cell-level auditing.

## Pass Criteria

- The output explicitly says model vision was used.
- The output records image paths.
- The output distinguishes page-level visual check from cell-level audit.
- The output identifies whether the PosCAR[-10,10] / NegCAR[-10,10] significance pattern in the restored table is visually supported or needs higher-resolution/manual QC.

