---
name: scholar-pdf-markdown-restoration
description: 将学术 PDF 抽取、分章节还原为 Markdown，并使用模型理解能力逐章修复原文还原质量与自然段边界。用于论文写作、投稿前自审、外部审稿和逐段审读中，需要把 PDF 手稿转成分章节 Markdown、完整还原标题、段落、公式 LaTeX、表格、图像/图注、脚注、特殊字符和正文顺序，同时确认 `[para N]` 是否对应 PDF 自然段、嵌入 Obsidian 可显示图片链接、必要时修改辅助脚本并输出 restoration QC 记录的场景。本 Skill 属于 workflow-paper-writing-review 的基础设施型子 Skill。
---

# Scholar PDF Markdown Restoration

## 定位

本 Skill 不负责生成最终审稿意见，也不负责判断论文贡献是否成立。它负责把 PDF 手稿抽取并还原为分章节 Markdown，再使用模型理解能力逐章修复该 Markdown，使其成为忠实于原文、可直接阅读、且可稳定引用定位的审读底稿。

上层目标是原文还原：保留正文顺序、标题层级、自然段、公式、表格、图像、图表标题、脚注、引用、特殊字符和作者原始措辞。`[para N]` 是定位层，用来支持写作分析、逐段审读、问题台账和审稿讨论。

不追求复刻 PDF 的视觉排版；追求可读、可核、可重跑、可定位。

本 Skill 是一个复合型 Skill：

```text
诊断路由型前置抽取层
+ 工序型学术 PDF 原文还原层
+ 强制视觉 QC / provenance 层
```

前置抽取层负责判断 PDF 类型、任务深度、可用工具和 fallback 路线；中后段 restoration / QC 主轴保持不变。粗抽取器只产生候选材料，不产生最终可信度。

## 触发条件

当用户提到以下任务时使用：

- 判断 PDF 转 Markdown 后的分段是否准确；
- 将 PDF 抽取为按章节组织的 Markdown；
- 判断 PDF 转 Markdown 后是否忠实还原原文；
- 核对 `[para N]` 是否对应 PDF 自然段；
- 逐章修复 PDF 抽取脚本产生的错字、漏句、错序、错段、漏段、合段、标题错误、公式碎片或图表泄漏；
- 将公式完整还原为 Markdown/Obsidian 可渲染的 LaTeX `$$...$$`；
- 将图片、图表截图或导出的图像用 Obsidian 图片嵌入语法链入正文；
- 为审稿、投稿前自审、论文写作逆向分析创建可引用的段落底稿；
- 生成 `restoration-qc.md`、`segmentation-qc.md` 或同类核查报告。

## 输入

优先读取同一 project / TASK 中的这些材料：

- 原始 PDF；
- 段落编号 Markdown；
- PDF 抽取脚本；
- extraction log；
- project README 或 TASK 说明。

如果没有现成脚本，先确认项目是否已有 PDF 抽取约定；没有约定时，应创建项目内可复现脚本，把依赖、命令、输入输出和 QC 记录写入项目文件。

可选但推荐准备：

- PDF 页面截图或图表区域截图；
- 导出的图像文件目录，例如 `outputs/assets/` 或 `outputs/figures/`；
- raw text / back matter / table inventory，用于辅助人工级还原。

当需要用模型视觉能力逐页/逐章修复粗抽取稿时，读取 [vision-restoration-rules.md](references/vision-restoration-rules.md)。

当需要选择抽取器、判断是否使用 Docling technical extraction、记录 extraction metadata 或设计 fallback 时，读取 [extraction-routing.md](references/extraction-routing.md)。

## 本机 Docling 入口

在 `/Users/narra/Documents/alib/Writer` 这套工作区中，Docling 已安装在共享虚拟环境中。优先复用该入口，不要优先用 `uvx --from docling docling` 新建隔离环境。

- Docling CLI：`/Users/narra/Documents/alib/Writer/.venv/bin/docling`
- Python 入口：`/Users/narra/Documents/alib/Writer/.venv/bin/python`
- 已验证版本：`docling 2.107.0`（2026-07-09）

推荐命令模板：

