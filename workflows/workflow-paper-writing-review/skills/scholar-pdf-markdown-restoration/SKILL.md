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

## 核心原则

- `[para N]` 对应 PDF 中一个自然段；标题不占用段落编号。
- Markdown 必须尽量忠实于 PDF 原文；不能为了分段整洁而改写作者措辞。
- 抽取产物应按章节组织；单文件总稿可作为主底稿，必要时同时输出逐章节 Markdown。
- 抽取前应先判断 PDF 类型和任务深度；text-heavy、table-heavy、formula-heavy、scanned、back-matter-heavy PDF 可以走不同粗抽取路线。
- Docling / PyMuPDF / `pymupdf4llm` / `pdftotext` / `pypdf` 等工具只能作为候选抽取器或 second opinion，不能替代视觉复核和 restored Markdown 的完成标准。
- 对 table-heavy / formula-heavy / technical born-digital PDF，可用 Docling technical extraction 生成结构化候选；但 `extraction_method = docling` 不等于 `visual checked` 或 `cell-level audited`。
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
2. 做 PDF 类型与任务深度诊断；如需选择抽取器或 fallback，读取 [extraction-routing.md](references/extraction-routing.md)。
3. 做 preflight：确认粗抽取器、页面渲染工具和 page image 路径可用，并记录到 extraction / restoration QC。
4. 如无抽取产物，创建或复用项目内脚本，生成分章节 Markdown、back matter/raw 输出、图像/图表素材、metadata 和 extraction log。
5. 对复杂图表或公式 PDF，可生成多抽取器候选，例如 Docling technical output 与 PyMuPDF / `pymupdf4llm` baseline，并标记来源。
6. 建立可人工修订的还原稿目录，例如 `outputs/sections-restored/` 和 `outputs/manuscript_restored.md`。
7. 建立或更新 `logs/restoration-qc.md`；如果项目已有命名约定，也可使用 `logs/segmentation-qc.md`。
8. 做全局结构检查：
   - 标题顺序是否完整；
   - 段落编号是否连续；
   - 正文与 back matter 是否分离；
   - 正文顺序是否与 PDF 一致；
   - 是否存在明显重复、缺失、半句开头、错序、乱码或公式碎片。
9. 建立视觉复核素材：
   - 渲染所有表格页、图像页、公式高风险页和跨页边界页；
   - 将页面图保存到 `outputs/page-images/`；
   - 对表格密集论文生成 contact sheet；
   - 若本轮有表格或图像，必须在继续前确认 page image 可打开。
10. 对需要视觉核验的章节，读取 [vision-restoration-rules.md](references/vision-restoration-rules.md)，按 rendered PDF page image 做 vision-first 还原；表格、图像和跨页对象不得跳过视觉复核。
11. 逐章进行模型还原修订：
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
12. 对图表执行多源处理：
   - 使用 Docling / PyMuPDF / `pymupdf4llm` 输出作为对象发现和结构化候选；
   - 以 PDF page image / crop image 作为最终视觉权威；
   - 在 QC 中记录 `docling candidate`、`pymupdf candidate`、`page-level visual checked`、`cell-level audited` 等状态；
   - 不得用抽取器输出替代视觉复核状态。
13. 还原 back matter：
   - 对照 PDF 检查 Conclusion 之后是否有 Conflict of Interest Statement、References、Data Availability、Funding、Acknowledgments、Appendix 等；
   - 将这些内容加入主 restored manuscript 的末尾；
   - 如存在逐章节输出，则创建独立 back matter section 文件，例如 `sections-restored/26-references.md`；
   - 不给 back matter 条目分配 `[para N]`；
   - 若参考文献只存在于 raw back matter 而未并入 restored manuscript，视为未完成。
14. 做高风险区域核查：
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
15. 做图表视觉复核并写入日志：
   - 表格至少生成或更新 `logs/table-visual-qc.md`；
   - 图像至少生成或更新 `logs/figure-visual-qc.md`；
   - 每张表/图必须有对象编号、PDF 页码、page image 路径、复核状态和剩余风险；
   - 若只完成页面级复核，写 `page-level visual checked`，不要写成 `cell-level audited`；
   - 若发现作者正文叙述与 PDF 表格不一致，必须在 QC 中单列为 `author-prose-conflict` 或同类标签。
16. 给每个错误打标签：
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
17. 对系统性错误修复规则或脚本，必要时重跑抽取命令；不要用重跑替代逐章还原。
18. 复查受影响区域，并确认没有引入新的错段或错序。
19. 汇总 QC 状态，说明是否可进入审稿阅读或写作分析阶段；如果视觉复核仍未完成，只能说明“可作为粗底稿”，不能说明“完整还原完成”。

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
- `logs/restoration-qc.md`
- `logs/segmentation-qc.md`
- `logs/table-visual-qc.md`
- `logs/figure-visual-qc.md`

QC 记录至少包含：

- source PDF 和抽取产物路径；
- 本轮核查日期；
- PDF 类型、任务深度、抽取工具、脚本和命令；
- extraction method / extraction mode / fallback events / tool versions；
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
- 已生成按章节组织的 Markdown；如果没有逐章节文件，QC 记录需说明单文件总稿为何足够。
- 正文段落编号连续，且标题不占用编号。
- 高风险页和跨页边界已按 rendered PDF page image 做视觉核验。
- 涉及表格或图像时，已生成 page image，并在 QC 中逐项列出复核状态；不能只写“需要视觉复核”。
- 跨页表格已确认起止页和归属；若只完成页面级复核而非逐单元格校对，必须明确写出。
- 标题层级已按全文语义结构核查，不只是接受抽取器输出。
- 公式已完整还原为 `$$...$$` LaTeX，且不再停留在 raw equation block。
- Figure 图像已精准裁剪并用 Obsidian 图片语法嵌入正文或对应章节。
- 表格已尽可能还原为 Markdown 表；复杂表格至少有可显示截图、表题、注释和页码。
- 表格最终状态不得停留在 `needs visual QC` / `pending visual QC`，除非本轮明确按失败或降级结束。
- References、Conflict of Interest Statement、Data Availability、Funding、Acknowledgments、Appendix 等 back matter 已作为独立 restored section 保留，不占用 `[para N]`，且没有只停留在 raw back matter。
- 脚注和 back matter 有合理处理，并说明与正文的关系。
- 高风险区域已按 PDF 对照核查。
- 已发现的系统性错误通过脚本或规则修复；单章局部错误直接在 restored Markdown 中修订。
- QC 记录说明哪些文本和段落已经可信，哪些区域仍需谨慎。
- 项目 README 或 TASK 说明能指向最新段落底稿和 QC 记录。

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
