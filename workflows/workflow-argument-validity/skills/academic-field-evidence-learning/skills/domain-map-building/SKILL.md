---
name: domain-map-building
description: 学术领域地图构建子 Skill。用于 academic-field-evidence-learning 第四步，根据检索结果、摘要、作者参考文献和高质量来源建立 domain-map、field-topic-ledger、key-journal-map、method-and-metric-map、sota-benchmark-map 和 review-risk-radar。
---

# Domain Map Building

## 定位

本 Skill 把检索和阅读结果转成“足够审稿的领域地图”。它不写正式文献综述，也不替代箭头审计。

## 输入

- `field-search-strategy.md`；
- `seed-literature-ledger.md` 或检索结果摘要；
- 作者参考文献、关键词、引言、核心图表；
- 期刊质量证据和来源约束。

## 输出

```text
domain-map.md
field-topic-ledger.md
key-journal-map.md
method-and-metric-map.md
sota-benchmark-map.md
evidence-standard-map.md
review-risk-radar.md
```

## 地图内容

- 领域核心话题和问题意识；
- 常见材料、对象、构念、方法、实验或识别策略；
- 常用指标、benchmark、baseline 和 SOTA 比较；
- 领域顶刊、综合顶刊子刊和权威综述来源；
- 常见夸大点、机制断点、指标错配、demo 到 application 的跃迁；
- 后续验箭头时应重点盯的风险。

## Source Selector

如果输入是 OpenAlex / WoS / CNKI / BibTeX 检索结果，先生成或读取 `seed-literature-ledger.md`。每条来源必须有：

```text
include_or_exclude
include_reason
journal_quality_evidence
verification_level
needs_fulltext
```

只有 `include` 的来源能进入领域地图和风险雷达。摘要或 metadata 只能形成领域地图和候选风险，不能伪装成 fulltext-derived evidence standard。

## 完成标准

- 每个主题簇有代表来源和质量证据；
- 不把普通相关文献当成领域标准；
- 明确哪些判断来自摘要，哪些来自全文或图表；
- 每条核心判断标明 `verification_level`；
- `review-risk-radar.md` 可直接提示第 3 步回填和第 5 步修箭头。
