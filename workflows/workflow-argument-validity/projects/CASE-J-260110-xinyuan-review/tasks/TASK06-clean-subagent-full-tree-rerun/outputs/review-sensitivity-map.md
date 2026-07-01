# Review Sensitivity Map

2B 审稿显影树只显影后续验箭头候选，不写最终审稿意见。所有条目均锚定到 2A evidence ledger 或 TASK05 QC；未把这些疑点混入作者树本体。

| sensitivity_id | 类型 | 需并读的 evidence_ids | 需回看的原文链接 | 为什么值得后续验箭头 | 影响 X1/X2/Y |
|---|---|---|---|---|---|
| S-T11-1 | mechanism-prose-table-conflict | E-MECH-RC-5; E-MECH-RC-6; E-MECH-RC-7; E-MECH-RC-8; E-T11-CONFLICT-1; E-T11-CONFLICT-2 | [[tables-restored/table-11]]; [[table-visual-qc#Key Finding]]; manuscript 五（一）para 3 | 正文称 PosCAR 三组均显著、NegCAR 三组均不显著；PDF 表 11 第三列显示 PosCAR[-10,10] 不显著而 NegCAR[-10,10] 显著为负。需后续验“声誉竞争机制”箭头是否在全窗口下成立。 | X2 / P7.1 |
| S-KV-1 | construct-measure-fit | E-YDEF-1; E-YDEF-2; E-YDEF-3; E-DESC-1; E-ROB-12 | [[tables-restored/table-01]]; [[tables-restored/table-09]] | 作者将 KV 指数解释为信息披露质量，并用 DA 做替代变量。需后续验 KV 与“信息披露质量改善/行业自律发展”的构念承载是否一致。 | X2 / P3 / P9 |
| S-TIME-1 | treatment-timing | E-SAMPLE-2; E-XDEF-4; E-XDEF-5; E-PT-1; E-PT-2; E-ROB-13 | manuscript 三（一）、三（二）；[[tables-restored/table-03]]; [[tables-restored/table-09]] | 事件窗口为前 3 年至后 2 年，POST 在 t 至 t+2 为 1，稳健性又按月份重构 POST_Month。需后续验理论反应过程、POST 编码和动态效应是否一致。 | X2 / P1 / P5 |
| S-SAMPLE-1 | sample-representativeness | E-SAMPLE-3; E-SAMPLE-4; E-SAMPLE-5; E-SAMPLE-7; E-SAMPLE-8; E-HET-MON-3 | manuscript 三（一）；[[tables-restored/table-16]] | 样本剔除多家行业事件、仅保留首次事件、剔除事件公司，并在金额不可识别时减少样本。需后续验识别清洁度与外部有效性/机制适配之间是否存在张力。 | X2 / P4 / P10 |
| S-CLUSTER-1 | cluster-level-fit | E-MODEL-3; E-XDEF-1; E-XDEF-5; E-MAIN-1; E-MAIN-3 | manuscript 三（三）；[[tables-restored/table-04]] | 处理变量在行业-事件时间层级变化，标准误按公司层面聚类。需后续验聚类层级是否匹配 treatment variation。 | X2 / P5 / P6 |
| S-NULL-IT-1 | null-result-reversal | E-MECH-IT-2; E-MECH-IT-3; E-MECH-IT-4; E-MECH-IT-5 | [[tables-restored/table-13]] | 作者用监管距离组间差异不显著、处罚结果不显著排除信息传导机制。需后续验“不显著”是否足以排除机制，以及 PunishCount/PunishStrict 是否是监管效率的充分代理。 | X2 / P7.3 |
| S-HET-COMP-1 | mechanism-boundary-consistency | E-THEORY-H1-2; E-THEORY-H2A-1; E-HET-COMP-1; E-HET-COMP-2; E-HET-COMP-3; E-HET-COMP-4 | manuscript 理论分析；[[tables-restored/table-18]] | 表 18 低竞争组系数显著为正，意味着 KV 上升、披露质量下降。需后续验该边界条件是否削弱主文“行业自律发展”的上升命题。 | X2 / P10.5 / Y |
| S-REPUTATION-1 | mechanism-sample-consistency | E-MECH-RC-1; E-MECH-RC-2; E-MECH-RC-3; E-MECH-RC-4; E-MECH-RC-5; E-MECH-RC-7 | [[tables-restored/table-10]]; [[tables-restored/table-11]] | 表 10 事件公司平均 CAR 为正，表 11 再按正/负 CAR 分组解释同行反应。需后续验事件公司市场反应样本和同行回归样本是否同构。 | X2 / P7.1 |
| S-ROBUST-1 | robustness-threat-fit | E-ROB-1; E-ROB-5; E-ROB-6; E-ROB-7; E-ROB-8; E-ROB-9; E-ROB-10; E-ROB-11 | [[tables-restored/table-05]] 至 [[tables-restored/table-08]] | 稳健性覆盖多时点 DID、样本匹配、共同政策因素和遗漏变量，但图 1、图 2 未做图像 QC。需后续验这些稳健性是否真正回应核心识别威胁。 | X2 / P8 |
| S-POLICY-1 | elevated-claim-over-evidence | E-MAIN-3; E-MECH-RC-3; E-MECH-MP-3; E-MECH-MP-5; E-X1-POLICY-1; E-HET-COMP-2 | [[tables-restored/table-04]]; [[tables-restored/table-12]]; manuscript 七（二） | 作者由同行 KV 改善和两类机制证据上升到主动披露豁免/减轻处罚机制。需后续验从公司层面信息披露质量到监管制度设计的跃迁是否足够。 | Y / P9 |
