---
name: task-driven-project-manager
description: Scaffold and document reproducible task-driven research or data projects. Use when the user asks to set up or standardize a project structure, split a project into TASK01/TASK02 subprojects, create a project README, add a top-level Notebook dashboard, design Makefile commands, manage a project-local .venv/Jupyter kernel, or establish TDD with red-green-refactor plus unit/e2e/UAT tests using GIVEN-WHEN-THEN Chinese comments.
---

# Task-Driven Project Manager

Use this skill to turn a medium-sized research, data, writing, or analysis task into a reproducible project workspace.

## Core Pattern

Prefer a **Task-driven architecture**:

- Keep a project-level `README.md` as the human entrypoint.
- Keep a project-level `00_project_dashboard.ipynb` as the visual control plane.
- Keep a project-level `Makefile` as the command entrypoint.
- Put shared dependencies and utility code in `common/`.
- Put tests in `tests/unit`, `tests/e2e`, `tests/uat`, and `tests/fixtures`.
- Put each stage in `tasks/TASKxx-name/`, with its own instructions, script, outputs, cache, and logs.
- Put only final deliverables in `final_outputs/`.

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
5. Add or recommend `common/requirements.txt` and a project-local `.venv`.
6. Specify that Jupyter must use the project `.venv` kernel.
7. Add `tests/` with unit/e2e/UAT layers and GIVEN-WHEN-THEN Chinese comment convention.
8. If implementing the structure, create skeleton directories and lightweight `TASKxx-说明.md` files.

## Standard Structure

Use this as the default shape, adapting names to the project:

```text
project-root/
├── README.md
├── Makefile
├── TASK-总-*.md
├── PROJECT-*.md
├── 00_project_dashboard.ipynb
├── .venv/
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

Always require the Notebook to use the project `.venv` kernel. A typical kernel display name is project-specific, for example `Python (Project Name)`.

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

Use `common/requirements.txt` as the default dependency file and `.venv/` as the default environment folder.

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

When reporting to the user, mention:

- what project files were created or updated;
- the chosen Task breakdown;
- how to initialize environment and run the dashboard;
- what human gates remain.