```bash
/Users/narra/Documents/alib/Writer/.venv/bin/docling convert --to md --no-ocr --output outputs/docling "manuscript.pdf"
```

使用建议：

- 对已有文本层的 born-digital / FineReader OCR PDF，先尝试 `--no-ocr`，保留 PDF 文本层并减少重复 OCR 成本。
- 对扫描件或文本层明显缺失的 PDF，再启用 `--ocr` 或 `--force-ocr`，并在 routing QC 中说明。
- 若该入口缺失、版本冲突或任务必须使用新版本，才 fallback 到项目 venv / `uvx` / 其他安装方式，并把实际命令和版本写入 `logs/extraction-routing-qc.md` 或对应 extraction metadata。
- 不论使用哪个 Docling 入口，其输出状态仍只能从 `extraction candidate` / `rough reading draft` 起步；不得因为使用 Docling 而省略 routing gate、table-leak scan 或必要视觉复核。

## 状态词

本 Skill 必须使用明确状态词，避免把粗抽取稿误当 restored manuscript：

```text
extraction candidate = 机器抽取候选，只能辅助定位，不可作为主阅读底稿；
rough reading draft = 正文可粗读，但表格、公式、图像和关键页仍需回 PDF；
degraded reading draft = 已知存在明显缺陷，只能降级使用；
table-leak high risk = 表格行/图注/表注被编号为普通 [para]，不能作为经验设计阅读底稿；
primary reading substrate = 已通过 routing / leak scan / 基础 QC，可进入文献阅读；
restored manuscript = 完成逐章还原和必要视觉 QC 的可信稿。
```

除非满足完成标准，不得使用 `primary reading substrate` 或 `restored manuscript`。

## 核心原则

- `[para N]` 对应 PDF 中一个自然段；标题不占用段落编号。
- Markdown 必须尽量忠实于 PDF 原文；不能为了分段整洁而改写作者措辞。
- 抽取产物应按章节组织；单文件总稿可作为主底稿，必要时同时输出逐章节 Markdown。
- 抽取前应先判断 PDF 类型和任务深度；text-heavy、table-heavy、formula-heavy、scanned、back-matter-heavy PDF 可以走不同粗抽取路线。
- Docling / PyMuPDF / `pymupdf4llm` / `pdftotext` / `pypdf` 等工具只能作为候选抽取器或 second opinion，不能替代视觉复核和 restored Markdown 的完成标准。
- 对 table-heavy / formula-heavy / technical born-digital PDF，可用 Docling technical extraction 生成结构化候选；但 `extraction_method = docling` 不等于 `visual checked` 或 `cell-level audited`。
- 对首次使用 Docling 的论文类型、表格密集论文或抽取器效果不明的任务，应先开独立 forward-test / comparison TASK；不得用 Docling 输出覆盖已有 paragraph / section scaffold。
- Docling table object 数量不等于论文表格数量；必须记录 object-mapping risk，并用 PDF page image 判断表号、panel、caption、notes 和跨页边界。
- 若 Docling 输出 `formula-not-decoded` 或 bbox / provenance warning，该对象或页面必须标为 high-risk，不能进入公式还原或表格核验完成状态。
- 原文顺序优先于 Markdown 美观；任何重排、合并或省略都要能从 PDF 结构中解释。
- 脚本只是粗抽取工具；逐章还原时应主动使用模型的语言、数学、视觉和版面理解能力修复 Markdown。
- 对复杂或高风险页面，优先对照渲染后的 PDF 页面图进行 vision-first 还原；不要把机器抽取结果当作权威原文。
- 标题层级必须按全文语义结构和编号关系判断，不能只按字体大小或抽取器输出判断。
- 跨页处必须检查是否有自然段断裂、重复、漏句、图表打断正文或页眉页脚混入正文。
- 公式必须从 PDF 对照还原为 LaTeX display math，使用 `$$...$$`；不要满足于 raw equation block。
- 正文中的 `[Insert Figure/Table ... about here]` 是插入位置，不是图表本体；应保留插入位置页，同时链接文末实际 Figure/Table 位置。
- Figure 应精准裁剪 PDF 中的图像区域，包含图题、Alt Text、图本体和 notes，并用 Obsidian 图片嵌入语法链接，例如 `![[figures-restored/figure-01.png]]`。
- 表格应优先还原为 Markdown table，并在正文插入位置用 Obsidian transclusion 嵌入，例如 `![[tables-restored/table-01.md]]`；截图只作为核对材料或复杂表格的兜底。
- 只要本轮任务涉及表格、图像、公式截图或 PDF 版面对象，必须渲染对应 PDF page image 并做视觉复核；不得只写“需要视觉复核”后把任务报告为完成。
- 公式、表格、图注、参考文献、页眉页脚、页码和行号不得作为普通正文段落编号。
- References、Conflict of Interest Statement、Data Availability、Funding、Acknowledgments、Appendix 等 back matter 不占用 `[para N]`，但必须作为独立 restored Markdown section 保留；不能只留在 raw back matter 中。
- 对单篇项目的最终可审读稿，可以逐章直接修订 Markdown；若发现系统性错误，再回头改脚本或规则并重跑。
- 被用于正式审稿判断、逐段批注或审稿意见定位的段落，必须在 QC 记录中标为已按 PDF 核验。
- 单篇稿件中的特殊规则只写入项目 TASK；反复出现的规则才回流到 workflow / Skill。

