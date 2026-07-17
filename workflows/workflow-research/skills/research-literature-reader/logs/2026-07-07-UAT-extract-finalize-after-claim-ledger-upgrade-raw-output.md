# UAT Raw Output: extract -> finalize after claim-ledger upgrade

- Date: 2026-07-07
- UAT type: black-box / gray-box
- SubAgent: `019f3b6e-8248-77c3-a7b6-5ff7bb24ca5f`
- Task: run `paper-extract -> paper-finalize` from the public entry Skill and original manuscript only.
- Isolation instruction: do not read `logs/`, existing outputs, or this thread's prior analysis.
- File status: this file records the SubAgent's raw returned content, without main-agent evaluation.

## SubAgent Raw Result

以下是按 `paper-extract -> paper-finalize` 路径、基于原始 `manuscript_paragraphs.md` 黑箱/灰箱执行后，我会交付给用户的内容与拟写入文件草案。未修改任何文件。

## 1. 我会返回给用户的内容

已完成这篇论文的自动抽取与 cold-start finalization 草案。核心结论是：Fang, Peress, and Zheng (2014) 认为，即使是专业基金经理也会受有限注意力影响；大众媒体报道会把股票推入基金经理的注意范围，主要诱发买入而非卖出；更强的买入媒体报道股票倾向与未来基金业绩较差相关。

本轮没有进入共同阅读环节，因此 `discussion-outline.md` 未生成。由于本轮只核验了 `manuscript_paragraphs.md`，而表格在该 Markdown 中被压成普通段落，精确系数、t 值、R2、样本量等只标为 `needs-source-check` 或 `verified-citable-directional-result`，不直接升级为 PDF 级 `verified-citable-table-value`。正文明确陈述的核心发现、数据来源、变量构造和主要方向性结果可以进入正式文献库，但精确表格值建议后续回 PDF/表格源再核一次。

---

## 2. automatic-extraction.md 草案

