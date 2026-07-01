---
name: docx-style-postprocessor
description: 用 python-docx 或直接修改 docx XML 对已生成 Word 文件做样式后处理的 Skill。用于修正中文字体、英文字体、NameOther、段落缩进、行距、标题大纲级别、列表、表格样式、页眉页脚和 profile 特定要求。
---

# DOCX Style Postprocessor

## 输入

```text
input.docx
profile.yaml
output.docx
```

## 处理项

- 设置 Normal / Body Text / Heading 1-3；
- 设置中文字体 `eastAsia`、英文字体 `ascii/hAnsi`、符号字体 `cs/other`；
- 设置段落对齐、首行缩进、行距、段前段后；
- 强制正文、图表名、注释等为 BodyText outline level；
- 按 profile 修正标题样式；
- 标题颜色必须按 profile 显式写入，默认黑色 `000000`，不得继承 Word 内置 Heading 的主题蓝色；
- 写标题颜色时必须同时处理 style font color 和 paragraph run color；若底层 XML 存在 `w:themeColor`，必须清除并写入 `w:val="000000"` 或 profile 指定颜色；
- 表格基础样式；
- 可选：隐藏拼写/语法检查标记、清理修订痕迹提示。

## Green

- 后处理脚本可重复运行；
- 不破坏 docx 可打开性；
- 标题颜色不再继承主题色；
- 修改记录写入 conversion-log。

## 标题颜色处理示例

后处理脚本应包含等价逻辑：

```python
from docx.shared import RGBColor
from docx.oxml.ns import qn

style.font.color.rgb = RGBColor(0, 0, 0)
color = style._element.rPr.find(qn("w:color"))
if color is not None:
    color.attrib.pop(qn("w:themeColor"), None)
    color.set(qn("w:val"), "000000")

for run in heading_paragraph.runs:
    run.font.color.rgb = RGBColor(0, 0, 0)
```
