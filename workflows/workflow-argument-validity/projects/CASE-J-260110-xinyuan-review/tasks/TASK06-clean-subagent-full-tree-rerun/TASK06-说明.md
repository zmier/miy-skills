# TASK06 Clean SubAgent Full Tree Rerun

## 目标

使用纯净 subAgent，基于 TASK05 新生成的完整 Markdown 底稿、表格文件和视觉复核日志，按更新后的 `academic-paper-argument-tree-extraction` Skill 重新盲跑学术论文 full-tree 抽取。

## 纯净边界

subAgent 不读取：

- 欣媛审稿意见；
- 旧版 V5 论证树；
- TASK01/TASK02/TASK04 的树或对照分析；
- 本线程中关于该论文的历史讨论摘要。

subAgent 只读取：

- 更新后的抽树 Skill 及其必要 references/assets；
- TASK05 主底稿；
- TASK05 表格文件；
- TASK05 表格视觉复核日志；
- TASK06 本说明。

## 输入

- 抽树 Skill：`/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/SKILL.md`
- 主底稿：`../TASK05-PDF手稿完整Markdown还原/outputs/manuscript_restored_with_tables.md`
- 表格目录：`../TASK05-PDF手稿完整Markdown还原/outputs/tables-restored/`
- 表格视觉 QC：`../TASK05-PDF手稿完整Markdown还原/logs/table-visual-qc.md`
- Restoration QC：`../TASK05-PDF手稿完整Markdown还原/logs/restoration-qc.md`

## 输出要求

写入 `outputs/`：

- `canonical-node-ledger.md`
- `canonical-edge-ledger.md`
- `evidence-ledger.md`
- `paper-argument-tree.md`
- `recursive-tree-master.md`
- `evidence-expanded-mermaid.md`
- `review-sensitivity-map.md`
- `sensitivity-expanded-mermaid.md`
- `obsidian-link-map.md`
- `extraction-qc.md`

写入 `logs/`：

- `log.md`

## 验收重点

- 是否抽出具体核心发现，而不是写成“作者做出来了”；
- 是否递归拆到最小证据单位，如单个系数、t 值、样本量、变量定义、脚注、表注、文献用途；
- 是否能使用 TASK05 的表格证据和视觉 QC；
- 是否发现表 11 的正文叙述与 PDF 表格冲突，并只放入 2B 显影树，不混入作者树；
- 是否先产出 canonical ledgers，再派生 Mermaid；
- 是否标清无法完成的地方，而不是用概括节点糊过去。
