---
name: academic-repair-knowledge-learning
description: 学术修箭头知识学习复合 Skill。用于 academic-arrow-repair-mapping 发现某类断箭头没有可靠 repair menu、用户要求不要用既有小抄、遇到新领域/新方法/新实验技术/新统计检验，或需要通过检索摘要、综述、顶刊原文、方法指南、官方文档、图表和补充材料来学习“别人如何证明这类学术箭头”时；编排检索策略设计、摘要扫描、原文证据包抽取和本案 repair menu 合成。
---

# Academic Repair Knowledge Learning

## 定位

本 Skill 是 `academic-arrow-repair-mapping` 的子复合 Skill。它不直接写审稿意见，也不重新验箭头，而是在修箭头阶段回答：

```text
我不知道这类断箭头该补什么实验 / 分析 / 文献 / 方法证据；
应该去哪里查？
摘要够不够？
哪些必须看原文、图表或补充材料？
如何把学到的证据标准变成本案 repair map 或候选 menu？
```

它解决的是“领域 repair menu 不能硬背”的问题：

```text
unknown / weak repair knowledge
-> repair-search-strategy
-> abstract scan
-> fulltext / figure / supplement pattern extraction
-> case-repair-menu
-> handoff to academic-arrow-repair-mapping
```

## 与验箭头检索的边界

`academic-argument-arrow-audit` 中的外部证据检索，目标是判断作者箭头是否成立：

```text
作者说 A 能推出 B；
外部资料帮助判断这个箭头 strong / weak / broken / unclear。
```

本 Skill 中的检索，目标是学习断箭头应该如何修：

```text
已知 A 到 B 这条箭头有断点；
外部资料帮助学习同领域通常补什么实验、比较、模型、数据、引用或降调表述。
```

如果任务还没完成箭头审计，先回到 `academic-argument-arrow-audit`；如果已经有 `target_arrow_id` 和断点说明，再进入本 Skill。

## 输入

- `repair-knowledge-gap.md`；
- `academic-arrow-audit-table.md` 中的目标 `arrow_id`；
- `academic-arrow-break-summary.md`；
- `external-evidence-request.md` / `external-evidence-ledger.md`；
- 论文领域、目标期刊/学科、关键词；
- 已有同类文献、综述、方法论文、官方文档或补充材料。

## 输出

```text
repair-search-strategy.md
repair-knowledge-learning-plan.md
abstract-scan-ledger.md
fulltext-pattern-ledger.md
case-repair-menu.md
repair-feedback-candidates.md
repair-learning-qc.md
```

其中 `case-repair-menu.md` 交回 `academic-arrow-repair-mapping` 使用。

## 主流程

1. 固定学习对象：
   - 读取 `target_arrow_id`；
   - 写明 `from_node A -> to_node B`；
   - 写明当前断点和为什么既有 menu 不足；
   - 不新增未审计断点。
2. 设计检索策略：
   - 调用 `skills/repair-search-strategy-design/SKILL.md`；
   - 输出 `repair-search-strategy.md`；
   - 明确查什么、去哪里查、如何筛、摘要扫描目标、何时必须深读原文。
3. 摘要扫描：
   - 调用 `skills/repair-abstract-scan/SKILL.md`；
   - 用摘要识别同类 claim、常用 metric、常用 method、同类 comparator；
   - 输出 `abstract-scan-ledger.md`；
   - 摘要扫描只能产生 `candidate repair route`，不能直接写成强证据标准。
4. 深读原文 / 图表 / 补充材料：
   - 调用 `skills/repair-fulltext-pattern-extraction/SKILL.md`；
   - 对需要具体 evidence package 的箭头，读取原文相关章节；
   - 优先看 Methods、Results、Figure captions、Supplementary Information、Appendix、Robustness checks、Control experiments、Benchmark tables；
   - 输出 `fulltext-pattern-ledger.md`。
5. 抽取 repair pattern：
   - 记录别人如何证明同类箭头；
   - 区分最低证据、强证据包和降调方案；
   - 标注来源数量与质量。
6. 生成 `case-repair-menu.md`：
   - 调用 `skills/repair-case-menu-synthesis/SKILL.md`；
   - 每条规则都标 `transfer_status`；
   - 单篇来源默认 `case-only` 或 `candidate-general`；
   - 多篇高质量来源或权威标准反复出现，才可标 `stable-menu`。
7. 生成反哺候选：
   - 不直接改写稳定 menu；
   - 把可迁移规则写入 `repair-feedback-candidates.md`；
   - 标明证据来源、适用边界、反例风险、需要回归测试的案例；
   - 只有经过人工确认或后续 UAT / 回归测试，才能沉淀进稳定 reference menu。
8. 回填修箭头：
   - 把 `case-repair-menu.md` 交给 `academic-arrow-repair-mapping`；
   - 在 `repair-learning-qc.md` 说明哪些问题仍需人工或 source QC。

## 摘要与原文分界

读取 `references/abstract-vs-fulltext.md`。核心原则：

