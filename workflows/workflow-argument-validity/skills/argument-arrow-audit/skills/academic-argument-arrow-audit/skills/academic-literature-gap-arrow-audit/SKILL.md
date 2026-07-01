---
name: academic-literature-gap-arrow-audit
description: 学术论文文献 gap 箭头审计子 Skill。用于审查作者是否能用文献缺口、知识树定位或引用证据推出 gap/contribution 成立；可编排 scholar-kit-literature-search、CNKI、WoS/OpenAlex 检索；输出 literature-gap-arrow-audit ledger，不直接写审稿意见。
---

# Academic Literature Gap Arrow Audit

## 定位

本子 Skill 只审查：

```text
literature evidence / claimed gap -> contribution or research significance
```

核心问题：

```text
作者说“现有文献没做/没做好/没从这个角度做”，这个 gap 真实、重要、不同于既有研究吗？
```

## 输入

- 目标 `arrow_id`；
- from_node：作者文献综述、gap 声称、引用清单；
- to_node：研究意义、贡献、发表价值；
- evidence_ids 与原文链接；
- 论文领域、关键词、作者声称的相邻文献流。
- 来自父 Skill 的 `external-evidence-request.md`。

本子 Skill 默认不主动扫描全篇并发起无限检索。它只处理父 Skill 已集中标记的请求。

## 外部 Skill 编排

需要补外部证据时，调用：

```text
/Users/narra/Documents/alib/Writer/.pytools/scholar-kit/skills/scholar-kit-literature-search/SKILL.md
```

调用前必须明确：

```text
检索目标：验证 gap / 找最接近研究 / 建知识树 / 查中文谱系
语种：英文 / 中文 / 中英文
质量门槛：FT50、UTD24、综合顶刊、Nature、Science、PNAS、中文川大B以上
关键词：X、Y、机制、方法、场景、近义概念
```

本 Skill 不实现检索，不覆盖 scholar-kit 子 Skill 的状态判断。

## 集中检索模式

当父 Skill 交来多个 request 时，先合并同类项，避免重复检索：

```text
A006 + A042 -> literature gap / contribution positioning
A010 + A013 + A029 -> measure validity
A025 -> method standard / clustering
A039 -> construct origin / operationalization fit
```

合并后仍需保留每个 `target_arrow` 的回填关系。

## 输出

```text
literature_gap_arrow_audit:
  arrow_id:
  author_gap_claim:
  closest_literature_streams:
  search_route:
  external_evidence_status:
  gap_status: strong / weak / broken / unclear / needs-search / needs-manual-qc
  why_gap_holds_or_breaks:
  impact_on_X1_or_Y:
  suggested_revision_or_downgrade:
```

若作为外部证据增强的一部分，还应输出到父 Skill：

```text
external_evidence_ledger_row:
  request_id:
  target_arrow:
  source:
  source_type:
  source_quality:
  key_finding:
  relevance_to_arrow:
  what_it_changes:
  followup_status:
```

## 完成标准

- 不把“作者引用少”直接等同于 gap 不成立；
- 必须区分没有检索、检索失败、真零结果和结果不足；
- 若检索证据不足，标 `needs-search` 或 `needs-manual-qc`；
- 不把非顶刊、弱相关或低质量文献直接当成推翻 gap 的证据；
- 输出交回父 Skill 的 `academic-arrow-audit-table.md`。
