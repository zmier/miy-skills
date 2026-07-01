# Workflow Feedback

## 来源

- case：`CASE-J-260110-xinyuan-review`
- TASK：`TASK01-学术论文论证树迁移校准`
- 证据：
  - `inputs/manuscript.md`
  - `inputs/xinyuan-review.txt`
  - `outputs/paper-argument-tree.md`
  - `outputs/review-issue-arrow-map.md`
  - `references/dialogues/001-004`

## 可反哺规则 1：学术论文顶层论证树

### 规则

学术论文审稿应先恢复：

```text
X1：问题有意义
+ X2：作者证明了核心发现
-> Y：论文值得发表 / 贡献成立
```

其中：

```text
gap + importance + novelty + unresolved puzzle -> X1
theory + measurement + data + identification + results + robustness/mechanism -> X2
X1 + X2 + actually answers gap -> Y
```

### 证据

J-260110 中，作者的问题具有一定新颖性，但欣媛意见主要削弱 `X2`：理论前提、样本筛选、变量测量、识别设定、机制排除和稳健性都不足以支撑“主动披露违规提升同行披露质量”这一核心发现。

### 建议落点

- `workflow-argument-validity/SKILL.md`：作为学术审稿领域适配核心图式；
- 新子 workflow：`subworkflows/workflow-academic-review-argument/`；
- `academic-review-argument-audit/SKILL.md`：作为 adapter 的入口规则。

## 可反哺规则 2：major concern 必须绑定断裂箭头

### 规则

学术审稿中的 major concern 不应只标为“变量问题”“方法问题”“机制问题”，而应记录：

```text
review issue -> target arrow -> weakened node -> impact on Y
```

### 证据

欣媛意见中的聚类层级、POST 定义、样本筛选、KV 指标、机制排除等问题，看似属于不同模块，但共同削弱：

```text
F1/F2/F3/F4/F6/F7 -> X2
X2 -> Y
```

### 建议落点

- `workflow-academic-review-argument` 输出契约；
- `academic-review-argument-audit` 输出增加 `review-issue-arrow-map.md`。

## 可反哺规则 2b：学术论文论证树必须命题化

### 规则

学术论文论证树不能只写模块节点：

```text
变量测量
识别策略
稳健性
机制检验
```

而应改写为可检验命题与箭头：

```text
KV 指数变化 -> 信息披露质量改善
公司层面聚类后的显著结果 -> DID 识别可信
常规稳健性通过 -> 核心威胁已被回应
处罚不显著 -> 信息传导机制不存在
```

### 证据

TASK01 v1 的树能区分 X1/X2/Y，但 F2/F4/F6 等节点仍偏模块名。经人工复核后，v2 改为 `P1-P9` 命题树和 `A1-A13` 箭头表，才更接近论效题的“作者用 A 推出 B，但 A 不足以推出 B”。

### 建议落点

- `workflow-academic-review-argument` 最小输出：
  - `paper-argument-tree.md`;
  - `argument-arrow-table.md`;
  - `review-issue-arrow-map.md`。
- 父 workflow `references/argument-tree-core.md` 可补一句：领域节点应尽量命题化，不停留在模块名。

## 可反哺规则 2c：X2 必须还原核心发现句

### 规则

`X2：作者做出来了` 只能作为验收标签，不能作为最终节点内容。学术论文论证树必须先写出作者声称自己做出的核心发现：

```text
哪个 X
通过什么机制 M
影响哪个 Y
是否还有 Y2 / 政策或贡献上升
```

最低输出：

```text
一句话发现：
X / M / Y / Y2 表：
核心发现箭头：
```

### 证据

TASK01 v2 初版仍写作 `X2: 作者做出来了`，用户指出这里更应看到“作者具体做出什么来了，哪几个 X 影响哪几个 Y”。修正后，X2 被还原为：

```text
上市公司主动披露违规
-> 通过声誉竞争和市场压力
-> 提升同行业其他企业的信息披露质量
-> 进而引导行业自律发展
```

