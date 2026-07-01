# Abstract Scan vs Fulltext Pattern

## 分工

摘要扫描回答：

```text
这个领域是否有人做；
别人声称什么；
常用哪些关键词、指标、材料、方法；
哪些文献可能是 comparator；
哪些文献值得深读。
```

原文 / 图表 / 补充材料深读回答：

```text
别人到底用哪些证据证明这根箭头；
证据包包括哪些实验、表格、图、稳健性、控制组；
最小可接受证据是什么；
强证据包是什么；
不能补证据时如何降调。
```

## 摘要可产出的内容

| 内容 | 可用程度 |
|---|---|
| 同类论文存在 | 可用 |
| 常见 claim / metric / method 名称 | 可用 |
| 候选 comparator | 可用 |
| repair route 初步猜测 | 只能标 candidate |
| 证据标准 | 不够 |

## 通常需要原文的位置

| 位置 | 可能抽取的 repair pattern |
|---|---|
| Methods | 实验条件、样本规则、识别设定、模型细节 |
| Results and Discussion | 作者如何把结果解释为机制或贡献 |
| Figure captions | 图表到底测了什么、条件是什么 |
| Supplementary Information | 控制实验、补充表征、稳健性、参数表 |
| Appendix | 证明、模型推导、稳健性、额外样本 |
| Benchmark tables | SOTA 对比字段和口径 |
| Reviewer response / rebuttal | 真实审稿人要求的修复动作 |

## 禁止事项

- 不把摘要里出现的关键词直接写成领域标准；
- 不用单篇文献的特殊做法硬编码成稳定 menu；
- 不用普通 web 解读替代方法原文、顶刊应用或官方文档；
- 不把没有读过的补充材料当成已验证。

