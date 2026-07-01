# Internal Arrow Audit Table

First round uses only manuscript-internal evidence from TASK07. External needs are marked but not searched.

| arrow_id | A 是否足以推出 B（内部证据） | hidden_premise | status | break_type | domain_expression | qc_flags | impact_on_X1_X2_Y |
|---|---|---|---|---|---|---|---|
| A001 | 内部上，X1 能支撑“问题有研究意义”，但不能单独证明论文贡献成立；贡献还依赖 X2 与 P9。 | 文献 gap 真实且重要，且 X2 成立。 | needs-external-evidence | overclaim | evidence-claim mismatch / literature gap needs verification | citation-qc; external-evidence-qc | Y0 |
| A002 | 如果 X2 成立，它是 Y0 的核心支撑；但 X2 内部含多个待 QC 的测量、识别和机制箭头。 | 主结果可因果解释，机制证据一致，Y 测量成立。 | weak | hidden-premise-missing | contribution depends on unresolved identification/mechanism premises | table-qc; method-qc | Y0 |
| A003 | 政策启示可作为论文意义的补充，但不能独立证明贡献成立。 | 发现可外推到政策设计。 | weak | scope-expansion | evidence supports narrower policy implications than asserted | external-evidence-qc | Y0 |
| A004 | 监管转向和案例能说明现实背景重要。 | 这些制度事实与本文研究对象直接相关。 | strong-with-qc | evidence-qc-gap | institutional relevance with date/source QC | source-date-qc | X1 |
| A005 | 正反机制并存足以说明方向不确定、值得实证。 | 两种方向均有理论可能性。 | strong-with-qc | evidence-qc-gap | theoretical tension is plausible but citations need verification | citation-qc | X1 |
| A006 | 内部只能看到作者声称已有文献未覆盖；是否真 gap 必须外部检索。 | 引用文献确实未直接研究该 X -> Y。 | needs-external-evidence | evidence-qc-gap | literature gap requires search/citation verification | citation-qc; external-evidence-qc | X1; Y0 |
| A007 | 贡献定位依赖 A006 的 gap 真实性，内部不能定论。 | gap 真实且本文确实比既有文献多出新解释。 | needs-external-evidence | hidden-premise-missing | contribution positioning depends on verified literature boundary | citation-qc | X1; Y0 |
| A008 | 定义、处理组和剔除事件公司能内部支撑 X 的基本操作化。 | “主动披露违规”规则没有混入被动披露或反向选择。 | strong-with-qc | evidence-qc-gap | treatment definition is traceable but needs sample/timing QC | sample-consistency-qc | X2 |
| A009 | 理论机制能说明可能方向，但不能证明主要机制。 | 信号、声誉竞争、市场压力会传导到同行披露行为。 | weak | hidden-premise-missing | mechanism is plausible but not sufficient without empirical mechanism support | citation-qc | X2 |
| A010 | 内部可确认作者定义“KV 越小披露质量越高”，但 KV 是否充分代表披露质量需要外部测量文献。 | KV 指标有效捕捉披露质量而非流动性/交易冲击等相邻概念。 | needs-external-evidence | measurement-mismatch | construct-measure validity pending | table-qc; external-evidence-qc | X2; Y0 |
| A011 | 样本结构清楚，能支撑经验检验对象；但是否充分适配机制和 DID 比较组仍需识别层审计。 | 筛选不会剔除关键机制场景或制造比较口径偏差。 | strong-with-qc | evidence-qc-gap | sample design is traceable with mechanism-fit QC | sample-qc | X2 |
| A012 | DID 证据内部上支持“有关联且方向一致”，但不足以完全推出因果声称。 | 平行趋势、无同期冲击、聚类层级、错峰处理和样本构造均足够。 | weak | causal-leap | identification does not yet fully support causal wording | method-qc; table-qc; figure-qc | X2; Y0 |
| A013 | 表4负显著能支撑主结果方向，但依赖 KV 有效性和表格 QC。 | 系数方向、显著性、量纲和 Y 解释均正确。 | strong-with-qc | evidence-qc-gap | result supports empirical association pending table/measure QC | table-qc; measure-qc | X2 |
| A014 | 机制总体内部证据不稳，尤其表11列(3)与正文冲突。 | 三类机制证据一致支持声誉竞争/市场压力，并排除信息传导。 | weak | contradiction | mechanism evidence contains table-text conflict and incomplete exclusion | table-text-conflict; table-qc | X2; Y0 |
| A015 | 稳健性覆盖面较广，但部分检验只重复相关框架，不能自动回应所有核心威胁。 | 每个稳健性检验都对应核心识别/测量威胁。 | weak | hidden-premise-missing | robustness-threat fit remains uneven | method-qc; figure-qc; table-qc | X2 |
| A016 | 定义规则可支撑 P1a。 | 无外部问询/处罚前披露即可视为主动。 | strong-with-qc | evidence-qc-gap | treatment definition traceable | table-qc | X2 |
| A017 | 编码说明清楚，但 t 到 t+2 的窗口需要与理论反应期和 POST_Month 结果一致。 | 事件影响从 t 年起至 t+2 年发生且同业可感知。 | strong-with-qc | hidden-premise-missing | timing assumption needs justification | timing-qc | X2 |
| A018 | 剔除事件公司有助于同行溢出识别。 | 剔除规则没有改变目标同行总体。 | strong-with-qc | evidence-qc-gap | peer-spillover scope mostly supported | sample-qc | X2 |
| A019 | 信号机制内部上是可能解释，不是已证明机制。 | 主动披露违规会被市场解读为诚信合规信号。 | weak | alternative-explanation | signal interpretation remains contestable | citation-qc | X2 |
| A020 | 声誉竞争理论可支持机制假设，但仍需表10/11实证一致。 | 同行会因事件公司获得诚信溢价而提升披露质量。 | weak | hidden-premise-missing | reputation mechanism requires consistent empirical support | citation-qc; table-qc | X2 |
| A021 | 市场压力理论支持机制假设。 | 外部关注能传导到同行披露改善。 | strong-with-qc | evidence-qc-gap | plausible mechanism pending citation/table QC | citation-qc; table-qc | X2 |
| A022 | 样本期和数据源能支撑数据基础。 | 数据源能覆盖全部关键变量。 | strong |  | data source support |  | X2 |
| A023 | 事件窗口和筛选规则清楚，但机制适配和样本损失需进一步核查。 | 筛选规则不引入选择性样本。 | strong-with-qc | sample-weakness | sample restriction may affect mechanism-relevant sample | sample-qc | X2 |
| A024 | 样本量和缩尾处理说明清楚。 | 缩尾不改变核心估计。 | strong-with-qc | evidence-qc-gap | reporting transparency pending table QC | table-qc | X2 |
| A025 | 模型设定内部完整，但公司层聚类是否匹配行业/事件层冲击需要方法 QC。 | 标准误聚类层级和固定效应足以处理相关性。 | needs-qc | evidence-qc-gap | cluster/reporting transparency concern | cluster-level-qc; method-qc | X2 |
| A026 | 处理前两期不显著支持前趋势，但仅靠不显著不能完全证明平行趋势。 | 无显著差异即足以证明趋势相同。 | weak | hidden-premise-missing | pretrend evidence is suggestive, not conclusive | table-qc; method-qc | X2 |
| A027 | stacked DID 系数支持方向，Bacon 权重信息有帮助；图1未精确 QC，方法充分性待核。 | 这些检验充分解决错峰 DID 异质性处理偏误。 | strong-with-qc | evidence-qc-gap | staggered DID robustness pending figure/method QC | figure-qc; method-qc | X2 |
| A028 | 表4系数负且显著，足以内部支撑结果方向。 | 表格数值准确，KV 解释成立。 | strong-with-qc | evidence-qc-gap | coefficient supports result pending table QC | table-qc | X2 |
| A029 | 9.58% 计算内部可复现，但“披露质量平均提升”表述依赖 KV 比例解释。 | 0.0111/KV均值可解释为披露质量提升百分比。 | strong-with-qc | numerical-trap | magnitude interpretation needs scale clarification | scale-qc; table-qc | X2 |
| A030 | 声誉竞争机制被表11列(3)冲突削弱。 | PosCAR 组在各窗口均更强且 NegCAR 组不显著。 | weak | contradiction | table-text conflict in reputation mechanism | table-text-conflict; table-qc | X2 |
| A031 | 高关注组更强总体支持市场压力，但投资者关注差异 p=0.0608 边际。 | 高关注与低关注差异稳定且经济含义清楚。 | strong-with-qc | evidence-qc-gap | market-pressure mechanism supported with group-difference QC | table-qc | X2 |
| A032 | 不显著处罚结果和监管距离差异不足以完全排除信息传导。 | 若监管传导存在，必然体现为距离分组差异或处罚次数/严重度变化。 | weak | condition-confusion | mechanism exclusion is stronger than evidence allows | alternative-explanation-qc; table-qc | X2 |
| A033 | PSM/熵平衡后结果方向一致，支持稳健性。 | 匹配后平衡性充分。 | strong-with-qc | evidence-qc-gap | matching robustness pending balance/table QC | matching-balance-qc; table-qc | X2 |
| A034 | 剔除共同因素后结果仍显著，支持一类威胁的排除。 | 分行业指引是主要共同因素。 | strong-with-qc | hidden-premise-missing | robustness addresses one threat, not all common shocks | table-qc | X2 |
| A035 | Oster、DA、POST_Month 提供补强，但 DA 只有边际显著且方法需外部标准。 | 这些检验足以排除遗漏变量和测量/时间口径威胁。 | needs-qc | evidence-qc-gap | omitted-variable and alt-measure robustness require method/table QC | method-qc; table-qc | X2 |
| A036 | placebo 需要图2精确核验；p 值呈单侧/双侧差异，内部不足以完全定论。 | placebo 分布足以排除随机伪处理和遗漏政策影响。 | needs-qc | evidence-qc-gap | placebo evidence pending figure/method QC | figure-qc; method-qc | X2 |
| A037 | 领先企业定义中两项差异显著、一项不显著；能支持部分边界。 | 三个领先指标一致证明领先事件公司冲击更强。 | strong-with-qc | evidence-qc-gap | heterogeneity partly supported | table-qc | X2 |
| A038 | 自涉违规边际更强，严重程度高低均有效但差异不显著；支持有限边界。 | 自涉/严重程度机制差异稳定。 | weak | overclaim | heterogeneity evidence supports narrower claim | table-qc; sample-loss-qc | X2 |
| A039 | 融资依赖一项差异不显著、一项显著；支持有限边界。 | 高融资依赖组稳定更强。 | strong-with-qc | evidence-qc-gap | financing-dependence boundary partly supported | table-qc; citation-qc | X2 |
| A040 | 高竞争组更强但低竞争组反向显著，说明边界复杂，不能简单作为总体支持。 | 低竞争组只是不显著或较弱，而非相反方向。 | weak | contradiction | reverse direction complicates boundary interpretation | reverse-direction-qc; table-qc | X2; Y0 |
| A041 | 信息披露影响因素贡献依赖文献 gap 和 X2 成立。 | 本文确实提供新影响因素而非已有因素换场景。 | needs-external-evidence | overclaim | contribution claim requires literature verification | citation-qc; external-evidence-qc | Y0 |
| A042 | 负面信息披露/同行溢出贡献依赖外部文献边界和 X2 成立。 | 既有负面披露和同行溢出文献未覆盖相似机制。 | needs-external-evidence | evidence-qc-gap | spillover contribution requires literature verification | citation-qc; external-evidence-qc | Y0 |
| A043 | 政策建议可由发现启发，但力度应随因果/机制证据降调。 | 经验发现足以支持政策工具设计。 | weak | scope-expansion | policy implication exceeds current evidence strength | overclaim-qc | Y0 |
