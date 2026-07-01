---
name: academic-argument-spine-extraction
description: 学术论文抽树的主干抽取子 Skill。用于从手稿中抽一句话核心发现、X/M/Y/Y2、X1 问题有意义、X2 作者证明了具体核心发现、Y 论文贡献成立；只产出 academic-argument-spine，不建完整节点树或证据台账。
---

# Academic Argument Spine Extraction

## 定位

本 Skill 只负责学术论文抽树的第一步：抽主干。

它回答：

```text
这篇论文到底想证明什么？
哪个 X 通过什么 M 影响哪个 Y？
作者如何把这个发现上升为贡献 / 值得发表？
```

## 输入

- `task-contract.md`
- restored manuscript Markdown / paper text
- abstract / introduction / theory / conclusion
- 必要时读取 `../../references/empirical-paper-adapter.md`、`../../references/theory-paper-adapter.md`、`../../references/conceptual-review-adapter.md` 或 `../../references/materials-hydrovoltaic-adapter.md`

## 输出

```text
academic-argument-spine.md
```

必须包含：

```text
one-sentence finding
X / M / Y / Y2
X1: 问题有意义
X2: 作者证明了具体核心发现
Y: 论文贡献成立 / 值得发表
paper_type
uncertainties / QC
```

## 边界

- 不建完整 `canonical-node-ledger.md`；
- 不填表格系数、文献证据或图表证据；
- 不做审稿攻击；
- X2 不得写成“作者做出来了”“核心发现成立”“作者证明了核心发现”等空泛占位，必须写成具体 X -> Y / X -> M -> Y 发现。

合格：

```text
X2: 作者声称企业主动披露违规改善同行企业信息披露质量，并通过 DID 主结果、机制检验、异质性和稳健性支撑该经验发现。
```

不合格：

```text
X2: 核心经验发现成立
X2: 作者证明了具体核心发现
X2: 作者做出来了
```
