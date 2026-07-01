# Audit Route Plan

## Route Summary

| route | arrows | action |
|---|---|---|
| parent academic arrow audit | A001, A002, A003, A008, A010, A011, A014, A015, A017, A018, A030-A036, A039-A043 | 用通用断点 + academic-fallacy-adapter 审计。 |
| academic-causal-arrow-audit | A012, A025, A026, A027 | 检查 DID 设计、前趋势、聚类、堆叠 DID/Bacon 是否支撑因果声称。 |
| academic-statistical-result-arrow-audit | A013, A028, A029 | 检查表4结果、显著性、量纲和经济意义。 |
| academic-literature-gap-arrow-audit | A006, A042 | 本轮不外部检索，只标 `needs-citation-qc / needs-search-if-used-as-major`。 |

## No Hard Method Gap

本轮未发现必须立即联网学习才能初步审计的“新方法”。Oster、DID、PSM、Bacon 分解均可先按现有审计框架初判；若后续要把某一项写成强 major concern，再单独做 method/source QC。

## QC Escalation

| escalation | arrows | reason |
|---|---|---|
| table cell visual QC | A013, A028, A029, A030-A035, A039, A040 | 关键表格来自 restored table，最终引用前需 cell-level 复核。 |
| figure QC | A027, A036 | Bacon 和 placebo 图未精准裁剪。 |
| citation search | A006, A041, A042 | 文献 gap 或贡献声称若要写强问题，需要检索验证。 |
| DAG-ready source check | A012, A025, A026, A027 | 对照组、处理时点、行业冲击外生性需要回原文精读。 |

