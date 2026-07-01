---
date: 2026-06-19
type: reference
status: seed
scope:
  - argument-arrow-audit
---

# Arrow Audit Core

## 来源与定位

本文件是验箭头的断点分类库，整合自：

```text
workflow-argument-validity/references/arrow-break-taxonomy.md
workflow-argument-validity/references/fallacy-taxonomy.md
workflow-argument-validity/skills/argument-validity-audit/SKILL.md
论效题案例 TASK 与 GRE Argument assisted UAT 的反哺
```

它不是“逻辑谬误 checklist”。使用顺序必须是：

```text
先固定 arrow_id: A -> B
再判断 A 为什么不足以推出 B
最后用 break_type / fallacy label 标注断裂类型
```

术语只服务于解释，不能替代解释。

## 核心问题

```text
A 是否足以推出 B？
```

不要只判断 B 对不对；要判断作者给出的 A 是否足以支撑 B。

## 状态

| 状态 | 含义 |
|---|---|
| strong | 当前证据足以支撑上层结论 |
| weak | 有一定支持，但范围、前提、口径或证据不足 |
| broken | 支撑关系不成立或严重跳跃 |
| unclear | 当前材料不足以判断 |
| needs-qc | 需要回原文、表格、数据或题干核验后才能判断 |

## 通用断点

| break_type | 判断问题 |
|---|---|
| concept-mismatch | A 与 B 是否不是同一概念，或概念关系被误判 |
| measurement-mismatch | 指标 A 是否不能代表目标概念 B |
| hidden-premise-missing | A -> B 是否依赖未证明前提 H |
| causal-leap | 是否把相关、共现、时序或机制猜测写成因果 |
| scope-expansion | 是否从局部、短期、个案推到整体、长期、一般结论 |
| extrapolation-mismatch | 是否跨时间、空间、对象、指标、场景或强度外推 |
| sample-weakness | 样本是否不足以代表目标总体或机制场景 |
| numerical-trap | 数字、比例、均值、增长率、份额或指数是否被误读 |
| comparison-mismatch | 比较对象是否同层级、同口径、同条件 |
| uncontrolled-comparison | 对比中是否不只目标变量改变，导致无法单一归因 |
| standard-shift | A 与 B 使用不同评价标准或口径 |
| alternative-explanation | A 是否还可由其他机制解释 |
| false-dichotomy | 是否把不互斥或不穷尽的选项当成二选一 |
| condition-confusion | 是否混淆必要、充分、辅助、唯一条件 |
| means-end-confusion | 是否把手段当成目的、唯一手段或必然有效手段 |
| mechanism-over-interpretation | 是否把工具、材料、记录、局部证据解释成主因、整体机制或唯一机制 |
| prediction-mechanism-missing | 是否从事实解释直接跳到未来价格、价值、需求、政策或行为预测 |
| contradiction | 文中不同位置是否互相冲突 |
| static-to-dynamic-leap | 是否把静态事实、历史事实直接推出动态趋势或后续阶段 |
| one-sided-reasoning | 是否只看一面，忽略反向机制、成本、约束或代价 |
| overclaim | A 只能支持弱结论，却被写成强结论 |
| evidence-qc-gap | 证据缺少原文、数值、表格或出处核验 |

## 概念关系检查

处理概念错配时，先判断 A 与 B 的关系：

| 关系 | 常见断点 |
|---|---|
| 同一 | 是否只是相近而非同一 |
| 包含 | 是否把部分/指标当整体 |
| 交叉 | 是否把有交集的概念当可替代 |
| 并列相容 | 是否把可同时成立的解释当互斥 |
| 手段目的 | 是否把一种手段当唯一必要手段 |
| 因果 | 是否把相关或条件之一当必然因果 |
| 定义回代 | 把定义代回原命题后是否重复、矛盾、范围变化或论证失效 |
| 二分 | 是否把不互斥或不穷尽的解释当二选一 |
| 条件 | 是否混淆必要、充分、辅助、唯一条件 |
| 概念簇 | 多个近义词是否具有不同历史语境、制度含义、对象或评价色彩 |

“速度/总量”“手段/结果”“局部/整体”不是独立 checklist，而是概念关系误判的例子。先判断关系，再选择断点标签。

## 数字与统计材料

数字不是自动证据。遇到数字、比例、指数、显著性或统计材料时，至少检查：

| 检查项 | 问题 |
|---|---|
| 基数 | 分母、总体、样本量是否清楚 |
| 口径 | 指标定义、时间窗口、计量单位是否一致 |
| 分布 | 均值是否掩盖分布、极端值或组间差异 |
| 比例/总量 | 比例变化是否被误写成绝对数量变化，或反之 |
| 指数/代理 | 指数变化是否真的代表目标概念 |
| 统计差异 | 显著性是否足以支持作者声称的实质差异 |
| 替代解释 | 数字变化是否可由其他机制解释 |

