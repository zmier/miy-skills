# Evidence Ledger

| evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点 / 箭头 | 证据粒度 | Obsidian 链接 |
|---|---|---|---|---|---|---|
| E-ABS | 摘要 | PDF Page 1 | 摘要声称主动披露违规提升同行披露质量，机制为声誉竞争和市场压力，行业地位、自涉违规、融资依赖、竞争程度强化效应 | Y, X2 | exact | [[manuscript#摘要]] |
| E-G1 | 现实背景 | `manuscript.md` 引言 para 1；PDF Page 2 | 证券法修订、信息披露违法处罚力度提升、2025 年信息披露管理办法强调事前预防 | G1 -> X1 | exact | [[manuscript#一、引言]] |
| E-G2 | 理论 puzzle | `manuscript.md` 引言 para 2；PDF Page 2-3 | 主动披露违规可能传递诚信信号并激励同行改善，也可能因风险曝光导致同行减少风险信息披露 | G2 -> X1 | exact | [[manuscript#一、引言]] |
| E-G3 | 文献 gap | `manuscript.md` 引言 para 3；PDF Page 3 | 既有研究多关注监管、特定信息披露或披露数量，作者称尚未关注主动披露违规对同行披露决策影响 | G3 -> X1 | exact | [[manuscript#一、引言]] |
| E-G4 | 贡献声称 | `manuscript.md` 引言 para 5-7；PDF Page 3-4 | 作者声称拓展企业信息披露影响因素、负面信息披露溢出和监管制度设计 | G4 -> X1, P12 -> Y | exact | [[manuscript#一、引言]] |
| E-T1 | 理论机制 | PDF Page 4-6 | 理论部分提出声誉竞争、市场压力、信息传导三类提升路径，也承认可能产生抑制效应 | P7/P8/P9 | exact | [[manuscript#二、理论分析]] |
| E-T2 | 假说 | PDF Page 6 | 提出 H1a 提升同行披露质量、H1b 抑制同行披露质量的竞争性假说 | G2, X2 | exact | [[manuscript#二、理论分析]] |
| E-D1 | 样本 | `manuscript.md` 三(一)；PDF Page 6-7 | 2007-2024 年沪深 A 股；最终 11339 个公司-年度观察数据；数据来自 CNRDS、CSMAR、WIND | P3 -> X2 | exact | [[manuscript#三、研究设计]] |
| E-D2 | 样本筛选 | PDF Page 6 | 剔除短间隔多事件行业、仅保留首次事件窗口、剔除事件公司、ST/*ST、金融保险、窗口不完整和关键变量缺失样本 | P3 -> X2 | exact | [[manuscript#三、研究设计]] |
| E-V1 | Y 定义 | `manuscript.md` 三(二)1；PDF Page 7 | 以交易量对收益率影响系数 KV 度量信息披露质量，KV 越小表示披露质量越高 | P2 -> X2 | exact | [[manuscript#三、研究设计]] |
| E-V2 | X 定义 | `manuscript.md` 三(二)2；PDF Page 7 | 若企业当年披露违规行为且不存在相关问询或处罚，认定为主动披露违规；同行业其他上市公司 Peerdumy=1 | P1 -> X2 | exact | [[manuscript#三、研究设计]] |
| E-V3 | POST 定义 | `manuscript.md` 三(二)2；PDF Page 7 | 行业内某公司 t 年主动披露违规，POST 在 t 至 t+2 为 1，t-3 至 t-1 为 0 | P3/P4 -> X2 | exact | [[manuscript#三、研究设计]] |
| E-MODEL | 模型 | `manuscript.md` 三(三)；PDF Page 8 | 构建 KV 对 Peerdumy×POST 和控制变量的 DID 模型，加入公司固定效应、年份固定效应，公司层面聚类标准误 | P4 -> X2 | exact | [[manuscript#三、研究设计]] |
| E-DESC | 描述统计 | PDF Page 8-9；表2 | KV 均值 0.1159，Peerdumy 均值 0.3870，Peerdumy×POST 均值 0.1972，样本 11339 | P3/P2 | needs-table-visual-qc | [[manuscript#Table 2]] |
| E-PT | 平行趋势 | PDF Page 9-10；表3 | Pre 系数不显著，After t+1 和 t+2 显著为负，作者据此认为事前趋势相对平行 | P6 -> X2 | needs-table-visual-qc | [[manuscript#Table 3]] |
| E-R1 | 主回归 | PDF Page 11；表4 | Peerdumy×POST 为 -0.0157*** 和 -0.0111***；作者称同行信息披露质量平均提升 9.58% | P5 -> X2 | needs-table-visual-qc | [[manuscript#Table 4]] |
| E-R2 | 堆叠 DID | PDF Page 12；表5 | Peerdumy×POST 为 -0.0184*** 和 -0.0129***；使用队列固定效应和公司-队列聚类 | P6 -> X2 | needs-table-visual-qc | [[manuscript#Table 5]] |
| E-R3 | Bacon / placebo | PDF Page 13；图1、图2 | Later vs Earlier 权重 2.4%；500 次混合安慰剂，双侧 p=0.0560、左侧 p=0.0240 | P6 -> X2 | summarized / needs-figure-qc | [[manuscript#Figure 1]], [[manuscript#Figure 2]] |
| E-R4 | PSM / 熵平衡 | PDF Page 14-15；表6 | PSM 下 Peerdumy×POST=-0.0116***；熵平衡下 -0.0103** | P6 -> X2 | needs-table-visual-qc | [[manuscript#Table 6]] |
| E-R5 | 排除共同政策 | PDF Page 15-16；表7 | 剔除分行业信息披露指引影响行业后，Peerdumy×POST=-0.0117** | P6 -> X2 | needs-table-visual-qc | [[manuscript#Table 7]] |
| E-R6 | Oster | PDF Page 16；表8 | β*=-0.0035 在 95% 置信区间内，δ=1.4633>1，作者称遗漏变量检验通过 | P6 -> X2 | needs-table-visual-qc | [[manuscript#Table 8]] |
| E-R7 | 替换变量/POST | PDF Page 17；表9 | DA 作为反向代理时 Peerdumy×POST=-0.0044*；POST_Month 下 -0.0117*** | P6 -> X2 | needs-table-visual-qc | [[manuscript#Table 9]] |
| E-M1 | 声誉机制事件研究 | PDF Page 18；图3、表10 | 事件日后 CAR 上升；[-5,5] CAR=0.0182***，[-10,10] CAR=0.0342*** | P7 -> X2 | needs-table-visual-qc / needs-figure-qc | [[manuscript#Table 10]] |
| E-M1A | 声誉机制分组 | PDF Page 19-20；表11 | 正 CAR 组交互项显著为负；负 CAR 组多为不显著；作者据此支持声誉竞争逻辑 | P7 -> X2 | needs-table-visual-qc | [[manuscript#Table 11]] |
| E-M2 | 市场压力机制 | PDF Page 20-21；表12 | 高投资者关注组 -0.0146**，高分析师关注组 -0.0259***；低关注组不显著 | P8 -> X2 | needs-table-visual-qc | [[manuscript#Table 12]] |
| E-M3 | 信息传导机制 | PDF Page 22-23；表13 | 高/低监管距离组均显著为负且差异不显著；处罚次数和处罚强度的 Peerdumy×POST 不显著 | P9 -> X2 | needs-table-visual-qc | [[manuscript#Table 13]] |
| E-H1 | 事件公司行业地位 | PDF Page 24-25；表14 | Leader 组 Peerdumy×POST 均在 1% 显著为负，NoLeader 不显著 | P10 -> X2 | needs-table-visual-qc | [[manuscript#Table 14]] |
| E-H2 | 自涉违规 | PDF Page 25-26；表15 | Peerdumy_Own×POST=-0.0183***，Peerdumy_Other×POST=-0.0054 不显著 | P10 -> X2 | needs-table-visual-qc | [[manuscript#Table 15]] |
| E-H3 | 违规严重程度 | PDF Page 27-28；表16 | HighMon 与 LowMon 均在 5% 显著为负，组内差异 p=0.9322；部分金额不可识别导致样本减少 | P10 -> X2 | needs-table-visual-qc | [[manuscript#Table 16]] |
| E-H4 | 外部融资依赖 | PDF Page 28-29；表17 | 高融资依赖组显著为负，低融资依赖组不显著；一组差异 p=0.0424 | P11 -> X2 | needs-table-visual-qc | [[manuscript#Table 17]] |
| E-H5 | 行业竞争程度 | PDF Page 30-31；表18 | 高竞争组显著为负，低竞争组显著为正，差异 p=0.0000 | P11 -> X2 | needs-table-visual-qc | [[manuscript#Table 18]] |
| E-C1 | 结论归纳 | PDF Page 31-32 | 结论重申主效应、声誉竞争/市场压力、事件公司特征、融资依赖和竞争程度 | Y/P12 | exact | [[manuscript#七、研究结论与启示]] |
| E-C2 | 监管启示 | PDF Page 32 | 建议修正行政处罚裁量规则，对主动披露违规企业从宽从轻处理 | P12 -> Y | exact | [[manuscript#七、研究结论与启示]] |
| E-C3 | 市场中介/企业启示 | PDF Page 32-33 | 建议外部中介评价披露治理能力，企业应积极披露违规相关信息 | P12 -> Y | exact | [[manuscript#七、研究结论与启示]] |

## QC

| item | reason | next action |
|---|---|---|
| table-values | `restoration-qc.md` 明示 Table 2-18 依赖 page text/table snippets，未视觉核验 | 回 PDF 逐表核对系数、t 值、样本量、星号和表注 |
| figure-values | Bacon、安慰剂、CAR 图仅有文字描述或少量数值 | 回 PDF 视觉核验图形趋势 |
| event-count | 手稿未在已读文本中清晰给出事件数或行业数 | 后续如审计识别强度，需要补充事件样本构成 |
| variable construction | KV、Peerdumy、POST 有定义，但部分违规公告识别流程细节未展开 | 后续验箭头需检查 CNRDS/公告识别可复现性 |