## Preflight / Extraction Routing Gate

任何 PDF 抽取前，必须先完成 routing gate，并写入 `logs/extraction-routing-qc.md`。不得跳过 routing gate 直接复用默认脚本。

`extraction-routing-qc.md` 至少记录：

- PDF 类型：
  - `text-heavy`
  - `table-heavy`
  - `formula-heavy`
  - `scanned`
  - `back-matter-heavy`
  - `mixed`
- 任务深度：
  - `quick extraction candidate`
  - `rough reading draft`
  - `primary reading substrate`
  - `full restoration`
  - `cell-level table audit`
- 是否为 empirical finance / accounting / management paper；
- 是否存在多张回归表、summary statistics、appendix tables、figure/table placeholders；
- 是否会在后续任务中使用变量定义、系数、显著性、样本量、R2、机制表或 robustness 表；
- 默认抽取器是否足够；
- 是否触发 Docling / `pymupdf4llm` / PyMuPDF / `pdftotext` / OCR / vision-first fallback；
- 输出允许进入的最高状态词。

### Docling / 多抽取器触发条件

若满足以下任一条件，必须考虑 Docling technical extraction 或多抽取器候选；若决定不用，必须在 `extraction-routing-qc.md` 中说明原因：

- empirical finance / accounting / management paper；
- 正文或 appendix 有多张回归表、summary statistics 或 robustness tables；
- PDF 或粗抽取中出现 `Table`、`Panel`、`(1) (2) (3)`、系数、标准误、`N`、`R2`、显著性星号等密集结构；
- 用户目标是实验设计、变量构造、识别策略学习、机制/异质性/稳健性提取；
- 研究判断会依赖表格或图形证据；
- 首轮抽取器效果不明，或已有抽取出现 table prose dump / table-leak。

Docling / 多抽取器输出只能作为 `extraction candidate` 或结构化 second opinion，不能直接替代视觉复核和 restored Markdown。

## Post-Extraction Table-Leak Scan Gate

任何生成 `manuscript_paragraphs.md` 或分章稿后，必须执行 table-leak scan，并将结果写入 `logs/table-leak-qc.md` 或 `logs/table-visual-qc.md`。

扫描至少检查：

- `[para N]` 中是否出现 `Table N`、`Panel A/B/C`、`(1) (2) (3)`、`N`、`R2`、standard errors、显著性星号；
- 是否存在连续多段短行呈现回归表行；
- 是否有 summary statistics / correlation matrix / PCA / appendix table 被编号为普通自然段；
- 表格、图题、图注、表注、figure/table placeholders 是否混入普通正文；
- References / appendix / back matter 是否被误分为正文 section。

若 table-leak scan 命中，强制状态为：

```text
table-leak high risk
not restored manuscript
not primary reading substrate for empirical design extraction
```

此时必须：

