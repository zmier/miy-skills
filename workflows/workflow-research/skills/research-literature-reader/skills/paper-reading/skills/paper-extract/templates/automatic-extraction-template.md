# <论文标题> - 自动抽取

## 来源

- 论文：
- PDF：
- Markdown 底稿：
- 阅读底稿状态：
- 当前项目：
- 当前 task / route：
- 创建时间：
- 最近更新：

## 抽取状态

- 抽取范围：
- source anchors 质量：
- 表格 / 图片可靠性：
- 未回原文核对前不可引用：
- 剩余风险：

## A01 核心断言与形式逻辑

> 理论纯度闸门：A01 必须先写理论对象 / 抽象构念 / 理论关系。变量名、数据库字段、回归构造、proxy、表格结果只能作为后续操作化提示，不得替代理论命题本身。
> 命题角色闸门：只有通过 collapse test、take-away test、independence test 的断言才列为 P1/P2/P3。机制、诊断模式、边界条件、排除解释、稳健性和 proxy 可信性默认列为 S-Pi-*。重要但不确定的分支列为 candidate S/P。

### 一句话核心发现：理论纯净版

> 用理论对象 / 抽象构念 / 理论关系表达；不得写 proxy、变量名、数据字段或表格结果。

### 一句话核心发现：读者导览版

> 可以加入本文关键 empirical implementation，帮助进入论文；不得替代理论纯净版。

### 形式逻辑完整还原

### 核心命题准入测试

| 候选命题 | Collapse Test | Take-Away Test | Independence Test | 判定为 P / S / candidate | 理由 |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### 命题登记表

| ID | 角色 | 分支类型 | 命题 / 支撑判断 | 服务对象 | 状态 | Source Anchors | 备注 |
|---|---|---|---|---|---|---|---|
| P1 | 核心命题 | core proposition |  | self | pending |  |  |
| P2 | 核心命题 | core proposition |  | self | pending |  |  |
| S-P1-diagnostic | 支撑分支 | diagnostic / mechanism / proxy / exclusion / robustness / boundary / measurement |  | P1 | pending |  |  |
| C-SP-1 | candidate S/P | role-uncertain |  | 待确认 | pending |  |  |

## A02 论证结构 / 理论关系

> A02 是从 A01 命题逆向拆概念。必须先做忠实形式逻辑化，再拆命题域顶层概念、概念内部结构、共享概念和 relation IDs，最后再写概念关系摘要和 Pi-KB。
> 形式逻辑化只能补全省略、还原指代词和标注命题形式，不得添加机制、proxy、诊断结果或证据链。
> 若出现可观察变量、统计构造、表格结果或具体数据库口径，必须判断是否越界；默认移到 A03 / A04 / A06 / A07。

### A02.1 命题形式逻辑化

| 命题 ID | A01 原命题 / 简写 | 形式逻辑完整表述 | 命题形式：直言 / 假言 / 联言 / 选言 | 忠实转写说明：补全了什么，是否添加新内容 | Source Anchors | 需要回原文核对 |
|---|---|---|---|---|---|---|
| P1 |  |  |  |  |  |  |
| P2 |  |  |  |  |  |  |

### A02.2 Shared Concept Registry

> 跨命题复用的概念必须优先放在这里。各 Pi 后续引用 concept ID，不要重复发明不同写法。

| Shared Concept ID | 概念名称 | 概念定义 / 边界 | 父概念 | 子概念 / 维度 | 被哪些命题引用 | Source Anchors | 备注 |
|---|---|---|---|---|---|---|---|
| Shared-C1 |  |  |  |  | P1; P2 |  |  |
| Shared-C2 |  |  |  |  |  |  |  |

### A02.3 Proposition-Scoped Top-Level Concepts

> 从形式逻辑完整命题中直接拆出来的才是 `top-level concept`。机制、维度、状态变化、诊断结果和 proxy 不得与顶层概念平铺。

