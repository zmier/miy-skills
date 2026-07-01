---
date: 2026-06-19
type: reference
status: structural-green
scope:
  - workflow-argument-validity
---

# 文本类型路由

## 目的

父 workflow 不直接假设文本属于论文、论效题或报告。先判断文本类型，再选择子 workflow、adapter 或父层通用模板。

```text
同一个问题
-> 先抽象成根结论、支撑节点、箭头和输出目标
-> 再根据文本类型选择节点模型和验箭头标准
```

## 路由表

| 输入类型 | 识别信号 | 首选路线 | 输出 |
|---|---|---|---|
| 论效题 | 短材料、要求“论证有效性分析”、考试作文 | `subworkflows/workflow-exam-argument-validity` | 论效题段落 / 完整文章 |
| GRE Analyze an Argument | 英文 argument prompt；要求分析 assumptions、evidence needed、questions、alternative explanations | `subworkflows/workflow-exam-argument-validity` 的 GRE Argument 分支 | assumption-impact outline / essay |
| 学术审稿 | 论文、手稿、审稿意见、贡献/gap/识别/变量/结果 | `skills/academic-review-argument-audit` | argument-tree、review issue、审稿段落 |
| 论文写作自审 | 作者在写引言、贡献、理论、结果叙事 | 父层树 + 写作方向补强 | 缺口清单、补强建议、段落改写 |
| 正向立论 / 观点构造 | 用户需要写观点文、论说文、Issue 类文章、政策主张或商业判断 | 父层树 + claim construction 路线 | 立场、支撑理由、反方压力测试、成文草稿 |
| 普通报告 / 政策 / 商业论证 | 报告、方案、政策建议、商业判断 | 父层通用树 | 论证审查表、修改建议 |
| 局部论证问题 | 用户只问某句话或某一箭头是否成立 | `skills/argument-validity-audit` | 最小箭头审计 |

## 判断顺序

1. 用户要做什么：考试成文、审稿、写论文、自审、报告审查，还是局部判断？
2. 根结论是什么：要证明观点、贡献、因果、政策、方案，还是发表价值？
3. 证据形态是什么：事实、数字、变量、模型、文献、结果表、案例、经验？
4. 工作方向是什么：拆别人已有论证，还是搭自己的论证并预先验箭头？
5. 输出目标是什么：Mermaid 图、表格、段落、完整文章、审稿意见？
6. 是否需要领域 adapter：若涉及学术论文专业证据链，进入学术审稿 adapter。
7. 若是考试型 argument 且题目指令要求 assumptions / evidence / questions，进入论效子 workflow 的 GRE Argument 分支，而不是中文论效题段落模板。

## 路由输出

每次路由至少记录：

- `text_type`;
- `root_claim`;
- `output_target`;
- `route`;
- `reason`;
- `fallback`。
