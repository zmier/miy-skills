# TASK01 Log

## 2026-06-19 ReAct：创建学术论文论证树迁移校准 TASK

### Thought

用户希望暂时不以 `workflow-paper-writing-review` 为主轴，而是从 `workflow-argument-validity` 自己长出学术论文审稿迁移路线。现有 `CASE-J-260110-xinyuan-review` 已包含欣媛审稿意见与稿件证据，因此适合在该 case 下开子 TASK，而不是另起大 project。

### Action

创建 `tasks/TASK01-学术论文论证树迁移校准/`，并加入 `inputs/`、`outputs/`、`docs/`、`cache/`、`logs/`。新增 TASK 说明、验收契约、输入索引、手工审读协议和 ReAct 日志。

### Observation

本 TASK 的目标被限定为：

```text
稿件 -> X1/X2/Y 论证树
欣媛审稿意见 -> 断裂箭头映射
断裂箭头 -> workflow / adapter 反哺建议
```

### Reflection

下一步应运行本 TASK：读取 dialogue 001/002/004、既有 argument map、稿件和欣媛意见，产出 `paper-argument-tree.md` 与 `review-issue-arrow-map.md`。本 TASK 是 prior-exposed calibration，不作为 strict blind。

## 2026-06-19 ReAct：运行 TASK01 并完成 UAT

### Thought

本 TASK 的关键不是复述欣媛审稿意见，而是验证真实审稿意见能否被映射回学术论文的 `X1 + X2 -> Y` 论证树。如果能映射，说明 `workflow-argument-validity` 可以从论效题/GRE 小树迁移到学术论文大树。

### Action

读取既有 case 输出、稿件和欣媛审稿意见，产出：

```text
outputs/paper-argument-tree.md
outputs/review-issue-arrow-map.md
outputs/adapter-gap-analysis.md
outputs/workflow-feedback.md
outputs/UAT.md
```

### Observation

欣媛意见中的 12 条主要问题均可映射到论文论证树上的支撑箭头。多数问题削弱 `X2: 作者证明了核心发现`，并通过 `X2 -> Y` 影响最终贡献成立。

### Reflection

UAT 结果为 `pass / case-calibration-green / subworkflow-recommended`。建议下一步创建 `workflow-academic-review-argument` 子 workflow，并将本 TASK 作为 seed case。

## 2026-06-19 ReAct：v2 复核论证树质量

### Thought

用户指出 `paper-argument-tree.md` 的 v1 虽然有 X1/X2/Y 顶层结构，但仍有模块树倾向：F2/F4/F6 等节点像“变量、识别、稳健性”模块名，不像论效题里的可检验命题。这个判断成立。

### Action

将 `paper-argument-tree.md` 升级为 V2 命题化论证树，并将 `review-issue-arrow-map.md` 增补为论效式箭头审查表：

```text
arrow_id | from_node | to_node | 作者如何论证 | 欣媛如何质疑 | 影响 X1/X2/Y
```

同时更新 `adapter-gap-analysis.md`、`workflow-feedback.md` 和 `UAT.md`。

### Observation

V2 将模块节点改写成具体箭头，例如：

```text
KV 变化 -> 信息披露质量改善
同行披露质量短期改善 -> 行业自律发展
公司层面聚类后的显著结果 -> DID 识别可信
处罚不显著 -> 信息传导机制不存在
```

### Reflection

学术论文版论证树子 workflow 的最小输出应强制包含“命题树 + 箭头表”。否则会退回传统审稿模块 checklist，无法真正继承论效题方法。

## 2026-06-19 ReAct：v2.1 还原 X2 核心发现句

### Thought

用户指出 `X2: 作者做出来了` 仍然只是概述，学术论文论证树中应先看到作者具体声称自己做出了什么：哪几个 X 通过什么机制影响哪几个 Y。这个反馈进一步提升了树的可读性和可审查性。

### Action

更新 `paper-argument-tree.md`：

