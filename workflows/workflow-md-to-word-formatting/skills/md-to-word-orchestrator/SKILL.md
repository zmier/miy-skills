---
name: md-to-word-orchestrator
description: workflow-md-to-word-formatting 的总编排子 Skill。用于读取 md/qmd/rmd 输入、识别目标 profile、选择 Pandoc/Quarto/markdown2docx/python-docx 路线、生成转换计划、调用后处理与 QC，并输出 docx 与 style-qc-report。
---

# MD to Word Orchestrator

## 主流程

1. 确认输入和目标：
   - 输入文件路径；
   - 输出 docx 路径；
   - target profile；
   - mode。
2. 读取父 workflow 的 `references/routing.md` 和目标 profile。
3. 生成 `conversion-plan.md`：
   - 使用哪个引擎；
   - 使用哪个 reference-doc / template；
   - 是否需要 python-docx 后处理；
   - QC 项目。
4. 规范化 Markdown：
   - 标题层级；
   - 列表；
   - 表格；
   - YAML metadata；
   - 图片路径；
   - 引用/脚注。
5. 路由到转换引擎：
   - Pandoc；
   - Quarto；
   - markdown2docx；
   - custom python-docx。
6. 调用 `docx-style-postprocessor`。
7. 调用 `docx-style-qc`。
8. 输出交付：
   - `.docx`；
   - `conversion-log.md`；
   - `style-qc-report.md`。

## 决策纪律

- 如果是外刊 manuscript 且有 Quarto journal template，优先 Quarto。
- 如果是普通 md 到审稿意见 Word，优先 Pandoc + reference-doc。
- 如果 Pandoc reference-doc 样式不够，使用 python-docx 后处理修正文体、段落、标题和列表。
- 如果用户提供的是复杂 Word 模板且希望保留固定页面内容，考虑 python-docx-template，而不是只用 Pandoc reference-doc。