```text
摘要像菜单名；
原文、图表和补充材料才是菜谱。
```

摘要通常够用：

```text
领域是否活跃；
同类 claim 是否存在；
常用 metric / material / method 名称；
潜在 comparator。
```

通常必须看原文：

```text
具体控制实验；
图表指标组合；
benchmark table 字段；
稳健性组合；
实验条件、时间、浓度、负载、样本规则；
方法假设和验收标准。
```

## 检索路由

文献检索默认调用：

```text
$scholar-kit-literature-search
```

它是 OpenAlex、Web of Science（WoS）和 CNKI 的 umbrella Skill。除非用户明确指定某个数据库或已有上游任务产物已经锁定子 Skill，否则不要绕过它直接调用 WoS / CNKI / OpenAlex 子 Skill。

调用原则：

- 未指定数据库的英文国际文献：先走 `$scholar-kit-literature-search`，由其按 routing policy 默认从 OpenAlex 开始；
- 明确需要 WoS 可追溯记录、FT50/UTD24/顶刊白名单：通过 `$scholar-kit-literature-search` 路由到 WoS；
- 中文文献、中文期刊、中国本土学术证据：通过 `$scholar-kit-literature-search` 路由到 CNKI；
- 同时需要中英文证据：通过 `$scholar-kit-literature-search` 形成 OpenAlex/WoS 与 CNKI 的互补路线；
- 政策文件、官方数据、标准文档、package docs 等非论文资料，可在 `repair-search-strategy.md` 另设 `official-doc / web / package-doc` 路线，但要和文献检索路线分开记录。

检索策略必须包含期刊质量门槛：

```text
journal_quality_policy:
journal_quality_sources:
```

默认只把以下来源用于形成强 repair pattern：

- 领域顶刊、综合顶刊及其子刊；
- 权威综述、方法原文、官方标准/文档；
- 管理/经济/商科中的 FT50、UTD24、ABS/AJG、领域公认顶刊；
- 中文文献至少满足用户约定的川大 B 以上。

Q1 / SJR-Q1 可作为辅助质量证据，但不能单独替代领域顶刊判断。候选期刊名单应在执行时动态获取：从目标稿件参考文献、同类综述、高相关检索结果、WoS/JCR category、SJR/SCImago、学会或出版社旗舰列表中核验，并记录 `quality_source`。无法核验时标记 `needs-journal-quality-qc`。

若调用检索工具，必须记录：

```text
search_route
search_skill
query
database_or_source
journal_quality_policy
journal_quality_sources
inclusion_criteria
screened_count
selected_sources
why_selected
what_remains_unchecked
```

如果检索失败、权限不足、验证码、数据库不可用或只完成摘要扫描，必须在 `repair-learning-qc.md` 写清：

```text
search_status:
missing_route:
what_can_be_concluded:
what_cannot_be_concluded:
```

如果只是设计检索策略、尚未执行检索，必须明确写：

```text
search_execution_status: planned-not-executed
next_skill_to_call: scholar-kit-literature-search
```

## 子 Skill 路由

| 子 Skill | 触发条件 | 输入 | 输出 |
|---|---|---|---|
| `repair-search-strategy-design` | 已有断点但不知道如何查资料学习修法 | `repair-knowledge-gap.md`, `target_arrow_id`, 领域关键词 | `repair-search-strategy.md` |
| `repair-abstract-scan` | 已有检索策略，需要快速判断哪些来源值得深读 | `repair-search-strategy.md`, 检索结果摘要 | `abstract-scan-ledger.md`, `deep-read-shortlist.md` |
| `repair-fulltext-pattern-extraction` | 摘要不足以知道别人具体怎么证明 | `deep-read-shortlist.md`, 原文/图表/补充材料 | `fulltext-pattern-ledger.md` |
| `repair-case-menu-synthesis` | 已有摘要和原文 pattern，需要转成本案可用修法，并识别可迁移反哺候选 | `abstract-scan-ledger.md`, `fulltext-pattern-ledger.md`, 断点说明 | `case-repair-menu.md`, `repair-feedback-candidates.md`, `repair-learning-qc.md` |

## 产物字段

模板见：

```text
assets/repair-knowledge-learning-templates.md
```

核心字段：

```text
target_arrow_id
unknown_repair_question
search_route
abstract_findings
fulltext_pattern
minimum_evidence
strong_evidence_package
fallback_downgrade
source_basis
transfer_status
handoff_to_repair_map
feedback_candidate
```

## 完成标准

- 每条学习任务绑定 `target_arrow_id`；
- 不用检索结果新增未经审计的新问题；
- 摘要扫描和原文深读分开记录；
- 不把摘要中出现的方法词直接当作强 repair 标准；
- `case-repair-menu.md` 中每条规则都有来源和迁移状态；
- 对无法确认的证据标准标记 `unknown` 或 `needs-fulltext-pattern-check`；
- 输出能被 `academic-arrow-repair-mapping` 直接消费。
