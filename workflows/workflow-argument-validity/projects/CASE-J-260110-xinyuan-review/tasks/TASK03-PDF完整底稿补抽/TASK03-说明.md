# TASK03 PDF 完整底稿补抽

## 目标

当前 case-local `inputs/manuscript.md` 基本保留正文段落，但回归表格、图和表注不完整。为了让后续未污染 subAgent 执行 `full-tree` 两步抽树，需要先从原始 PDF 补抽：

```text
页面文本
表格 inventory
表格 Markdown
表注 / 显著性说明
抽取 QC
```

## 输入

```text
/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.pdf
```

## 边界

- 本 TASK 只做 PDF restored evidence bundle，不读欣媛审稿意见。
- 先以 `pdfplumber` 做表格和文本补抽；不做最终视觉级逐页精修。
- 若表格结构复杂或跨页错误，标记 `needs-table-visual-qc`，不伪造。

## 输出

| 文件 | 用途 |
|---|---|
| `outputs/pdf-pages-text.md` | 每页文本抽取 |
| `outputs/pdf-table-inventory.md` | 表格页码、表题候选、抽取状态 |
| `outputs/tables/table-XX-*.md` | 抽取出的 Markdown 表格 |
| `outputs/restoration-qc.md` | PDF 补抽质量记录 |

