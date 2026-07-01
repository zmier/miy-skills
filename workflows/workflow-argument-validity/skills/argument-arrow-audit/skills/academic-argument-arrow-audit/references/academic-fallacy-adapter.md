---
date: 2026-06-20
type: reference
status: seed / structural-green / forward-test-pending
scope:
  - academic-argument-arrow-audit
  - academic-review-argument-audit
---

# Academic Fallacy Adapter

## 定位

本文件负责把父层 `arrow-audit-core.md` 中的通用 `break_type / fallacy_label` 翻译为学术论文审稿、自审和写作修改中的领域表达。

使用顺序固定为：

```text
1. 先在作者论证树上固定 arrow_id: A -> B；
2. 用父层 arrow-audit-core 判断 A 为什么不足以推出 B；
3. 标注通用 break_type / fallacy_label；
4. 判断论文类型与学科语境；
5. 翻译成审稿人能接受的领域术语和可执行修改建议。
```

不要在审稿正文中直接写“作者犯了某某逻辑谬误”。谬误标签只保留在工作表中，正文应写成克制、具体、可证据化的学术表达。

## 通用映射

| break_type / fallacy_label | 学术通用表达 | 审稿句式 |
|---|---|---|
| concept-mismatch / 偷换概念 | conceptual slippage / construct mismatch | The manuscript appears to move between different meanings of the focal construct. |
| measurement-mismatch / 指标错配 | construct-measure mismatch | The operational measure may not capture the theoretical construct claimed in the paper. |
| causal-leap / 强加因果 | causal claim not supported by design | The evidence is consistent with the proposed relationship, but the design does not yet support the causal interpretation. |
| alternative-explanation / 另有他因 | alternative mechanism / omitted explanation | The current analysis does not rule out plausible alternative explanations. |
| scope-expansion / 以偏概全 | overgeneralization / external validity concern | The evidence supports a narrower claim than the broader contribution currently asserted. |
| sample-weakness / 样本不足 | sample selection / population fit concern | The sample may not represent the population or mechanism relevant to the claim. |
| numerical-trap / 数字谬误 | scale, baseline, magnitude, or statistical interpretation concern | The magnitude and scale of the reported variable or coefficient need clearer interpretation. |
| comparison-mismatch / 不当比较 | non-comparable benchmark / inappropriate comparison | The comparison does not appear to use comparable units, conditions, or baselines. |
| uncontrolled-comparison / 对比未控变量 | confounded comparison | The comparison changes multiple factors at once, making the target interpretation difficult to isolate. |
| condition-confusion / 充分必要混淆 | necessary/sufficient condition ambiguity | The argument treats a possible condition as if it were necessary or sufficient. |
| hidden-premise-missing / 不当假设 | unstated assumption / unsupported premise | The inference depends on an assumption that is not yet established. |
| overclaim / 过度推理 | evidence-claim mismatch | The empirical/theoretical evidence supports a more limited conclusion than the manuscript claims. |
| evidence-qc-gap | reporting transparency / evidence traceability concern | The claim cannot be fully assessed without clearer reporting or traceable evidence. |

## 实证论文 Adapter

实证论文中，通用断点通常翻译为变量、样本、识别、估计、机制、稳健性和结果解释问题。

| 通用断点 | 实证表达 | 常见落点 |
|---|---|---|
| concept-mismatch | theoretical construct and empirical proxy are not aligned | 核心变量定义、代理变量、指标来源 |
| measurement-mismatch | the measure captures only a proxy, component, or adjacent outcome | 变量操作化、量纲、指数、份额 |
| causal-leap | identification does not support the causal claim | 内生性、反向因果、遗漏变量、共同趋势、IV 排除限制 |
| alternative-explanation | plausible omitted variables or rival mechanisms remain | 机制检验、控制变量、固定效应、事件窗口 |
| sample-weakness | sample selection limits mechanism or external validity | 样本筛选、行业/地区/年份覆盖、缺失值处理 |
| numerical-trap | unclear scale, transformation, magnitude, or statistical significance | 描述统计、回归表、系数解释、经济显著性 |
| comparison-mismatch | benchmark or comparison group is not comparable | 对照组、异质性分组、政策前后比较 |
| uncontrolled-comparison | multiple changes confound the target effect | DiD、PSM、事件研究、机制分组 |
| overclaim | result supports association/local effect, not broad causal contribution | 摘要、结论、贡献段、政策启示 |

表达原则：

```text
不要写：作者强加因果。
要写：The current design establishes an association, but it does not yet rule out reverse causality or omitted-variable explanations sufficiently to support the causal wording.
```

## 理论 / 模型论文 Adapter

理论或模型论文中，断点通常翻译为定义、假设、公理、命题、证明、边界条件和解释范围问题。

