# GRE Smoke Regression Log

## Task

- Run: `2026-06-20-exam-tree-smoke-regression/gre`
- Mode: quick-tree smoke regression
- Scenario: GRE Analyze an Argument
- Output file: `outputs/argument-tree.md`

## Read Boundary

Read only:

- `task-contract.md`
- parent Skill: `argument-tree-extraction/SKILL.md`
- exam Skill: `exam-argument-tree-extraction/SKILL.md`
- tests README: `exam-argument-tree-extraction/tests/README.md`
- input prompt summary: `TASK10-GRE-Corpora健身/inputs/prompt.md`

Did not read:

- old outputs in the source task
- reference answer files
- previous discussion logs
- unrelated TASK files
- academic paper extraction Skills

## Procedure

1. Confirmed task contract and output paths.
2. Read the parent extraction Skill for shared quick-tree requirements, node ledger, arrow table, Mermaid direction, and regression boundaries.
3. Read the exam extraction Skill for GRE prompt adaptation and required outputs.
4. Read the tests README for smoke target checks.
5. Read the GRE prompt summary.
6. Produced `argument-tree.md` with prompt type, root claim, support chain, node ledger, arrow table, hidden assumptions, evidence needs/questions, candidate flaws, best issue points, Mermaid, and QC.

## Prompt-Type Decision

The prompt is an assumptions prompt. The core output therefore emphasizes:

- assumption
- target arrow
- impact if false

Evidence needs and diagnostic questions are included as auxiliary GRE-compatible analysis, not as a replacement for the assumptions structure.

## Regression Smoke Result

| target | result |
|---|---|
| Identify GRE prompt type | pass |
| Capture root claim and support chain | pass |
| Produce arrow table | pass |
| Identify assumptions/questions/evidence needs | pass |
| Produce candidate flaws | pass |
| Select best 3-4 issue points | pass |
| Include Mermaid | pass |
| Include QC | pass |
| Avoid Chinese essay-only template | pass |
| Avoid academic-paper analysis frame | pass |

## Notes

- This is a quick-tree smoke output, not a full-tree evidence-ledger run.
- Evidence nodes are prompt-summary based and marked as summarized, consistent with the available input.
- No comparison against old outputs or reference answers was performed because the contract forbids reading them.