```markdown
# Does Media Coverage of Stocks Affect Mutual Funds’ Trading and Performance? - 自动抽取

## 来源

- 论文：Lily H. Fang, Joel Peress, Lu Zheng, "Does Media Coverage of Stocks Affect Mutual Funds’ Trading and Performance?", Review of Financial Studies, 2014.
- PDF：未直接读取；本轮使用带 PDF page marker 的 Markdown 段落稿。
- Markdown 底稿：/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/PDFs/基金经理/RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/1-md/manuscript_paragraphs.md
- 阅读底稿状态：rough reading draft；正文可读，表格被压入普通段落，table-leak high risk for exact values。
- 当前项目：260521-基金经理研究
- 当前 task / route：paper-extract -> paper-finalize；正式文献库草案；不进入共同阅读。
- 创建时间：2026-07-07
- 最近更新：2026-07-07

## 抽取状态

- 抽取范围：全文正文、表格标题与表格段落、公式段落、结论、参考文献。
- source anchors 质量：段落锚点 `[para x]` 可用；PDF page marker 可辅助定位；表格结构不稳定。
- 表格 / 图片可靠性：表格文字可粗核方向和变量；精确系数、t-stat、R2、样本量需回 PDF/表格源核验。
- 未回原文核对前不可引用：所有精确表格值、公式符号细节、未报告 robustness。
- 剩余风险：Markdown 合并了脚注、页眉、表格与正文；部分公式存在 OCR/编码噪声。

## A01 核心断言与形式逻辑

### 一句话核心发现：理论纯净版

专业投资者也受有限注意力约束；外部注意力触发会系统性影响其交易选择，并且由注意力而非优势信息驱动的交易倾向会预测较差的未来投资表现。

### 一句话核心发现：读者导览版

大众媒体报道会把股票推入共同基金经理的注意范围，基金经理更倾向买入被报道股票；基金层面越偏好买入媒体报道股票，未来业绩越差，而卖出端关系弱得多。

### 形式逻辑完整还原

若基金经理存在有限注意力，则媒体报道作为注意力触发会降低搜索成本并影响其交易集合选择；由于该交易不是优势信息驱动，媒体驱动买入倾向越强，未来业绩应越差；由于共同基金通常不能卖空，媒体影响应在买入端强于卖出端。

### 核心命题准入测试

| 候选命题 | Collapse Test | Take-Away Test | Independence Test | 判定为 P / S / candidate | 理由 |
|---|---|---|---|---|---|
| 专业基金经理受有限注意力影响，媒体报道影响交易 | 通过 | 通过 | 通过 | P1 | 删除后论文贡献塌缩；对应交易行为主结果。 |
| 媒体驱动买入倾向越强，未来基金业绩越差 | 通过 | 通过 | 通过 | P2 | 删除后论文从交易现象降为行为描述，失去绩效含义。 |
| 买入端强于卖出端 | 部分通过 | 主要服务 P1/P2 | 非独立 | S-P1/P2-boundary | 是有限注意力机制下的边界/诊断模式。 |
| 不是 flow catering 或新闻内容/RPI | 不通过 | 支撑主张 | 非独立 | S-P2-exclusion | 服务于排除替代解释。 |
| 经理更换后 propensity 下降 | 不通过 | 支撑机制 | 非独立 | S-P1-mechanism | 支撑“attention 是经理特征”的解释。 |

### 命题登记表

| ID | 角色 | 分支类型 | 命题 / 支撑判断 | 服务对象 | 状态 | Source Anchors | 备注 |
|---|---|---|---|---|---|---|---|
| P1 | 核心命题 | core proposition | 媒体报道作为注意力触发会影响基金经理交易，尤其是买入。 | self | first-pass | para 8-12, 51-56, 62 | 观察性面板证据。 |
| P2 | 核心命题 | core proposition | 基金经理买入媒体报道股票的倾向越强，未来基金业绩越差。 | self | first-pass | para 13, 90-99, 143 | 预测关系，不宜表述为严格因果。 |
| S-P1-boundary | 支撑分支 | boundary / diagnostic | 由于不能卖空和买入搜索空间更大，媒体影响应在买入端强于卖出端。 | P1/P2 | first-pass | para 10-11, 55-56, 98-99 | 买卖差异是机制诊断。 |
| S-P2-exclusion-flow | 支撑分支 | exclusion | 未来资金流不响应基金买入媒体报道股票，削弱 flow-catering 解释。 | P2 | first-pass | para 14, 104-114 | 精确表值待核。 |
| S-P2-exclusion-content | 支撑分支 | exclusion | PROPENSITY_BUY_MEDIA 比基于新闻方向的 mass media RPI 更能预测业绩。 | P2 | first-pass | para 115-123, 131-137 | 支持 coverage 而非 content 解释。 |
| S-P1-mechanism-manager | 支撑分支 | mechanism | 经理更换伴随买入媒体倾向下降，符合该倾向是经理特征。 | P1 | first-pass | para 137-141 | 单经理基金样本。 |

## A02 论证结构 / 理论关系

| 命题 ID | Pi-X | Pi-Y | Pi-R | Pi-KB | Source Anchors | 需要回原文核对 |
|---|---|---|---|---|---|---|
| P1 | 有限注意力、搜索成本、注意力触发 | 基金经理交易选择 | 注意力触发降低搜索成本，使被触发对象更可能进入交易集合；买入端更强 | 个人投资者 attention literature；专业投资者可能不受影响的 null | para 4-11, 16-20 | PDF 不必；表格细节需核 |
| P2 | 注意力驱动而非优势信息驱动的交易倾向 | 未来投资表现 | 越依赖注意力触发买入，未来表现越差 | RPI/公开信息依赖与基金表现文献；有限注意力 | para 10, 13, 19-20, 90-99 | 表 9 精确值需核 |
| S-P1/P2-boundary | 买入集合搜索成本大于卖出集合 | 买卖端媒体影响差异 | 媒体影响买入强于卖出 | 共同基金不能卖空 | para 10-11, 55-56 | 表 4/9 精确值需核 |

## A03 操作化 / Proxy Bridge

| Bridge ID | A02 对象 / 关系 | 经验 proxy / 测量 / 经验关系 | 代理资格 / warrant | 支持证据 / 诊断 / 排除检验 | 剩余威胁 / 竞争解释 | Source Anchors | 后续议程 |
|---|---|---|---|---|---|---|---|
| A03-P1-X | 注意力触发 | 股票上一期媒体报道数量、覆盖类型、是否被报道、高报道指示 | 大众媒体覆盖把股票推入投资者 radar screen；覆盖量代理 attention | 买入端对滞后媒体覆盖显著正向；正负报道均触发交易 | 媒体报道可能含信息而非纯注意力 | para 9-15, 51-56, 123-137 | A05/A07 |
| A03-P1-Y | 交易选择 | 基金季度持仓变化推断的 buys/sells，按 TNA 缩放 | 持仓变化可反映净交易 | 表 3/4；Abel Noser 日频辅助 | 季度持仓看不到日内或季内反转；无法观察未持有股票卖空 | para 27-28, 45, 48, 51-58 | A04/A05 |
| A03-P1-R | 媒体触发影响交易 | 滞后媒体覆盖对买入/卖出的回归关系 | 滞后设置缓解交易导致报道的反向解释 | Table 4 买入显著、卖出不显著；Table 5 日频机构交易 | 观察性相关；媒体覆盖与基本面信息共变 | para 51-56, 64-66 | A07 |
| A03-P2-X | 注意力驱动买入倾向 | PROPENSITY_BUY_MEDIA：基金-季度层面媒体覆盖 beta 的四季度精度加权平均 | 捕捉基金对媒体报道股票的稳定买入倾向 | 该指标有持续性；与其他基金特征相关性弱 | 可能混入风格、公开信息依赖、技能差异 | para 63-78 | A04/A05 |
| A03-P2-Y | 未来投资表现 | CAPM alpha、FF3 alpha、Carhart4 alpha、conditional 4-factor alpha、manipulation-proof measure | 多种业绩指标覆盖常用基金绩效评价 | 结果跨指标为负 | 仍是预测关系；未证明单笔交易导致低绩效 | para 90-99 | A06/A07 |
| A03-P2-R | 买入媒体倾向预测业绩 | PROPENSITY decile 对下一季度业绩的面板回归 | decile 降噪；控制基金特征和年份 | Table 9；Table 11/12 horse race | 可能存在未观测基金质量或策略差异 | para 94-102, 115-123 | A07 |

## A04 测量与数据构造

| Block ID | 服务的 Pi-R | 关联 A03 Bridges | 分析单位 | 样本 / 窗口 | 来自 A03 的核心测量 | 本 Block 的设计支撑测量 | 测量 / 数据风险 | Source Anchors |
|---|---|---|---|---|---|---|---|---|
| A04-P1-R | P1-R | A03-P1-X; A03-P1-Y; A03-P1-R | stock-fund-quarter；aggregate stock-quarter | 1993-2002；NYSE 全部股票 + 随机 500 NASDAQ；开放式美国国内权益基金 | LexisNexis 四大报纸报道数；季度基金 buys/sells | stock turnover, size, size², B/M, past return, quarter FE, fund FE | 媒体样本非全市场；持仓频率季度；表格精确值待核 | para 21-28, 45, 51-55 |
| A04-P2-R | P2-R | A03-P2-X; A03-P2-Y; A03-P2-R | fund-quarter / fund-month performance | 同上；业绩按未来季度/月度度量 | PROPENSITY_BUY_MEDIA/SELL_MEDIA；五类 performance measures | fund size, family size, expense, turnover, age, style indicators, average firm size, year FE | propensity 估计噪声；alpha 模型选择；基金样本偏大偏老 | para 63-78, 90-102 |
| A04-S-exclusion | S-P2-exclusion | A03-P2-R | fund-quarter / institutional stock-day | flow test；RPI；signed media；manager turnover | New Money Growth；RPI decile；Mass media RPI；manager change | alpha lags, controls, FE, DGTW adjusted returns | 新闻 tone 用股价反应代理；manager turnover 样本限制 | para 104-141 |

## A05 研究设计 / 识别策略

| Design ID | 关联 A04 Block | 命题 ID | 被检验的 Pi-R | 研究方式 | 经验检验 / 模型 / 比较逻辑 | 时间顺序 | 变量的设计功能 | 识别主张 | 关键假设 / 威胁 | Source Anchors |
|---|---|---|---|---|---|---|---|---|---|---|
| A05-P1-R | A04-P1-R | P1 | 注意力触发影响基金交易 | 观察性面板回归 + 单变量比较 | funds buys/sells on lagged media coverage and controls | 媒体覆盖滞后一季；交易在下一季 | 媒体变量为 attention trigger；controls 处理规模、流动性、估值、动量；FE 控制季度和基金异质性 | descriptive association / mechanism-consistent evidence | 媒体可能同时反映信息；季度持仓低频 | para 48-56 |
| A05-P2-R | A04-P2-R | P2 | 买入媒体倾向预测未来业绩 | 预测面板回归 | future fund performance on PROPENSITY decile + controls | propensity 滞后一季；业绩为未来表现 | decile 降估计噪声；基金控制变量减少混淆 | predictive relation / exclusion-enhanced explanation | 未证明因果；未观测基金能力仍可能残留 | para 90-102 |
| A05-S-exclusion | A04-S-exclusion | S-P2-exclusion | 排除 flow catering / RPI / content | horse race 与替代解释检验 | fund flow regression；RPI control；signed media RPI；manager turnover | 替代解释变量滞后或同步构造 | 判断 coverage attention 是否强于内容/公开信息/客户流量解释 | mechanism-consistent evidence | tone 代理粗糙；unreported tests 不可核 | para 104-141 |

## A06 资料分析 / 经验结果

| Result ID | 命题 ID | 被检验关系 | 主要结果 | 方向是否符合理论 | 统计意义 | 经济 / 实质意义 | 在论证中的角色 | Source Anchors |
|---|---|---|---|---|---|---|---|---|
| A06-P1-R | P1 | 媒体覆盖 -> 基金买入/卖出 | 控制后买入与媒体覆盖正相关；卖出不显著 | 是 | 方向性已由正文核验；精确值待 PDF | 支持买入端注意力效应 | 主证据 | para 51-56 |
| A06-P1-daily | P1 | 日频机构交易与媒体覆盖 | 日频机构买入和卖出均受媒体覆盖影响 | 部分符合 | 表 5 精确值待核 | 说明机构类型异质性和季内反转可能 | 辅助证据 | para 57-62, 65-66 |
| A06-P2-R | P2 | PROPENSITY_BUY_MEDIA -> 未来业绩 | 买入 propensity decile 与五类未来绩效均显著负相关；卖出无类似关系 | 是 | 方向性已核；系数精确值待 PDF | 高低 decile 年化差约 1.1%-2.8% | 主证据 | para 94-102 |
| A06-S-persistence | S-P1-mechanism | propensity 持续性 | 买入 propensity 三年后仍有差异；卖出不持续 | 是 | 方向性已核 | 支持经理特征解释 | 机制/诊断 | para 78-90 |
| A06-S-exclusion | S-P2-exclusion | flow/RPI/content 替代解释 | flow-catering 不获支持；PROPENSITY 不被 RPI 或 signed media RPI 吸收 | 是 | 方向性已核 | 强化 limited attention 解释 | 排除性证据 | para 104-137 |
| A06-S-manager | S-P1-mechanism | manager turnover -> propensity change | 经理更换后买入 propensity rank 下降 | 是 | 精确表值待核 | 支持 propensity 是 manager characteristic | 机制证据 | para 137-141 |

## A07 替代解释 / 稳健性 / 有效性威胁

| Threat ID | 服务命题 | 威胁 / 替代解释 | 作者检验 / 回应 | 有效性类型 | 是否解决 | 剩余风险 | Source Anchors |
|---|---|---|---|---|---|---|---|
| A07-P1-1 | P1 | 媒体覆盖只是信息含量而非注意力 | signed media / tone 检验；正负报道均带来更多交易 | construct / internal | partially resolved | tone 用收益代理，不是文本分析 | para 115-137 |
| A07-P1-2 | P1 | 交易导致媒体报道 | 使用滞后媒体覆盖；不含 contemporaneous coverage；稳健性称加入 contemporaneous 后类似 | internal | partially resolved | 未报告检验不可核 | para 64 |
| A07-P2-1 | P2 | 高 propensity 只是公开信息依赖 RPI | 控制 Kacperczyk-Seru RPI 后 PROPENSITY_BUY_MEDIA 仍显著 | internal / construct | partially resolved | RPI 数据外部共享，细节需核 | para 115, 122 |
| A07-P2-2 | P2 | 基金经理为迎合投资者资金流而买媒体股票 | future flow 对买入股票媒体覆盖不显著 | internal | partially resolved | 对 winner stocks 的特例仍存在 | para 104-114, 119-120 |
| A07-P2-3 | P2 | 低业绩来自基金风格/特征 | 控制基金规模、家族规模、费用、换手、年龄、风格、持仓平均规模 | internal | partially resolved | 未观测能力/策略仍可能残留 | para 95-102 |
| A07-P-all-1 | P1/P2 | 样本代表性 | 与 CRSP fund universe 比较；控制差异 | external | partially resolved | 样本偏大、偏老；媒体股票覆盖不全 | para 43-45 |

## A08 迁移到当前项目

- 可直接复用：用“行为倾向 proxy -> 未来业绩”的两阶段设计；先用个体层面行为回归估计风格/倾向，再用该倾向预测未来表现。
- 需要改造：媒体报道可替换为中国语境下的财经媒体、研报、社媒热度、平台曝光、公告关注度等 attention trigger；基金经理交易需用可得持仓或交易数据代理。
- 不可迁移：美国共同基金不能卖空的制度解释不能直接套用中国公募/私募或不同交易约束；四大美国报纸覆盖不能直接替代中文信息环境。
- 当前已有数据：未知；本轮未读项目数据文档。
- 仍需补充数据：基金持仓变动、基金经理/基金特征、媒体/关注度数据、未来业绩指标、风格/基准数据、资金流。
- 测量启发：为每个基金经理构造“买入高关注资产倾向”；做 shrinkage/rolling estimator；区分买入与卖出。
- 识别威胁：attention proxy 与信息含量、流动性、规模、动量、市场热点高度共变；业绩预测不是因果识别。
- route mapping：支持“基金经理有限注意力/追热点行为影响业绩”的 candidate route；更适合作为行为特征测量和机制证据，不宜直接作为因果设计模板。
- 下一步深读 / source-check 位置：Table 4, 9, 10-14；Equation (2)-(4)；数据筛选 para 21-28, 43-45。

## 开放问题

| ID | 问题 | 服务对象 | 是否需要回原文核对 | 备注 |
|---|---|---|---|---|
| Q1 | 精确系数、t-stat、R2、样本量是否与 PDF 表格一致？ | A06/A07 | 是 | Markdown 表格泄漏。 |
| Q2 | PROPENSITY 公式在 PDF 中的分母/权重是否完整？ | A04-P2 | 是 | 段落稿公式 OCR 噪声。 |
| Q3 | 作者所有 robustness 是否只在正文提及而未报告？ | A07 | 是 | para 64, 119-120, 127-130 有 unreported analysis。 |
| Q4 | 项目中可得交易数据是持仓级、成交级还是净值级？ | A08 | 否，需读项目数据 | 决定迁移可行性。 |
```

