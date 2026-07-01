---
type: reference
scope:
  - workflow-md-to-word-formatting
---

# Style Profile Contract

每个 profile 用 YAML 表示，最少包含：

```yaml
name:
locale:
target:
engine_preference:
page:
  size:
  margins:
fonts:
  east_asia:
  latin:
  other:
paragraphs:
  body:
    font_size_pt:
    line_spacing:
    first_line_indent_chars:
    alignment:
headings:
  h1:
    numbering:
    font:
    font_size_pt:
    font_color:
    alignment:
    outline_level:
tables:
  caption_position:
  note_style:
figures:
  caption_position:
notes:
  type:
references:
  style:
qc:
  required_checks:
```

## 重要字段

- `fonts.other` 必须显式设置，避免希腊字母和符号落到中文字体。
- `outline_level` 必须显式设置，避免正文误入目录。
- `headings.*.font_color` 必须显式设置。默认 `000000`；否则 Word 内置 Heading 样式可能继承主题蓝色。
- 四级标题若要求连排，不应单独建段落样式；用正文样式 + 局部加粗。
