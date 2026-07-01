# Review Sensitivity Map Full V2

状态：`2B-review-sensitivity-tree / review-frozen`

本文件不是最终审稿意见，也不读取欣媛意见。它只基于 `evidence-ledger.full-v2.md` 显影：哪些证据组合值得后续 `academic-argument-arrow-audit` 并读和验箭头。

字段：

```text
sensitivity_id | 显影类型 | 需并读的 evidence_ids | 原文链接 | 后续要验的箭头 | 潜在影响
```

## 显影表

| sensitivity_id | 显影类型 | 需并读的 evidence_ids | 原文链接 | 后续要验的箭头 | 潜在影响 |
|---|---|---|---|---|---|
| S1 | concept-consistency | E-P2-3, E-P2-4, E-P7-5, E-H3-2 | [[manuscript#Figure 3]], [[manuscript#Table 10]], [[manuscript#para 169]], [[manuscript#para 190]] | 低信息含量/低危害违规披露 -> 市场强正向反应 -> 声誉竞争机制成立 | X2 |
| S2 | sample-representativeness | E-P5-2, E-P5-3, E-P5-4, E-P5-5, E-P5-7 | [[manuscript#para 37]], [[manuscript#para 38]], [[manuscript#para 39]], [[manuscript#para 40]] | 剔除同业重叠事件和事件公司自身 -> 干净识别样本 -> 能代表同行溢出机制 | X2 |
| S3 | direct-effect-baseline | E-P5-5, E-P2-3, E-P2-4, E-P3-1 | [[manuscript#para 40]], [[manuscript#Figure 3]], [[manuscript#Table 10]] | 事件公司获得市场认可 -> 同行有理由模仿并改善披露 | X2 |
| S4 | treatment-timing | E-P1-1, E-P1-3, E-P6-3, E-P8-7 | [[manuscript#para 54]], [[manuscript#para 101]], [[manuscript#para 144]] | 当年无问询/处罚 + POST=t...t+2 -> 真正主动披露且效应时点被正确捕捉 | X2 |
| S5 | cluster-level-fit | E-P1-3, E-P6-1, E-P6-2, E-P6-4 | [[manuscript#para 54]], [[manuscript#para 81]], [[manuscript#Table 4]] | 公司层聚类后的显著主效应 -> 统计推断可靠 | X2 |
| S6 | construct-measure-fit | E-P4-1, E-P4-2, E-P4-3, E-P4-4, E-P9-4 | [[manuscript#para 90]], [[manuscript#para 105]], [[manuscript#para 215]] | KV 下降 -> 信息披露质量提升 -> 行业自律/资本市场环境净化 | X2/Y |
| S7 | mechanism-sample-consistency | E-P2-3, E-P2-4, E-P7-1, E-P5-3, E-P5-4 | [[manuscript#Figure 3]], [[manuscript#Table 10]], [[manuscript#Table 11]], [[manuscript#para 38]], [[manuscript#para 39]] | 图3/表10 的市场正反应 -> 表11 的回归样本声誉竞争机制成立 | X2 |
| S8 | null-result-reversal | E-P7-3, E-P7-4, E-P7-5 | [[manuscript#Table 13]], [[manuscript#para 169]] | 监管距离/处罚不显著 -> 信息传导机制不成立 | X2 |
| S9 | imported-measure-level | E-H4-1, E-H4-2 | [[manuscript#para 196]], [[manuscript#Table 17]] | Rajan and Zingales 方法 -> 公司年度外部融资依赖异质性解释成立 | X2/Y |
| S10 | robustness-threat-fit | E-P8-1, E-P8-2, E-P8-3, E-P8-4, E-P8-5, E-P8-6, E-P8-7, S2, S4, S5, S6 | [[manuscript#para 116]], [[manuscript#para 128]], [[manuscript#para 134]], [[manuscript#para 144]] | 多种稳健性通过 -> 核心威胁已被回应 | X2 |
| S11 | storyline-premise-consistency | E-G3-1, E-G3-3, E-P2-2, E-P3-1, E-H3-2 | [[manuscript#para 2]], [[manuscript#para 190]] | 主动披露的行为信号/内容信息/违规严重性在各章节保持同一前提 | X2 |
| S12 | policy-overextension | E-P4-3, E-P4-4, E-P9-1, E-P9-3, E-P9-4 | [[manuscript#para 105]], [[manuscript#para 211]], [[manuscript#para 215]] | 同行 KV 改善 -> 监管应鼓励主动披露并设豁免/减罚机制 | Y |
| S13 | mechanism-boundary-conflict | E-H5-1, E-P3-1, E-P9-2 | [[manuscript#para 202]], [[manuscript#para 211]] | 行业竞争越强越改善披露，低竞争组反向 -> 声誉竞争机制的一般性 | X2/Y |
| S14 | reporting-integrity-anchor | E-P4-3, E-P6-4 | [[manuscript#Table 4]] | 回归表括号值、标准误/t 值、显著性标注 -> 计量报告可信 | X2/Y |

## 与 2A 的关系

2A 只说：

```text
作者用 E-P2-4 表10 CAR 显著为正支撑 P2。
作者用 E-H3-2 解释违规金额差异不大、危害不高、信息含量少。
```

2B 把它们并读为：

```text
E-P2-4 + E-H3-2 -> S1：低信息含量却强市场正反馈，需要后续验箭头。
```

因此 2B 的价值不是新增攻击，而是把后续验箭头最应该看的证据组合提前显影。
