# Source Provenance

## 2026-07-08 TASK05 CSMAR Validation Batch

| Field | Value |
|---|---|
| Source type | real project feedback / field-discovery |
| Source case | `Writer/03 Projects/260521-基金经理研究/tasks/TASK05-external-fund-data-download-panel/` |
| Trigger | CSMAR was used as validation/backup source for RESSET P0 fund data. |
| Evidence | `outputs/csmar_p0_validation_download_qc.md`; `docs/download-ledger.md`; raw zips under `data/raw/csmar/`; parent `logs/log.md`. |
| Skill impact | Adds validation-batch mode and QC discipline for dictionary/sample downloads. |
| Cleaned into | Generic rule: when CSMAR is used as cross-source validation, save raw zip plus DES dictionary, distinguish full-small tables from sample windows for large tables, and document parser limitations from long text fields. |
| Kept in TASK | Specific fund table choices, exact school account, zip filenames, row counts, project-specific P0/P1 priority. |
| Migration status | structural-green / forward-test-pending |

This feedback does not change the default CSMAR download route. It adds a repeatable validation mode for projects that need source cross-checks before final panel construction.
