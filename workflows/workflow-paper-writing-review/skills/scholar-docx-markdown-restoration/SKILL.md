---
name: scholar-docx-markdown-restoration
description: 将学术 DOCX 手稿转换、清理并还原为带段落编号的 Markdown 审读底稿。用于论文写作、自审、外部审稿和论证树抽取前，需要从 .docx 提取正文、标题、脚注、尾注、图片、公式、参考文献和可定位段落，生成 `[para N]` Markdown、media inventory、figure QC、restoration QC，并交给 manuscript-quick-reconstruction 或 academic-paper-argument-tree-extraction 的场景。本 Skill 属于 workflow-paper-writing-review 的基础设施型子 Skill。
---

# Scholar DOCX Markdown Restoration

## 定位

本 Skill 负责把学术 DOCX 手稿还原为可阅读、可定位、可复核、可交给后续抽树和审稿 workflow 使用的 Markdown 底稿。

它不判断论文贡献是否成立，不做审稿攻击，不抽论证树。它只解决材料准备层问题：

```text
DOCX 手稿
-> 粗转换 Markdown + media
-> 清理 Word / OOXML 噪音
-> 保留脚注、尾注、公式、图片和参考文献
-> 增加正文自然段 `[para N]`
-> 生成 restoration / segmentation / figure QC
-> 可信审读底稿
```

与 `scholar-pdf-markdown-restoration` 是兄弟 Skill：PDF Skill 处理 PDF 页图、跨页表格和视觉还原；本 Skill 处理 DOCX 结构、media 提取、脚注/尾注和 Word 转 Markdown 清理。

## 触发条件

当用户提到以下任务时使用：

- `.docx` / Word 手稿转 Markdown；
- 为审稿、抽树、逐段审读或投稿前自审创建 DOCX 底稿；
- 需要保留脚注、尾注、图片、公式、参考文献；
- 需要给 DOCX 正文增加 `[para N]` 段落编号；
- 需要从 DOCX 提取 media 并生成图像清单；
- 需要判断 DOCX 能否直接抽树，或是否必须先底稿化。

## 输入

优先读取同一 project / TASK 中：

- 原始 `.docx`；
- 项目 README / TASK 说明；
- 已有转换稿、图片目录或 extraction log；
- 若有 PDF 版本，可作为视觉或页码对照材料，但不能替代 DOCX 结构抽取。

推荐输出到当前 TASK：

```text
outputs/manuscript_raw.md
outputs/manuscript_restored.md
outputs/media/
outputs/media-inventory.md
outputs/footnotes-endnotes.md
logs/extraction-log.md
logs/restoration-qc.md
logs/segmentation-qc.md
logs/figure-qc.md
scripts/convert_docx_to_markdown.py
```

若项目已有命名约定，可按项目约定命名，但必须能清楚定位最新 restored Markdown 和 QC 文件。

## 核心原则

- DOCX 不应直接作为 full-tree 抽树输入；正式审稿或论证树抽取前，应先形成可定位 Markdown 底稿。
- `[para N]` 对应正文中的一个自然段；标题、图题、表题、脚注、尾注、参考文献、声明和附录不占正文段落编号。
- 不改写作者原文。清理 Word 噪音时只能删除转换垃圾、重复 media 标记、空段、样式残留和明显抽取噪音。
- 标题层级按 Word 结构、编号和语义共同判断；不能只依赖 Pandoc 输出。
- 图片、图题、脚注、尾注、公式、参考文献必须保留或在 QC 中明确说明缺口。
- 工科、材料、器件、实验科学论文中，图片往往是关键 evidence。不能只抽正文后声称底稿可用于 full-tree；必须建立 media inventory 和 figure QC。
- 如果 DOCX 中图表是图片而非可编辑表格，必须把它们作为 figure/image evidence 处理，并在后续抽树中标 `needs-figure-qc`，除非已经人工视觉核验。
- 这里的视觉核验明确包括使用大模型视觉能力查看 DOCX 导出的 media、图表截图、可编辑表格渲染图或由 DOCX/PDF 对照生成的页面图。不能只用文件名、alt text、Pandoc 图片引用或 OCR 文本推断图表内容。
- 如果 DOCX 中存在 track changes、批注或文本框，必须在 QC 中说明是否保留、接受、忽略或无法抽取。
- 公式若可被 Pandoc 还原，应保留为 Markdown/LaTeX；若公式变成图片或乱码，标记 `formula-qc-needed`。
- References / Acknowledgments / Funding / Data Availability / Appendix 等 back matter 必须保留，但不分配正文 `[para N]`。
- 任何无法确认的对象不得伪装为已核验；使用 `needs-qc` / `pending-qc` / `not-extracted`。