- 在 README / TASK / QC 中明示 `table-leak high risk`；
- 建立 table inventory 或至少列出已知受影响页；
- 把可修复表格移入 `outputs/tables-restored/table-XX.md`，正文位置使用 transclusion；
- 若只完成 page-level visual check，不得写成 `cell-level audited`；
- 在后续交给 `research-literature-reader` 时声明它只能作为 candidate / degraded draft，除非关键表已恢复。

## 大模型视觉复核硬门槛

这是本 Skill 的完成门槛，不是可选建议。

当任务涉及表格、图像、图注、公式截图、跨页对象或用户明确要求“完整还原”时，必须执行以下动作：

这里的“视觉复核”明确指使用大模型视觉能力读取渲染后的 PDF 页面图、表格截图、图形截图或裁剪图，而不是只依赖文本抽取、OCR、表格解析器或模型凭文本推断。视觉复核的对象必须是原始 PDF 渲染图或从原始 PDF 裁剪出的图像。

1. 渲染 PDF 页面图：
   - 表格页、图像页、公式高风险页必须生成 page image；
   - 推荐保存到 `outputs/page-images/page-XX.png`；
   - 多页表格或跨页对象应额外生成 contact sheet，例如 `outputs/page-images/contact-tables.png`，用于检查表格起止与跨页边界。
2. 对照页面图做视觉复核：
   - 检查表题、列名、关键变量行、系数、显著性星号、t 值/标准误、样本量、R2、表注是否在 Markdown 或 raw table text 中可追溯；
   - 对跨页表格，必须确认上一页表尾和下一页表头/表尾没有被粘连、遗漏或归入错误表格；
   - 对图像，必须确认标题、图本体、图例、坐标轴、notes/caption 未缺失。
   - 对后续可能进入论证树或验箭头的表格/图形，必须用大模型视觉能力对照原图判断 restored Markdown / evidence ledger 是否存在错列、漏星、错显著性、正文-表格冲突或图形解释风险。
3. 写入视觉复核日志：
   - 推荐文件名：`logs/table-visual-qc.md`、`logs/figure-visual-qc.md` 或 `logs/vision-qc.md`；
   - 每个对象至少记录：对象编号、PDF 页码、page image 路径、复核层级、发现的问题、剩余风险。
4. 使用明确状态词：
   - `page-level visual checked`：已看页面图并确认对象存在、边界正确、关键行可追溯；
   - `cell-level audited`：已逐单元格人工校对；
   - `cross-page boundary checked`：已确认跨页起止和归属；
   - `needs visual QC` / `pending visual QC`：尚未完成视觉复核，只能作为中间状态，不能作为最终完成状态。
5. 最终回答和 QC 记录必须一致：
   - 如果仍有 `needs visual QC` / `pending visual QC`，最终回答必须明说“视觉复核未完成”，不能说“已完成完整还原”；
   - 如果工具缺失导致无法渲染页面图，必须先尝试替代工具或依赖环境；仍失败时按“失败与降级”处理。

禁止做法：

- 禁止把“需要视觉复核”写成已完成事项；
- 禁止只依赖 PDF 文本抽取结果恢复复杂表格后直接宣布完成；
- 禁止在未看页面图时使用 `visual checked`、`已视觉复核`、`已核验` 等表述；
- 禁止把可疑表格问题归咎于抽取器，除非已经对照页面图确认 PDF 本身没有该问题。

## 与相邻 Skills 的关系

- `pdf` / `pdf:pdf`：提供 PDF 渲染、页面检查、文本抽取和低层工具建议；可作为本 Skill 的工具层，但不负责 restored Markdown 的逐章还原。
- `markitdown`：可作为粗抽取候选，用于快速得到 LLM-friendly Markdown；不保证公式、表格、Figure 裁剪、段落编号和 Obsidian 嵌入满足审读底稿标准。
- `book-to-skill`：可借鉴 technical / text routing、Docling extraction、preflight、metadata、fallback 和大文档按需读取；不迁移其“书转 Skill / 框架提炼”目标。
- `split-pdf`：适合把论文拆分后深读并产出结构化阅读笔记；不负责把原文还原成可引用的 restored Markdown。
- `manuscript-quick-reconstruction`：应在可靠 restored Markdown 之后使用，用于贡献链快速还原；如果 Markdown 底稿不可靠，先回到本 Skill。

