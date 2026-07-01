# CNKI Request Ledger

status: pending

## 用途

本台账用于中文经管、中文社科或任何需要中文深库判断的学术审稿任务。

它回答：

```text
哪些中文文献 / 中文制度 / 中文期刊语境问题需要查 CNKI？
实际跑了哪些 query？
结果是 completed、true-zero、metadata-only、fulltext-needed，还是 technical-failure？
这些状态能否回填目标箭头？
```

## 字段

| cnki_request_id | source_request_id | target_arrow_id | local_sensitivity_type | query_intent | query_terms | required_scope | required_quality_floor | execution_status | result_count | selected_records | verification_level | fulltext_status | effect_on_arrow_status | what_can_be_concluded | what_cannot_be_concluded | next_action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## execution_status

```text
not-started
completed
completed-true-zero
metadata-only
abstract-only
fulltext-verified
technical-failure
login-or-captcha-blocked
manual-verification-needed
insufficient-result
not-required
```

## verification_level

```text
query-only
metadata
abstract
fulltext
manual
source-qc
```

## fulltext_status

```text
not-needed
needed
available
human-download-needed
blocked
not-legal-access
```

## 解释纪律

- `completed-true-zero` 只能说明当前 query / scope / quality floor 下没有结果，不能自动推出“中文文献没有相关研究”；
- `metadata-only` 不能支撑强判断，只能生成 `needs-fulltext-check` 或 `manual-verification-needed`；
- `technical-failure`、`login-or-captcha-blocked` 不能写成“没有文献”；
- CNKI 查询必须能回填到 `target_arrow_id`，不能只做泛泛背景检索；
- 如要判断中文文献 gap 是否真实，必须记录 query 扩展过程，不能只跑一个精确词。

