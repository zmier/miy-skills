---
name: paper-reading
description: research-literature-reader 的单篇或一组文献阅读父 Skill。用于在研究项目中先判断阅读模式，再路由到 collaborative-reading 或 automatic-summary；适用于用户要理解一篇论文、让 Agent 先讲解论文、自动生成文献摘要、围绕 task / route 提取实验设计、变量、机制、识别、research gap、文献对话、写作范式或可迁移性判断的场景。
---

# Paper Reading

状态：`seed / mode-router / forward-test-with-CASE-260521`

## 定位

本 Skill 是 `research-literature-reader` 下的二级父 Skill，负责“单篇或一组文献怎么读”的模式判断和路由。

它不直接替代：

```text
research-literature-reader：项目级文献资产、task / route / provenance；
scholar-pdf-markdown-restoration：PDF 到可信 Markdown 底稿；
collaborative-reading：对话优先的协同读文献；
automatic-summary：文件优先的自动摘要 / 自动提取。
```

## 模式

### collaborative-reading

默认用于：

- 用户还没读过论文；
- 用户说“边读边讨论”“你先给我讲讲”“我不知道怎么读”；
- 用户需要基于 Agent 的初步讲解继续追问；
- 当前目标是共同理解，而不是快速交付完整文件。

路由到：

```text
skills/collaborative-reading/SKILL.md
```

核心规则：

```text
先在对话中返回 Paper Orientation Card；
首轮同时创建或更新 discussion-outline.md，保存 Orientation Card Snapshot 和初始 Agenda；
后续围绕 discussion-outline.md 维护讨论进度；
等待用户追问、确认、纠偏或选择深读方向；
再决定是否写入 task-specific extraction / route map / writing patterns。
```

### automatic-summary

用于：

- 用户明确要求“帮我读完并整理”“自动总结”“生成摘要 / extraction”；
- 用户要批量处理多篇文献；
- 用户主要需要文件产物，而不是对话式学习；
- 当前文献已经有可接受的 reading substrate。

路由到：

```text
skills/automatic-summary/SKILL.md
```

核心规则：

```text
可以直接生成结构化摘要或任务化提取；
必须标明底稿状态、范围、不可引用边界和剩余风险。
```

## 模式判断

若用户没有明确指定模式，按以下规则判断：

```text
用户本人还没读 / 要一起读 / 要先讲解 -> collaborative-reading；
用户要批量处理 / 要文件产物 / 要快速整理 -> automatic-summary；
底稿不可靠且文献是 empirical / table-heavy -> 先回 research-literature-reader 的 substrate gate；
目标是 PDF 还原 -> 先路由 scholar-pdf-markdown-restoration。
```

如果用户从 collaborative-reading 中途转为“你把这个写进文件”，再回到 `research-literature-reader` 的资产沉淀协议。

如果用户从 automatic-summary 中途开始追问概念、变量或机制，应切回 collaborative-reading，不要继续机械写文件。

## Paper Orientation Card

无论最终是否写文件，只要进入 collaborative-reading，第一轮对话必须先给出：

```text
一句话核心发现；
主 X；
X 的操作化 / 代理变量；
主 Y；
Y 的操作化 / 代理变量；
主机制；
文献 / 学术基础和对话；
research gap；
对当前项目的初步可迁移性；
建议下一步深读位置。
```

该卡是对话界面，不是最终文献资产。进入 collaborative-reading 的首轮，应同时创建或更新 `discussion-outline.md`，作为后续讨论、pending 项和未来 review 的主入口；但不得把首轮 outline 误当成完整摘要、design extraction 或 route mapping。

## 完成标准

- 已判断本轮阅读模式，并在必要时说明为什么。
- collaborative-reading 下已先返回对话卡，并围绕 discussion outline 维护讨论进度，而不是直接写满文件。
- automatic-summary 下已直接产出用户要求的摘要 / extraction，并标明底稿状态。
- 需要沉淀项目资产时，回到 `research-literature-reader` 的文件结构与 log 规则。
- 不把 PDF restoration、协同阅读讲解和项目级文献资产沉淀混成同一个动作。

## 禁止事项

- 不把 collaborative-reading 和 automatic-summary 当成平级项目级能力。
- 用户还没读论文时，不直接默认进入完整 design extraction。
- 不把 Paper Orientation Card 当作最终精读结论。
- 不在底稿未通过接收验收时自动生成表格系数、识别细节或 robustness 结论。
