---
name: paper-reading
description: 单篇或一组文献阅读父 Skill，可独立用于读懂论文、共同读、自动摘要或最终文献笔记，也可被 research-literature-reader 在研究项目中调用。先通过 paper-extract 生成结构化 automatic-extraction.md，再按用户意图进入 paper-co-read 共同读、paper-finalize 核验定稿、自动文件输出、task-specific extraction、route mapping 或 writing patterns；若由项目型上层 Skill 调用，只返回 reading output handoff，是否回挂 task / route / node 由上层决定。
---

# Paper Reading

状态：`seed / pipeline-router / forward-test-with-CASE-260521`

## 定位

本 Skill 是 `research-literature-reader` 下的二级父 Skill，负责“单篇或一组文献怎么读”的管线编排和路由。

它不直接替代：

```text
research-literature-reader：项目级文献资产、task / route / provenance；
scholar-pdf-markdown-restoration：PDF 到可信 Markdown 底稿；
paper-extract：结构化自动抽取层，产出 automatic-extraction.md；
paper-co-read：基于 automatic-extraction.md 的协同共读层；
paper-finalize：基于 automatic-extraction、discussion-outline 和原文/PDF/表格的核验定稿层；
automatic-summary：legacy 文件优先自动摘要 / 自动提取入口；
collaborative-reading：legacy 协同阅读入口，验证期暂保留。
```

## 上层调用边界

`paper-reading` 可以单独使用，也可以被项目型上层 Skill 调用。

单独使用时，它只负责完成本轮论文阅读管线：

```text
读懂论文；
生成 automatic-extraction / discussion-outline / final-literature-note；
按用户要求输出摘要、设计提取、route map 或 writing patterns。
```

它不强制要求存在 project / task / node，也不强制把阅读产物回挂到研究项目。

若由 `research-literature-reader` 这类 project / task / route / node 型上层 Skill 调用，`paper-reading` 应在结束时返回可交接信息，而不是自行决定项目回挂：

```text
本轮阅读模式；
生成或更新的文件；
关键理解结论；
可迁移到项目的候选点；
可能影响的 task / route / node；
剩余 source / table / proxy / interpretation 风险。
```

是否真正更新 task reading ledger、route / node 文件或 project log，由上层 Skill 根据项目语境决定。

## 管线

论文阅读不再理解为 `collaborative-reading` 和 `automatic-summary` 二选一。更稳定的流程是：

```text
PDF / Markdown substrate
  -> paper-extract
     生成 automatic-extraction.md
  -> paper-co-read / paper-finalize / 文件资产化输出
     discussion-outline / final-literature-note / task-specific extraction / route map / writing patterns
```

核心原则：

```text
自动抽是上游结构化能力；
共同读是下游交互能力；
核验定稿是可引用文献资产能力；
自动摘要 / design extraction / route map 是文件资产化输出形态。
```

结构继承约束：

```text
A01 先形成 faithful propositions：P1 / P2 / P3；
A02 沿每个 proposition 逆向拆出 concept hierarchy 与 relation IDs：
  P1-C1 / P1-C1.1 / P1-R1 / Shared-C1；
A03 再把作者的 empirical observables / proxies / diagnostic patterns
  挂回 A02 nodes：
  A03-P1-C1 / A03-P1-C1.1 / A03-P1-R1 / A03-Shared-C1。
```

A02 不是变量清单，A03 也不是脱离 A02 的 proxy 清单。若 A03 出现无法挂回 A02 node 的变量、proxy 或诊断证据，必须回到 A02 增补概念 / 子概念 / 关系，或标记 `A02-revision-needed`。

三条正式流程：

```text
默认推荐：
  paper-extract -> paper-co-read -> paper-finalize

用户明确要求先核验：
  paper-extract -> paper-finalize -> paper-co-read

批量 / 正式文献库：
  paper-extract -> paper-finalize
```

### paper-extract

默认先执行或确认已存在：

```text
skills/paper-extract/SKILL.md
```

路由到 `paper-extract` 时，必须先完整读取：

```text
skills/paper-extract/SKILL.md
skills/paper-extract/templates/automatic-extraction-template.md
```

不得只根据本父 Skill 的摘要自行生成抽取草案。

适用：

- 用户要共同读，但尚无 `automatic-extraction.md`；
- 用户要自动摘要、批量整理、design extraction 或 route mapping；
- 需要先建立 A01-A08 结构化阅读底稿；
- 后续需要 UAT、复盘、项目资产沉淀。

核心规则：

