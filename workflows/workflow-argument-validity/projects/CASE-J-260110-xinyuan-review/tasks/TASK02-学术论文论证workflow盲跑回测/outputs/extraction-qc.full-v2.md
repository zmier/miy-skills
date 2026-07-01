# Extraction QC Full V2

## 状态

```text
full-tree: complete
2A author evidence tree: complete
2B review sensitivity map: complete
obsidian links: partial / needs-anchor
table QC: partial
```

## 通过项

| 项目 | 状态 | 说明 |
|---|---|---|
| 一句话核心发现 | pass | 已明确 X/M/Y/Y2 |
| X1/X2/Y | pass | 已拆为问题意义、核心发现证明、贡献成立 |
| evidence ledger | pass | 覆盖变量定义、样本规则、模型、主结果、机制、稳健性、异质性、贡献上升 |
| evidence-expanded Mermaid | pass | 关键 evidence node 已画回 Mermaid |
| review sensitivity map | pass | 生成 14 个可疑证据组合，供后续验箭头 |
| 作者树/审稿显影分离 | pass | 2A 不写攻击；2B 不写最终审稿意见 |

## 仍需 QC

| 缺口 | 影响 | 建议 |
|---|---|---|
| 多数表格没有完整数值 | 不能核实每个系数、t 值/标准误、样本量、星号 | 回到 PDF 或表格抽取文件补齐 Table 3-18 |
| 表注中括号含义未从稿件表格中核实 | 影响 reporting-integrity 检查 | 表格 QC 时记录括号是 t 值还是标准误 |
| Obsidian 链接没有稳定块 ID | 软锚点可能不能直接跳转 | 给 manuscript 增加 `^block-id` 或标题锚点 |
| 文献卡片链接未核实 | gap 和经典指标层级不能直接跳到文献笔记 | 后续文献/引用审查阶段补 `needs-citation-link` |
| 图3 / 表10 / 表11 样本是否一致未核实 | 影响 S7 机制样本一致性 | 表格和图示 QC 时记录样本量与样本筛选口径 |

## 这版相比 blind tree 的提升

| 维度 | blind tree | full-v2 |
|---|---|---|
| 样本规则 | 合并成一个设计节点 | 拆到 E-P5-1...E-P5-7，并在 S2 显影 |
| 时间结构 | 只说 Peerdumy x POST | 拆到 POST=t...t+2、动态效应、POST_Month，并在 S4 显影 |
| 聚类层级 | 在模型节点里一带而过 | 单独成为 E-P6-2，并在 S5 显影 |
| 机制一致性 | 列表式记录 CAR/关注/处罚 | S1/S7/S8/S11 跨表并读 |
| 贡献上升 | 只说 KV -> 行业自律 | S6/S12 显影 KV 与宏大叙事之间的层级跳跃 |
| 异质性 | 合并成边界条件 | E-H1...E-H5 单独进入 ledger，并显影 EFD 层级和竞争机制边界 |

## 下一步

用本版作为正式输入，重跑：

```text
academic-arrow-audit-table.full-v2.md
academic-selected-issues.full-v2.md
xinyuan-comparison.full-v2.md
```
