---
name: manuscript-variable-data-measurement-audit
description: 对学术手稿的变量、数据和测量有效性做审查。用于外部审稿、投稿前自审和论文方法诊断中，在已有文本底稿和贡献链基础上，检查核心概念是否被合适变量操作化，数据来源、样本构造、数据合并、编码匹配、时间结构、测量误差、机制变量和拓展变量是否支撑作者结论。本 Skill 不生成最终审稿意见。
---

# Manuscript Variable Data Measurement Audit

## 定位

本 Skill 是 workflow-paper-writing-review 中的第 6 步：变量、数据与测量审查。

它与第 2 步不同：

- 第 2 步文本底稿回答“作者写了什么、表格公式在哪里”；
- 第 6 步变量数据审查回答“作者这样测，是否真的测到了他声称的概念”。

核心问题：

```text
概念 -> 变量 -> 数据 -> 样本 -> 时间 -> 结论
这条测量链是否成立？
```

输出应优先使用中文大白话，同时保留必要英文术语、变量名、数据库名和 evidence location。

## 触发条件

当用户提出以下需求时使用：

- “变量数据审查”
- “测量有效性”
- “这个变量怎么算”
- “这个数据能不能支撑结论”
- “样本、数据合并、HS 匹配、口径是否可靠”
- “Robot / EPS / IFR / ASIF / Customs 这些变量靠谱吗”
- “第 6 步”

## 输入

优先读取：

- `notes/quick-read-contribution-chain.md`
- `notes/literature-positioning-and-genealogy.md`
- `notes/causal-identification-audit.md`
- `notes/review-issue-ledger.md`
- 段落编号 manuscript Markdown
- 数据、变量、样本、稳健性、机制、拓展分析相关表格

## 既有疑点查重门

第 6 步经常会被用户用追问方式反复触发，例如“这个变量怎么算”“这个 Y 合理吗”“之前是不是记录过”。在已有项目中，不得直接按新问题处理。

回答或新增产物前，先做模块内查重。默认读取：

```text
notes/review-issue-ledger.md
notes/variable-data-measurement-audit.md
```

按需读取相邻模块，而不是默认全项目扫描：

- 若问题涉及 Y 的文献位置、benchmark、清单源头或概念谱系，读取 `notes/literature-positioning-and-genealogy.md` 和相关 `tasks/TASK03*/outputs/*.md`。
- 若问题涉及 X/Y 的因果解释、DAG、IV、PSM、控制变量或时序识别，读取 `notes/causal-identification-audit.md`。
- 若问题涉及结果表述是否越界、拓展分析是否扩大结论，读取 `notes/results-narrative-consistency-audit.md`。
- 若用户问该问题是否已经进入审稿素材，读取 `review/review-materials.md` 或 `review/review-materials.zh.md`。

检索关键词至少包括：

- 变量名、缩写和中文概念，例如 `EPS`、`Robot`、`IFR`、`CHF`、`出口产品结构升级`；
- 数据源、清单或编码，例如 `Xiang`、`HS6`、`HS8`、`China Customs`；
- 用户问题中的层级词，例如 `宏观`、`微观`、`公司层面`、`企业层面`、`操作化`；
- 可能的 issue id，例如 `VAR-001`、`LIT-001`。

处理规则：

- 若已有 issue 覆盖该问题，先复述已有结论和落盘位置，再说明本轮是否新增判断。
- 若本轮只是把已有问题说得更精准，应更新同一 issue 的 addendum 或 next action，不新建重复 issue。
- 若准备新建专题证据包，必须说明它是对哪个已有 issue 的扩展，并在证据包 frontmatter 写入 `issue_ids`。
- 不承担跨模块全局去重职责；全局一致性由第 7 步处理，审稿素材合并和排序由第 8 步处理。

## 输出

默认输出到：

```text
notes/variable-data-measurement-audit.md
```

建议使用模板：

```text
templates/variable-data-measurement-audit-template.md
```

同时更新：

```text
notes/review-issue-ledger.md
```

## 分析顺序

### 1. 测量链总览

先列出作者核心贡献链里的关键概念和实际变量：

- intended construct / 作者想说的概念；
- observed variable / 数据里实际测到的变量；
- data source / 数据来源；
- construction steps / 构造步骤；
- interpretation gap / 概念和变量之间的落差；
- audit priority。

### 2. 核心因变量 Y

