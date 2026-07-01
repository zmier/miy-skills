---
name: repair-knowledge-synthesis
description: 学术修箭头知识合成子 Skill。用于 academic-field-evidence-learning 第六步，针对 repair-arrow 请求，消费摘要扫描、全文图表、补充材料和同类顶刊证据包，生成 fulltext-pattern-ledger、case-repair-menu 和 handoff-to-repair-mapping。
---

# Repair Knowledge Synthesis

## 定位

本 Skill 回答：如果箭头断了，同领域高质量研究通常怎么补。它不重新判箭头，也不写最终审稿意见。

默认用于审稿时，本 Skill 采用：

```text
learning_orientation: arrow-oriented
```

这意味着：即使已经获取全文，也采用“全文定点深读”，不是把每篇文献做成完整文献综述。阅读必须从当前 `repair-arrow` 和 `target_arrow_id` 出发，只深读与该箭头相关的 Methods、Results、Figures、Tables、Captions、Supplement 和 Appendix。

只有用户明确要求“系统学领域”“100 篇文献”“成为临时领域专家”时，才采用：

```text
learning_orientation: field-immersion
```

field-immersion 可额外抽完整文献笔记、概念谱系、领域开放问题和 canonical paper notes；审稿默认不这样做。

## 输入

- `field-learning-request-ledger.md` 中的 `repair-arrow` 请求；
- `repair-search-strategy.md` 或 `field-search-strategy.md`；
- `abstract-scan-ledger.md`、`deep-read-shortlist.md`；
- 原文、图表、补充材料、方法文档或真实返修材料；
- `domain-map.md` 和 `evidence-standard-map.md`。

## 输出

```text
abstract-scan-ledger.md
deep-read-shortlist.md
fulltext-pattern-ledger.md
case-repair-menu.md
handoff-to-repair-mapping.md
```

## 合成原则

- 摘要只能产生 candidate repair route；
- 具体 evidence package 通常必须来自原文、图表、方法、补充材料或 appendix；
- `arrow-oriented` 模式下，所有 fulltext pattern 必须绑定当前 `target_arrow_id` 或 `request_id`，不得泛读后把无关知识塞进 menu；
- 读全文时优先抽取：claim type、weak evidence pattern、minimum_evidence、strong_evidence_package、typical experiment、metric fields、figure/table/supplement location、fallback_downgrade；
- 区分最低证据、强证据包和降调方案；
- 单篇来源默认 `case-only` 或 `candidate-general`；
- 多篇高质量来源或权威标准反复出现，才可建议 `stable-menu`。

## 定点深读字段

`fulltext-pattern-ledger.md` 至少包含：

```text
pattern_id
target_arrow_id
request_id
source_id
paper_title
verification_level: fulltext / figure / supplement / source-qc
claim_type
weak_evidence_pattern
minimum_evidence
strong_evidence_package
typical_experiments_or_analyses
metric_fields
figure_table_supplement_location
fallback_downgrade
transfer_status: case-only / candidate-general / stable-menu
notes
```

如果只读到摘要或 metadata，必须写：

```text
verification_level: abstract / metadata
status: needs-fulltext-pattern-check
```

不得把摘要中出现的实验名直接升级为领域稳定标准。

## Menu 反哺边界

补厚 menu 是定点阅读的副产物，不是本步骤的无限扩张目标。

可以进入 `case-repair-menu.md` / `repair-feedback-candidates.md` 的内容必须满足至少一条：

- 直接服务当前 `target_arrow_id`；
- 多篇高质量来源反复出现；
- 能把“抽象断箭头”转成具体证据包；
- 能修正或增强现有 repair menu 的常见失败模式。

不要纳入：

- 与当前稿件断箭头无关的材料制备细节；
- 只属于单篇文献背景介绍、但无法迁移的知识；
- 为了“成为专家”而泛化抽取的完整领域综述内容。

若任务切到 `field-immersion`，这些内容可进入单独的领域学习产物，而不是塞进 repair menu。

## 完成标准

- 每条 repair pattern 绑定 `target_arrow_id` 和来源；
- 写清 `minimum_evidence`、`strong_evidence_package`、`fallback_downgrade`；
- 无全文时标记 `needs-fulltext-pattern-check`；
- `arrow-oriented` 模式下，每条 pattern 都能回答“它增强哪根 A -> B 箭头”；
- `repair-feedback-candidates.md` 只收录可迁移的 evidence pattern，且标明 `transfer_status`；
- 输出可直接交给 `academic-arrow-repair-mapping`。
