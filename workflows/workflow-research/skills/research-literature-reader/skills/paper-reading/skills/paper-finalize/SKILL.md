---
name: paper-finalize
description: paper-reading 的论文核验定稿层。用于在 paper-extract 和可选 paper-co-read 之后，回到 PDF / restored manuscript / tables / figures / source anchors 核验 automatic-extraction 与 discussion 共识，生成可引用最终文献笔记、source-check log、verified claims 和剩余不可引用边界；也可在用户明确要求先核验时作为 cold-start finalization 运行。
---

# Paper Finalize

状态：`seed / source-verified-note`

## 定位

本 Skill 是论文阅读的核验定稿层，不是 first-pass 抽取层，也不是共同读对话层。

它回答：

```text
哪些自动抽取 / 共同阅读结论已经被原文、PDF、表格和公式核验，可以进入最终文献笔记或被引用？
```

默认输入来自：

```text
paper-extract:
  automatic-extraction.md

paper-co-read:
  discussion-outline.md
```

默认输出是：

```text
final-literature-note.md
source-check-log.md
verified-claims.md
```

## 与上游 Skill 的关系

```text
paper-extract:
  生成 first-pass 结构化地图；
  允许 needs-source-check。

paper-co-read:
  与用户共同解释、纠偏、确定重点；
  形成 discussion consensus 和 pending questions。

paper-finalize:
  回源核验；
  修正或降级未被原文支持的判断；
  生成可引用最终文献资产。
```

默认推荐流程：

```text
paper-extract -> paper-co-read -> paper-finalize
```

允许流程：

```text
paper-extract -> paper-finalize -> paper-co-read
```

该流程称为 `cold-start finalization`。只有用户明确要求“先核验再共同读”“先给我可引用底稿”“不用先讨论，直接核原文”时使用。

批量 / 正式文献库流程：

```text
paper-extract -> paper-finalize
```

用于用户明确要求批量生成最终可引用文献笔记、文献库条目或 source-verified extraction。

## 输入检查

开始前必须确认：

```text
source PDF / restored manuscript / manuscript_paragraphs.md；
automatic-extraction.md；
discussion-outline.md 是否存在；
表格 / 公式 / 图像是否有可核验来源；
用户要求 finalize 的范围；
是否是 cold-start finalization。
```

如果没有 `automatic-extraction.md`，不得直接 finalize；先回到 `paper-extract`。

如果没有 `discussion-outline.md`，但用户明确要求 finalize，可以继续，但必须标记：

```text
finalization mode: cold-start finalization
co-read status: not performed
scope warning: 未经过共同读筛选，核验范围以 A01-A08 核心论证链为主。
```

## 核验范围

默认核验 A01-A08 的核心论证链：

```text
A01:
  一句话核心发现：理论纯净版；
  一句话核心发现：读者导览版；
  core proposition vs supporting branch 分类；
  source anchors 是否支撑命题。

A02:
  Pi-X / Pi-Y / Pi-R / Pi-KB 是否符合作者论述；
  是否把 proxy 错写成理论对象。

A03:
  proxy bridge 是否由作者明确论证；
  哪些是原文支持，哪些是 Agent 推断；
  proxy credibility evidence 是否存在。

A04:
  数据来源、样本、窗口、变量构造、控制变量、固定效应、聚合层级；
  是否与原文 / 表格 / 公式一致。

A05:
  研究设计、时间顺序、比较逻辑、识别强度；
  是否把预测 / 相关 / 机制一致性误写成因果。

A06:
  表格结果方向、显著性、经济意义、跨指标稳定性；
  表格数值必须回 PDF / table source 核验后才能引用。

A07:
  替代解释、稳健性、有效性威胁；
  作者是否真的排除，还是只部分缓解。

A08:
  对当前项目的可迁移性；
  哪些可直接迁移、哪些需要改造、哪些不可迁移。
```

## Claim Status

每条判断必须标注引用状态：

```text
verified-citable:
  已由原文 / PDF / 表格 / 公式核验，可引用。

verified-citable-text-summary:
  作者在摘要、引言、正文或结论中用文字明确陈述；
  可以引用为“作者的文本总结”；
  若包含表格派生的精确数值，表格值本身仍需 source-check。

verified-citable-method-description:
  数据来源、样本、变量定义、模型设定、控制变量、固定效应等方法描述已由原文核验，可引用。

verified-citable-directional-result:
  结果方向、显著/不显著的文字性结论已由原文核验，可引用；
  但精确系数、t-stat、R2、样本量、年化差距仍需表格 / PDF 核验。

verified-citable-table-value:
  精确数值已经由 PDF / restored table / source table 核验，可引用。

verified-understanding:
  可作为理解性表述，但不建议直接引用为精确结论。

inferred-not-citable:
  Agent 或读者推断；未被作者直接表述，不可直接引用。

needs-source-check:
  仍需回 PDF / 表格 / 公式 / 附录核验。

contradicted-or-revise:
  与原文不一致，必须修正或删除。
```

不要把 first-pass `needs-source-check` 自动升级为 `verified-citable`。

精确数值规则：

```text
凡是精确百分比、年化差距、系数、t-stat、p-value、R2、样本量、公式符号细节，
即使出现在摘要、引言、正文或结论的文字叙述中，
也不得直接标普通 verified-citable。

若只核验到正文文字：
  标 verified-citable-text-summary + table-value-needs-check。

若已核验 PDF / restored table / source table：
  才可标 verified-citable-table-value。
```

