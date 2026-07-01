---
date: 2026-06-19
type: reference
status: structural-green
scope:
  - workflow-argument-validity
---

# 支撑箭头断点分类

## 目的

断点不是散点挑错，而是路线选择信号。每个断点都必须回答：

```text
哪条箭头断了？
为什么下层节点不足以支撑上层节点？
它影响根结论吗？
```

## 状态

| 状态 | 含义 |
|---|---|
| `strong` | 当前证据足以支撑上层结论 |
| `weak` | 有一定支持，但前提、范围或证据不足 |
| `broken` | 支撑关系不成立或严重跳跃 |
| `unclear` | 文本没有足够信息判断 |

## 断点总表

| 断点 | 判断问题 | 常见输出 |
|---|---|---|
| concept mismatch | 论据与结论是否使用不同概念，或错误处理概念关系 | A 与 B 不是同一概念；A 只是 B 的部分、交集、手段或可并存项 |
| scope expansion | 是否从局部扩大到整体 | A 至多说明局部，不能推出整体 |
| causal leap | 是否把相关、共现或时间顺序写成因果 | 当前证据不足以支持因果表述 |
| hidden premise missing | 是否依赖未证明前提 | 只有在 H 成立时 A 才能支持 B |
| alternative explanation | 是否忽略替代解释 | A 也可能由 B/C/D 导致 |
| sample weakness | 样本是否可代表目标总体 | 样本不足以支持外推 |
| measurement mismatch | 指标是否代表目标概念 | 指标更直接测量 A1 而非 A |
| numerical trap | 数字、比例、均值、增长率是否被误读 | 数字变化不等于作者声称的能力/趋势 |
| comparison mismatch | 比较对象是否同口径同条件 | 两者缺少可比性 |
| standard shift | 评价标准是否中途改变 | 论据和结论使用了不同衡量标准 |
| false dichotomy | 是否把不互斥或不穷尽的选项当作二选一 | 否定 A 并不能推出 B |
| condition confusion | 是否混淆必要、充分、辅助、唯一条件 | 把一项标准当唯一标准，把部分条件当充分条件 |
| extrapolation mismatch | 是否跨时间、空间、对象、指标、场景或强度外推 | 过去推出未来，局部推出整体，弱证据推出强结论 |
| uncontrolled comparison | 对比中是否只有目标变量变化 | 多个因素同时变化却单一归因 |
| mechanism over-interpretation | 是否把工具、材料、记录或局部证据的存在解释成主因、整体机制或唯一机制 | 发现某类工具不等于该工具主导了全部生产过程 |
| prediction mechanism missing | 是否从事实解释直接跳到未来价格、价值、需求、政策或行为预测 | 缺少行动者、评价标准、传导机制和反向机制 |
| contradiction | 文中不同位置是否互相冲突 | 该解释与前文前提不一致 |
| overclaim | 结论强度越过证据 | 只能支持弱结论，不能支持强结论 |

## 学术审稿映射

## 概念关系误判

处理 `concept mismatch` 时，不要只找“术语不同”。先判断两个概念之间的关系：

| 关系 | 断裂形式 |
|---|---|
| 同一关系被误判 | 把相近概念当成完全同一 |
| 包含关系被误判 | 把部分、子类或指标表现当成整体概念 |
| 交叉关系被误判 | 把有交集的概念当作可以互相替代 |
| 并列相容被误判 | 把可以同时成立的概念写成互相排斥 |
| 无关关系被误判 | 把只是同段出现的概念写成支撑关系 |
| 手段目的被误判 | 把一种手段写成唯一必要手段 |
| 因果关系被误判 | 把相关、可能、条件之一写成必然因果 |
| 定义回代失败 | 将定义代回原命题后产生重复、矛盾、范围变化或论证失效 |
| 二分关系失败 | 两个解释、路径或方案并不互斥或并不穷尽，却被当作非此即彼 |
| 条件关系失败 | 必要条件、充分条件、辅助条件、唯一条件被混用 |
| 概念簇边界失败 | 多个近义词有不同历史语境、制度含义、对象或评价色彩，却被当作同义词滑动使用 |

“速度/总量”“手段/结果”“局部/整体”等不是独立 checklist，而是上述概念关系误判的例子。抽象到关系层，才具有迁移价值。

## 外推与实验断点

处理 `extrapolation mismatch` 时，优先检查六个维度：

| 维度 | 断裂形式 |
|---|---|
| 时间 | 用过去事实推出未来长期趋势 |
| 空间 | 用局部地区推出整体地区 |
| 对象 | 用某类样本推出目标总体 |
| 指标 | 用观测记录、曝光数量或主观感受推出真实水平 |
| 场景 | 用某一使用场景推出全部场景 |
| 强度 | 用弱证据推出“一定、唯一、杜绝、必然”等强结论 |

处理 `uncontrolled comparison` 时，先问对比是否只改变了作者要证明的目标因素。若两组同时改变口味、顺序、对象、环境或时间，差异结果不能单独归因于目标因素。

处理“偶然成功 -> 策略有效”时，通常落在 `causal leap / sample weakness / overclaim`：一次逃生、一次成功或一个案例不能替代成功率、失败样本、成本风险和反馈机制。

## 机制与预测断点

处理 `mechanism over-interpretation` 时，先区分：

| 关系 | 判断问题 |
|---|---|
| 存在 | 文本是否只证明某工具、材料、制度或记录存在？ |
| 局部使用 | 该证据是否只覆盖某个部位、环节、地区、时期或样本？ |
| 辅助机制 | 它可能只是练习、修补、辅助、研究或临时工具吗？ |
| 主因机制 | 文本是否足以证明它是主要机制或唯一机制？ |

处理 `prediction mechanism missing` 时，至少追问：

| 要素 | 判断问题 |
|---|---|
| 行动者 | 谁会改变定价、需求、政策或行为？ |
| 评价标准 | 行动者按什么标准重估价值或改变选择？ |
| 传导机制 | 新信息如何传到行动者并改变决策？ |
| 反向机制 | 稀缺性、审美、历史意义、替代需求等是否可能抵消作者预测？ |

| 通用断点 | 审稿表达 |
|---|---|
| concept mismatch | construct / concept mismatch |
| measurement mismatch | construct-measure mismatch |
| causal leap | identification -> causal claim 不足 |
| sample weakness | external validity / sample selection concern |
| overclaim | evidence-claim mismatch |
| standard shift | 指标口径或评价标准错配 |

## 记录要求

每条断点记录：

- `arrow_id`;
- `from_node`;
- `to_node`;
- `status`;
- `break_type`;
- `evidence_location`;
- `why_it_breaks`;
- `impact_on_root`;
- `possible_fix_or_downgrade`。
