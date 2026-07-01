# Paper Argument Tree

## 一句话核心发现

```text
X: 行业内企业主动披露违规（Peerdumy × POST）
M: 声誉竞争与市场压力；信息传导机制被作者作为非主要机制排除
Y1: 同行业其他企业信息披露质量提高，即 KV 指数下降
Y2 / contribution: 主动披露违规可通过市场化激励引导行业自律发展，并为监管激励、市场化监督和差异化监管提供政策依据
```

## 顶层论证

```text
X1：问题有意义
+ X2：作者证明了具体核心发现
-> Y：论文贡献成立 / 值得发表
```

## X/M/Y/Y2 表

| 元素 | 作者说法 | 操作化 / 证明方式 | 原文位置 | 备注 |
|---|---|---|---|---|
| X | 上市公司主动披露违规对同行其他企业产生溢出影响 | Peerdumy × POST；Peerdumy 为行业内是否有主动披露违规公司，POST 为 t 至 t+2 | 三、研究设计；表 1 | 处理窗口与样本筛选在 P1/P4 展开 |
| M1 | 声誉竞争 | 事件公司主动披露违规的 CAR；正/负 CAR 分组后回归 | 五（一）；表 10、表 11 | 表 11 第三列冲突不进入作者树，见 2B |
| M2 | 市场压力 | 高/低投资者关注、分析师关注分组回归 | 五（二）；表 12 | 高关注组显著更强 |
| M3 | 信息传导机制不是主要机制 | 监管距离分组、同行被处罚次数和处罚严重程度 | 五（三）；表 13 | 作者用不显著处罚结果排除该机制 |
| Y1 | 同行业其他企业信息披露质量提高 | KV 指数，KV 越小信息披露质量越高 | 三（二）；表 1、表 4 | 主结果列(2) Peerdumy×POST = -0.0111*** |
| Y2 | 行业自律发展与监管政策启示 | 主动披露激励、市场化监督、差异化监管 | 七（二） | 贡献上升节点 P9 |

## 命题节点表

| node_id | node_label | parent | evidence_ids | status |
|---|---|---|---|---|
| Y | 论文贡献成立 |  |  | complete |
| X1 | 问题有意义 | Y |  | complete |
| G1 | 制度背景强化信息披露监管 | X1 | E-X1-REG-1; E-X1-REG-2 | complete |
| G2 | 主动披露违规的行业外溢方向待定 | X1 | E-X1-PUZZLE-1 | complete |
| G3 | 文献缺口存在 | X1 | E-X1-GAP-1; E-X1-GAP-2 | complete |
| G4 | 作者声称贡献 | X1 | E-X1-CONTRIB-1; E-X1-CONTRIB-2 | complete |
| X2 | 作者证明核心发现 | Y |  | complete |
| P1 | X 被定义和操作化 | X2 | E-XDEF-1; E-XDEF-2; E-XDEF-3; E-XDEF-4; E-XDEF-5 | complete |
| P2 | 理论机制成立 | X2 | E-THEORY-H1-1; E-THEORY-H1-4 | complete |
| P2.1 | 声誉竞争理论逻辑 | P2 | E-THEORY-H1-2; E-THEORY-H2A-1 | complete |
| P2.2 | 市场压力理论逻辑 | P2 | E-THEORY-H1-3; E-THEORY-H2B-1 | complete |
| P3 | Y 被定义和操作化 | X2 | E-YDEF-1; E-YDEF-2; E-YDEF-3; E-DESC-1 | complete |
| P4 | 样本/数据适配 | X2 | E-SAMPLE-1 到 E-SAMPLE-10; E-DESC-2 | complete |
| P5 | 方法/识别可信 | X2 | E-CTRL-1; E-MODEL-1; E-MODEL-2; E-MODEL-3 | complete |
| P5.1 | 事前趋势支持 DID | P5 | E-PT-1 到 E-PT-5 | complete |
| P6 | 主结果支持 H1 | X2 |  | complete |
| P6.1 | 表 4 核心系数显著为负 | P6 | E-MAIN-1 到 E-MAIN-5 | complete |
| P6.2 | 经济意义为 9.58% | P6 | E-MAIN-6 | complete |
| P7 | 机制证据 | X2 |  | complete |
| P7.1 | 声誉竞争机制 | P7 | E-MECH-RC-1 到 E-MECH-RC-8 | complete |
| P7.2 | 市场压力机制 | P7 | E-MECH-MP-1 到 E-MECH-MP-6 | complete |
| P7.3 | 信息传导不是主要机制 | P7 | E-MECH-IT-1 到 E-MECH-IT-5 | complete |
| P8 | 稳健性回应 | X2 | E-ROB-1 到 E-ROB-13 | complete-with-qc |
| P10 | 进一步分析 | X2 | E-HET-* | complete |
| P9 | 贡献上升 | Y | E-X1-POLICY-1 | complete |

## 作者树边界

2A 作者证据树只还原作者如何支撑本文主张。表 11 第三列中 `PosCAR[-10,10]` 不显著且 `NegCAR[-10,10]` 显著为负的冲突证据，没有连入 P7.1 的作者支持链；它只进入 `review-sensitivity-map.md` 和 `sensitivity-expanded-mermaid.md`。
