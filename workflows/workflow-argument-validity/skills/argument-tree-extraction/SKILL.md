---
name: argument-tree-extraction
description: 通用论证树抽取与路由编排 Skill。用于把文本、论文、论效题、GRE argument、政策报告或商业论证抽成证据、子观点、中层命题、根结论的论证树，生成节点台账、箭头审计表、evidence ledger、evidence-expanded Mermaid 和链接索引，并路由到学术论文或考试论证树子 Skill。
---

# Argument Tree Extraction

## 定位

这是论证树抽取的通用抽象规则说明 + 路由/编排型 Skill。它保存跨文本类型稳定存在的抽树协议，并把专用场景路由到子 Skill：

```text
argument-tree-extraction
└── skills/
    ├── academic-paper-argument-tree-extraction
    ├── exam-argument-tree-extraction
    └── argument-tree-mermaid-rendering
```

不要把学术论文的 X1/X2/Y、论效题的限时作文、GRE 的 prompt instruction 全塞进父层。父入口只管共同协议、路线选择和最低完成标准。

复杂抽树任务不应期待单一子 Skill 一次性完成。父入口负责一条稳定主轴：

```text
task contract
-> argument spine
-> canonical node ledger
-> evidence ledger
-> canonical edge ledger
-> derived views
-> review sensitivity map
-> extraction QC
```

这条主轴是论证树对象从“未定义”到“可审计”的生命周期。每个环节只拥有自己产物的写权限，后续环节消费前序产物；如果发现前序缺口，写入 QC 或回退任务，而不是偷偷重复造轮子。

完整主轴规则见 [argument-tree-main-axis.md](references/argument-tree-main-axis.md)。

## 通用抽树协议

所有论证树都按这个方向恢复：

```text
E evidence / fact / quote / data
-> S subclaim
-> M middle claim
-> C root claim
```

默认用 Mermaid `flowchart BT`，箭头表示下层 supports 上层。

## Quick Tree 与 Full Tree

抽树任务必须先判断模式：

| 模式 | 适用场景 | 不足 |
|---|---|---|
| `quick-tree` | 临时讨论、快速定位、用户只问“这篇大概在证明什么” | 只能作为探索性草图，不能直接进入正式审稿、case 回测或专家意见对照 |
| `full-tree` | case 回测、正式审稿、投稿前自审、与专家意见对照、用户要求证据链 / Mermaid / Obsidian 链接 | 必须生成 evidence ledger 和 evidence-expanded Mermaid |

若任务属于 `full-tree` 场景，不得只输出简版 Mermaid 或概要树。缺少 evidence ledger 或 evidence-expanded Mermaid 时，必须标记：

```text
incomplete-full-tree
```

并暂停进入后续“验箭头 / 选问题”阶段，除非用户明确要求先用 quick-tree 临时推进。

## Full Tree 主轴状态机

`full-tree` 必须按以下状态推进，不能跳步：

| 状态 | 产物 | 拥有者 | 不做什么 |
|---|---|---|---|
| 0 定边界 | `task-contract.md` | 父入口 / orchestrator | 不抽树、不验箭头 |
| 1 抽主干 | `argument-spine.md` 或 `paper-argument-tree.md` 的 spine 部分 | 场景子 Skill | 不抽场景细证据 |
| 2 建节点 | `canonical-node-ledger.md` | 节点构建环节 | 不填满证据 |
| 3 证据下钻 | `evidence-ledger.md` | 证据环节 | 不重新设计树 |
| 4 建边 | `canonical-edge-ledger.md` | 边构建环节 | 不新增证据 |
| 5 生成视图 | `recursive-tree-master.md`、`evidence-expanded-mermaid.md`、`view-*.md` | 视图环节 | 不发明节点或证据 |
| 6 移交提示 | `extraction-qc.md` 中的 handoff hints | QC / handoff 环节 | 不生成 review-sensitivity-map，不写最终审稿意见 |
| 7 验收 QC | `extraction-qc.md` | QC 环节 | 不补正文分析 |

