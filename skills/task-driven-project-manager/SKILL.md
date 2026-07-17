---
name: task-driven-project-manager
description: Scaffold and document reproducible task-driven research or data projects across execution, governance, and optional external-interface layers. Use when the user asks to standardize a project structure, split work into TASK01/TASK02 subprojects, create standing TASK00 governance, add Roadmap/lineage/change maps, connect external notices and approval gates through a Timeline-Ex layer, add a Notebook dashboard or Makefile, manage a project environment, or establish unit/e2e/UAT testing and acceptance contracts.
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
Need cross-TASK route comparison and next-workstream arbitration -> use the standing TASK00 governance pattern from this Skill, with the parent workflow owning the portfolio gate.
Need external notices, obligations, eligibility gates, reviews or approvals on a real time axis -> use $timeline-ex as the external-interface layer.
```

Skill feedback provenance:

```text
references/source-provenance.md
```

## Core Pattern

### Three-Layer Project Model

Treat task-driven project management as three separable layers:

| Layer | Core question | Primary artifacts |
|---|---|---|
| Execution | What internal work produces the deliverable? | `tasks/TASKxx-*`, scripts, evidence, outputs, tests |
| Governance | Why does this route receive work, and how are changes accepted? | root README, Roadmap, lineage/change maps, TASK00, decision and ReAct logs |
| External Interface | When and under what outside conditions may the project enter the next state? | `$timeline-ex`, EVT/OBL/GATE/OUT nodes, notices, Gate register, calendar/reminder projections |

Do not materialize every layer as a large folder tree. The three layers are a reasoning model:

- small linear projects may need only Execution plus a compact README;
- exploratory multi-TASK projects usually need Governance;
- activate External Interface only when an outside authority, deadline window, submission obligation, review, approval or result changes eligibility or route;
- learning indexes, reading projects and lightweight knowledge maps do not automatically require TASK folders, Makefile, tests or TASK00.

Keep ownership separate:

```text
$roadmap    owns internal route narrative and cross-level visual navigation.
$timeline-ex owns time-scaled external lifecycle and notice-driven state change.
TASKs       own internal evidence and deliverables that prepare for external Gates.
```

An external Gate is not a TASK. Link them explicitly:

```text
TASK：准备送审材料
  -- produces-evidence-for -->
