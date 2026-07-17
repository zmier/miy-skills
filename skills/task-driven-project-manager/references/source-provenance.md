# Source Provenance

## 2026-07-08 TASK05 Multi-Agent Data Project

| Field | Value |
|---|---|
| Source type | real project feedback / field-discovery |
| Source case | `Writer/03 Projects/260521-基金经理研究/tasks/TASK05-external-fund-data-download-panel/` |
| Trigger | Parent task used three subagents for raw parse, matching, and panel construction while the main agent owned shared database downloads and final integration. |
| Evidence | Parent `README.md`; `docs/main-agent-download-and-integration-queue.md`; `logs/log.md`; subtask `acceptance-contract.md`, `evidence-ledger.md`, and `logs/log.md`. |
| Skill impact | Adds parent acceptance closeout rules for multi-agent subtasks. |
| Cleaned into | Generic rule: subagent `completed` is not parent `accepted`; parent must verify UAT, evidence ledger, output existence, write-scope compliance, and integration fit before updating parent status. |
| Kept in TASK | Agent names, IDs, exact fund data paths, row counts, database credentials/session details. |
| Migration status | structural-green / forward-test-pending |

The TASK05 case confirms that multi-agent scaffolding is valuable only if the parent task has a review queue and explicit acceptance gate. Local subtask completion should remain separate from parent integration acceptance.

## 2026-07-09 TASK06 Project Change Map And Lineage

| Field | Value |
|---|---|
| Source type | real project feedback / dialogue-insight / field-discovery |
| Source case | `Writer/03 Projects/260521-基金经理研究/tasks/TASK06-rte01-a01-a04-empirical-design/` |
| Trigger | A research-design task changed after discovering that the platform feature was invitation-only. The first-pass P1-P5 prototype needed to be frozen as historical evidence while a sibling amendment task handled sample universe, treatment, control group, and selection-audit changes. |
| Evidence | TASK06 parent `README.md`; `docs/restructure-map-20260709.md`; `outputs/task06-project-change-map.md`; `logs/log.md`; `subtasks/TASK06-1-first-pass-prototypes/`; `subtasks/TASK06-2-invited-universe-amendment/`. |
| Skill impact | Adds project change and lineage maps for exploratory tasks whose structure changes because new evidence changes scope or interpretation. |
| Cleaned into | Generic rule: keep a default task lineage map for multi-task projects; when a TASK is demoted/frozen and a sibling amendment is opened, create a project change map with Mermaid lineage graph, change-path graph, Markdown fallback links, traceability table, migration table, and parent log entry. |
| Kept in TASK | Fund-manager research claims, treatment definitions, exact file names of prototype outputs, row counts, co-author email content, and domain-specific invitation mechanics. |
| Migration status | structural-green / forward-test-pending |

The TASK06 case confirms that README prose alone is not enough when a research task changes shape. A compact visual lineage map should be available by default for multi-task projects; when the graph changes meaning, an old-path/new-path migration table and project change map make the project auditable without polluting frozen first-pass evidence.

## 2026-07-13 TASK00 Standing Project Governance

| Field | Value |
|---|---|
| Source type | real project feedback / dialogue-insight / field-discovery |
| Source case | `Writer/03 Projects/260521-基金经理研究/tasks/TASK00-project-governance/` |
| Trigger | After TASK01--TASK08 produced several competing research workstreams, the user questioned whether to continue a locally strong result, open another substantive TASK, or first review all roadmaps and create a standing TASK00 control plane. |
| Evidence | Project root `README.md`; TASK00 `README.md`, `task-registry.md`, `research-thread-portfolio.md`, `decision-log.md`, dated review and ReAct log; backlinks from TASK01--TASK08. |
| Skill impact | Adds conditional standing project governance for cross-TASK portfolio review, next-workstream arbitration, append-only decisions, and bidirectional roadmap navigation. |
| Cleaned into | Generic rule: when multiple evidence-backed workstreams compete, create a governance sibling that owns registry/portfolio/decision gates but not downstream evidence; keep root README compact and detailed TASKs as source of truth. |
| Kept in TASK | Research hypotheses, exact estimates and sample counts, platform/database details, collaborator correspondence, and domain-specific next-route decisions. |
| Migration status | structural-green / forward-test-pending |

The source case distinguishes three previously conflated artifacts: lineage maps explain organization, change maps explain restructuring, and TASK00 portfolio governance explains why one evidence-backed route should receive the next unit of work. The new pattern is conditional and must not burden small linear projects.

## 2026-07-14 Evidence-Gated Route Promotion And Protocol Repair

| Field | Value |
|---|---|
| Source type | real project feedback / dialogue-insight / field-discovery |
| Source case | `Writer/03 Projects/260521-基金经理研究/` |
| Trigger | A TASK00 seminar promoted one high-information route; the promoted analysis then exposed a mismatch between the frozen primary sample and the implementation, required append-only repair, and was accepted only after an independent alternate implementation. |
| Evidence | TASK00-1 Chair adjudication；TASK09-22 protocol repair；TASK11 acceptance contract；TASK11-1 independent audit；TASK00 dated review and decision log |
| Skill impact | Adds promotion closeout, protocol-conformance tests, append-only corrective history and independent-audit triggers to standing TASK00 governance. |
| Cleaned into | Generic rule: governance decides why a route is promoted; a new evidence owner freezes and executes the Gate; tests assert protocol semantics; historical implementation errors are repaired without overwriting; parent acceptance follows independent review when risk is high. |
| Kept in TASK | Domain estimates, sample counts, fund mappings, hypotheses, collaborator messages and case-specific route decisions. |
| Migration status | structural-green / forward-test-pending |

This source extends standing TASK00 governance without changing ordinary small-project scaffolding or the existing parent/subtask acceptance pattern.

## 2026-07-17 Three-Layer Model And External Timeline

| Field | Value |
|---|---|
| Source type | real project feedback / dialogue-insight / field-discovery / forward-test |
| Source case | `Writer/03 Projects/2026-学位/MPA/` and `skills/timeline-ex/` |
| Trigger | The MPA project had an internal Roadmap and TASK structure, but a teacher notice created a multi-stage external lifecycle of pre-defense, review, defense and degree-committee gates. Root README prose could not represent time certainty, prerequisites, pass/fail branches and notice-driven updates without mixing internal work with external authority. |
| Evidence | MPA `README.md`, `docs/project-roadmap.md`, `docs/external-timeline/`, node records, project log and browser UAT; Timeline-Ex node/HTML contracts. |
| Skill impact | Adds the three-layer model—Execution, Governance, External Interface—and routes persistent external lifecycles to `$timeline-ex`. |
| Cleaned into | Generic rule: TASKs own internal evidence work; Roadmap/TASK00 own internal route and governance; Timeline-Ex owns external EVT/OBL/GATE/OUT chronology. Activate layers conditionally and never create TASK00 merely to store dates. |
| Kept in project | Student identity, degree topic, exact cohort notice, school-specific conditions and current MPA task status. |
| Migration status | structural-green / forward-tested-on-MPA |

The case confirms that external project management is not a special notification archive. It is a distinct interface layer whose nodes can change several internal TASKs at once. The layer remains optional so small linear, learning-index and reading projects are not forced into TASK/tests/Makefile scaffolds.
