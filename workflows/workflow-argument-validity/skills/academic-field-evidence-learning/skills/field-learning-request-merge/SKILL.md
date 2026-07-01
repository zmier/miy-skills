---
name: field-learning-request-merge
description: 学术领域学习需求合并子 Skill。用于 academic-field-evidence-learning 第一步，把 external-evidence-request、repair-knowledge-gap、internal arrow audit 中的外部学习需求合并为 field-learning-request-ledger，区分 judge-arrow、repair-arrow 和 field-map，不执行检索。
---

# Field Learning Request Merge

## 定位

本 Skill 只负责把第 3 步和第 5 步回流的学习需求整理成一个可检索、可阅读、可回填的任务台账。

## 输入

- `external-evidence-request.md`；
- `repair-knowledge-gap.md`；
- `internal-arrow-audit-table.md` 或 `academic-arrow-audit-table.md`；
- `academic-arrow-break-summary.md`；
- `empirical-method-qc-request.md`、`chinese-literature-gap-request.md`、`handoff-to-field-learning.md`（adaptor 产物，如有）；
- 领域关键词、作者参考文献和任务目标。

## 输出

```text
field-learning-request-ledger.md
cnki-request-ledger.md（中文经管/中文社科或 CNKI-needed 请求时）
```

字段：

```text
learning_request_id
request_type: judge-arrow / repair-arrow / field-map
target_arrow_ids
source_request_ids
learning_question
shared_topic_or_method
priority
must_answer_before
can_merge_with
required_external_routes
adapter_source
sensitivity_type
notes
```

若请求来自中文经管 adaptor、中文文献 gap、中文制度语境、中文指标有效性或中文期刊报告规范，必须同步创建或更新 `cnki-request-ledger.md`，并为每条请求生成：

```text
cnki_request_id
source_request_id
target_arrow_id
local_sensitivity_type
query_intent
required_scope
required_quality_floor
execution_status: not-started
```

## 完成标准

- 每条需求可追溯到 `request_id` 或 `target_arrow_id`；
- 相同主题、方法、指标、领域或文献流的请求已合并；
- `judge-arrow` 和 `repair-arrow` 分开标记，但允许共享检索和阅读结果；
- 中文经管/中文社科或 `CNKI-needed` 请求已经进入 `cnki-request-ledger.md`，而不是只写在 notes 里；
- 不新增未被前序步骤提出的问题。
