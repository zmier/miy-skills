# Regression Comparison

## test_id

`2026-06-20-exam-tree-smoke-regression`

## changed_skill

- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/SKILL.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/exam-argument-tree-extraction/SKILL.md`

## outputs

| run | new_output | baseline_output | pass_fail |
|---|---|---|---|
| management-exam | `management-exam/outputs/argument-tree.md` | `PROJECT-260619-论效案例学习/tasks/TASK02-2009-民主集中制` proxy to `CASE-FEEDBACK-260619-2009-民主集中制/outputs/argument-tree.md` | pass |
| gre | `gre/outputs/argument-tree.md` | `PROJECT-260619-论效案例学习/tasks/TASK10-GRE-Corpora健身/outputs/argument-tree.md` and `outputs/UAT.md` | pass |

## expected_improvement

Recent parent Skill changes should preserve the exam branch while preventing academic full-tree concepts from leaking into exam extraction.

Expected behavior:

- quick-tree rather than academic full-tree;
- root claim and subclaims captured;
- prompt facts/data/examples restored into a compact support tree;
- arrow table, hidden assumptions, candidate flaws, and best issue points present;
- GRE prompt instruction recognized;
- no academic paper `X1/X2/Y`, citation evidence, table evidence, or figure evidence.

## observed_improvement

### Management Exam

The new output preserves the original blind-run's main strengths:

- captures the same root claim: `集中` should mean concentrating the majority's opinions rather than correct opinions;
- recovers the same major subclaims: self-contradiction, minority rule, decision-stage unknowability, and exclusion of the rival interpretation;
- produces a clear Mermaid tree and arrow table;
- selects 4 writable points suitable for Chinese argument-validity essay paragraphs.

It also improves on one known baseline gap. The old reference comparison noted that the previous blind-run did not sufficiently capture the point that if both `民主` and `集中` are reduced to majority opinion, the two basic points collapse into one. The new output includes this as:

> 民主和集中是两个基本点，不能因为民主含多数原则就把集中也化约为多数原则。

This is a real improvement and shows that the exam branch has retained the later "definition substitution / concept relation" upgrade.

### GRE

The new GRE output preserves the prior TASK10 UAT target:

- identifies the prompt as an assumptions prompt;
- organizes assumptions by `assumption -> target_arrow -> impact_if_false`;
- captures the standard core issues: standards comparability, computer ownership as proxy, regional confounding, low fitness spending as causal evidence, and unsupported prediction from recovery to fitness;
- includes evidence needs and diagnostic questions as auxiliary GRE-compatible analysis;
- avoids a Chinese exam essay-only template.

Compared with the baseline, the new output is slightly more structured because it includes a node ledger, arrow table, assumption-impact table, evidence/questions table, candidate flaws, best issue points, Mermaid, and QC in one file.

## observed_regression

No critical regression observed.

Minor caveats:

- Both runs are smoke regression, not strict blind forward tests.
- The GRE input is a prompt summary from a prior assisted calibration case, so this validates branch stability, not unseen GRE generalization.
- The management output includes more structure than a timed exam draft would need, but it remains quick-tree sized and does not drift into academic full-tree evidence-ledger mode.

## contamination_check

| contamination risk | management-exam | gre | result |
|---|---|---|---|
| academic `X1/X2/Y` frame | absent | absent | pass |
| citation evidence | absent | absent | pass |
| table/figure evidence | absent | absent | pass |
| academic paper full-tree bloat | absent | absent | pass |
| GRE reduced to Chinese essay template | n/a | absent | pass |

## pass_fail

`pass / no-regression-observed`

## next_action

1. Record this run in the exam extraction Skill regression log if repeated again.
2. Later add one unseen management-exam prompt and one unseen GRE prompt as stable fixtures under `tests/fixtures/`.
3. Keep the current parent/child split: parent provides quick/full tree discipline and routing; exam child preserves short-material extraction and prompt-type adaptation.
