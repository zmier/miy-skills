# Adapter Gap Analysis

## 当前 adapter 已覆盖的部分

`academic-review-argument-audit` 已经覆盖：

| 能力 | 覆盖情况 |
|---|---|
| 实际观察发现 -> 作者解释 -> 上升贡献 | covered |
| gap -> contribution | covered |
| construct -> measure | covered |
| identification -> causal claim | covered |
| result -> theory / contribution | covered |
| 稳健性是否解决核心威胁 | partially covered |
| 中文审稿意见可读性 | covered |
| case-derived review patterns | covered |

## TASK01 暴露的新缺口

### Gap 1：缺少学术论文顶层论证树入口

当前 adapter 以：

```text
实际观察发现 -> 作者解释 -> 作者上升贡献
```

为入口，这对单条 issue 很好用。但学术论文整篇审稿还需要更上游的顶层图式：

```text
X1：问题有意义
+ X2：作者证明了核心发现
-> Y：贡献成立 / 值得发表
```

否则，容易把 gap、变量、识别、结果、机制看成平行 checklist，而不是贡献成立的不同支撑节点。

建议：在 adapter 或新的子 workflow 中增加 `academic-paper-argument-tree` 入口。

### Gap 2：缺少 `major concern -> weakened node -> impact on Y`

当前 adapter 会写审稿段落，但没有强制每个 major concern 绑定：

```text
target arrow
weakened node: X1 / X2 / Y
impact on publication-worthiness
```

TASK01 显示，欣媛意见之所以有力，是因为技术问题最终都回扣到核心贡献链：

```text
样本筛选 / 变量 / 聚类 / POST / 机制
-> X2 作者是否真的做出来
-> Y 贡献是否成立
```

建议：输出契约加入 `review-issue-arrow-map.md`。

### Gap 2b：缺少论效式 `arrow table`

TASK01 v2 进一步显示，仅有 `major concern -> weakened node` 仍然不够，因为它容易退回“问题属于哪个模块”的写法。

学术论文审稿要真正继承论效题方法，必须显式输出：

```text
arrow_id
from_node
to_node
作者如何论证
审稿人如何质疑
影响 X1/X2/Y
```

例如：

```text
KV 变化 -> 信息披露质量改善 -> 行业自律发展
```

应拆成：

```text
A4: KV 变化 -> 信息披露质量改善
A12: 信息披露质量短期改善 -> 行业自律发展
```

建议：`workflow-academic-review-argument` 的最小输出必须包含 `arrow table`，不能只输出 Mermaid 树。

### Gap 3：缺少“结果回应 gap”的汇合箭头

Dialogue 001/002 强调：

```text
X1 问题有意义
+ X2 作者证明了核心发现
+ actually answers gap
-> Y 贡献成立
```

当前 adapter 有 gap 和 contribution，但没有显式检查：

```text
即使 X2 成立，作者做出来的东西是否真的回应 X1 所宣称的 gap？
```

J-260110 中的一个关键风险是：即使发现短期 KV 改善，也未必回应“行业自律发展”这一更宏大的 gap 和贡献。

建议：新增 `finding-answers-gap` 检查。

### Gap 4：case-derived patterns 缺少树上位置

已有 `case-derived-review-patterns.md` 很有用，但它们目前主要是 issue pattern：

- 核心故事线前提一致性；
- 机制相关样本剔除；
- 溢出效应的直接效应前提；
- 机制排除中的反向解释；
- 稳健性是否回应核心质疑。

TASK01 表明这些 pattern 应进一步标注默认影响节点：

| Pattern | 默认影响 |
|---|---|
| story premise consistency | X2 theory/mechanism；可能影响 Y |
| mechanism-relevant sample exclusion | X2 data/sample；external validity |
| direct effect baseline for spillover | X2 mechanism |
| mechanism-exclusion reversal | X2 mechanism |
| robustness must answer core threats | X2 robustness |
| tone downgrade | output layer，不直接影响树 |

建议：为 case-derived patterns 增加 `default tree location` 字段。

### Gap 5：缺少底层证据台账

当前 adapter 虽然能把审稿问题映射到贡献链，但如果只输出命题树和箭头表，仍可能停在较抽象层级，例如：

```text
P4: Y1 被 KV 捕捉
P8: 稳健性回应核心威胁
G2: 文献 gap 存在
```

学术论文的论证树还需要继续追到：

```text
表格
系数
显著性
变量定义
模型设定
文献引用
原文段落
```

否则，后续审稿意见会出现两类问题：

1. 看似抓住了命题，但没有证据定位，难以复核；
2. 写作时会把“作者说通过了稳健性”当成证据，而不是检查稳健性表到底回应了什么威胁。

建议：adapter 输出契约加入 `evidence-ledger.md`：

```text
evidence_id | 类型 | 原文位置 | 具体证据 | 支撑节点/箭头 | 证据粒度
```

并要求：

```text
exact / summarized / needs-table-qc
```

如果 Markdown 底稿缺少表格具体数值，必须标记 `needs-table-qc`，不臆造系数、t 值、标准误或显著性。

## 是否需要新建子 workflow

建议创建：

```text
workflow-argument-validity/
  subworkflows/
    workflow-academic-review-argument/
```

理由：

1. 学术论文不是普通局部论证，具有稳定的 `X1 + X2 -> Y` 顶层结构；
2. 它和论效/GRE 共享父层抽树、验箭头、断点输出能力；
3. 它和 `workflow-paper-writing-review` 不同，后者是审稿业务流程，前者是论证树审查主轴；
4. 欣媛 case 已经证明真实审稿意见可以被映射回这棵树；
5. 后续 EMFT 或其他稿件可以作为 forward-test。
6. TASK01 v2 表明，学术论文子 workflow 需要强制“命题树 + 箭头表”，否则容易退回模块 checklist。
7. TASK01 v5 表明，学术论文子 workflow 还需要强制 `evidence-ledger.md`，否则论证树会停在中层命题，无法追溯到底层证据。

## 不建议现在做的事

- 不直接把 `X1/X2/Y` 写进所有审稿 Skill 的主流程，先通过子 workflow 承载；
- 不把 J-260110 的具体变量、KV、违规披露判断写成通用规则；
- 不让 `workflow-paper-writing-review` 重新成为主轴；
- 不把欣媛的高压措辞迁移为审稿默认语气。
