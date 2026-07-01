# Canonical Node Ledger

| node_id | label | type | depth | parent_id | child_ids | evidence_ids | source_links | status |
|---|---|---:|---:|---|---|---|---|---|
| Y0 | 本文关于主动披露违规引导行业自律和改善信息披露质量的论文贡献成立 | root-claim | 0 |  | X1; X2; P9 |  | manuscript para 一-4; 七-1 to 七-5 | complete |
| X1 | 研究问题有意义且存在文献缺口 | major-claim | 1 | Y0 | G1; G2; G3; G4 |  | manuscript 一-1 to 一-7 | complete |
| G1 | 信息披露质量与监管转向使主动披露违规成为重要现实问题 | middle-claim | 2 | X1 |  | E-X1-POL-1; E-X1-POL-2; E-X1-EX-1 | manuscript 一-1; 一-2 | complete |
| G2 | 主动披露违规对同行披露行为的方向具有理论不确定性 | middle-claim | 2 | X1 |  | E-X1-MECH-1; E-X1-MECH-2; E-X1-MECH-3 | manuscript 一-2; 二-1 to 二-5 | complete |
| G3 | 既有信息披露质量研究未直接回答主动披露违规的同行溢出问题 | middle-claim | 2 | X1 |  | E-CIT-GAP-1; E-CIT-GAP-2; E-CIT-GAP-3; E-CIT-GAP-4 | manuscript 一-3; 参考文献 | complete |
| G4 | 本文提出可贡献于信息披露影响因素、负面信息披露和同行溢出研究 | middle-claim | 2 | X1 |  | E-X1-CONTR-1; E-CIT-CONTR-1; E-CIT-CONTR-2 | manuscript 一-5; 一-6 | complete |
| X2 | 作者声称企业主动披露违规改善同行业其他企业的信息披露质量，并主要通过声誉竞争和市场压力引导行业自律 | major-claim | 1 | Y0 | P1; P2; P3; P4; P5; P6; P7; P8 |  | manuscript 一-4; 四-三; 五; 六 | complete |
| P1 | 处理变量和冲击被定义为行业内企业主动披露违规及事后窗口 | middle-claim | 2 | X2 | P1a; P1b; P1c |  | manuscript 三-二-2; 表1 | complete |
| P1a | 主动披露违规事件具有可操作定义 | subclaim | 3 | P1 |  | E-XDEF-1; E-XDEF-2; E-XDEF-3 | manuscript 三-二-2 | complete |
| P1b | 处理组和事后窗口被编码为 `Peerdumy` 与 `POST` | subclaim | 3 | P1 |  | E-DID-TREAT-1; E-DID-POST-1; E-DID-POST-2 | 表1; manuscript 三-二-2 | complete |
| P1c | 作者排除事件公司本身并用同行企业承载溢出效应 | subclaim | 3 | P1 |  | E-SAMPLE-3; E-SAMPLE-4; E-SAMPLE-5 | manuscript 三-一 | complete |
| P2 | 理论机制说明 X 可能通过声誉竞争和市场压力影响 Y | middle-claim | 2 | X2 | P2a; P2b; P2c |  | manuscript 二-1 to 二-6 | complete |
| P2a | 主动披露违规可被市场解读为诚信/合规信号 | subclaim | 3 | P2 |  | E-THEORY-SIGNAL-1; E-CIT-SIGNAL-1; E-CIT-SIGNAL-2 | manuscript 二-1; 一-2 | complete |
| P2b | 同行业企业面对声誉竞争会改善信息披露质量 | subclaim | 3 | P2 |  | E-THEORY-REP-1; E-CIT-REP-1; E-CIT-REP-2 | manuscript 二-2; 五-一 | complete |
| P2c | 市场关注和外部监督压力会促使同行企业提升披露 | subclaim | 3 | P2 |  | E-THEORY-PRESS-1; E-CIT-PRESS-1; E-CIT-PRESS-2 | manuscript 二-3; 五-二 | complete |
| P3 | 被解释变量 KV 可操作化信息披露质量，且方向为 KV 越小披露质量越高 | middle-claim | 2 | X2 |  | E-YDEF-1; E-YDEF-2; E-DESC-1 | manuscript 三-二-1; 表1; 表2 | complete |
| P4 | 样本与数据结构适配 DID 风格的同行溢出检验 | middle-claim | 2 | X2 | P4a; P4b; P4c |  | manuscript 三-一 | complete |
| P4a | 样本期和数据源明确 | subclaim | 3 | P4 |  | E-SAMPLE-1; E-SAMPLE-7 | manuscript 三-一 | complete |
| P4b | 事件窗口和事件混淆筛选规则明确 | subclaim | 3 | P4 |  | E-SAMPLE-2; E-SAMPLE-3; E-SAMPLE-4; E-SAMPLE-5; E-SAMPLE-6 | manuscript 三-一 | complete |
| P4c | 最终样本量和缩尾处理明确 | subclaim | 3 | P4 |  | E-SAMPLE-8; E-SAMPLE-9; E-DESC-2 | manuscript 三-一; 表2 | complete |
| P5 | DID 识别设计被作者声称能够估计主动披露违规对同行 KV 的影响 | middle-claim | 2 | X2 | P5a; P5b; P5c |  | manuscript 三-三; 四-二 | complete |
| P5a | 基准回归模型、控制变量、固定效应和聚类层级被设定 | subclaim | 3 | P5 |  | E-MODEL-1; E-MODEL-2; E-MODEL-3; E-MODEL-4; E-MODEL-5 | manuscript 三-二-3; 三-三; 表3注 | complete |
| P5b | 事前趋势检验被作者用于支撑 DID 前提 | subclaim | 3 | P5 |  | E-PRETREND-1; E-PRETREND-2; E-PRETREND-3; E-PRETREND-4 | manuscript 四-二; 表3 | complete |
| P5c | 堆叠 DID 和 Bacon 分解被作者用于回应异质性处理效应 | subclaim | 3 | P5 |  | E-ROB-STACK-1; E-ROB-STACK-2; E-ROB-BACON-1 | manuscript 四-四-1; 四-四-2; 表5 | complete |
| P6 | 主结果显示主动披露违规后同行信息披露质量显著提升 | middle-claim | 2 | X2 | P6a; P6b |  | manuscript 四-三; 表4 | complete |
| P6a | 基准 DID 核心交互项为负且显著 | subclaim | 3 | P6 |  | E-MAIN-1; E-MAIN-2; E-MAIN-3; E-MAIN-4 | 表4; manuscript 四-三 | complete |
| P6b | 作者给出经济意义：列(2)系数对应 KV 均值约 9.58% | subclaim | 3 | P6 |  | E-MAIN-5; E-DESC-1 | manuscript 四-三; 表2 | complete |
| P7 | 机制证据支持声誉竞争和市场压力，且不支持监管信息传导为主要机制 | middle-claim | 2 | X2 | P7a; P7b; P7c |  | manuscript 五 | complete |
| P7a | 声誉竞争机制：事件公司获得市场积极反馈时，同行更改善披露 | subclaim | 3 | P7 |  | E-MECH-CAR-1; E-MECH-CAR-2; E-MECH-CAR-3; E-MECH-REP-1; E-MECH-REP-2; E-MECH-REP-3 | 表10; 表11; manuscript 五-一 | needs-table-visual-qc |
| P7b | 市场压力机制：高投资者关注和高分析师关注组效应更强 | subclaim | 3 | P7 |  | E-MECH-PRESS-1; E-MECH-PRESS-2; E-MECH-PRESS-3; E-MECH-PRESS-4; E-MECH-PRESS-5 | 表12; manuscript 五-二 | complete |
| P7c | 信息传导机制不是主要机制 | subclaim | 3 | P7 |  | E-MECH-INFO-1; E-MECH-INFO-2; E-MECH-INFO-3; E-MECH-INFO-4 | 表13; manuscript 五-三 | complete |
| P8 | 稳健性、进一步分析与边界条件支持核心发现的范围 | middle-claim | 2 | X2 | P8a; P8b; P8c; P8d; P8e; P8f; P8g; P8h |  | manuscript 四-四; 六 | complete |
| P8a | 匹配和熵平衡后结论仍成立 | subclaim | 3 | P8 |  | E-ROB-MATCH-1; E-ROB-MATCH-2; E-ROB-MATCH-3 | 表6 | complete |
| P8b | 排除分行业信息披露指引共同因素后结论仍成立 | subclaim | 3 | P8 |  | E-ROB-COMMON-1; E-ROB-COMMON-2 | manuscript 四-四-5; 表7 | complete |
| P8c | Oster 检验和替代变量/时间编码支持结果稳健 | subclaim | 3 | P8 |  | E-ROB-OSTER-1; E-ROB-OSTER-2; E-ROB-ALT-1; E-ROB-ALT-2; E-ROB-ALT-3 | 表8; 表9 | complete |
| P8d | 安慰剂检验被作者用于排除随机伪处理和遗漏政策影响 | subclaim | 3 | P8 |  | E-ROB-PLACEBO-1; E-ROB-PLACEBO-2 | manuscript 四-四-3 | needs-figure-qc |
| P8e | 行业领先事件公司冲击更强 | subclaim | 3 | P8 |  | E-HET-LEADER-1; E-HET-LEADER-2; E-HET-LEADER-3; E-HET-LEADER-4 | 表14; manuscript 六-一-1 | complete |
| P8f | 自涉违规更能触发同行披露改善，违规严重程度高低均有效 | subclaim | 3 | P8 |  | E-HET-OWN-1; E-HET-OWN-2; E-HET-MON-1; E-HET-MON-2; E-HET-MON-3 | 表15; 表16 | complete |
| P8g | 高外部融资依赖企业效应更强 | subclaim | 3 | P8 |  | E-HET-RELY-1; E-HET-RELY-2; E-HET-RELY-3; E-CIT-RELY-1 | 表17; manuscript 六-二 | complete |
| P8h | 高行业竞争行业效应更强，低竞争行业出现相反方向 | subclaim | 3 | P8 |  | E-HET-COM-1; E-HET-COM-2; E-HET-COM-3; E-CIT-COM-1; E-CIT-COM-2 | 表18; manuscript 六-三 | complete |
| P9 | 作者将发现上升为文献贡献和政策启示 | major-claim | 1 | Y0 | P9a; P9b; P9c |  | manuscript 一-5 to 一-7; 七-3 to 七-5 | complete |
| P9a | 贡献于信息披露影响因素研究 | subclaim | 2 | P9 |  | E-CONTR-1; E-CIT-CONTR-1 | manuscript 一-5 | complete |
| P9b | 贡献于负面信息披露和同行溢出研究 | subclaim | 2 | P9 |  | E-CONTR-2; E-CIT-CONTR-2; E-CIT-CONTR-3 | manuscript 一-6 | complete |
| P9c | 政策启示是鼓励主动披露、强化市场监督并差异化监管 | subclaim | 2 | P9 |  | E-POLICY-1; E-POLICY-2; E-POLICY-3 | manuscript 七-3 to 七-5 | complete |
