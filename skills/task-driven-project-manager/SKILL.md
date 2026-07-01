---
name: task-driven-project-manager
description: Scaffold and document reproducible task-driven research or data projects. Use when the user asks to set up or standardize a project structure, split a project into TASK01/TASK02 subprojects, create a project README, add a top-level Notebook dashboard, design Makefile commands, manage a project-local .venv/Jupyter kernel, or establish TDD with red-green-refactor plus unit/e2e/UAT tests using GIVEN-WHEN-THEN Chinese comments.
---

# Task-Driven Project Manager

Use this skill to turn a medium-sized research, data, writing, or analysis task into a reproducible project workspace.

## Relationship To Workflow

This Skill is the scaffold and project-structure execution unit. For long exploratory projects that need nested TASKs, evidence ledgers, ReAct logs, phase reviews, Obsidian double-link maps, forward tests, or workflow/skill feedback, use the parent workflow:

```text
Writer/00 信息/miy-skills/workflows/workflow-task-driven-project/
```

Rule of thumb:

```text
Need folders, README, Makefile, tests -> this Skill.
Need project evolution, evidence governance, phase review, skill feedback -> workflow-task-driven-project.
```

## Core Pattern

Prefer a **Task-driven architecture**:

- Keep a project-level `README.md` as the human entrypoint.
- Keep a project-level `00_project_dashboard.ipynb` as the visual control plane.
- Keep a project-level `Makefile` as the command entrypoint.
- Put shared dependencies and utility code in `common/`.
- Put tests in `tests/unit`, `tests/e2e`, `tests/uat`, and `tests/fixtures`.
- Put each stage in `tasks/TASKxx-name/`, with its own instructions, script, outputs, cache, and logs.
- Put only final deliverables in `final_outputs/`.
- For long exploratory projects, keep project-level phase reviews in `final_outputs/` and use Obsidian `[[...]]` links to connect them back to TASK evidence, logs, outputs, and reusable workflow/skill updates.

Use type-based folders such as `scripts/`, `outputs/`, and `docs/` only for cross-cutting or legacy material. The main workflow should be visible from the `tasks/` tree.

## Workflow

1. Read the user's current task, existing notes, and project files.
2. Identify 4-8 concrete Tasks. Keep them sequential when there are true dependencies; mark safe parallel work clearly.
3. Create or update the project `README.md` with:
   - background and goal;
   - key data/source paths;
   - Task-driven folder structure;
   - Notebook dashboard role;
   - Makefile/environment commands;
   - TDD and test policy;
   - expected final outputs.
4. Add a `Makefile` when the project needs repeatable commands.
5. Add or recommend `common/requirements.txt` and a project-local `.venv` by default.
   - If the user or workspace specifies a shared environment, use that explicit environment instead of creating a project-local `.venv`.
   - If new packages need to be installed, declare them in the current project's `pyproject.toml` before installation. Keep project-specific dependency intent in the project, even when using a shared workspace venv.
6. Specify that Jupyter must use the selected environment's kernel, either the project `.venv` kernel or the user-specified shared venv kernel.
7. Add `tests/` with unit/e2e/UAT layers and GIVEN-WHEN-THEN Chinese comment convention.
8. If implementing the structure, create skeleton directories and lightweight `TASKxx-说明.md` files.
9. For exploratory or long-running projects, add an evidence and review layer:
   - each major TASK keeps `logs/log.md` or `logs/LOG.md` with ReAct-style decisions;
   - important outputs get stable Markdown summaries, not only raw JSON/SQLite;
   - project-level `final_outputs/*复盘.md` documents connect phases with Obsidian double links;
   - reusable methods are explicitly listed as workflow/skill feedback candidates.

## Standard Structure

Use this as the default shape, adapting names to the project:

```text
project-root/
├── README.md
├── Makefile
├── TASK-总-*.md
├── PROJECT-*.md
├── 00_project_dashboard.ipynb
├── .venv/                     # optional when using a project-local venv
├── pyproject.toml             # required before adding/installing project-specific packages
├── common/
│   ├── requirements.txt
│   ├── README.md
│   ├── paths.py
│   └── text_cleaning.py
├── tests/
│   ├── unit/
│   ├── e2e/
│   ├── uat/
│   └── fixtures/
├── tasks/
│   ├── TASK01-name/
│   │   ├── TASK01-说明.md
│   │   ├── run.py
│   │   ├── outputs/
│   │   ├── cache/
│   │   └── logs/
│   └── TASK02-name/
├── final_outputs/
├── scripts/
│   └── legacy_or_experimental/
└── docs/
```

Read `references/templates.md` when you need copyable README, Task, Makefile, or test templates.

## Exploratory Project Evolution

For projects where the next task is discovered through evidence, do not force all Tasks to be known upfront. Use a stable top-level task tree plus nested subtasks when a single large task naturally becomes a workstream.

Recommended pattern:

```text
tasks/
├── TASK01-problem-framing/
├── TASK02-baseline/
├── TASK03-first-green/
├── TASKxx-major-workstream/
│   ├── TASKxx-说明.md
│   ├── logs/
│   │   └── log.md
│   ├── docs/
│   ├── outputs/
│   └── subtasks/
│       ├── TASKxx-01-subproblem/
│       ├── TASKxx-02-code-engineering/
│       └── TASKxx-03-limit-or-risk-investigation/
└── TASKyy-workflow-feedback/
```

Use subtasks when:

- the work is part of the same business objective;
- the parent task owns the state machine, database, queue, or main artifact;
- splitting into a new top-level task would hide the main storyline.

