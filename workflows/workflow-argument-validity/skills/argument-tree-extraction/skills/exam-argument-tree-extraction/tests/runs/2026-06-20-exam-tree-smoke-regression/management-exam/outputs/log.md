# Management Exam Smoke Regression Log

## run

- date: 2026-06-20
- mode: quick-tree smoke regression
- branch: exam / management-exam
- output files:
  - `outputs/argument-tree.md`
  - `outputs/log.md`

## allowed inputs read

1. Task contract:
   `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/exam-argument-tree-extraction/tests/runs/2026-06-20-exam-tree-smoke-regression/management-exam/task-contract.md`
2. Parent extraction Skill:
   `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/SKILL.md`
3. Exam extraction Skill:
   `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/exam-argument-tree-extraction/SKILL.md`
4. Exam tests README:
   `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/exam-argument-tree-extraction/tests/README.md`
5. Prompt input:
   `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/subworkflows/workflow-exam-argument-validity/projects/PROJECT-260619-论效案例学习/tasks/TASK02-2009-民主集中制/inputs/prompt.md`

## boundary compliance

- Did not read old outputs in the source TASK.
- Did not read reference answer files.
- Did not read previous discussion logs.
- Did not read academic paper extraction Skills.
- Did not modify unrelated files.
- Created only the two contract-specified output files.

## procedure

1. Read the task contract and confirmed the run as `quick-tree smoke regression`.
2. Read parent `argument-tree-extraction` Skill for common quick-tree direction and output discipline.
3. Read `exam-argument-tree-extraction` Skill for exam-style root claim, subclaim, arrow table, hidden assumption, candidate flaw, and writable point requirements.
4. Read exam tests README and matched the smoke checklist.
5. Read the management-exam prompt input.
6. Built a compact exam-style argument tree:
   - prompt facts / examples
   - subclaims
   - root claim
   - arrow table
   - hidden assumptions
   - candidate flaws
   - best 3-4 writable points
   - Mermaid
   - QC

## smoke checklist

| target | status |
|---|---|
| capture root claim and subclaims | pass |
| restore prompt facts/data/examples -> subclaim -> root claim | pass |
| produce arrow table | pass |
| identify hidden assumptions | pass |
| produce candidate flaws | pass |
| select best 3-4 writable points | pass |
| output can support Chinese exam essay paragraphs | pass |
| avoid academic paper variable framing | pass |
| avoid imported literature-support material | pass |
| avoid imported table or image material | pass |

## notes

The resulting tree treats the prompt as a short exam argument rather than a long-form research text. The strongest writable issues are concentrated on: false opposition between truth and majority principles, jump from minority truth to minority rule, overclaim about decision-stage unknowability, and false dilemma after rejecting one interpretation.
