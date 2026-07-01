# Recursive Tree Master

This is the canonical recursive evidence tree in text form. Mermaid is a derived view.

```text
Y0 本文关于主动披露违规引导行业自律和改善信息披露质量的论文贡献成立
├─ X1 研究问题有意义且存在文献缺口
│  ├─ G1 信息披露监管转向与主动披露违规现实案例使问题重要
│  │  ├─ E-X1-POL-1 2019 年证券法修订扩充信息披露责任并提高违规处罚
│  │  ├─ E-X1-POL-2 2025 年上市公司信息披露管理办法强调事前预防
│  │  └─ E-X1-EX-1 天虹股份主动披露股东违规减持案例
│  ├─ G2 主动披露违规对同行披露行为方向不确定
│  │  ├─ E-X1-MECH-1 主动披露可能传递诚信经营信号或降低未来损失
│  │  ├─ E-X1-MECH-2 违规曝光可能带来股价下跌、融资受限和风险披露减少
│  │  └─ E-X1-MECH-3 主动披露可能揭示行业共有违规手段并引发同行担忧
│  ├─ G3 既有文献未直接回答主动披露违规的同行披露质量效应
│  │  ├─ E-CIT-GAP-1 监管/监督视角的信息披露质量研究
│  │  ├─ E-CIT-GAP-2 Dye(1990)、Gleason et al.(2008)用于说明披露同行影响
│  │  ├─ E-CIT-GAP-3 环境、创新、ESG 等特定披露同群研究
│  │  └─ E-CIT-GAP-4 Seo(2021)用于说明披露数量而非质量研究
│  └─ G4 本文可贡献于信息披露影响因素、负面信息披露和同行溢出研究
│     ├─ E-X1-CONTR-1 作者明示尚未有研究关注主动披露违规对同行披露决策的影响
│     ├─ E-CIT-CONTR-1 信息披露影响因素定位文献
│     └─ E-CIT-CONTR-2 负面信息披露定位文献
├─ X2 作者声称企业主动披露违规改善同行业其他企业的信息披露质量，并主要通过声誉竞争和市场压力引导行业自律
│  ├─ P1 处理变量和冲击被定义为行业内企业主动披露违规及事后窗口
│  │  ├─ P1a 主动披露违规事件具有可操作定义
│  │  │  ├─ E-XDEF-1 披露违规且无相关问询或处罚即认定为主动披露违规
│  │  │  ├─ E-XDEF-2 违规事项包括虚构利润、内幕交易、违规担保等
│  │  │  └─ E-XDEF-3 表1定义 Peerdumy
│  │  ├─ P1b 处理组和事后窗口被编码为 Peerdumy 与 POST
│  │  │  ├─ E-DID-TREAT-1 同行业其他上市公司 Peerdumy 取 1
│  │  │  ├─ E-DID-POST-1 POST 在 t 至 t+2 为 1
│  │  │  └─ E-DID-POST-2 POST 在 t-3 至 t-1 为 0
│  │  └─ P1c 作者排除事件公司本身并用同行企业承载溢出效应
│  │     ├─ E-SAMPLE-3 多事件间隔过短则剔除行业样本
│  │     ├─ E-SAMPLE-4 仅保留行业内首次满足条件事件窗口
│  │     └─ E-SAMPLE-5 剔除主动披露违规公司样本
│  ├─ P2 理论机制说明 X 可能通过声誉竞争和市场压力影响 Y
│  │  ├─ P2a 主动披露违规可被市场解读为诚信/合规信号
│  │  │  ├─ E-THEORY-SIGNAL-1 主动披露展示诚实守信、敢于负责的治理态度
│  │  │  ├─ E-CIT-SIGNAL-1 Connelly et al.(2011)支撑信号传递理论
│  │  │  └─ E-CIT-SIGNAL-2 Leuz and Verrecchia(2000)、Healy and Palepu(2001)支撑披露成本收益逻辑
│  │  ├─ P2b 同行业企业面对声誉竞争会改善披露质量
│  │  │  ├─ E-THEORY-REP-1 诚信溢价或分析师关注促使同行改善披露
│  │  │  ├─ E-CIT-REP-1 Beyer et al.(2010)、Beyer and Dye(2012)定位声誉约束
│  │  │  └─ E-CIT-REP-2 行业领先地位和同群影响文献
│  │  └─ P2c 市场关注和外部监督压力促使同行提升披露
│  │     ├─ E-THEORY-PRESS-1 分析师、审计师、媒体提高行业合规风险关注
│  │     ├─ E-CIT-PRESS-1 刘柏和琚涛(2021)支撑关注度指标
│  │     └─ E-CIT-PRESS-2 Wang et al.、Matsumura et al.支撑负面披露潜在市场收益
│  ├─ P3 KV 可操作化信息披露质量，且 KV 越小披露质量越高
│  │  ├─ E-YDEF-1 KV 为交易量对收益率的影响系数
│  │  ├─ E-YDEF-2 KV 越小代表披露质量越高
│  │  └─ E-DESC-1 表2 KV 样本量 11339，均值 0.1159
│  ├─ P4 样本与数据结构适配 DID 风格同行溢出检验
│  │  ├─ P4a 样本期和数据源明确
│  │  │  ├─ E-SAMPLE-1 2007-2024 年沪深 A 股
│  │  │  └─ E-SAMPLE-7 数据源 CNRDS、CSMAR、WIND
│  │  ├─ P4b 事件窗口和事件混淆筛选规则明确
│  │  │  ├─ E-SAMPLE-2 前3年、当年、后2年窗口
│  │  │  ├─ E-SAMPLE-3 多事件间隔过短剔除
│  │  │  ├─ E-SAMPLE-4 保留首次事件窗口
│  │  │  ├─ E-SAMPLE-5 剔除事件公司
│  │  │  └─ E-SAMPLE-6 剔除 ST、金融业、单边存在样本和关键变量缺失样本
│  │  └─ P4c 最终样本量和缩尾处理明确
│  │     ├─ E-SAMPLE-8 最终 11339 个公司-年度观察
│  │     ├─ E-SAMPLE-9 连续变量 1%/99% 缩尾
│  │     └─ E-DESC-2 表2 Peerdumy 和 Peerdumy x POST 描述统计
│  ├─ P5 DID 识别设计被作者声称能够估计主动披露违规对同行 KV 的影响
│  │  ├─ P5a 基准模型、控制变量、固定效应和聚类层级被设定
│  │  │  ├─ E-MODEL-1 式(1) DID 回归模型
│  │  │  ├─ E-MODEL-2 控制变量组
│  │  │  ├─ E-MODEL-3 年份固定效应和公司固定效应
│  │  │  ├─ E-MODEL-4 公司层面聚类标准误
│  │  │  └─ E-MODEL-5 表4控制年份和公司固定效应
│  │  ├─ P5b 事前趋势检验被作者用于支撑 DID 前提
│  │  │  ├─ E-PRETREND-1 Pre t-3 = 0.0086, (1.38)
│  │  │  ├─ E-PRETREND-2 Pre t-2 = 0.0029, (0.60)
│  │  │  ├─ E-PRETREND-3 Aft t+1 = -0.0079*, (-1.67)
│  │  │  └─ E-PRETREND-4 Aft t+2 = -0.0175***, (-2.80)
│  │  └─ P5c 堆叠 DID 和 Bacon 分解回应异质性处理效应
│  │     ├─ E-ROB-STACK-1 构建独立事件队列和干净控制组
│  │     ├─ E-ROB-STACK-2 表5列(2) Peerdumy x POST = -0.0129***
│  │     └─ E-ROB-BACON-1 Bacon later-vs-earlier 权重 2.4%
│  ├─ P6 主结果显示主动披露违规后同行信息披露质量显著提升
│  │  ├─ P6a 基准 DID 核心交互项为负且显著
│  │  │  ├─ E-MAIN-1 表4列(1) Peerdumy x POST = -0.0157***
│  │  │  ├─ E-MAIN-2 表4列(2) Peerdumy x POST = -0.0111***
│  │  │  ├─ E-MAIN-3 表4样本量 11339，调整 R2 0.6139/0.6271
│  │  │  └─ E-MAIN-4 作者解释显著为负表示同行披露质量提高
│  │  └─ P6b 作者给出经济意义
│  │     ├─ E-MAIN-5 0.0111/0.1159 ≈ 9.58%
│  │     └─ E-DESC-1 表2 KV 均值 0.1159
│  ├─ P7 机制证据支持声誉竞争和市场压力，且不支持监管信息传导为主要机制
│  │  ├─ P7a 声誉竞争机制
│  │  │  ├─ E-MECH-CAR-1 事件研究设计：事件日前 140 至 21 个交易日估计窗口
│  │  │  ├─ E-MECH-CAR-2 表10 CAR[-5,5] = 0.0182***
│  │  │  ├─ E-MECH-CAR-3 表10 CAR[-10,10] = 0.0342***
│  │  │  ├─ E-MECH-REP-1 表11 PosCAR[-1,1] 显著、NegCAR[-1,1] 不显著
│  │  │  ├─ E-MECH-REP-2 表11 PosCAR[-5,5] 显著、NegCAR[-5,5] 不显著
│  │  │  └─ E-MECH-REP-3 表11列(3) PosCAR[-10,10] 不显著、NegCAR[-10,10] 显著且与正文冲突
│  │  ├─ P7b 市场压力机制
│  │  │  ├─ E-MECH-PRESS-1 投资者关注用互动平台提问数
│  │  │  ├─ E-MECH-PRESS-2 分析师关注用跟踪分析师人数
│  │  │  ├─ E-MECH-PRESS-3 表12 HighInv 显著、LowInv 不显著
│  │  │  ├─ E-MECH-PRESS-4 表12 HighAna 显著、LowAna 不显著
│  │  │  └─ E-MECH-PRESS-5 组间差异 p=0.0608/0.0001
│  │  └─ P7c 信息传导机制不是主要机制
│  │     ├─ E-MECH-INFO-1 用监管距离分组检验信息传导
│  │     ├─ E-MECH-INFO-2 高低监管距离组均显著且差异 p=0.7192
│  │     ├─ E-MECH-INFO-3 对被处罚次数不显著
│  │     └─ E-MECH-INFO-4 对处罚严重程度不显著
│  └─ P8 稳健性、进一步分析与边界条件支持核心发现范围
│     ├─ P8a PSM/熵平衡后结论仍成立: E-ROB-MATCH-1, E-ROB-MATCH-2, E-ROB-MATCH-3
│     ├─ P8b 排除分行业信息披露指引共同因素后仍成立: E-ROB-COMMON-1, E-ROB-COMMON-2
│     ├─ P8c Oster、DA、POST_Month 支持稳健性: E-ROB-OSTER-1, E-ROB-OSTER-2, E-ROB-ALT-1, E-ROB-ALT-2, E-ROB-ALT-3
│     ├─ P8d 安慰剂检验: E-ROB-PLACEBO-1, E-ROB-PLACEBO-2
│     ├─ P8e 行业领先事件公司效应更强: E-HET-LEADER-1, E-HET-LEADER-2, E-HET-LEADER-3, E-HET-LEADER-4
│     ├─ P8f 自涉违规更强且高低金额均有效: E-HET-OWN-1, E-HET-OWN-2, E-HET-MON-1, E-HET-MON-2, E-HET-MON-3
│     ├─ P8g 高外部融资依赖企业效应更强: E-HET-RELY-1, E-HET-RELY-2, E-HET-RELY-3, E-CIT-RELY-1
│     └─ P8h 高行业竞争中效应更强，低竞争中方向相反: E-HET-COM-1, E-HET-COM-2, E-HET-COM-3, E-CIT-COM-1, E-CIT-COM-2
└─ P9 作者将经验发现上升为文献贡献和政策启示
   ├─ P9a 贡献于信息披露影响因素研究
   │  ├─ E-CONTR-1 主动披露违规与企业违规纳入同一框架
   │  └─ E-CIT-CONTR-1 信息披露影响因素定位文献
   ├─ P9b 贡献于负面信息披露和同行溢出研究
   │  ├─ E-CONTR-2 主动披露违规从个体治理延伸到行业披露决策
   │  ├─ E-CIT-CONTR-2 负面信息披露资本提供者反应文献
   │  └─ E-CIT-CONTR-3 Gleason et al.(2008)负面信息披露溢出定位
   └─ P9c 政策启示是鼓励主动披露、强化市场监督并差异化监管
      ├─ E-POLICY-1 主动披露豁免或减轻处罚机制
      ├─ E-POLICY-2 支持分析师、媒体和投资者监督
      └─ E-POLICY-3 关注行业领先、融资需求大、竞争激烈行业并甄别策略性披露
```
