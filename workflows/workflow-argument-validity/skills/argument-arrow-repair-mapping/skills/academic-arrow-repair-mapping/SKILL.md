---
name: academic-arrow-repair-mapping
description: 学术论文断箭头修复映射 Skill。用于在 academic-argument-arrow-audit 与 academic-field-evidence-learning 之后，消费 weak、broken、unclear、needs-qc 或 needs-external-evidence 箭头、external-evidence-ledger、domain-map、case-repair-menu 等产物，把每个学术断点映射为可执行的补文献、补实验、补模型、补变量说明、补表图 QC、补稳健性、补机制证据或结论降调方案；输出 arrow-repair-map，供 academic-argument-issue-selection 选择 major/minor/revision action。
---

# Academic Arrow Repair Mapping

## 定位

本 Skill 位于：

```text
academic-argument-arrow-audit
-> academic-field-evidence-learning
-> academic-arrow-repair-mapping
-> academic-argument-issue-selection
```

它回答的问题不是：

```text
A 是否足以推出 B？
```

而是：

```text
如果 A 推不动 B，作者需要补什么，才能让这根箭头变强？
如果补不了，B 应该怎样降调？
```

本 Skill 不重新抽树，不重新全量验箭头，不决定哪些问题写成 major concern。

## 执行模式

继承父 Skill 的三种模式：

```text
mode: menu-assisted
mode: learning-required
mode: hybrid
```

默认 `hybrid`。也就是说：材料/器件等已覆盖断点可以读取既有 reference；未覆盖的新领域、新方法、新统计或新实验技术，必须先进入第 4 步 `academic-field-evidence-learning`，不得在本 Skill 中凭空生成 repair 标准。

## 输入

- `academic-arrow-audit-table.md`；
- `academic-arrow-break-summary.md`；
- `issue-selection-candidates.md`；
- `external-evidence-request.md`；
- `external-evidence-ledger.md`；
- `domain-map.md`；
- `review-risk-radar.md`；
- `handoff-to-repair-mapping.md`；
- `case-repair-menu.md`；
- `fulltext-pattern-ledger.md`；
- `review-sensitivity-map.md`；
- 表格、图、公式、引用、方法或文献检索 QC 标记。

## 输出

```text
arrow-repair-map.md
repair-knowledge-gap.md（如有新增学习缺口）
repair-feedback-candidates.md（如有可迁移规则）
```

## 主轴

1. 筛选待修复箭头：
   - 只处理 `weak / broken / unclear / needs-qc / needs-external-evidence`；
   - 保留 `arrow_id -> weakened_node -> impact_on_X1_X2_Y`；
   - `needs-qc` 不直接写强补救，先写核验动作；
   - `needs-external-evidence` 不直接写定论，先写检索或资料路线。
2. 判断断点属于哪类学术修复：
   - `concept / construct repair`：补概念边界、构念层级、定义回代；
   - `measurement repair`：补变量构造、量纲、口径、替代指标；
   - `sample / setting repair`：补样本代表性、机制场景、外部有效性；
   - `identification / causal repair`：补对照、DAG、前趋势、工具变量、安慰剂、机制排除；
   - `statistical / reporting repair`：补系数、显著性、F 值、R2、置信区间、效应量、表格一致性；
   - `literature / contribution repair`：补文献谱系、SOTA 对照、已有研究差异；
   - `mechanism repair`：补机制检验、替代机制排除、链路证据；
   - `claim downgrade`：当前数据无法补足时，降调发现、贡献或政策含义。
3. 做知识来源审计：
   - 已有领域 reference 覆盖时，标记 `knowledge_source: existing-menu`；
   - 只需逻辑降调、补定义、补口径时，标记 `knowledge_source: general-logic`；
   - 摘要扫描只能识别候选同类论文、claim、metric、method、comparator，标记 `knowledge_source: abstract-scan`；
   - 具体 evidence package 如实验参数、控制组、图表指标、稳健性组合、补充材料字段，通常需要 fulltext / figure / supplement，标记 `knowledge_source: fulltext-pattern`；
   - 无法判断时标记 `knowledge_source: unknown` 并写入 `repair-knowledge-gap.md`。
4. 如需学习，先回到第 4 步 `academic-field-evidence-learning`：
   - 本 Skill 优先消费既有 `case-repair-menu.md`、`fulltext-pattern-ledger.md` 和 `handoff-to-repair-mapping.md`；
   - 如果发现新的未知修复知识，写入 `repair-knowledge-gap.md`；
   - 不在本步骤另起零散检索或深读。
5. 形成临时 `case-repair-menu.md`：
   - `arrow_type`；
   - `common_break`；
   - `minimum_evidence`；
   - `strong_evidence_package`；
   - `fallback_downgrade`；
   - `source_basis`；
   - `transfer_status: case-only / candidate-general / stable-menu`。
6. 生成三层建议：
   - `minimum_repair`：最低限度澄清或补充；
   - `strong_repair`：真正增强箭头的实验/分析/证据；
   - `fallback_if_unavailable`：补不了时如何改写或降调。
