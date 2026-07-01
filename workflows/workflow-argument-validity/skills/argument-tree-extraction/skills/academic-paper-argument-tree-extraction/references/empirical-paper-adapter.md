# Empirical Paper Adapter

用于实证论文，包括定量回归、准实验、实验、问卷、文本分析、机器学习预测或混合方法论文。

## 节点命名

建议使用：

```text
G* = X1 支撑节点
P* = X2 支撑节点
E-* = 底层证据节点
```

`full-tree` 模式必须进一步使用 canonical recursive tree：

```text
Y
<- X1 / X2 / P9
<- P*
<- P*.*
<- E-* 最小证据
```

不要停在 `E-R1 表4主结果`、`E-D2 样本规则` 这种概括证据。必须拆到一个系数、一条脚注、一个表注、一个样本量、一个变量定义或一篇文献。

## X2 最小展开

| 节点 | 问题 |
|---|---|
| P1 X 被定义和操作化 | 核心处理、解释变量或事件是否清楚 |
| P2 M 理论机制成立 | 作者为什么认为 X 会影响 Y |
| P3 Y 被定义和操作化 | 结果变量是否承载目标概念 |
| P4 样本/数据适配 | 样本是否能检验机制和结论 |
| P5 方法/识别可信 | 回归、实验、DID、IV、PSM、机器学习等是否支撑 claim |
| P6 主结果支持核心发现 | 表格和系数是否真的支持 X -> Y |
| P7 机制/异质性支持解释 | 机制检验是否区分作者机制和替代机制 |
| P8 稳健性回应核心威胁 | 稳健性是否解决核心质疑，而不是重复同一偏误 |
| P9 贡献上升成立 | Y1 是否足以推出 Y2 / 政策启示 / 理论贡献 |

## Evidence Ledger 要求

实证论文 `full-tree` 模式下，evidence ledger 至少覆盖：

```text
X 的概念定义和操作化
Y 的概念定义和操作化
M / 机制变量或机制证据
样本期、样本筛选、排除规则、最终样本量
事件窗口 / 时间编码 / treatment timing
模型设定、固定效应、控制变量
标准误或聚类层级
主结果表号、核心变量、系数、显著性、样本量
机制 / 异质性表号和分组逻辑
稳健性检验分别回应的威胁
贡献上升或政策启示的原文依据
```

缺少任一类关键证据时，写入 `extraction-qc.md`。如果这些缺口影响后续验箭头，标记 `incomplete-full-tree`。

表格证据尽量记录：

```text
表号
列号
变量名
系数
t 值 / 标准误
显著性
样本量
固定效应
聚类层级
```

表格证据在 canonical tree 中要拆成独立 minimal evidence。示例：

```text
E-R4-1 表4列(1)：Peerdumy×POST = -0.0157***
E-R4-2 表4列(2)：Peerdumy×POST = -0.0111***
E-R4-3 表4列(2)括号值 = (-2.81)
E-R4-4 表4表注：括号内为公司层面聚类调整标准误
E-R4-5 表4样本量 = 11339
```

样本规则要拆成独立 minimal evidence。示例：

```text
E-SAMPLE-1 样本期为 2007-2024 年沪深 A 股
E-SAMPLE-2 事件窗口为主动披露违规前 3 年、当年、后 2 年
E-SAMPLE-3 若行业内多家企业主动披露违规且间隔过短，剔除该行业公司样本
E-SAMPLE-4 仅保留行业内第一次满足条件的主动披露违规窗口样本
E-SAMPLE-5 剔除主动披露违规的公司样本
E-SAMPLE-6 脚注：t 至 t+2 不应存在第二次冲击
E-SAMPLE-7 脚注：t-5 至 t 不应存在主动披露违规
```

变量证据记录：

```text
构念
含义
操作化指标
方向
量纲 / 转换
作者说明与辩护
原文引用或段落链接
```

如果只有作者正文摘要，证据粒度写：

```text
summarized / needs-table-qc
```

## 常见断点预留

抽树时只记录作者支撑，不展开攻击；但可在 `extraction-qc.md` 标出待审查点：

- construct-measure mismatch；
- macro-micro mismatch；
- identification-causal leap；
- significance fragility；
- sample-mechanism mismatch；
- robustness-does-not-answer-core-threat；
- elevated claim over evidence。

## 移交验箭头的关注点

实证论文完成作者证据树后，paper 抽树阶段只在 `extraction-qc.md` 标出哪些证据组合需要移交 `academic-argument-arrow-audit`。正式的 `review-sensitivity-map.md` 由学术验箭头 Skill 生成，不属于本 adapter 的产物。

| handoff 类型 | 建议移交的 evidence 位置 | 后续验箭头关注 |
|---|---|---|
| concept-consistency | 理论、变量定义、机制解释、异质性解释、结论 | 同一概念是否在不同章节承担不同含义 |
| treatment-timing | X 定义、事件窗口、POST 编码、动态效应表 | 处理时点是否匹配理论反应过程 |
| sample-representativeness | 样本筛选、脚注、剔除规则、最终样本量、机制样本 | 干净识别是否牺牲机制相关样本 |
| direct-effect-baseline | 溢出研究中的事件公司自身结果、被模仿对象结果 | 若声称同行模仿，事件公司自身是否有改善或收益 |
| construct-measure-fit | Y 定义、代理变量文献、描述统计、替代变量 | 操作化指标是否承载作者宏大概念 |
| cluster-level-fit | 处理变量变异层级、回归表注、标准误聚类说明 | 聚类层级是否低于处理变异层级 |
| mechanism-sample-consistency | 图示样本、机制表样本、主回归样本 | 机制前提是否来自同一有效样本 |
| null-result-reversal | 作者用不显著结果排除机制的位置 | 不显著是否可能有反向解释 |
| imported-measure-level | 引用经典指标的方法段、本文变量构造 | 原始指标层级是否被本文改变 |
| robustness-threat-fit | 稳健性章节、核心威胁清单 | 稳健性是否回应真正核心威胁 |

`extraction-qc.md` 可记录：

```text
handoff_to_academic_arrow_audit
handoff_type
suggested_evidence_ids
suggested_arrow_ids
reason
```

对于本类论文，尤其要尝试并读：

```text
理论机制证据 + 机制检验表 + 异质性解释
样本筛选规则 + 主结果外部有效性声称
POST 定义 + 动态效应表
主回归样本 + 机制图表样本
变量定义 + 描述统计/表注/替代变量
经典文献指标定义 + 本文操作化层级
```
