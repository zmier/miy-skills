# Theory Paper Adapter

用于理论、模型、数学证明、形式化机制或概念模型为核心的论文。

## 节点命名

建议使用：

```text
G* = X1 支撑节点
T* = X2 理论/模型支撑节点
E-* = 定义、假设、命题、证明步骤、反例或比较静态证据
```

## X2 最小展开

| 节点 | 问题 |
|---|---|
| T1 核心对象和边界定义清楚 | 模型研究谁、什么环境、什么限制 |
| T2 假设 / 公理合理 | 关键假设是否明确，是否过强 |
| T3 机制链可推出命题 | 从假设到命题的推理是否连续 |
| T4 命题 / 定理证明完整 | 证明步骤是否支撑结论 |
| T5 比较静态 / 推论支撑解释 | 参数变化是否支撑作者解释 |
| T6 边界条件清楚 | 结论在哪些条件下成立 |
| T7 与既有理论差异明确 | 新模型是否真的不同 |
| T8 贡献上升成立 | 模型结论是否支撑理论贡献或实践启示 |

## Evidence Ledger 要求

底层证据可包括：

```text
definition
assumption
lemma
proposition
theorem
proof step
corollary
comparative statics
counterexample
boundary condition
```

每条 evidence 记录：

```text
所在章节 / 公式 / 命题编号
原文或公式摘要
支撑哪个 T 节点
是否需要 proof-qc
```

## QC 标记

- `needs-proof-qc`：证明步骤没有完整核验；
- `needs-formula-qc`：公式转写或符号不确定；
- `assumption-too-strong`：假设可能直接内含结论；
- `boundary-unclear`：作者没有说明适用边界。