因此，本 Skill 的职责不是替代上述 Skills，而是编排 PDF 工具、Markdown 粗抽取、模型还原、公式/图表恢复和审读定位，产出可直接阅读和引用的 restored Markdown。

## GitHub 外部候选 Skills

需要判断是否直接安装/复用 GitHub 上的 PDF-to-Markdown Skill，或需要选择底层抽取器时，读取 [external-pdf2md-skills.md](references/external-pdf2md-skills.md)。

调研 GitHub 上的外部 Skill 时，优先区分两类对象：

- 真正包含 `SKILL.md`、可作为 agent skill 安装或改造的项目；
- 只是 PDF to Markdown CLI / library 的工具项目。

截至 2026-06-18，初步结论是：不直接用外部 Skill 替代本 Skill；采用“借鉴 + 可选抽取器”的方式。

重点候选包括：

- `yuhaoliu7456/pdf2md-skill`：借鉴 vision-first 还原、跨页连续性、公式精度和 float placement 规则。
- `neoncapy/doc2md`：借鉴工具路由、fallback、结构 QC 和 fix-and-rerun loop。
- `aliceisjustplaying/claude-skill-pdf-to-markdown`：可借鉴轻量 fast-mode 抽取、图片抽取和缓存；其输出只能作为粗抽取参考。
- Marker / Nutrient / Docling / MinerU 相关 Skill 或工具：作为可选粗抽取器或重模型 fallback，不作为 restored Markdown 的最终生产者。

这些外部 Skill 不直接替代本 Skill，原因是本 workflow 还需要：

- 按审稿项目输出分章节 restored Markdown；
- 保留和校准 `[para N]` 全文段落定位；
- 区分正文插入位置与文末实际 Figure/Table 位置；
- 精准裁剪 Figure，并用 Obsidian `![[...]]` 嵌入；
- 将 Table 优先还原为 Markdown table 文件并 transclude；
- 维护项目内 `restoration-qc.md`、TASK 说明和可复现脚本；
- 服务后续 `manuscript-quick-reconstruction` 和逐段审稿 workflow。

因此，外部 Skill 的最佳用法是作为本 Skill 的参考实现或可选抽取器，而不是替换本 Skill 的 workflow 约束。若要更改默认抽取器或新增重依赖，必须在具体 project / TASK 中先做小样本对比。

## Figure 精准裁剪

当 PDF 中的 Figure 位于文末或 back matter，而正文只出现 `[Insert Figure N about here]` 时，按以下流程处理：

1. 先在正文 restored Markdown 中保留插入位置：
   - `Insert Figure N about here`
   - `insertion position: PDF page X`
2. 从 back matter、figure inventory 或页面浏览中确认 Figure 本体所在页：
   - `actual Figure N appears in back matter on PDF page Y`
3. 将实际 Figure 所在 PDF 页渲染为高分辨率页面图，或直接用 PyMuPDF 对 PDF 页做 clip 裁剪。
4. 使用模型视觉判断或页面截图检查，确定 crop box 必须包含：
   - Figure title；
   - Alt Text，如 PDF 中存在；
   - 图本体；
   - Notes / caption / source；
   - 必要的图例和边缘箭头。
5. 保存到项目资产目录：
   - `outputs/figures-restored/figure-01.png`
6. 视觉复核裁剪结果：
   - 标题不能缺；
   - 图本体不能被裁边；
   - notes 不能丢；
   - 图中文字必须可读；
   - 如果任何元素缺失，调整 crop box 后重裁。
7. 在正文 restored Markdown 的插入位置嵌入精准裁剪图：

```markdown
> Insert Figure 1 about here
> insertion position: PDF page 7; actual Figure 1 appears in back matter on PDF page 27.

![[figures-restored/figure-01.png]]
```

8. PDF 整页图只作为核对材料，不作为正文中的 Figure 主体。

推荐使用 PyMuPDF 裁剪：

```python
import fitz

doc = fitz.open("manuscript.pdf")
page = doc[pdf_page_number - 1]
rect = fitz.Rect(x0, y0, x1, y1)
pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
pix.save("outputs/figures-restored/figure-01.png")
```

坐标可以先由页面截图粗定，再通过视觉检查迭代修正。不要把第一次裁剪视为最终结果。

