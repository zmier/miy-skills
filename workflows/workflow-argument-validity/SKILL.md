---
name: workflow-argument-validity
description: 论证有效性与论证树复合 Skill。用于论效题、学术审稿、论文写作自审、贡献链审查、Mermaid/Obsidian 论证树、拆箭头、搭箭头、验箭头、断箭头修复映射、选择重点问题，并把断裂箭头写成分析段或审稿意见。按恢复论证树、检查支撑箭头、映射补强或降调路线、选择重点问题、输出可读文本编排，并可调用学术审稿 adapter、课程论效提取稿、dialogue insights 和 case-derived patterns。
---

# Argument Validity Workflow

状态：`seed / structural-green / exam-forward-test-green / gre-assisted-uat-green / gre-question-branch-green / cross-domain-forward-test-pending`

## 目标

把通用论证有效性分析沉淀为可迁移 workflow，用来检查任意文本中的“论据是否足以推出结论”，并通过领域适配 Skill 把这套能力应用到学术审稿、论文写作自审、政策论证、商业报告和课程训练中。

核心问题不是“结论有没有可能正确”，而是：

```text
作者当前给出的论据、方法、数据、事实或例子
是否足以推出作者声称的结论
```

## 载体与边界

本 workflow 的可调用载体是 Skill。它不是单一原子 Skill，而是一个用于论证树、箭头审计和领域适配的复合 workflow 型 Skill。

```text
父层：恢复论证树、检查支撑箭头、选择重点问题、输出可读文本
子层：论效题、学术审稿、论文写作自审等文本类型的节点、标准和输出差异
```

需要创建或调整本 workflow 的父子结构时，可参考 `../workflow-tao/references/workflow-skill-shape.md`。

## 能力结构

```text
workflow-argument-validity
├── 论证树恢复
├── 支撑箭头审计
├── 断箭头修复映射
├── 问题选择
├── Mermaid / Obsidian 可视化
├── 文本类型路由
├── 领域适配与输出
└── 迁移评测
```

## 主流程

1. 判断任务类型：
   - 论效题；
   - GRE Analyze an Argument；
   - 学术审稿；
   - 论文写作自审；
   - 普通报告 / 政策 / 商业论证；
   - 局部论证问题。
2. 恢复论证树：
   - 结论 / 论点；
   - 论据 / 证据；
   - 显性箭头；
   - 隐含前提；
   - 总论点、分论点和总结论之间的关系。
   - 关键 claim 必须能表述为形式逻辑视角下的简单命题或复合命题。
   - 学术论文场景下，必须把 `X2` 还原为具体核心发现句：先从摘要提炼命题形态，再校准哪个 X 通过什么机制 M 影响哪个 Y，而不是只写“作者做出来了”。
3. 生成节点台账和 Mermaid：
   - 默认使用 `flowchart BT` 表达下层节点 supports 上层节点；
   - 每个节点应有证据位置或待补证据状态；
   - Obsidian 场景下可为节点使用双链。
   - 学术论文场景下，应同时生成 evidence ledger，追溯表格、系数、显著性、变量定义、模型设定、文献引用和原文段落。
   - 关键证据应画回 evidence-expanded Mermaid view，呈现 `E-* 具体证据 -> 子观点 -> 中层命题 -> X1/X2/Y`，避免只有台账而图上没有叶子。
4. 对齐关键词：
   - 论据中的关键词；
   - 结论中的关键词；
   - 是否出现概念漂移、范围扩大、层级错配或衡量标准错配。
5. 检查支撑箭头：
   - `A -> B` 是否成立；
   - B 是直言、假言、联言、选言还是混合命题；
   - 反驳形态是否真的击中目标命题，例如反驳 `A -> B` 需要 `A 且 非B`，单纯 `非A` 不构成反例；
   - `B -> C` 是否成立；
   - 多个论据是否真的可以合推结论；
   - 一个论据是否被分推到过多结论。
6. 识别断点：
   - 概念不一致；
   - 过度推理；
   - 因果跳跃；
   - 以偏概全；
   - 样本 / 数字陷阱；
   - 条件关系混淆；
   - 外推维度错配；
   - 对比实验未控变量；
   - 工具/材料/记录存在被过度解释为主因机制；
   - 预测类结论缺少行为或市场传导机制；
   - 概念簇边界滑动；
   - 不当假设；
   - 不当比较 / 类比；
   - 自相矛盾；
   - 忽略发展；
   - 顾此失彼；
   - 更换衡量标准。
7. 标注断点影响：
   - `strong / weak / broken / unclear`；
   - 断的是哪条箭头；
   - 影响哪个上层节点；
   - 是否影响根结论。
