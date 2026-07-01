# Exam Tree Smoke Regression 2026-06-20

## Purpose

Validate whether recent changes to the parent `argument-tree-extraction` Skill preserve the exam branch.

## Changed Skill

- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/SKILL.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/exam-argument-tree-extraction/SKILL.md`

## Regression Cases

| run | input | scenario |
|---|---|---|
| `management-exam` | `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/subworkflows/workflow-exam-argument-validity/projects/PROJECT-260619-论效案例学习/tasks/TASK02-2009-民主集中制/inputs/prompt.md` | 中文管理类论证有效性分析 |
| `gre` | `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/subworkflows/workflow-exam-argument-validity/projects/PROJECT-260619-论效案例学习/tasks/TASK10-GRE-Corpora健身/inputs/prompt.md` | GRE Analyze an Argument |

## Clean Agent Rule

The regression worker must not read old outputs, reference answers, prior discussion, or unrelated TASK files. It may read only:

- the input prompt;
- parent and exam extraction Skills;
- necessary references/assets directly required by those Skills;
- this README and the exam regression target.

## Expected Outputs

Each run should write:

- `outputs/argument-tree.md`
- `outputs/log.md`

The main agent will compare the new output with baseline/target after the clean run.