---

## 3. final-literature-note.md 草案

```markdown
# Does Media Coverage of Stocks Affect Mutual Funds’ Trading and Performance? - 最终文献笔记

## Finalization Metadata / 定稿元信息

- 论文：Fang, Lily H., Joel Peress, and Lu Zheng. 2014. "Does Media Coverage of Stocks Affect Mutual Funds’ Trading and Performance?" Review of Financial Studies 27(12): 3441-3466.
- PDF：未直接读取。
- Markdown 底稿：manuscript_paragraphs.md
- automatic-extraction：本轮拟生成草案。
- discussion-outline：未执行共同阅读；不存在本轮输入。
- Finalization mode：cold-start / batch-library
- Co-read status：not performed
- 创建时间：2026-07-07
- 最近更新：2026-07-07
- 定稿者：Codex UAT draft

## Source Basis / 核验来源基础

- PDF 状态：未直接打开 PDF；仅使用 Markdown 中 PDF page marker。
- Markdown 状态：rough reading draft；正文可用。
- 表格 / 图像状态：表格嵌入普通段落；精确值需 PDF/table source 二次核验。
- 公式状态：Equation (2)-(4) 可理解，但 OCR/编码噪声明显，公式细节需 PDF 核验。
- source-check 覆盖范围：摘要、引言、数据、主要设计、核心结果、替代解释、结论。
- 剩余 source 风险：表格精确数值、公式符号、未报告稳健性、脚注与页眉混排。

## Claim Status Vocabulary / 结论状态词

使用 `verified-citable-text-summary`、`verified-citable-method-description`、`verified-citable-directional-result`、`verified-understanding`、`needs-source-check` 等状态词。精确表格值未做 PDF 核验，不标 `verified-citable-table-value`。

## Verified Core Finding / 已核验核心发现

### 理论纯净版

| 表述 | 状态 | Source Anchors | 备注 |
|---|---|---|---|
| 专业投资者也会受有限注意力影响；外部注意力触发会系统性影响交易选择，并且注意力驱动的交易倾向与较差未来表现相关。 | verified-understanding | para 8-11, 15, 143-145 | 理论重构；可作为笔记核心，不宜逐字引用为作者原句。 |

### 读者导览版

| 表述 | 状态 | Source Anchors | 备注 |
|---|---|---|---|
| 基金更倾向买入被媒体报道的股票；基金层面的买入媒体报道股票倾向越强，未来表现越差；该结果不延伸到卖出端。 | verified-citable-text-summary | para 3, 12-15, 143-145 | 作者在摘要、引言和结论均有文字总结。 |

### 形式逻辑还原

| 逻辑形式 | 状态 | Source Anchors | 备注 |
|---|---|---|---|
| 若媒体报道降低搜索成本并触发有限注意力下的交易，且该交易不是优势信息驱动，则买入媒体报道股票的倾向应更强，并预测较差业绩；卖出端因卖空约束和持仓集合限制应较弱。 | verified-understanding | para 9-11, 90, 143-145 | 论证重构，非作者逐字表述。 |

## Verified Proposition Registry / 已核验命题登记表

| ID | 角色 | 分支类型 | 已核验表述 | 状态 | Source Anchors | 相比 automatic-extraction 的修订 |
|---|---|---|---|---|---|---|
| P1 | 核心命题 | core | 媒体报道与基金买入行为正相关；控制股票特征后，卖出端不显著。 | verified-citable-directional-result | para 12, 51-56, 143 | 表 4 精确系数未升为 table-value。 |
| P2 | 核心命题 | core | 基金买入媒体报道股票的倾向与未来基金业绩负相关；卖出倾向没有类似强关系。 | verified-citable-text-summary / directional-result | para 3, 13, 94-99, 143 | 年化 1.1%-2.8% 为正文文字总结；表格值仍待核。 |
| S-P1-boundary | 支撑分支 | diagnostic/boundary | 媒体影响在买入端强于卖出端，符合共同基金卖空约束和买入搜索成本更高的解释。 | verified-citable-text-summary | para 10-11, 55-56 | 保持支撑分支，不升为核心命题。 |
| S-P2-exclusion-flow | 支撑分支 | exclusion | 未来资金流对基金所买股票的媒体覆盖不显著，削弱 flow-catering 解释。 | verified-citable-directional-result | para 104-114 | 精确表值待核。 |
| S-P2-exclusion-content | 支撑分支 | exclusion | 基于覆盖量的 PROPENSITY_BUY_MEDIA 比基于新闻方向的 mass media RPI 更能预测业绩。 | verified-citable-text-summary | para 115-123, 132-137 | tone 代理限制保留。 |
| S-P1-mechanism-manager | 支撑分支 | mechanism | 经理更换后买入媒体倾向下降，支持该倾向与经理特征相关。 | verified-citable-text-summary | para 137-141 | 精确 rank change 待表格核验。 |

## Verified Proxy Bridge / 已核验 Proxy Bridge

| Bridge ID | 理论对象 / 关系 | Proxy / Measure | 原文支持的 warrant | 证据类型 | 状态 | 剩余威胁 |
|---|---|---|---|---|---|---|
| A03-P1-X | 注意力触发 | LexisNexis 四大报纸股票报道数量/覆盖类型 | 作者将 coverage 解释为 media attention；报道把股票放入 radar screen | construct warrant | verified-citable-method-description | coverage 也可能含信息。 |
| A03-P1-Y | 基金交易 | 持仓变化推断 buys/sells，按 lagged TNA 或持仓规模缩放 | 共同基金持仓数据库可推断季度净交易 | measurement description | verified-citable-method-description | 不能观察季内往返交易。 |
| A03-P2-X | 媒体驱动买入倾向 | PROPENSITY_BUY_MEDIA | 基金-季度回归中媒体覆盖 beta 的四季度精度加权平均 | measurement description | verified-citable-method-description | 公式细节需 PDF 核。 |
| A03-P2-Y | 未来业绩 | CAPM/FF3/Carhart4/conditional4 alpha 与 manipulation-proof measure | 常用基金业绩指标 | method description | verified-citable-method-description | alpha 模型假设。 |

## Citation-Ready Statements / 可引用表述

| ID | 表述 | 状态 | Source Anchors | 引用用途 |
|---|---|---|---|---|
| C1 | 作者研究大众媒体报道与共同基金交易及业绩之间的关系。 | verified-citable-text-summary | para 2, 4 | 文献定位 |
| C2 | 作者发现基金在买入媒体报道股票的倾向上存在持续差异，且该倾向与未来业绩负相关。 | verified-citable-text-summary | para 3, 78, 143-144 | 核心发现 |
| C3 | 作者的媒体数据来自 LexisNexis，覆盖 1993-2002 年全部 NYSE 股票和 500 个随机 NASDAQ 股票，并使用四份全国性日报。 | verified-citable-method-description | para 21, 26 | 数据来源 |
| C4 | 作者用 CRSP Survivor-Bias-Free Mutual Fund Database 与 Thompson CDA/Spectrum holdings 数据构造共同基金样本，并限制为开放式美国国内权益基金。 | verified-citable-method-description | para 27-28 | 样本说明 |
| C5 | 作者构造 PROPENSITY_BUY_MEDIA/SELL_MEDIA 来衡量基金买入/卖出媒体报道股票的倾向。 | verified-citable-method-description | para 63, 67-71 | 变量构造 |
| C6 | 作者报告高买入 propensity 基金相对低 propensity 基金年化低 1.1%-2.8%，具体取决于业绩指标。 | verified-citable-text-summary | para 3, 97-99, 143 | 结果概述；精确表值需核 |

## Not-Citable / Needs-Check Statements / 不可引用或待核验表述

| ID | 表述 | 原因 | 需要核验什么 |
|---|---|---|---|
| N1 | Table 4/9/11/12/13/14 的所有精确系数、t-stat、R2、样本量。 | 只从 Markdown 表格段落读取，表格结构泄漏。 | 回 PDF 或 restored table。 |
| N2 | Equation (2)-(4) 的完整数学形式。 | OCR/编码噪声。 | 回 PDF 公式。 |
| N3 | unreported robustness 的具体结果。 | 作者仅称 qualitatively similar。 | 查论文附录/早期版本/补充材料。 |
```

