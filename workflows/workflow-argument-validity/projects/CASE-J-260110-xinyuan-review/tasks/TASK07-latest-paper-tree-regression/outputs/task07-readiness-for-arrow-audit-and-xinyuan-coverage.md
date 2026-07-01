# TASK07 Readiness For Arrow Audit And Xinyuan Coverage

## Verdict

TASK07 is sufficient to enter `academic-argument-arrow-audit`.

It provides the required author-tree inputs:

- `canonical-node-ledger.md`
- `canonical-edge-ledger.md`
- `evidence-ledger.md`
- `recursive-tree-master.md`
- `evidence-expanded-mermaid.md`
- `extraction-qc.md`

The strongest point is that evidence has been decomposed into table coefficients, sample rules, variable definitions, treatment timing, clustering, mechanism evidence, robustness evidence, heterogeneity evidence, and citation uses. This is enough for the next stage to ask, arrow by arrow:

```text
A 是否足以推出 B？
```

The main caveat is that arrow audit will still need selective source checking for table cells, figures, citation notes, and some implied comparison/control-group details.

## Coverage Of Xinyuan Review

| Xinyuan issue | TASK07 coverage | Key TASK07 materials | Coverage judgment |
|---|---|---|---|
| X1 轻微违规 / 低信息含量 vs 强声誉效应 | partial-high | `P2a`, `P2b`, `P7a`, `P8f`; `E-THEORY-SIGNAL-1`, `E-THEORY-REP-1`, `E-MECH-CAR-*`, `E-MECH-REP-*`, `E-HET-MON-*` | Evidence exists, but arrow audit must combine theory, CAR, Table 11, and severity heterogeneity to expose the “行为信号 vs 内容信息” slippage. |
| X2 样本筛选偏差 | high | `P1c`, `P4b`; `E-SAMPLE-2` to `E-SAMPLE-6`; edges `A011`, `A018`, `A023`, `E007`, `E013` | Materials are sufficient to test whether clean sample rules weaken mechanism-relevant sample and external validity. |
| X3 事件公司自身效应缺失 | medium | `P1c`; `E-SAMPLE-5`; edge `A018` | TASK07 records that event firms are excluded, but does not itself create the missing direct-effect baseline claim. Arrow audit should formulate this as a hidden-premise gap. |
| X4 KV 指数支撑宏大标题 / 行业自律 | high | `P3`, `P6`, `P9`; `E-YDEF-*`, `E-DESC-1`, `E-MAIN-*`, `E-CONTR-*`, `E-POLICY-*`; edges `A010`, `A002`, `A003` | Sufficient for construct-measure and finding-contribution audit. |
| X5 主动披露定义时序漏洞 | high | `P1a`, `P1b`; `E-XDEF-*`, `E-DID-POST-*`; edges `A016`, `A017`, `E005`, `E006` | Sufficient to ask whether “no same-year inquiry/penalty” proves genuine active disclosure. |
| X6 EFD 构造层级错配 | high | `P8g`; `E-HET-RELY-1`, `E-HET-RELY-2`, `E-HET-RELY-3`, `E-CIT-RELY-1`; edge `E030` | Sufficient to audit company-year EFD vs Rajan-Zingales industry-level long-run construct. Citation note verification would strengthen it. |
| X7 聚类层级 | high | `P5a`; `E-MODEL-4`, `E-MODEL-5`, `E-MAIN-1`, `E-MAIN-2`; edges `A025`, `E015` | Sufficient to audit treatment variation level vs clustering level. |
| X8 POST 定义 / 时间滞后 | high | `P1b`, `P5b`, `P8c`; `E-DID-POST-*`, `E-PRETREND-*`, `E-ROB-ALT-2`, `E-ROB-ALT-3`; edges `A017`, `A026`, `A035` | Sufficient to test event-year POST and lagged effect logic. |
| X9 声誉机制样本一致性 | medium-high | `P7a`; `E-MECH-CAR-*`, `E-MECH-REP-*`; edge `A030`, `E020`, `E021` | TASK07 has CAR and Table 11 evidence, but still needs explicit sample-size/sample-consistency checking between figure/event study and Table 11 regression. |
| X10 信息传导机制排除反向解释 | high | `P7c`; `E-MECH-INFO-*`; edge `A032`, `E023` | Sufficient for alternative-explanation audit: insignificant punishment outcomes may not rule out information transmission. |
| X11 稳健性避重就轻 | high | `P8a` to `P8d`; `E-ROB-*`; edges `A015`, `A033` to `A036`, `E024` to `E027` | Sufficient to audit whether robustness tests address the actual threats: sample selection, construct validity, timing, clustering, industry boundary. |
| X12 表注错误 / t 值 vs 标准误 | partial | `E-MODEL-4`; many table coefficients record bracket values; QC says table cells need visual check | TASK07 is enough to flag reporting-QC as a candidate, but final claim requires table-note cell-level verification. |

## What Is Already Ready

Arrow audit can immediately start from these high-value handoff targets:

| target | candidate arrows | why |
|---|---|---|
| construct-measure fit | `A010`, `A002`, `A003` | KV decline and short-run disclosure proxy may not support broad “industry self-discipline” claim. |
| sample-mechanism fit | `A011`, `A018`, `A023` | Sample restrictions and event-firm exclusion may remove mechanism-relevant events. |
| identification-causal fit | `A012`, `A025`, `A026`, `A027` | DID design, timing, pretrend, clustering, and staggered treatment support need testing. |
| treatment-definition fit | `A008`, `A016`, `A017` | “Active disclosure” definition may include strategic or forced early disclosure. |
| mechanism-claim fit | `A014`, `A030`, `A031`, `A032` | Reputation, market pressure, and information transmission exclusion need cross-evidence audit. |
| robustness-threat fit | `A015`, `A033` to `A036` | Robustness tests may not target the core threats. |
| contribution elevation | `A002`, `A003`, `A041` to `A043` | Empirical short-run finding may be over-elevated to industry self-discipline and policy recommendations. |

## What Still Needs Checking During Arrow Audit

1. Table cell-level verification.

   TASK07 uses page-level table QC and restored table files. Before final review prose quotes coefficients, check key cells in Tables 3, 4, 10, 11, 13, 17, and 18.

2. Figure sample and shape verification.

   Figure 1/2, and the CAR figure discussed by Xinyuan, need precise figure crops or source-table confirmation if the audit relies on visual distributions.

3. Citation-note verification.

   Citation evidence is present as author-use evidence, but many links are `needs-citation-link`. If the arrow audit attacks or defends literature support, it should verify those citation notes.

4. Implied comparison/control-group text.

   `extraction-qc.md` notes that the comparison/control group is partly implied by `Peerdumy = 0`. A DAG-oriented audit should inspect the exact author wording before making a strong design criticism.

## Bottom Line

TASK07 does not itself reproduce Xinyuan's review opinion, because that belongs to arrow audit and issue selection. But it gives enough structured material to cover almost all of Xinyuan's claims and evidence.

Expected coverage:

```text
Can cover directly: X2, X4, X5, X6, X7, X8, X10, X11
Can cover after combining evidence: X1, X9
Can cover as hidden-premise / missing-analysis issue: X3
Can cover after table-note QC: X12
```

Therefore the next step can be `academic-argument-arrow-audit`, using TASK07 as the input baseline and Xinyuan review only as an external comparison after the audit output is frozen.