```text
生成 / 更新 automatic-extraction.md；
覆盖 A01-A08；
保留 proposition IDs；
标明 source anchors、底稿状态、不可引用边界和剩余风险；
可作为 paper-co-read 和文件资产化输出的输入。
```

### paper-co-read

默认用于：

- 用户还没读过论文；
- 用户说“边读边讨论”“你先给我讲讲”“我不知道怎么读”；
- 用户需要基于 Agent 的初步讲解继续追问；
- 当前目标是共同理解，而不是快速交付完整文件。

路由到：

```text
skills/paper-co-read/SKILL.md
```

路由到 `paper-co-read` 时，必须先完整读取：

```text
skills/paper-co-read/SKILL.md
skills/paper-co-read/templates/discussion-outline-template.md
```

核心规则：

```text
先读取 automatic-extraction.md；
若不存在，先运行 paper-extract 生成最小抽取底稿；
再在对话中返回 Paper Orientation Card；
首轮同时创建或更新 discussion-outline.md，保存 Orientation Card Snapshot 和初始 Agenda；
后续围绕 discussion-outline.md 维护讨论进度；
等待用户追问、确认、纠偏或选择深读方向；
再决定是否写入 task-specific extraction / route map / writing patterns。
```

### paper-finalize

用于：

- 用户明确要求“最终文献笔记”“可引用结论”“source-check”“核表格”“核公式”；
- 用户要求把 first-pass extraction 或 co-read 共识升级成最终文献资产；
- 用户明确说“先核验再共同读”；
- 用户做批量 / 正式文献库，希望生成 source-verified note。

路由到：

```text
skills/paper-finalize/SKILL.md
```

路由到 `paper-finalize` 时，必须先完整读取：

```text
skills/paper-finalize/SKILL.md
skills/paper-finalize/templates/final-literature-note-template.md
```

核心规则：

```text
必须先有 automatic-extraction.md；
默认读取 discussion-outline.md；
若没有 discussion-outline.md 但用户明确要求先核验，标记 cold-start finalization；
回到 PDF / restored manuscript / tables / figures / source anchors 核验；
输出 final-literature-note.md / verified-claims.md / source-check-log.md；
每条关键结论标注 verified-citable / verified-understanding / inferred-not-citable / needs-source-check / contradicted-or-revise。
```

`paper-finalize` 不是共同读替代品。若 finalize 后用户继续追问理解、变量、机制或迁移，应回到 `paper-co-read`，并把 finalize 的 verified note 作为更可靠底稿。

### automatic file output

用于：

- 用户明确要求“帮我读完并整理”“自动总结”“生成摘要 / extraction”；
- 用户要批量处理多篇文献；
- 用户主要需要文件产物，而不是对话式学习；
- 当前文献已经有可接受的 reading substrate。

默认先使用：

```text
skills/paper-extract/SKILL.md
```

再按 `research-literature-reader` 的资产沉淀协议生成 task-specific extraction、route map、writing patterns 或 literature matrix。

legacy `automatic-summary` 暂保留：

```text
skills/automatic-summary/SKILL.md
```

后续验证通过后，可考虑将其并入 `paper-extract` 或改为 automatic file output 的薄封装。

核心规则：

```text
先有 automatic-extraction.md；
再生成结构化摘要或任务化提取；
必须标明底稿状态、范围、不可引用边界和剩余风险。
```

## 路由判断

若用户没有明确指定管线，按以下规则判断：

```text
用户本人还没读 / 要一起读 / 要先讲解 -> paper-extract -> paper-co-read；
用户要最终文献笔记 / 可引用结论 / 核表格 / 核公式 / source-check -> paper-extract -> paper-finalize；
用户明确要求先核验再讨论 -> paper-extract -> paper-finalize -> paper-co-read；
用户要批量正式文献库 / source-verified literature notes -> paper-extract -> paper-finalize；
用户要批量处理 / 要文件产物 / 要快速整理 -> paper-extract -> automatic file output；
底稿不可靠且文献是 empirical / table-heavy -> 先回 research-literature-reader 的 substrate gate；
目标是 PDF 还原 -> 先路由 scholar-pdf-markdown-restoration。
```

如果用户从 `paper-co-read` 中途转为“你把这个写进文件”，再回到 `research-literature-reader` 的资产沉淀协议。

如果用户从 `paper-co-read` 中途转为“这能引用吗 / 你核一下表格 / 最终版文献笔记”，切到 `paper-finalize`。

如果用户从 automatic file output 中途开始追问概念、变量或机制，应切到 `paper-co-read`，不要继续机械写文件。

