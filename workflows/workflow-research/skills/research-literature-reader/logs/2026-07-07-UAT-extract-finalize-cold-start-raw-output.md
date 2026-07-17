# UAT Raw Output: extract -> finalize cold-start

## Metadata

- Date: 2026-07-07
- SubAgent: Gauss
- Tested entry Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/SKILL.md`
- Source material: `/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/PDFs/基金经理/RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/1-md/manuscript_paragraphs.md`
- Purpose: 保存 `extract -> finalize` cold-start 黑箱 UAT 中 subAgent 真实返回的结果；本文件不包含主 Agent 评价。

## SubAgent Raw Result

## 对话窗口会返回给用户的内容

我先给你一版 cold-start finalization 的最终文献笔记。由于本轮只基于 `manuscript_paragraphs.md` 和其中的表格线索核验，精确表格系数、t-stat、R2、样本量等我先不升级为可直接引用；需要引用这些数字时，还要回 PDF 或 restored table 做视觉核验。

# Fang, Peress and Zheng - Does Media Coverage of Stocks Affect Mutual Funds’ Trading and Performance?

## 核心结论

**理论纯净版：**
专业投资者并不完全免于有限注意力约束；当外部注意力线索降低搜索成本时，基金经理的交易选择会被系统性影响，而这种注意力驱动的交易倾向与较差的未来业绩相关。
状态：`verified-citable`。来源：paras 3, 8-15, 99, 143-145。

**读者导览版：**
作者用大众报纸对股票的报道作为“注意力触发”代理，发现共同基金更倾向于买入被媒体报道的股票；买入媒体报道股票倾向最高的基金，未来年化表现比最低组低约 1.1%-2.8%，卖出端没有类似结果。
状态：`verified-citable`，但“1.1%-2.8%”目前只基于正文/摘要段落核验；若要引用 Table 9 的具体模型系数，仍需回 PDF 表格核验。来源：paras 3, 12-15, 95-99, 143。

## 可引用结论

1. 本文研究问题是：大众媒体对个股的报道是否影响专业投资者，尤其是共同基金经理的交易和表现。
状态：`verified-citable`。来源：para 4。

2. 论文的核心机制解释是有限注意力：媒体报道降低从大量股票中搜索交易对象的成本，使被报道股票更容易进入基金经理的关注范围。
状态：`verified-citable`。来源：paras 8-11, 56。

3. 在控制股票规模、流动性、账面市值比、过去收益、季度固定效应和基金固定效应后，媒体报道与基金买入显著正相关，但卖出端不显著。
状态：`verified-citable` 用于方向和设计描述；Table 4 的精确系数需回 PDF 核。来源：paras 51-56。

4. 基金买入媒体报道股票的倾向具有持续性；卖出倾向不呈现同样的持续性。
状态：`verified-citable` 用于方向性结论；Table 8 数字需回 PDF 核。来源：paras 78-90。

5. 买入媒体报道股票倾向越强，基金未来表现越差；最高倾向 decile 相比最低倾向 decile 年化低约 1.1%-2.8%。
状态：`verified-citable`。来源：paras 3, 13, 96-99, 143。

6. 作者未发现媒体报道股票买入会带来未来资金流入，因此“基金经理为迎合投资者资金流而买入媒体报道股票”的解释缺少必要条件。
状态：`verified-citable`。来源：paras 14, 104-115。

7. 该效应不能简单归结为基金经理依赖公开信息或新闻方向性内容；PROPENSITY_BUY_MEDIA 在控制 RPI、signed media RPI 后仍有预测力。
状态：`verified-citable` 用于方向性结论；Table 11-12 精确数值需回 PDF 核。来源：paras 115-123, 131-132。

8. 正面和负面媒体报道都与更多交易相关，支持“覆盖本身作为注意力触发”而不只是“新闻内容方向”解释。
状态：`verified-citable` 用于方向性结论；Table 13 数字需回 PDF 核。来源：paras 123-137。

## 只能作为理解性判断

1. 这篇文章更像是“有限注意力的职业投资者版本”，不是严格的媒体报道因果识别论文。
状态：`verified-understanding`。理由：设计主要是滞后媒体报道、控制变量、固定效应、排序预测、替代解释检验和 horse race，不是随机或准实验设计。

2. `PROPENSITY_BUY_MEDIA` 可以理解为基金经理“被媒体注意力线索牵引的买入倾向”，但它仍是由交易-媒体覆盖回归构造出的经验指标，不等于心理层面的注意力直接测量。
状态：`verified-understanding`。来源：paras 63-72。

3. 买入端强、卖出端弱并不是独立核心命题，而是支持有限注意力机制的诊断模式：共同基金买入面对全市场搜索，卖出通常受既有持仓集合限制。
状态：`verified-understanding`。来源：paras 10-11, 55-56。

## 需要回 PDF 继续核的内容

1. Table 4、5、8、9、10、11、12、13、14 的精确系数、t-stat、R2、observations、显著性星号。
状态：`needs-source-check`。原因：当前 Markdown 把表格压成普通段落，适合定位和方向性核验，不适合最终引用精确表格数字。

2. Equation 2 和 Equation 3 的公式符号细节，尤其 shrinkage estimator 的排版。
状态：`needs-source-check`。来源线索：paras 63-71。

3. 媒体样本是否只覆盖 NYSE + 500 随机 NASDAQ，以及四家报纸覆盖是否可代表 broader media coverage。
状态：正文可引用，但如用于方法批评，需回 PDF 脚注与数据描述核。来源：paras 21, 26。

4. manager turnover test 的精确经济含义。
状态：`needs-source-check`。方向性结论可读，表格数字需回 PDF。来源：paras 137-141。

---

## 如果要写入本地文件，你会写入的文件草案

建议路径：

`/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/PDFs/基金经理/RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/2-task-readings/TASK01-final-literature-note.md`

正文草案：

```markdown
# Does Media Coverage of Stocks Affect Mutual Funds’ Trading and Performance? - Final Literature Note

