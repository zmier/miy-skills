---
date: 2026-06-20
type: reference
status: seed
source:
  - dialogue: paper argument tree child skill design
---

# Claim vs Evidence Boundary

## 一句话

学术论文抽树时：

```text
claim = 作者要让读者相信的、可判断真假的命题
evidence = 支撑判断的可定位、可核查材料
```

`academic-node-ledger-builder` 负责 claim 层级；`academic-evidence-drilling` 负责 evidence 叶子。两者不能互相抢活。

说明：`node_id`、`canonical-node-ledger.md` 是技术文件名；日常理解和 Skill 说明中优先使用 `claim` / `论点`，避免把问题误解成单纯画图。

## Claim 构建负责什么

Claim 构建负责建立作者论点的递归层级。

这些层级标签只是命名工具，不是固定五层模板。不要机械要求每篇论文都抽成 `root -> major -> middle -> subclaim -> sub-subclaim`。实际抽几层取决于作者论证：

```text
如果一个 claim 下面还有更小 claim 支撑，就继续拆；
如果下一层已经是可定位 evidence，就停止。
```

常用标签包括：

```text
root claim
major claim
middle claim
subclaim
sub-subclaim
```

只要一句话仍然是“作者要证明的判断”，无论多细，都属于 claim；只要还能问“为什么”，就还可以继续作为 claim 展开。

但“能问为什么”只是候选 claim 的识别线索。合格 claim 还必须能改写为形式逻辑视角下的简单命题或复合命题。若一句话只是“主结果”“机制检验”“核心发现成立”“贡献上升”等标签，应标记 `needs-claim-rewrite`，回到原文改写为可判真假的命题。

例子：

```text
R0: 本文值得发表
M1: 研究问题重要
S1: 现有文献没有回答 X 如何影响 Y
S1a: 既有机器人文献主要看就业和生产率
S1b: 既有出口产品结构文献较少讨论企业机器人采用
S1c: 因此本文的 gap 是真实的
```

这些都是 claim，因为都可以继续问：“为什么？”

但如果某篇论文的某条分支只有：

```text
root claim
-> subclaim
-> evidence
```

这也是合格结构。层数由论证需要决定，不由模板决定。

## 证据下钻负责什么

证据下钻负责为 claim 挂最小 evidence 叶子：

```text
原文句子
变量定义
表格单元格
模型设定
样本规则
图像事实
文献引用用途
政策或制度事实
```

证据必须能回答：

```text
在哪里？
哪张表？
哪一列？
哪个系数？
哪句话？
哪篇文献？
哪个变量定义？
```

## 判别法

| 问题 | 类型 |
|---|---|
| 能问“为什么？” | claim |
| 能问“在哪里 / 哪张表 / 哪个数 / 哪篇文献？” | evidence |
| “X 会影响 Y” | claim |
| “机制 M 解释 X 到 Y” | claim |
| “变量 X 可以衡量构念 A” | claim |
| “A 且 B”“如果 A 那么 B” | claim |
| “表 3 第 2 列 X 系数为正且显著” | evidence |
| “第 28 段定义 Robot 为机器人相关产品进口” | evidence |
| “Autor et al. 被作者用于说明技术变迁影响劳动需求” | evidence |

## 实验论文边界

实验设计类论文尤其容易混淆。规则是：

```text
实验做了什么、观测到什么 = evidence
实验设计是否足以识别因果、结果说明什么 = claim
```

例子：

| 内容 | 类型 | 原因 |
|---|---|---|
| 这个实验能够检验 X 是否导致 Y | claim | 作者对实验识别力的判断 |
| 实验随机分配处理组和控制组 | evidence | 可核查的设计事实 |
| 处理/对照组具有可比性 | claim | 需要随机化和平衡检验支撑 |
| 表 1 显示基线变量无显著差异 | evidence | 可定位的表格结果 |
| 处理组接受 A 干预，对照组没有 | evidence | 设计事实 |
| A 导致 Y 提升 | claim | 从实验结果上升出来的因果判断 |
| 表 2 第 1 列 treatment coefficient = 0.12, p < 0.05 | evidence | 最小结果证据 |

准实验设计同理。DID / IV / RD 等方法名称本身不是最小 evidence：

| 内容 | 类型 | 原因 |
|---|---|---|
| DID 能识别政策冲击对 Y 的影响 | claim | 需要平行趋势等假设支撑 |
| 政策发生时间、处理组定义、POST 编码 | evidence | 可定位的设计事实 |
| 平行趋势假设成立 | claim | 需要图表或事件研究证据支撑 |
| 图 2 处理前系数围绕 0 且不显著 | evidence | 可定位的 pretrend evidence |
| IV 是有效工具变量 | claim | 需要相关性和排除限制支撑 |
| 第一阶段 F 值、工具变量定义、制度解释 | evidence | 可定位的识别设计材料 |

详细规则见 `identification-design-adapter.md`。

## 接口规则

`academic-node-ledger-builder` 不填具体表格系数、文献链接或图像事实；这些缺口只留 `evidence_needed` 或空 `evidence_ids`。

`academic-evidence-drilling` 不重新发明 claim 树；如果发现 claim 缺失，只写入 QC 或提出回退，不直接改写 node ledger。

`academic-edge-ledger-builder` 只消费 node ledger 和 evidence ledger，建立支撑边；它不新增 claim 或 evidence。

## Red Flags

- 把研究设计或论文写作标签当成 claim，而没有还原为命题；
- 用 `X/M/Y/Y2` 替代一句话核心发现的命题结构；
- 把“主结果”“机制检验”“稳健性”“文献支持”当作 evidence leaf；
- 在证据下钻阶段重写 X1/X2/Y；
- 在 claim 构建阶段填大量表格系数导致作者论点树失焦；
- 把审稿攻击写成作者 claim；
- 把实验设计事实直接当成因果结论。
