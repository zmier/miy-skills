# Workflow Argument Validity Regression Tests

This directory stores reusable regression fixtures and run records for `workflow-argument-validity`.

## Stable Fixtures

| Fixture | Purpose |
|---|---|
| `fixtures/visual-source-qc-table11/` | Smoke fixture for checking whether PDF table / figure source QC uses model vision rather than only OCR or restored Markdown. |
| `fixtures/external-evidence-routing-mini/` | Route-only fixture for checking whether literature, citation, policy, and table-conflict evidence requests are routed to the correct tool/source class. |

## Current Runs

| Run | Purpose | Current Result |
|---|---|---|
| `runs/2026-06-20-mini-regression/` | Mini regression for visual QC, external-evidence routing, and first CNKI/WoS execution smoke. | Visual QC PASS; route-only PASS; CNKI PASS; WoS PARTIAL at that time. |
| `runs/2026-06-21-wos-executed-smoke/` | WoS-only rerun after manual verification / longer wait. | WoS executed-search PASS; remaining issue is intermediate waiting-state observability. |

## How To Use

When a workflow / Skill change touches any of these capabilities, rerun the relevant fixture:

- visual source QC change -> rerun `visual-source-qc-table11`;
- external evidence routing change -> rerun `external-evidence-routing-mini`;
- scholar-kit / CNKI / WoS execution change -> rerun the executed-search smoke tests;
- WoS status / browser / callback change -> rerun `2026-06-21-wos-executed-smoke` or create a new dated run with the same pass criteria.

## Reporting Discipline

- `route-only` means the workflow selected the correct source/tool. It does not prove the tool executed.
- `executed-capability` means the tool actually ran and wrote result/status artifacts.
- `status=scaffold` is not database execution.
- Browser handoff is not result retrieval.
- Slow manual verification should be recorded as a machine-readable waiting state whenever the underlying tool supports it.

See:

- `regression-log.md`
- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-tao/references/regression-test-protocol.md`
