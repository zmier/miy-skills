---
name: academic-field-evidence-learning
description: 学术论文领域地图与外部证据学习复合 Skill。用于 workflow-academic-argument-validity 的第 4 步，在内部验箭头之后、修箭头之前，集中处理领域不熟、needs-external-evidence、repair-knowledge-gap、文献 gap、方法标准、指标有效性、顶刊证据包学习等需求；编排需求合并、学习计划、检索与全文策略、领域地图、外部证据合成、修箭头知识合成和反哺移交。
---

# Academic Field Evidence Learning

## 定位

本 Skill 是学术论文论证 workflow 的集中外部学习层：

```text
第 3 步内部验箭头提出问题
-> 第 4 步集中学领域 / 查文献 / 读原文
-> 回填第 3 步判断，并供第 5 步修箭头使用
```

它解决的问题是：不要让“查文献”和“学文献”散落在验箭头与修箭头中各跑一套。

## 学习取向

审稿任务默认采用：

```text
learning_orientation: arrow-oriented
```

含义是：围绕当前稿件已经暴露的 `target_arrow_id`、`judge-arrow` 和 `repair-arrow` 需求做定点检索、跳读和抽读。即使拿到全文，也不是把整篇文献写成完整综述，而是优先深读与目标箭头有关的 Methods、Results、Figures、Tables、Captions、Supplement 和 Appendix，抽取同类高质量论文“如何证明这类箭头”的证据包。

用户明确要求“先熟悉领域”“100 篇文献研究”“成为临时领域专家”时，才切换为：

```text
learning_orientation: field-immersion
```

field-immersion 不只服务当前断箭头，还要系统建立领域问题谱系、方法谱系、指标体系、SOTA、开放争议、关键文献和证据标准。它更耗时、耗 token，通常对应 `deep` 或 `100-paper`。

重要区分：

```text
全文获取 != 全文全量学习
```

- `arrow-oriented`：全文定点深读，服务当前稿件审稿；
- `field-immersion`：全文系统学习，服务领域专家化。

menu 积累遵循“审稿主任务优先，反哺副产物”原则：

```text
当前断箭头 -> 定点读同类文献 -> 抽 evidence package -> 生成 case-repair-menu / repair-feedback-candidates
```

不要为了补厚 menu 而无限扩张成完整文献综述；只有与当前 `target_arrow_id` 或反复出现的高价值证据包相关的内容，才进入反哺候选。随着 case 积累，menu 会自然变厚，形成领域专家感。

## 输入

- `external-evidence-request.md`；
- `repair-knowledge-gap.md`；
- `academic-arrow-audit-table.md` 或 `internal-arrow-audit-table.md`；
- `empirical-review-sensitivity-map.md`、`empirical-method-qc-request.md`、`handoff-to-field-learning.md`（经管/社科实证 adaptor 产物，如有）；
- `chinese-literature-gap-request.md`、`local-expression-and-format-qc.md`（中文经管 adaptor 产物，如有）；
- `cnki-request-ledger.md`（已有中文深库请求台账时）；
- `academic-arrow-break-summary.md`；
- 作者参考文献、关键词、摘要、引言、核心图表；
- 领域熟悉度：`unfamiliar / partial / familiar`；
- 时间预算：`quick / standard / deep / 100-paper`；
- 来源约束：领域顶刊、综合顶刊及其子刊、FT50/UTD24、中文川大 B+ 等。

## 输出

```text
domain-map.md
field-topic-ledger.md
seed-literature-ledger.md
key-journal-map.md
method-and-metric-map.md
sota-benchmark-map.md
evidence-standard-map.md
review-risk-radar.md
external-reading-log.md
fulltext-acquisition-ledger.md
fulltext-source-inventory.md
handoff-to-fulltext-restoration.md
human-download-request.md
cnki-request-ledger.md
external-evidence-ledger.md
repair-search-strategy.md
abstract-scan-ledger.md
deep-read-shortlist.md
fulltext-pattern-ledger.md
case-repair-menu.md
repair-feedback-candidates.md
field-learning-qc.md
handoff-to-arrow-audit.md
handoff-to-repair-mapping.md
```