作者原文 vs 论证重构：

```text
作者明确说了什么：
  可进入 verified-citable-*，视核验程度而定。

Agent / 用户重构的论证角色：
  例如“这是 diagnostic branch 而不是 core proposition”；
  默认标 verified-understanding 或 inferred-not-citable；
  不得伪装成作者原文结论。
```

## Output Language

默认输出语言应跟随用户语言。

中文项目或中文用户请求下：

```text
final-literature-note.md；
verified-claims.md；
source-check-log.md；
对话窗口总结；
```

均默认使用中文。关键英文术语首次出现时保留括注：

```text
有限注意力（limited attention）；
买入媒体报道股票倾向（PROPENSITY_BUY_MEDIA）；
预测关系（predictive relation）；
机制一致性证据（mechanism-consistent evidence）；
可引用文本总结（verified-citable-text-summary）。
```

除论文标题、变量名、数据库名、模型名和必要术语外，不要把正文草案整体写成英文。

## Source-Check Log

必须维护逐项核验日志：

```text
claim ID；
原 first-pass 判断；
source anchor；
核验动作；
核验结果；
引用状态；
修正后表述；
剩余风险。
```

`source-check-log.md` 是逐条 claim 的核验账本，不是 final note 的附录摘要。每条核心 claim 至少记录：

```text
claim ID；
claim type：作者原文 / 表格结果 / 方法描述 / Agent 重构 / 项目迁移；
first-pass statement；
verified statement；
source checked；
check action；
claim status；
remaining risk；
next check。
```

核验动作示例：

```text
read paragraph anchors；
compare with PDF page；
check table title / sample / variables；
check coefficient direction / significance / economic magnitude；
check equation / variable definition；
check figure / appendix；
check source against discussion revision。
```

## Table / Formula Rules

表格、公式、图和脚注必须比正文判断更严格。

未经 PDF / restored table / figure source 核验，不得输出：

```text
精确系数；
t-stat；
p-value；
R2；
样本量；
年化差距；
公式符号细节；
图中数值。
```

可以输出：

```text
方向性 first-pass 判断；
needs-source-check；
qualitative summary。
```

若用户要求可引用结论，精确数值必须进入 `source-check-log.md`，并标注页码 / 表号 / 行列。

## Design Claim Level

A05 必须为每个 design block 标注识别强度：

```text
descriptive association；
predictive relation；
mechanism-consistent evidence；
exclusion-enhanced explanation；
quasi-causal / causal claim。
```

默认不要把观察性面板、排序预测、horse race 或 robustness 直接称为因果识别。

## 输出路径

推荐：

```text
2-task-readings/<TASKxx>-final-literature-note.md
2-task-readings/<TASKxx>-verified-claims.md
logs/<TASKxx>-source-check-log.md
```

若不属于特定 task：

```text
logs/final-literature-note.md
logs/verified-claims.md
logs/source-check-log.md
```

模板见：

```text
templates/final-literature-note-template.md
```

## 输出结构

默认必须输出三件套草案：

```text
final-literature-note.md:
  给人读的最终文献笔记；
  中文为主，术语括注英文。

verified-claims.md:
  可引用 / 可理解 / 不可引用的 claim 清单；
  以 claim status 为核心。

source-check-log.md:
  逐条 claim 的核验账本；
  记录核验动作和剩余风险。
```

若受篇幅限制不能完整展示三件套，必须明确标注：

```text
本轮已展示：
本轮未展示但应生成：
未展示原因：
```

最终文献笔记必须包含：

```text
Finalization Metadata；
Source Basis；
Reading Mode；
Verified Core Finding；
Verified Proposition Registry；
Verified Proxy Bridge；
Verified Measurement / Data；
Verified Design / Identification；
Verified Results；
Verified Alternatives / Validity Threats；
Transfer To Current Project；
Citation-Ready Statements；
Understanding-Only Statements；
Not-Citable / Needs-Check Statements；
Source-Check Log Summary；
Open Questions。
```

## 完成标准

- 已明确 finalize 模式：post-co-read / cold-start / batch-library。
- 已读取 `automatic-extraction.md`；若有 `discussion-outline.md`，已读取并纳入用户修订。
- 已回源核验 A01-A08 核心论证链。
- 表格 / 公式 / 数值结论已按严格规则标注状态。
- 每条核心结论都有 claim status。
- 已生成 final note、verified claims 和 source-check log 三件套，或明确说明本轮只完成其中哪一部分及原因。
- 明确哪些结论可引用，哪些只供理解，哪些仍不可引用。

## 禁止事项

- 不在没有 automatic-extraction.md 时直接 finalize。
- 不把 first-pass automatic extraction 当成最终文献笔记。
- 不把 discussion consensus 当成原文证据。
- 不在未核 PDF / 表格时引用精确数值。
- 不把正文中的精确数值直接标普通 `verified-citable`；最多标 `verified-citable-text-summary + table-value-needs-check`。
- 不把预测关系、相关关系或机制一致性证据写成因果结论。
- 不把 Agent / 用户的论证结构重构写成作者原文结论。
- 不在中文项目中默认输出英文正文草案。
- 不删除不稳判断；应降级为 `needs-source-check` 或 `inferred-not-citable`。
