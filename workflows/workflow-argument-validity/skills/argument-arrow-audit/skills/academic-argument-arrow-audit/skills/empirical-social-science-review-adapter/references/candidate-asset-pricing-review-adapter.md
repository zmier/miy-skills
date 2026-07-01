---
type: candidate-domain-adapter
status: draft / forward-test-pending
parent_adapter: empirical-social-science-review-adapter
source_project: SMK/0 学术体系/实证资产定价-横截面股票收益
created: 2026-06-25
---

# Candidate Asset Pricing Review Adapter

## 定位

这是 `empirical-social-science-review-adapter` 下的资产定价 / 实证金融候选领域适配器。

当前状态不是可调用子 Skill，而是候选 reference。它用于记录在学习 *Empirical Asset Pricing: The Cross Section of Stock Returns* 过程中，逐步形成的资产定价论文拆箭头敏感点。

升级为子 Skill 的条件：

```text
Ch.1-Ch.6 方法框架学习完成
→ 至少形成一批稳定 asset-pricing arrow types
→ 在一篇未参与提炼的资产定价论文或审稿任务中 forward-test
→ 再创建 skills/asset-pricing-review-adapter/SKILL.md
```

## 适用对象

- 横截面资产定价论文；
- return predictor / anomaly / factor 研究；
- portfolio sort、Fama-MacBeth regression、factor alpha、risk adjustment、mechanism / trading friction 解释；
- A 股或其他市场的资产定价实证研究。

## 候选拆箭头

| 通用箭头 | 资产定价适配 | 当前学习来源 | 候选断点 |
|---|---|---|---|
| sample -> target population | 样本构造能否支持“市场/股票总体”结论 | Ch.1 sample | 非平衡 panel、上市/退市/停牌/ST/新股筛选导致样本偏 |
| variable availability -> factor interpretation | 因子变量可得样本能否代表因子本身 | Ch.1 missingness | 缺失值不是随机小麻烦，变量覆盖范围可能改变研究对象 |
| predictor -> future return | predictor 能否支持收益预测声称 | Ch.1 sample; Ch.5/Ch.6 待回收 | 样本口径、未来收益可得性、持有期和交易约束未说明 |
| control set -> independent factor effect | 控制变量后核心因子是否仍有独立信息 | Ch.1 sample; Ch.3/Ch.6 待回收 | 控制变量吸收核心效应，或控制变量本身是机制/bad control |
| portfolio sort -> premium claim | 排序组合收益能否支持因子溢价声称 | Ch.5 待回收 | 分组、breakpoints、权重、再平衡频率和极端值处理影响结论 |
| Fama-MacBeth coefficient -> pricing claim | FM 系数能否支持横截面定价结论 | Ch.6 待回收 | 线性设定、控制变量、标准误、时间序列相关和经济含义未充分说明 |
| alpha -> anomaly claim | 风险调整 alpha 能否支持 anomaly 声称 | Ch.5/Part II 待回收 | 因子模型不足、风险暴露未解释、alpha 不等于可交易收益 |
| statistical significance -> tradable conclusion | 显著性是否足以支持可交易/实盘结论 | Ch.1/Ch.5 待回收 | 手续费、滑点、涨跌停、停牌、容量和可做空约束未处理 |

## 当前已确认候选规则

### 1. 缺失值可能断开 `sample -> target population`

若某资产定价论文用某个数据源或因子变量覆盖的股票样本，推出对“市场股票总体”的结论，需要检查变量缺失是否随机。

中文审稿表达模板：

```text
作者想由当前样本中的显著结果推出该因子在目标市场中普遍有效。
但样本进入条件本身可能已经筛掉了停牌、新股、低流动性或数据覆盖不足的股票。
因此，当前结果至少还需要说明保留样本与被剔除样本在市值、流动性、过去收益和交易状态上的差异。
否则，结论更稳妥地说，应限于数据覆盖充分且可交易性较好的股票。
```

### 2. 控制变量可能断开 `predictor -> independent effect`

若核心 predictor 在简单模型中显著，但加入市值、换手率、过去收益等控制变量后消失，不能直接得出“因子无效”或“因子有效”的单一结论。

需要区分：

```text
样本变化
控制变量吸收
核心 predictor 本身无稳定信息
```

中文审稿表达模板：

```text
作者将核心变量的显著系数解释为独立的资产定价效应。
但该变量可能与市值、换手率或过去收益高度重合。
如果控制这些变量后系数明显衰减或不再显著，当前证据更像是在说明核心变量捕捉了这些已知特征的一部分，而不是提供了独立的新因子。
作者需要进一步报告相关性、同样本估计和控制变量加入前后的系数变化，才能支撑独立效应声称。
```

### 3. 数据覆盖可能把 factor claim 收窄成 active-stock claim

若某个因子变量只在成交活跃、信息关注高或数据源覆盖充分的股票上可得，那么缺失值不是随机损耗，而可能改变研究对象。

典型箭头：

```text
热榜覆盖样本中的显著结果
→ 热榜注意力因子在目标市场中有效
```

可疑处：

```text
热榜覆盖样本
可能已经是活跃股票子样本
不等于全市场股票样本
```

需要检查：

```text
保留样本 vs 缺失样本：
市值
换手率
成交额
过去涨幅
停牌/涨跌停状态
上市时长
ST/退市风险
```

中文审稿表达模板：

```text
作者将热榜变量的显著结果解释为注意力因子的资产定价效应。
但如果热榜数据本身主要覆盖成交活跃或市场关注度较高的股票，当前样本就可能已经排除了低活跃、低关注或交易受限的股票。
在这种情况下，结果未必能支持“热榜注意力因子对市场股票普遍有效”的结论；它也可能只是说明，在活跃股票子样本中，热榜变量与未来收益存在关系。
作者需要比较热榜覆盖样本与未覆盖样本的市值、换手率、成交额、过去收益和交易状态，并说明结论应外推到全市场，还是仅限于热榜数据可覆盖的活跃股票。
```

## 待回收章节

- Ch.2 Summary Statistics：变量分布、偏态、极端值对 factor meaning 的影响；
- Ch.3 Correlation：Pearson/Spearman、predictor overlap、控制变量选择；
- Ch.4 Persistence：predictor 是否稳定到足以支持持有期/交易解释；
- Ch.5 Portfolio Analysis：sort、breakpoints、long-short、risk adjustment；
- Ch.6 Fama-MacBeth：控制变量、线性设定、系数时间序列推断。

## 边界

- 本文件不保存 A 股实盘结论；
- 不把教材美股结论写成资产定价论文审稿规则；
- 当前只记录候选拆箭头类型，不能替代具体论文的 evidence ledger；
- 使用时必须绑定具体稿件中的 `target_arrow_id`、`evidence_ids` 和作者声称。
