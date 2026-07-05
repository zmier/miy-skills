# Log

## 2026-06-20 ReAct：启动 paper 线盲跑回测

### Thought

用户希望回到 paper 线，测试新拆出的 `argument-issue-selection` 在学术论文审稿场景中是否可用。当前适合用欣媛 case 做回测：先冻结欣媛审稿意见，只读 manuscript，跑出作者树、全量箭头审计和选点，再解冻欣媛意见做对照。

### Action

创建：

```text
tasks/TASK02-学术论文论证workflow盲跑回测/
```

本轮先读取：

```text
../../inputs/manuscript.md
```

并按以下 Skill 链条执行：

```text
academic-paper-argument-tree-extraction
-> academic-argument-arrow-audit
-> academic-argument-issue-selection
```

### Observation

输入稿件含既有批注和疑问脚注，因此本轮标记为：

```text
review-frozen / manuscript-only / annotation-contaminated
```

### Reflection

本轮重点不是重新审稿，而是看新 workflow 拆层后的中间产物是否清楚：作者树是否只画作者树；验箭头是否只做全量诊断；选点是否从诊断表中选 major concern 候选。

## 2026-06-20 ReAct：解冻欣媛意见并对照

### Thought

blind outputs 已完成，可以打开 `../../inputs/xinyuan-review.txt` 做对照。重点看 workflow 自己抓到了哪些主问题、哪些问题只抓到大类但没有展开到底层证据、哪些问题完全漏掉。

### Action

生成：

```text
outputs/xinyuan-comparison.md
```

### Observation

盲跑抓住了五个主干方向：

```text
KV 测量
主动披露定义
识别可信度
机制解释
行业自律贡献上升
```

但欣媛意见更强在具体证据锚定：聚类层级、POST 时间结构、同业集中违规样本筛选、事件公司自身效应、图3与表11样本一致性、EFD 构造层级、表注错误等。

### Reflection

当前 paper workflow 可以做第一轮主干审稿，但距离强审稿意见还差“底层证据展开 / 表格脚注级 QC”。下一步应反哺：

```text
academic-paper-argument-tree-extraction
academic-argument-arrow-audit
```

## 2026-06-20 ReAct：追问为什么 TASK01 V5 强于 TASK02 blind

### Thought

用户指出旧版 V5 树比本轮 blind 树强很多。需要区分：这是模型能力差异，还是任务契约和输出验收物差异。

### Action

读取并对照：

```text
../TASK01-学术论文论证树迁移校准/outputs/paper-argument-tree.md
../TASK01-学术论文论证树迁移校准/outputs/evidence-ledger.md
../TASK01-学术论文论证树迁移校准/outputs/UAT.md
../TASK01-学术论文论证树迁移校准/outputs/workflow-feedback.md
outputs/paper-argument-tree.blind.md
TASK02-说明.md
```

生成：

```text
outputs/tree-v5-vs-blind-diagnosis.md
```

### Observation

TASK01 V5 / V5.1 的强度来自完整抽树契约：

```text
paper-argument-tree.md
evidence-ledger.md
evidence-expanded Mermaid
table / coefficient / variable / sample-rule / citation evidence nodes
```

TASK02 blind 只输出了单个简版 `paper-argument-tree.blind.md`，没有生成 evidence ledger 和 evidence-expanded Mermaid。因此它把很多底层证据压成中层摘要，后续验箭头自然弱。

### Reflection

这不是能力问题，而是调用契约问题。旧版 V5 证明方法可以做到；TASK02 暴露的是 full tree 与 quick tree 没有在任务验收中强制区分。后续应补跑 full tree v2，并把 TASK01 V5/V5.1 登记为 academic tree extraction 的 gold fixture。

## 2026-06-20 ReAct：修复 quick/full tree 契约

### Thought

用户进一步追问 workflow 和抽树 Skill 是否有责任。结论是：workflow 负责把回测、正式审稿、专家意见对照路由到 full tree；抽树 Skill 负责阻止简版树冒充完整树。本轮需要把这个责任分工写硬。

### Action

更新：

```text
../../../../skills/argument-tree-extraction/SKILL.md
../../../../skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/SKILL.md
../../../../subworkflows/workflow-academic-argument-validity/SKILL.md
../../../../skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/empirical-paper-adapter.md
```

### Observation

新增规则：

```text
quick-tree：临时讨论、快速定位。
full-tree：case 回测、正式审稿、投稿前自审、专家意见对照。
```

full-tree 必须交付：

```text
paper-argument-tree.md
evidence-ledger.md
evidence-expanded-mermaid.md
extraction-qc.md
```

若缺少 evidence ledger 或 evidence-expanded Mermaid，必须标记：

```text
incomplete-full-tree
```

并且不能作为正式输入进入后续验箭头和选点。

### Reflection

这次修复的目标是防止 TASK02 blind 这类退化再次发生：以后 paper line 的回测和正式审稿不能只产出简版树。

## 2026-06-20 ReAct：两步抽树 Skill 升级并跑 full-v2

### Thought

用户提出：抽树可能需要两步。第一步抽到 V5 那种作者证据树；第二步在证据树基础上进一步显影欣媛式敏感点。这个判断成立，需要写入 Skill 并用本 case 跑一版。

### Action

更新：

```text
../../../../skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/SKILL.md
../../../../subworkflows/workflow-academic-argument-validity/SKILL.md
../../../../skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/references/empirical-paper-adapter.md
```

新增输出：

```text
outputs/paper-argument-tree.full-v2.md
outputs/evidence-ledger.full-v2.md
outputs/evidence-expanded-mermaid.full-v2.md
outputs/review-sensitivity-map.full-v2.md
outputs/sensitivity-expanded-mermaid.full-v2.md
outputs/obsidian-link-map.full-v2.md
outputs/extraction-qc.full-v2.md
```

### Observation

full-v2 明确分为：

```text
2A 作者证据树
2B 审稿显影树
```

2A 复现 V5 的证据台账和证据叶子；2B 把低信息含量 vs 正 CAR、样本筛选 vs 代表性、POST 编码 vs 动态效应、公司层聚类 vs 处理层级、KV vs 行业自律等可疑组合显影出来。

### Reflection

这版比 blind tree 更适合作为后续验箭头输入。下一步应基于 full-v2 重跑箭头审计，而不是继续使用 `paper-argument-tree.blind.md`。
