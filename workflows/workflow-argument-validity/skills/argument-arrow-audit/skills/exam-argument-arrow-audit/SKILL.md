---
name: exam-argument-arrow-audit
description: 论效题/GRE 专用验箭头 Skill。用于在论效题、管理类/经济类联考论证有效性分析、GRE Analyze an Argument 中，从已抽取的论证树或题干材料中全量检查 A 到 B 是否成立，标注 strong、weak、broken、unclear 和 break_type；不负责选择 3 到 4 个可写问题。
---

# Exam Argument Arrow Audit

## 定位

这是 `argument-arrow-audit` 的考试型子 Skill。它继承通用验箭头原则，但服务目标不同：

```text
先穷尽关键论证链上的箭头强弱，
再把审计表交给 exam-argument-issue-selection 选 3-4 个可写问题。
```

## 输入

- 论效题/GRE 题干；
- 已抽取的小型论证树；
- 总论点、分论点、论据、结构关键词；
- GRE prompt instruction。

## 路由

| 场景 | 输出 |
|---|---|
| 中文论效题 | 全量检查题干论证树中的主要箭头 |
| GRE assumptions | 标注哪些箭头依赖 hidden premise |
| GRE questions | 标注哪些箭头需要 question 检验 |
| GRE evidence needed | 标注哪些箭头需要 evidence strengthen/weaken |
| GRE alternatives | 标注 observed fact 是否存在 rival explanation |

## 审计规则

断点分类与逻辑谬误标签使用父 Skill 的 `../../references/arrow-audit-core.md`，不要另起一套孤立谬误表。若后续需要选点，交给 `../../../argument-issue-selection/skills/exam-argument-issue-selection/SKILL.md`。

优先：

- 直接影响总论点；
- 影响上层结论或关键分论点，而不是只挑局部措辞；
- 能说清隐含前提或替代解释。

不要为了贴标签堆术语；每条 weak/broken 箭头都必须能回答：

```text
作者用什么 A 推出什么 B？
A 为什么不足以推出 B？
这如何削弱分论点、总结论或题目要求审查的 claim？
```

逻辑谬误标签只在解释清楚之后作为辅助标注：

```text
先写：作者用 A 推 B，但 A 只能说明 X，不能排除 Y，因此 B 不稳。
再标：这可概括为 concept-mismatch / alternative-explanation / causal-leap 等。
```

若是 GRE 题，必须先识别 prompt instruction：assumptions、questions、evidence needed 或 alternatives。不同指令对应不同输出，不得都写成中文论效式“存在某谬误”。

## 输出

1. `exam-arrow-audit-table.md`
2. `exam-arrow-break-summary.md`
3. 交给 issue selection 的候选箭头清单

模板见 `assets/exam-arrow-audit-template.md`。

## 完成标准

- 每个断点绑定 target arrow；
- 每个断点说明“作者用 A 推出 B，为什么推不出”；
- 每个 `break_type` 优先来自 `../../references/arrow-audit-core.md`，并可附中文谬误标签；
- GRE 审计必须记录 assumption/question/evidence/alternative 如何影响原论证；
- 不在本 Skill 中决定最终写哪 3-4 个问题。