## Finalization Metadata

- Paper: Fang, Lily H.; Peress, Joel; Zheng, Lu. "Does Media Coverage of Stocks Affect Mutual Funds’ Trading and Performance?"
- Markdown substrate: `1-md/manuscript_paragraphs.md`
- Finalization mode: cold-start finalization
- Co-read status: not performed
- Table / figure status: table text available in Markdown, but no PDF visual table check in this round
- Scope warning: precise coefficients, t-statistics, R2, observations, and formula notation remain `needs-source-check`

## Verified Core Finding

| Version | Statement | Status | Source Anchors |
|---|---|---|---|
| Theory-pure | Professional investors are subject to limited attention; attention-triggered trading affects portfolio choices and is associated with worse future performance. | verified-citable | paras 3, 8-15, 99, 143-145 |
| Reader-guide | Media coverage draws stocks onto mutual fund managers’ radar, predicts stronger buying, and funds with the highest media-buying propensity underperform the lowest group by about 1.1%-2.8% per year. | verified-citable | paras 3, 12-15, 95-99, 143 |

## Verified Proposition Registry

| ID | Role | Statement | Status | Source Anchors |
|---|---|---|---|---|
| P1 | core | Media attention affects professional investors’ trading behavior, especially buying. | verified-citable | paras 8-12, 51-56 |
| P2 | core | Stronger propensity to buy media-covered stocks predicts weaker future fund performance. | verified-citable | paras 13, 91-99, 143 |
| S-P1-diagnostic | support | Buy-side effects should be stronger than sell-side effects because buying requires search over the full market while selling is constrained by current holdings. | verified-citable | paras 10-11, 55-56 |
| S-P2-exclusion | support | Flow-catering, reliance on analyst/public information, and trading on media tone do not fully explain the main result. | verified-citable for direction; table values need PDF check | paras 14-15, 104-123, 131-137 |

## Verified Measurement / Data

