---
name: pandoc-docx-engine
description: 使用 Pandoc 将 Markdown 转为 docx 的引擎 Skill。用于 reference-doc 样式转换、citation/csl 支持、普通审稿意见 Word、中文期刊 profile 的初步 docx 生成；必须说明 Pandoc docx template 的限制，并把后处理交给 docx-style-postprocessor。
---

# Pandoc DOCX Engine

## 适用

- `.md` 到 `.docx`；
- 已有 `reference-docx`；
- 需要 citation / csl / bibliography；
- 输出后可用 python-docx 进一步修样式。

## 命令模板

```bash
pandoc input.md \
  --from markdown+pipe_tables+footnotes+smart \
  --to docx \
  --reference-doc reference.docx \
  --output output.docx
```

按需增加：

```bash
--citeproc
--bibliography refs.bib
--csl journal.csl
--metadata-file metadata.yaml
```

## 限制

Pandoc 的 `--reference-doc` 主要用于调整 Word styles，不是完整 Word 模板系统。复杂封面、固定页面、页眉页脚、变量插入、表单字段等，不应只依赖 reference-doc。

## Green

- 命令可复现；
- conversion-log 记录 pandoc 版本、命令、reference-doc；
- 输出 docx 可打开；
- 进入 postprocessor / QC。