## 段落编号规则

`[para N]` 是后续审稿、抽树、证据 ledger 和对话追踪的定位层。

编号规则：

```text
正文自然段: [para 1] ...
标题: 不编号
Abstract 正文: 编号
Keywords: 通常不编号，除非正文中明确作为段落分析对象
图题 / 表题: 不编号，登记到 media-inventory 或 figure-qc
脚注 / 尾注: 不编号，登记到 footnotes-endnotes
参考文献条目: 不编号
声明 / Funding / Data Availability: 不编号，作为 back matter section 保留
```

编号必须连续。若转换中发现疑似合段、断段、空段、图片插入打断正文，应在 `logs/segmentation-qc.md` 记录：

```text
para_id | issue | source clue | action | status
```

## 推荐工具链

默认优先：

```bash
pandoc --from=docx --to=gfm --wrap=none --extract-media=outputs/media manuscript.docx -o outputs/manuscript_raw.md
```

如果需要保留更多 DOCX 结构，可辅以：

- Python `zipfile` 读取 OOXML；
- `python-docx` 或 `lxml` 统计段落、图片、脚注、尾注、批注；
- `textutil` 作为 macOS fallback；
- markitdown / mammoth 作为粗抽取对照。

外部候选工具和 Skill 参考见 [external-docx2md-skills.md](references/external-docx2md-skills.md)。

## 工作流

1. 定位输入和任务边界：
   - 记录 DOCX 路径、文件大小、是否正式审稿、是否 full-tree；
   - 建立 `outputs/`、`logs/`、`scripts/`。
2. 预检 DOCX 结构：
   - 统计正文段落数、media 数、脚注/尾注、批注、表格、文本框；
   - 写入 `logs/extraction-log.md`。
3. 粗转换：
   - 使用 Pandoc 或项目脚本生成 `outputs/manuscript_raw.md`；
   - 用 `--extract-media` 保存图片到 `outputs/media/`。
4. 生成 media inventory：
   - 列出每个 media 文件、类型、大小、尺寸、可能出现位置；
   - 若图片很大或疑似包含图表，标记 `needs-figure-qc`。
5. 提取脚注和尾注：
   - 若 Pandoc 已内联脚注，确认格式；
   - 若 OOXML 中有 footnotes/endnotes，生成 `outputs/footnotes-endnotes.md`。
6. 清理并还原 Markdown：
   - 修正标题层级；
   - 删除 Word 噪音；
   - 保留公式、图像引用、脚注引用；
   - 将正文自然段编号为 `[para N]`；
   - 输出 `outputs/manuscript_restored.md`。
7. 图像 / 图表 QC：
   - 打开或检查每个 media 文件；
   - 判断是否为图、实验照片、机制图、性能曲线、表格截图或装饰图；
   - 写 `logs/figure-qc.md`；
   - 对关键图至少标出 `image-file`、`caption/source clue`、`qc_status`、`risk`。
   - 若图片、表格截图、性能曲线、机制图、实验照片或可视化结果将作为后续论证树 evidence，必须使用大模型视觉能力查看原始 media 或渲染图，并记录 `vision-checked`、`needs-higher-resolution`、`caption-mismatch`、`axis/legend-qc`、`table-image-qc` 等状态。
   - 若 DOCX 中存在可编辑表格，应导出或渲染为可核验视图；对后续要用于结果判断的关键表格，至少做页面级/对象级视觉复核，并在 QC 中说明是否达到逐单元格核验。
