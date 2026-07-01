# Table Visual QC: Table 11

## Scope

- Fixture: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/fixtures/visual-source-qc-table11`
- Restored table: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/fixtures/visual-source-qc-table11/table-11.restored.md`
- Page images inspected with model vision:
  - `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/fixtures/visual-source-qc-table11/page-19.png`
  - `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/tests/fixtures/visual-source-qc-table11/page-20.png`

## QC Level

- Status: `page-level visual checked`
- Cross-page status: `cross-page boundary checked`
- Cell-level status: no full cell-by-cell audit was performed

This QC used model vision on both page images. It is a page-level visual comparison of the table structure, cross-page continuation, and selected high-risk cells against the restored Markdown. It is not a full cell-by-cell audit of every coefficient, t-statistic, and note.

## Visual Findings

### Page 19

- Page 19 contains prose immediately above Table 11 and the start of `表 11 基于声誉竞争机制的检验结果`.
- The visible table header has dependent variable `KV` and columns `(1)`, `(2)`, `(3)`.
- The first regression rows and controls are visually present and align with the restored table.
- High-risk significance pattern:
  - `Peerdumy_PosCAR[-10, 10]×POST` appears in column `(3)` as `-0.0028` with t-statistic `(-0.57)` and no significance stars.
  - `Peerdumy_NegCAR[-10, 10]×POST` appears in column `(3)` as `-0.0168***` with t-statistic `(-3.33)`.
- This visually supports the restored table's PosCAR[-10,10] / NegCAR[-10,10] pattern.

### Page 20

- Page 20 continues the lower part of Table 11, beginning with the tail of the `MB` t-statistics and then `PROFIT`, `BOARD`, `INDEP`, `SOE`, `DUAL`, intercept, fixed effects, sample size, adjusted R2, and within-group p-values.
- The continuation belongs to the same Table 11 and ends before the next subsection heading `（三）市场压力机制`.
- The visual table tail supports the restored Markdown for the checked bottom rows:
  - `PROFIT`: `-0.0018***` across all three columns, with t-statistics `(-4.74)`, `(-4.71)`, `(-4.76)`.
  - `SOE`: `-0.0181*`, `-0.0176*`, `-0.0178*`.
  - Sample size: `11300` in all three columns, with a footnote marker on the first column.
  - Adjusted R2: `0.6287`, `0.6290`, `0.6287`.
  - Within-group p-values: `0.0735`, `0.0037`, `0.0282`.

## Comparison With Restored Markdown

- The restored Markdown records the table as cross-page, and the image evidence confirms the table begins on page 19 and continues onto page 20.
- The restored Markdown preserves the key high-risk pattern: `PosCAR[-10,10]` is not visually significant, while `NegCAR[-10,10]` is visually significant at `***`.
- The restored Markdown is structurally rough: several multi-column rows are compressed into two Markdown columns, so it should not be treated as a clean cell-level table reconstruction.
- The restored Markdown's note about an author-prose conflict is visually plausible: page 19 prose says the PosCAR interaction terms are significant at 1% and the NegCAR interaction terms are not significant, but the visible Table 11 evidence shows the opposite for the `[-10,10]` pair and likewise shows significant PosCAR rows for `[-1,1]` and `[-5,5]` while the corresponding NegCAR rows are not significant.

## Conclusion

The PosCAR[-10,10] / NegCAR[-10,10] significance pattern in the restored table is visually supported at page-level: `Peerdumy_PosCAR[-10, 10]×POST = -0.0028` with no stars, and `Peerdumy_NegCAR[-10, 10]×POST = -0.0168***`.

Residual risk remains because this was not a cell-level audit. The Markdown reconstruction remains unsuitable as a fully normalized regression table without additional manual or higher-resolution QC.