Create a new top-level task when:

- the goal, artifact, or acceptance contract changes;
- a new external system, data source, or workflow route becomes central;
- the result should be understandable without the parent task context.

For exploratory work, task IDs are not required to be perfectly sequential. Preserve historical IDs rather than renumbering. Add README/status tables so humans can navigate the history.

## Task Folder Rules

Each `tasks/TASKxx-name/` folder should answer:

- What does this Task do?
- What upstream files or Tasks does it depend on?
- What command runs it?
- What files does it produce?
- What counts as done?
- Does it require human review?

Use this internal layout by default:

```text
TASKxx-name/
├── TASKxx-说明.md
├── run.py
├── inputs/
├── outputs/
├── cache/
└── logs/
```

For pure manual review Tasks, replace `run.py` with `manual_review.md`.

For research or reverse-engineering style Tasks, prefer:

```text
TASKxx-name/
├── TASKxx-说明.md
├── README.md                 # optional human entrypoint for large tasks
├── acceptance-contract.md    # optional UAT / route boundary
├── request-or-evidence-ledger.md
├── docs/
├── scripts/
├── agent/
├── inputs/
├── outputs/
├── cache/
├── logs/
│   └── log.md
└── subtasks/
```

Each `logs/log.md` should use a lightweight ReAct rhythm:

```markdown
## YYYY-MM-DD HH:mm ReAct：标题

### Thought
当前判断、假设和为什么要做这一步。

### Action
实际命令、人工动作、脚本、参数、保存路径。

### Observation
结果、错误、证据文件、关键数字。

### Reflection
结论、边界、下一步、是否反哺 workflow/skill。
```

Do not rely only on terminal output. Important observations should be promoted into Markdown summaries under `outputs/` or `docs/` so they can be linked later.

## Notebook Dashboard

The top-level `00_project_dashboard.ipynb` is a control plane, not the main implementation. It should:

- summarize project background;
- show Task status;
- render flowcharts or Mermaid diagrams;
- check paths and environment;
- call `tasks/TASKxx-*/run.py`;
- preview key tables/outputs;
- stop at human-review gates;
- point to final outputs.

Always require the Notebook to use the selected project environment kernel. By default this is the project `.venv`; when the user specifies a shared workspace venv, use that shared venv and document the absolute interpreter path. A typical kernel display name is project-specific, for example `Python (Project Name)`.

## Makefile

Add a Makefile for repeatable commands when the project has scripts, tests, or a Notebook. Include targets like:

- `make init`
- `make install`
- `make kernel`
- `make notebook`
- `make test`
- `make test-unit`
- `make test-e2e`
- `make test-uat`
- `make freeze`

Use `common/requirements.txt` as the lightweight default dependency file and `.venv/` as the default environment folder. If project-specific packages will be installed, create or update `pyproject.toml` in the current project first, then install from that declared dependency set. If the user specifies a shared venv, point Makefile variables at that explicit venv instead of creating another one.

## TDD and Testing

Require TDD for implementation-heavy Tasks:

1. **Red**: write a failing test first.
2. **Green**: implement the smallest code that passes.
3. **Refactor**: clean the implementation while tests remain green.

Use three test layers:

- **unit**: functions and edge cases.
- **e2e**: small fixture data through multiple Tasks.
- **UAT**: researcher/user acceptance checks on output shape, naming, deliverability, and manual-review records.

Use Chinese GIVEN-WHEN-THEN comments in tests:

```python
def test_parse_standard_filename():
    # GIVEN：一个符合项目命名规则的文件名
    filename = "600519_2021.txt"

    # WHEN：解析文件名
    result = parse_filename(filename)

    # THEN：应返回正确的业务标识和年份
    assert result.code == "600519"
    assert result.year == 2021
```

## Output Discipline

Keep intermediate results inside each Task. Copy or export only reviewed final deliverables to `final_outputs/`.

Use this distinction:

- `tasks/TASKxx/outputs/`: evidence, raw/simplified outputs, batch summaries, reports for one task.
- `tasks/TASKxx/docs/`: task-local explanation, runbooks, decision notes, manual protocols.
- `docs/`: cross-cutting project references, Q&A, decision trees, conceptual explanations.
- `final_outputs/`: reviewed deliverables, phase reviews, final reports, project-level maps.

For Obsidian-friendly projects:

- Use `[[relative/path/to/doc|label]]` links in review documents.
- Link to specific evidence reports, not only to task folders.
- Prefer one project-level map/review in `final_outputs/` after each major phase.
- Keep raw sensitive data out of Markdown; link to sanitized summaries instead.

## Project Reviews and Skill Feedback

Long projects should produce review documents at phase boundaries:

```text
final_outputs/
├── Phase-1-*.md
├── Phase-2-*.md
└── Project-完整历程复盘.md
```

A good project review should include:

- the original question and how it changed;
- a phase-by-phase timeline;
- key Red -> Green transitions;
- evidence links using Obsidian double links;
- data and coverage boundaries;
- engineering pitfalls and recovery patterns;
- what should be generalized into a workflow, skill, template, or runbook.

When a project teaches a reusable method, add a `workflow/skill feedback` section either in the review document or a dedicated TASK. The feedback should say:

```text
Where did this rule come from?
What evidence supports it?
Which workflow/skill should receive it?
What should remain only in the TASK as case evidence?
```

When reporting to the user, mention:

- what project files were created or updated;
- the chosen Task breakdown;
- how to initialize environment and run the dashboard;
- what human gates remain.
