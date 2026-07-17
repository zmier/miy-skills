# Scholar PDF Markdown Restoration Log

## 2026-07-05 ReAct: 借鉴 book-to-skill 增强 PDF restoration 前置工程层

### Trigger

在基金经理研究项目中抽取 RFS 论文 PDF 时，暴露出一个流程问题：机器抽取 Markdown 不等于完成 `scholar-pdf-markdown-restoration`。尤其是表格、图像和公式对象，必须经过 PDF page image / crop image 的视觉复核，不能只把 `pending visual QC` 写进日志后宣称完成。

随后回查本机历史实践，发现 `book-to-skill` 工具已经在资产定价项目中使用过 Docling technical extraction：

- vendor: `workflows/../vendors/book-to-skill`
- historical project clone: `02 Sources/SMK/0 学术体系/实证资产定价-横截面股票收益/tools/book-to-skill`
- key function: `extract_with_docling()`
- key option: `pipeline_options.do_table_structure = True`
- historical output: `extraction_method = docling`, `extraction_mode = technical`

### 用户困惑

用户关心的不是“是否把 book-to-skill 整体搬进来”，而是：

1. `scholar-pdf-markdown-restoration` 是否应吸收 `book-to-skill` 的工程化抽取经验；
2. Docling 是否适合辅助 restoration / QC；
3. 除 Docling 外，`book-to-skill` 中的模式路由、preflight、metadata、fallback、成本估计、按需读取、分层输出、增量更新等流程知识，是否能增强本 Skill；
4. 图、表处理是否可以借助 Docling 或其他工具增强，但不削弱视觉复核硬门槛。

### 初步判断

`scholar-pdf-markdown-restoration` 应定位为一个复合 Skill，而不是单一线性脚本 Skill：

```text
scholar-pdf-markdown-restoration
= 诊断路由型前置抽取层
  + 工序型学术 PDF 原文还原层
  + 强制视觉 QC / provenance 层
```

前段可借鉴 `book-to-skill`，先判断 PDF 类型、任务目标和可用工具，再选择粗抽取路线。中后段仍维持原有主轴：逐章还原、段落校准、公式 LaTeX、Figure 裁剪、表格 Markdown / 截图兜底、back matter 并入、视觉 QC 和 restoration provenance。

### 可迁移内容

- PDF 类型 / 任务深度路由：
  - `text-heavy`
  - `table-heavy`
  - `formula-heavy`
  - `scanned`
  - `back-matter-heavy`
  - `quick-draft`
  - `full-restoration`
  - `cell-level-table-audit`
- preflight 依赖检查：
  - Docling
  - PyMuPDF / `fitz`
  - `pymupdf4llm`
  - Poppler / `pdftoppm`
  - `pdftotext`
  - `pypdf`
  - `pdfplumber`
  - page image rendering path
- 多抽取器 routing / fallback：
  - Docling technical extraction as structure-aware candidate;
  - PyMuPDF / `pymupdf4llm` as text / Markdown baseline;
  - `pdftotext` / `pypdf` as text fallback;
  - vision-first restoration when extraction quality is poor.
- standardized metadata:
  - source PDF;
  - extraction method;
  - extraction mode;
  - tool versions;
  - page count;
  - output paths;
  - fallback events;
  - pending visual QC objects.
- large-document access:
  - use `rg`, `sed`, page inventories and object inventories instead of loading the whole extraction into context.
- output layer separation:
  - raw extraction;
  - paragraph draft;
  - restored manuscript;
  - visual QC logs;
  - audit-ready manuscript.
- update / fold-in:
  - allow later passes to add Docling output, table visual QC, figure crops, or cell-level audits without regenerating everything from scratch.

### Docling 的合理位置

Docling 可以作为：

- structure-aware extractor;
- table candidate generator;
- figure / caption / layout object discovery helper;
- second opinion against PyMuPDF / `pymupdf4llm` output.

Docling 不能作为：

