---
name: academic-node-ledger-builder
description: 学术论文抽树的 claim 台账构建子 Skill。用于基于 academic-argument-spine，把作者论证递归拆成必要的 claim 层级，产出 canonical-node-ledger；不要求固定五层，不负责下钻具体表格、文献或图像证据。
---

# Academic Node Ledger Builder

## 定位

本 Skill 只负责建立作者树的 claim 层级。claim 层级是递归展开，不是固定模板；实际抽几层取决于作者论证复杂度。

它回答：

```text
作者需要让读者相信哪些判断？
这些判断之间有哪些层级？
哪些 claim 还需要证据下钻？
```

## 输入

- `task-contract.md`
- `academic-argument-spine.md`
- restored manuscript Markdown / paper text
- `../../references/claim-vs-evidence-boundary.md`
- `../../references/materials-hydrovoltaic-adapter.md` when the paper is a materials / device / hydrovoltaic paper
- `../../assets/canonical-node-ledger-template.md`

## 输出

```text
canonical-node-ledger.md
```

字段：

```text
node_id | label | type | depth | parent_id | child_ids | evidence_ids | source_links | status
```

claim 类型可用：

```text
root
major-claim
middle-claim
subclaim
sub-subclaim
evidence-needed
```

这些类型只是深度标签。若一条分支只有 `root -> subclaim -> evidence`，也可以合格；若一条分支需要继续拆到 `sub-subclaim` 或更细，也可以继续，但必须仍然是作者要证明的判断。

## 边界

- 只建 claim 层级，不填具体 evidence 叶子；
- 不机械补满 root / major / middle / subclaim / sub-subclaim 五层；
- 可以标 `evidence_needed`，但不发明表格系数、文献用途或变量定义；
- 不建立 `canonical-edge-ledger.md`；
- 不做审稿攻击；
- 如果发现 spine 不清，写 QC 或请求回退，不自行重写整篇 spine。