## 工作流

1. 定位文件：读取 PDF、抽取产物、抽取日志、脚本和 TASK 说明。
2. 做 PDF 类型与任务深度诊断；读取 [extraction-routing.md](references/extraction-routing.md)，并生成或更新 `logs/extraction-routing-qc.md`。没有 routing QC，不得进入默认抽取脚本。
3. 做 preflight：确认粗抽取器、页面渲染工具和 page image 路径可用，并记录到 extraction / restoration QC。
4. 根据 routing gate 选择抽取路线。如无抽取产物，创建或复用项目内脚本，生成分章节 Markdown、back matter/raw 输出、图像/图表素材、metadata 和 extraction log。
5. 对复杂图表或公式 PDF、empirical finance / accounting / management paper、表格密集论文、实验设计阅读任务，生成多抽取器候选，例如 Docling technical output 与 PyMuPDF / `pymupdf4llm` baseline，并标记来源；若是首次使用 Docling 或需要比较效果，先按 `extraction-routing.md` 开独立 Docling 抽取对比 TASK。
6. 建立可人工修订的还原稿目录，例如 `outputs/sections-restored/` 和 `outputs/manuscript_restored.md`。
7. 建立或更新 `logs/restoration-qc.md`；如果项目已有命名约定，也可使用 `logs/segmentation-qc.md`。
8. 做 post-extraction table-leak scan，生成 `logs/table-leak-qc.md` 或更新 `logs/table-visual-qc.md`；若命中，强制标记 `table-leak high risk`，并不得把该稿交付为 primary reading substrate。
9. 做全局结构检查：
   - 标题顺序是否完整；
   - 段落编号是否连续；
   - 正文与 back matter 是否分离；
   - 正文顺序是否与 PDF 一致；
   - 是否存在明显重复、缺失、半句开头、错序、乱码或公式碎片。
10. 建立视觉复核素材：
   - 渲染所有表格页、图像页、公式高风险页和跨页边界页；
   - 将页面图保存到 `outputs/page-images/`；
   - 对表格密集论文生成 contact sheet；
   - 若本轮有表格或图像，必须在继续前确认 page image 可打开。
11. 对需要视觉核验的章节，读取 [vision-restoration-rules.md](references/vision-restoration-rules.md)，按 rendered PDF page image 做 vision-first 还原；表格、图像和跨页对象不得跳过视觉复核。
12. 逐章进行模型还原修订：
   - 对照 PDF 页面修复正文错字、漏句、错序、断段和误标题；
   - 按全文语义结构修正标题层级，不按字体大小机械判断；
   - 对每个跨页边界检查自然段是否断裂、重复或漏句；
   - 将每个公式重写为 `$$...$$` LaTeX；
   - 将图像或图表截图保存到项目资产目录，并用 Obsidian 语法嵌入；
   - 对正文插图/插表占位，同时记录 insertion position 和 actual figure/table location；
   - 对 Figure 执行精准裁剪流程，不用整页 PDF 截图替代 Figure；
   - 将表格转为 Markdown table 文件，同时保留表题、注释、显著性说明和 PDF 页码；
   - 正文插表位置应嵌入 Markdown table 文件，而不是优先嵌入截图；
   - 保留 `[para N]`，但不让公式、图片或表格占用正文段落编号。
13. 对图表执行多源处理：
   - 使用 Docling / PyMuPDF / `pymupdf4llm` 输出作为对象发现和结构化候选；
   - 以 PDF page image / crop image 作为最终视觉权威；
   - 在 QC 中记录 `docling candidate`、`pymupdf candidate`、`page-level visual checked`、`cell-level audited` 等状态；
   - 记录 object inventory、object-mapping risk、high-risk pages、formula-not-decoded 和 bbox/provenance warning；
   - 不得用抽取器输出替代视觉复核状态。
14. 还原 back matter：
   - 对照 PDF 检查 Conclusion 之后是否有 Conflict of Interest Statement、References、Data Availability、Funding、Acknowledgments、Appendix 等；
   - 将这些内容加入主 restored manuscript 的末尾；
   - 如存在逐章节输出，则创建独立 back matter section 文件，例如 `sections-restored/26-references.md`；
   - 不给 back matter 条目分配 `[para N]`；
   - 若参考文献只存在于 raw back matter 而未并入 restored manuscript，视为未完成。
