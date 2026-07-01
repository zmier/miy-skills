---
name: argument-arrow-repair-mapping
description: 通用断箭头修复映射复合 Skill。用于在 argument-arrow-audit 已经诊断出 weak、broken、unclear、needs-qc 或 needs-external-evidence 箭头之后，先判断现有 repair menu 是否足够、是否需要检索/深读同类文献来学习证据标准，再把每个断点映射为可增强的证据、补充实验、补充分析、口径澄清、外部检索或降调方案；位于验箭头之后、issue selection 之前，不重新验箭头，也不决定 major concern。
---

# Argument Arrow Repair Mapping

## 定位

本 Skill 是“验箭头”和“选问题”之间的桥：

```text
argument-tree-extraction
-> argument-arrow-audit
-> argument-arrow-repair-mapping
-> argument-issue-selection
-> writing / review drafting
```

分层原则：

```text
验箭头 = 诊断：A 是否足以推出 B？
修复映射 = 治疗方案：如果推不出，补什么证据 / 分析 / 实验可以增强？补不了时如何降调？
选问题 = 决策：哪些断点值得写成 major / minor / revision action？
```

不要把修复建议塞回验箭头。验箭头必须保持诊断纯度；修复映射才引入“怎么补”“补到什么强度”“补不起怎么降调”。

## 执行模式

每次调用本 Skill，必须先在 TASK 或输出顶部声明模式：

```text
mode: menu-assisted
```

适用：已有领域 repair menu 足以覆盖主要断点，例如材料/器件论文已读取 `materials-device-repair-menu.md`。允许使用既有 menu，但必须标注 `knowledge_source: existing-menu`，不得把 menu 伪装成模型临场判断。

```text
mode: learning-required
```

适用：新领域、新方法、新实验技术、既有 menu 不覆盖，或用户要求“不要用小抄”。必须先生成 `repair-search-strategy.md`，再通过检索摘要、综述、顶刊原文、方法指南、官方文档或补充材料学习“别人如何证明这类箭头”，生成临时 `case-repair-menu.md` 和 `arrow-repair-map.md`。

```text
mode: hybrid
```

适用：部分断点已有 menu，部分断点没有。已有部分可用 menu；未知部分必须走 learning-required 路线，并在 `repair-knowledge-gap.md` 中标记。

若调用者未指定，默认：

```text
mode: hybrid
```

## 知识来源审计

修复映射前先判断每类断点的知识来源：

| knowledge_source | 含义 | 使用要求 |
|---|---|---|
| `general-logic` | 通用论证逻辑即可推出的修复，如降调、补定义、补口径 | 可以直接生成 |
| `existing-menu` | 领域 repair menu 已覆盖 | 必须说明使用哪个 menu / reference |
| `abstract-scan` | 摘要足以识别同类 claim、metric、method 或 comparator | 只能生成 candidate repair routes |
| `fulltext-pattern` | 需要原文、图表、方法、补充材料才能知道证据包 | 必须标记需深读或已深读来源 |
| `case-derived` | 来自真实审稿意见、返修、case UAT | 只能作为候选，需去个案化后沉淀 |
| `unknown` | 现有知识不足 | 生成 `repair-knowledge-gap`，不得硬编 |

摘要通常只适合识别领域、同类论文、常见 claim / metric / method 和候选 comparator；真正的 repair pattern 往往在 Methods、Results、Figure captions、Supplementary Information、Appendix、Robustness checks、Control experiments、Benchmark tables 或 reviewer response 中。

对 `abstract-scan` 产物必须使用条件式：

```text
candidate repair route
needs-fulltext-pattern-check
```

不得写成已确认领域标准。

## 输入

- `arrow-audit-table.md` 或场景专用审计表；
- `arrow-break-summary.md`；
- `external-evidence-ledger.md`；
- `qc_flags` / `needs-external-evidence` / `needs-qc` 清单；
- 任务目标：论效题、GRE、学术审稿、写作自审、返修准备等。

## 路由