## 主流程

1. 合并学习需求：
   - 调用 `skills/field-learning-request-merge/SKILL.md`；
   - 合并 `external-evidence-request.md` 与 `repair-knowledge-gap.md`；
   - 若存在经管/社科实证 adaptor 或中文经管 adaptor 输出，同时合并 `empirical-method-qc-request.md`、`chinese-literature-gap-request.md` 和 adaptor 的 `handoff-to-field-learning.md`；
   - 若任务属于中文经管/中文社科，或任何请求标记为 `CNKI-needed` / `Chinese-literature-needed`，必须创建或更新 `cnki-request-ledger.md`；
   - 区分两类问题：`judge-arrow`（判箭头是否成立）和 `repair-arrow`（学习怎么补箭头）；
   - 相同主题、方法、指标或文献流的请求合并检索，避免重复查。
2. 选择学习强度：
   - 调用 `skills/field-learning-plan-design/SKILL.md`；
   - `quick`：优先作者参考文献、综述、10-20 篇摘要；
   - `standard`：30-50 篇标题/摘要 + 5-10 篇核心原文；
   - `deep`：系统扩展同类研究和 benchmark；
   - `100-paper`：用户明确要求领域浸泡式学习时使用。
   - 同时声明 `learning_orientation`：审稿默认 `arrow-oriented`；用户明确要求领域浸泡时才用 `field-immersion`。
3. 设计检索策略：
   - 调用 `skills/field-search-fulltext-strategy/SKILL.md`；
   - 文献检索默认调用 `$scholar-kit-literature-search`；
   - 期刊质量门槛必须写入 `journal_quality_policy` 与 `journal_quality_sources`；
   - 中文经管/中文社科请求必须显式设计 CNKI query block，并写入 `cnki-request-ledger.md`；
   - CNKI query block 必须区分精确词、扩展词、相邻构念、方法/指标词和本土制度词；只跑一个精确词不能支撑“中文文献没有相关研究”的判断；
   - 政策、官方数据、标准、package docs 作为 `non_literature_routes` 分开记录；
   - 对必须深读的候选文献，调用 `skills/paper-fulltext-acquisition/SKILL.md` 获取合法 PDF、HTML、图表或补充材料；
   - 获取到的全文再移交 PDF/HTML/DOCX 还原流程。
4. 建领域地图：
   - 调用 `skills/domain-map-building/SKILL.md`；
   - 生成 `domain-map.md`、`field-topic-ledger.md`、`key-journal-map.md`；
   - 目标是建立足够审稿的领域认知，不写正式文献综述。
5. 处理判箭头证据：
   - 调用 `skills/external-evidence-synthesis/SKILL.md`；
   - 对 `judge-arrow` 请求生成 `external-evidence-ledger.md`；
   - 说明外部证据是否改变对应 `arrow_id` 的 status；
   - 不把未检索或检索失败写成“没有证据”。
6. 处理修箭头知识：
   - 调用 `skills/repair-knowledge-synthesis/SKILL.md`；
   - 对 `repair-arrow` 请求调用或沿用 `academic-repair-knowledge-learning` 的产物协议；
   - 生成 `repair-search-strategy.md`、`abstract-scan-ledger.md`、`fulltext-pattern-ledger.md` 和 `case-repair-menu.md`；
   - 如果需要全文而暂时只有摘要，标记 `needs-fulltext-acquisition` 或 `needs-fulltext-pattern-check`。
   - `arrow-oriented` 模式下，全文深读必须绑定 `target_arrow_id`，只抽与当前断箭头相关的证据包、指标、图表字段、实验组合和降调方式；
   - `field-immersion` 模式下，才额外抽完整领域地图、概念谱系、canonical paper notes 和开放问题。
7. 生成风险雷达与移交：
   - 调用 `skills/field-learning-handoff-feedback/SKILL.md`；
   - `review-risk-radar.md` 给后续验箭头/修箭头提示高风险 claim；
   - `handoff-to-arrow-audit.md` 指明哪些 `arrow_id` 可回填；
   - `handoff-to-repair-mapping.md` 指明哪些断点已有补救菜单、哪些仍 unknown。
