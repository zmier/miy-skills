---
name: miy-venv
description: Python 虚拟环境与依赖治理 Skill。用于扫描和治理 .venv 分布、判断哪些环境应保留/迁移/删除、补齐 pyproject.toml 或 requirements.txt、规划 uv/pip/poetry 使用边界、收敛项目内部阶段环境、维护根环境/项目环境/Skill 环境/submodule 环境规则。适用于用户要求“治理 .venv”“Python 环境治理”“依赖收敛”“requirements 怎么规划”“写 pyproject.toml”“删除虚拟环境前先评估”“uv/poetry/pip 怎么选”等场景。
---

# Miy Venv

Use this Skill to turn scattered Python virtual environments into a clear, reproducible environment system. Prefer declared dependencies over preserved `.venv` folders, and treat each environment as an architecture decision rather than a temporary convenience.

## Core Rules

- Inspect before acting: scan `.venv` recursively, record path, size, nearest `pyproject.toml` / `requirements.txt` / `Makefile` / README, and whether the directory is a Git repo or submodule.
- Do not delete `.venv` folders until their dependency source and replacement command are documented and verified.
- Judge by architecture identity before physical path. A directory under `02 Sources/` can still be an independent engineering project; a directory under `03 Projects/` can still be only a temporary stage.
- `.venv` is never the dependency source of truth. The source of truth should be `pyproject.toml`, `requirements.txt`, lock files, and documented commands.
- Prefer one environment per architecture boundary: Writer root, reusable Skill/tool, project root, app, or independent submodule.
- Project-internal stage folders should reuse the project root environment unless they have conflicting dependencies or are becoming standalone projects.
- Keep environment governance separate from Git cleanup: changing `.gitignore` is allowed, but removing tracked files or committing should follow `$miy-git`.

## Allowed Environment Identities

Use this classification before deciding whether a `.venv` is valid.

- `root-env`: `Writer/.venv`
  - Serves the Writer repository, daily scripts, document processing, shared lightweight tools, and non-isolated tasks.
- `skill-env`: reusable Skill or tool capability
  - Examples: `.pytools/**/skills/**/.venv`, long-lived tool folders, citation/review automation kits.
  - Allowed because Skills must work across projects and can have specialized dependencies.
- `project-env`: `03 Projects/<project>/.venv`
  - Serves an independent research/data/software project.
  - The environment should live at project root, not in every internal phase.
- `submodule-env`: independent Git submodule or standalone engineering repo
  - Allowed even if physically located under `02 Sources/` or `99 Assets/`.
  - Example pattern: data collection systems, apps, stock/quant tools, crawlers, reusable libraries.
- `app-env`: app/tool product with its own runtime
  - Allowed when the directory is a maintained application or package, not a one-off asset folder.

Default invalid identities:

- `source-material`: ordinary `02 Sources/**` documents or datasets.
- `archive-task`: archived review, citation, or one-off conversion tasks.
- `asset-folder`: ordinary `99 Assets/**` papers, PDFs, exports, and media.
- `project-stage`: `Codes/**`, `Docs/**`, `修稿/**`, `实验子任务/**` inside one larger project.
- `temporary-script`: one-off scripts or single-paragraph repair folders.

## Dependency Source Policy

Prefer dependency declaration in this order:

1. `pyproject.toml`
   - Use for long-lived projects, reusable tools, Skills, apps, packages, and submodules.
   - Use optional dependency groups such as `doc`, `pdf`, `browser`, `data`, `plotting`, `dev`, or `all`.
2. `requirements.txt`
   - Use for small scripts, legacy pip compatibility, or a narrow one-off task.
   - If the task is becoming long-lived, migrate to `pyproject.toml`.
3. lock files
   - Keep `uv.lock`, `poetry.lock`, or pinned requirements when reproducibility matters.
   - Do not invent a lock file unless the project’s toolchain actually uses it.
4. `.venv`
   - Runtime artifact only. Never treat it as the only record of dependencies.

For an existing orphan `.venv` with no declaration:

1. Inspect installed top-level packages using that environment’s Python.
2. Identify what local scripts import.
3. Write a minimal dependency declaration.
4. Verify dependency resolution.
5. Only then propose deletion.

## Tool Choice

- `uv`: preferred default for new lightweight governance work when available. Use for fast venv creation, dependency syncing, and lock-aware installs.
- `pip`: acceptable for simple compatibility and dry-run checks inside an existing venv.
- `poetry`: use only when the project already uses Poetry or needs its packaging workflow.
- `conda`: do not introduce unless binary/scientific stack constraints require it or the project already uses it.

Do not mix tools casually. If a project has chosen `uv`, keep using `uv`. If it has chosen Poetry, do not silently convert it.

