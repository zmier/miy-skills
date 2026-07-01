# TASK09-clean-subagent-academic-arrow-audit-v2 说明

## 任务边界

- 本轮是新版 `academic-argument-arrow-audit` SKILL 的干净视角盲跑。
- 只消费 TASK07 抽树产物；未读取 TASK08、旧版审稿/验箭头输出、欣媛审稿意见或任何对比欣媛意见的文件。
- TASK07 中 `task07-readiness-for-arrow-audit-and-xinyuan-coverage.md` 文件名显示与欣媛覆盖对比有关，已按盲跑限制跳过。
- 本轮不联网、不数据库检索；所有外部证据需求集中写入 `outputs/external-evidence-request.md`，并在 `outputs/external-evidence-ledger.md` 中标记 `not-searched / pending`。

## 输入材料

读取并使用：

- TASK07 `outputs/academic-argument-spine.md`
- TASK07 `outputs/canonical-node-ledger.md`
- TASK07 `outputs/canonical-edge-ledger.md`
- TASK07 `outputs/evidence-ledger.md`
- TASK07 `outputs/extraction-qc.md`
- TASK07 `outputs/paper-argument-tree.md`
- TASK07 `outputs/obsidian-link-map.md`

未使用为判断依据：

- TASK07 `outputs/task07-readiness-for-arrow-audit-and-xinyuan-coverage.md`
- 任何 TASK08 或旧版审稿/验箭头文件

## 产出说明

本目录按新版八步主轴产生：

- `logs/log.md`
- `outputs/audit-input-status.md`
- `outputs/review-sensitivity-map.md`
- `outputs/plain-language-arrow-list.md`
- `outputs/typed-arrow-ledger.md`
- `outputs/internal-arrow-audit-table.md`
- `outputs/external-evidence-request.md`
- `outputs/external-evidence-ledger.md`
- `outputs/academic-arrow-audit-table.md`
- `outputs/academic-arrow-break-summary.md`
- `outputs/issue-selection-candidates.md`
- `outputs/qc-and-skill-feedback.md`

## 总体盲跑判断

新版 SKILL 能按“作者箭头 -> 内部验箭头 -> 集中外部证据请求 -> 回填 ledger”的主轴运行。TASK07 材料足以完成一轮内部审计，但文献 gap、KV 指标有效性、DID 聚类/分期处理规范、Oster 方法细节、若干引用用途仍需要外部证据或人工表格 QC 后才能定论。