- visual QC 的替代；
- 表格 cell-level audit 的替代；
- `[para N]` 自然段边界的最终权威；
- Figure 精准裁剪和 Obsidian 嵌入的最终执行者；
- “完整 restored manuscript 已完成”的充分条件。

最终权威仍是：

```text
PDF page image / crop image + 模型视觉复核 + QC provenance
```

### 图表增强方向

拟新增“图表多源处理策略”：

1. object discovery:
   - 用 Docling / PyMuPDF / `pymupdf4llm` 识别 table、figure、caption、page；
2. candidate extraction:
   - 表格用 Docling 产 Markdown 候选；
   - 图像用 PyMuPDF 产 page image / crop 候选；
3. cross-extractor comparison:
   - 对比 Docling、PyMuPDF / `pymupdf4llm`、raw text；
   - 标记表头错位、缺 notes、caption 缺失、对象页码冲突；
4. visual authority:
   - 最终以 PDF page image / crop image 视觉复核为准；
5. QC provenance:
   - 每个对象记录来源和状态，例如：
     - `docling candidate`
     - `pymupdf candidate`
     - `page-level visual checked`
     - `cell-level audited`
     - `cross-page boundary checked`
     - `pending visual QC`

### 暂不提升为稳定规则的部分

- 不把 Docling 设为默认抽取器；
- 不把 Docling 输出视为已视觉核验；
- 不强制每篇论文都跑多抽取器；
- 不把 `book-to-skill` 的“书转 Skill / 框架提炼”目标迁移进本 Skill；
- 不在没有回归样本前拆出多个子 Skill。

### 下一步

1. 在 `SKILL.md` 中补充“复合 Skill / routing”定位；
2. 增加“PDF 类型与任务深度诊断”步骤；
3. 增加“preflight / extraction metadata / fallback”要求；
4. 增加“Docling as optional technical extractor / second opinion”的边界；
5. 增加“图表多源处理策略”；
6. 保持现有 restoration / visual QC / completion standards 不降低；
7. 用基金经理 RFS 论文作为 forward-test，检验增强后的 Skill 是否能避免“粗抽取被误报为完成”。

### Git 状态备注

截至本日志创建时，`miy-skills` 工作树已有多组未提交变更，包括 workflow-research、workflow-tao references、`vendors/book-to-skill` submodule、`vendors/larksuite-cli` submodule 和若干既有 skills 状态。建议在增强本 Skill 前先划分提交边界：

- 一个提交保存 workflow-research / workflow-tao 的结构性讨论与 references；
- 一个提交保存 vendor submodule 引入；
- 一个提交保存 `scholar-pdf-markdown-restoration` 的本次增强。

若暂不整理提交，也可以继续修改，但最终提交时应避免把不相关既有脏状态混入本 Skill 的增强提交。

## 2026-07-05 ReAct: RFS Docling forward-test 后的规则提升

### Trigger

在基金经理研究项目中，对 RFS 论文 `Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance` 开了独立 `TASK02-Docling抽取对比`，用新版 `scholar-pdf-markdown-restoration` 路由思路做 forward-test。

该 TASK 没有覆盖 TASK01，也没有宣称完成 full restoration。它只比较：

- TASK01 pdfplumber paragraph / section scaffold；
- Docling technical extraction Markdown / JSON；
- `pymupdf4llm` baseline；
- 少量 page image spot check。

### Observation

Docling 2.107.0 对 26 页 born-digital / table-heavy RFS PDF 约 30 秒完成 technical extraction。结果：

- 识别 17 个 table objects；
- 识别 17 个 caption labels；
- 识别 8 个 formula labels；
- 对 Table 1-14 等表格生成了比 TASK01 prose dump 更可用的 Markdown / JSON 候选；
- 对 table inventory、高风险页定位和表格重建初稿有明确增量。

同时发现：

