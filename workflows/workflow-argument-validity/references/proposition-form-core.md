---
date: 2026-07-06
type: reference
status: draft-rule
scope:
  - workflow-argument-validity
source:
  - workflow-research collaborative-reading proposition insight
---

# Proposition Form Core

## 一句话

论证树中的关键 claim 节点，尤其是学术论文的“一句话核心发现”、`X2`、根结论和主要分论点，必须能表述为形式逻辑视角下的简单命题或复合命题。

形式逻辑是核心骨架；论文写作、研究设计或审稿术语只是辅助标签。

## 为什么需要命题化

验箭头不是判断一句话“听起来像不像观点”，而是判断：

```text
A 是否足以推出 B？
```

如果 B 还不是可判真假的命题，后续就无法判断 A 支撑了什么、反例应该长什么样、断点削弱哪个上层节点。

因此，抽树阶段必须先把关键 claim 写成命题，再进入箭头审计和问题选择。

## 命题形态

常见形态包括：

| 形态 | 模板 | 说明 |
|---|---|---|
| 直言命题 | S 是 / 不是 P | 断言某对象、关系、属性或现象成立 |
| 假言命题 | 如果 A，那么 B | 断言 A 是 B 的充分条件或在给定条件下推出 B |
| 联言命题 | A 且 B | 同时断言多个子命题成立 |
| 选言命题 | A 或 B | 断言至少一个选项成立；需区分相容、排斥和穷尽 |

学术论文的一句话发现常常不是单一命题，而是复合命题。例如：

```text
基金经理受有限注意力影响，并且受有限注意力影响越大，表现越差。
```

形式上可还原为：

```text
A：基金经理受有限注意力影响。
B：基金经理受有限注意力影响越大，基金表现越差。
A 且 B
```

其中 B 也可进一步写成假言或比较关系：

```text
如果基金经理受有限注意力影响更大，那么其基金表现更差。
```

## 双版本输出

关键 claim 建议保留两个版本：

```text
full_logical_restoration:
  形式逻辑完整还原版，允许较长，必须说清简单/复合命题结构。

readable_compressed_version:
  给读者带走的锋利版本，简短有力，但不得丢失核心命题。
```

`readable_compressed_version` 可以更像“一颗钉子”，但 `full_logical_restoration` 必须能解释这颗钉子的逻辑结构。

## 学术论文的一句话发现

学术论文的一句话核心发现原则：

1. 先从摘要提炼，因为摘要通常已经压缩了论文最希望读者带走的发现；
2. 再用 introduction、theory / hypotheses、results 和 conclusion 校准；
3. 优先还原为命题，而不是先套 `X/M/Y/Y2`；
4. `X/M/Y/Y2` 是研究设计和论文写作标签，用来帮助定位命题成分，不能替代命题本身。

辅助标签可以包括：

```text
existence / descriptive
causal / effect / consequence
mechanism
heterogeneity / boundary
contribution / gap
```

这些标签来自论文写作和研究设计语境，不是统一稳定的逻辑术语。使用时必须标为 `research_function_label`，不得替代 `logical_form`。

## 反驳形态

命题形态决定有效反驳应长什么样。

| 目标命题 | 有效反驳形态 | 常见误判 |
|---|---|---|
| 直言命题：S 是 P | S 存在但不是 P；或 S/P 概念本身不成立 | 只质疑无关对象 |
| 假言命题：A -> B | A 且 非B | 只指出非A，误以为反驳了 A -> B |
| 联言命题：A 且 B | 反驳任一联言支即可削弱整体 | 只反驳弱支却忽略主支仍可独立成立 |
| 选言命题：A 或 B | 需看相容/排斥/穷尽；通常要排除所有可用选项 | 只反驳一个选项就以为整体不成立 |

特别注意：

```text
要反驳 A -> B，必须构造或寻找 A 且 非B。
单纯 非A 不能反驳 A -> B。
```

`非A` 可能说明作者没有证明前件存在，或样本不覆盖前件场景，但它不是对假言命题本身的反例。

## 推荐字段

在节点台账、主干抽取、箭头审计或问题选择中，关键 claim 可记录：

```text
logical_form
full_logical_restoration
readable_compressed_version
component_propositions
research_function_label
abstract_anchor
calibration_sources
valid_counterexample_shape
qc_flags
```

常见 QC flags：

```text
not-a-proposition-node
needs-claim-rewrite
compound-proposition-unparsed
counterexample-shape-unclear
research-label-used-as-claim
```
