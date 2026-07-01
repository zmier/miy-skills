# Regression Log

## 2026-06-20 Mini Regression

Run root:

- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/runs/2026-06-20-mini-regression`

Coverage:

| Test | Mode | Result | Purpose |
|---|---|---|---|
| `visual-source-qc-mini` | executed-capability / visual source QC | PASS | Confirm model vision is actually used on PDF table page images. |
| `external-evidence-routing-mini` | route-only | PASS as route-only | Confirm external evidence needs are routed to scholar-kit / official sources / source QC instead of generic web search. |
| `executed-search-smoke` | executed-capability | PARTIAL | CNKI executed and returned 3 records; WoS reached browser handoff but did not complete results retrieval. |

Backfed rules:

- `workflow-tao/references/regression-test-protocol.md` now distinguishes `route-only test` from `executed-capability test`.
- Route-only tests cannot be reported as database/tool capability passing.
- `status=scaffold` is not accepted as evidence of database execution.

## 2026-06-21 WoS Executed Smoke

Run root:

- `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/runs/2026-06-21-wos-executed-smoke`

Coverage:

| Test | Mode | Result | Purpose |
|---|---|---|---|
| `wos_handoff_probe_timeout` | executed-capability / browser handoff | PARTIAL | Confirm WoS Advanced Search opens through shared Chrome and writes a machine-readable handoff payload. |
| `wos_results_probe_timeout` | executed-capability / browser results | INITIAL FAIL / OBSERVABILITY ISSUE | Confirm WoS can submit a query and write completed / zero-result / awaiting-human / failed status. Short-timeout run stalled without writing output JSON. |
| `wos_results_probe_after_verification` | executed-capability / browser results | PASS | After manual verification / longer wait, WoS wrote `browser_results_ready`, detected 1,468 results, and extracted 50 candidates. |

Issue filed:

- `/Users/narra/Documents/alib/Writer/.pytools/scholar-kit/skills/scholar-kit-wos-search/issues/BUG-2026-06-21-wos-results-probe-stalls/README.md`

Regression status:

- Keep this run as the current WoS executed-capability baseline.
- WoS execution is confirmed after verification.
- Remaining improvement: `browser-stage results` should write an intermediate machine-readable waiting / blocked status during slow verification or page readiness.
