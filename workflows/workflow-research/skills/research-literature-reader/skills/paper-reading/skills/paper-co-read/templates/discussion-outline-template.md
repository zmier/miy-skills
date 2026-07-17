# <Paper Title> - Co-Reading Discussion Outline

## Source

- Paper:
- PDF:
- Markdown substrate:
- Automatic extraction:
- Reading status:
- Current project:
- Current task / route:
- Created:
- Last updated:

## Purpose

本文件是共同读工作台，不是完整自动抽取文档。结构化底稿见 `automatic-extraction.md`；本文件记录用户问题、讨论进度、当前共识、待核验点和可提升资产。

## Orientation Card Snapshot

> 第一轮卡片必须区分理论层和经验层。理论层写 core P1 / P2 / P3 的抽象命题；经验层再写 observable / proxy / measure。不要把 proxy 写成命题本身。
> 同时区分核心命题和支撑 / 诊断分支。机制、诊断模式、边界条件、替代解释排除、robustness、proxy 可信性支撑默认放在 Supporting / Diagnostic Branches，而不是自动升格为 P3。

### One-Sentence Core Finding: Theory-Pure Version

> Use theory objects / constructs / relations. Do not use proxy, variable names, data fields, or table results.

### One-Sentence Core Finding: Reader-Guide Version

> May include the paper's empirical implementation for orientation. Do not let it replace the theory-pure version.

### Initial Logical Form

### Core Proposition Branches

> Keep this at the theory-relation level. Only include propositions that pass collapse test, take-away test, and independence test.

### A02 Logical Form And Concept Hierarchy Snapshot

> A02 是从 A01 命题逆拆概念，不是全篇概念清单。先忠实还原形式逻辑完整命题，再拆顶层概念、子概念、共享概念和概念关系。不得在形式逻辑化时添加机制、proxy、诊断结果或证据链。

#### Proposition Logical Forms

| Proposition ID | A01 Short Proposition | Faithful Logical-Form Proposition | Proposition Type: categorical / hypothetical / conjunctive / disjunctive | Rewrite Notes |
|---|---|---|---|---|
| P1 |  |  |  |  |
| P2 |  |  |  |  |

#### Shared Concept Registry

| Shared Concept ID | Concept | Definition / Boundary | Used By | Role Difference Across Propositions |
|---|---|---|---|---|
| Shared-C1 |  |  | P1; P2 |  |

#### Proposition-Scoped Concept Hierarchy

| Proposition ID | Concept ID | Level | Concept | Parent / Shared Concept | Role | Directly From Proposition? |
|---|---|---|---|---|---|---|
| P1 | P1-C1 | top-level |  |  | subject / object / predicate concept / condition / relation-target | yes / no |
| P1 | P1-C1.1 | child |  | P1-C1 | dimension / mechanism candidate / state / boundary | yes / no |
| P2 | P2-C1 | top-level |  |  | subject / object / predicate concept / condition / relation-target | yes / no |
| P2 | P2-C1.1 | child |  | P2-C1 | dimension / mechanism candidate / state / boundary | yes / no |

#### Concept Internal Decomposition

| Parent Concept ID | Child Concept ID | Child Concept | Child Type | Source / Status | Stop Rule / Next Layer |
|---|---|---|---|---|---|
| P1-C1 | P1-C1.1 |  | dimension / component / boundary / mechanism-candidate / state-change | yes / inferred / needs-source-check |  |
| Shared-C1 | Shared-C1.1 |  | dimension / component / boundary / mechanism-candidate / state-change | yes / inferred / needs-source-check |  |

#### Concept Relation Summary

| Relation ID | Proposition ID | Relation Summary | Linked Concept IDs | Current Discussion Status | Open Question |
|---|---|---|---|---|---|
| P1-R1 | P1 |  |  | pending |  |
| P2-R1 | P2 |  |  | pending |  |

### Supporting / Diagnostic Branches

| ID | Branch Type | Support Claim | Serves | Why Not Core / Pending Role Question | Source Anchors |
|---|---|---|---|---|---|
| S-P1-diagnostic | diagnostic / mechanism / boundary / exclusion / robustness / proxy / measurement |  | P1 |  |  |
| C-SP-1 | candidate S/P |  | 待确认 |  |  |

### A03 Bridge Snapshot

> A03 必须回挂 A02 Node ID。这里记录共同读中已讨论过的 concept-to-proxy 和 relation-to-diagnostic bridge。

| Bridge ID | A02 Node ID | A02 Node Type | A02 Concept / Relation | Observable / Proxy / Diagnostic Measure | Proxy / Diagnostic Warrant | Remaining Risk |
|---|---|---|---|---|---|---|
| A03-P1-C1 | P1-C1 | concept |  |  |  |  |
| A03-P1-C1.1 | P1-C1.1 | child concept |  |  |  |  |
| A03-P1-R1 | P1-R1 | relation |  |  |  |  |
| A03-P2-R1 | P2-R1 | relation |  |  |  |  |

### Main Mechanism / Warrant

### Literature Conversation

### Research Gap

### Initial Transferability To Current Project

### Suggested Next Reading

## Proposition Registry