8. 映射修复路线：
   - 对 `weak / broken / unclear / needs-qc / needs-external-evidence` 箭头，说明需要补什么证据、实验、分析、QC 或外部检索；
   - 如果补不了，说明结论应如何降调；
   - 本步骤不决定哪些问题要写，只为选点提供“可修性、修复成本、补强路径”。
9. 选择重点问题：
   - 从 `weak / broken / unclear / needs-qc` 箭头中选择本次要写的问题；
   - 区分诊断层和决策层：验箭头负责全量判断，选问题负责优先级；
   - 选择标准包括影响根结论、任务目标、可写性、审稿价值、篇幅和重复度；
   - 不把“未选中”误认为“没有问题”。
10. 做组合分析：
   - 同一组论证若有多个断点，按“先定位、再分析、再回扣结论”组织；
   - 不把断点列成散点清单；
   - 每个断点都说明它如何削弱作者结论。
11. 领域适配：
   - 使用 domain adapter 把通用论证元素映射到具体领域；
   - 例如学术审稿中，论据可能是数据、模型、文献、识别策略、结果表和机制检验。
12. 输出可读文本：
   - 用克制、中性、可执行的语言；
   - 避免只贴“谬误术语”；
   - 必须解释为什么推不出，以及作者应如何补强或降调。
   - 中文输出默认采用“论效题中文论说文”风格：少翻译术语，多按“作者想由 A 推出 B；但 A 只能说明 A1，不能自然推出 B；若要维持 B，需要补什么；否则结论应收在哪里”的方式行文。

## 分层原则：验箭头、修复映射与选问题分离

`argument-arrow-audit`、`argument-arrow-repair-mapping` 和 `argument-issue-selection` 必须分开：

```text
验箭头是诊断层：A -> B 到底推不推得动。
修复映射是治疗方案层：断了以后补什么证据、实验、分析，或如何降调。
选问题是决策层：这么多断点里，这次要写哪几个。
```

拆开的原因：

- 验箭头追求覆盖和忠实，选问题追求优先级和表达策略；
- 修复映射追求可执行补强路线，会引入实验、方法、文献、成本和降调判断，不应污染验箭头的诊断纯度；
- 验箭头的标准是逻辑强弱，选问题还要考虑任务目标、篇幅、读者、可写性、审稿价值和重复度；
- 选问题需要知道某个断点是否可修、修复成本多高、是否只能降调，因此修复映射应在选问题之前；
- 如果在验箭头阶段就选问题，容易漏掉重要但暂时不写的断点；
- 如果在选问题阶段重新验箭头，容易把决策偏好倒灌进诊断结果。

## 中文论证写作风格

当输出中文审稿意见、中文论文自审、中文论证分析或中文给编辑说明时，默认使用“论效题中文论说文”风格，而不是英文审稿意见的直译腔。

核心不是把英文术语逐个翻成中文，而是把断裂箭头写成中文读者能自然跟上的论证段：

```text
作者想证明 B。
文中给出的材料是 A。
但 A 直接说明的只是 A1，并不能自然推出 B。
从 A1 到 B 还缺少 H 这个前提 / 证据 / 检验。
因此，若作者要维持 B，需要补充 H；否则，结论应收窄为 A 能直接支持的范围。
```

中文段落优先采用：

```text
定位 -> 分析 -> 收尾
```

- 定位：用一句话说明作者把什么当成什么的证据，或想由什么推出什么；
- 分析：说明两者为什么不等同，哪里跳了一步，缺了哪个前提；
- 收尾：说明这会削弱哪个上层结论，并给出补强或收窄方向。

推荐句式：

- “作者想证明的是……但文中实际观察到的更像是……”
- “从后者推出前者，中间还需要……”
- “A 并不意味着 B；A 至多说明 A1。”
- “这一做法并非不能成立，但需要额外论证。”
- “如果不能补充这部分证据，结论更稳妥的表述应是……”
- “第一阶段强只能说明……不能证明……”
- “这些结果可以说明方向一致，但还不能证明传导链已经成立。”

避免句式：

- 不把英文术语作为句子的主干，例如“这一测量桥梁仍需验证”“构念边界不清”“outcome construct 不一致”；
- 不堆砌抽象标签，例如“存在 construct-measure mismatch”后就停止分析；
- 不写成机器式清单：每段都必须回答“为什么推不出”和“怎么补或怎么收”；
- 不把必要英文术语删光。做法是中文先行，必要术语括注，例如“排除限制（exclusion restriction）”“中介或路径检验（mediation/path test）”。

当中文文本读起来像英文审稿意见翻译稿时，应重写而不是只替换词语。重写标准是：每个主要问题段都能还原为“作者由 A 推 B，但 A 不足以推出 B”的论效题段落。

## Skills

