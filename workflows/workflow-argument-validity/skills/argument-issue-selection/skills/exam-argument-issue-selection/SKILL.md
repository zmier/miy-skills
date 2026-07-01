---
name: exam-argument-issue-selection
description: 论效题/GRE 专用问题选择 Skill。用于在 exam-argument-arrow-audit 已经产出全量箭头审计表之后，按中文论效或 GRE prompt instruction 从 weak、broken、unclear 箭头中选择 3 到 4 个最可写问题，并生成选点表和段落路线。
---

# Exam Argument Issue Selection

## 定位

这是考试型“选问题”子 Skill。它不负责全量验箭头，只消费 `exam-arrow-audit-table.md`。

```text
exam-argument-arrow-audit
-> exam-argument-issue-selection
-> exam writing
```

## 输入

- 论效题/GRE 题干；
- 已抽取的小型论证树；
- `exam-arrow-audit-table.md`；
- 总论点、分论点、论据；
- GRE prompt instruction。

## 选点规则

详见 `references/exam-issue-selection.md`。

优先选择：

- 直接影响总论点或关键分论点的断点；
- 容易用题干原词定位的问题；
- 能用“作者用 A 推 B，但 A 不能推出 B”讲清的问题；
- 不依赖外部专业知识的问题；
- 中文论效可写成 3-4 段，GRE 能响应 prompt instruction 的问题。

避免：

- 只改措辞的问题；
- 离总结论太远的问题；
- 重复攻击同一小点的问题；
- 只有谬误术语、没有推理解释的问题。

## GRE 路由

| prompt instruction | 选点单位 |
|---|---|
| assumptions / unstated assumptions | hidden assumption |
| evidence needed | needed evidence |
| questions that need to be answered | question |
| alternative explanations | rival explanation |

## 输出

```text
exam-selected-issues.md
```

字段：

```text
issue_id | target_arrow | selected_unit | why_selected | paragraph_route
```

## 完成标准

- 已从全量箭头审计表中选出 3-4 个问题；
- 每个问题绑定 target arrow；
- 每个问题说明为什么值得写；
- GRE 输出已响应题目指令；
- 未入选但重要的问题有简短说明。
