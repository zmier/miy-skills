---
name: field-search-fulltext-strategy
description: 学术领域检索与全文获取策略子 Skill。用于 academic-field-evidence-learning 第三步，根据 field-learning-plan 设计 scholar-kit-literature-search 路由、期刊质量门槛、摘要扫描、fulltext-acquisition-plan、PDF或HTML还原移交和非文献资料路线；实际全文获取交给 paper-fulltext-acquisition，不绕过付费墙。
---

# Field Search Fulltext Strategy

## 定位

本 Skill 负责设计检索和全文获取策略。它可以调用或移交 `$scholar-kit-literature-search`，但不自行实现数据库检索；它只生成 `fulltext-acquisition-plan.md`，实际合法全文获取交给 `../paper-fulltext-acquisition/SKILL.md`。

## 输入

- `field-learning-plan.md`；
- `field-learning-request-ledger.md`；
- `cnki-request-ledger.md`（如已有中文深库请求）；
- 关键词、作者参考文献、seed journals；
- 来源约束：领域顶刊、综合顶刊及其子刊、FT50/UTD24、中文川大 B+；
- 可用工具状态。

## 输出

```text
field-search-strategy.md
fulltext-acquisition-plan.md
cnki-request-ledger.md
external-reading-log.md
field-learning-qc.md
```

## 策略规则

- 文献检索默认调用 `$scholar-kit-literature-search`；
- `journal_quality_policy` 必须写明：领域顶刊、综合顶刊及其子刊、权威综述、方法原文优先；
- 中文经管、中文社科或 `CNKI-needed` 请求必须设计 CNKI query block，并更新 `cnki-request-ledger.md`；
- CNKI query block 至少区分：精确词、扩展词、相邻构念、方法/指标词、本土制度词；
- 只跑一个精确词只能支撑该精确词 `completed-true-zero`，不能支撑“中文文献没有相关研究”；
- Q1/SJR-Q1 只能作为辅助证据，不能单独替代领域顶刊判断；
- 政策文件、官方数据、标准文档、package docs 写入 `non_literature_routes`；
- 需要全文时，优先合法 OA、publisher OA、OpenAlex OA、Unpaywall、arXiv、PMC、bioRxiv/medRxiv；
- 无法合法获取全文时标记 `requires-human-access` 或 `no-legal-fulltext-found`，不绕 paywall；
- 对每个 `fulltext_trigger=yes` 的来源，必须写入 `fulltext-acquisition-plan.md`，并标明下一步调用 `paper-fulltext-acquisition`。

## 移交字段

`fulltext-acquisition-plan.md` 至少包含：

```text
source_id
title_or_doi
why_fulltext_required
requested_materials
route_priority
legal_access_route
fallback_if_unavailable
next_skill_to_call: paper-fulltext-acquisition
```

## 完成标准

- 每条检索策略绑定 request id；
- 写清数据库路线、query blocks、纳入排除标准和期刊质量证据；
- 中文经管/中文社科或 `CNKI-needed` 请求有 `cnki-request-ledger.md`，并记录每个 query block 的 `execution_status`、`verification_level` 和 `fulltext_status`；
- 写清哪些只需摘要，哪些必须全文/图表/补充材料；
- 需要全文的来源已移交给 `paper-fulltext-acquisition`；
- 失败、验证码、权限问题写入 `field-learning-qc.md`；
- 输出可交给 `domain-map-building`、`external-evidence-synthesis` 和 `repair-knowledge-synthesis`。
