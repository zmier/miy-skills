# PDF Extraction Routing

本文件记录 `scholar-pdf-markdown-restoration` 的前置抽取路由规则。它借鉴 `vendors/book-to-skill` 的 technical / text extraction 设计，但服务目标不同：这里的抽取器只产生 restored Markdown 的候选材料，不能替代逐章还原、视觉复核和 QC provenance。

## 目标

在正式还原 PDF 前，先判断 PDF 类型、任务深度和可用工具，选择合适的粗抽取路线，并把 extraction provenance 写入项目日志。

```text
PDF diagnosis -> preflight -> extraction candidates -> comparison -> restoration / QC
```

## Fail-Closed Gate

抽取路由必须 fail closed：

```text
No extraction-routing-qc.md
  -> no primary reading substrate
  -> no restored manuscript
```

任何 PDF 抽取前必须生成 `logs/extraction-routing-qc.md`。该文件记录 routing decision、允许进入的最高状态词和是否触发 Docling / 多抽取器。若没有该文件，只能输出 `extraction candidate`。

生成 `manuscript_paragraphs.md` 后必须做 table-leak scan。若命中：

```text
table-leak high risk
not primary reading substrate
not restored manuscript
```

`table-leak high risk` 的稿件不得进入经验研究 design extraction，除非本轮只提取非表格性的研究问题和后续修复任务。

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

- `quick extraction candidate`：只需候选抽取，不能作为主阅读底稿；
- `rough reading draft`：正文可粗读，但表格、图像、公式仍需回 PDF；
- `degraded reading draft`：存在明显缺陷，只能降级使用；
- `primary reading substrate`：通过 routing / table-leak scan / 基础 QC，可进入文献阅读；
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

优先触发 Docling technical extraction 的信号：

- 论文是 RFS / JF / JFE / AER / QJE / finance empirical paper 等回归表密集文献；
- 论文是 empirical finance / accounting / management paper，且任务目标是实验设计、变量构造、识别策略、机制、异质性或稳健性学习；
- TASK 粗抽取中 Table / Panel / Notes 被压成 prose dump；
- post-extraction table-leak scan 命中；
- 文末、appendix 或 back matter 有大量横向表格；
- 需要快速建立 table inventory、caption inventory 或高风险页清单；
- 需要用第二抽取器对照 PyMuPDF / `pymupdf4llm` 的标题、表格和脚注顺序；
- 用户明确要求“有 table 的完整 md”，但当前只有粗抽取稿。

Docling 不能作为：

- visual QC 的替代；
- cell-level audit 的替代；
- `[para N]` 自然段边界的最终权威；
- Figure 精准裁剪和 Obsidian 嵌入的最终执行者；
- “完整 restored manuscript 已完成”的充分条件。

若满足上述触发条件但决定不使用 Docling / 多抽取器，必须在 `logs/extraction-routing-qc.md` 记录原因，并将输出最高状态限制为 `rough reading draft` 或更低。

Forward-test 经验：在 RFS `Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance` 中，Docling 2.107.0 约 30 秒完成 26 页 technical extraction，识别 17 个 table objects、17 个 caption labels、8 个 formula labels。它明显改善了表格候选结构，但也暴露出：

- `table object count != paper table count`，不能直接映射为论文表号；
- 公式可能输出 `<!-- formula-not-decoded -->`，只能作为定位线索；
- caption、table note、正文仍可能粘连或错序；
- section heading 可能误判表内变量名或对象标题；
- 横向表格页若出现 bbox / provenance clamp warning，应自动标为 high-risk page；
- Docling JSON / Markdown 不构成 page-level visual checked 或 cell-level audited。

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

- `extraction candidate`：机器抽取候选，只能辅助定位；
- `rough reading draft`：正文可粗读，但表格、图像、公式不可直接引用；
- `degraded reading draft`：已知存在明显缺陷；
- `table-leak high risk`：表格行/图注/表注被编号为普通 `[para]`；
- `primary reading substrate`：通过 routing / leak scan / 基础 QC，可进入文献阅读；
- `restored manuscript`：完成逐章还原和必要视觉 QC；
- `docling candidate`：Docling 识别 / 结构化候选；
- `pymupdf candidate`：PyMuPDF / `pymupdf4llm` 识别候选；
- `page-level visual checked`：已看页面图并确认对象存在、边界正确、关键行可追溯；
- `cell-level audited`：已逐单元格核对；
- `cross-page boundary checked`：已确认跨页起止和归属；
- `pending visual QC`：尚未完成视觉复核，不能作为最终完成状态。