并结构化为 X、Y1、M1、M2、M3、Z1、Y2。

### 建议落点

- `workflow-academic-review-argument` 的 `paper-argument-tree.md` 模板；
- `academic-review-argument-audit` 的审查流程第一步；
- 父 workflow `argument-tree-core.md` 的学术论文默认根结构。

## 可反哺规则 2d：中层命题必须继续展开

### 规则

学术论文论证树不能停在中层命题，例如：

```text
G1 信息披露监管重要
P5 样本能代表机制相关事件
P8 稳健性回应核心威胁
```

每个关键中层命题都要继续展开：

```text
底层论据 / 原文事实 / 表格结果 / 文献引用
-> 子观点
-> 中层命题
-> 上层命题
```

### 证据

用户指出 G1、P5、P8 仍缺少论据和箭头。TASK01 v3 将其展开为：

```text
证券法修订 + 处罚提高 + 违规仍多 + 事前预防监管
-> G1 信息披露监管重要

剔除同业重叠事件 + 保留行业首次事件 + 剔除事件公司自身样本 + 常规样本清洗
-> 干净同行溢出样本
-> P5 样本能代表机制相关事件

堆叠 DID + Bacon + 安慰剂 + PSM/熵平衡 + 政策剔除 + Oster + 替换变量
-> 结果稳健
-> P8 稳健性回应核心威胁
```

### 建议落点

- `workflow-academic-review-argument` 的论证树模板；
- `argument-tree-core.md` 的完成标准；
- `review-issue-arrow-map.md` 必须允许同一中层节点拆出多个底层箭头。

### V4 追加

TASK01 V4 将“中层节点必须继续展开”进一步具体化为最低覆盖：

```text
X1: G1-G4
X2: P1-P8
Y: X1 + X2 + P9
```

学术论文论证树模板不能只展开被审稿人攻击的节点；至少要覆盖作者顶层贡献链中的所有关键支撑节点。否则审稿攻击虽然清楚，但作者原本的论证结构仍不完整。

## 可反哺规则 2e：学术论文论证树必须有 evidence ledger

### 规则

学术论文的作者论证树不能只停在命题节点，还必须建立底层证据台账：

```text
evidence node
-> subclaim
-> X1 / X2 / Y
```

底层证据至少包括：

```text
表格结果
系数
显著性
变量定义
模型设定
文献引用
原文段落
```

建议使用字段：

```text
evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点/箭头 | 证据粒度
```

其中 `证据粒度` 应区分：

```text
exact
summarized
needs-table-qc
```

如果 restored Markdown 没有保存具体表格值，必须标记 `needs-table-qc`，不能臆造系数、t 值、标准误、显著性或样本量。

### 证据

TASK01 v4 已经展开 G1-G4、P1-P9，但用户进一步指出：真正的论证树应继续追到表格、显著性和具体引用等底层证据。V5 因此新增 `outputs/evidence-ledger.md`。

例如：

```text
Table 4 column (2) 系数 -0.0111
-> EPS 提升
-> P4: Y1 可被 KV 变化捕捉
-> X2: 主动披露违规通过声誉竞争和市场压力提升同行披露质量
```

又如：

```text
Karpoff et al. (2008); Armour et al. (2017)
-> 违规披露研究多关注违规者自身
-> G2: 文献 gap 存在
-> X1: 问题有意义
```

### 建议落点

- 父 workflow `references/argument-tree-core.md`：增加 evidence ledger 完成标准；
- `workflow-argument-validity/SKILL.md`：结构化输出增加 evidence ledger；
- `academic-review-argument-audit/SKILL.md`：学术审稿 adapter 强制输出底层证据台账；
- 后续子 workflow `workflow-academic-review-argument`：将 `evidence-ledger.md` 设为最小输出之一。

## 可反哺规则 2f：作者树与审稿攻击树分离

### 规则

