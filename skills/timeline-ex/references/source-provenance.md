# Source Provenance

## 2026-07-16—17 MPA External Lifecycle

| Field | Value |
|---|---|
| Source type | dialogue-insight / field-discovery / forward-test |
| Source case | `Writer/03 Projects/2026-学位/MPA/docs/external-timeline/` |
| Trigger | A teacher notice created a chain of pre-defense, similarity check, blind review, defense and degree-committee gates; the existing internal Roadmap had no clean place for external qualification state. |
| Evidence | MPA `README.md`; `docs/project-roadmap.md`; External Timeline HTML, data source and node records; project `logs/log.md`; browser UAT. |
| Skill impact | Creates a reusable external-interface control plane with data-driven HTML, EVT/OBL/GATE/OUT nodes, semantic arrows, time certainty and append-only notice updates. |
| Cleaned into | Generic rule: external notices become immutable EVT records; they create/update/supersede obligations, gates and outcomes; internal TASKs produce evidence for gates; HTML is the main view but not the sole fact source. |
| Kept in project | Student identity, degree topic, exact school notice, submission materials, dates specific to the MPA cohort and project-specific task state. |
| Migration status | structural-green / forward-tested-on-MPA |

The MPA forward test produced one EVT, five GATE nodes, one conditional OUT and nine semantic links. Checks confirmed unique IDs, valid link endpoints, existing Markdown documents, JavaScript syntax, browser initialization, filtering and drawer navigation.

## 2026-07-17 Project Management Textbook Mapping

| Field | Value |
|---|---|
| Source type | textbook mapping / dialogue-insight |
| Source case | `Writer/03 Projects/高项/learning/` and extracted Chapter 10 material |
| Trigger | The user asked whether the external timeline corresponded to standard project-management tools and whether its arrows resembled an arrow diagram. |
| Evidence | Chapter 10 schedule material on milestone charts, external interfaces, schedule network diagrams and schedule visualization; Ch8 integration/change-control discussion. |
| Skill impact | Frames Timeline-Ex as a synthesis of milestone timeline, schedule-network dependency semantics, node evidence and a lightweight PMIS control view. |
| Cleaned into | Generic rule: use real time for chronology, semantic arrows for eligibility/state dependency, and evidence records for auditability; do not claim strict ADM semantics when arrows are relationships rather than activities. |
| Kept in learning project | Exam-study notes, chapter progress, MPA-specific classroom discussion and learning-session artifacts. |
| Migration status | conceptual-green / implemented-in-MPA |

## Roadmap Boundary

| Field | Value |
|---|---|
| Source type | sibling-skill extraction |
| Source case | `skills/roadmap/SKILL.md` external actor and Mail RPC pattern |
| Trigger | Roadmap already distinguished internal decision gates, external actors and communication artifacts, but did not own a persistent time-scaled external lifecycle. |
| Skill impact | Keeps Roadmap responsible for internal route narration and navigation; gives Timeline-Ex ownership of external chronology, eligibility gates, obligations, outcomes and notice-driven change. |
| Migration status | structural-green |

Timeline-Ex should remain a sibling to Roadmap, not a replacement or nested variant.