8. 结构 QC：
   - 检查标题顺序、段落编号连续性、Abstract、Conclusion、References、Appendix 是否保留；
   - 检查是否存在大段乱码、公式丢失、图片缺失、脚注丢失；
   - 写 `logs/restoration-qc.md` 和 `logs/segmentation-qc.md`。
9. 交付状态判断：
   - 若正文、脚注、media inventory 和段落编号齐，可标 `ready-for-quick-reconstruction`；
   - 若图像 QC 足够，可标 `ready-for-academic-paper-argument-tree-extraction`；
   - 若关键图未核验，标 `ready-with-figure-qc-caveats`；
   - 若正文结构不可信，标 `rough-draft-only`。

## 输出模板

`logs/restoration-qc.md` 至少包含：

```text
source_docx:
conversion_command:
paragraph_count_raw:
paragraph_count_restored:
media_count:
footnotes:
endnotes:
comments:
tables:
formula_status:
figure_qc_status:
back_matter_status:
para_index_status:
ready_for_next_step:
remaining_risks:
```

`outputs/media-inventory.md` 至少包含：

```text
media_id | file | type | size | dimensions | likely_role | source_or_caption_clue | vision_qc_status | qc_status | notes
```

`logs/segmentation-qc.md` 至少包含：

```text
check | status | notes
para_count | ...
continuous_para_ids | ...
heading_not_numbered | ...
footnotes_not_numbered | ...
back_matter_not_numbered | ...
suspected_split_or_merge | ...
```

## 完成标准

- 已生成 `outputs/manuscript_raw.md` 和 `outputs/manuscript_restored.md`。
- `manuscript_restored.md` 的正文自然段带连续 `[para N]`。
- 标题、脚注、尾注、参考文献和 back matter 不占正文段落编号。
- 已提取 DOCX media，并生成 `media-inventory.md`。
- 已生成 `restoration-qc.md`、`segmentation-qc.md` 和必要的 `figure-qc.md`。
- 对关键图像、表格截图、机制图、性能曲线或实验照片，已用大模型视觉能力查看原始 media 或渲染图，并在 QC 中记录视觉复核状态；若未完成，不得标 `ready-for-full-tree`。
- QC 清楚说明是否可进入：
  - `manuscript-quick-reconstruction`;
  - `academic-paper-argument-tree-extraction`;
  - 或只能作为 rough draft。
- 若关键图片、公式或脚注未能核验，最终回答必须明说，不能声称完整 restored。

## 失败与降级

如果 Pandoc 转换失败：

- 尝试 `textutil` 或 markitdown/mammoth fallback；
- 保留失败命令和错误信息到 `logs/extraction-log.md`；
- 不能跳过底稿化直接进入 full-tree。

如果 media 与正文位置无法稳定对应：

- 仍应保存 media inventory；
- 在 restored Markdown 中保留 Pandoc 生成的图片引用；
- 在 QC 中标 `media-position-uncertain`；
- 后续抽树把相关图证据标为 `needs-figure-qc`。

如果公式大量丢失：

- 标 `formula-qc-needed`；
- 对工科/理论论文，不能直接标 `ready-for-full-tree`；
- 必要时要求 PDF 或原始 LaTeX/Word 公式截图作为补充。

## 与相邻 Skills 的关系

- `scholar-pdf-markdown-restoration`：兄弟 Skill，处理 PDF 版底稿还原。
- `manuscript-quick-reconstruction`：在可靠 restored Markdown 后调用，用于快速还原贡献链。
- `workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction`：在可靠 restored Markdown 后调用，用于抽作者论证树。
- `academic-paper-argument-tree-extraction/references/materials-hydrovoltaic-adapter.md`：材料、器件、水伏发电等工科论文抽树时读取；本 Skill 只准备底稿，不替代该 adapter。
