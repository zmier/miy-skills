# Tree V5 vs Blind Diagnosis

## 问题

用户指出：TASK01 中旧版 `paper-argument-tree.md` 的 V5 / V5.1 明显强于 TASK02 本轮盲跑生成的 `paper-argument-tree.blind.md`。

这个判断成立。

## 被比较对象

旧版强树：

```text
../TASK01-学术论文论证树迁移校准/outputs/paper-argument-tree.md
../TASK01-学术论文论证树迁移校准/outputs/evidence-ledger.md
```

本轮盲跑树：

```text
outputs/paper-argument-tree.blind.md
```

## 直接差异

| 维度 | TASK01 V5 / V5.1 | TASK02 blind |
|---|---|---|
| 输出形态 | `paper-argument-tree.md` + `evidence-ledger.md` + V5 evidence-expanded Mermaid | 只有 `paper-argument-tree.blind.md` |
| 证据粒度 | 表格、系数、显著性、变量定义、模型设定、样本规则、文献引用均进入 evidence node | 多数证据压缩成章节摘要和中层命题 |
| Mermaid | `E-* 具体证据 -> e 子观点 -> G/P 中层命题 -> X1/X2/Y` | `E* 摘要证据 -> G/R/M 节点 -> X1/X2/Y`，叶子不够细 |
| 样本规则 | 单独列出事件窗口、剔除同业重叠事件、首次事件、剔除事件公司、最终样本量 | 合并为“2007-2024 A股；同行业事件窗口；剔除事件公司自身” |
| 稳健性 | 堆叠 DID、Bacon、安慰剂、PSM/熵平衡、政策剔除、Oster、替换变量各自成为 evidence node | 这些检验合并成一个 R3 节点 |
| 机制证据 | CAR、正/负 CAR 组、关注组、监管距离、处罚次数等分别进入 evidence ledger | 机制证据有列出，但没有 ledger 化和逐项支撑关系 |
| QC | 明确标记哪些表格需要 table QC，哪些系数为 exact / summarized | 只有总括式 `needs-table-qc` |

## 为什么旧版更强

### 1. 旧版 V5 是多轮 case-calibration 结果，不是一次性盲跑结果

TASK01 的 UAT 记录显示，旧版树经历了 V1 -> V5.1 的逐轮修正：

```text
V3：要求中层节点继续展开
V4：要求作者论证树关键节点完整展开
V5：新增 evidence-ledger.md
V5.1：把 evidence-ledger 的 E-* 节点画回 Mermaid
```

这说明 V5 的强度来自“用户持续追问 + case 校准 + 反复修正”。它不是单次 blind run 自然生成的。

### 2. 本轮 TASK02 的验收物被收窄了

TASK02 说明中，抽树阶段只列了：

```text
outputs/paper-argument-tree.blind.md
```

而 `workflow-academic-argument-validity` 和 `academic-paper-argument-tree-extraction` 的完整输出契约其实要求：

```text
paper-argument-tree.md
evidence-ledger.md
evidence-expanded-mermaid.md
obsidian-link-map.md
extraction-qc.md
```

因此本轮执行时实际跑成了“主链轻量回测”，不是“完整抽树回测”。

### 3. Skill 本身已经写了完整要求，但执行没有完全落实

`academic-paper-argument-tree-extraction/SKILL.md` 已经明确要求：

```text
5. 建立 evidence ledger
6. 生成 evidence-expanded Mermaid
7. 生成 Obsidian 链接索引
```

`empirical-paper-adapter.md` 也明确要求表格证据记录：

```text
表号
列号
变量名
系数
t 值 / 标准误
显著性
样本量
固定效应
聚类层级
```

本轮弱的原因不是 Skill 没有这条规则，而是任务执行时没有把这些规则变成必交付文件。

### 4. workflow 中同时存在“最小输出”和“完整输出”，本轮走了最小路径

`workflow-academic-argument-validity/SKILL.md` 同时写了：

最小输出：

```text
一句话核心发现
X1 / X2 / Y
作者关键论证链
最可疑的 3-5 条箭头
```

完整输出：

```text
paper-argument-tree.md
evidence-ledger.md
evidence-expanded-mermaid.md
obsidian-link-map.md
academic-arrow-audit.md
review-issue-arrow-map.md
argument-validity-review-notes.md
extraction-qc.md
```

TASK02 是回测任务，理论上应该走完整输出。但实际由于任务说明只列了简化产物，执行时走成了最小路径。

### 5. 本轮没有把 TASK01 的经验作为 test fixture 约束

TASK01 的 `outputs/UAT.md` 已经明确：

```text
是否追溯到底层证据台账：pass after v5
底层证据是否画回 Mermaid：pass after v5.1
```

但 TASK02 没有把这两条作为强制回归标准。因此出现了“workflow 文档里有，实际盲跑却退化”的情况。

## 这不是模型能力问题，而是调用契约问题

更准确的判断是：

```text
旧版 v5 证明这套方法能抽出强树；
TASK02 证明当前 workflow 调用契约还不能稳定保证每次都抽出强树。
```

也就是说，问题不在“能不能做到”，而在“如何让它每次都必须做到”。

## 对后续修复的要求

### 修复 1：TASK / UAT 中区分 quick tree 与 full tree

建议固定两个模式：

| 模式 | 何时用 | 必交付 |
|---|---|---|
| quick tree | 临时讨论、快速定位 | 一句话发现、X/M/Y、简版 Mermaid、QC |
| full tree | case 回测、审稿正式输入、UAT | `paper-argument-tree.md`、`evidence-ledger.md`、`evidence-expanded-mermaid.md`、`extraction-qc.md` |

TASK02 这种“用欣媛 case 回测 workflow”的场景应默认 `full tree`。

### 修复 2：academic workflow 的步骤 2 要写明“回测/正式审稿不得只交简版树”

建议在 `workflow-academic-argument-validity/SKILL.md` 的步骤 2 增加：

```text
若任务是 case 回测、正式审稿、自审或用户要求与专家意见对照，
不得只输出简版 Mermaid；
必须至少交付 paper-argument-tree.md、evidence-ledger.md、evidence-expanded-mermaid.md、extraction-qc.md。
```

### 修复 3：academic-paper-argument-tree-extraction 要把 V5 作为 gold fixture

建议在 `academic-paper-argument-tree-extraction` 中增加：

```text
CASE-J-260110 TASK01 V5/V5.1 是当前学术论文抽树 gold fixture。
新任务如果输出比 V5 少 evidence ledger 或 evidence-expanded Mermaid，
应标记为 incomplete-full-tree。
```

### 修复 4：TASK02 应补跑 full tree v2

下一步可以在 TASK02 下新增：

```text
outputs/paper-argument-tree.full-v2.md
outputs/evidence-ledger.full-v2.md
outputs/evidence-expanded-mermaid.full-v2.md
outputs/extraction-qc.full-v2.md
```

然后再重新跑：

```text
academic-arrow-audit-table.full-v2.md
academic-selected-issues.full-v2.md
xinyuan-comparison.full-v2.md
```

这样才能真正测试：

```text
完整抽树 -> 完整验箭头 -> 选点
```

是否能接近欣媛意见。

## 一句话结论

TASK02 这次弱，不是因为 `academic-paper-argument-tree-extraction` 设计得不如旧版，而是因为本轮回测没有按旧版 V5 的完整交付契约执行；它只跑了简版树，导致后面的箭头审计和选点都失去了底层证据叶子。
