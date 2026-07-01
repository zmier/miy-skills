# Regression Comparison: 2026-06-20 Mini Regression

## Scope

This run tests two narrow regression risks introduced by the latest workflow updates:

1. Source-table / figure QC should explicitly use large-model vision, not only text extraction, OCR, or parser output.
2. External-evidence requests should route to the right evidence channel before making claims: scholar-kit / WoS / CNKI / DOI / official sources / source-QC as appropriate.

The tests are intentionally small fixtures, not full-case UATs.

## Results

| Test | Result | What It Was Supposed To Prove | Observed Behavior |
|---|---|---|---|
| `visual-source-qc-mini` | PASS | A clean agent should inspect table page images with model vision and distinguish page-level visual QC from full cell-level audit. | The agent inspected `page-19.png` and `page-20.png`, recorded image paths, confirmed the Table 11 PosCAR / NegCAR significance pattern, and marked the result as page-level visual checked rather than full cell-level audited. |
| `external-evidence-routing-mini` | PASS as route-only | A clean agent should route different external-evidence needs to the correct channel instead of using generic web search for everything. | The agent routed literature-gap search to `scholar-kit-literature-search` / OpenAlex / WoS / CNKI consideration, citation verification to scholar-kit / DOI / publisher metadata, policy checks to official sources, and table numeric conflict back to PDF/DOCX source QC with model vision or manual inspection. This did not execute WoS or CNKI. |
| `executed-search-smoke` | PARTIAL | The scholar-kit execution layer should actually run a minimal CNKI/WoS probe or report a machine-readable blocked state. | CNKI executed successfully and returned 3 records. WoS default mode only produced `status=scaffold`; WoS browser handoff reached the advanced search page; WoS browser results mode entered manual-confirmation wait but did not write a machine-readable waiting-state or results file. |

## What This Proves

- The PDF/DOCX restoration update is enforceable at least for a PDF table-page fixture: the agent understood that visual QC means actually using model vision on rendered pages or crops.
- The academic arrow-audit update is enforceable as a route-selection discipline: the agent did not collapse literature, policy, citation, and source-table conflicts into one generic "search the web" behavior.
- CNKI execution is confirmed for a minimal query.
- The two changes are now regression-testable with small fixtures, instead of requiring a full manuscript run every time.

## What This Does Not Prove

- The visual test is page-level, not a normalized full cell-by-cell audit of the entire table.
- The visual test only covers a PDF table fixture. It does not yet cover DOCX embedded media, exported DOCX figures, scientific plots, or formula-heavy tables.
- The routing test is route-only. It does not verify actual database availability, login state, DOI resolution, or successful official-source retrieval.
- The executed-search smoke test verifies CNKI execution, but does not yet verify WoS result retrieval.
- A full evidence audit still has to execute the routed child skill or source-QC workflow and record concrete evidence status.

## Residual Issues

- The visual mini-run reported that `references/vision-restoration-rules.md` was missing under the tested PDF restoration skill. Local inspection shows the file now exists, so this may be a path-resolution or stale-read warning rather than a true missing file. Future regression runs should treat this as a reference-resolution check.
- Table 11 is now visually checked for the key PosCAR / NegCAR pattern, but the restored Markdown table remains structurally compressed. It should not be used as a fully normalized table without a dedicated table-reconstruction pass.
- WoS needs a better machine-readable blocked-state contract. Reaching `browser_handoff_ready` is useful, but it must not be reported as completed WoS evidence retrieval.

## Fixture Status

- Keep `fixtures/visual-source-qc-table11/` as a stable smoke fixture for source-table visual QC.
- Keep `fixtures/external-evidence-routing-mini/` as a stable route-only fixture for external-evidence routing discipline.
- Add a later DOCX media fixture when testing `scholar-docx-markdown-restoration`.
- Keep `executed-search-smoke/` as the first execution-level fixture: CNKI currently passes; WoS currently needs handoff/status hardening before it can pass result retrieval.
