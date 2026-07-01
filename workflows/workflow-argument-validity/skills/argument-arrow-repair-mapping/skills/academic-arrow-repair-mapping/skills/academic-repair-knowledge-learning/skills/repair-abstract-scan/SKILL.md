---
name: repair-abstract-scan
description: 修箭头摘要扫描子 Skill。用于按 repair-search-strategy.md 执行摘要层筛选，识别同领域同类论文、常见 claim、metric、method、comparator 和候选 repair route；输出 abstract-scan-ledger 和 deep-read shortlist，但不得把摘要中出现的方法词直接当作强 repair 标准。
---

# Repair Abstract Scan

## 定位

本 Skill 用摘要快速判断哪些资料可能教会我们“这类断箭头通常怎么补”。摘要扫描是筛选和定位，不是最终证据标准。

## 输入

- `repair-search-strategy.md`；
- 检索结果的题名、摘要、关键词、来源、年份；
- 可选：引用量、期刊层级、领域标签。

## 输出

```text
abstract-scan-ledger.md
deep-read-shortlist.md
```

`abstract-scan-ledger.md` 字段：

```text
source_id
citation_or_url
source_type
abstract_claim
relevant_metric_or_method
candidate_repair_route
needs_fulltext
why_selected_or_excluded
notes
```

## 扫描原则

- 记录同类 claim：别人声称解决的是哪类箭头。
- 记录常用 metric：别人用什么指标承接 claim。
- 记录常用 method：别人用什么方法或实验支持 claim。
- 记录 comparator：别人和什么基准、对照组、benchmark 比。
- 标出 `needs_fulltext=yes` 的来源。

## 禁止

- 不把摘要里出现的方法名直接写成强证据标准。
- 不把单篇摘要当作稳定 menu。
- 不新增未经 `academic-arrow-audit` 审计的新断点。

## 完成标准

- 有明确的筛选理由；
- 有深读候选清单；
- 每个候选 repair route 都能追溯到来源摘要；
- 输出可直接交给 `repair-fulltext-pattern-extraction`。

