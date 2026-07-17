---
name: paper-co-read
description: paper-reading 的论文协同共读层。用于用户希望边读边讨论、先听 Agent 导览、继续追问、共同判断重点或逐步决定是否沉淀项目资产的场景；必须读取 paper-extract 产出的 automatic-extraction.md 作为结构化底稿，再生成低假设 Paper Orientation Card 和 discussion-outline.md，维护 Discussion Agenda、Ledger、共识、pending 项和提纲外问题。
---

# Paper Co-Read

状态：`seed / dialogue-over-extraction`

## 定位

本 Skill 是论文共同读的交互层，不是完整自动抽取层。

它回答：

```text
如何基于 automatic-extraction.md，与用户共同读论文、生成 Agenda、推进追问和共识？
```

核心输入是：

```text
automatic-extraction.md
```

核心工作台是：

```text
discussion-outline.md
```

## 与 paper-extract 的关系

```text
paper-extract:
  生成结构化阅读底稿 automatic-extraction.md。

paper-co-read:
  读取 automatic-extraction.md；
  选择适合对话展开的内容；
  生成 Paper Orientation Card；
  创建 / 更新 discussion-outline.md；
  通过用户追问持续校正和深化。
```

如果没有可用的 `automatic-extraction.md`，必须先运行 `paper-extract` 生成最小抽取底稿，再进入共同读。不要从零开始聊天，也不要把共同读当成绕过自动抽。

## 输入检查

开始前确认：

```text
source PDF / Markdown substrate；
automatic-extraction.md 是否存在；
automatic extraction 的 reading status 和 source anchors 质量；
当前 task / route；
用户问题或想讨论的位置；
已有 discussion-outline.md 是否存在。
```

若 automatic extraction 标记 `needs-source-check`、`rough`、`degraded` 或 `table-leak high risk`，对话中必须用低假设表达，并提示哪些判断不能直接复用。

## 第一轮对话输出

第一轮在对话窗口只输出 Paper Orientation Card，不输出完整 automatic extraction，不直接写满 design extraction、route map 或 writing patterns。

Paper Orientation Card 应从 `automatic-extraction.md` 中抽取并压缩为：

```text
一句话核心发现：理论纯净版；
一句话核心发现：读者导览版；
形式逻辑结构初判；
核心命题支初判；
命题域概念层级初判；
共享概念复用初判；
支撑 / 诊断分支初判；
每个命题支的待证对象；
每个命题支中的可观察对象 / proxy；
主机制 / warrant；
文献 / 学术基础和对话；
research gap；
对当前项目的初步可迁移性；
建议下一步深读位置。
```

卡片必须保持低假设：

```text
用“我目前的理解是”标记初步判断；
区分来自 automatic extraction 的判断、原文 anchor 和 Agent 推断；
不把 needs-source-check 写成确定结论；
不把 proxy 当成理论 claim；
不预设全篇只有一组 X/Y。
```

命题支小段必须保持理论层：

```text
P1/P2/P3 的标题和第一句应写理论对象 / 理论关系；
如果展示 A02，先展示 Pi 的形式逻辑完整表述和命题形式；
再展示该 Pi 的 top-level concepts、child concepts、relation IDs 和 concept relation；
empirical proxy 只能放在该命题支下的“可观察对象 / proxy”或单独 proxy 小段；
不要把 `media coverage -> fund buying`、`PROPENSITY_BUY_MEDIA -> alpha` 直接写成核心命题标签。
```

A02 共同读展示规则：

```text
A02 是从 A01 命题逆拆概念；
不是全篇概念清单；
也不是主 X / 主 Y 的变量清单。

必须保留：
  Pi 原命题 / 简写；
  Pi 形式逻辑完整表述；
  命题形式：直言 / 假言 / 联言 / 选言；
  Pi top-level concepts；
  Pi child concepts / dimensions / mechanism candidates；
  Shared Concept Registry；
  Pi relation IDs；
  Pi concept relation。
```

共同读中必须维持符号连续性：

```text
A01: P1 / P2
A02: P1-C1 / P1-C1.1 / P1-R1 / Shared-C1
A03: A03-P1-C1 / A03-P1-C1.1 / A03-P1-R1 / A03-Shared-C1
```

当用户问“这个变量是在测什么？”时，必须回到 A02 concept ID 回答；当用户指出某个 proxy 找不到对应概念时，记录为 `A02-revision-needed`。

形式逻辑化不得添加原命题没有的机制、proxy、诊断结果或证据链。若用户指出 Agent 添加了内容，必须承认并在 `discussion-outline.md` 的 Extraction Revision Notes 中记录 `faithful logical-form rewrite needed`。