`paper-argument-tree.md` 只保存作者自己的论证树：

```text
作者论据 -> 作者子观点 -> 作者核心发现 -> 作者贡献声称
```

不要把审稿人的攻击、削弱、修改建议直接画进这棵树。否则一张图同时包含“作者支撑方向”和“审稿反驳方向”，会让 Mermaid 图过乱，也会混淆证据层级。

审稿攻击应放在独立输出中：

```text
review-issue-arrow-map.md
```

必要时后续可以另建：

```text
critique-tree.md
```

### 证据

TASK01 v3 初版把欣媛审稿节点画进作者论证树，用户指出这会让树变乱。修正后，`paper-argument-tree.md` 只保留作者论证，`review-issue-arrow-map.md` 负责说明欣媛如何攻击具体箭头。

### 建议落点

- `workflow-academic-review-argument` 的输出契约；
- `mermaid-obsidian-rules.md` 的图层规则；
- `argument-tree-core.md` 的边界说明。

## 可反哺规则 2g：抽作者树应独立成 Skill

### 规则

学术论文作者论证树抽取已经不再只是审稿 adapter 的一个步骤，而是可复用的独立能力。它应先于审稿攻击执行，专门产出：

```text
paper-argument-tree.md
evidence-ledger.md
evidence-expanded-mermaid.md
obsidian-link-map.md
extraction-qc.md
```

审稿攻击再基于作者树生成：

```text
review-issue-arrow-map.md
```

### 证据

TASK01 从 V1 到 V5.1 的迭代显示，抽作者树至少包括：

```text
一句话核心发现
X/M/Y/Y2
X1/X2/Y 顶层结构
中层命题完整展开
底层 evidence ledger
evidence-expanded Mermaid
Obsidian 双链 / 图表 / 文献回溯
```

这些工作已经超过普通审稿 issue 检查，应独立封装。

### 已落点

先创建过：

```text
workflow-argument-validity/skills/academic-paper-argument-tree-extraction/
```

后续按“父 Skill / 子 Skill”原则重构为：

```text
workflow-argument-validity/skills/argument-tree-extraction/
└── skills/
    ├── academic-paper-argument-tree-extraction/
    └── exam-argument-tree-extraction/
```

该结构采用：

```text
argument-tree-extraction
-> 保存通用节点/箭头/evidence/Mermaid/link map 协议

academic-paper-argument-tree-extraction
-> empirical-paper-adapter
-> theory-paper-adapter
-> conceptual-review-adapter
-> obsidian-evidence-linking helper

exam-argument-tree-extraction
-> management-exam-adapter
-> gre-argument-adapter
```

父 workflow 和 orchestrator 已登记最终结构：整篇抽树先进入 `argument-tree-extraction`，再由该 Skill 路由到 academic 或 exam 子 Skill；审稿攻击和段落写作再调用 `academic-review-argument-audit`。

## 可反哺规则 2h：学术论文应有独立子 workflow

### 规则

学术论文在 `workflow-argument-validity` 中不应只表现为零散 Skills。它需要一个独立子 workflow 来串联：

```text
读稿抓论证
-> 画作者论证树
-> 验箭头/找断点
-> 组织审稿或自审问题
-> 写成审稿/自审素材
-> 回归沉淀
```

其中 `evidence-ledger.md`、`evidence-expanded-mermaid.md`、`obsidian-link-map.md` 是“画作者论证树”的承载物；`review-issue-arrow-map.md` 是“组织审稿或自审问题”的承载物。它们很重要，但不应全部升格为主流程节点，否则学术论文子 workflow 会比论效题子 workflow 更散、更重，失去“抓论证 -> 画树 -> 验箭头 -> 成文”的清晰主轴。

### 证据

TASK01 显示，学术论文论证有效性分析同时需要：

- 长文本作者树；
- 表格、系数、变量、文献和原文证据追溯；
- 学术专属箭头审计；
- 审稿攻击与作者树分离；
- 输出到审稿意见或写作自审。

