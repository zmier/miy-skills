# Restoration QC

- date: 2026-06-20
- source_pdf: `/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.pdf`
- readable_markdown_source: `/Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260110/企业主动披露违规何以引导行业自律发展：来自信息披露质量改善的经验证据.md`
- pdf_page_text_source: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/projects/CASE-J-260110-xinyuan-review/tasks/TASK03-PDF完整底稿补抽/outputs/pdf-pages-text.md`
- skill: `scholar-pdf-markdown-restoration`

## 本轮完成

- 已生成带表格嵌入的主底稿：`outputs/manuscript_restored_with_tables.md`
- 已生成 PDF 页文本备份：`outputs/manuscript_pdf_page_text_with_tables.md`
- 已生成表 1 至表 18 的独立表格文件：`outputs/tables-restored/table-01.md` 至 `table-18.md`
- 主底稿中已加入 Obsidian transclusion：`![[tables-restored/table-XX.md]]`
- 已清理现有 Markdown 中的讨论批注、高亮标记和脚注式疑问标记。
- 本轮未拆分 `sections-restored/`：现有主稿章节结构已经清楚，且后续任务需要完整上下文抽取论证树；因此优先保留单文件主底稿。

## 表格还原状态

- 表 1 使用现有 Markdown 表格并保留 PDF QC 标记。
- 表 2 至表 18 使用 TASK03 PDF 页文本抽取结果恢复。
- 已补做表格页图像渲染和页面级视觉复核：`outputs/page-images/page-08.png` 至 `page-31.png`
- 已补做两张表格页总览：`outputs/page-images/contact-08-19.png`、`outputs/page-images/contact-20-31.png`
- 跨页表与版式风险表已做跨页边界视觉确认：表 6, 表 7, 表 11, 表 13, 表 14, 表 16, 表 18
- 表 11 发现作者正文解释与 PDF 表格本身疑似不一致：正文说三组 PosCAR 显著、NegCAR 不显著；PDF 表格第三列显示 `Peerdumy_PosCAR[-10,10]×POST = -0.0028` 不显著，而 `Peerdumy_NegCAR[-10,10]×POST = -0.0168***` 显著。

## 未完成 / 风险

- 本轮已做页面级视觉复核，但未做每个单元格的人工录入式全量校对。
- 当前 Markdown 表格重建是 row-level readable reconstruction；复杂回归表的精确列对齐仍以 PDF page image 和 `Raw PDF table text` 为准。
- 图像/图 1、图 2尚未做精准裁剪，仅在 PDF 页文本中保留文字线索。
- 该底稿适合进入论证树抽取和证据定位；若用于正式审稿逐句引用，建议先对关键表格做视觉复核。