跨命题复用概念时，Paper Orientation Card 应说明同一个 concept 在不同命题中的不同论证角色。例如：

```text
Shared-C：普通投资者公开信息整合困难
  P1 中：待证明其存在；
  P2 中：待证明其可被双向互动沟通缓解。
```

同时必须区分 `Core Proposition Branches` 与 `Supporting / Diagnostic Branches`：

```text
Core Proposition Branches:
  只放通过 collapse test、take-away test、independence test 的 P1 / P2 / P3。

Supporting / Diagnostic Branches:
  放机制、诊断模式、边界条件、替代解释排除、robustness、proxy 可信性支撑。
```

不要因为某个分支重要就把它写成 P3。若它是在回答“凭什么相信 P1 / P2”，通常应写成：

```text
S-P1-diagnostic；
S-P1-mechanism；
S-P2-exclusion；
S-P2-robustness；
candidate S/P。
```

如果 automatic extraction 把疑似 supporting branch 升成 core proposition，Paper Orientation Card 应低假设地标注：

```text
P? / candidate S/P:
  这个分支很重要，但可能只是 diagnostic / mechanism / boundary support；
  需要共同读时确认是否应降为 S-Pi-*。
```

推荐形态：

```text
P1：有限注意力影响基金经理交易行为。
  可观察对象 / proxy：media coverage 作为 attention trigger；fund buys/sells 作为 trading behavior。

P2：受有限注意力影响越强，未来业绩越差。
  可观察对象 / proxy：PROPENSITY_BUY_MEDIA 作为 attention-driven propensity；future alpha 作为 performance。
```

第一轮卡片必须使用“双层表述”：

```text
理论层核心断言：
  用理论对象、抽象构念和理论关系表达 core P1 / P2 / P3。
  对应 automatic-extraction.md 的“一句话核心发现：理论纯净版”。

经验层实现：
  单独说明作者用哪些 observable / proxy / measure / empirical relation
  来操作化这些理论对象和关系。
  必须尽量带出 A03 bridge ID 和 A02 node ID，
  例如：A03-Shared-C4 -> 问题文本分类；
  A03-P2-R1 -> 流动性 / 价格信息含量诊断。
  可形成“一句话核心发现：读者导览版”。
```

不要让经验层实现污染理论层命题。常见错误：

```text
Bad:
  P2：PROPENSITY_BUY_MEDIA 越高，future alpha 越低。

Good:
  P2：基金经理受有限注意力影响越大，未来投资表现越差。
  经验层实现：PROPENSITY_BUY_MEDIA 代理有限注意力影响程度；
  future alpha 代理未来投资表现。
```

如果自动抽取底稿本身存在 proxy 污染，Paper Orientation Card 应先做低假设修正，并在 `discussion-outline.md` 的 Extraction Revision Notes 中记录：

```text
theory/proxy separation needed；
需要回写 automatic-extraction.md。
```

## discussion-outline.md

第一轮应同时创建或更新 `discussion-outline.md`，除非用户明确要求“只聊天、不写文件”。

推荐路径：

```text
2-task-readings/<TASKxx>-discussion-outline.md
```

若不属于特定 task：

```text
logs/discussion-outline.md
```

模板见：

```text
templates/discussion-outline-template.md
```

`discussion-outline.md` 是协同阅读工作台，不是最终摘要。它必须保存：

```text
Source；
Automatic Extraction Link；
Orientation Card Snapshot；
Proposition Registry；
Discussion Agenda；
Discussion Ledger；
Agenda Details；
Appendix: Out-Of-Agenda Questions；
Review Snapshot。
```

如果本轮需要在回复中展示“文件侧草案结构”，必须区分：

```text
automatic-extraction.md 草案：
  应保留 paper-extract 模板的 A01-A08 主结构；
  必须保留 A01 核心命题准入测试表、命题登记表；
  必须保留 A02/A03/A04/A05/A06/A07 的表格骨架；
  A04/A05 必须使用 Pi-R / design block；
  不得写成自由摘要式小标题列表。

discussion-outline.md 草案：
  应保留共同读工作台结构；
  记录 Orientation Card Snapshot、Agenda、Ledger、pending 项。
```

不要把 automatic-extraction 草案写成压缩版 discussion outline，也不要把 discussion-outline 草案写成完整自动抽取。

如果用户或 UAT 要求“输出你会写入的文件草案”，即使只是草案，也不得省略关键表格。信息不足时在表格单元中写：

```text
needs-source-check；
not yet extracted；
unknown from current substrate。
```

## Agenda 生成原则

Agenda 必须基于 `automatic-extraction.md` 的 A01-A08，而不是现场凭空生成。

