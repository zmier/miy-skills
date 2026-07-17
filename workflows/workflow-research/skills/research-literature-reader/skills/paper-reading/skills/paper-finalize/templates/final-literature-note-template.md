# <论文标题> - 最终文献笔记

## Finalization Metadata / 定稿元信息

- 论文：
- PDF：
- Markdown 底稿：
- automatic-extraction：
- discussion-outline：
- Finalization mode：post-co-read / cold-start / batch-library
- Co-read status：
- 创建时间：
- 最近更新：
- 定稿者：

## Source Basis / 核验来源基础

- PDF 状态：
- Markdown 状态：
- 表格 / 图像状态：
- 公式状态：
- source-check 覆盖范围：
- 剩余 source 风险：

## Claim Status Vocabulary / 结论状态词

```text
verified-citable:
  已由原文 / PDF / 表格 / 公式核验，可引用。

verified-citable-text-summary:
  作者在正文中明确文字总结，可引用为“作者文本总结”；
  若包含表格派生数值，表格值仍需核验。

verified-citable-method-description:
  方法、数据、变量、模型设定已由原文核验，可引用。

verified-citable-directional-result:
  结果方向或显著/不显著的文字性结论已核验，可引用；
  精确数值仍需表格 / PDF 核验。

verified-citable-table-value:
  精确表格数值已由 PDF / restored table / source table 核验，可引用。

verified-understanding:
  可作为理解性判断，不建议直接作为作者原文结论引用。

inferred-not-citable:
  Agent / 用户推断，未被作者直接表述，不可直接引用。

needs-source-check:
  仍需回 PDF / 表格 / 公式 / 附录核验。

contradicted-or-revise:
  与原文不一致，必须修正或删除。
```

## Verified Core Finding / 已核验核心发现

### 理论纯净版

| 表述 | 状态 | Source Anchors | 备注 |
|---|---|---|---|
|  |  |  |  |

### 读者导览版

| 表述 | 状态 | Source Anchors | 备注 |
|---|---|---|---|
|  |  |  |  |

### 形式逻辑还原

| 逻辑形式 | 状态 | Source Anchors | 备注 |
|---|---|---|---|
|  |  |  |  |

## Verified Proposition Registry / 已核验命题登记表

| ID | 角色 | 分支类型 | 已核验表述 | 状态 | Source Anchors | 相比 automatic-extraction 的修订 |
|---|---|---|---|---|---|---|
| P1 | 核心命题 | core |  |  |  |  |
| P2 | 核心命题 | core |  |  |  |  |
| S-P1-diagnostic | 支撑分支 | diagnostic |  |  |  |  |

## Verified Proxy Bridge / 已核验 Proxy Bridge

| Bridge ID | 理论对象 / 关系 | Proxy / Measure | 原文支持的 warrant | 证据类型 | 状态 | 剩余威胁 |
|---|---|---|---|---|---|---|
| A03-P1-X |  |  |  | construct warrant / behavioral diagnostic / exclusion support / measurement validation |  |  |
| A03-P1-Y |  |  |  |  |  |  |
| A03-P2-X |  |  |  |  |  |  |

## Verified Measurement / Data / 已核验测量与数据

| Block ID | 关联 Pi-R | 数据来源 | 分析单位 | 样本 / 窗口 | 变量构造 | 状态 | Source Anchors |
|---|---|---|---|---|---|---|---|
| A04-P1-R |  |  |  |  |  |  |  |
| A04-P2-R |  |  |  |  |  |  |  |

## Verified Design / Identification / 已核验研究设计与识别强度

| Design ID | 关联 Pi-R | 设计 / 模型 | 时间顺序 | Design Claim Level | 能声称什么 | 不能声称什么 | 状态 |
|---|---|---|---|---|---|---|---|
| A05-P1-R |  |  |  | descriptive association / predictive relation / mechanism-consistent evidence / exclusion-enhanced explanation / quasi-causal / causal claim |  |  |  |
| A05-P2-R |  |  |  |  |  |  |  |

## Verified Results / 已核验经验结果

| Result ID | 关联命题 | 结果表述 | 方向 | 统计 / 经济意义 | 状态 | Source Anchors |
|---|---|---|---|---|---|---|
| A06-P1-R |  |  |  |  |  |  |
| A06-P2-R |  |  |  |  |  |  |

## Verified Alternatives / Validity Threats / 已核验替代解释与有效性威胁

| Threat ID | 关联命题 | 替代解释 / 威胁 | 作者检验 | 有效性类型 | 解决程度 | 剩余风险 | 状态 |
|---|---|---|---|---|---|---|---|
| A07-P1-1 |  |  |  | construct / internal / external / statistical conclusion | resolved / partially resolved / unresolved |  |  |
| A07-P2-1 |  |  |  |  |  |  |  |

## Transfer To Current Project / 迁移到当前项目

| 迁移项 | 可直接迁移 | 需要改造 | 不可迁移 | 需要数据 | 识别威胁 | 状态 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Citation-Ready Statements / 可引用表述

| ID | 表述 | 状态 | Source Anchors | 引用用途 |
|---|---|---|---|---|
| C1 |  |  |  |  |

## Understanding-Only Statements / 仅供理解表述

| ID | 表述 | 为什么不可直接引用 | Source Anchors |
|---|---|---|---|
| U1 |  |  |  |

## Not-Citable / Needs-Check Statements / 不可引用或待核验表述

| ID | 表述 | 原因 | 需要核验什么 |
|---|---|---|---|
| N1 |  |  |  |

## Verified Claims / 已核验 Claims 清单

> 如果单独生成 `verified-claims.md`，使用本节作为文件主体。

| Claim ID | Claim Type | Claim | Status | Source Anchors | Citation Use | Remaining Risk |
|---|---|---|---|---|---|---|
| VC1 | 作者原文 / 表格结果 / 方法描述 / Agent 重构 / 项目迁移 |  |  |  |  |  |

## Source-Check Log / Source-Check 核验账本

> 如果单独生成 `source-check-log.md`，使用本节作为文件主体。

| Check ID | Claim ID | Claim Type | First-Pass Statement | Source Checked | Check Action | Result | Claim Status | Verified Statement | Remaining Risk | Next Check |
|---|---|---|---|---|---|---|---|---|---|---|
| SC1 |  | 作者原文 / 表格结果 / 方法描述 / Agent 重构 / 项目迁移 |  |  | read paragraph anchors / compare with PDF page / check table / check equation / check figure |  |  |  |  |  |

## Open Questions / 开放问题

| ID | 问题 | 影响的 claim | 需要的 source / action | 优先级 |
|---|---|---|---|---|
| Q1 |  |  |  |  |