## Standard Workflow

1. Map environment state:
   - recursively list `.venv` folders;
   - collect size with `du -sh`;
   - detect nearest dependency declaration;
   - detect Git boundaries and submodules;
   - identify Python version and key installed packages when needed.
2. Classify each environment:
   - `keep`: valid architecture boundary and dependency source exists;
   - `migrate`: valid code/task but `.venv` is at the wrong level or dependencies are undeclared;
   - `delete-candidate`: temporary/archive/stage environment with dependency source now covered elsewhere;
   - `needs-decision`: ambiguous project identity, possible app/submodule, secrets, large local data, or risky dependency conflicts.
3. Design the target layout:
   - root environment for shared Writer utilities;
   - project root environment for each independent project;
   - Skill/app/submodule environments only at their own root;
   - no nested `.venv` inside project stages unless justified.
4. Add or update dependency declarations:
   - prefer `pyproject.toml` for maintained code;
   - use optional groups to absorb stage-specific dependencies;
   - keep `requirements.txt` only as compatibility when useful;
   - document install commands in README, ENVIRONMENT.md, or Makefile.
5. Verify before deletion:
   - run `pip install --dry-run -e .` or equivalent when safe;
   - for real migrations, create/sync the target environment and run `pip check`;
   - run representative tests, imports, or smoke commands.
6. Delete only after user confirmation:
   - summarize exact paths and expected space savings;
   - confirm replacement commands;
   - remove `.venv` folders explicitly, never via broad `find ... -delete`;
   - rescan to verify counts.
7. Record outcome:
   - update governance docs;
   - update `.gitignore` / pre-commit rules if needed;
   - report remaining valid environments and unresolved decisions.

## Writer Repository Policy

For this Writer/alib workspace, use the following baseline unless the user updates the policy:

- `Writer/.venv`: allowed root environment.
- `skills/**/.venv` and `.pytools/**/skills/**/.venv`: allowed for reusable Skills/tools when dependencies are declared.
- `03 Projects/<project>/.venv`: allowed at project root, especially when the project may become a Git submodule.
- `02 Sources/SMK/.venv`: allowed because SMK is an independent stock/data engineering submodule, not ordinary source material.
- `99 Assets/Apps/**/.venv`: allowed only for real apps/tools with dependency declarations.
- Archive folders, PDF reading folders, one-off citation checks, and project-internal stage directories should not keep long-term `.venv` folders.

Current reference documents:

- `00 信息/README_Python环境与依赖治理.md`
- `00 信息/知识管理/J-260607-Python虚拟环境治理清单.md`

Use these as background context, but report the current filesystem state freshly before taking action.

## Deletion Protocol

Use this when the user asks whether `.venv` folders can be removed.

1. Produce a table with:
   - path;
   - size;
   - identity classification;
   - dependency source;
   - replacement command;
   - recommendation.
2. Mark deletion candidates, but do not delete yet unless the user explicitly asks to proceed.
3. Before deleting:
   - ensure `.venv/` is ignored;
   - ensure no active process is using the environment;
   - ensure replacement environment has been tested or the task is archival;
   - preserve or create `pyproject.toml`, `requirements.txt`, README, or Makefile instructions.
4. Delete exact paths only.
5. Rescan and report:
   - before count and size;
   - after count and size;
   - remaining environments and why they remain.

## Red Flags

Stop and ask before continuing when:

- a `.venv` belongs to an active submodule or app whose ownership is unclear;
- dependencies cannot be inferred from scripts or installed packages;
- migration would require changing many imports, entrypoints, or notebooks;
- compiled/native packages may depend on a specific Python version or system library;
- the environment may contain local credentials, cookies, browser profiles, tokens, or private datasets;
- deleting would affect a running service, crawler, notebook server, or GUI app;
- the requested cleanup overlaps unrelated user changes or Git operations.

## Testing and Verification

Use the lightest reliable verification for the risk level:

- `syntax`: inspect declarations, run TOML parse checks.
- `dry-run`: dependency resolver can resolve packages without installing.
- `sync/install`: create or update the target venv.
- `pip check`: installed packages are internally consistent.
- `import smoke`: import key packages used by scripts.
- `unit/e2e`: run project tests when they exist.
- `manual UAT`: run the actual command or notebook the user depends on.

For project-wide migrations, require at least `pip check` plus representative imports or tests before deleting source environments.

## Reporting

Final reports should include:

- environment count and size before/after;
- which `.venv` folders were kept, migrated, or deleted;
- dependency declarations created or changed;
- verification commands and results;
- any environments intentionally left unresolved;
- exact next commands the user can run, such as `make install`, `uv sync`, or `.venv/bin/python -m pip install -e ".[all]"`.
