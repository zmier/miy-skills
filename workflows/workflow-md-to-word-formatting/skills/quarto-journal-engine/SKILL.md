---
name: quarto-journal-engine
description: 使用 Quarto journal template 将 qmd/rmd/md 转为外刊 manuscript docx 的引擎 Skill。适用于外刊投稿、PLOS/Frontiers/特定 journal template、引用和图表较复杂的 manuscript；优先复用 quarto-journals 生态。
---

# Quarto Journal Engine

## 适用

- 外刊 manuscript；
- 用户已有 `.qmd` / `.rmd`；
- 目标 journal 有 Quarto template；
- 需要 citations、crossrefs、figures、tables、supplement 组织。

## 常用路线

```bash
quarto use template quarto-journals/<template-name>
quarto render manuscript.qmd --to docx
```

如果 profile 只要求通用外刊 Word，可使用 Quarto built-in docx 或 Pandoc reference-doc。

## Green

- 记录 Quarto 版本；
- 记录 journal template 来源；
- 输出 docx 可打开；
- QC report 说明哪些是 journal template 控制，哪些仍需人工检查。

## 注意

Quarto journal templates 的 docx 支持因模板而异。若模板主要面向 PDF/LaTeX，需回退到 Pandoc reference-doc 或 custom docx profile。

