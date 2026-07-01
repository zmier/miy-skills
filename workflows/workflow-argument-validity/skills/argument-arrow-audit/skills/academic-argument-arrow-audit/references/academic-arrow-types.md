---
date: 2026-06-19
type: reference
status: seed
scope:
  - academic-argument-arrow-audit
---

# Academic Arrow Types

本文件不是传统审稿 checklist。它只用于给已经抽出的 `arrow_id: A -> B` 标注学术论文中的箭头类型。

若需要把通用断点或逻辑谬误翻译成实证、理论、综述/概念论文的审稿语言，读取 `academic-fallacy-adapter.md`。若论文是材料、器件、能源收集、传感器、柔性电子、可穿戴或其他工科实验论文，读取 `materials-device-arrow-adapter.md`。本文件回答“这是什么学术箭头”，adapter 回答“这个断点在论文里怎么说”。

正确顺序：

```text
先取 arrow_id
-> 判断 A 是否足以推出 B
-> 再标 arrow_type
-> 最后翻译成审稿问题
```

错误顺序：

```text
按 gap / 变量 / 样本 / 识别 / 机制 / 稳健性 逐项巡检
```

模块名不能替代箭头审计。

| arrow_type | from -> to | 常见问题 |
|---|---|---|
| gap-contribution | 文献缺口 -> 贡献成立 | gap 不真实、不重要、只是换样本/场景/指标 |
| construct-measure | 理论构念 -> 操作化指标 | 指标只测到代理、局部、结果或相邻概念 |
| treatment-definition | 处理定义 -> X 成立 | 处理变量混入被动、滞后、反向选择或定义漂移 |
| sample-mechanism-fit | 样本规则 -> 机制相关样本 | 样本筛选剔除最能检验机制的事件 |
| construct-level-fit | 经典构念层级 -> 本文操作化层级 | 宏观/行业构念被改成公司/事件指标但未说明适配 |
| timing-fit | 事件/处理窗口 -> 行为反应/结果测量 | 信息可见、行为反应和结果测量窗口错位 |
| baseline-fit | 剔除/分组规则 -> 溢出或机制比较成立 | 缺少事件公司、自身变化或必要对照基准 |
| identification-causal | 模型/识别 -> 因果声称 | 后门路径未关闭、共同趋势不足、聚类层级错误 |
| result-finding | 回归结果 -> 核心发现 | 显著性、方向、经济意义、量纲或报告不清 |
| mechanism-claim | 机制检验 -> 机制成立 | 机制代理弱、排除机制有反向解释、样本不一致 |
| robustness-threat | 稳健性 -> 核心威胁已回应 | 只换口径，没有回应真正威胁 |
| finding-contribution | 具体发现 -> 理论/政策/管理贡献 | 短期、局部、代理指标被上升为宏大贡献 |

## 材料 / 器件 / 工科实验论文常见箭头

这些箭头仍然服从通用 `A -> B` 审计，只是证据形态不同。详细验法见 `materials-device-arrow-adapter.md`。

| arrow_type | from -> to | 常见问题 |
|---|---|---|
| process-material-identity | 制备流程/工艺参数 -> 材料或器件被成功制备 | 关键参数、批次、重复性、尺寸分布或产率缺失 |
| characterization-structure | SEM/FTIR/XPS/Raman/XRD 等表征 -> 结构/成分/性质改变 | 表征只能证明局部或表面变化，不能推出整体功能 |
| characterization-mechanism | 表征/示意图/传输测试 -> 机制成立 | plausibility 被写成 proof，缺直接机制实验 |
| control-factor-causality | 单因素对照 -> 某因素导致性能提升 | 多因素同时改变，缺等量/等结构/等面积对照 |
| metric-performance | 电压/电流/效率/灵敏度等指标 -> 高性能 | 量纲、面积、质量、长度、负载、环境或误差不清 |
| normalized-sota-superiority | current density / power density / per-mass 指标 -> 优于 SOTA | 分母、工况、负载和器件几何不可比 |
| stability-durability | 短时稳定/循环/洗涤/弯折 -> 长期耐久或可穿戴 | 测试时间、循环次数和真实工况不足 |
| demo-application | LED/织物/传感/手机/灯泡 demo -> 实际应用能力 | demo 只支持 proof-of-concept，不支持连续真实负载 |
| lab-realworld-fit | 模拟液/标准环境/静态测试 -> 真实环境部署 | 实验室条件不能自动外推到真实人体、现场或产业环境 |

## 审查口诀

```text
先问作者用什么推什么；
再问这个证据最直接说明什么；
最后问差出来的那一步需要什么前提。
```

例子：

