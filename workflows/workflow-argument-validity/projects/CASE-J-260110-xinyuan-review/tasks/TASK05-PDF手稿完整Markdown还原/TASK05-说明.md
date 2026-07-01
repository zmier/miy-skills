# TASK05 PDF 手稿完整 Markdown 还原

## 目标

使用 `scholar-pdf-markdown-restoration` 的规则，为欣媛 case 中的原始 PDF 生成一份带完整表格入口的 Markdown 底稿，服务后续学术论文论证树抽取和证据定位。

## 输入

- 原始 PDF：`/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.pdf`
- 现有可读 Markdown：`/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.md`
- TASK03 PDF 页文本：`../TASK03-PDF完整底稿补抽/outputs/pdf-pages-text.md`

## 输出

- 主底稿：`outputs/manuscript_restored_with_tables.md`
- PDF 页文本备份：`outputs/manuscript_pdf_page_text_with_tables.md`
- 表格文件：`outputs/tables-restored/table-01.md` 至 `outputs/tables-restored/table-18.md`
- 表格插入映射：`outputs/table-insertion-map.md`
- 图表清单：`outputs/figures-tables-inventory.md`
- QC 记录：`logs/restoration-qc.md`

## 本轮边界

- 本 TASK 不做论文质量判断。
- 表格以 PDF 页文本为基础恢复；跨页或版式复杂表格保留原始表格文本并标记 `needs-table-visual-qc`。
- 当前产物适合作为论证树抽取底稿；若用于正式逐段审稿引用，还应对关键表格做 PDF 视觉复核。
