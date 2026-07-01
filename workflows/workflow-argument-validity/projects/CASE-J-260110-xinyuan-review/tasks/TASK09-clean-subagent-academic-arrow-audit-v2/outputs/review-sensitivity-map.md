# Review Sensitivity Map

| sensitivity_id | 类型 | 需并读的 evidence_ids | 需回看的原文链接 | 为什么值得后续验箭头 | 影响 X1/X2/Y |
|---|---|---|---|---|---|
| S01 | construct-measure | E-YDEF-1; E-YDEF-2; E-DESC-1; E-ROB-ALT-1 | manuscript 三-二-1; 表1; 表2; 表9 | KV 被作者直接等同于信息披露质量，且替代变量 DA 也被用来稳健化同一 Y。需要确认“交易量对收益率影响系数下降”是否足以推出披露质量提升。 | X2; Y0 |
| S02 | treatment-timing | E-XDEF-1; E-DID-TREAT-1; E-DID-POST-1; E-DID-POST-2; E-ROB-ALT-2; E-ROB-ALT-3 | manuscript 三-二-2; 表9 | 处理冲击、同行范围、POST 年度编码决定 DID 的核心 X。月度重构改变样本量，需回看口径一致性。 | X2 |
| S03 | identification-method | E-MODEL-1; E-MODEL-3; E-MODEL-4; E-MODEL-5; E-PRETREND-1 to E-PRETREND-4; E-ROB-STACK-1; E-ROB-STACK-2; E-ROB-BACON-1 | manuscript 三-三; 四-二; 表3; 表5; 图1 | 作者用 DID、前趋势、堆叠 DID 和 Bacon 支撑因果解释；内部 evidence 支持方向，但聚类层级、错峰处理和前趋势充分性需方法 QC。 | X2; Y0 |
| S04 | main-result-scale | E-MAIN-1; E-MAIN-2; E-MAIN-3; E-MAIN-4; E-MAIN-5; E-DESC-1 | 表4; 表2; manuscript 四-三 | 负且显著的交互项是 X2 的主支撑；9.58% 的经济意义计算需要确认指标方向、基数和量纲解释。 | X2 |
| S05 | reputation-mechanism-conflict | E-MECH-CAR-1; E-MECH-CAR-2; E-MECH-CAR-3; E-MECH-REP-1; E-MECH-REP-2; E-MECH-REP-3 | 表10; 表11; manuscript 五-一 | 表11列(3)显示 PosCAR[-10,10] 不显著、NegCAR[-10,10] 显著，与作者“三组 PosCAR 显著、NegCAR 不显著”叙述冲突。 | X2; Y0 |
| S06 | market-pressure-mechanism | E-MECH-PRESS-1 to E-MECH-PRESS-5 | 表12; manuscript 五-二 | 高关注组显著、低关注组不显著，且组间 p 值一个边际、一个强显著；支撑市场压力但仍需表格 QC。 | X2 |
| S07 | mechanism-exclusion | E-MECH-INFO-1 to E-MECH-INFO-4 | 表13; manuscript 五-三 | 作者用监管距离和处罚结果不显著排除信息传导机制；内部上可能只能说明未观测到某些监管结果，未必排除信息传导。 | X2 |
| S08 | robustness-threat-fit | E-ROB-MATCH-1 to E-ROB-MATCH-3; E-ROB-COMMON-1; E-ROB-COMMON-2; E-ROB-OSTER-1; E-ROB-OSTER-2; E-ROB-PLACEBO-1; E-ROB-PLACEBO-2 | 表6; 表7; 表8; 图2 | 稳健性覆盖匹配、共同政策、遗漏变量、伪处理，但需要逐条看是否回应真正威胁，而不只是重复同一模型框架。 | X2 |
| S09 | heterogeneity-boundary | E-HET-LEADER-*; E-HET-OWN-*; E-HET-MON-*; E-HET-RELY-*; E-HET-COM-* | 表14-18; manuscript 六 | 异质性被作者用于解释边界和机制，部分组间差异不显著，低竞争组方向相反。 | X2; Y0 |
| S10 | contribution-elevation | E-CONTR-1; E-CONTR-2; E-POLICY-1; E-POLICY-2; E-POLICY-3; E-CIT-CONTR-* | manuscript 一; 七 | 从局部 DID 发现上升到文献贡献和政策启示，依赖 X1 文献 gap、X2 因果/机制链和外部文献真实性。 | Y0 |
