---
name: manuscript-causal-identification-audit
description: 对学术手稿的因果识别做大白话审查。用于外部审稿、投稿前自审和论文方法诊断中，把作者声称的因果发现还原为实际观测关系，检查二者是否匹配，并用 DAG、后门路径、前门路径、IV、固定效应、控制变量、机制检验和稳健性检验分析识别是否支撑结论。本 Skill 不生成最终审稿意见。
---

# Manuscript Causal Identification Audit

## 定位

本 Skill 是 workflow-paper-writing-review 中的第 5 步：方法识别审查。

它负责回答一个朴素问题：

```text
作者实际观察到了什么？作者声称发现了什么？从前者跳到后者，中间的因果桥够不够稳？
```

输出应优先使用中文大白话，同时保留必要英文术语，如 `observed finding`、`claimed causal finding`、`DAG`、`backdoor path`、`frontdoor path`、`IV`、`exclusion restriction`。

## 触发条件

当用户提出以下问题时使用：

- “因果识别策略是什么”
- “这个能说导致吗”
- “实际发现和作者声称发现是否 match”
- “用大白话讲，不要绕圈子”
- “能不能画 DAG”
- “前门、后门怎么分析”
- “IV / DiD / PSM / FE 是否可靠”
- “方法审查 / identification audit / causal audit”

## 输入

优先读取：

- `notes/quick-read-contribution-chain.md`
- `notes/review-issue-ledger.md`
- 段落编号 manuscript Markdown
- 方法、变量、结果、稳健性、机制相关段落和表格

当需要系统审查回归表、IV 表、PSM 表、稳健性表、机制表或异质性表时，读取：

```text
references/statistical-identification-table-audit.md
```

## 输出

默认输出到：

```text
notes/causal-identification-audit.md
```

建议使用模板：

```text
templates/causal-identification-audit-template.md
```

同时更新：

```text
notes/review-issue-ledger.md
```

## 分析顺序

### 1. 实际观测发现 vs 作者上升发现

先拆两句话，不要直接沿用作者抽象说法：

- actual observed finding / 实际观测发现：数据中真正被回归或比较的 X、Y 是什么；
- claimed causal finding / 作者上升发现：作者把这个关系解释成什么因果发现；
- match status：matched / partly matched / overstated / unclear；
- bridge assumptions：要让两句话等价，必须成立哪些假设。

示例格式：

```text
实际观测发现：进口机器人相关产品的企业，其某类产品出口占比更高。
作者上升发现：机器人采用导致出口产品结构升级。
是否匹配：partly matched；依赖 X 是否真是机器人采用、Y 是否真是结构升级、识别是否排除反向因果和共同原因。
```

### 2. 因果对象

明确：

- treatment / X：作者想解释的处理或冲击；
- observed X：数据里实际测到的 X；
- outcome / Y：作者想解释的结果；
- observed Y：数据里实际测到的 Y；
- unit：企业、地区、个人、产品、行业或国家；
- time order：X 和 Y 的时间先后；
- estimand：作者想估计的是 ATE、ATT、LATE、相关性、预测关系还是机制关联。

如果作者没有说明 estimand，写“大概率是想解释平均因果效应，但未清楚定义”。

### 3. DAG 大白话建模

用 Mermaid 画一个最小 DAG。只放审稿判断需要的节点：

- X / treatment；
- Y / outcome；
- U / unobserved confounders；
- observed controls；
- fixed effects absorbed factors；
- instrument or shock；
- mechanisms / mediators；
- sample selection or collider if relevant。

DAG 后必须用中文解释每条关键箭头：

- “这条箭头表示作者想证明的因果路径”；
- “这条箭头表示反向因果”；
- “这条箭头表示共同原因，也就是后门路径”；
- “这条箭头表示机制变量，不能随便当普通控制变量”。

### 4. 后门路径 / Backdoor

列出最可能的 backdoor paths：

```text
X <- U -> Y
X <- industry trend -> Y
X <- firm capability -> Y
```

对每条路径判断：

- 作者用什么处理：controls / FE / DiD / IV / PSM / trend / placebo / robustness；
- 是否真的堵住；
- 如果没堵住，偏误方向可能是什么；
- 需要什么额外证据。

### 5. 前门路径 / Frontdoor

只有当作者的机制变量可能形成完整中介链时，才使用 frontdoor 分析。不要硬套。

检查：