默认 Agenda：

```text
A01 One-sentence core finding
A02 Proof structure / argument plan
A03 Operationalization and proxy bridge
A04 Measurement and data construction
A05 Research design and identification strategy
A06 Data analysis and empirical results
A07 Alternative explanations, robustness, and validity threats
A08 Transfer to current project
A09 Next reading targets
```

若用户已经讨论过部分 Agenda，应更新状态，而不是重复第一轮。

## 面向用户的 Agenda 汇报

`A01 / A02 / A03` 等编号是共同读工作台的内部索引，不是默认的用户语言。

对用户汇报进度、下一步、已完成项或待讨论项时，不得只裸报内部编号和状态词。

必须使用：

```text
编号 + 自然语言任务名 + 当前状态 / 含义。
```

例如：

```text
Bad:
  当前 Agenda 状态：
  A01：settled-for-now
  A02：discussed
  A03：next
  A04-A06：pending

Good:
  当前共读进度：
  - A01 核心发现：已暂定
  - A02 作者如何在理论层论证核心发现：已讨论
  - A03 抽象概念如何落到可观察 proxy：下一步
  - A04 变量如何进入数据：待讨论
  - A05 作者如何组织研究设计 / 识别策略：待讨论
  - A06 经验结果如何支撑命题：待讨论
```

如果用户不是 Skill 作者或没有显式使用 A01/A02 语言，优先使用更自然的口语总结：

```text
我们已经完成：
1. 把论文最想让读者带走的核心发现定下来；
2. 初步拆开作者在理论层如何论证这个发现。

下一步进入：
抽象概念如何落到可观察变量，也就是作者怎样把“有限注意力”
操作化为媒体覆盖、买入倾向和未来业绩之间的经验链条。
```

只有在用户已经明确使用编号推进讨论时，才可以保留 A01/A02 编号；即便如此，也必须同时给出自然语言解释，避免把 `settled-for-now / pending / next` 等内部状态词直接丢给用户。

写入 `discussion-outline.md` 时可以保留内部编号和状态词；对话窗口输出时必须翻译成人类可读的阅读进度。

## 讨论推进规则

每轮用户追问后判断问题落在哪里：

```text
提纲中有：
  更新对应 Agenda 项状态、用户问题、Agent 回答、当前共识、source anchors 和 open questions。

提纲中没有：
  写入 Appendix: Out-Of-Agenda Questions；
  判断是否提升为正式 Agenda。

用户纠正 automatic extraction：
  标记为 revised-by-discussion；
  必要时反向更新 automatic-extraction.md 或记录 extraction revision needed。
```

状态词：

```text
pending = 提纲中有，但尚未讨论；
discussed = 已讨论，但可能还有问题；
settled-for-now = 当前形成暂定共识；
needs-source-check = 需要回到原文 / PDF / 表格核对；
promote-to-asset = 可写入 task-specific extraction / route map；
revised-by-discussion = 用户讨论修订了自动抽取判断；
dropped = 暂不继续。
```

## 与资产沉淀的边界

共同读可以产生可迁移洞见，但不要自动写满最终资产。

```text
discussion-outline.md:
  记录共同读过程和当前共识。

automatic-extraction.md:
  记录结构化自动抽取底稿。

TASKxx-design-extraction.md / route-map.md / writing-patterns.md:
  只有用户确认或任务需要时，回到 research-literature-reader 资产沉淀协议生成。
```

## 完成标准

- 已读取 automatic-extraction.md；若不存在，已先生成最小抽取底稿。
- 若展示 automatic-extraction 草案，已保留 A01-A08 和 A04/A05 block 结构。
- 已在对话中返回低假设 Paper Orientation Card。
- 已向用户汇报进度时，把 A01/A02/A03 等内部编号翻译为自然语言任务名。
- 已创建或更新 discussion-outline.md。
- Discussion Agenda 与 automatic extraction 的 A01-A08 对齐。
- 每轮用户追问都更新 Ledger / Agenda / Appendix。
- 明确哪些共识可提升为项目资产，哪些还需 source-check。

## 禁止事项

- 不从零开始共同读而跳过 automatic extraction。
- 不把 automatic-extraction.md 原样塞给用户当对话卡。
- 不把 discussion-outline.md 当成完整自动抽取文档。
- 不把 Paper Orientation Card 当最终精读结论。
- 不在用户只要求共同读时直接写满 design extraction / route map / writing patterns。
- 不对用户裸报 `A01/A02/A03`、`pending`、`settled-for-now` 等内部工作台语言；必须翻译成自然语言进度。
- 不忽略用户纠偏；用户纠偏必须反映到 discussion-outline 或 extraction revision note。