| Skill | 职责 |
|---|---|
| `skills/argument-workflow-orchestrator` | 父层总编排：按文本类型路由，组织抽树、验箭头、画树和输出 |
| `skills/argument-validity-audit` | 通用论证有效性审查：还原论证链、检查箭头、识别断点、输出分析表和可写段落 |
| `skills/argument-tree-extraction` | 通用抽树与路由编排 Skill：定义节点/箭头/证据台账/Mermaid/link map 协议，并路由到学术论文或考试型抽树子 Skill |
| `skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction` | 学术论文作者论证树抽取：按实证/理论/综述适配器生成 X1/X2/Y、evidence ledger、evidence-expanded Mermaid 和 Obsidian 链接 |
| `skills/argument-tree-extraction/skills/exam-argument-tree-extraction` | 考试型短材料抽树：服务论效题/GRE 的总论点、分论点、箭头和隐含假设 |
| `skills/argument-arrow-audit` | 通用验箭头父 Skill：检查 A -> B 是否成立，识别隐含前提和断点，并路由到学术或考试型验箭头子 Skill |
| `skills/argument-arrow-audit/skills/academic-argument-arrow-audit` | 学术论文验箭头：沿作者树逐条审计 `arrow_id: A -> B`；gap、变量、样本、识别、结果、机制、稳健性和贡献上升只作为 arrow_type 标签，输出全量箭头审计表 |
| `skills/argument-arrow-audit/skills/academic-argument-arrow-audit/skills/empirical-social-science-review-adapter` | 经管/社科实证审稿敏感箭头适配：显影 construct-proxy、sample-scope、model-identification、control-variable、clustering、mechanism、robustness 等断点候选 |
| `skills/argument-arrow-audit/skills/academic-argument-arrow-audit/skills/empirical-social-science-review-adapter/skills/chinese-management-econ-review-adapter` | 中文经管/中文社科审稿语境适配：显影指标方向、文本口径、本土制度语境、中文文献谱系和报告规范 |
| `skills/argument-arrow-audit/skills/exam-argument-arrow-audit` | 论效题/GRE 验箭头：检查题干论证树上的 `A -> B` 是否成立，输出全量箭头审计表 |
| `skills/argument-arrow-repair-mapping` | 通用断箭头修复映射父 Skill：先审计知识来源，再把 weak/broken/unclear/needs-qc/needs-external-evidence 箭头转为补证据、补实验、补分析、补 QC 或降调路线 |
| `skills/argument-arrow-repair-mapping/skills/academic-arrow-repair-mapping` | 学术论文修复映射：为审稿和写作自审生成 `arrow-repair-map.md`，必要时先生成 `repair-knowledge-learning-plan.md` 和 `case-repair-menu.md` |
| `skills/argument-issue-selection` | 通用问题选择父 Skill：在全量验箭头之后，从 weak/broken/unclear/needs-qc 箭头中选择本次要写的问题 |
| `skills/argument-issue-selection/skills/academic-argument-issue-selection` | 学术论文问题选择：生成 review issue arrow map、major concern candidates 和 revision action map |
| `skills/argument-issue-selection/skills/exam-argument-issue-selection` | 论效题/GRE 问题选择：按中文论效或 GRE prompt instruction 选 3-4 个可写问题 |
| `skills/academic-review-argument-audit` | 学术审稿领域适配：把已选断点写成 gap、contribution、construct、measurement、identification、results 和 review writing 语言 |

## Subworkflows

| Subworkflow | 职责 |
|---|---|
| `subworkflows/workflow-exam-argument-validity` | 论效题子 workflow：审题抓论证、画小型论证树、全量验箭头、选择断点、规划行文、写成本论段和二三稿训练 |
| `subworkflows/workflow-academic-argument-validity` | 学术论文子 workflow：编排作者树抽取、evidence ledger、全量学术验箭头、问题选择、审稿/自审素材输出 |

该子 workflow 同时承载 GRE Analyze an Argument 的考试型分支：共享抽树、验箭头和断点选择，但按题目指令输出为 `assumption -> arrow -> impact if false` 或 `question -> target arrow -> yes/no impact` 的英文 argument response。

学术论文子 workflow 只承载“论文作为论证”的主轴，不复制 `workflow-paper-writing-review` 的项目归档、PDF 还原、文献检索和最终审稿表流程。

## 父层 References