```text
X2-core：作者声称的核心发现
X / Y1 / M1 / M2 / M3 / Z1 / Y2 结构表
```

同步更新 `review-issue-arrow-map.md`、`workflow-feedback.md` 和 `UAT.md`。

### Observation

X2 被明确为：

```text
上市公司主动披露违规
-> 通过声誉竞争和市场压力
-> 提升同行业其他企业的信息披露质量
-> 进而引导行业自律发展
```

### Reflection

后续 `workflow-academic-review-argument` 的模板必须要求输出“一句话发现”和 X/M/Y 表。否则顶层论证树虽有 X1/X2/Y，但读者仍不知道作者到底声称自己发现了什么。

## 2026-06-19 ReAct：v3.1 分离作者树和审稿攻击

### Thought

用户指出“欣媛怎么攻击的”不应直接放到作者论证树上，否则会乱。这个判断成立：作者论证树和审稿攻击图是两个方向不同的图层。

### Action

清理 `paper-argument-tree.md`：

- 删除 Mermaid 中的欣媛攻击节点；
- 删除 G/P 展开表中的“欣媛质疑”列；
- 将攻击、削弱和断点说明迁移到 `review-issue-arrow-map.md` 承接；
- 更新 `workflow-feedback.md` 和 `UAT.md`，固定“作者树与审稿攻击树分离”的规则。

### Observation

现在 `paper-argument-tree.md` 只表达：

```text
作者论据 -> 作者子观点 -> 作者核心发现 -> 作者贡献声称
```

`review-issue-arrow-map.md` 表达：

```text
审稿意见 -> target arrow -> weakened node -> impact
```

### Reflection

后续 `workflow-academic-review-argument` 至少需要两份图/表：作者论证树和审稿箭头映射。不要把二者揉成一张 Mermaid。

## 2026-06-19 ReAct：v4 完整展开作者论证树

### Thought

用户要求继续做“完整展开论证树”。此前 v3 只示范性展开 G1、P5、P8，还不算完整。

### Action

在 `paper-argument-tree.md` 新增 `V4：完整展开论证树`，系统展开：

```text
G1-G4
P1-P9
Y 汇合箭头
V4 Mermaid 完整展开骨架
```

同步更新 `UAT.md` 和 `workflow-feedback.md`。

### Observation

V4 仍保持图层分离：只放作者自己的底层论据、子观点、中层命题和上层贡献声称，不放欣媛攻击节点。

### Reflection

后续子 workflow 的模板应要求：作者论证树至少完整展开 X1 的 G 节点、X2 的 P 节点和 Y 的汇合节点；审稿攻击再用独立 map 映射回这些箭头。

## 2026-06-19 ReAct：v5 底层证据台账与 workflow/SKILL 反哺

### Thought

用户指出 v4 虽然已经完整展开 G1-G4、P1-P9，但仍没有真正展开到“底层证据”：具体表格、系数、显著性、变量定义、模型设定和文献引用。这个反馈成立。学术论文论证树如果不能追到 evidence node，就仍然可能停留在中层命题。

### Action

新增：

```text
outputs/evidence-ledger.md
```

并同步更新：

```text
outputs/paper-argument-tree.md
outputs/UAT.md
outputs/workflow-feedback.md
outputs/adapter-gap-analysis.md
TASK01-说明.md
```

同时将规则反哺到正式 workflow / SKILL：

```text
workflow-argument-validity/references/argument-tree-core.md
workflow-argument-validity/SKILL.md
workflow-argument-validity/skills/academic-review-argument-audit/SKILL.md
workflow-argument-validity/skills/argument-workflow-orchestrator/SKILL.md
workflow-argument-validity/assets/mermaid-argument-tree-template.md
workflow-argument-validity/references/mermaid-obsidian-rules.md
workflow-argument-validity/tests/argument-validity-fixtures.md
```

### Observation

`evidence-ledger.md` 现在把证据记录为：

```text
evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点/箭头 | 证据粒度
```

