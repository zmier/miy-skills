---
name: field-learning-handoff-feedback
description: 学术领域学习移交与反哺子 Skill。用于 academic-field-evidence-learning 第七和第八步，把领域地图、外部证据、修箭头菜单和 QC 状态整理成 handoff-to-arrow-audit、handoff-to-repair-mapping、review-risk-radar、repair-feedback-candidates 和 field-learning-qc。
---

# Field Learning Handoff Feedback

## 定位

本 Skill 负责把第 4 步学到的东西交回 workflow。它不再检索、不再读文献，只做移交、QC 和反哺候选。

## 输入

- `domain-map.md`、`review-risk-radar.md`；
- `external-evidence-ledger.md`；
- `case-repair-menu.md`、`fulltext-pattern-ledger.md`；
- `field-learning-qc.md`；
- `internal-arrow-audit-table.md` 和 `academic-arrow-break-summary.md`。

## 输出

```text
handoff-to-arrow-audit.md
handoff-to-repair-mapping.md
repair-feedback-candidates.md
field-learning-qc.md
```

## 移交规则

- 给第 3 步：只移交能改变箭头状态或说明仍需 QC 的证据；
- 给第 5 步：只移交能形成修复动作、降调方案或 hold-for-learning 的知识；
- 给第 8 步：只移交可迁移候选，不直接改稳定 reference menu。

## 完成标准

- 每条 handoff 绑定 arrow id 或 request id；
- QC 状态写清 `done / pending / technical-failure / requires-human-access / needs-fulltext-pattern-check`；
- 反哺候选写明来源、适用边界、反例风险和所需回归测试；
- 没有完成的外部学习不包装成完成。

