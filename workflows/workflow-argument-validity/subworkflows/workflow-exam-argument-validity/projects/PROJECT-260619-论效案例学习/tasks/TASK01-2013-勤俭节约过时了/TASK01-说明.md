# TASK01 2013 勤俭节约过时了

## 定位

- 来源文件：`../CASE-UAT-260619-论效新题/inputs/final/2013-10-MBA-勤俭节约过时了.final.md`
- 质量：`final-complete`
- 模式：`completed-uath`
- 当前状态：`done / forward-test-pass`

## 目标

围绕本题完成一次论效 workflow 学习循环：

```text
拆 prompt/reference -> blind-run -> reference comparison -> skill feedback decision
```

## 冻结边界

- blind 阶段可读：`inputs/prompt.md`、通用 workflow 规则。
- blind 阶段冻结：`inputs/reference.md`、范文、点评、佳句。
- 若模式为 `prior-exposed` 或 `assisted`，不得声称 strict blind。

## 预期产物

| 文件 | 内容 | 状态 |
|---|---|---|
| `inputs/prompt.md` | 题干 | done |
| `inputs/reference.md` | 解析/范文/点评 | done |
| `outputs/argument-tree.md` | 审题记录与 Mermaid 论证树 | done |
| `outputs/arrow-audit.md` | 箭头断点表 | done |
| `outputs/essay-draft.md` | 作文草稿 | done |
| `outputs/reference-comparison.md` | 对照答案 | done |
| `outputs/skill-feedback.md` | 反哺判断 | done |
| `logs/log.md` | ReAct 日志 | done |

## Done 标准

- 完成 blind-run 或按暴露等级完成 assisted-run；
- 完成 reference comparison；
- 明确是否反哺、反哺到哪里、是否只留在 TASK；
- 更新项目总览。