并将证据粒度分为：

```text
exact
summarized
needs-table-qc
```

其中 `needs-table-qc` 用于标记 restored Markdown 没有保存具体表格值的情况。不得臆造系数、t 值、标准误、显著性或样本量。

### Reflection

学术论文论证树的最低完成标准应升级为：

```text
一句话核心发现
+ X/M/Y/Y2 结构表
+ 作者命题树
+ 底层证据台账
+ 审稿攻击映射
```

这使 `workflow-argument-validity` 从“能画树”推进到“能追证据、验箭头、写审稿意见”。

## 2026-06-19 ReAct：v5.1 将 evidence node 画回 Mermaid 树

### Thought

用户指出“树变茂盛了吗？没看到”。复核后发现：V5 已经新增 `evidence-ledger.md`，但 `paper-argument-tree.md` 中的可视化 Mermaid 仍主要停留在 V4 骨架；证据叶子虽然在台账里，却没有画回树上。这个反馈成立。

### Action

在 `paper-argument-tree.md` 的 V5 部分新增：

```text
V5 Mermaid：证据叶子展开图
```

用 `E-G*`、`E-P*` 节点显式表达：

```text
具体证据
-> 子观点
-> 中层命题
-> X1 / X2 / Y
```

并同步更新 `UAT.md`。

### Observation

现在读者不只可以在 `evidence-ledger.md` 中看到底层证据，也能在 Mermaid 图里看到证据叶子如何支撑 G/P 节点，再汇入 X1/X2/Y。

### Reflection

后续 workflow 的验收不应只要求“建立 evidence ledger”，还应检查：关键 evidence node 是否已经以可视化方式回填到论证树，至少形成一个可读的 evidence-expanded view。

## 2026-06-19 ReAct：创建 academic-paper-argument-tree-extraction Skill

### Thought

用户指出当前抽树效果已经不错，但这套能力不应继续停留在 TASK 临场组合中。它应独立成 Skill，并支持实证论文、理论论文和综述/概念论文的不同适配；同时要支持 Obsidian 双链，把证据节点链接回稿件图表、文献笔记和后续审稿 issue。

### Action

创建：

```text
workflow-argument-validity/skills/academic-paper-argument-tree-extraction/
```

并加入：

```text
SKILL.md
references/empirical-paper-adapter.md
references/theory-paper-adapter.md
references/conceptual-review-adapter.md
references/obsidian-evidence-linking.md
assets/paper-argument-tree-template.md
assets/evidence-ledger-template.md
assets/obsidian-link-map-template.md
agents/openai.yaml
```

同步更新父 workflow：

```text
workflow-argument-validity/SKILL.md
skills/argument-workflow-orchestrator/SKILL.md
tests/argument-validity-fixtures.md
```

### Observation

新的调用关系为：

```text
academic-paper-argument-tree-extraction
-> 抽作者树、证据台账、evidence-expanded Mermaid、Obsidian 链接

academic-review-argument-audit
-> 在作者树基础上做审稿攻击、断裂箭头映射和审稿段落
```

官方 `quick_validate.py` 使用 `Writer/.venv/bin/python` 成功执行，结果为：

```text
Skill is valid!
```

`agents/openai.yaml` 也已用同一环境重新生成。

### Reflection

这一步把“从欣媛 case 中长出来的成熟雏形”正式固化为可复用 Skill。后续应使用一篇未参与提炼的新实证论文做 forward-test，再根据失败点补强 adapter 和模板。

## 2026-06-19 ReAct：抽出 argument-tree-extraction 父 Skill

### Thought

用户进一步指出：学术论文抽树和论效题抽树的差异，不只是 adapter 能解决；二者任务目标、输入形态和输出形态都不同。更合理的结构是把共同抽树协议抽成父 Skill，再把 academic 和 exam 作为父 Skill 的 `skills/` 子 Skill，而不是平铺在 workflow 顶层。

### Action

创建父 Skill：

