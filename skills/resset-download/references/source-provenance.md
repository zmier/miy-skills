# Source Provenance

## 2026-07-08 TASK05 RESSET Matched-Universe Download

| Field | Value |
|---|---|
| Source type | real project feedback / field-discovery |
| Source case | `Writer/03 Projects/260521-基金经理研究/tasks/TASK05-external-fund-data-download-panel/` |
| Trigger | RESSET `FDSHRCHG` needed a large matched fund universe download through the web UI, with captcha, duplicate same-table download-center rows, and Chrome download-event instability. |
| Evidence | `outputs/fdshrchg_matched_universe_download_qc.md`; `docs/download-ledger.md`; `cache/browser-probes/resset_submit_existing_table.js`; `cache/browser-probes/resset_fetch_download_center_token.js`; parent `logs/log.md`. |
| Skill impact | Adds text-file code upload, exact download-center row selection, page-context token fallback, and multi-CSV zip QC rules. |
| Cleaned into | Generic route: use `cSearchFile` when a RESSET table supports text-file code filtering; match download-center tasks by row time/row text and parsed `downloadtask(...)`; if browser download event fails after a UI-created 100% task, page-context `fetch('/verifyDownload?token=...')` can be a bounded retrieval fallback after zip magic validation. |
| Kept in TASK | Specific token, download id, code count, fund table batch id, exact row counts, captcha image, school session. |
| Migration status | structural-green / forward-test-pending |

This feedback preserves the existing boundary: task creation remains UI/captcha/download-center based. The token fallback is only for retrieving a completed task already created through the authorized browser session.
