# Academic Arrow Audit Table

本表是全量诊断层产物，不选择 major concern。

| arrow_id | 作者用 A | 推出 B | status | break_type | fallacy_label | arrow_type | why_it_breaks / holds | impact_on_X1_X2_Y | possible_revision | selection_hint |
|---|---|---|---|---|---|---|---|---|---|---|
| A006 | 作者引用既有文献覆盖信息披露质量、同行披露和负面信息披露研究 | 现有文献未直接回答主动披露违规的同行溢出问题 | unclear | evidence-qc-gap | 不当假设 | gap-contribution | TASK07 只还原了作者引用用法，未外部检索最接近文献。当前不能确认 gap 真实或不真实。 | X1/Y0 | 若作为 major，需要检索 FT50/UTD24/综合顶刊与中文核心中相近研究。 | candidate-useful |
| A008 | “无同年相关问询或处罚”的违规披露定义 | X 是主动披露违规 | weak | hidden-premise-missing | 不当假设 | treatment-definition | 定义可操作，但依赖隐含前提：未被同年问询/处罚就代表披露动机主动、且不是预期监管压力下的策略性披露。作者文本未充分说明。 | X2 | 说明识别流程、公告来源、监管滞后和策略性披露边界；可把结论降调为“较早披露/未见同年监管触发的违规披露”。 | candidate-major |
| A010 | KV 越小披露质量越高 | Y 被有效测量为信息披露质量 | weak | measurement-mismatch | 偷换概念 | construct-measure | KV 可作为披露质量代理，但它更接近交易量-收益率关系下的信息环境指标。作者把 KV 下降上升为信息披露质量提升、行业自律和透明度改善，需要额外解释代理指标边界。 | X2/Y0 | 强化 KV 与主动披露质量、同业治理改进之间的理论连接；降调宏观表述。 | candidate-major |
| A011 | 样本期、窗口、首次事件和剔除规则 | 样本适合检验同行溢出 | weak | sample-weakness | 以偏概全 | sample-mechanism-fit | 样本规则清楚，但剔除事件公司、多事件间隔过短行业、仅保留首次事件可能提升清洁度，也可能排除最有机制信息的场景。 | X2 | 报告被剔除事件/行业特征，补充含事件公司或多事件样本的边界分析。 | candidate-major |
| A012 | DID 设计、前趋势、堆叠 DID/Bacon | 可以识别 X 对 Y 的因果影响 | weak | causal-leap | 强加因果 / 另有他因 | identification-causal | 设计有 DID 元素和若干检查，但处理发生在行业层面且与行业治理环境、监管关注、共同冲击可能相关。TASK07 也标出对照组文本与 DAG-ready 信息仍 partial。 | X2/Y0 | 明确冲击外生性、对照组构造、行业趋势、聚类层级和共同冲击处理；补充 DAG 或识别假设图。 | candidate-major |
| A013 | 表4 `Peerdumy x POST` 显著为负 | 主结果支持同行披露质量提升 | weak | measurement-mismatch | 指标错配 | result-finding | 表4支持 KV 下降这一经验事实，但从 KV 下降到“信息披露质量提升”依赖 A010 的代理变量前提。若 A010 只是弱代理，A013 支持的是更窄发现。 | X2 | 结果叙述先写为 KV 指标改善，再解释为何可代表披露质量。 | candidate-major |
| A017 | POST 为 t 到 t+2，t-3 到 t-1 为前期 | 处理时点和事后窗口被正确操作化 | weak | hidden-premise-missing | 不当假设 | treatment-timing | POST 当年生效隐含同行在事件年内及时观察、理解并调整披露行为；若披露在年末发生，当年 KV 变化可能难以归因。作者虽有 POST_Month 稳健性，但主定义仍需解释。 | X2 | 说明事件日分布和年度 KV 计算窗口；主结果可补按披露月份、滞后窗口或剔除当年分析。 | candidate-useful |
| A018 | 剔除事件公司本身 | 本文聚焦同行溢出 | weak | hidden-premise-missing | 不当假设 | sample-mechanism-fit | 剔除事件公司让同行效应更纯，但也缺少事件公司自身披露质量变化作为基准，难判断同行变化是学习/竞争还是行业共同变化。 | X2 | 补充事件公司自身变化或解释为何不需要该基准。 | candidate-major |
| A025 | 公司/年份 FE、控制变量、公司层面聚类 | 模型设定适合识别 | unclear | evidence-qc-gap | 数字/统计解释不足 | identification-causal | 处理与冲击主要在行业-年份/事件层面，标准误仅公司层面聚类是否足以反映冲击相关性需要更细方法判断和表注复核。 | X2 | 说明聚类层级选择，补充行业、行业-年份或双向聚类稳健性。 | candidate-major |
| A026 | 处理前两期不显著 | 平行趋势前提可接受 | weak | hidden-premise-missing | 不当假设 | identification-causal | 事前项不显著是必要线索，但不等于平行趋势充分成立；表3还显示事后效应逐步出现，需看动态图、置信区间和处理组构造。 | X2 | 提供完整动态效应图、联合检验和处理/对照组趋势描述。 | candidate-useful |
| A027 | 堆叠 DID 和 Bacon 分解 | 异质性处理效应威胁已解决 | unclear | evidence-qc-gap | 不当假设 | identification-causal | 堆叠 DID 结果有支持，但 Bacon 图未视觉核验；作者文字称负权重问题较小，仍需确认分解细节和队列构造。 | X2 | 视觉复核 Bacon 图和堆叠 DID 设定，报告队列构造与权重。 | candidate-useful |
| A028 | 表4核心交互项显著为负 | 基准经验结果成立 | strong-with-qc |  |  | result-finding | 在 TASK07 抽取表4信息下，系数方向和显著性与作者声称一致。仍需表格 cell-level QC 后用于正式文本。 | X2 | 保留为经验事实：`Peerdumy x POST` 与 KV 下降相关。 | no-issue |
| A029 | `0.0111 / 0.1159 ≈ 9.58%` | 结果具有经济意义 | weak | numerical-trap | 数字谬误 | result-finding | 计算本身清楚，但读者需要知道 KV 的单位和基准含义。将“KV 均值 9.58%”直接解释为“信息披露质量平均提升 9.58%”容易跨指标。 | X2/Y0 | 明确这是相对 KV 均值的变化，不是披露质量本身提升 9.58%。 | candidate-useful |
| A030 | CAR 正反分组和表11 | 声誉竞争机制成立 | broken/needs-table-qc | contradiction | 自相矛盾 | mechanism-claim | TASK07 记录表11列(3)与正文叙述冲突：PosCAR[-10,10] 不显著而 NegCAR[-10,10] 显著。若表格无误，机制叙述至少不稳定。 | X2 | 先做表11 cell-level QC；若确认冲突，修正文中机制解释并重新组织机制证据。 | candidate-major |
| A031 | 高投资者关注/高分析师关注组效应更强 | 市场压力机制成立 | weak | hidden-premise-missing | 不当假设 | mechanism-claim | 分组异质性支持“关注度高时效应更强”，但它也可能反映信息环境、企业规模或治理差异，不自动等于市场压力机制。 | X2 | 补充机制变量变化、关注变化或替代解释排除。 | candidate-useful |
| A032 | 监管距离、处罚次数、处罚严重程度不显著 | 信息传导不是主要机制 | weak | alternative-explanation | 另有他因 | mechanism-claim | 不显著结果不能充分证明信息传导机制不存在；处罚结果可能受监管资源、滞后、样本和测量误差影响。 | X2 | 将表述降调为“未发现支持信息传导机制的证据”，而不是排除该机制。 | candidate-major |
| A033 | PSM 和熵平衡后结果仍显著 | 样本可比性威胁已回应 | weak | robustness-threat-mismatch | 不当假设 | robustness-threat | 匹配回应可观测协变量差异，但不能回应主动披露冲击内生性、行业共同冲击或处理定义问题。 | X2 | 明确匹配只能缓解 observables；补充针对核心威胁的识别或敏感性分析。 | candidate-useful |
| A034 | 剔除分行业信息披露指引样本 | 共同政策因素不驱动结果 | weak | robustness-threat-mismatch | 另有他因 | robustness-threat | 该检验只回应一种共同政策因素，不能排除行业层面的其他共同冲击或监管关注变化。 | X2 | 扩展共同冲击控制或更窄地表述该稳健性。 | candidate-useful |
| A035 | Oster、DA、POST_Month | 遗漏变量、替代测量和时点设定威胁已回应 | weak | robustness-threat-mismatch | 不当假设 | robustness-threat | 三类稳健性分别回应不同威胁，但仍未直接回应处理定义、样本筛选、行业层面聚类和机制一致性问题。 | X2 | 将稳健性按 threat map 展示，避免笼统称“结论稳健”。 | candidate-major |
| A036 | placebo 图和 p 值 | 随机伪处理/遗漏政策影响可排除 | unclear | evidence-qc-gap | 数字谬误 | robustness-threat | 图2未精准视觉复核，且右尾/左尾 p 值解释需清楚。当前可作为待核验支持，不能作为强排除证据。 | X2 | 做 figure QC，说明 p 值方向和检验目标。 | candidate-useful |
| A039 | 公司外部融资依赖分组 | 融资依赖越高效应越强 | weak | concept-mismatch | 概念错配 | mechanism-claim | 作者借 Rajan-Zingales 思路，但 TASK07 显示其操作化为公司层面指标。若原构念偏行业长期外部融资依赖，需要解释公司年度化适配。 | X2 | 说明为何公司层面 Rely1/Rely2 能承接该构念，或降调为样本内财务约束异质性。 | candidate-major |
| A040 | 行业竞争高低分组 | 高竞争行业中效应更强 | mixed | overclaim | 过度推理 | mechanism-claim | 高竞争组结果支持作者方向，但低竞争组为正且显著，说明边界不仅是“更弱”，而可能是反向机制。 | X2/Y0 | 正面解释低竞争组反向结果，作为边界条件而非只写强化机制。 | candidate-useful |
| A041 | 将主动披露违规与企业违规纳入同一框架 | 贡献于信息披露影响因素研究 | weak | overclaim | 过度推理 | finding-contribution | 若识别和构念前提只是局部成立，贡献应限于特定违规披露冲击下的同行 KV 反应，而非广泛影响因素框架。 | Y0 | 收窄贡献边界，突出场景和机制条件。 | candidate-useful |
| A042 | 将主动披露违规从个体治理引申到行业披露决策 | 贡献于负面信息披露和同行溢出研究 | unclear | evidence-qc-gap | 不当假设 | finding-contribution | 需要外部文献检索确认最接近研究是否已经覆盖“负面披露-同行披露行为”链条。本轮只能标为待检索。 | X1/Y0 | 调用 literature search 建知识树后再判断 gap 强弱。 | candidate-useful |
| A043 | 经验发现和机制结果 | 鼓励主动披露、强化市场监督、差异监管 | weak | scope-expansion | 以偏概全 | finding-contribution | 政策建议依赖因果识别、主动性定义和福利判断。如果主动披露可能是策略性披露，鼓励机制需要更谨慎。 | Y0 | 政策建议降调，区分真实主动纠错与策略性披露，并说明监管豁免边界。 | candidate-major |

