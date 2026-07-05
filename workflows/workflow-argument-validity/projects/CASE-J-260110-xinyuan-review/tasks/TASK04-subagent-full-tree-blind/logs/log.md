# TASK04 Log

## 读取的输入文件

- `inputs/manuscript.md`
- `tasks/TASK03-PDF完整底稿补抽/outputs/pdf-pages-text.md`
- `tasks/TASK03-PDF完整底稿补抽/outputs/table-text-snippets.md`
- `tasks/TASK03-PDF完整底稿补抽/outputs/pdf-table-inventory.md`
- `tasks/TASK03-PDF完整底稿补抽/outputs/restoration-qc.md`

## 读取的 Skill / references / assets

- `skills/argument-workflow-orchestrator/SKILL.md`
- `subworkflows/workflow-academic-argument-validity/SKILL.md`
- `skills/argument-tree-extraction/SKILL.md`
- `skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/SKILL.md`
- `skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/empirical-paper-adapter.md`
- `skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/obsidian-evidence-linking.md`
- `references/mermaid-obsidian-rules.md`
- `skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/assets/paper-argument-tree-template.md`
- `skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/assets/evidence-ledger-template.md`
- `skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/assets/obsidian-link-map-template.md`
- `skills/argument-tree-extraction/assets/evidence-expanded-mermaid-template.md`

## 明确未读取的禁止文件

- 未读取 `inputs/xinyuan-review.txt`
- 未读取 `inputs/xinyuan-review.docx`
- 未读取 `outputs/xinyuan-review-argument-map.md`
- 未读取 `tasks/TASK01-*` 下任何 `outputs`
- 未读取 `tasks/TASK02-*` 下任何已有 blind/full-v2/xinyuan-comparison/arrow-audit/selected-issues 输出

说明：曾用 `rg --files` 列出项目文件名以确认边界，未打开或读取禁止文件内容。

## 使用的 Skill 规则

- 按学术论文整篇抽树路由到 `academic-paper-argument-tree-extraction`。
- 论文类型判断为实证论文，使用 `empirical-paper-adapter`。
- 抽树模式为 `full-tree`。
- 按两步执行：`2A 作者证据树` 与 `2B 审稿显影树` 分离。
- 2A 只忠实还原作者证据链，不写审稿意见。
- 2B 只从 2A evidence ledger 中组合可疑证据，不凭空添加无锚点问题，不写最终审稿意见。
- Mermaid 使用 `flowchart BT`，箭头表示下层 supports 上层。
- 表格证据来自 `table-text-snippets.md` 和 `pdf-pages-text.md`；因未视觉核验 PDF 表格，精确表格值标记 `needs-table-visual-qc`。

## QC

- PDF 表格 inventory 显示仅识别到 2 个候选假表，Table 2-18 主要依赖 page text/table snippets 抽取，所有表格精确值需视觉核验。
- `inputs/manuscript.md` 带有若干批注样式标记，但本任务只把它作为手稿文本，不读取外部审稿意见。
- 输出已覆盖 X1、X2、Y/Y2，覆盖实证论文 adapter 要求的变量定义、样本规则、模型设定、主结果、机制、稳健性、异质性和贡献上升。
- 状态：`full-tree-complete-with-table-visual-qc-needed`。

## 2026-06-20 主线程复盘补记

用户指出：本 TASK 虽有 Mermaid，但不是老王论效式“总论点 -> 分论点 -> 子论点 -> 最小证据”的完整递归树。该意见成立。

本 TASK 的信息台账和 2B 显影有价值，但 `evidence-expanded-mermaid.md` 更像分块结构图，不是 canonical recursive evidence tree。后续已将 `academic-paper-argument-tree-extraction` 升级为：

```text
canonical-node-ledger.md
canonical-edge-ledger.md
evidence-ledger.md
recursive-tree-master.md
```

并要求 Mermaid 只是从 canonical ledgers 派生的视图。后续重跑 subAgent 时，应按新标准生成 canonical recursive tree，不能用 `E-R1 表4主结果`、`E-D2 样本剔除规则` 这类抽象叶子冒充最小证据。
