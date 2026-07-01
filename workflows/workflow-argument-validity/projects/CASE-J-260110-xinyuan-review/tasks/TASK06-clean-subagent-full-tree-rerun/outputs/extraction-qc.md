# Extraction QC

## Status

| check | status | notes |
|---|---|---|
| full-tree mode | complete-with-qc | 已产出 canonical node/edge/evidence ledger、paper tree、recursive master、evidence-expanded Mermaid、2B sensitivity map、sensitivity Mermaid、Obsidian link map |
| empirical adapter | complete | 已按实证论文覆盖 X/Y/M、样本、变量、模型、固定效应、聚类、主结果、机制、稳健性、异质性和贡献上升 |
| canonical ledgers before Mermaid | complete | 先写入 `canonical-node-ledger.md`、`canonical-edge-ledger.md`、`evidence-ledger.md`，再派生 Mermaid |
| 2A/2B separation | complete | 表 11 冲突只进入 2B，不连入作者树 P7.1 的支持链 |
| recursive minimal evidence | complete-with-qc | 已拆到单个变量定义、样本规则、系数、括号值、显著性、样本量、FE/聚类、p 值、图形文字证据；图形证据标记 needs-figure-qc |
| table visual QC usage | complete | 使用 `table-visual-qc.md` 和 `restoration-qc.md`，并记录表 11 冲突 |
| incomplete-full-tree | no | 必交付均已生成 |
| incomplete-canonical-tree | no | canonical node/edge/evidence ledger 均已生成 |
| incomplete-recursive-tree | no | 关键非叶节点均有 child_ids 或 evidence_ids |
| abstract-evidence-leaf | no material abstract leaf | “稳健性/机制/主结果/样本规则”均已拆分；图 1/2/3 因未裁剪只作为正文锚点标 QC |

## QC Flags

| flag | location | reason | impact |
|---|---|---|---|
| needs-figure-qc | E-ROB-5; E-ROB-6; mechanism figure prose | TASK05 未精准裁剪图 1、图 2、图 3；目前仅有正文描述和表格旁证 | 影响后续对 Bacon、placebo 分布、CAR 趋势的图形级验箭头 |
| page-level-table-qc-only | E-QC-TABLE-1; E-QC-TABLE-2 | 表格为页面级视觉复核，不是逐单元格人工复核 | 正式审稿逐句引用前应复核关键表格单元 |
| table-11-author-prose-conflict | E-T11-CONFLICT-1; E-T11-CONFLICT-2 | PDF 表 11 第三列与作者正文叙述不一致 | 已显影到 S-T11-1；不混入作者树 |
| needs-citation-link | obsidian-link-map | 文献卡片未逐篇核验，仅保留作者年份或已有双链线索 | 不影响作者树结构；影响 Obsidian 文献穿透 |

## Coverage Checklist

| requirement | evidence / output |
|---|---|
| X 定义和操作化 | P1; E-XDEF-1 至 E-XDEF-5 |
| Y 定义和操作化 | P3; E-YDEF-1 至 E-YDEF-3 |
| M 理论机制 | P2; P2.1; P2.2; E-THEORY-* |
| 样本期、样本筛选、样本量 | P4; E-SAMPLE-* |
| 模型设定、固定效应、控制变量、聚类 | P5; E-CTRL-1; E-MODEL-1 至 E-MODEL-3 |
| 主结果单元格 | P6.1; E-MAIN-1 至 E-MAIN-5 |
| 机制检验 | P7.1-P7.3; E-MECH-* |
| 稳健性 | P8.1-P8.7; E-ROB-* |
| 异质性/边界 | P10.1-P10.5; E-HET-* |
| 贡献上升 | P9; E-X1-POLICY-1 |
| 2B 显影 | `review-sensitivity-map.md`; `sensitivity-expanded-mermaid.md` |