检查：

- Y 是否直接测到了作者声称的结果；
- 是否依赖外部清单、代码表、分类法或跨库匹配；
- 分类口径是否过时、过粗或跨国迁移困难；
- 比例型变量的分母是否会机械变化；
- 替代 Y 是否真的检验同一概念，还是换了概念。

如果 Y 是清单或分类口径，必须要求作者说明：

- 清单来源；
- 时间覆盖；
- code crosswalk；
- 匹配率；
- 未匹配项处理；
- 对研究场景的适用性。

### 3. 核心解释变量 X

检查：

- X 是否直接测到 treatment / adoption / exposure；
- 如果是 proxy，proxy 与真实概念差在哪里；
- 替代 X 是否补强，还是换了 estimand；
- X 的时间是否先于 Y；
- X 是否可能反映能力、进口网络、行业趋势或其他共同原因。

### 4. 描述统计和量纲 sanity check

必须检查关键变量的 reported summary statistics 是否与定义一致：

- share / proportion / ratio 理论上是否应在 0-1 之间；若均值、最大值大于 1，必须判断是否为百分比、对数、标准化、金额或其他 transform；
- dummy / binary variable 是否只取 0/1；若最大值大于 1，必须追问它到底是强度指标、金额、数量、对数值还是命名错误；
- count / value / log variable 的单位、币种、价格调整、winsorize、加 1 取 log 等转换是否说清楚；
- mean、SD、min、max 是否存在不可能值、极端值或与变量叙述冲突；
- 不同表的 N 是否一致；若样本量变化，是否有 sample flow、缺失值和样本期说明；
- R²、显著性和 F-stat 不是本步骤主战场，但当它们暴露出量纲、样本、变量构造或模型口径问题时，应记录并路由到第 5 步或第 7 步。

这一步要用大白话写出“如果作者说它是 A，表里却长得像 B”，并把严重疑点写入 `notes/review-issue-ledger.md`。

### 5. 数据来源和合并

检查：

- 每个数据源的单位、时间、覆盖范围；
- 合并键和合并成功率；
- 样本流失和选择性；
- 是否有 firm id、product code、industry code、year harmonization；
- 是否报告了 sample construction table。

### 6. 样本限制和外部有效性

检查：

- 样本是否只覆盖特定规模、行业、地区、出口企业；
- 删除规则是否可能系统性排除弱企业、小企业、非出口企业或数据质量差企业；
- 样本与作者结论的推广范围是否一致。

### 7. 时间结构

检查：

- X、Y、controls、mechanisms 的时间先后；
- 控制变量是否可能是 post-treatment variables；
- 是否有滞后、采用前测量、pre-trend 或事件窗口；
- 数据版本和分类体系是否跨年份统一。

### 8. 机制变量和拓展变量

机制变量不是自动可信。检查：

- 是否真的测量机制概念；
- 是否只是另一个结果变量；
- 是否与主 Y 有机械关系；
- 是否需要中介路径或时序证明。

拓展变量要检查：

- 是否服务主贡献；
- 是否构造清楚；
- 是否只是扩大结果边界。

### 9. 审稿出口

最后输出：

- measurement strength：strong / moderate / weak / unclear；
- main construct-validity concerns；
- data/sample concerns；
- concrete author requests；
- issue ledger updates。

## 输出结构

~~~markdown
# Variable Data Measurement Audit

## Plain-Language Bottom Line

## Measurement Chain Overview

| Construct | Observed Variable | Data Source | Construction Steps | Interpretation Gap | Priority |
|---|---|---|---|---|---|

## Core Outcome Audit

## Core Treatment Audit

## Summary Statistics and Variable Scale Sanity Check

## Data Sources and Merge Audit

## Sample and External Validity

## Timing and Lag Structure

## Mechanism and Extension Variable Audit

## Measurement Claim Strength

## Concrete Author Requests

## Issue Ledger Updates
~~~

## 判断纪律

- 不重复第 2 步的抽取工作；只在需要证据时引用原文位置。
- 不把作者变量名当成概念本身；必须拆开“作者想测什么”和“数据实际测到什么”。
- 对代理变量、清单变量、跨库匹配变量和行业推企业变量保持高敏感度。
- 不把替代指标自动当作稳健；先判断替代指标是否仍测同一概念。
- 不生成最终审稿意见，只生成可核验的审稿素材。