| ID | Role | Proposition / Support Claim | Serves | Current Status | Source In Automatic Extraction | Notes |
|---|---|---|---|---|---|---|
| P1 | core proposition |  | self | pending |  |  |
| P2 | core proposition |  | self | pending |  |  |
| S-P1-diagnostic | support / diagnostic / mechanism / boundary / exclusion / robustness / proxy / measurement |  | P1 | pending |  |  |
| C-SP-1 | candidate S/P |  | 待确认 | pending |  |  |

## Discussion Agenda

| ID | Topic | Status | Why It Matters | Current Consensus | Open Questions |
|---|---|---|---|---|---|
| A01 | One-sentence core finding | pending | Establish shared understanding |  |  |
| A02 | Logical form and concept hierarchy | pending | Turn each core proposition into faithful logical form, proposition-scoped concepts, shared concepts, and theory-level relations |  |  |
| A03 | Operationalization and proxy bridge | pending | Map abstract objects to proxies and warrants |  |  |
| A04 | Measurement and data construction | pending | Understand how proxies / measures are quantified in data |  |  |
| A05 | Research design and identification strategy | pending | Understand how variables test each Pi-R |  |  |
| A06 | Data analysis and empirical results | pending | Judge whether results support each Pi-R |  |  |
| A07 | Alternative explanations, robustness, and validity threats | pending | Judge credibility against competing explanations |  |  |
| A08 | Transfer to current project | pending | Decide what becomes project asset |  |  |
| A09 | Next reading targets | pending | Decide what to read next |  |  |

## User-Facing Progress Summary

> 对话窗口向用户汇报时，不能只写 `A01: pending` 这类内部编号。必须写成“编号 + 自然语言任务名 + 当前含义”。如果用户不熟悉编号，优先用口语总结。

### Compact Summary

- 已完成：
- 正在推进：
- 下一步建议：
- 仍需核验：

### Agenda Translation

| Internal ID | User-Facing Topic | Current Status In Plain Language | Why It Matters To The Reader |
|---|---|---|---|
| A01 | 核心发现 / 论文最想让人带走的那句话 |  |  |
| A02 | 作者如何在理论层论证核心发现 |  |  |
| A03 | 抽象概念如何落到可观察 proxy |  |  |
| A04 | 变量如何进入数据 |  |  |
| A05 | 作者如何组织研究设计 / 识别策略 |  |  |
| A06 | 经验结果如何支撑命题 |  |  |
| A07 | 替代解释、稳健性和有效性威胁 |  |  |
| A08 | 对当前项目的迁移 |  |  |
| A09 | 下一步深读位置 |  |  |

## Discussion Ledger

| Date | Agenda ID | User Question / Cognition | Agent Response Summary | Status Update | Follow-up |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Agenda Details

### A01 One-Sentence Core Finding

- Status: pending
- Linked proposition IDs:
- Based on automatic extraction:
- User questions:
- Current explanation:
- Current consensus:
- Open questions:
- Source anchors:
- Should promote to asset: no

### A02 Proof Structure / Argument Plan

- Status: pending
- Linked proposition IDs:
- Based on automatic extraction:
- User questions:
- Current explanation:
- Current consensus:
- Open questions:
- Source anchors:
- Should promote to asset: no

### A03 Operationalization And Proxy Bridge

- Status: pending
- Linked proposition IDs:
- Based on automatic extraction:
- User questions:
- Current explanation:
- Current consensus:
- Open questions:
- Source anchors:
- Should promote to asset: no

### A04 Measurement And Data Construction

- Status: pending
- Linked proposition IDs:
- Based on automatic extraction:
- User questions:
- Current explanation:
- Current consensus:
- Open questions:
- Source anchors:
- Should promote to asset: no

### A05 Research Design And Identification Strategy

- Status: pending
- Linked proposition IDs:
- Based on automatic extraction:
- User questions:
- Current explanation:
- Current consensus:
- Open questions:
- Source anchors:
- Should promote to asset: no

### A06 Data Analysis And Empirical Results

- Status: pending
- Linked proposition IDs:
- Based on automatic extraction:
- User questions:
- Current explanation:
- Current consensus:
- Open questions:
- Source anchors:
- Should promote to asset: no

### A07 Alternative Explanations, Robustness, And Validity Threats

- Status: pending
- Linked proposition IDs:
- Based on automatic extraction:
- User questions:
- Current explanation:
- Current consensus:
- Open questions:
- Source anchors:
- Should promote to asset: no

### A08 Transfer To Current Project

- Status: pending
- Linked proposition IDs:
- Based on automatic extraction:
- User questions:
- Current explanation:
- Current consensus:
- Open questions:
- Source anchors:
- Should promote to asset: no

### A09 Next Reading Targets

- Status: pending
- User questions:
- Current consensus:
- Open questions:

## Appendix: Out-Of-Agenda Questions

| ID | User Question / Cognition | Agent Response Summary | Promote To Agenda? | Notes |
|---|---|---|---|---|
| X01 |  |  |  |  |

## Extraction Revision Notes

| Date | Affected Section | Original Extraction | Discussion Revision | Needs Update In automatic-extraction.md? |
|---|---|---|---|---|
|  |  |  |  |  |

## Review Snapshot

- What we currently think this paper says:
- What we have discussed:
- What remains pending:
- What can already enter project assets:
- What should not be reused without source check:
