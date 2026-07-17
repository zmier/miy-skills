---
name: argument-arrow-audit
description: 通用验箭头复合 Skill。用于在已有论证树、节点台账、evidence ledger 或短文本论证中，全量检查 A 到 B 的支撑是否成立，识别隐含前提、概念错配、测量错配、因果跳跃、样本外推、过度上升等断点，标注 strong/strong-with-qc/weak/broken/unclear/needs-qc/needs-external-evidence，并路由到学术论文审稿或论效题/GRE 子 Skill；不负责从断点中选择可写问题。
---

# Argument Arrow Audit

## 定位

这是“验箭头”的父复合 Skill。它只保存跨场景稳定存在的协议：

```text
作者用 A 推出 B；
A 是否足以推出 B？
如果不足，断在哪条箭头，削弱哪个上层结论？
```

专用场景通过内部子 Skill 实现：

```text
argument-arrow-audit
└── skills/
    ├── academic-argument-arrow-audit
    └── exam-argument-arrow-audit
```

本 Skill 是诊断层，不是选题层。若已经完成全量验箭头，需要从 weak/broken/unclear 中选择可写问题、major concern 或 revision action，调用：

```text
../argument-issue-selection/SKILL.md
```

## 输入

- 已抽出的 `paper-argument-tree.md`、Mermaid 论证树、节点台账或 `evidence-ledger.md`；
- 或短文本论证、论效题/GRE argument 材料；
- 或已有 `arrow table` / `review issue map`，需要复核箭头强弱。

## 路由

| 场景 | 调用 |
|---|---|
| 学术论文、审稿项目、论文贡献链、变量/模型/结果/稳健性/机制 | `skills/academic-argument-arrow-audit/SKILL.md` |
| 管综/经综论效题、GRE Analyze an Argument、考试型短材料 | `skills/exam-argument-arrow-audit/SKILL.md` |
| 普通政策、商业、局部论证 | 使用父层协议直接审计，必要时沉淀新子 Skill |

如果用户已经在学术审稿项目中，且输入含 `X1/X2/Y`、表格、系数、变量、识别、机制、稳健性，优先路由到 academic 子 Skill。

路由到 academic 子 Skill 后，仍必须以 `arrow_id: A -> B` 为主轴；gap、变量、样本、识别、结果、机制、稳健性只作为学术箭头类型标签，不得退回传统模块 checklist。

如果输入含“论效题、老王、审题、GRE assumptions/questions/evidence”，优先路由到 exam 子 Skill。若用户要求“选 3-4 个可写问题”，验箭头后继续调用 `../argument-issue-selection/skills/exam-argument-issue-selection/SKILL.md`。

如果任务涉及“逻辑谬误、断点类型、为什么 A 推不出 B、隐含假设、需要什么问题/证据、替代解释”，必须读取 `references/arrow-audit-core.md`。该文件是本 Skill 的可执行断点库，已经整合父 workflow 的 `arrow-break-taxonomy.md`、`fallacy-taxonomy.md` 和论效/GRE 案例反哺。

## 通用验箭头协议

0. 检查命题形态：

   ```text
   from_node / to_node 若是 claim，必须能表述为可判真假的命题；
   若只是标签，标记 needs-claim-rewrite，回到 argument-tree-extraction；
   对 to_node 记录 target_proposition_form 和 valid_counterexample_shape。
   ```

1. 固定箭头：

   ```text
   arrow_id | from_node A | to_node B | 作者如何推出 | evidence_ids
   ```

2. 还原隐含前提：

   ```text
   A -> B 需要 H 成立；
   作者是否证明 H；
   若 H 不成立，B 或根结论如何变弱。
   ```

3. 对齐关键词和层级：

   - A 与 B 是否是同一概念；
   - A 是否只是 B 的部分、指标、代理、结果、手段或相邻现象；
   - A 是否从局部、短期、特定样本上升到整体、长期、一般结论；
   - A 是否从相关/共现/时序跳到因果。

4. 标注状态：

   ```text
   strong
   strong-with-qc
   weak
   broken
   unclear
   needs-qc
   needs-external-evidence
   ```

5. 写清影响：

   ```text
   该箭头削弱哪个上层节点？
   是否影响 root claim？
   应补什么证据，或把结论降调到什么边界？
   ```

断点分类详见 `references/arrow-audit-core.md`。输出表可用 `assets/arrow-audit-table-template.md`。

谬误术语只能作为 `fallacy_label` 或解释辅助，不能替代分析本身。输出必须先说明 `A -> B` 为什么推不动，再决定是否贴“偷换概念、以偏概全、强加因果、另有他因、数字谬误、充分必要混淆”等标签。

## 最小输出

```text
arrow audit table:
  arrow_id | from_node | to_node | target_proposition_form | valid_counterexample_shape | does_break_match_counterexample_shape | status | break_type | fallacy_label | hidden_premise | why_it_breaks | impact_on_root | fix_or_downgrade

task_instruction:
  assumption / question / evidence / alternative / paragraph / review concern
```

## 与抽树 Skill 的关系

`argument-tree-extraction` 负责把材料抽成树；本 Skill 负责检查树上的支撑关系是否成立。

抽树阶段可以把箭头标为 `not-yet-audited`；进入本 Skill 后必须改为 `strong / strong-with-qc / weak / broken / unclear / needs-qc / needs-external-evidence`。

## 完成标准

- 每条主要问题绑定具体 `arrow_id`；
- 每个关键 claim 节点已命题化；未命题化者标记 `needs-claim-rewrite`，不强行验标签；
- 不把“模块问题”当作审查结论，必须说清哪条 A -> B 推不动；
- 每个 `break_type` 优先来自 `references/arrow-audit-core.md`；若确需新增类型，标为 `proposed-new-break-type` 并写明原因；
- 谬误标签必须绑定具体箭头，不得单独列成脱离论证树的术语清单；
- 每个 broken/weak 箭头说明影响哪个上层节点或根结论；
- 每个 `needs-external-evidence` 箭头说明需要什么外部证据，并在学术场景中交给 `external-evidence-request.md` 集中处理；
- 输出可以被 `argument-issue-selection` 继续筛选，再转成审稿意见、论效段落或 GRE response；
- 不把个案判断写成通用规则。
