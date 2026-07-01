# Academic Paper Argument Tree Regression Tests

## Purpose

`academic-paper-argument-tree-extraction` 是学术论文抽树的复合型子 Skill。学术主轴、adapter、claim/evidence 边界、证据下钻、citation evidence、table/figure evidence 或输出契约变化后，应做 academic 分支回归。

## Clean SubAgent Rule

按 `workflow-tao/references/regression-test-protocol.md`：

- 使用纯净 subAgent；
- 禁读修改讨论和无关旧答案；
- 只读测试输入、被测 Skill、必要 references/assets 和 target；
- 产物与 baseline / target md 做质量对比。

## Smoke Target

- [ ] 明确 X/M/Y/Y2；
- [ ] 产出 canonical node/edge/evidence ledger；
- [ ] 表格证据拆到单元格或明确 QC；
- [ ] 文献证据拆到单篇文献用途或标 `missing-citation-evidence`；
- [ ] Mermaid 从 ledger 派生；
- [ ] 表文冲突、审稿攻击和 sensitivity 结论不混入作者树；
- [ ] `extraction-qc.md` 能说明是否可移交 `academic-argument-arrow-audit`；
- [ ] `extraction-qc.md` 说明缺口。
