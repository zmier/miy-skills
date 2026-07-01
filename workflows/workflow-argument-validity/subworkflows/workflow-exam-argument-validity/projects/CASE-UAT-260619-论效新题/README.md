---
date: 2026-06-19
type: uat-case
status: forward-test-pass
workflow: workflow-exam-argument-validity
---

# CASE-UAT-260619 论效新题

## 目的

使用一篇未参与 workflow 提炼的新论效题，测试 `workflow-exam-argument-validity` 是否具备迁移能力。

本 case 用于总体 UAT / forward-test，不用于课程单元回归。

## 输入

| 文件 | 内容 | 状态 |
|---|---|---|
| `inputs/prompt.md` | 完整题干材料：2013 年 10 月 MBA 联考真题“勤俭节约”过时了 | final-complete |
| `inputs/reference.md` | 论证结构、题目解析、范文参考 | final-complete |
| `inputs/student-draft.md` | 学生初稿或待修改稿 | partial / OCR-mixed |
| `inputs/cleaned/README.md` | OCR 文件概览、全量清洗索引与状态边界 | done |
| `inputs/cleaned/*.md` | 2003-2013 年早年 MBA 联考真题清洗稿 | cleaned / first-pass；2012、2011 为 partial |
| `inputs/final/README.md` | 最终精校语料索引、质量等级和使用边界 | done |
| `inputs/final/*.md` | 2003-2013 年早年 MBA 联考真题最终版 | final-complete / final-with-ocr-caveats / incomplete-source |
| `inputs/final/FULL-CORPUS.final.md` | 全量最终版合并入口 | done |

## 输出

| 文件 | 内容 | 状态 |
|---|---|---|
| `outputs/argument-tree.md` | 审题记录与 Mermaid 论证树 | blind-run complete |
| `outputs/arrow-audit.md` | 箭头断点表与选点说明 | blind-run complete |
| `outputs/essay-draft.md` | 论效题作文草稿 | blind-run complete |
| `outputs/revision-notes.md` | 修改清单、二稿建议和 workflow 回填点 | blind-run complete |
| `outputs/reference-comparison.md` | 解冻参考解析后的对照评测 | pass |
| `outputs/skill-change-proposal-concept-relation.md` | 概念关系审查反哺提案 | partial / source-case-green |
| `outputs/course-skill-evaluation.md` | 课程驱动 Skill 工程评测 | forward-test-pass |
| `outputs/UAT.md` | UAT 状态、通过项、未完成项和下一步 | forward-test-pass |

## 验收标准

通过本 case 至少需要产出：

```text
审题记录 -> Mermaid 论证树 -> 箭头断点表 -> 行文规划 -> 文章草稿 -> 修改清单
```

本 case 已通过 reference comparison，可将 `workflow-exam-argument-validity` 状态从 `structural-green / forward-test-pending` 推进为 `forward-test-green`。