15. 做高风险区域核查：
   - Abstract；
   - Introduction 首尾；
   - 理论假设；
   - 变量定义；
   - 公式前后；
   - 表格、图和插入占位符前后；
   - 回归结果解释；
   - Conclusion；
   - References / back matter 起止页；
   - 跨页段落。
16. 做图表视觉复核并写入日志：
   - 表格至少生成或更新 `logs/table-visual-qc.md`；
   - 图像至少生成或更新 `logs/figure-visual-qc.md`；
   - 每张表/图必须有对象编号、PDF 页码、page image 路径、复核状态和剩余风险；
   - 若只完成页面级复核，写 `page-level visual checked`，不要写成 `cell-level audited`；
   - 若发现作者正文叙述与 PDF 表格不一致，必须在 QC 中单列为 `author-prose-conflict` 或同类标签。
17. 给每个错误打标签：
   - `text-error`：文字识别错误、乱码、特殊字符错误或词语被错误改写；
   - `order`：文本顺序与 PDF 不一致；
   - `split`：一个自然段被拆成多个 `[para]`；
   - `merge`：多个自然段被合并；
   - `missing`：PDF 有但 Markdown 缺失；
   - `duplicate`：重复抽取；
   - `heading`：标题层级错误、标题缺失或标题被编号；
   - `equation`：公式缺失、错序、碎片化，或公式碎片混入正文；
   - `table-leak`：表格、图题、图注或表注混入普通正文；
   - `figure-table-missing`：图、表、标题、编号或占位位置缺失；
   - `footnote`：脚注、尾注或声明位置错误；
   - `backmatter`：参考文献、附录或声明缺失、只留 raw 未并入 restored、或混入正文编号；
   - `noise`：页眉页脚、页码、行号或系统水印混入正文。
18. 对系统性错误修复规则或脚本，必要时重跑抽取命令；不要用重跑替代逐章还原。
19. 复查受影响区域，并确认没有引入新的错段或错序。
20. 汇总 QC 状态，说明是否可进入审稿阅读或写作分析阶段；如果 routing / table-leak scan / 视觉复核仍未完成，只能说明“可作为 extraction candidate / 粗底稿”，不能说明“完整还原完成”。

## 推荐输出

在具体 project / TASK 中生成或更新：

- `outputs/*_manuscript_paragraphs.md`
- `outputs/sections/*.md`
- `outputs/sections-restored/*.md`
- `outputs/*_manuscript_restored.md`
- `outputs/assets/*` 或 `outputs/figures/*`
- `outputs/figures-restored/*`
- `outputs/page-images/*`
- `outputs/page-images/contact-*.png`
- `outputs/sections-restored/*references*.md` 或其他 back matter section 文件
- `outputs/*_back_matter_raw.md`
- `outputs/*_figures_tables.md`
- `logs/extraction-log.md`
- `logs/extraction-routing-qc.md`
- `logs/table-leak-qc.md`
- `logs/restoration-qc.md`
- `logs/segmentation-qc.md`
- `logs/table-visual-qc.md`
- `logs/figure-visual-qc.md`
- `outputs/comparison-report.md`（当本轮是抽取器 forward-test 时）
- `outputs/metadata.json`（包含 extraction method / mode / tool versions / object inventory / high-risk pages）

QC 记录至少包含：

- source PDF 和抽取产物路径；
- 本轮核查日期；
- PDF 类型、任务深度、抽取工具、脚本和命令；
- extraction method / extraction mode / fallback events / tool versions；
- routing decision、允许进入的最高状态词、是否触发 Docling / 多抽取器；
- table-leak scan 结果和已知受影响页；
- object inventory、object-mapping risk、high-risk pages 和抽取器 warning；
- 抽查范围和全检范围；
- 错误清单；
- 修复动作；
- 逐章还原进度；
- 重跑命令；
- 段落总数变化；
- 原文还原质量说明；
- 公式、图像、表格还原状态；
- PDF page image 路径和视觉复核范围；
- 每个表格/图像的复核层级：`page-level visual checked`、`cell-level audited`、`cross-page boundary checked` 或 `pending visual QC`；
- References / back matter 是否已并入 restored manuscript；
- 已核验段落范围；
- 剩余风险。