- X 是否影响 mediator；
- mediator 是否影响 Y；
- X 到 Y 的直接路径是否被 mediator 完整承接；
- mediator 与 Y 之间是否仍有未控制混杂；
- 作者机制检验是 frontdoor 识别，还是只是“X 对 mediator 有影响”的结果回归。

多数应用论文的机制检验不是严格 frontdoor。此时要大白话写：

```text
这些机制结果说明 X 和若干中间变量相关，但还不能证明完整中介路径。
```

### 6. IV 审查

如果作者使用 IV，逐条检查：

- relevance：Z 是否影响 X；
- exclusion restriction：Z 是否只能通过 X 影响 Y；
- independence：Z 是否与未观测混杂无关；
- monotonicity：是否可理解为对一类 compliers 的 LATE；
- first-stage strength：是否弱工具；
- interpretation：IV 估计的是谁的效应，而不是所有样本平均效应。

大白话模板：

```text
这个 IV 的意思是：用 Z 推动 X 的那部分变化来解释 Y。
它最怕的问题是：Z 自己也会影响 Y，或者 Z 代表了别的趋势。
```

### 7. 控制变量和固定效应

区分：

- 好控制：X 之前就存在、同时影响 X 和 Y 的变量；
- 坏控制：X 之后才发生的机制变量或结果变量；
- 固定效应：能吸收哪些不变因素，不能吸收哪些随时间变化的冲击；
- 过度控制：把真实机制控制掉；
- 不足控制：漏掉行业-年份、地区-年份、产品-年份等共同冲击。

### 8. PSM / robustness

PSM 只能帮助比较可观测相似的样本，不能自动解决不可观测混杂。稳健性检验要说清楚它堵的是哪条路径，而不是把“做了很多检验”当成因果识别。

### 9. 统计证据与识别表审查

如果稿件有回归表、IV 表、PSM 表、稳健性表、机制表或异质性表，必须把统计证据接回因果识别问题。必要时读取 `references/statistical-identification-table-audit.md`。

检查：

- 主回归系数方向、显著性、大小和经济意义；
- 加入 controls / FE 后系数是否稳定；
- 样本量、R²、标准误聚类和变量量纲是否支持解释；
- IV 第一阶段、F-statistic、weak-IV risk、第二阶段和 LATE 解释；
- PSM balance / overlap 是否报告；
- 稳健性检验到底堵哪条 DAG 威胁，是否只是换口径或堆表；
- 机制和异质性是否被作者解释过度。

大白话原则：

```text
DAG 告诉我们哪里可能偏；统计表告诉我们作者有没有拿出证据去堵这个偏。
显著不等于因果，F 值强不等于排除限制成立，稳健性多不等于每条威胁都被堵住。
```

### 10. 审稿出口

最后输出：

- causal claim strength：strong / moderate / weak / descriptive only；
- downgrade suggestion：作者因果表述是否需要降级；
- major concerns；
- minor concerns；
- concrete author requests；
- issue ledger updates。

## 输出结构

~~~markdown
# Causal Identification Audit

## Plain-Language Bottom Line

## Actual Observed Finding vs Claimed Causal Finding

| Item | Plain Chinese | Evidence Location | Concern |
|---|---|---|---|
| Actual observed finding |  |  |  |
| Claimed causal finding |  |  |  |
| Match status | matched / partly matched / overstated / unclear |  |  |
| Bridge assumptions |  |  |  |

## Causal Object

## DAG

```mermaid
flowchart LR
```

## DAG Explanation in Plain Chinese

## Backdoor Analysis

| Backdoor Path | Why It Matters | Author's Strategy | Does It Block? | Remaining Concern |
|---|---|---|---|---|

## Frontdoor / Mechanism Analysis

## IV / Research Design Audit

## Controls and Fixed Effects

## Robustness and PSM

## Statistical Evidence and Identification Table Audit

| Evidence Table | What It Is Supposed to Prove | Key Statistical Evidence | Does It Support the Causal Claim? | Remaining Concern | Route |
|---|---|---|---|---|---|

## Causal Claim Strength

## Issue Ledger Updates
~~~

## 判断纪律

- 不替作者美化变量：数据里是什么就说什么。
- 不把“相关性 + 固定效应 + 很多稳健性”自动当成因果。
- 不把机制检验误写成严格 frontdoor，除非作者真的满足前门条件。
- 不用术语压人；每个方法判断都要能翻译成大白话。
- 不生成最终审稿意见，只生成可核验的审稿素材。