---

## 4. verified-claims.md 草案

```markdown
# Does Media Coverage of Stocks Affect Mutual Funds’ Trading and Performance? - Verified Claims

| Claim ID | Claim Type | Claim | Status | Source Anchors | Citation Use | Remaining Risk |
|---|---|---|---|---|---|---|
| VC1 | 作者原文 | 本文研究个股大众媒体报道与共同基金交易和业绩之间的关系。 | verified-citable-text-summary | para 2, 4 | 文献定位 | 无重大风险 |
| VC2 | 作者原文 | 作者提出 limited attention hypothesis：媒体报道降低搜索成本，使基金经理更可能交易被报道股票；这种交易不是优势信息驱动，因此预期与较差表现相关。 | verified-citable-text-summary | para 9-11 | 理论机制 | 可引用为作者假说，不是已证明事实 |
| VC3 | 方法描述 | 媒体数据来自 LexisNexis，覆盖 1993-2002 年全部 NYSE 股票和 500 个随机 NASDAQ 股票，报纸包括 USA Today、WSJ、NYT、Washington Post。 | verified-citable-method-description | para 21, 26 | 数据说明 | 需核报纸名称拼写和覆盖比例 |
| VC4 | 方法描述 | 共同基金样本由 CRSP Survivor-Bias-Free Mutual Fund Database 和 Thompson CDA/Spectrum holdings 合并而来，限制为开放式美国国内权益基金。 | verified-citable-method-description | para 27-28 | 数据说明 | 无重大风险 |
| VC5 | 方法描述 | 基金交易由季度持仓变化推断，并区分 buys 和 sells。 | verified-citable-method-description | para 28, 45 | 变量构造 | 季度净交易限制需说明 |
| VC6 | 表格结果 / 正文总结 | 控制股票特征后，媒体覆盖与基金买入正相关；卖出端不显著。 | verified-citable-directional-result | para 51-56 | 主结果方向 | 精确系数/t-stat/R2 待 PDF 核 |
| VC7 | 方法描述 | PROPENSITY_BUY_MEDIA 是基于每个基金-季度回归中媒体覆盖系数的四季度精度加权平均；SELL 指标类似。 | verified-citable-method-description | para 63, 67-71 | 核心变量定义 | 公式符号需 PDF 核 |
| VC8 | 作者原文 / 表格结果 | PROPENSITY_BUY_MEDIA 具有持续性，PROPENSITY_SELL_MEDIA 没有类似持续性。 | verified-citable-directional-result | para 78-90 | 机制证据 | 表 8 精确值待 PDF 核 |
| VC9 | 作者原文 / 表格结果 | PROPENSITY_BUY_MEDIA 与未来基金业绩显著负相关；PROPENSITY_SELL_MEDIA 与未来业绩关系弱或不显著。 | verified-citable-directional-result | para 94-99, 101-102 | 核心结果 | 表 9 精确值待 PDF 核 |
| VC10 | 作者原文 | 高买入 propensity decile 基金相对低 decile 基金年化低 1.1%-2.8%，取决于业绩指标。 | verified-citable-text-summary | para 3, 97-99, 143 | 结果概述 | 年化差为正文总结；表值仍需核 |
| VC11 | 替代解释 | 买入媒体报道股票并不显著吸引未来 fund flow，削弱 flow-catering hypothesis。 | verified-citable-directional-result | para 104-114 | 替代解释 | 表 10 精确值待 PDF 核 |
| VC12 | 替代解释 | 控制 Kacperczyk-Seru RPI 后，PROPENSITY_BUY_MEDIA 仍预测未来业绩，说明不被 RPI 效应吸收。 | verified-citable-text-summary | para 115, 122 | 替代解释 | RPI 数据来源和表值待核 |
| VC13 | 替代解释 | 正负 tone 的报道均与更多交易相关；coverage 比 content 更符合 limited attention 解释。 | verified-citable-text-summary | para 123-137 | 机制/替代解释 | tone 用 DGTW 调整收益代理，非文本分析 |
| VC14 | 机制证据 | 经理更换后买入 media propensity rank 显著下降，支持 propensity 与经理特征相关。 | verified-citable-text-summary | para 137-141 | 机制证据 | 表 14 精确值待 PDF 核 |
| VC15 | Agent 重构 | 本文的设计强度应标为 predictive relation / mechanism-consistent evidence，而非严格因果识别。 | verified-understanding | para 51-56, 94-102, 104-141 | 阅读判断 | 不可作为作者原文引用 |
| VC16 | 项目迁移 | 该文可迁移为“估计基金经理 attention-driven trading propensity，再预测未来业绩”的研究设计模板。 | verified-understanding | 全文综合 | 项目路线 | 需结合项目数据可得性 |
```

