---
task: TASK11-GRE-Kali雕塑
stage: reference-comparison
status: complete
---

# TASK11 参考对照

## 命中情况

| 官方 reference 要点 | assisted-run 是否覆盖 | 说明 |
|---|---|---|
| 头部和手部模具是否足以推出整体由模具制成 | 覆盖 | `A1-B1` 标为范围外推。 |
| 模具可能只是练习、研究或辅助工具 | 覆盖 | `A1-B1/B2` 标为主因机制未证。 |
| 真人大小与微型雕塑是否同源、同时期、同材料、同市场 | 覆盖 | `B1-B3` 标为可比对象审查。 |
| 微型雕塑抽象风格是否只能由不能用模具解释 | 覆盖 | 加入时代、用途、材料、传统等替代解释。 |
| 工具少不等于没有使用工具 | 覆盖 | `B2-B4` 标为观测/保存偏差。 |
| 收藏价值是否主要由制作方式决定 | 覆盖 | `B1-C1-D` 与 `B3-C2-E` 标为价值预测机制不足。 |
| 高分答案强调问题答案如何影响预测 | 覆盖 | `arrow-audit.md` 单独列 yes/no impact。 |

## 与 TASK10 的关系

TASK10 验证了 assumption 型 GRE 输出：

```text
assumption -> arrow -> impact if false
```

TASK11 验证了 question 型 GRE 输出：

```text
question -> target arrow -> if yes / if no impact
```

这说明 GRE 分支不只是单一模板，而是要先识别题目指令，再选择 assumption-impact 或 question-impact 的输出形态。

## 反哺判断

建议反哺两个上位规则：

1. **问题影响链**：当题目要求提出 questions 时，每个问题必须绑定 target arrow，并说明 yes/no 两种答案如何改变结论可信度。
2. **预测类结论机制审查**：从事实发现推出价格、价值、市场反应、政策效果等预测时，必须补上行为主体、评价标准和传导机制。

其中第 1 条已由 TASK10 的 GRE 分支支持，应明确写入 GRE 分支；第 2 条可进入父层断点 taxonomy，作为 `overclaim / hidden premise missing` 的子提示。
