---
name: academic-evidence-drilling
description: 学术论文抽树的证据下钻子 Skill。用于基于 canonical-node-ledger，为 claim 节点挂最小可核查 evidence 叶子，覆盖文本、变量、样本、模型、表格单元格、图像、文献用途和制度事实；不重新设计 claim 树。
---

# Academic Evidence Drilling

## 定位

本 Skill 只负责证据下钻。

它回答：

```text
每个 claim 节点由哪些最小、可定位、可核查的证据支撑？
```

## 输入

- `task-contract.md`
- `academic-argument-spine.md`
- `canonical-node-ledger.md`
- restored manuscript Markdown / paper text
- table extraction outputs / visual QC logs if available
- bibliography / citation sections if available
- `../../references/claim-vs-evidence-boundary.md`
- `../../references/identification-design-adapter.md` when the paper contains experiment / quasi-experiment / causal identification design
- `../../references/materials-hydrovoltaic-adapter.md` when the paper is a materials / device / hydrovoltaic paper
- `../../assets/evidence-ledger-template.md`

## 输出

```text
evidence-ledger.md
```

字段：

```text
evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点/箭头 | 证据粒度 | Obsidian 链接
```

合格 evidence leaf：

```text
一句可定位原文
一个变量定义
一个样本筛选规则
一个模型设定
一个识别设计事实
一个材料制备 / 表征 / 器件测试事实
一个表格单元格
一个图像事实
一篇文献的具体用途
一个政策或制度事实
```

## 边界

- 不重新设计 `canonical-node-ledger.md`；
- 不建立 `canonical-edge-ledger.md`；
- 不生成 Mermaid；
- 不做审稿攻击；
- 如果发现 claim 缺失或层级错误，写入 QC / handoff，不直接改写节点树；
- citation evidence、table / figure evidence 可先在本 Skill 内完成；若反复失败，再抽独立子 Skill。
- 实验 / 准实验 / 因果识别设计必须按 `identification-design-adapter.md` 拆成设计 claim 和设计 evidence，不能只写“DID / IV / RCT 设计”。
- 材料 / 器件 / 水伏发电论文必须按 `materials-hydrovoltaic-adapter.md` 拆成材料设计、结构表征、测试条件、性能结果、机制对照、稳定性和 SOTA 对比 evidence，不能只写“性能优异”。
