# External Evidence Request Template

## Purpose

集中记录第一轮内部验箭头后，需要外部文献、方法、政策文件、官方数据、监管文件、官方文档、citation verification 或联网核验才能定性的箭头。

## Execution Mode

```text
mode:
  internal-blind-audit / full-evidence-audit
```

- `internal-blind-audit`：本文件是“待查清单”，`status` 默认 `not-searched`，后续 ledger 只能写 pending。
- `full-evidence-audit`：本文件是集中检索任务清单，必须逐条或合并同类项处理，并回填 `external-evidence-ledger.md`。

## Request Table

| request_id | target_arrow | current_status | why_external_evidence_needed | search_type | source_priority | suggested_skill_or_route | query_seed | output_needed | status |
|---|---|---|---|---|---|---|---|---|---|
| XR1 | A010 | needs-external-evidence | 判断 KV 是否足以代表信息披露质量 | measure-validity-search | FT50 / UTD24 / QJE/JAR/TAR/JAE / 中文川大B+ | scholar-kit-literature-search / web | KV information disclosure quality alternative measures | 判断 measurement-mismatch 是否被外部文献加强或削弱 | not-searched |

## Search Type Values

```text
literature-gap-search
measure-validity-search
method-standard-search
citation-verification
official-documentation-check
policy-document-check
official-data-check
regulatory-filing-check
recent-top-journal-check
software-package-doc-check
```

## Status Values

```text
not-searched
search-in-progress
searched
true-zero-result
insufficient-result
manual-verification-needed
technical-failure
```