```text
workflow-argument-validity/skills/argument-tree-extraction/
```

并将学术论文抽树 Skill 迁入：

```text
workflow-argument-validity/skills/argument-tree-extraction/skills/academic-paper-argument-tree-extraction/
```

新增考试型抽树子 Skill：

```text
workflow-argument-validity/skills/argument-tree-extraction/skills/exam-argument-tree-extraction/
```

同步更新：

```text
workflow-argument-validity/SKILL.md
skills/argument-workflow-orchestrator/SKILL.md
tests/argument-validity-fixtures.md
outputs/workflow-feedback.md
```

### Observation

最终结构变为：

```text
argument-tree-extraction
├── 通用节点/箭头/evidence/Mermaid/link map 协议
└── skills
    ├── academic-paper-argument-tree-extraction
    └── exam-argument-tree-extraction
```

其中 academic 子 Skill 负责长文本、论文类型 adapter、图表文献和 Obsidian 回溯；exam 子 Skill 负责短文本审题、总论点/分论点、隐含假设、断点候选和 GRE prompt instruction。

三项 Skill 均使用 `Writer/.venv/bin/python` 通过官方校验：

```text
workflow-argument-validity: Skill is valid!
argument-workflow-orchestrator: Skill is valid!
argument-tree-extraction: Skill is valid!
academic-paper-argument-tree-extraction: Skill is valid!
exam-argument-tree-extraction: Skill is valid!
academic-review-argument-audit: Skill is valid!
argument-validity-audit: Skill is valid!
```

### Reflection

这比“一个 academic Skill 伪装成通用 Skill”更稳。父层保留真正通用的抽树协议，专用性由子 Skill 承担；子 Skill 内部再用 adapter/reference 处理更细分的场景。

## 2026-06-19 ReAct：将 argument-tree-extraction 去 core 化命名

### Thought

用户指出 `argument-tree-extraction-core` 这个名字不准确：它现在不是底层库式 core，而是通用抽象规则说明 + 路由/编排型 Skill。该判断成立。

### Action

将目录和 Skill 名从：

```text
argument-tree-extraction-core
```

改为：

```text
argument-tree-extraction
```

同步更新：

```text
SKILL.md frontmatter
agents/openai.yaml
workflow-argument-validity/SKILL.md
skills/argument-workflow-orchestrator/SKILL.md
tests/argument-validity-fixtures.md
outputs/workflow-feedback.md
```

### Observation

最终结构为：

```text
argument-tree-extraction
├── SKILL.md
├── references
├── assets
└── skills
    ├── academic-paper-argument-tree-extraction
    └── exam-argument-tree-extraction
```

`argument-tree-extraction` 的定位已改为通用抽树与路由编排 Skill，不再称为 core。

### Reflection

这更符合 workflow-tao 对 composite skill 的定义：父入口负责目标、抽象协议、路由和完成标准；子 skills 负责具体文本类型和输出形态执行。

## 2026-06-19 ReAct：补充 workflow-academic-argument-validity 子 workflow

### Thought

用户追问 `workflow-argument-validity` 下的论文子 workflow 是否也需要调整。复核后确认：学术论文能力已经有抽树、验箭头和审稿 adapter，但 Subworkflows 里只有论效题子 workflow，缺少把学术论文论证有效性流程串起来的子 workflow。

### Action

创建：

```text
subworkflows/workflow-academic-argument-validity/
```

并加入：

```text
SKILL.md
references/academic-workflow-routing.md
assets/academic-argument-workflow-output-template.md
```

同步更新：

```text
workflow-argument-validity/SKILL.md
skills/argument-workflow-orchestrator/SKILL.md
tests/argument-validity-fixtures.md
outputs/workflow-feedback.md
```

### Observation

新的学术论文子 workflow 编排：

```text
academic-paper-argument-tree-extraction
-> academic-argument-arrow-audit
-> academic-review-argument-audit
```