- `table object count != paper table count`；
- 公式可能输出 `formula-not-decoded`；
- caption、table note、正文仍会粘连或错序；
- 标题层级可能误判；
- 横向表格页可能出现 bbox / provenance clamp warning；
- Docling candidate 不能替代 page-level visual checked 或 cell-level audited。

### 提升为稳定规则

已提升到 `references/extraction-routing.md` 和 `SKILL.md`：

- 对 RFS / JF / JFE / finance empirical paper、回归表密集论文、TASK 粗抽取中表格被压成 prose dump 的情形，优先触发 Docling technical extraction 作为候选层；
- 增加 `TASKxx-Docling抽取对比/` 标准结构；
- 增加 Docling candidate 到 restoration 的进入路径：

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

- 增加 Forward-Test Green / Red 标准；
- 增加 object inventory、object-mapping risk、high-risk pages、formula-not-decoded、bbox/provenance warning 的 QC 要求；
- 明确 forward-test 的 Green 是 comparison report / metadata 完整，不是 restored manuscript 完成。

### 仍保留为边界

- 不把 Docling 设为所有 PDF 的默认抽取器；
- 不把 Docling 输出作为 restored manuscript 主稿；
- 不把 Docling table object 数量当作论文表格数量；
- 不把 formula label / formula-not-decoded 视为公式还原；
- 不把 table Markdown 视为已通过 visual QC；
- 不强制每篇论文都开 Docling 对比 TASK，只有 table-heavy / technical / first-use / extraction quality unclear 时触发。

## 2026-07-06 ReAct: CASE-260521 weekend effort table-leak 反例

### Trigger

在基金经理研究项目 TASK01 中，`2025 (Not) Everybody's Working for the Weekend A Study of Mutual Fund Manager Effort` 被直接复用轻量 `pdfplumber` 脚本抽取为 `manuscript_paragraphs.md`。用户指出 `[para 191]` 到 `[para 199]` 实际是 Table 2 的回归表行，却被编号成普通自然段。

复查后确认：

```text
Table 1 begins around PDF page 43 and leaks into numbered paragraphs;
Table 2 on PDF page 44 leaked into [para 189]-[para 200];
Table 3 begins on PDF page 45 and leaks from [para 201] onward;
later main tables and appendix tables also show similar risk.
```

### Root Cause

本 Skill 已经写明 Docling / 多抽取器可以用于 table-heavy paper，也写明表格不能作为普通 `[para]`。但流程缺少不可绕过的硬闸门：

```text
PDF input
  -> SHOULD HAVE: extraction routing gate
  -> SHOULD HAVE: table-leak scan gate
  -> THEN: rough extraction / restoration
```

实际执行时直接走了：

```text
PDF input
  -> reuse pdfplumber script
  -> manuscript_paragraphs.md
```

因此，问题不是 Docling 表现不符合预期，而是 routing gate 没有触发，table-leak scan 也没有阻止粗稿被继续使用。

### Rule Upgrade

已提升为稳定规则：

- 抽取前必须生成 `logs/extraction-routing-qc.md`；
- empirical finance / accounting / management paper、表格密集论文、实验设计阅读任务必须考虑 Docling / 多抽取器候选；
- 抽取后必须执行 table-leak scan；
- 若 `[para]` 中出现 Table / Panel / 回归列号 / 系数 / 标准误 / N / R2 / 显著性星号等密集表格结构，强制状态为 `table-leak high risk`；
- `table-leak high risk` 不得称为 `primary reading substrate` 或 `restored manuscript`；
- 只能作为 `extraction candidate` / `degraded reading draft`，除非关键表已恢复并完成相应视觉 QC。

### Status Vocabulary

新增状态词体系：

```text
extraction candidate
rough reading draft
degraded reading draft
table-leak high risk
primary reading substrate
restored manuscript
```

### Lesson

Docling 不需要成为所有 PDF 的默认抽取器，但 table-heavy empirical paper 不能再默认走轻量脚本。默认路径必须 fail closed：没有 routing QC 和 table-leak scan，就不能交付为阅读底稿。
