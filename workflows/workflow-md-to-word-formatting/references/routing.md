---
type: reference
scope:
  - workflow-md-to-word-formatting
---

# Routing

## 场景识别

| trigger | profile | engine | note |
|---|---|---|---|
| 审稿意见、review comments、给编辑说明、response letter | review-comment | pandoc | 轻量 Word，可编辑、清楚、稳 |
| 管理世界 | management-world | pandoc + postprocessor | 使用本地龙章规范 |
| 金融研究 | financial-research | pandoc + postprocessor | 注意匿名和固定 20 磅行距 |
| 川大学位论文、四川大学、学位论文样式 | scu-thesis | pandoc + postprocessor | 标题字号层级明确；短文档可关闭一级标题分页 |
| 外刊、journal manuscript、submission docx | foreign-generic-manuscript | quarto / pandoc | 若有 journal template，优先 Quarto |
| PLOS、Frontiers、Quarto journal template | quarto-journal | quarto | 使用 quarto-journals 生态 |
| 复杂封面、固定页眉页脚、表单 | custom-template | python-docx-template | Pandoc reference-doc 不足 |

## 引擎优先级

```text
有 Quarto journal template -> Quarto
普通 Markdown + reference-doc -> Pandoc
Pandoc 样式不足 -> python-docx 后处理
固定 Word 模板内容必须保留 -> python-docx-template
需要完全自定义渲染 -> markdown2docx / JS docx
```