并明确边界：它只承载“论文作为论证”的主轴，不复制 `workflow-paper-writing-review` 的项目归档、PDF 还原、文献检索和最终审稿表流程。

### Reflection

现在 `workflow-argument-validity` 的结构更对称：论效题有 exam 子 workflow，学术论文也有 academic 子 workflow；二者共享抽树和验箭头父 Skill，但输出目标和业务边界不同。

## 2026-06-20 ReAct：学术论文子 workflow 与论效题六步主轴对齐

### Thought

用户指出学术论文子 workflow 的主流程“固定任务边界 -> 抽作者论证树 -> 建 evidence ledger -> 画 evidence-expanded Mermaid -> 验箭头 -> 生成 issue arrow map -> 输出审稿/自审素材”过于复杂，不如 exam 子 workflow 清晰。复核后确认：这里把主任务、技术承载和中间产物混成了同一层级。

### Action

将 `subworkflows/workflow-academic-argument-validity/SKILL.md` 改为与 exam 子 workflow 同构的六步轴：

```text
读稿抓论证
-> 画作者论证树
-> 验箭头/找断点
-> 组织审稿或自审问题
-> 写成审稿/自审素材
-> 回归沉淀
```

并明确：

```text
evidence-ledger.md / evidence-expanded-mermaid.md / obsidian-link-map.md
-> 属于“画作者论证树”的承载物

review-issue-arrow-map.md
-> 属于“组织审稿或自审问题”的承载物
```

### Observation

现在 academic 子 workflow 和 exam 子 workflow 都共享父层动作：

```text
恢复论证树 -> 检查支撑箭头 -> 标注断点影响 -> 输出可读文本
```

差异只保留在领域适配层：exam 走“审题/选点/成文/练习回归”，academic 走“读稿/作者树/学术验箭头/审稿或自审素材/案例沉淀”。

### Reflection

这次修正把“功能完整”重新压回“主轴清晰”。workflow 型 Skill 的主流程应描述人脑和 agent 的工作推进顺序；台账、Mermaid、link map、issue map 是重要产物，但应挂在相应步骤下面，而不是抢主轴位置。

## 2026-06-20 ReAct：抽出 argument-issue-selection

### Thought

用户指出“验箭头”和“选问题”不应放在同一个 Skill 里：验箭头应基于逻辑谬误和支撑关系，把所有关键箭头全量诊断一遍；下一环节再从诊断结果中选择重点阐述哪些问题。这个判断成立，因为二者分属诊断层和决策层。

### Action

创建：

```text
skills/argument-issue-selection/
├── SKILL.md
├── references/issue-selection-principles.md
├── assets/selected-issues-template.md
└── skills
    ├── exam-argument-issue-selection
    └── academic-argument-issue-selection
```

同步更新：

```text
workflow-argument-validity/SKILL.md
skills/argument-workflow-orchestrator/SKILL.md
skills/argument-arrow-audit/SKILL.md
skills/argument-arrow-audit/skills/exam-argument-arrow-audit/SKILL.md
skills/argument-arrow-audit/skills/academic-argument-arrow-audit/SKILL.md
subworkflows/workflow-exam-argument-validity/SKILL.md
subworkflows/workflow-academic-argument-validity/SKILL.md
skills/academic-review-argument-audit/SKILL.md
tests/argument-validity-fixtures.md
```

### Observation

现在主链条变为：

```text
抽树
-> 全量验箭头
-> 选问题
-> 写成目标文本
```

exam 场景中：

```text
exam-argument-arrow-audit
-> exam-argument-issue-selection
```

academic 场景中：

```text
academic-argument-arrow-audit
-> academic-argument-issue-selection
-> academic-review-argument-audit
```

### Reflection

这次抽层让 workflow 更接近真正可复用的工程结构：诊断结果可以完整保存，选题策略可以按任务变化，写作层可以只消费已选问题。这样不会因为一次审稿只写了 3 个问题，就丢掉其他已诊断出的弱箭头。