如果某一步无法完成，必须在 `extraction-qc.md` 标记：

```text
blocked-at-state-N
missing-input
incomplete-canonical-tree
incomplete-recursive-tree
abstract-evidence-leaf
missing-domain-evidence
missing-source-anchor
```

继续推进前应说明是“降级推进”还是“回退补抽”。

## 路由

| 场景 | 调用 |
|---|---|
| 学术论文、手稿、审稿项目 Markdown、PDF 还原稿 | `skills/academic-paper-argument-tree-extraction/SKILL.md` |
| 管综/经综论效题、GRE Analyze an Argument、考试型短材料 | `skills/exam-argument-tree-extraction/SKILL.md` |
| 普通政策/商业/局部论证 | 使用父层协议直接抽树，必要时再沉淀新子 Skill |

如果用户明确要求“论文贡献链、文献 gap、实证表格、Obsidian 链接”，优先走 academic 子 Skill。

如果用户明确要求“论效题、老王、审题、GRE assumptions/questions/evidence”，优先走 exam 子 Skill；若进一步要求选 3-4 个问题，抽树后交给 `../argument-issue-selection/skills/exam-argument-issue-selection/SKILL.md`。

## 最小输出

`quick-tree` 最小输出：

```text
root claim:
support chain:
node ledger:
Mermaid:
QC / unresolved anchors:
```

`full-tree` 最小输出：

```text
task-contract.md
argument-spine.md 或 paper-argument-tree.md 的 spine 部分
canonical-node-ledger.md
evidence-ledger.md
canonical-edge-ledger.md
recursive-tree-master.md
evidence-expanded-mermaid.md
link map or unresolved anchors
extraction-qc.md
```

`review-sensitivity-map.md` 不属于 `full-tree` 最小输出；它由后续 `academic-argument-arrow-audit` 生成。抽树阶段如发现可疑证据组合，只写入 `extraction-qc.md` 的 handoff hints。

## 节点台账

使用：

```text
node_id | node_label | node_type | parent | evidence_ids | status
```

`node_type` 可用：

```text
root
middle-claim
subclaim
evidence
implicit-premise
```

## 箭头审计

使用：

```text
arrow_id | from_node | to_node | support_type | status | why
```

`status` 可用：

```text
strong
weak
broken
unclear
not-yet-audited
```

抽树阶段可以先标 `not-yet-audited`；审查阶段再判断 weak / broken。

## Evidence Ledger

使用：

```text
evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点/箭头 | 证据粒度 | link
```

证据粒度：

```text
exact
summarized
needs-qc
```

不要把“作者说有证据”当成已核实证据。无法回到原文、图表、题干或文献时，标 QC。

证据下钻环节应由场景子 Skill 定义具体证据类型。父层只要求证据能回到可核源头。常见通用证据类型包括：

```text
text-evidence
data-evidence
definition-evidence
source-evidence
example-evidence
domain-specific-evidence
```

场景子 Skill 可进一步细化。例如学术论文可以定义 `table-cell-evidence`、`figure-evidence`、`citation-evidence`；考试论证题可以定义 `prompt-quote-evidence`、`implicit-assumption-evidence`。

父层不强制所有文本都有文献证据、表格证据或图像证据；但如果某一场景子 Skill 将其列为必需证据，缺失时必须在 QC 中标明。

## Mermaid 规则

Mermaid 生成属于派生视图环节。复杂、正式或需要高清图片的论证树，应调用：

```text
skills/argument-tree-mermaid-rendering/SKILL.md
```

最低规则：

