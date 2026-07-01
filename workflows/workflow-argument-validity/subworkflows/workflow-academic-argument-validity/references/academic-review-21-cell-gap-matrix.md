---
date: 2026-06-21
type: reference
status: structural-green / forward-test-pending
scope:
  - workflow-academic-argument-validity
  - academic-argument-arrow-audit
  - academic-argument-issue-selection
source_case:
  - /Users/narra/Documents/alib/Writer/03 Projects/审稿/J-260621-AI漂洗盲审/tasks/TASK03-真实审稿意见对照/outputs/skill-feedback-framework-21cell.md
---

# Academic Review 21-Cell Gap Matrix

## 用途

本 reference 用来把真实审稿案例暴露的漏点，放回学术论文论证 workflow 中定位。

它不是 21 个 Skill 的清单，而是一个诊断矩阵：

```text
7 个 workflow 阶段
x
3 层适配能力
=
判断某个漏点应该补到哪里
```

三层能力：

```text
通用论证层：所有论文和论证任务共享。
经管 / 社科实证层：实证论文的构念、代理变量、模型、识别、样本、推断与机制标准。
中文经管层：中文经管审稿语境中的指标方向、文本口径、本土制度语境、中文文献谱系和表达规范。
```

## 放置原则

不要把本矩阵直接拆成 21 个 Skill。

更稳的落位是：

- 通用层补到父 workflow、通用抽树、通用验箭头和通用选点规则；
- 经管 / 社科实证层由 `empirical-social-science-review-adapter` 承载；
- 中文经管层由 `chinese-management-econ-review-adapter` 承载；
- 具体案例留在 TASK、fixture、provenance 或 regression，不直接写进通用规则。

## 7 步 x 3 层

| 阶段 | 通用论证层 | 经管 / 社科实证层 | 中文经管层 |
|---|---|---|---|
| 1. 读稿抓论证 | 还原 root claim、X1/X2/Y、外层发表价值 claim 与内层发现 claim | 记录研究对象、核心变量、样本、模型、识别、机制、稳健性、外推 | 记录政策化拔高、指标方向、文本口径、中文制度语境和本土文献缺口 |
| 2. 抽作者论证树 | claim 层级递归展开到最小 evidence leaf | 强制显影 construct-proxy、sample-scope、model-identification、mechanism-evidence、robustness-threat | 对文本、指数、政策和制度语境变量额外记录方向、来源、语气和本土语境 |
| 3. 验箭头 | 问 `A 是否足以推出 B`，统一 status 与 qc_flags | 检查 construct-proxy fit、sample-scope fit、control-variable role、inference-clustering fit 等 | 检查 signed interpretation、text-source distinction、Chinese literature genealogy、local reviewer-sensitive reporting |
| 4. 领域学习 / 外部证据 | 集中处理 `needs-external-evidence`、`needs-method-qc`、`needs-source-qc` | 检索同类构念、代理变量、识别策略、聚类、bad control、机制证据标准 | 检索中文高质量文献、本土政策制度、中文期刊审稿语境和表达规范 |
| 5. 修箭头 | 为 weak/broken/unclear 箭头给补证据、补分析、降调路线 | 输出变量重构、替代指标、样本重切、识别增强、机制重做、推断修正 | 输出作者可执行的中文修改任务：解释方向、区分口径、补中文文献、降低政策化拔高 |
| 6. 选审稿问题 | 按 claim level 与 bottleneck 判断优先级 | 低层技术点若阻断核心因果、变量、机制或推断，可升级为 major candidate | 表格、变量解释、描述统计、表达问题若导致核心论证不可复核，可升级或作为 linked hold |
| 7. 写成审稿意见 | 按 issue arrow map 写：定位、断点、影响、建议 | 把技术问题翻译成可执行审稿要求 | 中文主体清楚，术语括注英文；不让内部 Skill 黑话进入正文 |

## 经管 / 社科实证层的抽象敏感点

- `construct-proxy fit`：理论构念是否能由当前代理变量承接；
- `sample-scope fit`：样本是否能支撑目标总体、机制和外推；
- `model-identification fit`：模型、识别和结果是否能支撑作者的因果语言；
- `control-variable role`：控制变量是否可能是 bad control、post-treatment control 或机制变量；
- `inference-clustering fit`：标准误、聚类层级和显著性推断是否与处理/冲击层级匹配；
- `mechanism-evidence strength`：机制检验是否只是相关通道，还是能支撑机制声称；
- `robustness-threat fit`：稳健性是否回应核心威胁，而不是同一偏误框架内重复验证；
- `descriptive-validity of constructed variables`：构造指标的方向、量纲、分布、异常值和可解释性是否清楚。

## 中文经管层的抽象敏感点

- `signed / directional index interpretation`：指标越大到底代表更强、更多、更负面，还是更正面；
- `text-based proxy distinction`：文本数量、语气、情感、来源、人工/机器抽取口径是否混合；
- `institutional-context sample-scope fit`：中文制度、监管、市场结构是否支持样本外推和机制解释；
- `Chinese literature genealogy`：是否遗漏中文高质量研究中的相邻概念、成熟指标或反向结论；
- `policy-language / rhetorical-expression control`：政策化、口号化或修辞化表达是否超过证据；
- `local reporting convention`：表格、变量定义、描述统计、稳健性和附录是否达到中文期刊可复核水平；
- `local reviewer-sensitive clarification`：虽然低层，但若不澄清会导致核心变量或结果无法判断。

## 反哺状态

```text
structural-green
forward-test-pending
```

它已经可以指导 Skill 补强，但不能宣称为经管审稿通用定论。后续每个新案例应把新增漏点先写回 TASK，再判断是否进入 adaptor reference。