| 场景 | 调用 |
|---|---|
| 学术论文审稿、投稿前自审、返修准备 | `skills/academic-arrow-repair-mapping/SKILL.md` |
| 论效题 / GRE Argument | 父层轻量处理：把修复映射写成“还需要什么证据 / 问什么问题 / 哪个假设需证明” |
| 普通政策、商业、技术论证 | 使用父层协议直接生成 repair map，必要时沉淀新子 Skill |

学术论文中若需要检索学习 repair knowledge，由学术子 Skill 路由到：

```text
skills/academic-arrow-repair-mapping/skills/academic-repair-knowledge-learning/SKILL.md
```

## 通用主轴

1. 接收断点：
   - 只消费已审计箭头；
   - 只处理 `weak / broken / unclear / needs-qc / needs-external-evidence`；
   - `strong` 一般不进入修复映射，除非任务要求说明“如何进一步增强”。
2. 识别断点类型：
   - `concept-mismatch`、`measurement-mismatch`、`causal-leap`、`sample-weakness`、`comparison-mismatch`、`overclaim`、`evidence-qc-gap` 等；
   - 保留原 `arrow_id`、`from_node`、`to_node` 和 `impact_on_root`。
3. 做知识来源审计：
   - 判断每类断点是 `general-logic`、`existing-menu`、`abstract-scan`、`fulltext-pattern`、`case-derived` 还是 `unknown`；
   - 已有 menu 不够时，不得硬编，先生成 `repair-knowledge-gap.md`；
   - 新领域或新方法必须先生成 `repair-search-strategy.md`，再执行摘要扫描和必要的原文证据包抽取。
4. 如需学习，先生成临时知识：
   - 摘要扫描用于识别同类论文、常见 claim、metric、method 和 comparator；
   - 原文 / 图表 / 补充材料深读用于抽取具体 evidence package；
   - 输出 `case-repair-menu.md`，并标注哪些规则可迁移、哪些只适用于本案。
5. 映射修复动作：
   - 补概念定义或边界；
   - 补测量口径、变量构造或指标解释；
   - 补对照、稳健性、机制、替代解释排除；
   - 补文献、官方资料、方法来源或引用核验；
   - 补表格、图、公式、原始数值 QC；
   - 降调结论，把强声称改成当前证据能支撑的弱声称。
6. 区分修复强度：
   - `minimum_repair`：最低限度能让读者理解或暂时相信；
   - `strong_repair`：真正增强箭头、接近可发表/可接受标准；
   - `fallback_if_unavailable`：补不了时如何改写、降调或移除。
7. 标记修复成本与选点含义：
   - `repair_cost: low / medium / high / not-feasible-with-current-data`;
   - `selection_implication: major-candidate / minor-candidate / revision-action / hold-for-qc / hold-for-external-evidence`。
8. 输出 `arrow-repair-map.md`，交给 `argument-issue-selection`。

## 输出字段

模板见 `assets/arrow-repair-map-template.md`。

```text
repair_id
target_arrow_id
break_type
why_arrow_breaks
repair_type
minimum_repair
strong_repair
fallback_if_unavailable
expected_effect_on_claim
repair_cost
external_or_qc_needed
selection_implication
knowledge_source
source_reference_or_learning_route
notes
```

可选输出：

```text
repair-knowledge-learning-plan.md
repair-search-strategy.md
case-repair-menu.md
repair-knowledge-gap.md
repair-feedback-candidates.md
```

## 完成标准

- 每条 repair 都绑定已审计 `arrow_id`；
- 不新增未审计的问题；
- 不把“作者应该做什么”写成“作者已经错了”的证据；
- 对 `needs-qc` 和 `needs-external-evidence` 保持条件式表达；
- 每条修复建议都说明它增强哪根箭头，而不是泛泛说“建议补充实验/文献”；
- 每条修复建议都标注 `knowledge_source`，说明来自通用逻辑、既有 menu、摘要扫描、原文深读、case 反哺还是未知；
- `abstract-scan` 只能产生候选路线，不能替代 fulltext evidence standard；
- 如果没有足够领域知识判断该补什么，标记 `repair-knowledge-gap`，并指出需要查的方法、文献、官方资料或专家知识。
