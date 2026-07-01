# Evidence Ledger

| evidence_id | evidence_type | source_location | exact_content | supports_node_or_edge | granularity | qc_status | source_link |
|---|---|---|---|---|---|---|---|
| E-X1-POL-1 | policy/institution fact | manuscript 一[para 1] | 2019-12-28 修订后的《证券法》扩充信息披露责任主体和范围，并提高违法违规处罚力度。 | G1 | minimal | verified | [[manuscript_restored_with_tables#一、引言]] |
| E-X1-POL-2 | policy/institution fact | manuscript 一[para 1] | 2025-03-26 新修订《上市公司信息披露管理办法》强调事前预防式信息披露要求。 | G1 | minimal | verified | [[manuscript_restored_with_tables#一、引言]] |
| E-X1-EX-1 | text evidence | manuscript 一[para 2] | 天虹股份案例：2015年3月至4月股东违规减持超八千万元，5月19日主动披露并承诺加强学习。 | G1 | minimal | verified | [[manuscript_restored_with_tables#一、引言]] |
| E-X1-MECH-1 | text evidence | manuscript 一[para 2] | 作者指出主动披露违规可能传递诚信经营信号或降低未来声誉损失与处罚成本。 | G2 | minimal | verified | [[manuscript_restored_with_tables#一、引言]] |
| E-X1-MECH-2 | text evidence | manuscript 一[para 2] | 作者指出违规曝光也可能带来股价下跌、融资受限等风险，同行可能减少风险信息披露。 | G2 | minimal | verified | [[manuscript_restored_with_tables#一、引言]] |
| E-X1-MECH-3 | text evidence | manuscript 一[para 2] | 作者指出主动披露违规可能揭示行业共有违规手段，引发外部利益相关者对同行同类违规的担忧。 | G2 | minimal | verified | [[manuscript_restored_with_tables#一、引言]] |
| E-CIT-GAP-1 | citation evidence | manuscript 一[para 3] | 伊志宏等(2010)、滕飞等(2022)、翟胜宝等(2022)被作者用于说明既有信息披露质量研究多认为披露改善来自内外部监督。 | G3 | minimal | needs-citation-link | [[伊志宏2010产品市场竞争公司治理与信息披露质量]]; [[滕飞2022证监会随机抽查制度与上市公司规范运作]]; [[翟胜宝2022媒体关注与企业ESG信息披露质量]] |
| E-CIT-GAP-2 | citation evidence | manuscript 一[para 3] | Dye(1990)、Gleason et al.(2008)被作者用于说明信息披露可影响同行披露决策。 | G3 | minimal | needs-citation-link | [[Dye 1990 Mandatory Versus Voluntary Disclosures]]; [[Gleason Jenkins Johnson 2008 Contagion Effects]] |
| E-CIT-GAP-3 | citation evidence | manuscript 一[para 3] | Cao et al.(2018)、巫岑等(2022)、李宗泽和李志斌(2023)、陆雪艳等(2025)被作者用于说明既有同群披露研究集中于环境、创新、ESG 等特定披露。 | G3 | minimal | needs-citation-link | needs-literature-note |
| E-CIT-GAP-4 | citation evidence | manuscript 一[para 3] | Seo(2021)被作者用于说明既有文献关注信息披露的量而非质。 | G3 | minimal | needs-citation-link | [[Seo 2021 Peer Effects in Corporate Disclosure Decisions]] |
| E-X1-CONTR-1 | text evidence | manuscript 一[para 3] | 作者明示尚未有研究关注企业主动披露违规及其对同行业其他企业信息披露决策的影响。 | G4 | minimal | verified | [[manuscript_restored_with_tables#一、引言]] |
| E-CIT-CONTR-1 | citation evidence | manuscript 一[para 5] | 滕飞等(2022)、翟胜宝等(2022)、巫岑等(2022)、Beyer et al.(2010)、Beyer and Dye(2012)被作者用于定位信息披露影响因素研究。 | G4; P9a | minimal | needs-citation-link | needs-literature-note |
| E-CIT-CONTR-2 | citation evidence | manuscript 一[para 6] | Desai and Schaupp(2024)、Fu and Trigilia(2024)被作者用于定位负面信息披露研究主要关注资本提供者反应。 | G4; P9b | minimal | needs-citation-link | needs-literature-note |
| E-CIT-CONTR-3 | citation evidence | manuscript 一[para 6] | Gleason et al.(2008)被作者用于说明负面信息披露溢出研究关注行业整体股价下跌，而非同行回应披露行为。 | P9b | minimal | needs-citation-link | [[Gleason Jenkins Johnson 2008 Contagion Effects]] |
| E-XDEF-1 | design evidence | manuscript 三[para 3] | 若企业当年披露违规行为且不存在与该违规有关的问询或处罚，作者认定为“主动披露违规”。 | P1a | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-XDEF-2 | design evidence | manuscript 三[para 3] | 违规包括违反《证券法》《上市公司信息披露管理办法》等监管明文禁止事项，如虚构利润、内幕交易、违规担保。 | P1a | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-XDEF-3 | variable evidence | 表1 | `Peerdumy`：行业内存在企业主动披露违规，则该行业为处理组行业，赋值为 1，否则为 0。 | P1a; P1b | minimal | needs-table-visual-qc | [[tables-restored/table-01#表 1 变量定义表]] |
| E-DID-TREAT-1 | design evidence | manuscript 三[para 3] | 若公司样本年度内主动披露符合标准的违规行为，其同行业其他上市公司的 `Peerdumy` 取值为 1。 | P1b | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-DID-POST-1 | design evidence | manuscript 三[para 3] | 若行业内某家公司在 t 年度主动披露违规，`POST` 在 t 年至 t+2 为 1。 | P1b | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-DID-POST-2 | design evidence | manuscript 三[para 3] | `POST` 在 t-3 至 t-1 为 0。 | P1b | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-YDEF-1 | variable evidence | manuscript 三[para 2] | 作者参考 Kim and Verrecchia(2001)、陈运森等(2019)，以交易量对收益率影响系数 KV 度量信息披露质量。 | P3 | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-YDEF-2 | variable evidence | manuscript 三[para 2]; 表1 | KV 越小表明上市公司信息披露质量越高；表1定义 KV 为交易量对收益率的影响系数。 | P3 | minimal | needs-table-visual-qc | [[tables-restored/table-01#表 1 变量定义表]] |
| E-DESC-1 | table statistic | 表2 | KV 样本量 11339，均值 0.1159，标准差 0.1453。 | P3; P6b | minimal | needs-table-visual-qc | [[tables-restored/table-02#表 2 描述性统计结果]] |
| E-DESC-2 | table statistic | 表2 | `Peerdumy` 均值 0.3870；`Peerdumy x POST` 均值 0.1972。 | P4c | minimal | needs-table-visual-qc | [[tables-restored/table-02#表 2 描述性统计结果]] |
| E-SAMPLE-1 | sample evidence | manuscript 三[para 1] | 初始研究样本为 2007-2024 年沪深两市 A 股上市公司。 | P4a | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-SAMPLE-2 | sample evidence | manuscript 三[para 1] | 估计期间为主动披露违规前 3 年、当年、后 2 年的对称窗口。 | P4b | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-SAMPLE-3 | sample evidence | manuscript 三[para 1] | 若行业内存在多家主动披露违规企业且时间间隔过短，则剔除该行业公司样本。 | P1c; P4b | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-SAMPLE-4 | sample evidence | manuscript 三[para 1] | 处理组仅保留行业内第一次满足条件的主动披露违规所对应窗口期样本。 | P1c; P4b | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-SAMPLE-5 | sample evidence | manuscript 三[para 1] | 剔除主动披露违规的公司样本。 | P1c; P4b | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-SAMPLE-6 | sample evidence | manuscript 三[para 1] | 另剔除 ST/*ST、金融保险业、仅在冲击前或冲击后存在的同行业公司、关键变量缺失样本。 | P4b | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-SAMPLE-7 | data evidence | manuscript 三[para 1] | 数据源为 CNRDS、CSMAR 与 WIND。 | P4a | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-SAMPLE-8 | sample evidence | manuscript 三[para 1] | 最终得到 11339 个有效公司-年度观察数据。 | P4c | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-SAMPLE-9 | data-processing evidence | manuscript 三[para 1] | 所有连续变量在 1% 和 99% 分位上 Winsorize 缩尾。 | P4c | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-MODEL-1 | model evidence | manuscript 三[para 5] | 作者构建式(1)：`KV_it = beta0 + beta1 Peerdumy_it x POST_it + controls + theta_i + lambda_t + epsilon_it`。 | P5a | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-MODEL-2 | model evidence | manuscript 三[para 4] | 控制变量包括 SIZE、LEV、ROA、MB、PROFIT、BOARD、INDEP、SOE、DUAL，并另在模型式中包含 CFO。 | P5a | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-MODEL-3 | fixed-effect evidence | manuscript 三[para 5] | 作者加入年份固定效应 `lambda_t` 和公司固定效应 `theta_i`。 | P5a | minimal | verified | [[manuscript_restored_with_tables#三、研究设计]] |
| E-MODEL-4 | cluster evidence | manuscript 三[para 5]; 表3注 | 作者在公司层面对统计标准误进行聚类调整；表注说明括号内为经公司层面聚类调整的标准误。 | P5a | minimal | needs-table-visual-qc | [[tables-restored/table-03#表 3 事前趋势检验结果]] |
| E-MODEL-5 | fixed-effect evidence | 表4 | 表4列(1)(2)均控制年份固定效应和公司固定效应。 | P5a; P6a | minimal | needs-table-visual-qc | [[tables-restored/table-04#表 4 多元回归分析结果]] |
| E-PRETREND-1 | table coefficient | 表3 | `Peerdumy x Pre t-3 = 0.0086`，括号值 `(1.38)`，不显著。 | P5b | minimal | needs-table-visual-qc | [[tables-restored/table-03#表 3 事前趋势检验结果]] |
| E-PRETREND-2 | table coefficient | 表3 | `Peerdumy x Pre t-2 = 0.0029`，括号值 `(0.60)`，不显著。 | P5b | minimal | needs-table-visual-qc | [[tables-restored/table-03#表 3 事前趋势检验结果]] |
| E-PRETREND-3 | table coefficient | 表3 | `Peerdumy x Aft t+1 = -0.0079*`，括号值 `(-1.67)`。 | P5b | minimal | needs-table-visual-qc | [[tables-restored/table-03#表 3 事前趋势检验结果]] |
| E-PRETREND-4 | table coefficient | 表3 | `Peerdumy x Aft t+2 = -0.0175***`，括号值 `(-2.80)`。 | P5b | minimal | needs-table-visual-qc | [[tables-restored/table-03#表 3 事前趋势检验结果]] |
| E-MAIN-1 | table coefficient | 表4列(1) | `Peerdumy x POST = -0.0157***`，括号值 `(-3.92)`。 | P6a | minimal | needs-table-visual-qc | [[tables-restored/table-04#表 4 多元回归分析结果]] |
| E-MAIN-2 | table coefficient | 表4列(2) | `Peerdumy x POST = -0.0111***`，括号值 `(-2.81)`。 | P6a | minimal | needs-table-visual-qc | [[tables-restored/table-04#表 4 多元回归分析结果]] |
| E-MAIN-3 | table statistic | 表4 | 表4列(1)(2)样本量均为 11339，调整 R2 分别为 0.6139 和 0.6271。 | P6a | minimal | needs-table-visual-qc | [[tables-restored/table-04#表 4 多元回归分析结果]] |
| E-MAIN-4 | text evidence | manuscript 四[para 3] | 作者解释：交互项显著为负表明公司主动披露违规之后，同行业企业信息披露质量显著提高。 | P6a | minimal | verified | [[manuscript_restored_with_tables#四、实证结果分析与讨论]] |
| E-MAIN-5 | text/statistic evidence | manuscript 四[para 3] | 作者以列(2)为例，计算 `0.0111 / 0.1159 ≈ 0.0958`，称信息披露质量平均提升 9.58%。 | P6b | minimal | verified | [[manuscript_restored_with_tables#四、实证结果分析与讨论]] |
| E-ROB-STACK-1 | design evidence | manuscript 四[para 4] | 堆叠 DID 以行业内首次主动违规时点为冲击，识别处理组企业和“干净”的控制组企业，并构建队列数据。 | P5c | minimal | verified | [[manuscript_restored_with_tables#四、实证结果分析与讨论]] |
| E-ROB-STACK-2 | table coefficient | 表5列(2) | 堆叠 DID 中 `Peerdumy x POST = -0.0129***`，括号值 `(-3.41)`，样本量 83471，控制队列-年份和队列-公司固定效应。 | P5c | minimal | needs-table-visual-qc | [[tables-restored/table-05#表 5 堆叠 DID 估计]] |
| E-ROB-BACON-1 | figure/text evidence | manuscript 四[para 5] | 图1 Bacon 分解中 `Later Group Treatment vs. Earlier Group Comparison` 权重仅 2.4%。 | P5c | minimal | needs-figure-qc | [[manuscript_restored_with_tables#四、实证结果分析与讨论]] |
| E-ROB-PLACEBO-1 | figure/text evidence | manuscript 四[para 6] | 混合安慰剂检验随机构建伪处理时间和伪处理组行业，重复 500 次。 | P8d | minimal | needs-figure-qc | [[manuscript_restored_with_tables#四、实证结果分析与讨论]] |
| E-ROB-PLACEBO-2 | figure/text evidence | manuscript 四[para 6] | 图2中 500 个回归系数均值大多接近 0；双侧 p=0.0560，左侧 p=0.0240。 | P8d | minimal | needs-figure-qc | [[manuscript_restored_with_tables#四、实证结果分析与讨论]] |
| E-ROB-MATCH-1 | design evidence | manuscript 四[para 7] | PSM 使用处理组企业受冲击前一年样本，以模型(1)控制变量为协变量，1:1 无放回近邻匹配。 | P8a | minimal | verified | [[manuscript_restored_with_tables#四、实证结果分析与讨论]] |
| E-ROB-MATCH-2 | table coefficient | 表6列(1) | PSM 后 `Peerdumy x POST = -0.0116***`，括号值 `(-2.68)`，样本量 8472。 | P8a | minimal | needs-table-visual-qc | [[tables-restored/table-06#表 6 匹配回归的结果]] |
| E-ROB-MATCH-3 | table coefficient | 表6列(2) | 熵平衡后 `Peerdumy x POST = -0.0103**`，括号值 `(-2.31)`，样本量 11339。 | P8a | minimal | needs-table-visual-qc | [[tables-restored/table-06#表 6 匹配回归的结果]] |
| E-ROB-COMMON-1 | design evidence | manuscript 四[para 8] | 作者剔除已受到分行业信息披露指引影响的行业公司样本，以排除共同决定因素。 | P8b | minimal | verified | [[manuscript_restored_with_tables#四、实证结果分析与讨论]] |
| E-ROB-COMMON-2 | table coefficient | 表7 | 排除共同因素后 `Peerdumy x POST = -0.0117**`，括号值 `(-2.50)`，样本量 8953。 | P8b | minimal | needs-table-visual-qc | [[tables-restored/table-07#表 7 排除共同决定因素干扰的检验]] |
| E-ROB-OSTER-1 | table statistic | 表8 | Oster 方法1：`beta* = -0.0035`，位于 `[-0.0218, -0.001]`，表中判断为通过。 | P8c | minimal | needs-table-visual-qc | [[tables-restored/table-08#表 8 Oster 检验结果]] |
| E-ROB-OSTER-2 | table statistic | 表8 | Oster 方法2：`delta = 1.4633 > 1`，表中判断为通过。 | P8c | minimal | needs-table-visual-qc | [[tables-restored/table-08#表 8 Oster 检验结果]] |
| E-ROB-ALT-1 | table coefficient | 表9列(1) | 替换被解释变量 DA 后 `Peerdumy x POST = -0.0044*`，括号值 `(-1.65)`，样本量 11125。 | P8c | minimal | needs-table-visual-qc | [[tables-restored/table-09#表 9 替换变量衡量方式的检验]] |
| E-ROB-ALT-2 | design evidence | manuscript 四[para 10] | 作者将 7-12 月主动披露违规事项认定为 t+1 年发挥作用，1-6 月认定为 t 年发挥作用，重构 `POST_Month`。 | P8c | minimal | verified | [[manuscript_restored_with_tables#四、实证结果分析与讨论]] |
| E-ROB-ALT-3 | table coefficient | 表9列(2) | `Peerdumy x POST_Month = -0.0117***`，括号值 `(-3.55)`，样本量 14296。 | P8c | minimal | needs-table-visual-qc | [[tables-restored/table-09#表 9 替换变量衡量方式的检验]] |
| E-THEORY-SIGNAL-1 | text evidence | manuscript 二[para 1] | 作者称主动披露违规向市场展示诚实守信、敢于负责的治理态度，并可能缓解投资者对道德风险的担忧。 | P2a | minimal | verified | [[manuscript_restored_with_tables#二、理论分析]] |
| E-CIT-SIGNAL-1 | citation evidence | manuscript 二[para 1] | Connelly et al.(2011)被作者用于支持信号传递理论。 | P2a | minimal | needs-citation-link | needs-literature-note |
| E-CIT-SIGNAL-2 | citation evidence | manuscript 一[para 2] | Leuz and Verrecchia(2000)、Healy and Palepu(2001)被作者用于说明企业可能因收益大于披露成本而主动披露负面信息。 | P2a | minimal | needs-citation-link | needs-literature-note |
| E-THEORY-REP-1 | text evidence | manuscript 二[para 2] | 作者称同行业企业在资本市场上存在声誉竞争；事件公司获得诚信溢价或分析师正向关注时，同行有动力改善披露。 | P2b | minimal | verified | [[manuscript_restored_with_tables#二、理论分析]] |
| E-CIT-REP-1 | citation evidence | manuscript 一[para 5] | Beyer et al.(2010)、Beyer and Dye(2012)被作者用于定位声誉约束对披露行为的影响。 | P2b | minimal | needs-citation-link | needs-literature-note |
| E-CIT-REP-2 | citation evidence | manuscript 六[para 1] | Adhikari and Agrawal(2018)、陆蓉等(2017)、吴娜等(2022)被作者用于支持按行业领先地位刻画同群影响。 | P2b; P8e | minimal | needs-citation-link | needs-literature-note |
| E-THEORY-PRESS-1 | text evidence | manuscript 二[para 3] | 作者称主动披露违规会引发证券分析师、审计师及媒体对行业整体合规风险的警觉，提高外部关注和监督压力。 | P2c | minimal | verified | [[manuscript_restored_with_tables#二、理论分析]] |
| E-CIT-PRESS-1 | citation evidence | manuscript 五[para 5] | 刘柏和琚涛(2021)被作者用于支持用互动平台提问数和分析师人数度量外部关注。 | P2c; P7b | minimal | needs-citation-link | needs-literature-note |
| E-CIT-PRESS-2 | citation evidence | manuscript 一[para 2] | Wang et al.(2010)、Matsumura et al.(2014)被作者用于说明负面信息披露可能带来投资者信任、融资便利或更高市场价值。 | P2c | minimal | needs-citation-link | needs-literature-note |
| E-MECH-CAR-1 | design evidence | manuscript 五[para 1] | 事件研究以每个事件公司首次主动披露违规日为事件日，估计窗口为事件日前 140 至 21 个交易日。 | P7a | minimal | verified | [[manuscript_restored_with_tables#五、机制检验]] |
| E-MECH-CAR-2 | table statistic | 表10 | CAR[-5,5] = 0.0182***，Patell Z=2.6041。 | P7a | minimal | needs-table-visual-qc | [[tables-restored/table-10#表 10 事件公司主动披露违规的短期市场反应]] |
| E-MECH-CAR-3 | table statistic | 表10 | CAR[-10,10] = 0.0342***，Patell Z=3.4036；CAR[-1,1] = 0.0063，Patell Z=1.3450。 | P7a | minimal | needs-table-visual-qc | [[tables-restored/table-10#表 10 事件公司主动披露违规的短期市场反应]] |
| E-MECH-REP-1 | table coefficient | 表11列(1) | `Peerdumy_PosCAR[-1,1] x POST = -0.0174***`，括号值 `(-3.14)`；`Peerdumy_NegCAR[-1,1] x POST = -0.0057`，括号值 `(-1.21)`。 | P7a | minimal | needs-table-visual-qc | [[tables-restored/table-11#表 11 基于声誉竞争机制的检验结果]] |
| E-MECH-REP-2 | table coefficient | 表11列(2) | `Peerdumy_PosCAR[-5,5] x POST = -0.0204***`，括号值 `(-3.79)`；`Peerdumy_NegCAR[-5,5] x POST = -0.0016`，括号值 `(-0.34)`。 | P7a | minimal | needs-table-visual-qc | [[tables-restored/table-11#表 11 基于声誉竞争机制的检验结果]] |
| E-MECH-REP-3 | table coefficient / conflict | 表11列(3) | 表格显示 `Peerdumy_PosCAR[-10,10] x POST = -0.0028`，括号值 `(-0.57)`；`Peerdumy_NegCAR[-10,10] x POST = -0.0168***`，括号值 `(-3.33)`，与正文“三组 PosCAR 显著、NegCAR 不显著”叙述冲突。 | P7a | minimal | needs-table-visual-qc | [[tables-restored/table-11#表 11 基于声誉竞争机制的检验结果]] |
| E-MECH-PRESS-1 | design evidence | manuscript 五[para 5] | 投资者关注用“上证 e 互动”和“互动易”提问数之和衡量。 | P7b | minimal | verified | [[manuscript_restored_with_tables#五、机制检验]] |
| E-MECH-PRESS-2 | design evidence | manuscript 五[para 5] | 分析师关注用跟踪企业的分析师人数衡量，并按事前一年是否高于行业中位数分组。 | P7b | minimal | verified | [[manuscript_restored_with_tables#五、机制检验]] |
| E-MECH-PRESS-3 | table coefficient | 表12列(1) | `Peerdumy_HighInv x POST = -0.0146**`，括号值 `(-2.54)`；`Peerdumy_LowInv x POST = -0.0014`，括号值 `(-0.24)`。 | P7b | minimal | needs-table-visual-qc | [[tables-restored/table-12#表 12 基于市场压力机制的检验结果]] |
| E-MECH-PRESS-4 | table coefficient | 表12列(2) | `Peerdumy_HighAna x POST = -0.0259***`，括号值 `(-4.63)`；`Peerdumy_LowAnaPOST = -0.0009`，括号值 `(-0.20)`。 | P7b | minimal | needs-table-visual-qc | [[tables-restored/table-12#表 12 基于市场压力机制的检验结果]] |
| E-MECH-PRESS-5 | table statistic | 表12 | 组内系数差异 p 值：投资者关注列 0.0608，分析师关注列 0.0001。 | P7b | minimal | needs-table-visual-qc | [[tables-restored/table-12#表 12 基于市场压力机制的检验结果]] |
| E-MECH-INFO-1 | design evidence | manuscript 五[para 6] | 作者以企业与证监局地理距离衡量监管距离，推断高监管距离企业更可能受信息传导影响。 | P7c | minimal | verified | [[manuscript_restored_with_tables#五、机制检验]] |
| E-MECH-INFO-2 | table coefficient | 表13列(1) | `Peerdum_LowDistance x POST = -0.0110**`，括号值 `(-2.13)`；`Peerdum_HighDistance x POST = -0.0133***`，括号值 `(-2.62)`；组内差异 p=0.7192。 | P7c | minimal | needs-table-visual-qc | [[tables-restored/table-13#表 13 基于信息传导机制的检验结果]] |
| E-MECH-INFO-3 | table coefficient | 表13列(2) | 被处罚次数模型中 `Peerdumy x POST = -0.2028`，括号值 `(-0.64)`，不显著。 | P7c | minimal | needs-table-visual-qc | [[tables-restored/table-13#表 13 基于信息传导机制的检验结果]] |
| E-MECH-INFO-4 | table coefficient | 表13列(3) | 处罚严重程度模型中 `Peerdumy x POST = -0.0035`，括号值 `(-0.15)`，不显著。 | P7c | minimal | needs-table-visual-qc | [[tables-restored/table-13#表 13 基于信息传导机制的检验结果]] |
| E-HET-LEADER-1 | design evidence | manuscript 六[para 1] | 行业领先企业按总资产、营业收入、企业年龄是否位于行业前 30% 定义。 | P8e | minimal | verified | [[manuscript_restored_with_tables#六、进一步分析]] |
| E-HET-LEADER-2 | table coefficient | 表14列(1) | `Peerdumy_Leader1 x POST = -0.0230***`，括号值 `(-3.58)`；`NoLeader1 = -0.0060`，括号值 `(-1.37)`；差异 p=0.0150。 | P8e | minimal | needs-table-visual-qc | [[tables-restored/table-14#表 14 基于事件公司行业地位的检验结果]] |
| E-HET-LEADER-3 | table coefficient | 表14列(2) | `Peerdumy_Leader2 x POST = -0.0256***`，括号值 `(-3.90)`；`NoLeader2 = -0.0038`，括号值 `(-0.90)`；差异 p=0.0022。 | P8e | minimal | needs-table-visual-qc | [[tables-restored/table-14#表 14 基于事件公司行业地位的检验结果]] |
| E-HET-LEADER-4 | table coefficient | 表14列(3) | `Peerdumy_Leader3 x POST = -0.0175***`，括号值 `(-2.85)`；`NoLeader3 = -0.0073`，括号值 `(-1.64)`；差异 p=0.1325。 | P8e | minimal | needs-table-visual-qc | [[tables-restored/table-14#表 14 基于事件公司行业地位的检验结果]] |
| E-HET-OWN-1 | design evidence | manuscript 六[para 2-3] | 自涉违规指违规事项与控股股东、实际控制人、董事长、总经理或持股超过 5% 大股东有关。 | P8f | minimal | verified | [[manuscript_restored_with_tables#六、进一步分析]] |
| E-HET-OWN-2 | table coefficient | 表15 | `Peerdumy_Own x POST = -0.0183***`，括号值 `(-3.16)`；`Peerdumy_Other x POST = -0.0054`，括号值 `(-1.17)`；差异 p=0.0558。 | P8f | minimal | needs-table-visual-qc | [[tables-restored/table-15#表 15 基于事件公司披露违规主动性的检验结果]] |
| E-HET-MON-1 | design evidence | manuscript 六[para 5] | 事件企业主动披露违规公告中的违规事项所涉金额是否大于中位数用于划分高/低严重程度。 | P8f | minimal | verified | [[manuscript_restored_with_tables#六、进一步分析]] |
| E-HET-MON-2 | table coefficient | 表16 | `Peerdumy_HighMon x POST = -0.0119**`，括号值 `(-2.14)`；`Peerdumy_LowMon x POST = -0.0113**`，括号值 `(-2.27)`。 | P8f | minimal | needs-table-visual-qc | [[tables-restored/table-16#表 16 基于事件公司违规严重程度的检验结果]] |
| E-HET-MON-3 | table note/statistic | 表16 | 表16样本量 10935；表注称部分违规事项无法识别所涉金额，所以回归样本减少；组内差异 p=0.9322。 | P8f | minimal | needs-table-visual-qc | [[tables-restored/table-16#表 16 基于事件公司违规严重程度的检验结果]] |
| E-HET-RELY-1 | design evidence | manuscript 六[para 7] | 外部融资依赖度按 Rajan and Zingales(1998)思路，用 `(资本支出 - 经营性现金流量净额) / 资本支出` 度量，并构造 Rely1、Rely2。 | P8g | minimal | verified | [[manuscript_restored_with_tables#六、进一步分析]] |
| E-HET-RELY-2 | table coefficient | 表17列(1) | `Peerdumy_HighRely1 x POST = -0.0174***`，括号值 `(-3.22)`；`LowRely1 = -0.0073`，括号值 `(-1.50)`；差异 p=0.1216。 | P8g | minimal | needs-table-visual-qc | [[tables-restored/table-17#表 17 基于公司外部融资依赖度的检验结果]] |
| E-HET-RELY-3 | table coefficient | 表17列(2) | `Peerdumy_HighRely2 x POST = -0.0190***`，括号值 `(-3.50)`；`LowRely2 = -0.0057`，括号值 `(-1.20)`；差异 p=0.0424。 | P8g | minimal | needs-table-visual-qc | [[tables-restored/table-17#表 17 基于公司外部融资依赖度的检验结果]] |
| E-CIT-RELY-1 | citation evidence | manuscript 六[para 6-7] | 李志军和王善平(2011)、任宏达和王琨(2019)、Rajan and Zingales(1998)、姜付秀等(2017)、沈红波等(2018)被作者用于支撑外部融资依赖分组逻辑和指标构造。 | P8g | minimal | needs-citation-link | needs-literature-note |
| E-HET-COM-1 | design evidence | manuscript 六[para 9] | 行业竞争程度用处理组行业上一年度营业收入和总资产计算的赫芬达尔指数反向代理，并按中位数划分高/低竞争组。 | P8h | minimal | verified | [[manuscript_restored_with_tables#六、进一步分析]] |
| E-HET-COM-2 | table coefficient | 表18列(1) | `Peerdumy_HighCom1 x POST = -0.0224***`，括号值 `(-4.80)`；`LowCom1 = 0.0128**`，括号值 `(2.30)`；差异 p=0.0000。 | P8h | minimal | needs-table-visual-qc | [[tables-restored/table-18#表 18 基于行业竞争程度的检验结果]] |
| E-HET-COM-3 | table coefficient | 表18列(2) | `Peerdumy_HighCom2 x POST = -0.0237***`，括号值 `(-5.01)`；`LowCom2 = 0.0124**`，括号值 `(2.30)`；差异 p=0.0000。 | P8h | minimal | needs-table-visual-qc | [[tables-restored/table-18#表 18 基于行业竞争程度的检验结果]] |
| E-CIT-COM-1 | citation evidence | manuscript 六[para 8] | Allee et al.(2021)、Hsu et al.(2023)被作者用于支持竞争激烈行业中企业更易受市场舆论和投资者比较影响。 | P8h | minimal | needs-citation-link | needs-literature-note |
| E-CIT-COM-2 | citation evidence | manuscript 六[para 8-9] | Ali et al.(2014)、王红建等(2016)、彭俞超等(2018)被作者用于支持低竞争行业披露逻辑和 HHI 竞争指标构造。 | P8h | minimal | needs-citation-link | needs-literature-note |
| E-CONTR-1 | text evidence | manuscript 一[para 5] | 作者称本文将主动披露违规与企业违规两类公司治理行为纳入同一框架，丰富企业信息披露决策情景。 | P9a | minimal | verified | [[manuscript_restored_with_tables#一、引言]] |
| E-CONTR-2 | text evidence | manuscript 一[para 6] | 作者称本文把主动披露违规由企业个体治理问题引申至行业信息披露决策问题。 | P9b | minimal | verified | [[manuscript_restored_with_tables#一、引言]] |
| E-POLICY-1 | text evidence | manuscript 七[para 3] | 作者建议监管部门设立“主动披露豁免”或“减轻处罚”机制，鼓励企业在违规被监管发现前主动披露。 | P9c | minimal | verified | [[manuscript_restored_with_tables#七、结论与启示]] |
| E-POLICY-2 | text evidence | manuscript 七[para 4] | 作者建议继续支持分析师、媒体和投资者通过互动平台等渠道监督上市公司。 | P9c | minimal | verified | [[manuscript_restored_with_tables#七、结论与启示]] |
| E-POLICY-3 | text evidence | manuscript 七[para 5] | 作者建议重点关注行业领先企业及融资需求大、竞争激烈行业的信息披露行为，并甄别策略性披露。 | P9c | minimal | verified | [[manuscript_restored_with_tables#七、结论与启示]] |