| Block | Data / Measure | Status | Source Anchors |
|---|---|---|---|
| Media coverage | LexisNexis articles for all NYSE stocks and 500 randomly selected NASDAQ stocks, 1993-2002; four national newspapers. | verified-citable | paras 21, 26 |
| Fund sample | CRSP Survivor-Bias-Free Mutual Fund Database merged with Thompson CDA/Spectrum via MFLink; open-end domestic equity funds, excluding index funds and small/few-holding funds. | verified-citable | paras 27-28 |
| Fund trades | Buys/sells inferred from quarterly holdings changes, adjusted for splits and dividends. | verified-citable | paras 28, 45 |
| PROPENSITY_BUY_MEDIA / SELL | Fund-quarter regression of buys/sells on lagged stock media coverage and controls; shrinkage estimator over four quarters. | verified-citable for construction summary; formula details need PDF check | paras 63-72 |

## Verified Design / Identification

| Design ID | Design | Claim Level | What It Can Claim | What It Cannot Claim | Status |
|---|---|---|---|---|---|
| A05-P1 | Panel regressions of fund trades on lagged media coverage with stock controls, quarter FE, fund FE, clustered SE. | descriptive association / mechanism-consistent evidence | Media coverage is associated with more mutual fund buying after controls. | It does not by itself prove exogenous causal effects of media coverage. | verified-citable for design; table values need PDF check |
| A05-P2 | Fund-level propensity measures sorted into deciles and used to predict next-quarter performance. | predictive relation | Buy-media propensity predicts lower future performance. | It should not be stated as a clean causal effect of media propensity on performance. | verified-citable |
| A05-A07 | Alternative explanation tests: fund flows, RPI, signed media tone, daily institutional trades, manager turnover. | exclusion-enhanced explanation | These tests make limited attention more plausible than several alternatives. | They do not eliminate every possible omitted manager characteristic. | verified-understanding / partly verified-citable |

## Citation-Ready Statements

| ID | Statement | Source Anchors |
|---|---|---|
| C1 | Fang, Peress, and Zheng study whether mass media coverage of stocks affects mutual fund managers’ trading and performance. | para 4 |
| C2 | Mutual funds buy stocks with heavier prior media coverage more intensely, while fund sells are much less affected after controls. | paras 12, 51-56 |
| C3 | Funds with the strongest propensity to buy media-covered stocks underperform funds with the weakest propensity by about 1.1%-2.8% per year. | paras 3, 13, 96-99, 143 |
| C4 | The evidence is consistent with limited attention among professional investors rather than only individual investors. | paras 15-20, 145 |
| C5 | The paper finds little support for the flow-catering explanation because media coverage of purchased stocks does not significantly predict future fund flows. | paras 104-115 |

## Understanding-Only Statements

| ID | Statement | Why Not Citation-Ready |
|---|---|---|
| U1 | The paper’s design is best read as predictive and exclusion-enhanced, not as a clean quasi-experiment. | This is an interpretation of the design rather than the authors’ own stated causal classification. |
| U2 | Buy-side asymmetry is a diagnostic implication of limited attention rather than a separate core proposition. | This is a reconstruction of the argument structure. |
| U3 | Media coverage is used as an attention proxy, not a direct psychological measure of attention. | This is a construct-validity reading of the empirical proxy. |

## Not-Citable / Needs-Check Statements

| ID | Statement | Required Check |
|---|---|---|
| N1 | Any exact Table 4/5/8/9/10/11/12/13/14 coefficient, t-stat, R2, observation count, or significance star. | Check PDF or restored table visually. |
| N2 | Exact formulas for Equations 2 and 3. | Check PDF formula rendering. |
| N3 | Precise manager turnover effect size from Table 14. | Check PDF table. |

## Transfer To Current Project

| Transfer Item | Use |
|---|---|
| Attention proxy design | Useful if the project needs to measure how external information salience affects fund manager behavior. |
| Propensity measure | Reusable as a manager-level behavioral trait: estimate individual manager/fund sensitivity to an information-salience proxy, then test persistence and performance prediction. |
| Buy/sell asymmetry | Useful diagnostic pattern where buying involves broad search but selling is constrained by existing holdings. |
| Caveat | Do not overstate causality; this is strongest as a predictive/behavioral mechanism design with alternative-explanation checks. |
```
