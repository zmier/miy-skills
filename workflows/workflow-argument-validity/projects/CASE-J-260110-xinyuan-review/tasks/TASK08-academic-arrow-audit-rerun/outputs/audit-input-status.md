# Audit Input Status

## Verdict

`ready-for-academic-arrow-audit`，但带 QC caveats。

## Consumed Inputs

| input | status | notes |
|---|---|---|
| TASK07 `academic-argument-spine.md` | read | 用于固定 X/M/Y/Y2 和识别设计主轴。 |
| TASK07 `canonical-node-ledger.md` | read | 用于固定作者 claim 层级。 |
| TASK07 `canonical-edge-ledger.md` | read | 用于固定 `arrow_id: A -> B`。 |
| TASK07 `evidence-ledger.md` | read | 用于绑定底层 evidence。 |
| TASK07 `extraction-qc.md` | read | 用于保留表格、图、引用和 DAG-ready caveats。 |
| TASK07 `task07-readiness-for-arrow-audit-and-xinyuan-coverage.md` | read | 只用于 handoff target，不读取外部审稿判断文本。 |

## Frozen Comparison Materials

本阶段未读取欣媛审稿意见，也未读取旧审计表。对照应在本 TASK 的 `academic-arrow-audit-table.md` 冻结后另行进行。

## QC Caveats

| caveat | impact |
|---|---|
| `needs-table-visual-qc` | 表格系数、括号值和表注可以用于初步审计，但最终审稿引用前需 cell-level 复核。 |
| `needs-figure-qc` | Bacon 分解、placebo 图等只能作为作者文字证据，不能当作已视觉核验图形事实。 |
| `table-text-conflict` | 表11列(3)与正文机制叙述冲突，可以进入 `needs-table-qc / unclear` 审计项。 |
| `needs-citation-link` | 文献 gap 和引用支撑可初审为 `needs-citation-qc`，不能直接判 gap 断裂。 |
| `dag_ready: partial` | 可做初步因果箭头审计，但若要强 DAG 结论，需要回原文确认对照组/处理时点/冲击独立性。 |