---

## 5. source-check-log.md 草案

```markdown
# Does Media Coverage of Stocks Affect Mutual Funds’ Trading and Performance? - Source-Check Log

| Check ID | Claim ID | Claim Type | First-Pass Statement | Source Checked | Check Action | Result | Claim Status | Verified Statement | Remaining Risk | Next Check |
|---|---|---|---|---|---|---|---|---|---|---|
| SC1 | VC1 | 作者原文 | 论文研究媒体报道与共同基金交易/业绩关系。 | para 2, 4 | read paragraph anchors | 支持 | verified-citable-text-summary | 作者明确说明研究 mutual fund trades and mass media coverage，并提出研究问题。 | 无 | 无 |
| SC2 | VC2 | 作者原文 | 媒体通过降低搜索成本影响有限注意力下交易，并预期损害业绩。 | para 9-11 | read paragraph anchors | 支持 | verified-citable-text-summary | 作者称 media lower search cost，交易不是 superior information 驱动，因此预期 inferior performance。 | 理论假说非因果证明 | 引用时写为 hypothesis |
| SC3 | VC3 | 方法描述 | 媒体数据为 LexisNexis、1993-2002、四份全国性日报。 | para 21, 26 | read paragraph anchors | 支持 | verified-citable-method-description | 数据覆盖全部 NYSE 和 500 随机 NASDAQ 股票；四份报纸为 USA Today、WSJ、NYT、Washington Post。 | 报纸 circulation 细节可核 PDF | PDF check optional |
| SC4 | VC4 | 方法描述 | 基金样本来自 CRSP + CDA/Spectrum，开放式美国国内权益基金。 | para 27-28 | read paragraph anchors | 支持 | verified-citable-method-description | 作者说明合并 CRSP Survivor-Bias-Free Mutual Fund Database 与 Thompson CDA/Spectrum holdings。 | 无 | 无 |
| SC5 | VC5 | 方法描述 | 基金交易由持仓变化推断。 | para 28, 45 | read paragraph anchors / equation text | 支持 | verified-citable-method-description | buys/sells 由季度 holdings changes 推断。 | Equation (1A/1B) 格式需 PDF 核 | PDF equation check |
| SC6 | VC6 | 表格结果 | 控制后媒体覆盖影响买入，不影响卖出。 | para 51-56 | read paragraph anchors + table paragraph | 方向支持 | verified-citable-directional-result | 正文解释 Table 4：more coverage associated with more fund buys；sells not influenced after controls。 | 精确系数、t-stat、R2 待核 | PDF Table 4 |
| SC7 | VC7 | 方法描述 | PROPENSITY 为四季度精度加权媒体 beta。 | para 63, 67-71 | read formula paragraph | 基本支持 | verified-citable-method-description | 作者说明以四个季度 regression coefficients 的 precision-weighted average 构造。 | 公式 OCR 噪声 | PDF Equation (2)-(3) |
| SC8 | VC8 | 表格结果 | PROPENSITY_BUY_MEDIA 持续，SELL 不持续。 | para 78-90 | read paragraph anchors + table paragraph | 支持方向 | verified-citable-directional-result | 正文称三年后高买入 propensity 仍显著高于低组；SELL 无类似 persistence。 | 表 8 精确值待核 | PDF Table 8 |
| SC9 | VC9 | 表格结果 | 买入 propensity 负向预测未来业绩，卖出不显著。 | para 94-102 | read paragraph anchors + table paragraph | 支持方向 | verified-citable-directional-result | 正文称 PROPENSITY_BUY_MEDIA coefficient negative and significant in all regressions；SELL small/not significant。 | 表 9 精确值待核 | PDF Table 9 |
| SC10 | VC10 | 作者原文 | 高低 decile 年化业绩差 1.1%-2.8%。 | para 3, 97-99, 143 | read paragraph anchors | 支持文字总结 | verified-citable-text-summary | 摘要、正文和结论均陈述 1.1%-2.8% per year。 | 该数来自表 9 计算，精确表值待核 | PDF Table 9 if quoting as table-derived |
| SC11 | VC11 | 替代解释 | flow-catering 不成立。 | para 104-114 | read paragraph anchors + table paragraph | 支持方向 | verified-citable-directional-result | 作者称 media measures not significant，invalidates necessary condition for flow-catering。 | 表 10 精确值待核；winner-stock 特例 | PDF Table 10 |
| SC12 | VC12 | 替代解释 | 不被 RPI 吸收。 | para 115, 122 | read paragraph anchors + table paragraph | 支持 | verified-citable-text-summary | 作者称 controlling for RPI 后 PROPENSITY_BUY_MEDIA remains significant。 | 表 11 精确值待核 | PDF Table 11 |
| SC13 | VC13 | 替代解释 | coverage 强于 content/tone 解释。 | para 123-137 | read paragraph anchors + table paragraphs | 支持 | verified-citable-text-summary | 作者称 PROPENSITY_BUY_MEDIA stronger than mass media RPI；正负 tone 均伴随更多交易。 | tone 非文本测量；表 12/13 待核 | PDF Tables 12-13 |
| SC14 | VC14 | 机制证据 | manager turnover 后 propensity 下降。 | para 137-141 | read paragraph anchors + table paragraph | 支持 | verified-citable-text-summary | 作者称 manager changes lead to significant reduction in PROPENSITY quintile ranks。 | 表 14 精确值待核 | PDF Table 14 |
| SC15 | VC15 | Agent 重构 | 本文不是严格因果识别。 | para 51-56, 94-102, 104-141 | design-level review | 支持为阅读判断 | verified-understanding | 设计以滞后面板、预测回归、horse race 和机制一致性为主。 | 不可作为作者原文 | 若写综述，用“design supports predictive/mechanism-consistent interpretation” |
| SC16 | VC16 | 项目迁移 | 可迁移为 attention-driven trading propensity 设计。 | 全文 | synthesize | 支持为迁移判断 | verified-understanding | 两阶段 propensity 构造和未来业绩预测可迁移。 | 需项目数据验证 | 读项目数据字典 |
```

---

## 6. 读取了哪些 Skill / 模板 / 原始材料

- 入口 Skill：`/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/SKILL.md`
- 子 Skill：`/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/skills/paper-reading/SKILL.md`
- 子 Skill：`/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/skills/paper-reading/skills/paper-extract/SKILL.md`
- 模板：`/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/skills/paper-reading/skills/paper-extract/templates/automatic-extraction-template.md`
- 子 Skill：`/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/skills/paper-reading/skills/paper-finalize/SKILL.md`
- 模板：`/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/skills/paper-reading/skills/paper-finalize/templates/final-literature-note-template.md`
- 原始材料：`/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/PDFs/基金经理/RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/1-md/manuscript_paragraphs.md`

未读取 `logs/`，未读取已有 `automatic-extraction.md`、`discussion-outline.md`、`final-literature-note.md`、`verified-claims.md`、`source-check-log.md`。