8. 反哺候选：
   - 仍由 `skills/field-learning-handoff-feedback/SKILL.md` 承载；
   - 可迁移知识写入 `repair-feedback-candidates.md`；
   - 不直接改稳定 reference menu；
   - 需要人工确认、UAT 或回归测试后再沉淀。

## 子 Skill 路由

| 子 Skill | 承载步骤 | 输入 | 输出 |
|---|---|---|---|
| `field-learning-request-merge` | 1. 合并学习需求 | `external-evidence-request.md`, `repair-knowledge-gap.md`, internal audit | `field-learning-request-ledger.md` |
| `field-learning-plan-design` | 2. 选择学习强度 | request ledger、领域熟悉度、时间预算 | `field-learning-plan.md` |
| `field-search-fulltext-strategy` | 3. 检索与全文策略 | learning plan、来源约束 | `field-search-strategy.md`, `fulltext-acquisition-plan.md`, `external-reading-log.md` |
| `paper-fulltext-acquisition` | 3B. 合法全文获取与人工下载通知 | `fulltext-acquisition-plan.md`, DOI/title/URL/OpenAlex id、用户已提供文件 | `fulltext-acquisition-ledger.md`, `fulltext-source-inventory.md`, `handoff-to-fulltext-restoration.md`, `human-download-request.md` |
| `domain-map-building` | 4. 建领域地图 | 检索结果、摘要、seed 文献、参考文献 | `domain-map.md`, `field-topic-ledger.md`, `key-journal-map.md`, `review-risk-radar.md` |
| `external-evidence-synthesis` | 5. 判箭头证据 | judge-arrow requests、检索/阅读结果 | `external-evidence-ledger.md`, `handoff-to-arrow-audit.md` |
| `repair-knowledge-synthesis` | 6. 修箭头知识 | repair-arrow requests、摘要/原文 pattern | `case-repair-menu.md`, `fulltext-pattern-ledger.md`, `handoff-to-repair-mapping.md` |
| `field-learning-handoff-feedback` | 7-8. 移交与反哺 | 上述全部 ledger | `review-risk-radar.md`, `repair-feedback-candidates.md`, `field-learning-qc.md` |

## 执行模式与交付清单

每次调用必须声明 mode。默认：

```text
mode: standard
```

同时必须在 `field-learning-plan.md` 声明：

```text
learning_orientation: arrow-oriented / field-immersion
```

默认审稿、投稿前自审、返修准备均为 `arrow-oriented`。只有用户明确提出“系统学领域”“100 篇文献”“成为领域专家”等目标时，才使用 `field-immersion`。

`standard` / `standard-field-learning-uat` 必交付：

```text
field-learning-request-ledger.md
field-learning-plan.md
field-search-strategy.md
fulltext-acquisition-plan.md
fulltext-acquisition-ledger.md
cnki-request-ledger.md                 # 中文经管/中文社科或 CNKI-needed 请求时必交；不适用时写 not-applicable 占位
domain-map.md
field-topic-ledger.md
key-journal-map.md
method-and-metric-map.md
sota-benchmark-map.md
evidence-standard-map.md
review-risk-radar.md
external-evidence-ledger.md
handoff-to-arrow-audit.md
case-repair-menu.md
handoff-to-repair-mapping.md
field-learning-qc.md
```

条件性交付：

```text
human-download-request.md            # 需要人工下载全文/补充材料时
fulltext-source-inventory.md         # 已获取本地全文材料时
handoff-to-fulltext-restoration.md   # 已获取 PDF/HTML/DOCX 且需要还原时
abstract-scan-ledger.md              # 本轮实际做摘要扫描时
deep-read-shortlist.md               # 本轮筛出必须深读来源时
fulltext-pattern-ledger.md           # 本轮实际读全文/图表/补充材料时
repair-feedback-candidates.md        # 有可迁移规则候选时
```

如某个条件性产物不适用，应创建占位文件并写明：

```text
status: not-applicable / pending / blocked
reason:
```

