---
name: repair-fulltext-pattern-extraction
description: 修箭头原文证据包抽取子 Skill。用于对 repair-abstract-scan 选出的深读文献、官方资料或方法文档读取原文、方法、结果、图注、补充材料、appendix、benchmark table 或 reviewer response，抽取别人如何证明这类箭头的 evidence package；输出 fulltext-pattern-ledger，不直接写审稿意见。
---

# Repair Fulltext Pattern Extraction

## 定位

本 Skill 负责从原文、图表和补充材料里抽“别人具体怎么补这类箭头”。它产出 evidence package，不产出审稿文字。

## 输入

- `deep-read-shortlist.md`；
- 原文 PDF/HTML/Markdown、图表、补充材料、方法文档或官方文件；
- `target_arrow_id` 和断点说明；
- `repair-search-strategy.md`。

## 输出

```text
fulltext-pattern-ledger.md
```

字段：

```text
source_id
section_or_figure
target_arrow_type
claim_being_supported
evidence_package_observed
minimum_evidence
strong_evidence_package
fallback_downgrade
quote_or_anchor
confidence
```

## 抽取重点

- Methods：样本、实验、模型、识别、参数、控制条件。
- Results：核心结果、显著性、效应量、稳健性。
- Figure captions：图对应的实验或机制证据。
- Supplementary Information / Appendix：关键控制实验、额外表、算法细节。
- Benchmark tables：同类对比基准。
- Reviewer response：真实审稿人要求补什么、作者如何补。

## 完成标准

- 每个 pattern 有来源锚点；
- 区分最低证据、强证据包、降调方案；
- 标记只来自单篇个案还是多篇重复出现；
- 对未读全文、图表未核验、补充材料缺失的情况写 `needs-fulltext-pattern-check` 或 `needs-visual-qc`。

