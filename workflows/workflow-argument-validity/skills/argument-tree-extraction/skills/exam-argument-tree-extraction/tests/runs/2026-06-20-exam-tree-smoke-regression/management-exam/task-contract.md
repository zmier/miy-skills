# Task Contract: Management Exam Smoke

## Mode

quick-tree smoke regression.

## Scenario

中文管理类论证有效性分析题。

## Input

`/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/subworkflows/workflow-exam-argument-validity/projects/PROJECT-260619-论效案例学习/tasks/TASK02-2009-民主集中制/inputs/prompt.md`

## Must Read

- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/SKILL.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/exam-argument-tree-extraction/SKILL.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/exam-argument-tree-extraction/tests/README.md`

## Must Not Read

- old outputs in the source TASK;
- reference answer files;
- previous discussion logs;
- academic paper extraction Skills.

## Output

Write:

- `outputs/argument-tree.md`
- `outputs/log.md`

## Smoke Target

- capture root claim and subclaims;
- restore prompt facts/data/examples -> subclaim -> root claim;
- produce an arrow table;
- identify hidden assumptions;
- produce candidate flaws;
- select best 3-4 writable points;
- avoid academic paper `X1/X2/Y`, citation evidence, table/figure evidence.
