---
date: 2026-06-20
type: reference
status: structural-green
scope:
  - academic-argument-arrow-audit
---

# Academic Arrow Audit Main Axis

## 定位

本文件定义学术论文“验箭头”复合 Skill 的主轴。它回答：

```text
抽树之后，如何逐条检查作者的 A -> B 是否成立？
哪些步骤由父 Skill 承载？
哪些步骤路由到子 Skill 或外部检索？
每一步输入和输出是什么？
```

本流程只做诊断，不做修复映射、选点和最终行文。

## 执行模式

本主轴有两种模式。调用方必须在 TASK 说明或 log 中写明模式。

| 模式 | 用途 | 第 5 步 | 第 6 步 | 禁止事项 |
|---|---|---|---|---|
| `internal-blind-audit` | 盲跑、回归测试、初审、用户要求先不查 | 只生成 `external-evidence-request.md` | 生成 `external-evidence-ledger.md`，全部标 `not-searched / pending`；保留 `needs-external-evidence` | 不联网、不检索、不伪造来源、不把 pending 写成 confirmed |
| `full-evidence-audit` | 正式诊断、需要判断 gap/方法/指标有效性、用户要求完整验箭头 | 集中调用文献检索、方法来源、政策/监管文件、官方数据、官方文档、citation verification 或联网核验 | 将外部证据回填到 `academic-arrow-audit-table.md`，更新为 `weak-confirmed / broken-confirmed / strong-after-search / still-unclear` 等 | 不边验边散查、不脱离 `request_id` 和 `target_arrow` 检索 |

若未指定，默认：

```text
mode: internal-blind-audit
```

只有当用户明确要求查文献、完整验箭头、回填外部证据、判断 gap 是否真实或判断方法标准时，才使用：

```text
mode: full-evidence-audit
```

## 八步主轴

| 步骤 | 目标 | 输入 | 输出 | 承载 |
|---|---|---|---|---|
| 1. 接收作者论证树 | 固定验收对象，确认材料是否够审计 | `canonical-node-ledger.md`、`canonical-edge-ledger.md`、`evidence-ledger.md`、`extraction-qc.md` | `audit-input-status.md` | 父 Skill |
| 2. 逐条改写作者箭头 | 把每条边改成大白话 | edge ledger | `plain-language-arrow-list.md` | 父 Skill |
| 3. 判断箭头类型 | 给每条箭头贴学术类型标签 | arrow list、evidence type、claim type | `typed-arrow-ledger.md` | 父 Skill + `academic-arrow-types.md` |
| 4. 第一轮内部验箭头与外部证据打标 | 先用稿件内部证据审计，并集中标出需要外部依据的箭头 | typed arrow ledger、稿件 evidence | `internal-arrow-audit-table.md`、`external-evidence-request.md` | 父 Skill + 子 Skill |
| 5. 集中外部证据增强 | `internal-blind-audit` 只列请求；`full-evidence-audit` 集中查文献、方法、政策/监管文件、官方数据、官方文档或 citation | external evidence request | `external-evidence-ledger.md`、method/literature/policy/data notes 或 not-searched ledger | 子 Skill / 检索 Skill / web |
| 6. 回填审计 ledger | 把外部证据或 pending 状态回填到对应 arrow_id | internal audit、external evidence ledger | `academic-arrow-audit-table.md` | 父 Skill |
| 7. 生成 summary 和 candidates | 汇总 strong/weak/broken/unclear/needs-qc | audit table | `academic-arrow-break-summary.md`、`issue-selection-candidates.md` | 父 Skill |
| 8. 移交修复映射 / 选点 | 把全量诊断交给 repair mapping；快速或考试式任务可直接交给 issue selection 并标记缺少 repair map | candidates、audit table | handoff note | 父 Skill |

## 步骤 0：审稿显影图

在第 1 步正式逐条验箭头前，可以先基于作者树和 evidence ledger 生成：

```text
review-sensitivity-map.md
```

它不是作者树，也不是最终审稿意见。它只用于显影后续最值得并读的证据组合，例如：

```text
同一概念跨章节是否滑动；
同一机制在理论、表格、异质性和排除检验中是否一致；
图形样本和回归样本是否一致；
表格报告和正文解释是否冲突；
稳健性是否真的对应核心威胁。
```

该文件属于验箭头阶段的默认准备物，可以作为第 4 步路由和第 5 步逐条审计的输入。若材料不足以生成，必须在 `audit-input-status.md` 写明跳过原因。

显影时要专门防止“工序很完整但判断变钝”。除表文冲突、显著性和方法 QC 外，还要显影下列高敏感前提：