输出时说明该数字支持的是较弱结论、较强结论，还是根本不能支持作者当前结论。

## 外推维度

处理 `scope-expansion` 或 `extrapolation-mismatch` 时，优先检查六个维度：

| 维度 | 断裂形式 |
|---|---|
| 时间 | 用过去事实推出未来长期趋势，或用短期变化推出长期状态 |
| 空间 | 用局部地区、局部场景推出整体 |
| 对象 | 用某类样本推出目标总体 |
| 指标 | 用观测记录、曝光数量、代理指标推出真实水平或理论构念 |
| 场景 | 用某一使用场景推出全部场景 |
| 强度 | 用弱证据推出“一定、唯一、杜绝、必然”等强结论 |

## 机制与预测

处理 `mechanism-over-interpretation` 时，先区分：

| 层级 | 判断问题 |
|---|---|
| 存在 | 文本是否只证明某工具、材料、制度、记录或现象存在 |
| 局部使用 | 该证据是否只覆盖某个部位、环节、时期或样本 |
| 辅助机制 | 它是否可能只是辅助、修补、训练、临时工具或局部机制 |
| 主因机制 | 文本是否足以证明它是主要机制或唯一机制 |

处理 `prediction-mechanism-missing` 时，至少追问：

| 要素 | 判断问题 |
|---|---|
| 行动者 | 谁会改变定价、需求、政策或行为 |
| 评价标准 | 行动者按什么标准重估价值或改变选择 |
| 传导机制 | 新信息如何传到行动者并改变决策 |
| 反向机制 | 稀缺性、审美、成本、制度约束、替代需求等是否可能抵消作者预测 |

## 谬误标签映射

中文论效或普通读者场景可使用通俗标签，但标签必须回到 arrow：

| 常见中文标签 | 推荐 break_type |
|---|---|
| 偷换概念 / 概念不一致 | concept-mismatch |
| 以偏概全 | scope-expansion / sample-weakness / extrapolation-mismatch |
| 强加因果 / 因果倒置 | causal-leap |
| 另有他因 | alternative-explanation |
| 不当假设 | hidden-premise-missing |
| 不当类比 / 比较不当 | comparison-mismatch |
| 数字谬误 | numerical-trap |
| 充分必要混淆 | condition-confusion |
| 非黑即白 | false-dichotomy |
| 自相矛盾 | contradiction |
| 忽略发展 | static-to-dynamic-leap |
| 顾此失彼 | one-sided-reasoning |
| 更换衡量标准 | standard-shift |
| 手段目的混淆 | means-end-confusion |

## 任务指令型输出

遇到 GRE Argument 或类似题目时，断点必须按题目指令输出：

| instruction | 输出结构 |
|---|---|
| assumptions / hidden premises | `assumption -> supporting arrow -> impact if false` |
| questions | `question -> target arrow -> yes/no or alternative-answer impact` |
| evidence needed | `evidence -> which arrow it would strengthen/weaken -> why` |
| alternative explanations | `observed fact -> rival mechanism -> impact on author's explanation` |

不要只列问题；每个问题都要说明不同答案如何改变箭头和根结论可信度。

## 记录字段

```text
arrow_id
from_node
to_node
status
break_type
hidden_premise
evidence_location
why_it_breaks
impact_on_parent
impact_on_root
fix_or_downgrade
selection_hint
task_instruction
```

## 选题提示

`selection_hint` 只给 `argument-issue-selection` 作为输入提示，不在验箭头阶段决定最终写哪些问题。

| selection_hint | 含义 |
|---|---|
| candidate-major | 直接影响根结论或主要贡献，可能适合写成 major concern |
| candidate-useful | 影响中层论点，可能适合写成次要问题或补充建议 |
| minor | 表述、规范或局部清晰度问题 |
| no-issue | 当前箭头足够强，不构成问题 |

## 使用纪律

- 不要求每次输出谬误术语；
- 不把 break_type 当作分析本身；
- 同一箭头可有多个断点，验箭头阶段应记录主要断点，不决定最终入选问题；
- 同一组问题是否组合分析，交给 `argument-issue-selection` 和写作层决定；
- 对学术审稿，先使用通用 break_type，再翻译成 construct、measurement、identification、sample、result、claim 等专业表达；
- 对论效题，验箭头阶段只说明哪些断点影响总结论；是否选入 3-4 个问题，交给 `exam-argument-issue-selection`。
