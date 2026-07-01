---
name: repair-case-menu-synthesis
description: 修箭头临时菜单合成与反哺候选子 Skill。用于把 abstract-scan-ledger 和 fulltext-pattern-ledger 中抽到的证据包合成为本案 case-repair-menu，区分 minimum evidence、strong evidence package、fallback downgrade、source basis 和 transfer status；同时生成 repair-feedback-candidates，但不自动改写稳定 menu。
---

# Repair Case Menu Synthesis

## 定位

本 Skill 把学习到的 repair pattern 转成本案可用的临时修复菜单，并把可能可迁移的规则写成反哺候选。它不直接写审稿意见，也不把个案经验自动升级为通用规则。

## 输入

- `abstract-scan-ledger.md`；
- `fulltext-pattern-ledger.md`；
- `repair-knowledge-gap.md`；
- `academic-arrow-break-summary.md`；
- 目标稿件的断箭头清单。

## 输出

```text
case-repair-menu.md
repair-feedback-candidates.md
repair-learning-qc.md
```

`case-repair-menu.md` 字段：

```text
arrow_type
common_break
minimum_evidence
strong_evidence_package
fallback_downgrade
source_basis
transfer_status
handoff_to_repair_map
```

`repair-feedback-candidates.md` 字段：

```text
candidate_id
source_case
candidate_rule
target_reference_or_menu
evidence_basis
scope_conditions
known_exceptions
required_regression_tests
promotion_status
```

## 迁移状态

- `case-only`：只来自本案或单篇来源，只能作为本案建议。
- `candidate-general`：多篇高质量来源或权威资料提示同一模式，可作为候选规则。
- `stable-menu`：跨来源反复出现，且有清楚验收标准，可沉淀进稳定 repair menu。
- `unknown`：资料不足，不应强行给方案。

## 反哺纪律

- `case-repair-menu.md` 服务当前审稿或自审；
- `repair-feedback-candidates.md` 服务后续 Skill / reference 增强；
- 不在本 Skill 中直接修改稳定 `references/*repair-menu.md`；
- 只有满足以下条件之一，才建议后续提升为稳定 menu：
  - 多篇高质量来源反复出现同一 evidence package；
  - 权威方法文档、官方标准或顶刊综述明确给出验收标准；
  - 真实 case UAT 和回归测试显示该规则能提升质量且不误伤其他案例。

## 完成标准

- 每条 menu 都绑定来源；
- 每条 menu 都说明能修哪类断点；
- 不把审稿人个案意见包装成普遍规律；
- 可迁移内容已进入 `repair-feedback-candidates.md`，并标明升级前需要什么验证；
- 输出能被 `academic-arrow-repair-mapping` 直接消费。