```text
A = KV 下降
B = 信息披露质量提升
问题不是“变量模块有没有问题”，而是：
KV 下降是否足以推出信息披露质量提升？
若不足，再标为 construct-measure arrow 的 measurement mismatch。
```

```text
A = PSM / placebo / Oster / 替换变量通过
B = 样本筛选、处理定义、聚类层级等核心威胁已被回应
问题不是“稳健性模块有没有问题”，而是：
这些检验是否真的回应了目标威胁？
若不足，再标为 robustness-threat arrow。
```

## 类型到验法的路由

判断 arrow_type 之后，按下表决定验法。注意：路由不是审查顺序，仍然必须从具体 `arrow_id: A -> B` 出发。

| arrow_type | 默认验法 | 何时升级 |
|---|---|---|
| gap-contribution | 检查 gap 是否真实、重要、不同于既有研究 | 需要检索或知识树定位时，调用 `skills/academic-literature-gap-arrow-audit` |
| construct-measure | 用父层概念关系、定义回代和 measurement mismatch 审查 | 若形成复杂学科指标库，再拆子 Skill |
| treatment-definition | 检查处理定义是否能代表 X，是否混入选择、滞后或反向机制 | 若涉及复杂政策/事件编码，先沉淀 reference |
| sample-mechanism-fit | 检查样本是否覆盖机制发生场景 | 若跨多个数据源和样本筛选规则，先沉淀 reference |
| construct-level-fit | 检查原构念层级与本文指标层级是否一致，是否需要外部文献或原始构念定义 | 若需系统梳理构念来源，进入 external evidence request |
| timing-fit | 检查事件、披露、反应和结果测量的时间链条 | 若涉及复杂事件研究或动态 DID，调因果/统计子 Skill |
| baseline-fit | 检查是否缺少证明溢出/学习/竞争所需的基准 | 若涉及样本设计和机制识别，先由父 Skill 审 |
| identification-causal | 检查因果设计是否支持 causal claim | 调用 `skills/academic-causal-arrow-audit`；可使用 DAG、后门/前门、DID/IV/PSM/RDD 等方法 |
| result-finding | 检查表格、系数、显著性、量纲和经济意义是否支持发现 | 调用 `skills/academic-statistical-result-arrow-audit` |
| mechanism-claim | 检查机制检验是否足以证明机制，而非相关代理、概念滑动、样本不一致或反向解释 | 父 Skill 先审；复杂中介/调节/实验机制后再拆 |
| robustness-threat | 检查稳健性是否回应目标威胁 | 父 Skill 先审；高频方法后沉淀 method reference |
| finding-contribution | 检查具体发现是否被过度上升为理论/政策/发表价值 | 父 Skill 先审，输出给 issue selection 和写作层 |
| materials/device arrows | 检查表征、性能、SOTA、稳定性和 demo 是否足以推出机制、性能和应用声称 | 读取 `materials-device-arrow-adapter.md`；若涉及 SOTA 或机制标准，进入 external evidence request |

## 外部证据与工具调用

只有当箭头本身需要外部证据时才调用检索 Skill。例如：

```text
arrow_type: gap-contribution
作者声称：现有文献没有研究 X 对 Y
需要：查 FT50 / UTD24 / 综合顶刊 / Nature / Science / PNAS / 中文川大B以上是否已有相同或近似研究
调用：scholar-kit-literature-search
```

不得因为“文献模块”四个字就自动检索；先判断目标箭头是否真的依赖外部文献证据。

## 机制箭头的额外检查

机制箭头不能只看“机制表是否显著”。至少检查三类一致性：

```text
mechanism-concept-consistency:
  理论部分、机制检验、异质性分析、排除机制和结论中，机制概念是否保持同一含义？
  例如“披露行为的信号效应”和“披露内容的信息效应”是否被按需切换？

mechanism-sample-consistency:
  事件研究、机制分组、主回归和异质性回归是否使用同一或可比样本？
  如果图形样本和回归样本不同，机制前提能否推到机制结论？

mechanism-direction-consistency:
  机制证据是否支持作者声称方向？
  不显著结果、反向显著结果或某一窗口冲突是否被正文选择性解释？
```

对应 QC flags：

```text
mechanism-concept-qc
sample-consistency-qc
table-text-conflict-qc
```


## Major Concern 选择

优先写：

- 断点影响核心发现 `X2`；
- 断点影响最终贡献 `Y`；
- 多个表格/机制/稳健性共同指向同一弱箭头；
- 需要作者新增核心分析，而非只改文字。

降为 minor：

- 单个表注、措辞、格式；
- 不影响主要识别和贡献链的补充说明；
- 可通过一句解释修复的术语不清。
