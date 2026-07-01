# Canonical Recursive Evidence Tree

## 核心定义

完整论证树不是几张 Mermaid 图，而是一棵 canonical recursive evidence tree：

```text
root claim
<- recursively lower claim(s)
<- minimal evidence
```

全篇论文逻辑上只有一棵 master tree。分树只是从 master tree 派生出来的阅读视图。

Claim 层级是递归的，不是固定层数。中间有几层 claim 就画几层；没有就不补。

## 必交付

`full-tree`、case 回测、正式审稿、专家意见对照必须输出：

```text
canonical-node-ledger.md
canonical-edge-ledger.md
evidence-ledger.md
recursive-tree-master.md
evidence-expanded-mermaid.md
extraction-qc.md
```

可选但推荐输出：

```text
view-x1-tree.md
view-x2-identification-tree.md
view-mechanism-tree.md
view-robustness-tree.md
view-contribution-tree.md
obsidian-link-map.md
```

## 节点台账

`canonical-node-ledger.md` 使用：

```text
node_id | label | type | depth | parent_id | child_ids | evidence_ids | source_links | status
```

`type` 可用：

```text
root-claim
major-claim
middle-claim
subclaim
minimal-evidence
implicit-premise
```

`status` 可用：

```text
complete
needs-children
needs-evidence
needs-anchor
abstract-evidence-leaf
needs-table-visual-qc
```

## 边台账

`canonical-edge-ledger.md` 使用：

```text
edge_id | from_node | to_node | relation | support_type | status | notes
```

`relation` 默认是：

```text
supports
```

可选：

```text
defines
operationalizes
measures
identifies
tests
generalizes-to
```

抽树阶段的 edge status 默认：

```text
not-yet-audited
```

验箭头阶段再改成 `strong / weak / broken / unclear`。

## 证据台账

`evidence-ledger.md` 使用：

```text
evidence_id | evidence_type | source_location | exact_content | supports_node_or_edge | granularity | qc_status | source_link
```

`granularity` 可用：

```text
minimal
compound-needs-split
summary-only
```

`qc_status` 可用：

```text
verified
needs-table-visual-qc
needs-figure-qc
needs-citation-link
needs-anchor
```

## 递归下钻规则

对每个非叶子节点，必须继续问：

```text
作者用哪些更小命题或证据支撑它？
```

如果 answer 仍然是下列抽象词，就不能停：

```text
样本设计
识别策略
稳健性检验
机制检验
异质性分析
主结果
理论支持
文献支持
变量定义
政策启示
```

这些都必须继续拆到更小的节点。

## 最小证据停止规则

只有以下对象可以作为 leaf：

- 一个可定位原文句子；
- 一个脚注规则；
- 一个表格中的单个系数；
- 一个 t 值、标准误、显著性星号或样本量；
- 一个变量定义、量纲、方向或转换；
- 一个模型设定；
- 一个固定效应设定；
- 一个聚类层级说明；
- 一个图表结果；
- 一篇文献被作者用于支持某个命题；
- 一个政策文件或制度事实。

## 抽象叶子禁止

不合格 leaf：

```text
E-R1 表4主结果
E-D2 样本剔除规则
E-M1 CAR为正
E-H5 行业竞争异质性
E-P8 稳健性通过
```

合格 leaf：

```text
E-R1a 表4列(1)：Peerdumy×POST = -0.0157***
E-R1b 表4列(2)：Peerdumy×POST = -0.0111***
E-R1c 表4表注：括号内为公司层面聚类调整标准误
E-R1d 表4样本量 = 11339
E-D2a 脚注：t 至 t+2 不应存在第二次冲击
E-D2b 脚注：t-5 至 t 不应存在主动披露违规
E-M1a 表10：CAR[-5,5] = 0.0182***
E-CIT1 Dye 被作者用于支持同行披露决策会相互影响
```

如果暂时只有概括性抽取结果，必须标记：

```text
abstract-evidence-leaf
```

并写入 `extraction-qc.md`。

## Mermaid 生成规则

先完成：

```text
canonical-node-ledger.md
canonical-edge-ledger.md
evidence-ledger.md
```

再生成：

```text
recursive-tree-master.md
evidence-expanded-mermaid.md
view-*.md
```

Mermaid 不是主产物。Mermaid 节点必须来自 node/evidence ledger，不允许手写概括图替代 canonical tree。

`evidence-expanded-mermaid.md` 的首要目标是完整显影，而不是好读。full-tree 场景下，应尽量从每个 minimal evidence 出发，沿 ledger 中记录的 parent / edge 递归画到 root claim：

```text
minimal evidence
-> nearest supporting claim
-> recursively higher claim(s)
-> root claim
```

中间 claim 层数由 ledger 决定，不得机械补成固定五层。

Mermaid 视觉规范：

- claim / evidence / needs-qc 必须视觉区分；
- 默认使用 `flowchart BT`，下层 evidence 指向上层 claim；
- 优先折线，减少大图曲线缠绕；
- 节点 label 保持短，完整证据写在 ledger；
- 完整图用于覆盖检查，阅读分图用于人类阅读；
- 高清 PNG 应使用 Mermaid CLI / Chromium 渲染，不能使用会丢失 Mermaid HTML label 文字的转换方式。

不要因为图太大、太长或不够美观而删除 evidence leaf。可读性问题用派生视图解决：

```text
recursive-tree-master.md       # 主树完整文本视图
evidence-expanded-mermaid.md   # 尽量完整的全量 Mermaid
view-x1-tree.md                # 派生阅读视图
view-x2-identification-tree.md
view-mechanism-tree.md
view-robustness-tree.md
view-contribution-tree.md
mermaid-zh-views/              # 中文可读分图和高清 PNG
```

如果 Mermaid 渲染限制导致无法容纳全量树，必须：

1. 在 `evidence-expanded-mermaid.md` 中说明 `mermaid-render-limit`;
2. 尽量输出可渲染的最大完整子图；
3. 用 `recursive-tree-master.md` 保留全量结构；
4. 在 `extraction-qc.md` 标记哪些 evidence leaf 未进入 Mermaid。

不能把“为了可读性简化”作为 full-tree Mermaid 缺失底层 evidence 的理由。

## 验收规则

若满足任一情况，不能宣称 full-tree 完成：

| 状态 | 触发条件 |
|---|---|
| `incomplete-canonical-tree` | 缺 `canonical-node-ledger.md` 或 `canonical-edge-ledger.md` |
| `incomplete-recursive-tree` | 大量非叶子节点没有 child_ids，也没有 evidence_ids |
| `abstract-evidence-leaf` | evidence leaf 仍是“主结果、稳健性、机制检验、样本规则”等概括短语 |
| `incomplete-full-tree` | 缺 evidence ledger 或 evidence-expanded Mermaid |
| `needs-anchor` | 关键证据无法定位到段落、表格、脚注或文献 |
| `incomplete-mermaid-evidence-view` | evidence-expanded Mermaid 未覆盖关键底层 evidence，且没有说明渲染限制 |

## 推荐深度

实证论文至少达到：

```text
Y 贡献成立
<- X2 作者证明核心发现
<- P6 主结果支持核心发现
<- P6.1 表4列(2)核心交互项显著为负
<- E-R1b Peerdumy×POST = -0.0111***
```

而不是停在：

```text
表4主结果 -> 主结果成立
```