这已经超过单个 adapter 的职责，也不同于论效题子 workflow。

### 已落点

已创建：

```text
workflow-argument-validity/subworkflows/workflow-academic-argument-validity/
```

该子 workflow 不替代 `workflow-paper-writing-review`，只承载“论文作为论证”的主轴。

### 已修正

2026-06-20 已将 `workflow-academic-argument-validity/SKILL.md` 与 `workflow-exam-argument-validity/SKILL.md` 对齐为六步主流程，并把证据台账、expanded Mermaid、issue arrow map 降回对应步骤的输出承载。

## 可反哺规则 2i：验箭头与选问题必须分离

### 规则

论证 workflow 中应区分两个阶段：

```text
验箭头 = 诊断层
选问题 = 决策层
```

验箭头阶段负责尽量全量、忠实地判断：

```text
A -> B 是否推得动
status = strong / weak / broken / unclear / needs-qc
```

选问题阶段才负责从所有断点中决定：

```text
这次写哪些
哪些作为 major concern
哪些作为 minor concern
哪些暂时记录但不写
```

### 理由

- 验箭头追求覆盖和忠实；
- 选问题追求优先级、表达策略、篇幅控制和任务匹配；
- 如果在验箭头阶段就选问题，容易把“没选中”误认为“没有问题”；
- 如果在选问题阶段重新验箭头，容易把写作偏好倒灌进诊断结果。

### 已落点

已创建：

```text
workflow-argument-validity/skills/argument-issue-selection/
```

并拆出：

```text
skills/argument-issue-selection/skills/exam-argument-issue-selection/
skills/argument-issue-selection/skills/academic-argument-issue-selection/
```

同步修正：

```text
argument-arrow-audit
-> 只负责全量验箭头

argument-issue-selection
-> 负责选 3-4 个可写问题 / major concern / revision action

academic-review-argument-audit
-> 负责把已选问题写成审稿语言
```

## 可反哺规则 3：结果必须回应 gap

### 规则

即使研究问题有意义，实证结果也需要真正回应作者声称的 gap。审稿时应检查：

```text
finding holds
+ finding answers the claimed gap
-> contribution holds
```

### 证据

J-260110 中，即使短期 KV 指标变化成立，也未必足以回应“行业自律发展”这一更宏大的贡献叙事。

### 建议落点

- `workflow-argument-validity` 的学术论文领域适配原则；
- `academic-review-argument-audit` 的 gap/contribution 检查。

## 可反哺规则 4：case-derived patterns 增加 tree location

### 规则

每个 case-derived review pattern 应标注默认树上位置：

```text
default tree location: X1 / X2 / Y / output-layer
```

### 证据

TASK01 显示：

- story premise consistency -> X2 theory/mechanism；
- sample exclusion -> X2 data/sample；
- direct effect baseline -> X2 mechanism；
- mechanism-exclusion reversal -> X2 mechanism；
- robustness core threats -> X2 robustness；
- tone downgrade -> output layer。

### 建议落点

- `skills/academic-review-argument-audit/references/case-derived-review-patterns.md`

## 暂不反哺内容

| 内容 | 原因 |
|---|---|
| J-260110 的 KV 指标具体判断 | 领域和个案依赖 |
| 对“主动披露违规”的具体定义建议 | 个案研究设计建议 |
| 欣媛审稿意见的高压措辞 | 只迁移结构，不迁移语气 |
| 对 J-260110 的最终推荐意见 | 保密且不属于 workflow 能力 |

## 建议下一步

创建学术论文论证树子 workflow：

```text
workflow-argument-validity/
  subworkflows/
    workflow-academic-review-argument/
      SKILL.md
      references/
      assets/
      tests/
```

初始职责：

```text
恢复学术论文 X1/X2/Y 论证树
-> 映射 major concerns 到断裂箭头
-> 输出 review issue arrow map
-> 决定哪些问题进入审稿意见
```
