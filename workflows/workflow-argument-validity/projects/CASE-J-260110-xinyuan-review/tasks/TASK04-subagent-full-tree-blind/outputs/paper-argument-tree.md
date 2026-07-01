# Paper Argument Tree

## 一句话核心发现

```text
X: 上市公司在未被监管锁定或外部曝光前主动披露违规。
M: 同行企业感知到声誉竞争压力与市场关注/市场预期压力；监管信息传导机制被作者检验为非主要路径。
Y1: 同行业其他上市公司提升信息披露质量，表现为 KV 指数下降。
Y2 / contribution: 主动披露违规可成为引导行业自律和优化信息披露监管的市场化机制。
```

## 顶层论证

```text
X1: 问题有意义，现有信息披露与同群效应文献尚未充分处理“主动披露违规”对同行披露质量的溢出。
+ X2: 作者证明了主动披露违规通过声誉竞争与市场压力提升同行信息披露质量。
-> Y: 论文贡献成立，能扩展信息披露影响因素、负面信息披露经济后果和监管制度创新讨论。
```

## X/M/Y/Y2 表

| 元素 | 作者说法 | 操作化 / 证明方式 | 原文位置 | 备注 |
|---|---|---|---|---|
| X | 主动披露违规 | 企业当年披露违规行为，且不存在与该项违规有关的问询或处罚；同行业其他上市公司 Peerdumy=1 | `manuscript.md` 三(二)2；`pdf-pages-text.md` PDF Page 7 | 定义依赖违规类型清单与“无问询/处罚”条件 |
| M1 | 声誉竞争 | 事件研究 CAR；正 CAR 组中同行 KV 下降更明显 | PDF Page 18-20；表10、表11 | 表值需视觉核验 |
| M2 | 市场压力 | 高投资者关注/高分析师关注组中处理效应更强 | PDF Page 20-21；表12 | 表值需视觉核验 |
| M3 | 信息传导 | 监管距离、处罚次数、处罚强度检验不支持其为主要机制 | PDF Page 22-23；表13 | 作者用非显著处罚结果排除机制 |
| Y1 | 信息披露质量提升 | KV 指数越小表示信息披露质量越高；Peerdumy×POST 系数显著为负 | PDF Page 7、11；表4 | 主结论是 KV 下降 |
| Y2 | 行业自律与监管创新 | 鼓励主动披露违规可通过市场化机制促进信息透明度 | 引言贡献、PDF Page 31-32 | 政策上升依赖 Y1/M 成立 |

## 命题节点表

| node_id | node_label | parent | evidence_ids | status |
|---|---|---|---|---|
| Y | 论文贡献成立：主动披露违规可引导行业自律并提供监管启示 | root | E-ABS, E-C1, E-C2, E-C3 | not-yet-audited |
| X1 | 研究问题有意义 | Y | E-G1, E-G2, E-G3, E-G4 | not-yet-audited |
| G1 | 现实监管背景需要从事后纠偏转向事前预防 | X1 | E-G1 | not-yet-audited |
| G2 | 主动披露违规的行业溢出方向理论上不确定 | X1 | E-G2 | not-yet-audited |
| G3 | 既有文献关注监管、市场竞争或披露同群效应，但未聚焦主动披露违规对同行披露质量 | X1 | E-G3 | not-yet-audited |
| G4 | 论文声称贡献在于把主动披露违规扩展到行业信息披露决策 | X1 | E-G4 | not-yet-audited |
| X2 | 作者证明了主动披露违规提升同行信息披露质量并解释机制 | Y | E-D1, E-V1, E-M0, E-R1, E-M1, E-M2, E-M3, E-H1, E-H2, E-H3 | not-yet-audited |
| P1 | X 被定义为“无相关问询或处罚前提下主动披露违规” | X2 | E-V2 | not-yet-audited |
| P2 | Y 被定义为 KV 指数反向度量的信息披露质量 | X2 | E-V1 | not-yet-audited |
| P3 | 样本和事件窗口能够构造多时点 DID | X2 | E-D1, E-D2, E-V3 | not-yet-audited |
| P4 | 模型设定使用 Peerdumy×POST、控制变量、公司/年度固定效应和公司层面聚类 | X2 | E-MODEL | not-yet-audited |
| P5 | 主结果支持主动披露违规后同行披露质量提升 | X2 | E-R1 | not-yet-audited |
| P6 | 稳健性检验支持主结果 | X2 | E-R2, E-R3, E-R4, E-R5, E-R6, E-R7 | not-yet-audited |
| P7 | 声誉竞争机制被事件研究和正 CAR 分组检验支持 | X2 | E-M1, E-M1A | not-yet-audited |
| P8 | 市场压力机制被投资者关注与分析师关注分组检验支持 | X2 | E-M2 | not-yet-audited |
| P9 | 信息传导机制不是主要路径 | X2 | E-M3 | not-yet-audited |
| P10 | 事件公司特征支持声誉解释 | X2 | E-H1, E-H2, E-H3 | not-yet-audited |
| P11 | 同行企业融资依赖与行业竞争条件强化溢出效应 | X2 | E-H4, E-H5 | not-yet-audited |
| P12 | 贡献上升为监管与市场化监督启示 | Y | E-C1, E-C2, E-C3 | not-yet-audited |