| 通用断点 | 理论表达 | 常见落点 |
|---|---|---|
| concept-mismatch | key concept is defined or used inconsistently | 定义、命题、变量含义 |
| hidden-premise-missing | proposition relies on an unstated assumption | 假设集合、证明步骤、命题前提 |
| condition-confusion | condition is treated as necessary/sufficient without proof | 定理条件、命题边界、比较静态 |
| causal-leap | mechanism is asserted rather than derived | 理论机制、模型推导、命题解释 |
| scope-expansion | result under narrow assumptions is generalized too broadly | 边界条件、适用情境、贡献段 |
| contradiction | assumptions, propositions, or implications conflict | 模型设定、推导、讨论 |
| one-sided-reasoning | countervailing mechanism or equilibrium response is ignored | 均衡、约束、反向激励、成本 |
| overclaim | model result is presented as a general theory | 讨论、结论、理论贡献 |

表达原则：

```text
不要写：作者不当假设。
要写：The proposition appears to require an additional assumption about [...], but this assumption is not stated or justified in the model setup.
```

## 综述 / 概念 / 框架论文 Adapter

综述、概念和框架论文中，断点通常翻译为文献谱系、概念边界、分类维度、整合逻辑和研究议程问题。

| 通用断点 | 综述/概念表达 | 常见落点 |
|---|---|---|
| concept-mismatch | concept boundary is unstable or conflates adjacent constructs | 概念定义、分类表、框架图 |
| scope-expansion | limited literature stream is treated as field-wide consensus | 文献覆盖、知识树、研究议程 |
| comparison-mismatch | categories are not mutually comparable | 分类维度、类型学、对照表 |
| false-dichotomy | framework treats non-exclusive categories as mutually exclusive | 二分框架、类型划分 |
| standard-shift | classification criteria change across sections | 维度、编码规则、纳入排除标准 |
| hidden-premise-missing | synthesis relies on an unstated organizing principle | 理论整合、框架构建 |
| overclaim | framework is positioned as more integrative than demonstrated | 贡献段、结论、未来研究 |

表达原则：

```text
不要写：作者偷换概念。
要写：The framework would be stronger if the boundary between [...] and [...] were specified more consistently, because the current synthesis sometimes treats them as interchangeable.
```

## 材料 / 器件 / 工科实验论文 Adapter

材料、器件和工科实验论文仍然遵循父层 `arrow-audit-core.md` 的通用逻辑：先问 `A 是否足以推出 B`，再把断点翻译成实验论文语言。

详细规则见：

```text
materials-device-arrow-adapter.md
```

常见翻译：

| 通用断点 | 工科实验表达 | 常见落点 |
|---|---|---|
| mechanism-over-interpretation / hidden-premise-missing | characterization evidence does not yet establish the proposed mechanism | SEM/XPS/FTIR/Raman/XRD、schematic、传输模型 |
| comparison-mismatch / numerical-trap | performance comparison is not normalized under comparable conditions | current density、power density、SOTA 表、面积/质量/长度归一化 |
| uncontrolled-comparison | control experiments do not isolate the claimed factor | 单因素优化、材料替换、工艺参数筛选 |
| scope-expansion / overclaim | prototype demonstration does not yet support practical application | LED、织物、传感、手机、灯泡、人体佩戴 demo |
| extrapolation-mismatch | short-term stability is insufficient for long-term durability | 600 s 曲线、短循环、洗涤/弯折/储存 |
| evidence-qc-gap | source figures, supplementary data, or raw values need verification | 图面板、补充图、原始数据、误差线、n |

表达原则：

```text
不要写：作者以偏概全。
要写：The current demonstration supports proof-of-concept integration, but it does not yet establish continuous operation under realistic load and wearing conditions.
```

## 案例反哺协议

后续遇到真实审稿意见、返修意见或优秀论文表达时，按 `course-driven-skill-engineering` 的真实案例/对话洞见反哺方式积累。

每条新增表达至少记录：

```text
case_id:
paper_type: empirical / theory-model / review-concept / methods / mixed
discipline:
arrow_id:
from_node:
to_node:
break_type:
fallacy_label:
domain_expression:
review_sentence_pattern:
evidence_location:
why_transferable:
status: candidate / structural-green / forward-test-pending / validated
```

沉淀规则：

- 个案原文、保密稿件、具体判断留在 TASK 或 case；
- 可迁移表达进入本 adapter；
- 新增映射不得只因为“这句话好听”就进入通用表，必须说明它解决哪类 `A -> B` 断点；
- 新表达先标 `candidate`，至少经过一个新案例可用后再标 `validated`；
- 如果某表达只适用于特定学科、期刊或方法传统，写入对应论文类型或 discipline-specific 小节，不进入通用映射表。
