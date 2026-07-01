---
date: 2026-06-20
type: reference
status: seed
scope:
  - experimental-design
  - quasi-experimental-design
  - causal-identification
  - dag-ready-evidence
---

# Identification Design Adapter

## 定位

本 adapter 用于 paper 抽树阶段抽取实验设计、准实验设计和因果识别设计的信息。

它不负责判断识别是否成立；它负责把后续 `academic-argument-arrow-audit`、DAG 分析、前门/后门分析需要的作者 claim 和 evidence 抽完整。

核心边界：

```text
设计事实 = evidence
设计有效性判断 = claim
```

## 何时读取

遇到以下内容时必须读取本 adapter：

- randomized experiment / RCT / field experiment / lab experiment;
- natural experiment / quasi-experiment;
- DID / event study / staggered DID;
- IV / 2SLS;
- RD / RDD;
- PSM / matching / entropy balancing;
- synthetic control;
- regression discontinuity / cutoff rule;
- policy shock / institutional shock / event shock;
- causal graph / mediation / mechanism identification;
- 作者声称 causal effect、identification、exogenous variation、natural experiment、random assignment。

## Claim 抽取

识别设计相关 claim 通常包括：

```text
C-ID: 本设计能够识别 X 对 Y 的因果影响
C-ID-RAND: 处理分配近似随机 / 外生
C-ID-COMP: 处理组与对照组可比
C-ID-PT: DID 满足平行趋势
C-ID-IV-REL: IV 与内生解释变量相关
C-ID-IV-EXCL: IV 只通过 X 影响 Y
C-ID-RD: cutoff 附近个体近似随机
C-ID-NOSPILL: 不存在严重溢出 / 干扰
C-ID-NOATTR: 不存在严重选择性退出 / 缺失
C-ID-MECH: 机制路径 M 能解释 X -> Y
```

这些都是 claim，因为都可以继续问：

```text
为什么？
作者用什么设计事实或结果支撑？
```

## Evidence 抽取

识别设计相关 evidence 必须尽量拆到最小可核查单位。

### 通用设计 evidence

```text
E-DES-XDEF: treatment / exposure / shock 的定义
E-DES-YDEF: outcome 的定义
E-DES-GROUP: 处理组 / 对照组 / 比较组定义
E-DES-TIME: 处理发生时间、观察窗口、事件窗口
E-DES-SAMPLE: 样本来源、筛选规则、最终样本量
E-DES-MODEL: 回归公式、固定效应、控制变量、聚类层级
E-DES-BALANCE: 基线平衡表中的具体变量、差异、显著性
E-DES-PLACEBO: placebo / falsification test 的具体设置和结果
E-DES-MISSING: attrition / missingness 的比例和组间差异
```

### RCT / 实验

```text
E-RCT-ASSIGN: 随机分配规则
E-RCT-COMPLIANCE: compliance / take-up / manipulation check
E-RCT-BALANCE: 表 1 基线平衡结果
E-RCT-ATTRITION: attrition rate 与组间差异
E-RCT-SUTVA: spillover / interference 处理说明
E-RCT-RESULT: treatment effect 表格单元格
```

### DID / Event Study

```text
E-DID-POLICY: 政策 / 冲击发生时间和适用对象
E-DID-TREAT: treatment group 定义
E-DID-CONTROL: control group 定义
E-DID-POST: POST 编码规则
E-DID-FE: unit / time / industry-year 等固定效应
E-DID-CLUSTER: 标准误聚类层级
E-DID-PRETREND-FIG: 平行趋势图的处理前系数
E-DID-PRETREND-TAB: 事件研究表中处理前项
E-DID-PLACEBO: placebo shock / pseudo treatment 结果
E-DID-STAGGER: staggered DID / Bacon / cohort 处理说明
```

### IV / 2SLS

```text
E-IV-ZDEF: 工具变量定义
E-IV-FIRST: 第一阶段系数和 F 值
E-IV-REL: 相关性说明
E-IV-EXCL-TEXT: 作者对排除限制的制度解释
E-IV-OVERID: 过识别检验结果
E-IV-REDUCED: reduced form 结果
E-IV-MONO: 单调性 / LATE 适用范围说明
```

### RD / RDD

```text
E-RD-RUNNING: forcing / running variable 定义
E-RD-CUTOFF: cutoff 规则
E-RD-BW: bandwidth 选择
E-RD-DENSITY: McCrary / density manipulation test
E-RD-COVAR: 协变量连续性检验
E-RD-DONUT: donut RD / robustness bandwidth
E-RD-GRAPH: cutoff 附近图像 evidence
```

### Matching / Weighting / Synthetic Control

```text
E-MATCH-METHOD: PSM / matching / entropy balancing 方法说明
E-MATCH-BALANCE: 匹配前后协变量平衡
E-MATCH-SUPPORT: common support / overlap
E-SCM-DONOR: donor pool 定义
E-SCM-PREFIT: treatment 前拟合质量
E-SCM-PLACEBO: placebo unit / placebo time 结果
```

## DAG-ready 输出

如果后续可能做 DAG / 前门 / 后门分析，`evidence-ledger.md` 或 QC 中应尽量保留以下字段或 notes：

```text
treatment X
outcome Y
mediator M
confounders C
instrument Z
running variable R
selection / sample restriction S
time ordering
unit of analysis
cluster / aggregation level
possible spillover channel
author-claimed exclusion / ignorability / parallel trend
```

这些信息仍然是 paper 抽树阶段的 evidence / claim 抽取，不是 DAG 结论。DAG 判断属于后续验箭头或因果识别审查。

## Handoff to Arrow Audit

paper 抽树阶段只在 `extraction-qc.md` 标记：

```text
ready-for-academic-arrow-audit
dag-ready: yes / partial / no
missing-identification-design-evidence
needs-design-qc
```

若缺少关键识别设计 evidence，不要写“识别不成立”，只写：

```text
缺少用于后续验箭头的设计事实或识别假设证据。
```

## Red Flags

- 把“DID 设计”当成一个 evidence leaf，不拆 treatment/control/post/FE/pretrend；
- 把“IV 有效”当成 evidence，而不是 claim；
- 没抽第一阶段 F 值却给 IV 识别留下完整状态；
- 没抽平行趋势证据却让 DID claim 进入 ready 状态；
- 把“随机分配规则”直接写成“因果识别成立”；
- 在 paper 抽树阶段判断前门/后门是否成立。
