---
date: 2026-06-21
type: reference
status: structural-green / forward-test-pending
scope:
  - chinese-management-econ-review-adapter
---

# Chinese Management / Econ Reviewer Sensitive Points

## 原则

这些敏感点只在中文经管 / 中文社科审稿语境中作为显影规则使用。它们不是固定 checklist，更不是具体题材清单。

使用时必须绑定：

```text
target_arrow_id
evidence_ids
parent_claim
bottleneck_status_candidate
```

## 敏感类型

### signed / directional index interpretation

指标方向、正负含义或变量越大代表什么不清楚。

典型问题：

```text
变量越大是更强、更差、更多披露、更负面，还是更正面？
作者在变量定义、描述统计、回归解释和结论中的方向是否一致？
```

### text-based proxy distinction

文本类指标的数量、语气、情感、来源、人工/机器识别口径混在一起。

典型问题：

```text
文本量增加是否等于行为增加？
正向、负向、中性文本是否被区分？
不同来源文本是否代表同一构念？
```

### institutional-context sample-scope fit

中文制度背景、市场结构、监管语境或组织行为逻辑影响样本外推和机制解释。

典型问题：

```text
样本是否能代表作者声称的制度场景？
制度背景是否支持作者的机制和政策启示？
是否需要分制度环境、行业环境或监管环境讨论边界？
```

### Chinese literature genealogy

中文高质量研究中已有相邻概念、成熟指标、反向结论或本土理论，但作者没有对话。

典型问题：

```text
中文文献中是否已有相近构念或测量？
作者的 gap 是否忽略了本土文献谱系？
中文文献能否改变 contribution 的新颖性判断？
```

### policy-language / rhetorical-expression control

中文论文容易把经验结果上升为政策口号、宏大叙事或价值判断。

典型问题：

```text
政策启示是否由结果直接推出？
表述是否把局部经验发现写成宏观治理结论？
是否需要降调为更具体、更有边界的启示？
```

### local reporting convention

变量定义、描述统计、表格、稳健性、附录、样本说明没有达到中文期刊可复核标准。

典型问题：

```text
变量构造是否能让审稿人复算或理解方向？
表格是否说明固定效应、聚类、样本量、控制变量和显著性？
描述统计是否暴露异常值、量纲或指标方向问题？
```

### local reviewer-sensitive clarification

有些低层澄清不是 major，但在中文审稿中高频触发修改要求。

判断方式：

```text
如果不澄清，核心变量 / 样本 / 方法 / 结果是否无法判断？
如果只是让文章更顺滑，放 minor 或 revision action；
如果卡住 parent claim，交给 issue selection 判断是否升级。
```

