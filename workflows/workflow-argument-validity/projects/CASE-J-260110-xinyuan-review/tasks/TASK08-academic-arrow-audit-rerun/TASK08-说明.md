# TASK08 Academic Arrow Audit Rerun

## 目标

使用升级后的 `academic-argument-arrow-audit`，基于 TASK07 的作者论证树产物，执行一版学术论文验箭头实操，并记录可反哺点。

## Skill 路线

```text
workflow-academic-argument-validity
-> argument-arrow-audit
-> academic-argument-arrow-audit
```

本 TASK 对应学术论证 workflow 的第 3 步：

```text
验箭头 / 找断点
```

## 输入冻结

本轮审计输入只使用 TASK07：

- `canonical-node-ledger.md`
- `canonical-edge-ledger.md`
- `evidence-ledger.md`
- `academic-argument-spine.md`
- `extraction-qc.md`
- `task07-readiness-for-arrow-audit-and-xinyuan-coverage.md`

冻结期不读取：

- 欣媛审稿意见；
- 旧 TASK01/TASK02/TASK04/TASK06 的审稿判断；
- 旧 arrow audit / selected issues；
- 当前对话之外的人工审稿结论。

## 预期输出

```text
outputs/audit-input-status.md
outputs/plain-language-arrow-list.md
outputs/typed-arrow-ledger.md
outputs/audit-route-plan.md
outputs/review-sensitivity-map.md
outputs/academic-arrow-audit-table.md
outputs/academic-arrow-break-summary.md
outputs/issue-selection-candidates.md
outputs/method-knowledge-gap.md
outputs/workflow-feedback.md
logs/log.md
```

## 完成标准

- 每个审计判断绑定 `arrow_id`；
- 每个 weak/broken/unclear/needs-qc 绑定 `evidence_id` 或 QC 缺口；
- 不直接选择 major concern；
- 不写最终审稿意见；
- 不把“拿不准”硬判为作者错误；
- 明确哪些地方需要后续 table / figure / citation / method QC。

