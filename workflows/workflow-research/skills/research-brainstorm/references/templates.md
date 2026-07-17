# Research Brainstorm Templates

按需复制到具体 TASK / subtask。模板中的 `<...>` 应替换为项目内容。

## Seminar Brief

```markdown
# Seminar Brief

> 状态：draft  
> 日期：YYYY-MM-DD  
> 研究项目：<project>  
> 父任务：<path>

## 核心谜题

<一句话写清楚本轮要解释的现象。>

## 已知事实

| Fact ID | 事实 | 证据入口 | 边界 |
|---|---|---|---|
| F01 |  |  |  |

## 数据与样本边界

| 项目 | 当前状态 |
|---|---|
| 样本 universe |  |
| treatment / X |  |
| outcome / Y |  |
| 已有 controls / FE |  |
| 不可观察项 |  |

## 本轮禁止声称

- 不把相关性写成因果。
- 不把机制候选写成已验证机制。
- 不把样本诊断写成主结论推翻。

## 本轮产出

- raw possibility pool
- mechanism route menu
- threat register
- next gate
```

## Agent Brief

```markdown
# Agent Brief: <Role>

> Round：1 independent divergence  
> 输入：`outputs/seminar-brief.md`

## 你的视角

<说明该角色的信息优势和批评函数。>

## 任务

请提出 3-7 个候选机制或解释。每个候选必须填写：

| 字段 | 内容 |
|---|---|
| Mechanism ID | Mxx |
| 机制名称 |  |
| 机制直觉 |  |
| 如何解释核心谜题 |  |
| 文献锚点 / search keywords |  |
| 可观察 proxy |  |
| 反事实预测 |  |
| 主要识别威胁 |  |
| 下一步检验 |  |
| 初始优先级 | high / medium / low |

## 边界

- 只写在自己的 `agents/<role>/` 下。
- 不改父任务 README、log、email 或共享数据。
- 不宣称最终结论。
```

## Blackboard

```markdown
# Brainstorming Blackboard

> 状态：active  
> Chair：<name/agent>  

## Mechanism Candidates

| ID | 机制 | 提出视角 | 解释对象 | proxy | 反事实预测 | 状态 | 备注 |
|---|---|---|---|---|---|---|---|
| M01 |  |  |  |  |  | proposed |  |

## Threat Register

| ID | 威胁 / 替代解释 | 影响哪条机制 | 可排除证据 | 状态 |
|---|---|---|---|---|
| T01 |  |  |  | open |

## Merge / Downgrade Decisions

| 决策 | 涉及 ID | 理由 | 处理 |
|---|---|---|---|
| merge / downgrade / archive |  |  |  |
```

## Cross Critique

```markdown
# Cross Critique: <Role>

> Round：2 cross critique  
> 批评对象：从 blackboard 中选择非自己提出的机制

| Mechanism ID | 最强版本 | 最大问题 | 需要的数据 / 文献 | falsification | 建议 |
|---|---|---|---|---|---|
| Mxx |  |  |  |  | keep / revise / merge / downgrade / archive |

## General Concerns

- <跨机制共同问题。>
```

## Response And Revision

```markdown
# Response And Revision: <Role>

> Round：3 response and revision

| Original ID | 收到的主要批评 | 回应 | 修订后状态 | 新 ID / 合并对象 |
|---|---|---|---|---|
| Mxx |  |  | keep / revise / merge / downgrade / archive |  |
```

## Chair Synthesis

```markdown
# Seminar Synthesis

> 状态：draft / ready for gate  
> Chair：<name/agent>

## Raw Possibility Pool

| ID | 机制 / 解释 | 类别 | 当前状态 | 保留原因 |
|---|---|---|---|---|
| M01 |  | mechanism / threat / heterogeneity / data issue | keep |  |

## Route Menu

| Priority | Route | 解释力 | 文献支撑 | 数据可检验性 | 贡献潜力 | 下一步 |
|---|---|---|---|---|---|---|
| P0 |  | high / medium / low |  |  |  |  |

## Final Adjudication

| Stable ID | Decision | Information gain | Reason | Next trigger |
|---|---|---|---|---|
| M01 | promote-now / queue-data / theory-boundary / diagnostic-only / merge / archive | high / medium / low |  |  |

## Key Disagreements

| Issue | 分歧双方 | 为什么重要 | 如何用证据区分 |
|---|---|---|---|
|  |  |  |  |

## Next Gate

建议下一步优先进入：

1. <route 1>
2. <route 2>
3. <route 3>

暂缓路线：

| Route | 暂缓原因 | 未来触发条件 |
|---|---|---|
|  |  |  |

## Promotion Contract

| Field | Frozen value |
|---|---|
| Economic object / unit |  |
| Primary universe |  |
| One primary Gate |  |
| Distinguishing DGPs |  |
| Pass / mixed / fail consequences |  |
| Forbidden follow-ups |  |
| Claim ceiling |  |
| Independent audit trigger |  |
```
