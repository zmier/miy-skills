---
date: 2026-06-20
type: reference
status: seed
scope:
  - scholar-docx-markdown-restoration
---

# External DOCX To Markdown Skills And Tools

## 结论

外部项目可以借鉴转换器和 fallback 设计，但不直接替代本 workflow 的审稿底稿还原 Skill。

原因：

- 外部工具多解决“docx 转 md”，不保证审稿所需 `[para N]` 定位层；
- 不一定区分正文、脚注、尾注、figure evidence、back matter；
- 不一定生成 restoration / segmentation / figure QC；
- 不一定服务后续 `academic-paper-argument-tree-extraction` 的 claim/evidence ledger。

## 候选

| 项目 | 用法 | 可借鉴点 | 限制 |
|---|---|---|---|
| `sheepmao/doc-to-markdown-skill` | Claude Code Skill / doc to markdown | Word 转 Markdown、图片提取、清理 Word 噪音、fallback | 不直接满足学术审稿段落定位和 evidence QC |
| `neoncapy/doc2md` | 多格式 document to markdown pipeline | provider registry、conversion + QC loop、图片分析 prompt | 更偏通用 pipeline，需要裁剪成 workflow 子 Skill |
| `wangminle/skills-doc-to-md` | Codex Skill / docx-to-markdown | `pandoc --extract-media`、脚注/尾注、文本框、公式和嵌入对象处理 | 仍需加学术审稿底稿规则和 `[para N]` |
| `anthropics/skills docx` | 通用 DOCX 读写 Skill | OOXML、track changes、pandoc track-changes 思路 | 不是 Markdown restored manuscript Skill |
| markitdown / mammoth | 底层抽取器 | 快速粗抽取、可作为对照 | 不保证图表、公式、段落和审稿 QC |

## 使用原则

```text
外部 Skill / CLI = 转换器或参考实现
本 Skill = 审稿可定位底稿还原器
```

默认优先 Pandoc：

```bash
pandoc --from=docx --to=gfm --wrap=none --extract-media=outputs/media input.docx -o outputs/manuscript_raw.md
```

若遇到复杂 OOXML 对象，再引入 fallback。

