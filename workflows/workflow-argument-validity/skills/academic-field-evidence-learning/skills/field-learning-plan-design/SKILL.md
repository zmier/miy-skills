---
name: field-learning-plan-design
description: 学术领域学习计划设计子 Skill。用于 academic-field-evidence-learning 第二步，根据 field-learning-request-ledger、领域熟悉度、时间预算和来源约束选择 quick、standard、deep 或 100-paper 学习强度，输出 field-learning-plan，不执行检索。
---

# Field Learning Plan Design

## 定位

本 Skill 决定第 4 步“学到什么程度”。它不检索、不读文献，只把学习任务排程。

## 输入

- `field-learning-request-ledger.md`；
- 领域熟悉度：`unfamiliar / partial / familiar`；
- 时间预算：`quick / standard / deep / 100-paper`；
- 审稿任务类型：快速初审、正式审稿、case 回测、投稿前自审；
- 来源约束和期刊质量门槛。

## 输出

```text
field-learning-plan.md
```

字段：

```text
plan_id
learning_mode
learning_orientation
request_ids
reading_depth
abstract_target_count
fulltext_target_count
must_build_domain_map
must_build_repair_menu
must_update_arrow_audit
stop_rule
qc_risks
```

## 学习强度

- `quick`：10-20 篇摘要/综述，用于先获得领域感。
- `standard`：30-50 篇标题摘要 + 5-10 篇核心原文。
- `deep`：系统扩展同类研究、benchmark 和方法标准。
- `100-paper`：用户明确要求领域浸泡式学习时使用。

## 学习取向

学习强度决定“读多少”，学习取向决定“怎么读”。

```text
learning_orientation: arrow-oriented
```

审稿默认使用。目标是围绕当前 `target_arrow_id`、`judge-arrow`、`repair-arrow` 定点学习：查同类高质量文献，全文跳读/抽读与目标箭头有关的 Methods、Results、Figures、Tables、Captions、Supplement 和 Appendix，抽 evidence package。它不是完整领域综述。

```text
learning_orientation: field-immersion
```

用户明确要求“熟悉领域”“100 篇文献”“成为临时领域专家”时使用。目标是系统建立领域地图、概念谱系、方法谱系、指标体系、SOTA、开放问题和 canonical paper notes。

默认映射：

| task situation | default learning_orientation |
|---|---|
| 正式审稿 / 投稿前自审 / 返修准备 | `arrow-oriented` |
| quick / standard 时间预算 | `arrow-oriented` |
| deep 但仍以当前稿件为中心 | `arrow-oriented`，可加宽文献面 |
| 用户明确要求领域浸泡或 100-paper | `field-immersion` |

`field-learning-plan.md` 必须写明选择理由：

```text
orientation_reason:
```

## 完成标准

- 每个 request 都有学习深度和停止规则；
- 已声明 `learning_orientation` 和 `orientation_reason`；
- 陌生领域默认至少生成 `domain-map.md` 和 `review-risk-radar.md`；
- 需要修箭头知识时明确是否必须读全文、图表或补充材料；
- `arrow-oriented` 模式下，全文阅读任务必须绑定 `target_arrow_id`，并说明只抽哪些 evidence fields；
- `field-immersion` 模式下，必须增加领域专家化产物，如 canonical paper notes、concept glossary、field open questions；
- 输出可交给 `field-search-fulltext-strategy`。
