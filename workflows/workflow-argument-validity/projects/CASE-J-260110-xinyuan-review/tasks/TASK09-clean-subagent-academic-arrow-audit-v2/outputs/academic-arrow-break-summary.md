# Academic Arrow Break Summary

## Status Count

| status | count | arrows |
|---|---:|---|
| strong | 1 | A022 |
| strong-with-qc | 19 | A004; A005; A008; A011; A013; A016; A017; A018; A021; A023; A024; A027; A028; A029; A031; A033; A034; A037; A039 |
| weak | 14 | A002; A003; A009; A012; A014; A015; A019; A020; A026; A030; A032; A038; A040; A043 |
| needs-qc | 3 | A025; A035; A036 |
| needs-external-evidence | 6 | A001; A006; A007; A010; A041; A042 |
| broken | 0 | none in this internal-only round |
| unclear | 0 | none separately; external-dependent arrows use `needs-external-evidence` |

## Main Break Clusters

| cluster_id | target_arrows | break_type | plain-language diagnosis | impact |
|---|---|---|---|---|
| B01 | A010; A013; A029; A035 | measurement-mismatch / evidence-qc-gap | 作者把 KV 下降直接写成披露质量提升。内部可见作者定义，但指标是否有效、量纲如何解释、DA 替代变量是否同构，都需要外部测量文献与表格 QC。 | X2; Y0 |
| B02 | A012; A025; A026; A027 | causal-leap / hidden-premise-missing / evidence-qc-gap | DID 链条有完整内部材料，但因果措辞依赖聚类层级、平行趋势、错峰 DID 方法和图表 QC。当前证据更稳地支持“方向一致的估计结果”，尚不足以无条件推出因果。 | X2; Y0 |
| B03 | A014; A030 | contradiction | 表11列(3)显示 PosCAR[-10,10] 不显著、NegCAR[-10,10] 显著，与声誉竞争机制正文叙述冲突。这是内部证据即可显影的机制断点。 | X2; Y0 |
| B04 | A032 | condition-confusion | 作者用监管距离和处罚结果不显著排除信息传导机制，但这只是不支持某些监管结果，并不充分等于“信息传导不是主要机制”。 | X2 |
| B05 | A015; A033; A034; A035; A036 | robustness-threat fit | 稳健性检验数量多，但每项是否对应核心威胁不均衡。匹配/熵平衡和共同因素排除较有帮助，Oster、替代变量、placebo 需方法与图表 QC。 | X2 |
| B06 | A037; A038; A039; A040 | heterogeneity overclaim / contradiction | 异质性结果并非全部一致。领先与融资依赖较有支持；自涉/严重程度和竞争分组更复杂，尤其低竞争组反向显著。 | X2; Y0 |
| B07 | A001; A006; A007; A041; A042 | literature gap / contribution pending | 文献 gap 和贡献上升必须外部检索才能定性。内部 citation ledger 只能证明作者如何使用文献，不能证明 gap 真实。 | X1; Y0 |
| B08 | A003; A043 | scope-expansion | 政策建议从实证发现上升到豁免/减罚、差异监管等工具，内部证据只能支持谨慎启示，不能直接推出具体政策设计。 | Y0 |

## Most Sensitive Arrows for Later Issue Selection

| arrow_id | why sensitive | current status | next needed action |
|---|---|---|---|
| A010 | Y 的测量基础；若 KV 不能代表披露质量，X2 主结论整体变弱。 | needs-external-evidence | 检索 KV 指标文献，核验替代变量 DA 是否同构。 |
| A012 | 因果识别主箭头；决定作者能否写“主动披露违规改善”。 | weak | 方法审查 DID、聚类、平行趋势、错峰处理。 |
| A014/A030 | 机制主箭头；内部已见表11冲突。 | weak | 原表逐单元格 QC；若冲突为真，重写机制结论。 |
| A025 | 聚类层级可能影响显著性可信度。 | needs-qc | 方法和稳健标准误 QC。 |
| A035/A036 | 稳健性中最依赖方法/图表的部分。 | needs-qc | 方法标准、图2和 Oster 参数 QC。 |
| A040 | 边界条件出现反向显著，影响“行业自律”叙述。 | weak | 解释低竞争组反向效应或降调边界结论。 |
| A006/A041/A042 | 贡献上升依赖文献 gap 真实性。 | needs-external-evidence | 文献谱系检索。 |
