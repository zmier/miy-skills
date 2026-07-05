# PDF Extraction Routing

本文件记录 `scholar-pdf-markdown-restoration` 的前置抽取路由规则。它借鉴 `vendors/book-to-skill` 的 technical / text extraction 设计，但服务目标不同：这里的抽取器只产生 restored Markdown 的候选材料，不能替代逐章还原、视觉复核和 QC provenance。

## 目标

在正式还原 PDF 前，先判断 PDF 类型、任务深度和可用工具，选择合适的粗抽取路线，并把 extraction provenance 写入项目日志。

```text
PDF diagnosis -> preflight -> extraction candidates -> comparison -> restoration / QC
```

## PDF 类型诊断

开始抽取前，至少判断以下维度：

- `text-heavy`：正文为主，少量或无表格 / 公式 / 图像；
- `table-heavy`：有大量回归表、描述统计表、appendix 表或跨页表；
- `formula-heavy`：理论模型、数学推导或复杂 display equation 密集；
- `figure-heavy`：图像、流程图、坐标图或实验图较多；
- `scanned`：扫描件或 OCR 质量不稳定；
- `back-matter-heavy`：图表、appendix、supplement、references 大量位于正文之后；
- `born-digital`：可直接抽取文字和版面对象；
- `mixed-risk`：以上多类混合。

同时判断任务深度：

- `quick-draft`：只需临时阅读底稿；
- `restoration-draft`：需要章节化、段落编号和明显错误修复；
- `full-restoration`：需要可进入审稿 / 写作分析的 restored manuscript；
- `cell-level-table-audit`：需要逐单元格核对关键表格。

## Preflight

若项目没有现成抽取脚本，先检查可用工具并写入 `logs/extraction-log.md` 或 `logs/restoration-qc.md`：

- `docling`：technical / table-aware candidate extraction；
- PyMuPDF / `fitz`：页面、文字块、截图和裁剪；
- `pymupdf4llm`：LLM-friendly Markdown baseline；
- Poppler / `pdftoppm`：page image rendering；
- `pdftotext`：text-heavy fallback；
- `pypdf`：text fallback；
- `pdfplumber`：表格 / 页面调试 fallback；
- 是否能生成并读取 `outputs/page-images/page-XX.png`。

preflight 失败时不要直接降级为“完成”。应记录尝试过的工具、失败原因、替代路线和剩余风险。

## 抽取器路由

### Text-heavy born-digital PDF

推荐路线：

```text
pymupdf4llm / PyMuPDF baseline
-> paragraph draft
-> page image spot checks
-> restoration / QC
```

若 `pymupdf4llm` 不可用，可降级到 `pdftotext` / `pypdf`，但必须在 QC 中标记为 degraded extraction。

### Table-heavy / formula-heavy technical PDF

推荐路线：

```text
Docling technical extraction as structure-aware candidate
+ PyMuPDF / pymupdf4llm baseline
+ rendered page images
-> compare candidates
-> table / formula / figure visual QC
-> restoration / QC
```

Docling 适合作为：

- table candidate generator；
- caption / layout / object discovery helper；
- second opinion against PyMuPDF / `pymupdf4llm`；
- quick way to identify high-risk pages.

Docling 不能作为：

- visual QC 的替代；
- cell-level audit 的替代；
- `[para N]` 自然段边界的最终权威；
- Figure 精准裁剪和 Obsidian 嵌入的最终执行者；
- “完整 restored manuscript 已完成”的充分条件。

### Scanned or OCR-unstable PDF

推荐路线：

```text
page image first
-> OCR / text extraction as auxiliary
-> vision-first restoration for high-value sections
-> explicit degraded / pending QC status
```

若无法稳定 OCR，关键段落、公式、表格、图像应直接对照 page image 还原。

### Back-matter-heavy PDF

推荐路线：

```text
extract main text
+ build back matter inventory
+ identify actual Figure/Table pages
-> preserve insertion positions
-> restore actual Figure/Table objects
-> merge references / declarations / appendix
```

正文中的 `[Insert Figure/Table ... about here]` 只是插入位置；实际 Figure/Table 通常在文末。不能把插入占位符误认为对象本体。

## 图表多源处理策略

图表处理分五层：

1. `object discovery`
   - 用 Docling / PyMuPDF / `pymupdf4llm` 识别 table、figure、caption、page；
2. `candidate extraction`
   - 表格用 Docling 产 Markdown 候选；
   - 图像用 PyMuPDF 产 page image / crop 候选；
3. `cross-extractor comparison`
   - 对比 Docling、PyMuPDF / `pymupdf4llm`、raw text；
   - 标记表头错位、缺 notes、caption 缺失、对象页码冲突；
4. `visual authority`
   - 最终以 PDF page image / crop image 视觉复核为准；
5. `QC provenance`
   - 每个对象记录来源和状态。

推荐状态词：

- `docling candidate`：Docling 识别 / 结构化候选；
- `pymupdf candidate`：PyMuPDF / `pymupdf4llm` 识别候选；
- `page-level visual checked`：已看页面图并确认对象存在、边界正确、关键行可追溯；
- `cell-level audited`：已逐单元格核对；
- `cross-page boundary checked`：已确认跨页起止和归属；
- `pending visual QC`：尚未完成视觉复核，不能作为最终完成状态。

## Extraction Metadata

每次抽取建议生成或更新 metadata，JSON 或 Markdown 均可。至少包含：

```text
source_pdf:
page_count:
extraction_mode:
extraction_method:
tool_versions:
command:
raw_output:
paragraph_output:
section_output:
page_images:
table_candidates:
figure_candidates:
fallback_events:
pending_visual_qc:
degraded_reasons:
```

`extraction_method = docling` 只说明粗抽取方法，不说明 restored manuscript 已完成。

## 与 book-to-skill 的边界

可借鉴：

- technical / text route；
- preflight；
- metadata；
- fallback；
- large-document programmatic probing；
- update / fold-in mindset。

不可迁移：

- 书籍框架提炼目标；
- chapter summary / glossary / cheatsheet 生成目标；
- 将 extracted text 当成最终知识产物的完成标准。

本 Skill 的最终产物仍是忠实于 PDF 原文的 restored Markdown 和 QC provenance。
