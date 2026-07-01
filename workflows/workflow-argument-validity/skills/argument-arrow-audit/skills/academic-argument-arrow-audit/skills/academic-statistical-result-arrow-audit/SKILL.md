---
name: academic-statistical-result-arrow-audit
description: 学术论文统计结果箭头审计子 Skill。用于审查作者是否能用表格、系数、显著性、量纲、R2、F 值、置信区间、经济意义、报告透明度或非线性检验结果推出经验发现；特别检查括号值/标准误/t值、星号、聚类说明、代理指标与实体结论之间的跳跃；输出 statistical-result-arrow-audit ledger。
---

# Academic Statistical Result Arrow Audit

## 定位

本子 Skill 审查：

```text
table / coefficient / significance / model fit -> empirical finding
```

核心问题：

```text
表格和统计结果是否足以支撑作者声称的经验发现？
```

## 输入

- 目标 `arrow_id`；
- 表格、图、模型、系数、标准误、显著性、样本量；
- 表注、括号值含义、星号说明、聚类层级、固定效应说明；
- 变量定义、量纲、转换、描述统计；
- 作者对经济意义、方向、大小和稳健性的解释。

## 审查主轴

1. 固定作者声称的发现；
2. 核对方向、显著性和样本；
3. 核对量纲、转换和经济意义；
4. 检查统计报告是否透明；
5. 检查表格报告与正文解释是否一致；
6. 判断结果是否支持作者上升后的说法。

## 常见检查

```text
significance:
  p-value / t-stat / standard error / confidence interval 是否清楚？

magnitude:
  系数大小是否有经济意义？
  变量单位变化是否说清？

scale:
  share、log、index、percentage point、level 是否混用？

model fit / diagnostics:
  R2、first-stage F、weak IV、clustered SE、fixed effects 是否与作者声称相关？

reporting QC:
  括号内数值到底是标准误、t 值还是 z 值？
  星号、p 值、标准误和聚类层级是否说明一致？
  表注和正文是否矛盾？
  表格样本量、固定效应、控制变量是否与正文一致？

proxy result vs substantive claim:
  表格直接支持的是代理指标变化，还是作者上升后的实体概念？
  例如 KV 下降支持的是 KV 指标改善，不自动等于行业自律或长期披露治理改善。

nonlinear / NPLR:
  非线性形状、拐点、边际效应、显著区间是否支撑作者说法？
```

## 输出

```text
statistical_result_arrow_audit:
  arrow_id:
  claimed_finding:
  table_or_figure:
  reported_statistics:
  scale_and_unit_status:
  significance_status:
  magnitude_status:
  reporting_qc:
  proxy_to_substantive_claim_status:
  status: strong / strong-with-qc / weak / broken / unclear / needs-qc / needs-external-evidence
  qc_flags:
  why_it_breaks_or_holds:
  impact_on_X2_or_Y:
  fix_or_downgrade:
```

## 完成标准

- 不用“显著”两个字替代统计解释；
- 不在未看表格时标 `verified`；
- 表注和括号值含义不一致时，标 `reporting-qc`，不得把显著性解释写死；
- 量纲不清时标 `unclear` 或 `needs-qc`，并在 `qc_flags` 写 `scale-qc`、`table-cell-qc` 或 `reporting-qc`；
- 表格只支持代理指标时，必须写清是否存在 `proxy-to-substantive-claim` 跳跃；
- 方法知识不足时记录 `method_knowledge_gap`；
- 输出交回父 Skill 的 `academic-arrow-audit-table.md`。