## 作者证据链摘要

1. 作者从监管升级和主动披露违规的现实行为进入，指出主动披露违规既可能被解读为诚信信号，也可能被解读为风险暴露或策略性自利行为，因此同行披露质量的方向需要实证检验。
2. 理论部分提出竞争性假说：主动披露违规可能提升或抑制同行信息披露质量，并提出声誉竞争、市场压力和信息传导三条可能机制。
3. 研究设计以 2007-2024 年沪深 A 股、11339 个公司-年度观测值构造多时点 DID；核心变量是 `Peerdumy×POST`，Y 为 KV 指数，KV 越低表示信息披露质量越高。
4. 主回归中 `Peerdumy×POST` 显著为负，作者解释为同行企业披露质量提升，经济意义约为 9.58%。
5. 稳健性部分用堆叠 DID、Bacon 分解、混合安慰剂、PSM/熵平衡、剔除分行业披露指引影响、Oster、替代 Y 和替代 POST 编码支持主结论。
6. 机制部分把声誉竞争落到事件公司 CAR 与正/负 CAR 分组，把市场压力落到投资者关注/分析师关注分组，把信息传导落到监管距离、处罚次数和处罚强度。
7. 异质性进一步显示事件公司行业地位、自涉违规、高外部融资依赖和高行业竞争时正向溢出更强，违规严重程度高低均有效但差异不显著。

## 箭头台账

| arrow_id | from_node | to_node | support_type | status | why |
|---|---|---|---|---|---|
| A-G1-X1 | G1 | X1 | real-world importance | not-yet-audited | 监管背景支撑问题重要性 |
| A-G2-X1 | G2 | X1 | theoretical ambiguity | not-yet-audited | 方向不确定支撑研究必要性 |
| A-G3-X1 | G3 | X1 | literature gap | not-yet-audited | 既有文献边界支撑 novelty |
| A-X1-Y | X1 | Y | contribution relevance | not-yet-audited | 问题重要性支撑贡献 |
| A-P1-X2 | P1 | X2 | treatment definition | not-yet-audited | X 的操作化支撑实证检验 |
| A-P2-X2 | P2 | X2 | outcome definition | not-yet-audited | Y 的操作化支撑主结论 |
| A-P3-X2 | P3 | X2 | data/sample fit | not-yet-audited | 样本和窗口支撑识别框架 |
| A-P4-X2 | P4 | X2 | model specification | not-yet-audited | DID 模型支撑估计 |
| A-P5-X2 | P5 | X2 | main result | not-yet-audited | 主回归支撑核心发现 |
| A-P6-X2 | P6 | X2 | robustness | not-yet-audited | 稳健性支撑结果可靠性 |
| A-P7-X2 | P7 | X2 | mechanism | not-yet-audited | CAR 与分组检验支撑声誉机制 |
| A-P8-X2 | P8 | X2 | mechanism | not-yet-audited | 关注度分组支撑市场压力机制 |
| A-P9-X2 | P9 | X2 | mechanism exclusion | not-yet-audited | 处罚/监管距离检验排除信息传导 |
| A-P10-X2 | P10 | X2 | heterogeneity | not-yet-audited | 事件公司特征支撑声誉解释 |
| A-P11-X2 | P11 | X2 | heterogeneity | not-yet-audited | 同行/行业条件支撑机制边界 |
| A-X2-Y | X2 | Y | empirical proof to contribution | not-yet-audited | 实证链支撑贡献成立 |
| A-P12-Y | P12 | Y | policy implication | not-yet-audited | 政策启示支撑 Y2 |

