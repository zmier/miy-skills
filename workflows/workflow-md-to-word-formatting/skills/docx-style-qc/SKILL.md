---
name: docx-style-qc
description: 对 md-to-word 输出的 docx 做版式质检的 Skill。用于检查 docx 可打开、段落样式、字体、行距、缩进、标题大纲、列表、表格、匿名要求、脚注/尾注、人工视觉复核项，并输出 style-qc-report.md。
---

# DOCX Style QC

## 检查项

1. 文件可打开：
   - `python-docx` 能读取；
   - 段落和表格数量非零。
2. 样式抽样：
   - 标题样式；
   - 正文样式；
   - 列表；
   - 表格；
   - 图表标题和注释。
3. profile 必查项：
   - 中文/英文字体；
   - 行距；
   - 首行缩进；
   - 段前段后；
   - 大纲级别；
   - 标题字体颜色：不得继承 Word 主题蓝，除非 profile 显式要求；
   - 匿名要求；
   - 脚注/尾注；
   - reference-doc/template 来源。
4. 人工视觉检查：
   - 首页；
   - 第一页正文；
   - 一个列表；
   - 一个表格；
   - 一个英文段落；
   - 一个中文段落。

## 输出

```text
style-qc-report.md
```

状态：

```text
pass / warning / fail / human-check
```
