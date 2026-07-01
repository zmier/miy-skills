---
name: empirical-social-science-review-adapter
description: 学术验箭头中的经管/社科实证论文适配器。用于在 academic-argument-arrow-audit 中，把作者论证树和 evidence ledger 映射为经管/社科实证审稿敏感箭头，检查构念-代理变量、样本-总体、模型-因果声称、控制变量角色、聚类推断、机制证据、稳健性威胁和构造变量可解释性；输出 empirical-review-sensitivity-map、empirical-arrow-candidate-ledger、method/external evidence 请求，并可路由到中文经管子适配器。
---

# Empirical Social Science Review Adapter

## 定位

这是 `academic-argument-arrow-audit` 的诊断路由型子 Skill。

它不重跑抽树，不写审稿意见，不直接做文献检索。它只回答：

```text
对于一篇经管 / 社科实证论文，
哪些作者箭头需要用实证审稿标准重新显影和优先审计？
```

主轴仍然是：

```text
arrow_id: A -> B
A 是否足以推出 B
```

不要把本 Skill 写成“经管 checklist”。所有敏感点都必须绑定作者树中的 `arrow_id`、`from_node`、`to_node`、`evidence_ids` 和 `impact_on_X1_X2_Y`。

## 触发条件

满足任一条件时调用：

- 论文是经济学、金融、会计、管理、公共管理、社会科学或相邻实证研究；
- 论文使用回归、DID、IV、PSM、RDD、面板模型、事件研究、文本指标、问卷/实验、数据库或政策冲击；
- 用户要求判断“变量是否可靠”“识别是否成立”“显著性/聚类/R 方/F 值”等；
- `academic-argument-arrow-audit` 发现 construct、proxy、sample、model、mechanism、robustness 或 inference 相关断点。

若论文是中文经管或中文社科审稿语境，还要调用：

```text
skills/chinese-management-econ-review-adapter/SKILL.md
```

## 输入

```text
canonical-node-ledger.md
canonical-edge-ledger.md
evidence-ledger.md
paper-argument-tree.md
academic-argument-spine.md
internal-arrow-audit-table.md
external-evidence-request.md
extraction-qc.md
restored manuscript Markdown
table / figure / formula QC logs
```

若缺少 canonical ledgers，不要补造作者树；在输出中标记：

```text
input_status: incomplete-tree-input
missing:
```

## 输出

写入当前 TASK 的 `outputs/`：

```text
empirical-review-sensitivity-map.md
empirical-arrow-candidate-ledger.md
empirical-method-qc-request.md
handoff-to-field-learning.md
handoff-to-issue-selection.md
```

若触发中文经管子适配器，还要消费或合并：

```text
chinese-reviewer-sensitive-candidates.md
chinese-literature-gap-request.md
local-expression-and-format-qc.md
```

## 主流程

1. 识别实证 claim spine：

   ```text
   X construct
   X proxy / treatment / shock
   Y construct
   Y proxy / outcome
   sample / population
   model / identification
   mechanism / channel
   robustness / alternative explanations
   contribution / policy or managerial claim
   ```

2. 从 canonical edge ledger 中标出经管/社科实证敏感箭头：

   ```text
   construct -> proxy
   proxy / treatment -> X
   Y proxy -> Y construct
   sample -> target population
   model / design -> causal claim
   control set -> estimated relationship
   standard error / clustering -> significance claim
   mechanism test -> mechanism claim
   robustness test -> threat addressed
   result -> contribution / policy implication
   ```

3. 对每条敏感箭头写入 `empirical-review-sensitivity-map.md`：

   ```text
   sensitivity_id
   target_arrow_id
   empirical_sensitivity_type
   from_node
   to_node
   evidence_ids
   why_sensitive
   impact_on_X1_X2_Y
   required_internal_check
   external_evidence_need
   suggested_qc_flags
   ```

4. 生成 `empirical-arrow-candidate-ledger.md`：

   ```text
   arrow_id
   arrow_plain_language
   empirical_type
   current_status_if_known
   likely_break_type
   evidence_basis
   qc_flags
   needs_field_learning
   candidate_issue_if_bottleneck
   ```

5. 对需要方法、文献、官方资料或数据源标准才能判断的箭头，生成 `empirical-method-qc-request.md` 和 `handoff-to-field-learning.md`。
6. 若论文处于中文经管语境，调用中文子适配器，并把它的候选项合并为 `local_context_candidates`、`local_literature_requests`、`local_reporting_qc`。
7. 移交回 `academic-argument-arrow-audit`。本 Skill 不直接决定 major concern。

## 敏感类型

读取：

```text
references/empirical-social-science-arrow-types.md
```

不要硬编码单篇论文对象。比如不要写“某类专利指标一定有问题”或“某类样本一定太宽”；应写成：

```text
construct-proxy fit
sample-scope fit
descriptive-validity
```

再由具体 `evidence_ids` 解释为什么在当前稿件中触发。

## 完成标准

- 每个敏感点都绑定 `target_arrow_id`；
- 每个敏感点都能回到作者树或 evidence ledger；
- 不把“经管常见问题”写成没有证据锚点的泛泛提醒；
- 不把低层技术点直接升级为 major，只标记它可能阻断的 parent claim；
- 对需要文献、方法或外部标准的判断，写入 `handoff-to-field-learning.md`，不硬判；
- 若触发中文经管语境，已调用或明确说明为何不调用中文子适配器；
- 输出能被 `academic-argument-arrow-audit`、`academic-field-evidence-learning` 和 `academic-argument-issue-selection` 继续消费。