## Docling Candidate 到 Restoration 的进入路径

Docling 进入后续 restoration 时，应走以下路径，而不是直接替换主稿：

```text
TASK01 paragraph / section scaffold
+ Docling table / object candidate
+ PyMuPDF / pymupdf4llm baseline
+ page image / crop image
-> table inventory
-> page-level visual checked
-> restored Markdown table
-> optional cell-level audited
-> restored manuscript transclusion
```

执行规则：

- TASK01 类段落 / 章节 scaffold 仍是主阅读底稿；
- Docling Markdown / JSON 只作为表格、caption、formula、page 的候选索引；
- 每个表格候选必须写明来源：`docling candidate`、`pymupdf candidate`、`manual candidate`；
- 若 Docling 表格数量与论文表号不一致，必须在 QC 中记录为 object-mapping risk；
- 若 Docling 输出 formula-not-decoded，公式状态只能是 `formula located` 或 `pending formula restoration`；
- 若 Docling 或 PyMuPDF 对同一对象页码冲突，必须回到 page image 判断；
- 进入 restored manuscript 前，表格至少应达到 `page-level visual checked`；关键结果表才可声明 `cell-level audited`。

## Table-Leak Scan

抽取后必须扫描 `manuscript_paragraphs.md` 和 section 文件：

- `[para]` 中出现 `Table N`、`Panel A/B/C`、`(1) (2) (3)`；
- `[para]` 中出现连续系数、标准误、显著性星号、`N`、`R2`；
- summary statistics、correlation matrix、PCA、regression rows 被编号为普通段落；
- figure/table captions 或 notes 混入正文段落；
- appendix / references / back matter 被误判为正文 section。

输出建议：

```text
logs/table-leak-qc.md
```

若命中，应列出受影响页、受影响 `[para]` 范围、对象名和下一步修复路径。该稿只能作为 `table-leak high risk`，直到关键表被移入 `outputs/tables-restored/` 并完成相应视觉 QC。

## Technical Extraction Forward-Test TASK 模板

当新增重抽取器、第一次在某类论文上使用 Docling，或用户要求比较抽取效果时，优先开一个独立 TASK，避免覆盖主 restoration：

```text
tasks/TASKxx-Docling抽取对比/
├── TASKxx-说明.md
├── logs/
│   ├── docling-convert.log
│   ├── pymupdf4llm-baseline.log
│   └── extraction-routing-qc.md
└── outputs/
    ├── docling/
    ├── pymupdf4llm/
    ├── page-images/
    ├── comparison-report.md
    └── metadata.json
```

该 TASK 的目标是比较候选抽取效果，不是完成 full restoration。它必须明确写：

- source PDF；
- existing baseline TASK；
- PDF diagnosis；
- tool versions；
- command and timing；
- fallback / warning events；
- Docling object inventory；
- comparison against existing baseline；
- helpful scenarios；
- non-replaceable QC steps；
- final status: `not_full_restoration: true`。

## Forward-Test Green / Red

Green：

- preflight 已记录工具版本和可用性；
- Docling candidate、baseline candidate、metadata 和日志已保存；
- comparison report 明确说明 Docling 的帮助、风险和适用场景；
- object inventory 区分 table object、paper table number、caption、formula；
- 高风险页、bbox warning、formula-not-decoded、caption/order risk 已进入 QC；
- 最终状态明确不是 full restoration。

Red：

- 把 Docling Markdown 直接当作 restored manuscript；
- 把 Docling table object count 直接当成论文表格数量；
- 看到 Markdown table 就跳过 page image visual QC；
- 把 `formula-not-decoded` 当作公式已还原；
- 把 `extraction_method = docling` 写成 `visual checked`；
- 用 Docling 输出覆盖已有 TASK 的 paragraph / section scaffold；
- 未记录 CLI 失败参数、fallback、bbox warning 等 provenance。

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
object_inventory:
high_risk_pages:
comparison_report:
not_full_restoration:
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
