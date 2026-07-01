# External Evidence Ledger Template

## Purpose

记录集中检索/学习后的外部证据，并说明它如何改变对应 `arrow_id` 的审计判断。

## Evidence Table

| request_id | target_arrow | source | source_type | source_quality | key_finding | relevance_to_arrow | what_it_changes | followup_status |
|---|---|---|---|---|---|---|---|---|
| XR1 | A010 |  | method paper / top-journal application / policy document / official data / regulatory filing / official docs / CNKI / web | high/medium/low |  |  | weak-confirmed / broken-confirmed / strong-after-search / still-unclear |  |

## Not-Searched / Pending Row

如果本轮明确不检索或无法检索，仍然生成 ledger，但使用 pending 格式，不得伪造来源：

| request_id | target_arrow | search_status | reason_not_searched | current_audit_status | what_would_change_after_search | followup_status |
|---|---|---|---|---|---|---|
| XR1 | A010 | not-searched | 本轮为内部盲跑，不执行外部检索 | needs-external-evidence | 若权威文献支持 KV 可代表信息披露质量，则可能转为 strong-with-qc；若只支持更窄指标，则转为 weak-confirmed | pending |

## Source Quality

```text
high:
  原始方法论文、FT50/UTD24/综合顶刊、Nature/Science/PNAS、政策/监管正式文件、官方统计数据、官方文档、replication package

medium:
  权威综述、教材、handbook、领域核心中文期刊

low:
  普通网页、博客、未核验讲义、二手解释
```

## 回填规则

每条外部证据必须回答：

```text
它加强、削弱还是不改变 target_arrow 的判断？
它是否足以把 needs-external-evidence 改为 weak / broken / strong？
它是否只适合留作背景，不应进入审稿判断？
```
