# Academic Argument Spine

- task_id: TASK07-latest-paper-tree-regression
- mode: full-tree regression
- paper_type: empirical / quasi-experimental / DID-style Chinese management paper
- source_scope: latest restored manuscript and TASK05 restoration/table QC only
- audit_boundary: author tree only; no review attack, issue selection, or sensitivity conclusion

## One-Sentence Core Finding

本文声称：在 2007-2024 年沪深 A 股样本中，行业内事件公司主动披露违规这一冲击，会通过声誉竞争和市场压力机制促使同行业其他企业提高信息披露质量；经验上表现为多时点 DID 中 `Peerdumy x POST` 对 KV 指数显著为负，且该结论在堆叠 DID、匹配、排除共同政策因素、Oster、替代变量和重新编码 POST 等检验后仍成立。

## X / M / Y / Y2

| element | extraction |
|---|---|
| X | 行业内有上市公司主动披露违规，作者将其操作化为处理组变量 `Peerdumy` 与事后时间变量 `POST` 的交互项。 |
| M | 作者主张主要机制是声誉竞争与市场压力；信息传导给监管部门不是主要机制。 |
| Y | 同行业其他企业的信息披露质量提高，作者用 KV 指数下降表示信息披露质量提升。 |
| Y2 | 论文贡献上升为：主动披露违规不仅是事件公司个体治理行为，也可能通过市场化机制引导行业自律和提升资本市场透明度。 |

## Top-Level Author Tree

```text
Y0: 本文关于主动披露违规引导行业自律和改善信息披露质量的论文贡献成立
<- X1: 研究问题有意义，且现有文献尚未直接回答主动披露违规对同行信息披露质量的影响
<- X2: 作者声称企业主动披露违规会改善同行业其他企业的信息披露质量，并主要通过声誉竞争和市场压力引导行业自律
<- P9: 作者将经验发现上升到信息披露研究、同行溢出研究和监管政策启示
```

## X1: Research Meaning

作者用三个论证支撑研究问题：

1. 资本市场信息披露监管从事后纠偏转向事前预防，企业主动披露违规是现实中存在且具有政策意义的行为。
2. 主动披露违规对同行披露质量的方向不确定：可能激励同行改善披露，也可能引发风险规避和披露减少。
3. 既有研究主要关注监管、市场竞争、声誉约束或其他信息披露同群效应，尚未直接研究主动披露违规及其对同行披露质量的影响。

## X2: Concrete Finding

X2 不是“作者做出来了”或“核心经验发现成立”，而是以下具体 X -> Y 作者声称：

```text
行业内事件公司主动披露违规后，同行业非事件公司 KV 指数显著下降；作者据此声称企业主动披露违规改善了同行企业的信息披露质量，并通过声誉竞争和市场压力推动行业自律。机制上，声誉竞争和市场压力解释该正向溢出，而监管信息传导不是主要机制；边界上，该效应在行业领先事件公司、自涉违规、高外部融资依赖和高竞争行业中更强。
```

## Identification Design Spine

| item | author design fact |
|---|---|
| treatment / shock | 行业内有企业在未受到相关问询或处罚前主动披露违规。 |
| treated group | 主动披露违规公司所在行业的同行业其他上市公司，`Peerdumy = 1`。 |
| comparison group | 未发生符合条件主动披露违规冲击的行业/公司样本，`Peerdumy = 0`。 |
| timing | 若行业内某公司在 `t` 年主动披露违规，`POST` 在 `t` 至 `t+2` 为 1，`t-3` 至 `t-1` 为 0。 |
| sample window | 主动披露违规前 3 年、当年、后 2 年；2007-2024 年沪深 A 股。 |
| model | `KV_it = beta0 + beta1 Peerdumy_it x POST_it + controls + firm FE + year FE + epsilon_it`。 |
| fixed effects | 公司固定效应和年份固定效应；堆叠 DID 中为公司-队列和年度-队列固定效应。 |
| clustering | 基准模型公司层面聚类；堆叠 DID 公司-队列层面聚类。 |
| pretrend | 表 3 中处理前 `Peerdumy x Pre t-3` 和 `Peerdumy x Pre t-2` 不显著。 |
| placebo / robustness | 混合安慰剂 500 次、堆叠 DID、Bacon 分解、PSM/熵平衡、排除共同政策因素、Oster、替代变量 DA、重构 POST_Month。 |

## Handoff Status

- author_tree_status: full-tree produced
- edge_status_scope: `not-yet-audited` / `needs-qc` only
- ready_for_academic_arrow_audit: yes, with QC caveats about table-level visual limits and Table 11 text/table conflict
