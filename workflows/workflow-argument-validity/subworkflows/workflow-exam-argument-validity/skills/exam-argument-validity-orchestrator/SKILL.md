---
name: exam-argument-validity-orchestrator
description: 论效题子 workflow 的总编排 Skill。用于把中文论证有效性分析题或 GRE Analyze an Argument 材料按考试场景处理为审题记录、论证树、断点选择、题目指令响应、行文规划、本论段和二三稿修改清单。
---

# Exam Argument Validity Orchestrator

## 核心原则

论效题不是先“评价观点”，而是先“恢复论证”。

```text
论据 / 事实 / 数字
-> 分论点 / 中间结论
-> 总论点 / 总结论
```

考点通常在箭头上：材料给出的论据是否足以推出它声称的结论。

GRE Analyze an Argument 不是写自己的立场，也不是泛泛找错；它要按照题目指令评价作者论证的 logical soundness。

## 启动流程

1. 读取 `../../references/exam-reading-rules.md`，完成审题：
   - 找总论点和总结论；
   - 对比话题关键词；
   - 按“句号先，逗号后”找结构关键词；
   - 标出直推、合推、分推。
2. 若是 GRE Argument，先识别 prompt instruction：
   - `assumptions` / `unstated assumptions`;
   - `evidence needed`;
   - `questions that need to be answered`;
   - `alternative explanations`;
   - `recommendation` / `prediction` / `conclusion`。
3. 使用 `../../assets/exam-argument-tree-template.md` 输出 Mermaid 小树。
4. 调用父层验箭头 Skill：`../../../skills/argument-arrow-audit/skills/exam-argument-arrow-audit/SKILL.md`；断点分类与逻辑谬误标签优先读取 `../../../skills/argument-arrow-audit/references/arrow-audit-core.md`。
5. 调用问题选择 Skill：`../../../skills/argument-issue-selection/skills/exam-argument-issue-selection/SKILL.md`，从全量箭头审计表中选 3-4 个可写问题。
6. 读取 `../../references/exam-writing-rules.md`，做行文规划。
7. 使用 `../../assets/exam-paragraph-template.md` 写本论段。
8. 读取 `../../references/exam-practice-loop.md`，生成修改清单或二稿任务。

## 选点编排规则

具体选点执行交给 `../../../skills/argument-issue-selection/skills/exam-argument-issue-selection/SKILL.md`。本节只说明 orchestrator 如何判断是否需要进入该环节。

- 优先选择能削弱总论点或关键分论点的断点；
- 同一组论证中多个断点并存时，选最容易讲清、最影响结论的 1 个；
- 不为了术语丰富而堆叠问题；
- 每个本论段必须回答“作者用什么推出什么，为什么推不出”。
- 逻辑谬误标签属于断点解释的辅助标注，不是选点主轴；选点主轴始终是 `A -> B` 是否推得动。
- GRE Argument 不默认选“3-4 个谬误”；按题目指令选 3-4 个 assumptions、questions、needed evidence 或 alternative explanations。
- GRE 问题型题目必须说明答案为 yes/no 或存在替代答案时，目标箭头如何增强或削弱。

## GRE 输出路由

| 指令信号 | 选点单位 | 段落骨架 |
|---|---|---|
| `assumptions` / `unstated assumptions` | 隐含假设 | `assumption -> arrow -> impact if false` |
| `evidence needed` | 缺失证据 | `evidence -> target arrow -> strengthen/weaken impact` |
| `questions that need to be answered` | 待回答问题 | `question -> target arrow -> yes/no impact` |
| `alternative explanations` | 替代解释 | `observed fact -> rival mechanism -> weakens original explanation` |

GRE 段落不能只写问题或术语。每段至少说明：

```text
这个假设/问题/证据针对哪条 A -> B 箭头；
为什么它是作者结论所必需；
不同答案或证据状态会如何改变上层结论可信度。
```

## 完成标准

- 已识别材料总论点；
- 已恢复至少 3 条主要论证链；
- 已给出 3-4 个可写断点；
- 每个断点绑定具体箭头；
- 若是 GRE Argument，已响应题目指令，且不是中文论效模板的直接翻译；
- 若是 questions/evidence 题，已说明答案或证据如何影响结论；
- 本论段不是术语清单，而有定位、分析和回扣；
- 若生成作文，开头和结尾不过度展开个人观点。
