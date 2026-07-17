---
date: 2026-06-20
type: reference
status: seed
scope:
  - argument-issue-selection
---

# Issue Selection Principles

## 全量候选池与最终选点分离

选问题不是一上来就删减。必须先生成全量候选池，再生成建议选点方案：

```text
验箭头结果
-> full issue candidate pool
-> human-readable issue candidates
-> selection plan
-> final drafting
```

全量候选池负责“摊开所有可写问题”，最终选点负责“决定这次写哪些”。subAgent 可以建议优先级、合并关系和写作路线，但不应把重要候选提前删掉。否则很容易把高层断点压成低层标签，例如把“进口机器人/组件不等于企业实际采用并使用机器人”压成“Robot 变量构造不清”。

全量候选池必须同时有人类可读版本。机器字段如 `A6 / E-X1 / needs-proxy-qc` 可以保留，但必须翻译成接近审稿意见或论效作文的问题说明，让用户不用回查 ledger 也能判断是否入稿。

## 诊断层与决策层分离

验箭头和选问题必须拆开：

```text
验箭头：判断每条 A -> B 是否成立。
选问题：决定哪些 weak / broken / unclear / needs-qc / needs-external-evidence 箭头值得进入本次输出。

`needs-external-evidence` 只能选为 evidence-needed、search-before-major 或 hold-for-external-evidence；外部证据增强完成前，不得写成已确认断点。
```

拆开的理由：

1. 验箭头追求覆盖和忠实，选问题追求优先级和表达策略。
2. 验箭头的判断标准是逻辑强弱，选问题的判断标准还包括任务目标、篇幅、读者、可写性、审稿价值和重复度。
3. 如果在验箭头阶段就选问题，容易漏掉重要但暂时不写的断点，也容易把“没选中”误解为“没有问题”。
4. 如果在选问题阶段重新验箭头，容易把决策偏好倒灌进诊断结果。

## 通用优先级

优先选择：

- 直接削弱根结论、总结论或 `Y` 的断点；
- 削弱关键中层节点、`X2` 或主要分论点的断点；
- 能有效削弱目标命题形态的断点，而不是只制造相关疑问；
- 能用原文、表格、题干或 evidence ledger 清楚定位的断点；
- 能明确说明“作者用 A 推 B，但 A 不足以推出 B”的断点；
- 与当前任务指令匹配的断点。

谨慎选择：

- 只影响措辞、不影响论证链的问题；
- 需要大量外部知识才能说明的问题；
- 与已选问题高度重复的问题；
- 只有术语标签、无法说清推理断裂的问题；
- 对假言命题 `A -> B` 只指出 `非A`，却没有说明这如何构成前件未确立、范围错配或 `A 且 非B` 的问题；
- 证据缺口尚未 QC，且影响范围不明的问题。

## 输出原则

每个入选问题都必须保留：

```text
target_arrow
target_proposition_form
valid_counterexample_shape
does_issue_match_counterexample_shape
weakened_node
impact_on_root
why_selected
writing_route
```

未入选的重要断点也应进入 `discarded but noted`，说明是因为篇幅、重复、证据不足还是影响较小而暂不写。