```text
treatment-definition:
  操作性定义是否真的推出作者声称的 X？
  例如“未见同年问询/处罚”是否足以推出“主动披露”？

sample-mechanism-fit:
  样本筛选是否剔除了最能检验机制的对象、事件或基准？
  例如剔除事件公司后，是否仍能判断同行效应相对事件公司的变化？

construct-level-fit:
  经典构念的原始层级和本文操作化层级是否一致？
  例如行业长期外部融资依赖是否能改成公司年度指标？

timing-fit:
  事件发生、信息可见、行为反应和结果测量是否在同一时间链条中？

baseline-fit:
  作者是否缺少判断学习、竞争、溢出或排除机制所需的基准组？
```

## 步骤说明

### 1. 接收作者论证树

只接收抽树阶段的作者 claim、evidence、edge，不把审稿攻击补进作者树。

学术作者树可能同时有两类边：

```text
claim-to-claim arrows:
  claim / subclaim / mechanism / contribution 之间的支撑关系；

evidence-to-claim arrows:
  表格、图、数字、引用、样本规则等底层 evidence 指向某个 claim。
```

默认全量审计 `claim-to-claim arrows`。`evidence-to-claim arrows` 默认作为 `evidence_ids` 绑定到上层箭头；只有当 evidence 本身有争议、直接影响 X1/X2/Y、或存在表文冲突/引用错配/图表 QC 红灯时，才单独展开审计。这样避免 evidence edge 爆炸，也避免遗漏关键底层证据。

若输入缺少 canonical edge ledger 或 evidence ledger，标记：

```text
incomplete-tree-input
```

若表格、图、文献锚点尚未核验，保留：

```text
status: needs-qc 或 strong-with-qc
qc_flags: table-cell-qc / figure-qc / citation-qc
```

不要在验箭头阶段重新抽树；必要时退回 `academic-paper-argument-tree-extraction`。

### 2. 逐条改写作者箭头

每条箭头必须改写成：

```text
作者想用 A 证明 B。
```

示例：

```text
作者想用 Table 3 中 DID 系数显著为负，证明处罚改善了信息披露质量。
```

这一步不评价对错，只让后续审查对象变清楚。

### 3. 判断箭头类型

arrow_type 是标签，不是 checklist 顺序。

常见类型：

```text
gap-contribution
construct-measure
treatment-definition
sample-mechanism-fit
identification-causal
result-finding
mechanism-claim
robustness-threat
finding-contribution
```

一条箭头可以有主类型和副类型：

```text
primary_arrow_type: identification-causal
secondary_arrow_type: result-finding
```

### 4. 第一轮内部验箭头与外部证据打标

父 Skill 判断：

```text
这条箭头能否用通用 arrow-audit-core 直接审？
是否需要专门 reference？
是否需要子 Skill？
是否需要外部检索或人工 QC？
```

第一轮先只使用稿件内部 evidence、抽树产物、表格抽取和已存在的 reference。目标是把所有箭头扫完，区分：

```text
内部证据足以初判；
内部证据足以发现弱点但仍需 QC；
离不开外部文献/方法/官方材料；
必须人工表格/图/引用复核。
```

外部证据需求统一写入：

```text
external-evidence-request.md
```

第一轮内部审计不能只做“证据是否显著”的窄判断。对每条高风险箭头至少追问：

```text
作者的 A 最直接证明的是什么？
作者的 B 比 A 多上升了哪一步？
这一步依赖哪个隐含前提？
该前提是内部可判、需要 QC，还是必须外部证据？
如果该前提不成立，X1/X2/Y 哪一层被削弱？
```

特别注意下列容易被轻放的箭头：

| 箭头类型 | 内部审计追问 |
|---|---|
| treatment-definition | 操作性排除规则是否真的推出作者声称的处理含义？是否混入策略性选择、监管预期或滞后？ |
| sample-mechanism-fit | 样本清洁是否以牺牲机制相关场景为代价？是否缺少事件公司、自身变化或多事件基准？ |
| construct-measure / construct-level-fit | 指标是否只测到代理、局部或不同层级构念？经典构念是否从行业/宏观层级滑到公司/微观层级？ |
| timing-fit | 处理窗口、反应窗口和结果测量窗口是否一致？ |
| mechanism-claim | 机制表、理论叙述、排除机制和异质性是否指向同一机制，而不是各说各话？ |
| robustness-threat | 每个稳健性检验回应的是哪个具体威胁？是否只是重复同一模型框架？ |
| finding-contribution | 局部、短期、代理指标发现是否被上升成理论/政策/发表价值？ |

路由原则：

