# TASK11 GRE Kali 雕塑

## 定位

- 来源文件：`../../../../docs/GRE-Argument-original-chapters.extract.md`
- 原 PDF 页码：Task prompt 位于 PDF page 221；scored responses/commentary 位于 PDF page 248-254。
- 质量：`official-gre-argument / scored-responses`
- 模式：`prior-exposed / assisted`
- 当前状态：`done / assisted-uat-pass / feedback-applied`

## 目标

把 GRE Analyze an Argument 的官方练习题 2 纳入论效案例学习工程，用作英文官方校准样本：

```text
题干摘要 -> 官方答案结构摘要 -> reader commentary 摘要 -> 反哺候选判断
```

## 冻结边界

- 本题答案和 reader commentary 已被读取，因此不得标为 strict blind。
- 后续若运行本 TASK，只能作为 `assisted-run` 或 `calibration-run`。
- 原文长材料保留在 `docs/GRE-Argument-original-chapters.extract.md`，本 TASK 只保存摘要、页码和可迁移结构。

## 预期产物

| 文件 | 内容 | 状态 |
|---|---|---|
| `inputs/prompt.md` | 题干摘要与原文位置 | done |
| `inputs/reference.md` | 官方多档答案与 reader commentary 摘要 | done |
| `outputs/case-summary.md` | 本题对 workflow 的校准价值 | done |
| `outputs/argument-tree.md` | GRE 题干论证树与 Mermaid | done |
| `outputs/arrow-audit.md` | question -> target arrow -> yes/no impact 审查表 | done |
| `outputs/gre-response-draft.md` | GRE 问题型 response 草稿 | done |
| `outputs/reference-comparison.md` | 与官方 reader commentary 的对照 | done |
| `outputs/skill-feedback.md` | 反哺候选与已应用规则 | done |
| `outputs/UAT.md` | assisted UAT 判断 | done |
| `logs/log.md` | 纳入项目的处理记录 | done |

## Done 标准

- 真题和答案摘要已进入 TASK；
- 已声明 prior-exposed / assisted；
- 已链接原文章节；
- 已完成 assisted-run、官方答案对照和 UAT；
- 已把 question-impact chain、prediction mechanism audit、tool-existence vs mechanism 回收到 workflow；
- 已更新项目总览和反哺候选池。
