---
name: repair-search-strategy-design
description: 修箭头检索策略设计子 Skill。用于 academic-repair-knowledge-learning 已固定目标断箭头和修复疑问后，在摘要扫描之前设计可执行检索策略，包括检索目标、资料源、关键词组合、纳入排除标准、摘要扫描目标、必须深读条件和预期抽取字段；不负责实际深读或生成 repair map。
---

# Repair Search Strategy Design

## 定位

本 Skill 只负责把“我不知道这条断箭头该怎么补”翻译成可执行检索策略。它不判断作者是否错了，也不生成最终修法。

## 输入

- `repair-knowledge-gap.md`；
- `target_arrow_id` 和断点说明；
- `academic-arrow-audit-table.md` 中相关箭头；
- 论文领域、关键词、目标期刊或方法名称；
- 可用数据库或资料源。

## 输出

```text
repair-search-strategy.md
```

必须包含字段：

```text
learning_id
target_arrow_ids
repair_question
search_goal
source_priority
journal_quality_policy
journal_quality_sources
literature_search_skill
databases_or_routes
query_blocks
inclusion_criteria
exclusion_criteria
abstract_scan_goal
fulltext_trigger
expected_pattern_fields
stop_rule
qc_risks
```

## 路由规则

- 文献检索默认写明 `literature_search_skill: scholar-kit-literature-search`；
- 除非用户明确指定数据库或已有任务已锁定子 Skill，不直接把 WoS / CNKI / OpenAlex 写成独立执行入口，而是写成 `$scholar-kit-literature-search` 的候选路由；
- 文献 gap / SOTA：优先综述、领域顶刊、综合顶刊及其子刊、同类 benchmark。
- 机制 / 实验：优先同类高质量原文、领域顶刊/综合顶刊及其子刊的 Methods、Results、Figure captions、Supplementary Information。
- 统计 / 识别 / 方法：优先方法原文、权威 handbook、顶刊应用、官方 package docs。
- 政策 / 官方数据：优先官方文件、数据说明、统计口径。
- 中文领域：优先 CNKI / 中文核心 / 川大 B 以上来源，再补英文数据库。

## 期刊质量门槛

检索策略必须写明 `journal_quality_policy`。默认策略：

```text
优先纳入领域顶刊、综合顶刊及其子刊、权威综述、方法原文、官方标准/文档；普通相关论文只能作为背景线索，不能单独生成 stable repair menu。
```

候选期刊名单不要硬编码，执行时动态获取并记录来源。可用路线：

- 从目标稿件参考文献、关键词、同类综述和高被引 benchmark 中提取 seed journals；
- 用 `$scholar-kit-literature-search` 先搜同类 claim / method / material，统计高相关结果集中反复出现的期刊；
- 需要可追溯分区或期刊层级时，通过 `$scholar-kit-literature-search` 路由 WoS，并在 `journal_quality_sources` 记录 JCR quartile、WoS category 或检索页面证据；
- 无法访问 JCR/WoS 时，可用 SJR/SCImago Q1、领域学会/出版社旗舰期刊列表、顶刊综述来源作为替代证据，但必须标 `quality_source: proxy`；
- 管理/经济/商科可用 FT50、UTD24、ABS/AJG、领域公认顶刊列表；
- 综合顶刊包括 Nature、Science、PNAS、Cell 等及其相关子刊；但子刊是否适配本领域，需要按文章主题和期刊 scope 再判断；
- 中文文献必须记录中文期刊层级，最低按用户约定采用川大 B 以上；不能确认时标 `needs-journal-quality-qc`。

纳入规则：

```text
include:
  - field-top-journal
  - general-top-journal-or-sister-journal
  - authoritative-review
  - original-method-paper
  - official-standard-or-doc
conditional:
  - Q1/SJR-Q1 as supporting evidence, not sole criterion
exclude_or_low_weight:
  - ordinary related paper without journal-quality evidence
  - unclear venue
  - predatory or non-peer-reviewed source unless used only as background
```

## 执行状态

本 Skill 只设计策略，不执行检索。输出中必须写：

```text
search_execution_status: planned-not-executed
next_skill_to_call: scholar-kit-literature-search
```

如果还需要官方文件、标准、package docs 或普通 web 资料，另写：

```text
non_literature_routes:
```

## 完成标准

- 每条检索策略绑定 `target_arrow_id`；
- 写清期刊质量门槛、候选期刊名单如何获得、用什么来源核验；
- 写清摘要扫描能回答什么、不能回答什么；
- 写清何时必须深读全文、图表或补充材料；
- 写清文献检索是否应交给 `$scholar-kit-literature-search`；
- 不把关键词堆砌当作检索策略；
- 输出可直接交给 `repair-abstract-scan`。