## 完成标准

- Markdown 正文顺序、标题层级、自然段和原始措辞忠实于 PDF。
- 已完成 `extraction-routing-qc.md`；没有 routing QC 的稿件不得称为 primary reading substrate。
- 已完成 table-leak scan；若命中 `table-leak high risk`，不得称为 primary reading substrate 或 restored manuscript。
- 已生成按章节组织的 Markdown；如果没有逐章节文件，QC 记录需说明单文件总稿为何足够。
- 正文段落编号连续，且标题不占用编号。
- 高风险页和跨页边界已按 rendered PDF page image 做视觉核验。
- 涉及表格或图像时，已生成 page image，并在 QC 中逐项列出复核状态；不能只写“需要视觉复核”。
- 跨页表格已确认起止页和归属；若只完成页面级复核而非逐单元格校对，必须明确写出。
- 标题层级已按全文语义结构核查，不只是接受抽取器输出。
- 公式已完整还原为 `$$...$$` LaTeX，且不再停留在 raw equation block。
- Figure 图像已精准裁剪并用 Obsidian 图片语法嵌入正文或对应章节。
- 表格已尽可能还原为 Markdown 表；复杂表格至少有可显示截图、表题、注释和页码。
- 若使用 Docling，已明确区分 `docling candidate`、`page-level visual checked` 和 `cell-level audited`；不得把 Docling table object 直接视为已还原表格。
- 若本轮只是 Docling / 多抽取器 forward-test，完成标准是 comparison report 和 metadata 完整，而不是 restored manuscript 完成。
- 表格最终状态不得停留在 `needs visual QC` / `pending visual QC`，除非本轮明确按失败或降级结束。
- References、Conflict of Interest Statement、Data Availability、Funding、Acknowledgments、Appendix 等 back matter 已作为独立 restored section 保留，不占用 `[para N]`，且没有只停留在 raw back matter。
- 脚注和 back matter 有合理处理，并说明与正文的关系。
- 高风险区域已按 PDF 对照核查。
- 已发现的系统性错误通过脚本或规则修复；单章局部错误直接在 restored Markdown 中修订。
- QC 记录说明哪些文本和段落已经可信，哪些区域仍需谨慎。
- 项目 README 或 TASK 说明能指向最新段落底稿和 QC 记录。

## 禁止事项

- 禁止绕过 routing gate 直接运行默认抽取脚本。
- 禁止在没有 `extraction-routing-qc.md` 和 table-leak scan 的情况下，把 `manuscript_paragraphs.md` 标为 primary reading substrate。
- 禁止把 table-heavy empirical paper 的 `pdfplumber` / raw text prose dump 当成可直接进入实验设计阅读的底稿。
- 禁止把 table-leak 行保留为普通 `[para]` 后继续做变量、识别或结果表提取。

## 失败与降级

如果 PDF 版式、扫描质量或公式表格密度导致自动抽取无法稳定：

- 保留机器抽取稿作为辅助阅读材料；
- 使用模型对照 PDF 页面逐章还原；
- 对关键公式、图、表采用 LaTeX 转写、截图嵌入或人工表格重建；
- 在 QC 记录中明确哪些对象已经还原，哪些对象仍需 PDF 原图辅助；
- 不把失败个案规则回流成通用 workflow 规则。

如果无法生成或读取 PDF page image：

- 先尝试项目已有脚本、bundled Python、`pdfplumber.to_image()`、PyMuPDF、Poppler、系统预览导图等替代路径；
- 将尝试过的工具、失败原因和命令写入 `logs/restoration-qc.md`；
- 不得使用 `visual checked`、`已视觉复核` 或 `完整还原完成`；
- 最终回答必须明确说“视觉复核未完成，本轮是降级产物”；
- 若用户请求的是“完整 md 文档（有 table 的）”，且表格尚未视觉复核，只能交付“临时阅读底稿/粗抽取底稿”，不能交付为“完整 restored manuscript”。