GATE：外部盲审
```

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

For multi-task or exploratory projects, use the general `$roadmap` Skill as the visual navigation layer. `task-driven-project-manager` owns folder structure, logs, evidence ledgers, tests, and acceptance rules; `$roadmap` owns the cross-level visual grammar for Project Roadmap, Task Lineage Map, Project Change Map, click links, Kanban-style status, and stable Mermaid styling.

When the project has a persistent external lifecycle, use `$timeline-ex` beside `$roadmap`. Keep Roadmap compact and internal; route external chronology, authority, eligibility, time certainty, obligations and pass/fail branches to `docs/external-timeline/`.

## Workflow

1. Read the user's current task, existing notes, and project files.
2. Identify 4-8 concrete Tasks. Keep them sequential when there are true dependencies; mark safe parallel work clearly.
3. Create or update the project `README.md` with:
   - background and goal;
   - key data/source paths;
   - a project roadmap when the project has multiple phases, uncertain next steps, or non-linear branches;
   - Task-driven folder structure;
   - a link to the default task lineage map when the project has multiple tasks or nested subtasks;
   - Notebook dashboard role;
   - Makefile/environment commands;
   - TDD and test policy;
   - expected final outputs.
   - when several completed/active TASKs leave competing workstreams, keep the root roadmap compact and route detailed portfolio review to a standing `TASK00-project-governance/`.
   - when external gates are activated, link the Timeline-Ex HTML main view and explain its boundary from the internal Roadmap.
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
   - create or update a default task lineage map so the task tree is visible as a graph, not only as folders;
   - project-level `final_outputs/*复盘.md` documents connect phases with Obsidian double links;
   - when task structure changes because new evidence changes scope, create a project change map with task lineage, change path, migration table, and stable links;
   - reusable methods are explicitly listed as workflow/skill feedback candidates.
10. If external notices or authorities control eligibility, add the External Interface layer with `$timeline-ex`:
   - preserve important notices as append-only EVT records;
   - derive OBL/GATE/OUT nodes without inventing exact dates;
   - map each affected TASK to the Gate it prepares for;
   - update the project Roadmap, next actions and logs when external state changes.

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
│   ├── TASK00-project-governance/    # optional standing control plane for complex exploratory projects
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
    ├── task-lineage-map.md      # default Mermaid task tree/navigation map for multi-task projects
    └── external-timeline/       # optional; activate only for persistent external lifecycle
        ├── index.html           # Timeline-Ex main view
        ├── timeline-data.js     # structured external state
        └── nodes/               # EVT / OBL / GATE / OUT evidence records
```

Read `references/templates.md` when you need copyable README, Task, Makefile, or test templates.

## External Interface / Timeline-Ex

Activate `$timeline-ex` when multiple external nodes form a lifecycle, not for a single ordinary deadline.

Typical triggers:

- a notice creates or changes several future dates or Gate conditions;
- participation or approval at one Gate unlocks the next;
- failure, rejection or missing a window changes the project batch or route;
- external state affects more than one TASK;
- collaborators need one place to see authority, source, time certainty and residual unknowns.

Default relationship:

```text
Roadmap node -- prepared by --> TASK
TASK -- produces evidence for --> External Gate
External Gate -- pass/fail --> next Gate or Outcome
New EVT -- updates/supersedes --> existing external nodes
```

Keep the detailed node contract, HTML architecture, time certainty and append-only update protocol inside `$timeline-ex`. This Skill only decides whether the layer is needed, where it sits, and how TASK/Governance artifacts link to it.

Do not create `TASK00` merely to store a timeline. TASK00 compares internal workstreams and owns governance decisions; Timeline-Ex tracks outside state transitions. A complex project may use both, but neither substitutes for the other.

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

## Standing TASK00 Project Governance

When a project changes from “execute the next known task” to “compare several evidence-backed workstreams before deciding what deserves the next task,” create a standing project-governance control plane.

Use this pattern when several of the following are true:

- multiple top-level TASKs have produced accepted, diagnostic, held, or archived evidence;
- the root README is overloaded with detailed status, evidence, and decision history;
- the next action is not a natural sequence and requires comparing competing workstreams;
- opening another substantive TASK would hide the fact that the immediate job is portfolio review;
- collaborators need one place to see why a route was continued, monitored, held, or archived.

Do not create TASK00 for a small linear project, a single parent TASK with ordinary subtasks, or a one-off status report.

Default to `tasks/TASK00-project-governance/` in numbered projects. Treat it as a governance sibling, not the evidence-owning parent of TASK01+. Keep the root README compact; keep detailed TASK files as source of truth; use TASK00 for registry, workstream portfolio, append-only reviews, decision log, bidirectional navigation, and the `continue / diagnostic / monitor / hold / archive` gate.

Read `references/standing-project-governance.md` for the full protocol and `assets/standing-task00-governance-template.md` for a copyable scaffold. Use `$roadmap` for all Mermaid grammar and visual status semantics.

When TASK00 uses a research seminar to promote one competing route into a substantive TASK, apply the `Evidence-Gated Route Promotion` closeout in `references/standing-project-governance.md`. The research-side lifecycle is owned by `workflow-research/references/evidence-gated-route-adjudication.md`; this Skill owns the promoted TASK scaffold, frozen protocol, protocol-conformance tests, parent acceptance and append-only correction record.

## Default Task Lineage Map

For multi-task projects, keep a default task lineage map even before any major restructure happens.

Use `$roadmap` for the diagram grammar when creating or revising lineage maps: stepped arrows, stable node shapes, `done` / `active` / `planned` / `archived` / `blocked` classes, click links, emoji as second signal, and Markdown fallback link tables. Keep this Skill focused on what the tasks mean and where they live.

Use this by default when:

- the project has more than one `TASKxx-*`;
- a parent task has nested subtasks;
- subagents or parallel workers create separate local workstreams;
- the project is exploratory and later tasks may be discovered through evidence;
- the user or future collaborator will need a visual entrypoint.

Recommended artifact:

```text
docs/task-lineage-map.md
```

For a large single parent task, a task-local lineage map is also acceptable:

```text
tasks/TASKxx-name/outputs/taskxx-task-lineage-map.md
```

Include:

- a Mermaid task lineage graph showing project root, major tasks, nested subtasks, and likely next gates;
- key status/date labels on graph nodes, such as `opened`, `active`, `accepted`, `blocked`, `frozen`, or `next`;
- `click` links in Mermaid nodes when the target renderer supports them;
- a Markdown fallback link table because Mermaid click support varies across renderers;
- a compact task status table if the graph alone cannot express state.

Do not treat the default lineage map as a heavy deliverable. It is a navigation surface. Update it when adding, freezing, accepting, or restructuring tasks.

## Project Roadmap / Visual Navigation

For projects with more than one meaningful phase, add a project-level roadmap in the root `README.md` or `docs/project-roadmap.md`.

Use this when:

- tasks are not just sequential steps but represent evolving project understanding;
- a new result or data constraint creates a new branch;
- collaborators need one visual entrypoint before reading task folders;
- there are active, planned, blocked, archived, or superseded workstreams;
- a project has both task lineage and project change maps.

Default split:

```text
Project Roadmap = why the project is moving this way.
Task Lineage Map = how task folders and subtasks are organized.
Project Change Map = why structure or interpretation changed.
Technical Route = how commands, scripts, data, or models execute.
```

Recommended artifacts:

```text
README.md                         # short project roadmap near the top
tasks/TASK00-project-governance/  # detailed portfolio roadmap and decisions, when triggered
docs/task-lineage-map.md          # task tree / navigation surface
final_outputs/project-roadmap.md  # reviewed phase-level roadmap, optional
final_outputs/project-change-map.md
```

When generating these diagrams, explicitly use `$roadmap` rather than re-inventing Mermaid styling locally.

## Project Change Maps

Project change maps build on the default task lineage map. They are created when the task graph changes meaning, not just when a new ordinary task is added.

For exploratory projects, create a project change map when new evidence changes task structure, scope, or interpretation.

Use this when:

- a TASK is demoted into a subtask but its evidence ledger must remain frozen;
- a new finding creates a sibling amendment, risk investigation, or revised-design task;
- a parent task becomes an umbrella that owns integration, correspondence, or final gates;
- old results remain useful but need a new interpretation boundary;
- paths are moved and readers need a stable old-path to new-path map.

Recommended artifact:

```text
tasks/TASKxx-name/outputs/taskxx-project-change-map.md
```

or, for project-level phase changes:

```text
final_outputs/project-change-map.md
```

Include:

- a Mermaid task lineage graph showing parent task, frozen subtasks, amendments, and likely next gates;
- a Mermaid change-path graph showing which new evidence triggered the restructure;
- key dates/status labels on graph nodes, such as `opened`, `accepted`, `frozen`, `restructured`, or `next gate`;
- `click` links in Mermaid nodes when the target renderer supports them;
- a Markdown fallback link table because Mermaid click support varies across renderers;
- a traceability table with `change item | date/date-time | old interpretation | new interpretation | handling | evidence`;
- a migration table with `date/date-time | old path | new path`;
- a parent `logs/log.md` entry explaining why the change happened and what remains frozen.

Use date-only labels for phase-level changes. Use full date-time only when several order-sensitive decisions happen on the same date.

Do not use a Gantt chart as the default for research-design restructures. Use Gantt only when timing and scheduling are the main problem. For evidence-driven design changes, lineage and change-path diagrams are usually clearer.

After creating a change map, update the parent `README.md`, task index, and relevant logs so the map becomes a navigation surface rather than an orphan output.

## Multi-Agent Subtask Governance

When a task uses multiple subagents, workers, or parallel agent threads, manage them as subtasks under the parent task instead of only listing them in the parent README.

Use subtasks for subagents when:

- the subagent work serves the same parent objective and final artifact;
- the parent task owns shared state, source data, browser sessions, credentials, downloads, or final integration;
- each subagent has a separable local write scope, such as parsing, matching, panel construction, validation, or report drafting;
- the work needs independent logs, UAT, and evidence trail before the parent task can accept it.

Do not split subagents into new top-level Tasks unless their goal, external system, artifact, or acceptance contract becomes independently meaningful.

For each subagent subtask, create the management scaffold before allowing substantive work:

```text
TASKxx-parent/
├── README.md                     # parent dashboard and integration status
├── logs/log.md                   # parent decisions, shared systems, downloads, final integration
└── subtasks/
    ├── TASKxx-A-short-name/
    │   ├── README.md             # subtask roadmap, inputs, outputs, status
    │   ├── TASKxx-A-说明.md       # scope, write boundary, done criteria
    │   ├── acceptance-contract.md # UAT / acceptance checks
    │   ├── evidence-ledger.md     # input-command-output-provenance ledger
    │   ├── outputs/
    │   └── logs/
    │       └── log.md            # subagent ReAct log
    └── TASKxx-B-short-name/
```

Parent README should include a compact subagent table:

```text
Role | Owner/Agent ID | Subtask Path | Responsibility | Browser/Download/Shared-State Access
```

Coordination rules:

- The parent agent keeps ownership of shared external systems, credentials, browser tabs, captcha, download centers, raw download ledgers, email/correspondence, and final integration.
- Subagents work only in local files and in their declared write scopes.
- Subagents must not edit parent `docs/download-ledger.md`, parent `logs/log.md`, parent `README.md`, correspondence/email folders, or shared state unless explicitly assigned.
- Subagents must write or update their own `logs/log.md` before substantive work, using the ReAct format.
- Subagents must maintain `evidence-ledger.md` so every output can be traced back to raw inputs, commands, scripts, and QC numbers.
- For research, analysis, review, or interpretation-heavy subtasks, require or strongly prefer a subagent `outputs/peer-brief.md`: an explain-back written as if explaining the task to an outside peer and asking for methodological advice. This is an internal review artifact, not permission to publish.
- Subagent outputs are not accepted into the parent task until their `acceptance-contract.md` UAT passes and the parent agent reviews integration fit.
- If a subagent discovers that new downloads, credentials, browser actions, or human verification are needed, it records a request in its evidence ledger or output note; the parent agent queues and executes the shared-system action.
- If a subagent was interrupted after creating partial scripts, temp files, or incomplete outputs, record those artifacts as `pending review`, not as accepted outputs.

### Subagent Peer Brief / Explain-Back

When a subagent is asked to do non-trivial research reasoning, empirical diagnosis, literature review, design critique, result interpretation, or exploratory analysis, ask it to produce a peer-facing explain-back in addition to the technical report.

Default artifact:

```text
outputs/peer-brief.md
```

Purpose:

```text
The technical report answers: what did I do, what files did I produce, what numbers did I find?
The peer brief answers: what problem am I actually working on, why does it matter, what would a knowledgeable outsider question, and what advice should we ask for?
```

Use a "知乎-style同行解释稿" only as a writing posture: clear context, vivid problem framing, enough details for a peer to reason with, and explicit questions for advice. Do not treat it as a public publishing artifact unless the user explicitly approves publication.

Keep this artifact subtask-local. When the job changes from “explain one worker's assignment” to “integrate several TASKs, update an actual Zhihu post, reconstruct the current research narrative, or audit the project from a stranger's perspective,” route to `$research-zhihu-post`. `task-driven-project-manager` owns the trigger, file location and acceptance check; `$research-zhihu-post` owns the full outside-view audit and publication-mode boundary.

Recommended structure:

```markdown
# 标题：一句话说明这个 subtask 在解决什么问题

## 给同行的背景
这个研究 / 项目为什么会走到这里？上游发现是什么？

## 我接到的任务
我的具体问题是什么？我负责哪条分支？不负责什么？

## 我用到的数据 / 材料
用通俗名称说明数据、样本、变量或文献；避免暴露敏感路径、账号、未公开字段细节。

## 我怎么做
说明方法、比较组、诊断逻辑、验收标准或模型思路。

## 目前看到的结果
用同行能理解的语言解释结果，同时区分事实、解释和推测。

## 我现在的困惑
列出识别、样本、测量、机制、外推或写作上的不确定性。

## 想请同行建议的问题
提出 3-7 个具体问题，便于外部同行给建设性反馈。

## 边界与脱敏说明
说明哪些内容被省略、匿名化或只保留为内部证据。
```

Safety and confidentiality rules:

- Do not reveal credentials, tokens, private collaborator names, raw internal paths, unpublished raw records, sensitive business identifiers, or download URLs.
- Use generic labels such as `platform answer data`, `external fund database`, `theme invitation edges`, or `fund-quarter panel`.
- Keep exact counts only when they are already approved for task-level reporting; otherwise round or describe qualitatively.
- Make limitations explicit. A peer brief should invite critique, not over-sell the result.
- If the brief is intended for actual external sharing, the parent task or user must review and approve it first.

Parent acceptance should check:

- `outputs/peer-brief.md` exists when required by the parent task or acceptance contract;
- it explains the subtask in plain language without losing the research logic;
- it clearly separates evidence, interpretation, and open questions;
- it contains no sensitive details that should not leave the project workspace;
- it is linked from the subtask README, evidence ledger, or parent review queue when used for collaborator review.

Parent acceptance closeout:

- Treat subagent `completed` as a claim, not as parent acceptance. The parent task must run a short review before marking the subtask accepted.
- Keep a parent-level review queue, for example:

```text
Review ID | Subtask | Expected Artifact | Status | Parent Acceptance Check
RV-01     | TASKxx-A | outputs/report.md  | waiting/accepted/rejected | UAT passes; integration fit reviewed
```

- Accept a subtask only after checking:
  - its `README.md` roadmap status and top-level `Status` agree, or any mismatch is corrected or documented;
  - its `acceptance-contract.md` UAT checks are explicitly reported as pass/fail;
  - its `evidence-ledger.md` links inputs, commands, scripts, outputs, and QC numbers;
  - required output files actually exist and are readable;
  - the subagent respected its write boundary and did not edit parent ledger/log/README/emails unless explicitly assigned;
  - known limitations are promoted into a Markdown report, not left only in terminal output;
  - required peer brief / explain-back exists and is safe to share internally or externally at the stated level;
  - the output can be used by the parent integration gate, or the blocker is explicit.
- After acceptance, update the parent README/status table, parent review queue, and parent `logs/log.md` with the acceptance result and residual risk. Do not silently leave parent status as `waiting` after accepting downstream work.
- If parent integration depends on a later shared-system action, mark the subtask `accepted` but keep the integration gate open; avoid overclaiming the whole parent TASK as complete.

Good subagent subtasks are small enough to own, but complete enough to verify. Avoid creating one subagent per vague phase; prefer 2-4 disjoint workstreams with non-overlapping write scopes.

## Task Folder Rules

Each `tasks/TASKxx-name/` folder should answer:

- What does this Task do?
- What upstream files or Tasks does it depend on?
- What command runs it?
- What files does it produce?
- What counts as done?
- Does it require human review?
- Which external OBL or GATE, if any, does it prepare for?

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

For frozen empirical or analytical protocols, tests must also protect the protocol itself: assert the primary sample filter, unique keys, mapping/version choice, missing-versus-zero rules, planned contrasts, and separation of primary from sensitivity panels. A script that runs successfully is not sufficient evidence that it executed the frozen design.

## Output Discipline

Keep intermediate results inside each Task. Copy or export only reviewed final deliverables to `final_outputs/`.

Use this distinction:

- `tasks/TASKxx/outputs/`: evidence, raw/simplified outputs, batch summaries, reports for one task.
- `tasks/TASKxx/docs/`: task-local explanation, runbooks, decision notes, manual protocols.
- `docs/`: cross-cutting project references, Q&A, decision trees, conceptual explanations.
- `docs/external-timeline/`: cross-cutting external chronology, Gate state and notice evidence when `$timeline-ex` is activated.
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
- whether the current phase can be explained without TASK-private context; when several TASKs changed the main interpretation, invoke `$research-zhihu-post` and link the latest outside-view explanation from the review or TASK00.
- when External Interface is active, which outside Gates changed status, what notice caused the change, and which internal TASKs are affected.

When a project teaches a reusable method, add a `workflow/skill feedback` section either in the review document or a dedicated TASK. The feedback should say:

```text
Where did this rule come from?
What evidence supports it?
Which workflow/skill should receive it?
What should remain only in the TASK as case evidence?
```

For standing-governance projects, cross-TASK portfolio reviews live under `tasks/TASK00-project-governance/reviews/`. Phase deliverables intended for broad consumption may still be promoted to `final_outputs/`; do not duplicate the full decision ledger in both places.

When reporting to the user, mention:

- what project files were created or updated;
- the chosen Task breakdown;
- how to initialize environment and run the dashboard;
- what human gates remain.
