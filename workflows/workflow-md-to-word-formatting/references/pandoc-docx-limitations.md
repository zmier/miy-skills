---
type: reference
scope:
  - workflow-md-to-word-formatting
---

# Pandoc DOCX Limitations

Pandoc 很适合把 Markdown 转成 docx，但以下情况不能只靠 `--reference-doc`：

- 需要完整保留模板正文、封面、固定页面；
- 需要复杂页眉页脚、分节、表单字段；
- 需要特定 Word 宏或 VBA；
- 需要四级标题连排和局部样式强控制；
- 需要精确控制中文字体、Other 字符字体和大纲级别；
- 需要对表格三线表做复杂修正。

策略：

```text
Pandoc 负责结构转换；
reference-doc 负责基础 Word styles；
python-docx 后处理负责精修；
QC report 负责发现人工视觉复核点。
```

