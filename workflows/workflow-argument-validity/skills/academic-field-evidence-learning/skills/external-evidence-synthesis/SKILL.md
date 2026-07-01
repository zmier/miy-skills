---
name: external-evidence-synthesis
description: 学术外部证据合成子 Skill。用于 academic-field-evidence-learning 第五步，针对 judge-arrow 请求，把文献、方法原文、官方资料或数据库检索结果合成为 external-evidence-ledger 和 handoff-to-arrow-audit，用于回填箭头状态。
---

# External Evidence Synthesis

## 定位

本 Skill 只回答：外部证据是否改变某条箭头的审计判断。它不生成修复建议。

## 输入

- `field-learning-request-ledger.md` 中的 `judge-arrow` 请求；
- `field-search-strategy.md`；
- `cnki-request-ledger.md`（中文经管/中文社科或 CNKI-needed 请求时）；
- `domain-map.md`、`key-journal-map.md`；
- 检索结果、摘要、原文、方法文档、官方资料；
- `internal-arrow-audit-table.md`。

## 输出

```text
external-evidence-ledger.md
handoff-to-arrow-audit.md
```

字段：

```text
evidence_id
request_id
target_arrow_id
evidence_type
source
verification_level
source_quality
finding
effect_on_arrow_status
remaining_qc
```

## 判断规则

- 区分 `metadata verified`、`abstract verified`、`fulltext verified` 和 `manual verification needed`；
- 未检索、检索失败、权限不足不能写成“没有证据”；
- 普通 web 不能替代数据库级文献检索或官方来源；
- 证据只能回填对应 `target_arrow_id`，不能新增未经审计的新问题。
- CNKI 路线的结论必须读取 `cnki-request-ledger.md`：`completed-true-zero` 只能说明该 query 真零；`metadata-only` / `abstract-only` 只能弱回填；`technical-failure`、`login-or-captcha-blocked`、`manual-verification-needed` 必须保留为 `needs-external-evidence` 或 `needs-qc`。

## 完成标准

- 每条外部证据绑定 request id 和 arrow id；
- 清楚说明是否建议把状态改成 `strong / strong-with-qc / weak / broken / unclear / needs-qc`；
- 无法判断时保留 `needs-external-evidence` 或 `needs-qc`；
- 对中文文献 gap、中文指标有效性、本土制度语境等依赖 CNKI 的判断，只有 `abstract` 以上且来源质量符合要求时才能强回填；`metadata-only` 默认只能生成 `strong-with-qc`、`weak-with-qc` 或 `needs-fulltext-check`；
- 输出可直接交给 `academic-argument-arrow-audit` 回填。
