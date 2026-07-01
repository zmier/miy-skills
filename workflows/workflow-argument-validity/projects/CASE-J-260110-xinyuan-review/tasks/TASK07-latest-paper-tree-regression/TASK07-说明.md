# TASK07 Latest Paper Tree Regression

## 目标

用最新版 `academic-paper-argument-tree-extraction` 对欣媛 case 重新做一次纯净 full-tree 抽树回测，检查近期 Skill 调整是否改善：

- claim/evidence 边界；
- 递归 claim 层级而非固定五层；
- 识别设计 evidence；
- citation / table evidence；
- edge 只还原作者支撑关系；
- Mermaid 尽量完整显影；
- paper 抽树不混入 review sensitivity / arrow audit。

## 输入

- `../TASK05-PDF手稿完整Markdown还原/outputs/manuscript_restored_with_tables.md`
- `../TASK05-PDF手稿完整Markdown还原/logs/table-visual-qc.md`
- `../TASK05-PDF手稿完整Markdown还原/logs/restoration-qc.md`

## 禁读

- 欣媛审稿意见；
- 本 case 旧 outputs；
- TASK01/TASK02/TASK04/TASK06 outputs；
- 当前对话记录；
- 任何 review issue / sensitivity / arrow audit 旧产物。

## 输出

写入本 TASK 的 `outputs/` 和 `logs/`。

最终由主 agent 与旧版 baseline 对比。