- 文献 gap 且需要外部证据：调 `academic-literature-gap-arrow-audit`，必要时编排 `scholar-kit-literature-search`；
- 因果识别：调 `academic-causal-arrow-audit`，可使用 DAG、后门/前门、设计假设审查；
- 统计结果：调 `academic-statistical-result-arrow-audit`，检查显著性、量纲、经济意义、报告透明度；
- 概念/变量、样本适配、机制、稳健性、贡献上升：先由父 Skill 按 reference 审，复杂后再升级子 Skill。

### 5. 集中外部证据增强

只处理第 4 步标记的请求，不做无边界扩展检索。先看执行模式：

```text
internal-blind-audit:
  不检索；
  只把请求写入 external-evidence-request.md；
  external-evidence-ledger.md 使用 not-searched / pending 格式；
  不改变 needs-external-evidence 的定性。

full-evidence-audit:
  集中检索；
  优先按证据类型调用 scholar-kit / method source / official source / official data route；
  生成真实 external-evidence-ledger.md；
  回到 target_arrow 判断 A 是否足以推出 B。
```

典型请求类型：

```text
literature-gap-search
measure-validity-search
method-standard-search
citation-verification
official-documentation-check
policy-document-check
official-data-check
regulatory-filing-check
recent-top-journal-check
```

路线纪律：

| search_type | route |
|---|---|
| literature-gap-search | 优先 `scholar-kit-literature-search`；英文 OpenAlex/WoS，中文 CNKI；web 只作补充 |
| citation-verification | scholar-kit / DOI / journal page / publisher metadata / cited paper source |
| method-standard-search | 原始方法论文、顶刊应用、官方 package/docs、handbook |
| policy-document-check | 官方监管机构、法律法规、交易所或政府部门原文 |
| official-data-check | 官方统计、监管数据库、交易所/政府/机构数据说明 |
| regulatory-filing-check | 官方监管公告、处罚决定、交易所/监管披露原文 |
| table / figure / formula / numeric conflict | 不属于外部检索；退回 PDF/DOCX restoration source QC，用大模型视觉能力或人工核验原稿 |

如果没有完成必需路线，必须在 ledger 中说明 `missing_required_route` 和 `why_route_not_completed`，不能把未检索当作无证据。

检索和学习结果写入：

```text
external-evidence-ledger.md
```

如果本轮明确不检索，也必须生成 not-searched ledger，格式为：

```text
request_id:
target_arrow:
search_status: not-searched
reason_not_searched:
current_audit_status: needs-external-evidence / needs-qc
what_would_change_after_search:
```

not-searched ledger 只能说明“还需要什么证据”，不能填入虚构来源，也不能把 pending 判断写成已确认。

每条外部证据必须绑定：

```text
request_id
target_arrow
source_type
source_quality
what_it_changes
```

不得把搜索失败、登录失败、验证码或数据库故障当作“没有文献”。

### 6. 回填审计 ledger

把外部证据回填到对应 `arrow_id`：

```text
needs-external-evidence -> weak-confirmed / broken-confirmed / strong-after-search / still-unclear
needs-method-source -> weak-confirmed / method-qc-pending / still-unclear
citation-qc -> citation-verified / citation-mismatch / still-unclear
```

若用户选择暂不检索，保留 `needs-external-evidence`，不能把该箭头写成定论。

### 7. 生成审计 ledger

核心问题：

```text
A 真的足以推出 B 吗？
```

必须写出：

```text
hidden_premise:
why_it_breaks:
impact_on_X1_X2_Y:
fix_or_downgrade:
```

逻辑谬误先用父层 `arrow-audit-core.md` 识别，再由 `academic-fallacy-adapter.md` 翻译成学术表达。

输出全量审计，不筛选：

```text
strong
strong-with-qc
weak
broken
unclear
needs-qc
needs-external-evidence
```

`weak/broken/unclear/needs-qc/needs-external-evidence` 才进入 `issue-selection-candidates.md`。

### 8. 移交修复映射 / 选点

验箭头阶段只交付：

```text
哪些箭头弱/断/不清楚；
它们影响 X1、X2 还是 Y；
需要什么补证、降调或人工核验。
```

正式学术审稿和写作自审中，下一步优先交给：

```text
../../../argument-arrow-repair-mapping/skills/academic-arrow-repair-mapping/SKILL.md
```

生成：

```text
arrow-repair-map.md
```

再交给 `argument-issue-selection` 判断是否写成 major concern、minor concern 或 revision action。

若用户只要求快速选点、考试式输出或临时讨论，可以直接交给 `argument-issue-selection`，但必须在选点输出中标记：

```text
missing-repair-map
```
