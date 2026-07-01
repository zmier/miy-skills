# Evidence Ledger

## 目标

本文件把作者论证树继续下钻到底层证据节点。它服务于 `paper-argument-tree.md`，只记录作者用来支撑自己论证的证据，不记录审稿人的攻击。

字段说明：

| 字段 | 含义 |
|---|---|
| evidence_id | 可被论证树引用的证据编号 |
| 类型 | `text / table / model / coefficient / variable-definition / citation / policy-background` |
| 原文位置 | restored Markdown 中的段落、表格或章节位置 |
| 具体证据 | 能直接支撑命题的底层材料 |
| 支撑节点 / 箭头 | 该证据支撑哪个节点或箭头 |
| 证据粒度 | `exact / summarized / needs-table-qc` |

## X1 证据：问题有意义

| evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点 / 箭头 | 证据粒度 |
|---|---|---|---|---|---|
| E-G1-1 | policy-background | 引言 para 1 | 信息披露有利于资源配置和资本市场稳定 | G1-e1 -> G1 | summarized |
| E-G1-2 | policy-background | 引言 para 1 | 2019 年《证券法》修订扩充信息披露责任主体和责任范围，并提高处罚力度 | G1-e2 -> G1 | summarized |
| E-G1-3 | policy-background | 引言 para 1 | 监管增强后，违法违规手段仍调整，企业违法违规仍屡见不鲜 | G1-e3 -> G1 | summarized |
| E-G1-4 | policy-background | 引言 para 1 | 2025 年新修订《上市公司信息披露管理办法》强调“事前预防”式信息披露要求 | G1-e4 -> G1 | summarized |
| E-G2-1 | citation | 引言 para 3 | 伊志宏等、滕飞等、翟胜宝等用于支持“披露改善多被视为响应内外部监督要求” | G2-e1 -> G2 | summarized |
| E-G2-2 | citation | 引言 para 3 | Dye、Gleason et al. 支持“企业披露可影响同行披露决策” | G2-e2 -> G2 | summarized |
| E-G2-3 | citation | 引言 para 3 | Cao et al.、巫岑等、李宗泽和李志斌、陆雪艳等被作者归为特定信息披露研究；Seo 被作者归为披露“量”研究 | G2-e2/G2-e3 -> G2 | summarized |
| E-G2-4 | text | 引言 para 3 | 作者声称尚未有研究关注企业主动披露违规及其对同行信息披露决策的影响 | G2-e4 -> G2 | summarized |
| E-G3-1 | text | 引言 para 2 | 主动披露违规可能传递诚信经营信号，也可能降低未来声誉损失和处罚成本 | G3-e1/G3-e2 -> G3 | summarized |
| E-G3-2 | citation | 引言 para 2 | Leuz and Verrecchia、Healy and Palepu 支持披露收益/成本逻辑；Wang et al.、Matsumura et al. 支持负面信息披露可能带来信任或市场价值 | G3-e2 -> G3 | summarized |
| E-G3-3 | text | 引言 para 2 | 作者提出主动披露违规可能激励同行改善披露，也可能抑制披露动力 | G3-e3 -> G3 | summarized |
| E-G3-4 | text | 引言 para 5-6 | 作者声称把企业个体治理问题引申到行业信息披露决策问题 | G3-e4 -> G3 | summarized |
| E-G4-1 | text | 引言 para 7 | 作者声称政策制定者多考虑事前事中监督和事后惩罚 | G4-e1 -> G4 | summarized |
| E-G4-2 | text | 引言 para 7 | 作者提出通过激励政策鼓励企业主动披露违规信息 | G4-e2 -> G4 | summarized |
| E-G4-3 | text | 引言 para 7 | 作者提出通过市场机制引导行业内其他企业增强信息披露 | G4-e3 -> G4 | summarized |

## X2 证据：主动披露违规通过声誉竞争和市场压力提升同行披露质量

| evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点 / 箭头 | 证据粒度 |
|---|---|---|---|---|---|
| E-P1-1 | variable-definition | 研究设计 para 3；表1 | 主动披露违规定义为企业当年披露违规，且不存在与该项违规有关的问询或处罚 | P1-e1 -> P1 | summarized |
| E-P1-2 | variable-definition | 研究设计 para 3 | 违规包括违反证券法、信披管理办法等监管明文禁止事项，例如虚构利润、内幕交易、违规担保 | P1-e2 -> P1 | summarized |
| E-P1-3 | variable-definition | 研究设计 para 3；表1 | 同行业其他上市公司的 Peerdumy 取值为 1；POST 在 t 年至 t+2 为 1，t-3 至 t-1 为 0 | P1-e3 -> P1 | summarized |
| E-P2-1 | citation | 理论分析 para 1 | Connelly et al. 被用于支持信号传递理论 | P2-e1 -> P2 | summarized |
| E-P2-2 | text | 理论分析 para 1 | 作者认为主动披露违规展示诚实守信、敢于负责、内部控制和自我纠偏机制 | P2-e2 -> P2 | summarized |
| E-P2-3 | table | 机制检验 para 2；图3 | 图3显示公告后第 4 天起累计超额收益率明显上升 | P2-e3 -> P2 | summarized / needs-figure-qc |
| E-P2-4 | table | 机制检验 para 2；表10 | 表10显示 [-5,5]、[-10,10] 累计超额收益率至少在 5% 水平显著为正 | P2-e4 -> P2 | summarized / needs-table-qc |
| E-P3-1 | text | 理论分析 para 2 | 作者认为行业内企业存在声誉竞争，诚信溢价或正向关注会激励同行改善披露 | P3-e1/P3-e2 -> P3 | summarized |
| E-P3-2 | text | 理论分析 para 3 | 作者认为主动披露违规会引发投资者、分析师、审计师、媒体对行业合规风险的警觉 | P3-e3 -> P3 | summarized |
| E-P3-3 | table | 机制检验 para 5；表12 | 高投资者关注组和高分析师关注组的交乘项系数至少在 5% 水平显著为负，低关注组不显著 | P3-e4 -> P3 | summarized / needs-table-qc |
| E-P3-4 | table | 机制检验 para 3；表11 | `Peerdumy_PosCAR x POST` 在 1% 水平显著为负，`Peerdumy_NegCAR x POST` 不显著 | P3-e5 -> P3 | summarized / needs-table-qc |
| E-P4-1 | citation | 研究设计 para 2 | Kim and Verrecchia、陈运森等被用于支持用 KV 指数度量信息披露质量 | P4-e1 -> P4 | summarized |
| E-P4-2 | variable-definition | 研究设计 para 2；表1 | KV 越小表示上市公司信息披露质量越高 | P4-e2 -> P4 | summarized |
| E-P4-3 | coefficient | 实证结果 para 3；表4 | 基准回归中 `Peerdumy x POST` 系数在 1% 水平显著为负 | P4-e3/P6-e4 -> P4/P6 | summarized / needs-table-qc |
| E-P4-4 | coefficient | 实证结果 para 3；表4 | 作者给出列(2)系数 `-0.0111`，并计算经济意义为 `0.0111 / 0.1159 ≈ 9.58%` | P4-e4/P6-e5 -> P4/P6 | exact |
| E-P5-1 | sample-rule | 样本选择 para 1 | 样本期为 2007-2024 年沪深 A 股上市公司 | P5-e1 -> P5 | exact |
| E-P5-2 | sample-rule | 样本选择 para 1 | 作者选择主动披露违规前 3 年、当年、后 2 年窗口 | P5-e2 -> P5 | exact |
| E-P5-3 | sample-rule | 样本选择 para 1 | 若行业内多家企业主动披露违规且时间间隔过短，则剔除该行业公司样本 | P5-e3 -> P5 | exact |
| E-P5-4 | sample-rule | 样本选择 para 1 | 处理组仅保留行业内第一次满足条件的主动披露违规事件 | P5-e4 -> P5 | exact |
| E-P5-5 | sample-rule | 样本选择 para 1 | 剔除主动披露违规的公司样本 | P5-e5 -> P5 | exact |
| E-P5-6 | sample-rule | 样本选择 para 1 | 剔除 ST、金融保险、仅前/后期存在和关键变量缺失样本，最终得到 11339 个公司-年度观察 | P5-e6 -> P5 | exact |
| E-P6-1 | model | 研究设计 para 5 | 模型以 `KV` 为因变量、`Peerdumy x POST` 为核心解释变量，并加入公司固定效应和年度固定效应 | P6-e1 -> P6 | summarized |
| E-P6-2 | table | 事前趋势 para 2；表3 | `Peerdumy x Pre1-3` 和 `Peerdumy x Pre-2` 不显著，作者据此认为满足平行趋势 | P6-e2 -> P6 | summarized / needs-table-qc |
| E-P6-3 | table | 事前趋势 para 2；表3 | `Peerdumy x After+1` 和 `Peerdumy x After+2` 至少在 10% 水平显著为负 | P6-e3 -> P6 | summarized / needs-table-qc |
| E-P6-4 | coefficient | 实证结果 para 3；表4 | `Peerdumy x POST` 在 1% 水平显著为负；列(2)系数为 `-0.0111` | P6-e4 -> P6 | exact for coefficient / summarized for t-stat |
| E-P7-1 | table | 机制检验 para 3；表11 | 正 CAR 组处理效应显著，负 CAR 组不显著 | P7-e1 -> P7 | summarized / needs-table-qc |
| E-P7-2 | table | 机制检验 para 5；表12 | 高关注组效应显著，低关注组不显著 | P7-e2 -> P7 | summarized / needs-table-qc |
| E-P7-3 | table | 机制检验 para 7；表13 列(1) | 高监管距离与低监管距离组均显著，组间系数差异不显著 | P7-e3 -> P7 | summarized / needs-table-qc |
| E-P7-4 | table | 机制检验 para 8；表13 列(2)(3) | `Peerdumy x POST` 对被处罚次数和处罚严重程度的系数均不显著 | P7-e4 -> P7 | summarized / needs-table-qc |
| E-P7-5 | text | 机制检验 para 8 | 作者解释违规公告多仅简述违规主体和行为，缺少具体违规细节 | P7-e5 -> P7 | summarized |
| E-P8-1 | table | 稳健性 para 4；表5 | 堆叠 DID 后 `Peerdumy x POST` 仍在 1% 水平显著为负 | P8-e1 -> P8 | summarized / needs-table-qc |
| E-P8-2 | table | 稳健性 para 5；图1 | Bacon 分解中 later-vs-earlier 权重仅 2.4% | P8-e2 -> P8 | exact |
| E-P8-3 | table | 稳健性 para 6；图2 | 500 次安慰剂检验系数均值接近 0；双侧 p=0.0560、左侧 p=0.0240 | P8-e3 -> P8 | exact |
| E-P8-4 | table | 稳健性 para 7；表6 | PSM 后 1% 显著为负；熵平衡后 5% 显著为负 | P8-e4 -> P8 | summarized / needs-table-qc |
| E-P8-5 | table | 稳健性 para 8；表7 | 剔除受分行业信息披露政策影响行业后，交乘项仍在 5% 水平显著为负 | P8-e5 -> P8 | summarized / needs-table-qc |
| E-P8-6 | table | 稳健性 para 9；表8 | Oster 检验中方法1的 beta* 在 95% 置信区间内，方法2的 delta 大于 1 | P8-e6 -> P8 | summarized / needs-table-qc |
| E-P8-7 | table | 稳健性 para 10；表9 | DA 替代指标下 10% 显著为负；重构 POST_Month 后 1% 显著为负 | P8-e7 -> P8 | summarized / needs-table-qc |
| E-P9-1 | text | 结论 para 1 | 作者总结主动披露违规有效提升同行信息披露质量 | P9-e1 -> P9 | summarized |
| E-P9-2 | text | 结论 para 1 | 作者总结声誉竞争和市场压力是主要机制 | P9-e2 -> P9 | summarized |
| E-P9-3 | text | 政策启示 para 3 | 作者建议监管部门设立主动披露豁免或减轻处罚机制 | P9-e3 -> P9 | summarized |
| E-P9-4 | text | 政策启示 para 4 | 作者建议支持分析师、媒体、投资者等市场监督，利用市场机制引导披露 | P9-e4 -> P9 | summarized |

## 证据粒度缺口

当前 restored Markdown 对多张表格只保留了作者正文解释，未完整保留表格数值。因此以下证据需要回到原 PDF / 表格抽取结果做 QC：

```text
表3：各 lead/lag 项具体系数、t 值、显著性
表4：各列 Peerdumy x POST 的系数、t 值/标准误、显著性
表5-表9：稳健性表的具体系数、t 值/标准误、显著性
表10-表13：机制检验表的具体系数、t 值/标准误、显著性
表14-表18：进一步分析表的具体系数、组间差异检验和显著性
```

在完成 table QC 前，本 ledger 对这些表格证据只使用作者正文中的显著性描述，不伪造具体表格数值。
