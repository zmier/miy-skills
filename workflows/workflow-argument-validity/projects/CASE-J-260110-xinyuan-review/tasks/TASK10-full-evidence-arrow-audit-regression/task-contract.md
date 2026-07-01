# Task Contract

## Scenario

Academic argument arrow audit regression for CASE-J-260110-xinyuan-review.

## Mode

```text
mode: full-evidence-audit
```

## Tested Skill

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-arrow-audit/skills/academic-argument-arrow-audit/SKILL.md
```

## Expected Steps

1. Read required skill and direct references/assets.
2. Read TASK07 author-tree outputs.
3. Build or update audit input status and review sensitivity map.
4. Rewrite and type all claim-to-claim arrows.
5. Run first-round internal arrow audit.
6. Generate centralized `external-evidence-request.md`.
7. Perform external evidence enhancement for every request, merging equivalent searches when appropriate.
8. Generate `external-evidence-ledger.md`.
9. Backfill `academic-arrow-audit-table.md`.
10. Generate break summary and issue-selection candidates.
11. Freeze audit outputs.
12. Only after freezing, read TASK08/TASK09 outputs and write regression comparison.

## Allowed External Evidence Routes

- Literature search: OpenAlex / WoS / CNKI / web, following `scholar-kit-literature-search` where practical.
- Method standard search: method papers, econometrics references, top-journal applications, official package docs.
- Policy / regulatory document search: official regulator or government pages where relevant.
- Official data search: official statistical or regulatory data pages where relevant.
- Official documentation search: official docs, replication packages, author/package documentation.
- Citation verification: original cited paper metadata or accessible source pages.

## Forbidden External Evidence Routes

- Do not treat search failure, login failure, CAPTCHA, paywall or database error as evidence that no source exists.
- Do not invent sources.
- Do not use low-quality web pages as decisive evidence when high-quality sources are required.

## Pending Outputs Allowed

Pending is allowed only when search is blocked or evidence remains insufficient after a good-faith search. In that case write:

```text
search_status: technical-failure / insufficient-result / manual-verification-needed
```

and keep the corresponding arrow as `still-unclear`, `needs-qc`, or `needs-external-evidence`.

## Inputs

Read only these audit inputs before freezing:

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs/academic-argument-spine.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs/canonical-node-ledger.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs/canonical-edge-ledger.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs/evidence-ledger.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs/extraction-qc.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs/paper-argument-tree.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs/recursive-tree-master.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs/evidence-expanded-mermaid.md
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK07-latest-paper-tree-regression/outputs/obsidian-link-map.md
```

Do not read `task07-readiness-for-arrow-audit-and-xinyuan-coverage.md` before freezing because it includes coverage framing.

## Forbidden Before Freeze

Do not read:

```text
../TASK08-academic-arrow-audit-rerun/
../TASK09-clean-subagent-academic-arrow-audit-v2/
../TASK02-学术论文论证workflow盲跑回测/outputs/xinyuan-comparison.md
欣媛审稿意见
current conversation logs
```

## Outputs

Write only under:

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK10-full-evidence-arrow-audit-regression/
```

Required outputs:

```text
logs/log.md
outputs/audit-input-status.md
outputs/review-sensitivity-map.md
outputs/plain-language-arrow-list.md
outputs/typed-arrow-ledger.md
outputs/internal-arrow-audit-table.md
outputs/external-evidence-request.md
outputs/external-evidence-ledger.md
outputs/academic-arrow-audit-table.md
outputs/academic-arrow-break-summary.md
outputs/issue-selection-candidates.md
outputs/task10-regression-comparison.md
outputs/qc-and-skill-feedback.md
```

## Completion Standard

- Every audit issue must bind to `arrow_id`.
- Every external source must bind to `request_id` and `target_arrow`.
- Every external source row must include source quality and URL/path/metadata where available.
- The final audit must distinguish internal-only judgment from externally confirmed judgment.
- The comparison must explicitly say what is more/less than TASK08 and TASK09.
