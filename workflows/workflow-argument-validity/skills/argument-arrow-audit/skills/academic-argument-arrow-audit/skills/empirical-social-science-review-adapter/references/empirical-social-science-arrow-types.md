---
date: 2026-06-21
type: reference
status: structural-green / forward-test-pending
scope:
  - empirical-social-science-review-adapter
---

# Empirical Social Science Arrow Types

## 原则

这些类型是经管 / 社科实证论文中的高频审稿敏感箭头。它们不是审查顺序，也不是 checklist。使用时必须绑定具体：

```text
target_arrow_id
from_node
to_node
evidence_ids
parent_claim
impact_on_X1_X2_Y
```

## 类型

### construct-proxy fit

作者用某个可观测指标、文本指标、问卷题项、数据库变量或算法构造值来代表理论构念。

审查问题：

```text
这个 proxy 是否真的能承接 construct？
是否只覆盖 construct 的一部分？
是否方向、量纲、边界、来源或噪声不清？
```

### sample-scope fit

作者用某个样本支持总体、机制或外推声称。

审查问题：

```text
样本是否覆盖目标总体？
筛选规则是否剔除了最能检验机制的对象？
样本结构是否支持作者的机制解释和政策/管理外推？
```

### model-identification fit

作者用模型、识别设计或估计策略支撑因果、机制或政策解释。

审查问题：

```text
模型结果是否只是相关，还是足以支撑因果语言？
关键识别假设是否被说明、检验或至少讨论？
是否存在反向因果、遗漏变量、选择偏误或同时性？
```

### control-variable role

作者加入控制变量来“净化”关系，但控制变量可能改变 estimand。

审查问题：

```text
控制变量是前置混杂因素，还是处理之后的机制变量 / bad control？
控制变量是否吸收了作者想解释的效应？
控制变量是否与核心机制高度重合？
```

### inference-clustering fit

作者用显著性、标准误、聚类或检验统计支撑结果成立。

审查问题：

```text
聚类层级是否与处理/冲击/样本相关结构匹配？
显著性是否可能被错误标准误放大？
F 值、弱工具、平行趋势、动态效应等是否达到相应方法要求？
```

### mechanism-evidence strength

作者用机制检验、渠道变量、中介模型、异质性或附加结果支撑机制声称。

审查问题：

```text
这些证据是机制的直接证据、间接一致证据，还是只是相关现象？
机制变量是否和核心解释变量或结果变量过近？
是否存在同样能解释结果的替代机制？
```

### robustness-threat fit

作者用稳健性检验回应威胁。

审查问题：

```text
稳健性是否对应核心威胁？
是否只是换口径、换窗口、换样本，但没有回应真正断点？
是否存在没有被处理的更强替代解释？
```

### descriptive-validity of constructed variables

作者构造变量或指数，但描述统计、分布、方向、异常值或可解释性不足。

审查问题：

```text
变量越大代表什么？
均值、最大值、最小值是否与作者定义一致？
是否存在比例变量超过合理范围、dummy 却不止 0/1、指数方向不明等问题？
```

### result-contribution fit

作者从结果上升到理论贡献、政策启示或管理启示。

审查问题：

```text
实际发现是否支持上升后的贡献？
是否从短期/局部/特定样本结果跳到长期/总体/政策结论？
是否把“有相关结果”写成“解释了理论机制”？
```