| Reference | 何时读取 |
|---|---|
| `references/text-type-routing.md` | 需要判断论效题、审稿、写作自审或普通论证路线时 |
| `references/proposition-form-core.md` | 需要还原关键 claim、一句话核心发现、X2、目标命题形态或反驳形态时 |
| `references/argument-tree-core.md` | 需要恢复论证树、定义节点/箭头/隐含前提时 |
| `skills/argument-arrow-audit/references/arrow-audit-core.md` | 执行验箭头时读取；这是整合断点分类、逻辑谬误、概念关系、数字统计、外推、机制预测和 GRE 指令输出的可执行断点库 |
| `skills/argument-arrow-repair-mapping/assets/arrow-repair-map-template.md` | 已有断点，需要输出可执行修复路线、知识来源审计、临时 repair menu 或降调方案时使用 |
| `skills/argument-issue-selection/references/issue-selection-principles.md` | 已有全量箭头审计表，需要选择可写问题、major concern 或 revision action 时读取 |
| `references/arrow-break-taxonomy.md` | 父层历史断点分类参考；新增验箭头任务优先使用 `arrow-audit-core.md` |
| `references/fallacy-taxonomy.md` | 父层逻辑谬误参考；新增验箭头任务优先在 `arrow-audit-core.md` 中作为 `break_type / fallacy_label` 使用 |
| `references/mermaid-obsidian-rules.md` | 需要输出 Mermaid / Obsidian 论证树时 |
| `references/output-ladder.md` | 需要决定输出为图、表、段落、审稿意见或完整文章时 |

## 领域适配原则

通用 workflow 不直接假设文本属于论文、商业报告或考试材料。任何专用领域必须通过 adapter 声明映射关系：

| 通用元素 | 学术审稿适配示例 |
|---|---|
| 论点 | 作者贡献声称、理论结论、政策启示 |
| 论据 | 文献、数据、变量、模型、回归结果、稳健性 |
| 箭头 | gap -> contribution；construct -> measure；identification -> causal claim；result -> theory |
| 概念不一致 | construct-measure mismatch |
| 过度推理 | evidence-claim mismatch |
| 因果跳跃 | identification 不足 |
| 更换衡量标准 | 用不适配指标评价目标概念 |

## 输出契约

最小输出：

```text
作者想证明：C
作者用来证明 C 的材料：A/B
隐含中间推理：A/B -> M -> C
当前最可疑的箭头：...
为什么推不出：...
建议如何补强或降调：...
```

当任务要求分析 assumptions / hidden premises 时，最小输出改为：

```text
作者隐含假设：H
H 支撑哪条箭头：A -> B
如果 H 不成立：B/C/root claim 如何变弱或断裂
需要什么证据补强：...
```

当任务要求列出 questions / evidence needed 时，最小输出改为：

```text
需要回答的问题：Q
Q 检验哪条箭头：A -> B
如果答案为 yes：论证如何被加强
如果答案为 no 或 alternative answer：论证如何被削弱
需要什么证据或澄清：...
```

结构化输出：

1. 核心论证链；
2. Mermaid 论证树；
3. 论证节点台账；
4. 支撑箭头审计表；
5. 断箭头修复映射表；
6. 关键词对照表；
7. 隐含假设表；
8. 标准匹配表；
9. 断点 / 谬误表；
10. 可直接改写成目标领域文本的段落草稿。

中文可读文本输出还应附带一次文风自检：

```text
是否能看出 A -> B 的断裂；
是否说明 A 只能支持 A1；
是否说明缺少哪个前提 / 证据 / 检验；
是否给出补强或收窄方向；
是否避免英文直译腔和抽象术语堆叠。
```

学术论文完整论证树还应输出：

```text
一句话核心发现：
X / M / Y / Y2 结构表：
evidence ledger：
  evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点/箭头 | 证据粒度
evidence-expanded Mermaid：
  E-* 具体证据 -> 子观点 -> 中层命题 -> X1/X2/Y
```

若底稿未保留表格具体数值，应标记 `needs-table-qc`，不得补写未核实的系数、t 值或显著性。

## 证据边界

- 通用 workflow 只保存可迁移规则，不保存具体稿件、审稿意见、课程逐字稿之外的个案判断。
- 课程资料和提取稿放在 `references/source-provenance.md` 与 `references/course-notes/` 中，不写入普通 Skill 主流程。
- 当前论效题子 workflow 已通过中文论效案例 forward-test 与 GRE official prior-exposed assisted UAT。
- 父 workflow 的跨领域迁移仍需在未参与提炼的新学术审稿、政策报告或商业论证案例上继续 forward-test。

## 与论文审稿 Workflow 的关系

`workflow-paper-writing-review` 不复制本 workflow 的通用论证知识。论文审稿场景调用：

```text
../workflow-argument-validity/skills/academic-review-argument-audit/
```

调用位置包括：

- 快速通读：还原作者贡献链；
- 文献定位：检查 gap -> contribution；
- 方法识别：检查 identification -> causal claim；
- 变量数据：检查 construct -> measure；
- 结果叙事：检查 result -> contribution；
- 最终审稿：把断点写成克制、清楚、可执行的审稿意见。
