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
