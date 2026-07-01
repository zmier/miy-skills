---
name: argument-workflow-orchestrator
description: workflow-argument-validity 的父层编排 Skill。用于按文本类型路由论效题、GRE Analyze an Argument、学术审稿、论文写作自审和普通论证问题，恢复论证树，建立节点台账，生成 Mermaid/Obsidian 图，审计支撑箭头，映射断箭头修复路线，选择重点问题，并把结果输出为分析段、论效题文章、GRE argument response、审稿意见或写作自审建议。
---

# Argument Workflow Orchestrator

当前状态：`seed / structural-green / forward-test-pending`

## 核心原则

不从“找错”开始，而从“恢复论证树”开始。

```text
下层证据 / 论据
-> 分论点 / 中间结论
-> 根结论
```

所有断点必须绑定到一条支撑箭头，并说明它如何削弱上层节点或根结论。

验箭头、修复映射和选问题必须拆开：

```text
argument-arrow-audit
-> 全量诊断每条 A -> B 是否推得动

argument-arrow-repair-mapping
-> 给断裂箭头映射补证据、补实验、补分析或降调路线

argument-issue-selection
-> 从诊断结果和修复路线中选择本次要写的问题
```

## 启动流程

1. 判断任务类型。需要细分时读取 `../../references/text-type-routing.md`。
2. 若任务是整篇/整段抽树，优先调用 `../argument-tree-extraction/SKILL.md`；由该 Skill 决定是否进入学术论文或考试型抽树子 Skill。
3. 若是考试型 argument，先识别 prompt instruction：`assumptions`、`evidence needed`、`questions`、`alternative explanations`、`recommendation/prediction/conclusion`。
4. 恢复论证树。需要标准节点模型时读取 `../../references/argument-tree-core.md`。
5. 使用 `../../assets/argument-node-ledger-template.md` 建立节点台账。
6. 若已有论证树或需要验箭头，调用 `../argument-arrow-audit/SKILL.md`；由其决定是否进入学术论文或考试型验箭头子 Skill。
7. 使用 `../../assets/argument-arrow-audit-template.md` 或 `../argument-arrow-audit/assets/arrow-audit-table-template.md` 建立箭头审计表。
8. 输出 Mermaid / Obsidian 图。需要规则时读取 `../../references/mermaid-obsidian-rules.md` 和 `../../assets/mermaid-argument-tree-template.md`。
9. 对每条箭头做断点分类。需要分类时优先读取 `../argument-arrow-audit/references/arrow-audit-core.md`；必要时再读取 `../../references/arrow-break-taxonomy.md`。
10. 若需要把断点转为可执行补强、补实验、补分析、补证据或降调路线，调用 `../argument-arrow-repair-mapping/SKILL.md`；学术论文场景默认在 issue selection 前执行。
11. 若需要选择可写问题、major concern 或 revision action，调用 `../argument-issue-selection/SKILL.md`；由其决定是否进入 exam 或 academic 子 Skill。
12. 按输出阶梯选择交付形态。需要判断时读取 `../../references/output-ladder.md`。
13. 若是学术审稿攻击、审稿段落或 issue map，再调用 `../academic-review-argument-audit/SKILL.md` 做领域适配。
14. 把对话洞见、case-derived patterns 或 forward-test 发现回收到 references / assets / tests，并标注迁移状态。

## 路由规则

- 论效题：先调用 `argument-tree-extraction/skills/exam-argument-tree-extraction` 抽短文本小型论证树，再调用 `argument-arrow-audit/skills/exam-argument-arrow-audit` 全量验箭头，再调用 `argument-issue-selection/skills/exam-argument-issue-selection` 选 3-4 个可写断点，最后进入 `subworkflows/workflow-exam-argument-validity` 做写作。
- GRE Analyze an Argument：先调用 `argument-tree-extraction/skills/exam-argument-tree-extraction` 抽树并识别 prompt instruction；再调用 `argument-arrow-audit/skills/exam-argument-arrow-audit` 全量验箭头；再调用 `argument-issue-selection/skills/exam-argument-issue-selection` 按题目指令选 assumptions、questions、needed evidence 或 alternatives。不要默认写中文论效模板。
- 学术论文整篇抽树：进入 `subworkflows/workflow-academic-argument-validity`；由该子 workflow 调用 `argument-tree-extraction/skills/academic-paper-argument-tree-extraction` 生成作者树、evidence ledger、evidence-expanded Mermaid 和 Obsidian link map。
- 学术审稿：进入 `subworkflows/workflow-academic-argument-validity`；在作者树基础上调用 `argument-arrow-audit/skills/academic-argument-arrow-audit` 逐条审计 `arrow_id: A -> B`，再调用 `argument-arrow-repair-mapping/skills/academic-arrow-repair-mapping` 生成修复或降调路线，最后调用 `argument-issue-selection/skills/academic-argument-issue-selection` 把 weak/broken/unclear 箭头选成 major concern、minor concern 或 revision action。`X2` 必须写清“哪个 X 通过什么机制 M 影响哪个 Y”，不能只写成“作者做出来了”。
- 论文写作自审：进入 `subworkflows/workflow-academic-argument-validity`；从作者目标结论反向检查缺失节点和弱箭头，再调用 `argument-arrow-repair-mapping/skills/academic-arrow-repair-mapping` 形成补强优先级，最后调用 `argument-issue-selection/skills/academic-argument-issue-selection` 输出修订路线。
- 普通论证：使用父层通用论证树，不强行套学术节点。

## 完成标准

- 已判断文本类型；
- 已给出根结论和至少一层支撑节点；
- 每个主要问题都绑定到具体箭头；
- 学术审稿或写作自审中，每个主要问题尽量绑定修复或降调路线；
- 若任务有 prompt instruction，输出结构已响应该指令，而不是泛泛列断点；
- 若是学术论文，已给出一句话核心发现、X/M/Y/Y2 表，并在需要时建立 evidence ledger、evidence-expanded Mermaid 和 Obsidian link map；
- 箭头状态标为 `strong / weak / broken / unclear`；
- 若输出 Mermaid，默认使用 `flowchart BT` 表达 supports；
- 输出文本解释“为什么推不出”，而不是只贴谬误术语；
- 未把具体 case 的固定判断写成通用规则。