| 命题 ID | Concept ID | 概念名称 | 父概念 / 引用 Shared-C | 概念角色 | 是否直接来自命题文本 | Source Anchors | 备注 |
|---|---|---|---|---|---|---|---|
| P1 | P1-C1 |  |  | subject / object / predicate concept / condition / relation-target | yes / no |  |  |
| P1 | P1-C2 |  |  | subject / object / predicate concept / condition / relation-target | yes / no |  |  |
| P2 | P2-C1 |  |  | subject / object / predicate concept / condition / relation-target | yes / no |  |  |
| P2 | P2-C2 |  |  | subject / object / predicate concept / condition / relation-target | yes / no |  |  |

### A02.4 Concept Internal Decomposition

> 每个 top-level concept 必须检查是否需要继续拆分。A02 子概念是概念内部的理论维度、构成要素、边界条件、机制候选或状态变化；经验 proxy / 变量 / 数据字段进入 A03/A04。

| Parent Concept ID | Child Concept ID | 子概念名称 | 子概念类型：dimension / component / boundary / mechanism-candidate / state-change / relation-target | 是否来自作者文本 | Source Anchors | 停止拆分理由 / 下一层去向 |
|---|---|---|---|---|---|---|
| P1-C1 | P1-C1.1 |  |  | yes / inferred / needs-source-check |  |  |
| P1-C2 | P1-C2.1 |  |  | yes / inferred / needs-source-check |  |  |
| P2-C1 | P2-C1.1 |  |  | yes / inferred / needs-source-check |  |  |
| Shared-C1 | Shared-C1.1 |  |  | yes / inferred / needs-source-check |  |  |

### A02.5 Concept Relation Summary

| Relation ID | 命题 ID | Relation Statement | Relation Type | Linked Concept IDs | Pi-KB | Source Anchors | 需要回原文核对 |
|---|---|---|---|---|---|---|---|
| P1-R1 | P1 |  | categorical / causal / association / mechanism / boundary | P1-C1; P1-C2 |  |  |  |
| P2-R1 | P2 |  | categorical / causal / association / mechanism / boundary | P2-C1; P2-C2 |  |  |  |

### A02.6 A02 Boundary Notes

| Item | 判断 | 应放位置 | 理由 |
|---|---|---|---|
| 机制 / warrant |  | A02 child concept / Main Mechanism / A07 |  |
| empirical proxy / observable measure |  | A03 |  |
| 变量计算、数据库、窗口、样本 |  | A04 |  |
| 模型、控制变量、固定效应、识别策略 |  | A05 |  |
| 表格结果、系数、显著性、经济意义 |  | A06 |  |
| diagnostic evidence / robustness / exclusion |  | A07 or S-Pi-* |  |

## A03 操作化 / Proxy Bridge

> A03 回答“抽象构念如何落到可观察对象”。每一行必须回挂 A02 Node ID，不得只列 proxy / variable。若 proxy 对应的概念尚未出现在 A02，先回 A02 补概念，或标记 `A02-revision-needed`。
> `为什么可信` 必须回答：代理哪个 A02 node；为什么有资格代理；作者用了什么 evidence / diagnostic / exclusion test 支持；仍有什么测量误差或竞争解释。

### A03.1 Concept-To-Proxy Bridge

| Bridge ID | A02 Node ID | A02 Node Type | A02 Concept / Subconcept | Empirical proxy / observable / measure | Proxy warrant：为什么能代理 | 支持证据 / 诊断 / 排除检验 | 构念效度风险 / 竞争解释 | Source Anchors | 后续议程 |
|---|---|---|---|---|---|---|---|---|---|
| A03-P1-C1 | P1-C1 | top-level concept |  |  |  |  |  |  | A04 |
| A03-P1-C1.1 | P1-C1.1 | child concept |  |  |  |  |  |  | A04 |
| A03-Shared-C1 | Shared-C1 | shared concept |  |  |  |  |  |  | A04 |
| A03-P2-C1 | P2-C1 | top-level concept |  |  |  |  |  |  | A04 |

### A03.2 Relation-To-Diagnostic Bridge

| Bridge ID | A02 Relation / Supporting ID | Node Type | A02 Relation / Support Claim | Diagnostic empirical pattern / measure | Diagnostic warrant：为什么能支持该关系 | 剩余威胁 / 替代解释 | Source Anchors | 后续议程 |
|---|---|---|---|---|---|---|---|---|
| A03-P1-R1 | P1-R1 | relation |  |  |  |  |  | A05/A06/A07 |
| A03-P2-R1 | P2-R1 | relation |  |  |  |  |  | A05/A06/A07 |
| A03-S-P2-diagnostic | S-P2-diagnostic | supporting branch |  |  |  |  |  | A06/A07 |