1. 默认 `flowchart BT`，下层证据向上支撑；
2. Mermaid 必须从 `canonical-node-ledger.md`、`evidence-ledger.md`、`canonical-edge-ledger.md` 派生；
3. 节点 label 短，复杂内容放台账；
4. claim 与 evidence 必须有视觉区分；
5. `needs-qc` evidence 必须可见，不能被画成普通 verified evidence；
6. Mermaid 阅读视图的节点第一行必须是自然语言，编号只做回查锚点；
7. 只读 Mermaid 应能读出“证据 -> 子 claim -> 上层 claim -> 根结论”的逻辑；
8. 区分 `full-reading view` 和 `summary-reading view`：前者保留证据颗粒度，后者可以合并但必须标注；
9. 优先使用折线配置，如 `curve: "linear"` 或 `curve: "stepAfter"`，减少曲线缠绕；
10. 如果图过大，必须同时输出完整图和阅读分图；
11. 如果建立了 evidence ledger，关键 evidence node 必须画回 Mermaid，否则树在视觉上没有长叶子；
12. 如果输出 PNG，必须检查是否有文字；Mermaid SVG 经 `rsvg-convert` 可能出现“只有框没有字”的失败模式；
13. README 或日志必须说明优先打开哪个高清文件。

## 链接规则

可输出 link map：

```text
node_id | evidence_id | source_link | ledger_link | issue_link | status
```

链接可以是 Obsidian 双链、Markdown 标题链接、段落编号、块 ID、URL 或本地文件路径。无法稳定定位时写 `needs-anchor`。

## 子 Skill 分工

- `academic-paper-argument-tree-extraction`：长文本、图表、文献、模型、实证/理论/综述适配，重证据追溯。
- `exam-argument-tree-extraction`：短材料、限时审题、总论点/分论点/结构关键词和隐含假设，重速度与结构清晰。

复杂任务的子 Skill 协同原则：

- 子 Skill 可以负责某个状态的执行，但不能同时拥有多个状态的最终写权限；
- 如果子 Skill 既抽节点又抽证据，必须在输出中分清 node ledger 与 evidence ledger；
- Mermaid 生成只能消费 ledger，不能反向新增节点；
- 2B 显影只能消费 evidence ledger 和 QC，不能把审稿攻击写回作者树；
- 场景专属证据类型可以逐步抽成更小子 Skill，但父主轴不变。

## 回归测试纪律

本 Skill 是复合型父 Skill；任何父入口、主轴、路由、输出契约或子 Skill 分工改动，都可能影响 academic / exam / GRE 等分支。此类改动必须按 `workflow-tao` 的回归测试协议处理：

```text
../../workflow-tao/references/regression-test-protocol.md
```

核心要求：

- 父 Skill 改动后，列出受影响子分支；
- 每个受影响分支至少选择一个 smoke case；
- 由纯净 subAgent 执行回归，优先 `fork_context=false`；
- subAgent 只读测试输入、被测 Skill、必要 references/assets 和测试目标；
- 禁读修改讨论、人工期望、旧答案和无关 TASK；
- 将新产物与 baseline / target md 做质量对比；
- 产出 `regression-comparison.md`，判断增强、持平、退化或失败。

抽树父 Skill 的最小分支回归：

| 分支 | 回归目标 |
|---|---|
| academic | 仍能按学术主轴产出 full-tree，不丢 citation/table/figure 专属要求 |
| exam | 不被学术 full-tree 污染，仍保持考试材料的快速审题、找结论、拆论证和 issue selection 适配 |
| GRE | 不被中文论效或学术论文主轴污染，仍适配 GRE argument 的 assumptions/questions/evidence |

回归样本可先放在项目 TASK；重复使用后迁移到 `tests/fixtures/` 与 `tests/runs/`。

## 边界

- 父层不保存单篇论文、单道题、单个项目的固定判断。
- 父层不决定最终审稿意见或作文成稿。
- 父层不把所有 adapter 平铺；专用差异进入子 Skill。

## 资源

- `references/argument-tree-main-axis.md`：复杂抽树任务的主轴状态机、产物写权限和回退规则。
- `assets/task-contract-template.md`：full-tree 任务定边界模板。
- `skills/argument-tree-mermaid-rendering/SKILL.md`：论证树 Mermaid 视图、中文版图、高清渲染、分图、claim/evidence 视觉规范和渲染 QC。
- `tests/README.md`：抽树父 Skill 的回归测试说明和受影响分支清单。
