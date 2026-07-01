# Extraction QC

## 状态

`full-tree-complete-with-table-visual-qc-needed`

## 完整性检查

| check | status | note |
|---|---|---|
| 论文类型判断 | pass | 实证论文：DID、事件研究、机制/异质性/稳健性表 |
| 抽树模式 | pass | `full-tree` |
| 2A/2B 分离 | pass | `paper-argument-tree.md` 不写审稿意见；`review-sensitivity-map.md` 只列待验组合 |
| 一句话核心发现 | pass | X/M/Y/Y2 已固定 |
| X1 展开 | pass | 覆盖现实背景、理论 puzzle、文献 gap、贡献声称 |
| X2 展开 | pass | 覆盖变量定义、样本、模型、主结果、稳健性、机制、异质性 |
| Y/Y2 展开 | pass | 覆盖监管、市场中介、企业实践启示 |
| evidence ledger | pass | 关键节点均有 evidence_id |
| evidence-expanded Mermaid | pass | evidence leaves 画回 Mermaid |
| review-sensitivity-map | pass | 12 个显影项均绑定 evidence_ids |
| Obsidian link map | partial | 手稿缺块 ID，当前为标题级链接/needs-anchor |
| 表格视觉核验 | needs-qc | `restoration-qc.md` 明示精确值需回 PDF 复核 |

## 关键 QC 标记

| qc_id | 类型 | 关联证据 | 问题 | 后续动作 |
|---|---|---|---|---|
| QC01 | needs-table-visual-qc | E-DESC, E-PT, E-R1-E-R7, E-M1-E-M3, E-H1-E-H5 | Table 2-18 的系数、t 值、星号、样本量来自 PDF 文本/table snippets，未视觉核验 | 回原 PDF 对表格逐项核验 |
| QC02 | needs-figure-qc | E-R3, E-M1 | Bacon、安慰剂、CAR 图只有抽取文本和少量描述 | 回 PDF 视觉核验图形与作者文字是否一致 |
| QC03 | needs-anchor | all | 手稿没有稳定段落块 ID | 给 `inputs/manuscript.md` 或复制稿补段落锚点后更新 link map |
| QC04 | mechanism-behavior-link | E-M1, E-M1A, E-M2 | 机制检验多为分组异质性，缺同行企业实际披露行为改变的微观行为证据 | 后续 arrow audit 验 P7/P8 -> X2 |
| QC05 | treatment-active-status | E-V2, E-D2 | “无问询或处罚”是否足以证明主动披露未受其他外部压力驱动未核验 | 后续 arrow audit 验 P1 -> X2 |
| QC06 | policy-boundary | E-H5, E-C2 | 低竞争行业出现反向结果，可能影响普遍政策启示 | 后续 arrow audit 验 P11/P12 -> Y |

## 禁止文件合规

- 未读取欣媛审稿意见或任何 xinyuan comparison 输出。
- 未读取 TASK01/TASK02 禁止输出内容。
- 只写入 `tasks/TASK04-subagent-full-tree-blind/`。