所有 map / ledger / handoff 类产物都应包含或显式说明 `verification_level`：

```text
metadata / abstract / fulltext / figure / supplement / source-qc / manual-needed
```

## 检索与来源纪律

- 文献检索默认走 `$scholar-kit-literature-search`；
- 领域顶刊、综合顶刊及其子刊、权威综述、方法原文、官方标准优先；
- Q1/SJR-Q1 只能作为辅助质量证据，不能单独替代领域顶刊判断；
- 中文文献按用户约定最低川大 B 以上；
- 需要 PDF/HTML/full text 时，优先合法 OA、出版商开放页面、arXiv/PMC/Unpaywall/OpenAlex OA 等路线；无法合法获取时标记 `requires-human-access`，不绕 paywall；
- 实际全文获取由 `paper-fulltext-acquisition` 承载；拿不到全文时不能假装完成原文深读；
- 当需要用户手动下载 PDF/HTML/Supplement 时，`paper-fulltext-acquisition` 必须生成 `human-download-request.md`，并调用 `$feishu-notify` 通知用户；
- 所有失败、验证码、权限、技术故障都写入 `field-learning-qc.md`。

## CNKI 中文深库闭环纪律

中文经管、中文社科或任何 `CNKI-needed` 请求，必须使用 `assets/cnki-request-ledger-template.md` 创建：

```text
cnki-request-ledger.md
```

每条 CNKI 请求必须绑定：

```text
target_arrow_id
source_request_id
local_sensitivity_type
query_intent
query_terms
required_scope
required_quality_floor
execution_status
verification_level
fulltext_status
effect_on_arrow_status
what_can_be_concluded
what_cannot_be_concluded
next_action
```

执行状态必须保守：

- `completed-true-zero` 只代表当前 query 的真零，不代表中文文献谱系真空；
- `metadata-only` / `abstract-only` 只能支持弱判断或生成全文核验请求；
- `technical-failure`、`login-or-captcha-blocked`、`manual-verification-needed` 不能回填为 `no-evidence`；
- 如果 CNKI 路线失败，`field-learning-qc.md` 必须记录失败原因、未完成 query block、可得结论和不可得结论；
- 若中文文献 gap、中文指标有效性或本土制度语境会影响 `X1/X2/Y`，但 CNKI 未闭环，选点层只能写 `evidence-needed` 或 `search-before-major`，不能写 confirmed major。

## Source Selector

OpenAlex / WoS / CNKI / BibTeX 检索结果进入领域地图或 handoff 前，必须先做 source selector，避免把噪声、弱相关、future-dated 或相邻领域结果直接当证据。

推荐输出到 `seed-literature-ledger.md`：

```text
source_id
title
year
journal_or_venue
doi_or_url
linked_request_ids
include_or_exclude
include_reason
journal_quality_evidence
verification_level
needs_fulltext
notes
```

只有 `include_or_exclude=include` 的来源才能进入 `domain-map.md`、`external-evidence-ledger.md` 或 `case-repair-menu.md`；被排除来源可保留为背景，但不能支撑箭头判断。

## 完成标准

- 每个学习任务绑定 `request_id` 或 `target_arrow_id`；
- 对 adaptor 产生的学习请求，必须保留 `adapter_source`、`sensitivity_type` 和 `parent_claim`，避免学习结果无法回填到箭头；
- 每次学习声明 `learning_orientation`，并按该取向决定是全文定点深读还是全文系统学习；
- 判箭头证据和修箭头知识分开记录，但共享检索与阅读产物；
- 领域地图能说明核心话题、方法、指标、期刊和常见证据包；
- `external-evidence-ledger.md` 可回填验箭头；
- 中文经管/中文社科或 CNKI-needed 请求已生成 `cnki-request-ledger.md`，且未完成 CNKI 的请求不会被写成已验证外部证据；
- `case-repair-menu.md` 可供修箭头使用；
- `repair-feedback-candidates.md` 只收录与当前断箭头相关、且可能迁移的 evidence pattern；不把无关文献知识为了“补厚 menu”强行纳入；
- 没有全文时不假装完成 fulltext pattern extraction。
