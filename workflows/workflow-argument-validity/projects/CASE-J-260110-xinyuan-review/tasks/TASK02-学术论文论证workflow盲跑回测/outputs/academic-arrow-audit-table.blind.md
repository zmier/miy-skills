# Academic Arrow Audit Table Blind Run

状态：`review-frozen / manuscript-only / annotation-contaminated`

## 边界

本文件消费 `paper-argument-tree.blind.md`，只做全量验箭头，不选择 major concern。

## 箭头审计表

| arrow_id | from_node A | to_node B | status | break_type | arrow_type | why_it_breaks | impact_on_X1_X2_Y | selection_hint |
|---|---|---|---|---|---|---|---|---|
| A1 | 既有研究未关注主动披露违规对同行信息披露质量的影响 | 本文存在真实且重要的 gap | weak | gap-overclaim / literature-boundary-qc | gap -> contribution | 引言承认已有信息披露同群、负面信息披露、违规溢出等相邻研究；作者需要更清楚说明“主动披露违规”与既有同群/负面披露/违规传染文献的不可替代差异。 | X1 | candidate-useful |
| A2 | 主动披露违规可能传递诚信信号、获得市场认可 | 同行会因声誉竞争提升信息披露质量 | weak | hidden premise missing | theory -> mechanism | 理论链需要证明事件公司主动披露违规确实被市场解释为“诚信”而非策略性披露或风险暴露；作者后文有 CAR 支持，但理论部分的正负机制转换仍较快。 | X2 | candidate-major |
| A3 | 市场压力使同行受到更多关注 | 同行会主动提升信息披露质量 | weak | causal mechanism under-specified | theory -> mechanism | 外部关注可能促使企业提升披露，也可能促使企业降低风险暴露或保守披露；作者需要说明为何压力转化为质量提升而非沉默或策略披露。 | X2 | candidate-major |
| A4 | KV 指数可反映投资者关于信息不对称程度的客观评价 | KV 下降等于信息披露质量提高 | unclear | construct-measure fit | construct -> measure | KV 更接近交易量-收益关系中的信息不对称/交易反应指标；它能否直接代表“信息披露质量”尤其是文本透明度、及时性、完整性，需要更充分辩护。 | X2/Y | candidate-major |
| A5 | 企业当年披露违规且无问询或处罚 | 该行为可定义为“主动披露违规” | weak | treatment-definition ambiguity | treatment definition -> X | “无问询或处罚”只能排除部分外部强制情形，未必能证明披露真正主动；披露时点、监管线索、媒体关注、内部调查等前置压力可能影响主动性。 | X2 | candidate-major |
| A6 | 剔除事件公司自身、保留同行业其他企业 | 样本代表同行溢出效应 | weak | sample-mechanism fit | sample rule -> mechanism-relevant sample | 剔除事件公司自身有助于观察同行，但样本筛选是否同时排除了最能说明机制的事件或造成选择性样本，需要更多说明。 | X2 | candidate-useful |
| A7 | Pre 系数不显著、After 系数显著为负 | 平行趋势成立且 DID 有效 | weak | identification assumption | model/result -> causal claim | Pre 不显著是必要但不充分证据；多时点 DID 还依赖无同步冲击、处理时点可比、行业层面事件不与其他政策/监管变化混同。 | X2 | candidate-major |
| A8 | 表4 中 Peerdumy×POST 系数显著为负 | 主动披露违规导致同行信息披露质量提升 | weak | causal leap | result -> causal claim | 回归显著说明处理组在事件后 KV 下降，但从相关变化上升为因果仍依赖处理定义、行业冲击排除、样本选择和平行趋势等前提共同成立。 | X2 | candidate-major |
| A9 | 堆叠 DID、Bacon、安慰剂、PSM/熵平衡、政策剔除、Oster、替换变量均支持 | 稳健性回应核心威胁 | unclear | robustness-threat fit | robustness -> core threat addressed | 这些检验覆盖面广，但是否针对最核心威胁：主动披露事件内生性、行业共同冲击、处理定义主动性、KV 构念适配，仍需逐项对应说明。 | X2 | candidate-major |
| A10 | 正 CAR 组效应显著、负 CAR 组不显著 | 声誉竞争机制成立 | weak | mechanism identification | mechanism test -> mechanism claim | 正 CAR 组结果支持“市场正向反应相关”，但声誉竞争还需证明同行观察到并因竞争地位而提升披露；CAR 分组不完全等同于声誉竞争机制。 | X2 | candidate-major |
| A11 | 高投资者/分析师关注组效应更强 | 市场压力机制成立 | weak | mechanism proxy fit | mechanism test -> mechanism claim | 投资者关注和分析师关注也可能代表信息环境、公司规模、治理水平或融资需求差异；需说明为何这是市场压力而非其他异质性。 | X2 | candidate-useful |
| A12 | 监管距离和处罚检验不支持 | 信息传导机制不成立 | weak | exclusion-mechanism ambiguity | mechanism exclusion -> mechanism claim | 不显著结果未必足以排除信息传导；监管距离、处罚次数和严重程度能否捕捉监管效率提升需要辩护。 | X2 | candidate-useful |
| A13 | 行业领先、自涉违规、外部融资依赖、行业竞争结果 | 机制和边界条件更完整 | weak | heterogeneous interpretation | heterogeneity -> theory | 异质性结果有助解释，但部分变量可能同时承载规模、可见度、融资需求、竞争结构等多重含义，需避免过度机制化解释。 | X2/Y | candidate-useful |
| A14 | 主结果和机制检验 | 主动披露违规可以引导行业自律发展 | broken | overclaim | result -> broad contribution | 结果显示同行 KV 指标改善，不必然等于“行业自律发展”；行业自律是更宏观、更长期、更制度化的概念，需要更谨慎表述或更多证据。 | Y | candidate-major |
| A15 | 研究发现正向溢出 | 监管应鼓励主动披露、设立豁免或减轻处罚机制 | weak | policy overextension | evidence -> policy implication | 从同行披露质量改善到具体监管激励制度仍有距离；还需考虑策略性披露、违规严重性、道德风险和监管公平。 | Y | candidate-useful |

## 候选总结

高优先候选：

```text
A4, A5, A7/A8/A9, A10, A14
```

中优先候选：

```text
A1, A3, A6, A11, A12, A13, A15
```
