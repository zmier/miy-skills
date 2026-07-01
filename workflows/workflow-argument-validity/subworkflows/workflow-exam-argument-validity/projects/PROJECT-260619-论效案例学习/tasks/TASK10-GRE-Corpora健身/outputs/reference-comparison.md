---
task: TASK10-GRE-Corpora健身
stage: reference-comparison
status: complete
---

# TASK10 参考对照

## 命中情况

| 官方 reference 要点 | assisted-run 是否覆盖 | 说明 |
|---|---|---|
| 二十年前标准与当前标准未必可比 | 覆盖 | `A1+A2-B1` 标为 `standard shift / extrapolation mismatch`。 |
| 电脑拥有率不等于电脑使用时间 | 覆盖 | `A3-B2` 标为 `measurement mismatch`。 |
| 高拥有率地区可能有收入、资源等第三因素 | 覆盖 | `A3-B2` 加入 `alternative explanation`。 |
| 健身支出低不一定说明经济衰退是主因 | 覆盖 | `A4-B3` 标为支出与健康行为错配。 |
| 免费锻炼等低支出替代可能存在 | 覆盖 | GRE draft 第三段展开。 |
| 经济改善不必然推出健康改善 | 覆盖 | `B3-F` 标为 hidden premise missing / overclaim。 |
| 高分答案强调假设如何影响论证 | 覆盖 | `arrow-audit.md` 单独列 `hidden_assumption` 与影响。 |

## 和前 9 个中文论效案例的差异

GRE Argument 的核心输出不是“找 3-4 个可写问题”而是“围绕题目指令组织假设分析”。这要求每个断点必须写成：

```text
hidden assumption -> supporting arrow -> if false, impact on root claim
```

中文论效题也需要解释“为什么推不出”，但 GRE 官方评分更强调：

- 是否紧扣 prompt instruction；
- 是否具体说明 assumption 的 role；
- 是否说明 assumption failure 的 implication；
- 是否避免转向自己的立场或泛泛评论。

## 反哺判断

建议反哺父 workflow 和论效子 workflow：

1. 在父 workflow 的输出契约中加入“假设影响链”字段。
2. 在 `output-ladder.md` 的 L4/L5 增加要求：问题型输出不能只列问题，要说明答案如何影响结论。
3. 在文本类型路由中加入 GRE Analyze an Argument，暂可路由到父层通用树 + exam 子 workflow 的审题和段落输出，不必立即新建独立子 workflow。