7. 标记修复成本：
   - `low`：文字澄清、引用补充、表格解释、变量口径说明；
   - `medium`：补稳健性、补替代指标、补机制回归、补已有数据分析；
   - `high`：新增实验、新增样本、新增数据、重跑识别设计；
   - `not-feasible-with-current-data`：当前数据或设计无法补救，只能降调。
8. 给选点层提供提示：
   - `major-candidate`：断点重要且强修复成本高或影响 X2/Y；
   - `minor-candidate`：断点局部、低成本可修；
   - `revision-action`：适合直接写成“建议作者补充...”；
   - `hold-for-qc`：需先核验表图/公式/原文；
   - `hold-for-external-evidence`：需先查文献、方法、官方资料。

## 领域路由

按论文类型选择需要读取的 reference：

| 论文类型 / 断点 | Reference |
|---|---|
| 材料、器件、能源收集、传感器、柔性电子、可穿戴、工程实验论文 | `references/materials-device-repair-menu.md` |
| 经济学、管理学、社会科学实证论文 | 暂由本 Skill 主轴处理；遇到高频修复菜单再沉淀 reference |
| 新统计方法、专门实验技术或前沿方法 | 先标记 `repair-knowledge-gap`，再按外部证据路线检索学习 |

当任何断点被标记为 `knowledge_source: unknown`、`needs-fulltext-pattern-check`，或当前领域没有可靠 repair menu 时，回到 workflow 第 4 步：

```text
../../skills/academic-field-evidence-learning/SKILL.md
```

该集中学习层负责生成或编排：

```text
repair-search-strategy.md
repair-knowledge-learning-plan.md
abstract-scan-ledger.md
deep-read-shortlist.md
fulltext-pattern-ledger.md
case-repair-menu.md
repair-learning-qc.md
handoff-to-repair-mapping.md
```

然后本 Skill 再消费 `case-repair-menu.md` 生成 `arrow-repair-map.md`。

## 外部知识纪律

如果不知道某类断点该补什么，不能硬编实验或分析。必须写：

```text
repair-knowledge-gap:
  target_arrow_id:
  missing_knowledge:
  why_current_references_insufficient:
  needed_route: literature / official-doc / method-paper / expert-qc / source-figure-qc
  proposed_feedback_target:
```

对学术论文，修复建议优先来自：

- 本文同类顶刊或高质量论文的通行证据结构；
- 方法原始论文、官方文档、手册或权威综述；
- 真实审稿意见、返修意见和 case UAT 的可迁移经验；
- 表图、公式、原始数据的 source QC。

不得把普通常识包装成领域实验标准。

## 文献学习纪律

当进入 `learning-required` 或 `hybrid` 的未知部分时：

- 优先消费第 4 步的摘要扫描、领域地图、原文证据包和 `case-repair-menu.md`；
- 不把摘要扫描直接当成强 repair 标准；
- 若问题是“这类箭头具体怎么证明”，通常需要第 4 步提供原文、图表、方法、补充材料或 appendix 的 pattern；
- 如果第 4 步没有完成文献检索或全文获取，只能标记 `hold-for-field-learning` / `needs-fulltext-pattern-check`；
- 只把多篇文献或权威来源反复出现的做法沉淀为 general menu；单篇 case 只标 `case-only` 或 `candidate-general`。

摘要大概率够用的问题：

```text
领域是否活跃；
同类 claim 是否存在；
常用 metric / material / method 名称；
潜在 comparator。
```

通常必须看原文或补充材料的问题：

```text
具体控制实验；
图表指标组合；
benchmark table 字段；
稳健性组合；
实验条件、时间、浓度、负载、样本规则；
方法假设和验收标准。
```

## 输出写法

用中文主体阐述，必要英文术语放括号中。每条 repair 用大白话说明：

```text
作者现在用 A 推 B；
这根箭头现在的问题是什么；
最少要补什么；
真正强的补法是什么；
如果做不到，结论应该降到什么范围。
```

## 完成标准

- 每条 repair 都绑定 `target_arrow_id`；
- 每条 repair 都说明补强的是哪一根 `A -> B`；
- 不把诊断、修复和选点混在一张表里；
- `needs-qc` 先给 QC 动作，不能直接写成 confirmed weakness；
- `needs-external-evidence` 优先消费第 4 步 `external-evidence-ledger.md`；若没有学习产物，标记 `hold-for-field-learning`，不能直接写成 confirmed weakness；
- 对材料/器件/工科实验论文，若使用既有菜单，已读取 `references/materials-device-repair-menu.md` 并标注 `knowledge_source: existing-menu`；
- 对新领域或 menu 不覆盖断点，已消费第 4 步 `academic-field-evidence-learning` 产物，或已输出 `repair-knowledge-gap.md` 说明为什么需要回到第 4 步补学；
- 输出可直接交给 `academic-argument-issue-selection`，帮助判断哪些问题“可写、可修、影响大”。