如果用户从 `paper-finalize` 中途开始追问“为什么 / 怎么理解 / 和项目怎么迁移”，切回 `paper-co-read`，并把 verified note 的 claim status 带入讨论。

## Paper Orientation Card

无论最终是否写文件，只要进入 `paper-co-read`，第一轮对话必须先基于 `automatic-extraction.md` 给出：

```text
一句话核心发现：理论纯净版；
一句话核心发现：读者导览版；
形式逻辑结构初判；
命题支初判；
每个命题支的待证对象；
每个命题支中的可观察对象 / proxy；
必要时按命题支标注 X/Y 关系；
主机制 / warrant；
文献 / 学术基础和对话；
research gap；
对当前项目的初步可迁移性；
建议下一步深读位置。
```

不要预设所有论文都有单一 `主 X / 主 Y`。X/Y 只有在对理解作者论证有帮助时才出现，并且必须说明它属于哪个命题支。

该卡是对话界面，不是最终文献资产。进入 `paper-co-read` 的首轮，应同时创建或更新 `discussion-outline.md`，作为后续讨论、pending 项和未来 review 的主入口；但不得把首轮 outline 误当成完整摘要、design extraction 或 route mapping。

## 用户可读性边界

`paper-reading` 可以在内部使用 A01-A09、P1/P2、S-Pi-*、pending、settled-for-now 等工作台语言，但对用户汇报进度时必须翻译。

不得只说：

```text
A01：settled-for-now
A02：discussed
A03：next
```

必须说：

```text
A01 核心发现：已暂定；
A02 作者如何在理论层论证核心发现：已讨论；
A03 抽象概念如何落到可观察 proxy：下一步。
```

如果用户没有主动使用编号，优先使用无编号口语版：

```text
我们已经把论文核心发现和作者的理论论证拆清楚了。
下一步该看作者如何把“有限注意力”落到可观察变量上。
```

内部编号可以保留，但必须服务于推进讨论，而不是把 Skill 的工作台结构直接暴露给普通读者。

## Legacy Compatibility

验证期暂保留旧入口：

```text
skills/collaborative-reading/SKILL.md
skills/automatic-summary/SKILL.md
```

旧 `collaborative-reading` 已包含大量 A01-A08 规则，可作为拆分来源和回归参照，但新任务优先使用：

```text
paper-extract -> paper-co-read
```

旧 `automatic-summary` 是早期文件优先自动提取入口。后续若 UAT 证明 `paper-extract` 能稳定覆盖它的功能，可再决定退役、改名或薄封装。

## 完成标准

- 已判断本轮阅读管线，并在必要时说明为什么。
- 已按路由读取对应子 Skill 和模板，而不是只依赖本父 Skill 摘要。
- 需要读论文时，已先确认或生成 automatic-extraction.md。
- paper-co-read 下已基于 automatic extraction 返回对话卡，并围绕 discussion outline 维护讨论进度，而不是直接写满文件。
- 面向用户汇报时，已将 A01/A02/A03 等内部编号和状态词翻译为自然语言阅读进度。
- paper-finalize 下已核验原文 / PDF / 表格 / 公式，并区分可引用结论、理解性结论和待核验结论。
- automatic file output 下已基于 automatic extraction 产出用户要求的摘要 / extraction，并标明底稿状态。
- 若由项目型上层 Skill 调用，已返回 reading output handoff：产物清单、候选回挂对象和剩余风险。
- 需要沉淀项目资产时，回到 `research-literature-reader` 的文件结构、task / node 回挂和 log 规则。
- 不把 PDF restoration、协同阅读讲解和项目级文献资产沉淀混成同一个动作。

## 禁止事项

- 不把 collaborative-reading 和 automatic-summary 当成平级项目级能力。
- 不在没有 automatic-extraction.md 或最小自动抽底稿时直接进入共同读。
- 用户还没读论文时，不直接默认进入完整 design extraction。
- 不把 Paper Orientation Card 当作最终精读结论。
- 不把 discussion-outline.md 当作 automatic-extraction.md。
- 不把 automatic-extraction.md 当作 final-literature-note.md。
- 不把 A01/A02/A03、pending、settled-for-now 等内部工作台语言裸露给用户；必须同时给出自然语言解释。
- 不在没有 automatic-extraction.md 时直接进入 paper-finalize。
- 不在底稿未通过接收验收时自动生成表格系数、识别细节或 robustness 结论。
- 不在缺少 project / task / node 语境时强制创建项目回挂。