### A03.3 Proxy Credibility / Construct Validity Summary

| Bridge ID | 可信度判断 | 最主要风险 | 是否需要回原文 / PDF / 表格核对 | 备注 |
|---|---|---|---|---|
| A03-P1-C1 |  |  |  |  |
| A03-P2-R1 |  |  |  |  |

## A04 测量与数据构造

> A04 按 Pi-R / design block 组织。核心测量承接 A03；控制变量、固定效应变量、筛选变量、滞后项、权重、分组变量等都是特定 design block 的支撑测量，不是全篇统一 controls。

| Block ID | 服务的 Pi-R | 关联 A03 Bridges | 分析单位 | 样本 / 窗口 | 来自 A03 的核心测量 | 本 Block 的设计支撑测量 | 测量 / 数据风险 | Source Anchors |
|---|---|---|---|---|---|---|---|---|
| A04-P1-R1 | P1-R1 | A03-P1-C1; A03-P1-C1.1; A03-P1-R1 |  |  |  |  |  |  |
| A04-P2-R1 | P2-R1 | A03-P2-C1; A03-P2-R1; A03-S-P2-diagnostic |  |  |  |  |  |  |

### A04 说明

- A04 回答：变量如何进入数据？
- 核心测量应说明 A03 关联变量的数据来源、变量构造、聚合方式、滞后、分组和窗口。
- 设计支撑测量应列出本 block 特有的控制变量、固定效应变量、样本筛选变量、排序 / 分组变量、权重和稳健性变量变体如何被量化。
- 不要暗示整篇论文共享一套全局 controls。

## A05 研究设计 / 识别策略

> A05 与 A04 使用同一 Pi-R / design block 组织。A05 解释变量为什么进入模型或比较逻辑，而不是重复变量如何被测量。

| Design ID | 关联 A04 Block | 命题 ID | 被检验的 Pi-R | 研究方式 | 经验检验 / 模型 / 比较逻辑 | 时间顺序 | 变量的设计功能 | 识别主张 | 关键假设 / 威胁 | Source Anchors |
|---|---|---|---|---|---|---|---|---|---|---|
| A05-P1-R | A04-P1-R | P1 |  |  |  |  |  |  |  |  |
| A05-P2-R | A04-P2-R | P2 |  |  |  |  |  |  |  |  |

### A05 说明

- A05 回答：变量为什么进入模型或比较逻辑？
- 说明核心变量、控制变量、固定效应、分组、匹配、权重、滞后和窗口各自的设计功能。
- 说明该设计支持相关、预测、机制解释，还是因果解释。
- 不要把 A04 的变量测量细节搬到 A05，除非这些细节直接影响设计逻辑。

## A06 资料分析 / 经验结果

| Result ID | 命题 ID | 被检验关系 | 主要结果 | 方向是否符合理论 | 统计意义 | 经济 / 实质意义 | 在论证中的角色 | Source Anchors |
|---|---|---|---|---|---|---|---|---|
| A06-P1-R | P1 |  |  |  |  |  |  |  |
| A06-P2-R | P2 |  |  |  |  |  |  |  |

## A07 替代解释 / 稳健性 / 有效性威胁

| Threat ID | 服务命题 | 威胁 / 替代解释 | 作者检验 / 回应 | 有效性类型 | 是否解决 | 剩余风险 | Source Anchors |
|---|---|---|---|---|---|---|---|
| A07-P1-1 | P1 |  |  |  |  |  |  |
| A07-P2-1 | P2 |  |  |  |  |  |  |

## A08 迁移到当前项目

- 可直接复用：
- 需要改造：
- 不可迁移：
- 当前已有数据：
- 仍需补充数据：
- 测量启发：
- 识别威胁：
- route mapping：
- 下一步深读 / source-check 位置：

## 开放问题

| ID | 问题 | 服务对象 | 是否需要回原文核对 | 备注 |
|---|---|---|---|---|
| Q1 |  |  |  |  |
