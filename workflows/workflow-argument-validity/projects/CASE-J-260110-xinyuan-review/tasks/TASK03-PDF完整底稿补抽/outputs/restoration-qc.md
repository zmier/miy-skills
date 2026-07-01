# Restoration QC

## Source

- PDF: `/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.pdf`
- extractor: `pdfplumber`

## Table Extraction Notes

| item | status | note |
|---|---|---|
| T01 | needs-table-visual-qc | pdfplumber extracted 9 rows x 1 cols on page 3; compare against PDF before using exact values. |
| T02 | needs-table-visual-qc | pdfplumber extracted 2 rows x 1 cols on page 4; compare against PDF before using exact values. |
| total_tables | info | extracted 2 candidate tables. |

## Page Text Table Snippets

`pdfplumber.extract_tables()` 对本文回归表结构识别较弱，只抽到 2 个假表。但 `pdf-pages-text.md` 中已经包含 Table 2-18 的大量文本行、核心变量、系数、星号、表注和聚类说明。

已额外生成：

```text
outputs/table-text-snippets.md
```

该文件可作为抽树阶段的表格证据线索，但使用精确数值前仍需回 PDF 视觉核验。
