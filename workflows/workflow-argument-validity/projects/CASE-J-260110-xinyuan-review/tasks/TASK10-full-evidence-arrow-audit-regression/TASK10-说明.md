# TASK10 Full Evidence Arrow Audit Regression

## 目标

使用新版 `academic-argument-arrow-audit`，以 `mode: full-evidence-audit` 对 TASK07 作者论证树产物做一轮完整验箭头回归。

本轮同时测试：

1. 新版 SKILL 是否保留 TASK08 的锋利度；
2. 新版 SKILL 是否保留 TASK09 的工序纪律；
3. 外部证据增强是否能覆盖文献、方法来源、政策/监管文件、官方数据、官方文档和 citation verification；
4. 外部证据是否能正确回填到 `academic-arrow-audit-table.md`。

## 模式

```text
mode: full-evidence-audit
```

## 输入

只用 TASK07 抽树产物作为审计输入：

```text
../TASK07-latest-paper-tree-regression/outputs/
```

## 对比基线

审计表冻结前禁读 TASK08、TASK09 和欣媛审稿意见。

冻结后允许读取：

```text
../TASK08-academic-arrow-audit-rerun/outputs/
../TASK09-clean-subagent-academic-arrow-audit-v2/outputs/
```

并生成 `task10-regression-comparison.md`。

## 完成标准

- 先完成内部验箭头；
- 集中生成 `external-evidence-request.md`；
- 再集中查文献 / 方法 / 政策 / 官方数据 / 官方文档；
- 生成 `external-evidence-ledger.md`，每条外部证据绑定 `request_id` 和 `target_arrow`；
- 回填 `academic-arrow-audit-table.md`；
- 输出 `academic-arrow-break-summary.md` 和 `issue-selection-candidates.md`；
- 写 `logs/log.md`；
- 与 TASK08/TASK09 做质量对比。
