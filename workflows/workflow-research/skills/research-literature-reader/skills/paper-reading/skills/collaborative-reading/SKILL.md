---
name: collaborative-reading
description: paper-reading 的协同阅读模式。用于用户还没读过论文、希望 Agent 先在对话窗口讲解论文、边读边问、共同判断重点、逐步决定是否沉淀文件的场景；必须先在对话窗口返回 Paper Orientation Card，覆盖一句话核心发现、主 X/Y 及代理变量、机制、文献对话、research gap 和项目可迁移性；同时在文件侧创建或更新 discussion-outline.md，保存 Orientation Card Snapshot 和初始 Discussion Agenda，再等待用户追问或确认。
---

# Collaborative Reading

状态：`seed / dialogue-first`

## 定位

本 Skill 用于“协同读文献”，不是自动摘要。

目标是先在对话中建立共同理解，让用户能继续追问、纠偏和选择深读方向。

协同阅读的主工作台是 `discussion-outline.md`。`Paper Orientation Card` 是启动讨论的第一张导览卡；`discussion-outline.md` 负责维护整个讨论过程、提纲状态、用户问题、Agent 回答、当前共识、pending 项和提纲外问题。

## 第一轮必须输出 / 写入

第一轮在对话窗口只输出 Paper Orientation Card，不输出完整摘要、design extraction、route map 或 writing patterns。

但第一轮应同时在文件侧创建或更新 `discussion-outline.md`，除非用户明确要求“只聊天、不写文件”。该文件不是最终阅读资产，而是协同阅读工作台；它必须保存：

```text
Orientation Card Snapshot；
initial Discussion Agenda；
Discussion Ledger 的首轮记录；
Agenda Details 的 pending / discussed 状态；
Review Snapshot 的初始状态。
```

这条规则用于避免协同阅读只停留在聊天记录里。首轮写入 `discussion-outline.md` 不等于进入 automatic-summary，也不等于生成 task-specific extraction / route map。

卡片包含：

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

### 一句话核心发现原则

`一句话核心发现` 应停留在 claim 层，回答：

```text
这篇文献最想让读者相信什么？
```

它要是一个简短有力的断言，足够锋利，更像“文献最想让人带走的那颗钉子”。优先表达最核心的理论对象、方向性关系或主张张力，而不是研究场景导览。

这里的“断言”应按形式逻辑意义理解为一个可判断真假的命题。论文的 `一句话核心发现` 必须能表述为一句“形式逻辑视角下的简单命题或复合命题”。生成时必须做“命题化检查”：这句话是否能还原为清楚的直言命题、假言命题、联言命题或选言命题？

常见形态：

```text
直言命题：A 是 / 不是 B。
假言命题：如果 A，那么 B；A 越强，B 越强 / 越弱。
联言命题：A 且 B。
选言命题：A 或 B。
```

“锋利”来自逻辑结构清楚，而不是强行省字。若论文核心 claim 本身是条件关系或方向关系，可以直接写成假言命题；`如果...那么...` 不会降低锋利程度，只要它没有夹带证据层展开。

当自然语言压缩句可能损失逻辑结构时，优先给出“形式逻辑完整还原版”，必要时再附一个可读压缩版：

```text
形式逻辑完整还原版：A；并且，如果 A 的程度越高，那么 B 越强 / 越弱。
可读压缩版：A，且 A 越强，B 越强 / 越弱。
```

### 双重视角：形式逻辑为核心，论文写作为辅助

`一句话核心发现` 的主轴必须是形式逻辑视角下的命题化还原。论文写作、研究设计或 argumentation 术语只能作为辅助标注，用来说明该命题在论文中的功能，不得替代命题化检查。

优先级：

```text
第一层：形式逻辑结构
  直言 / 假言 / 联言 / 选言；
  简单命题 / 复合命题；
  是否可判断真假；
  若要反驳，反例形态是什么。

第二层：论文写作 / 研究设计功能
  descriptive / existence claim；
  causal / consequence / effect claim；
  mechanism claim；
  heterogeneity / boundary claim；
  contribution / gap claim。
```

注意：第二层术语在不同论文写作课、学科和研究设计传统中并不稳定，因此只能帮助理解，不能作为 `一句话核心发现` 的主分类。若两层冲突，以第一层形式逻辑结构为准。

### 一句话核心发现的来源优先级

`一句话核心发现` 应优先从摘要提炼。摘要通常是论文最想让读者带走的 claim 的第一来源和默认锚点。

推荐顺序：

```text
1. 先读 abstract，抽出候选核心命题；
2. 用 introduction 的研究问题、gap 和贡献段校准该命题；
3. 用 conclusion 检查作者最终希望读者记住的版本；
4. 再进入变量、机制、识别、表格和 robustness 的 Agenda 展开。
```

不要一开始就从表格、系数、robustness 或识别细节反推一句话核心发现；那些材料主要用于回答“凭什么？”，不是第一句 claim 的默认来源。

注意：

```text
摘要有时列出的是发现组合，需要进一步命题化；
摘要有时只写 empirical result，需要结合 introduction / conclusion 还原理论 claim；
复杂论文的摘要可能包含多个 claim，此时判断它是否应表述为复合命题；
如果从摘要完全提炼不出核心命题，需要标记为 needs-source-check，并用 introduction / conclusion 重新定位。
```

好的 `一句话核心发现` 应让读者自然产生一个高质量疑问：

```text
凭什么？
```

这个疑问不是缺陷，而是协同阅读的入口。后续 Agenda 要承接这个疑问，逐步展开：

```text
凭什么这么说？ -> 主 X / 主 Y / 代理变量；
怎么证明？ -> identification / empirical design；
为什么是这个机制？ -> mechanism / alternative explanations；
还可能是什么？ -> robustness / boundary conditions；
对当前项目有什么用？ -> transfer / route mapping。
```

不要把证据层、变量代理、识别设计、机制检验、robustness 或结果组合塞进一句话。代理变量和证据链应放到后续 Agenda 项，如主 X、X 的操作化、机制、识别、设计或证据讨论。

判断规则：

```text
如果一句话写成“作者通过 A/B/C/D 证据证明……”，通常已经过度展开。
如果一句话必须依赖“用什么变量代理 / 在什么样本检验 / 做了哪些 robustness”才成立，通常还不够 claim-level。
如果删掉代理变量后仍能留下一个清楚、有方向、有张力的主张，那个主张通常更适合作为一句话核心发现。
如果一句话读完后，读者不会想追问“凭什么？”，它可能太平、太像主题句或背景句。
如果一句话已经回答了所有“凭什么？”，它通常把后续 Agenda 的工作提前做掉了。
如果一句话不能还原成一个可判断真假的命题，它通常还停留在主题、对象或研究场景层。
如果论文的核心发现包含多个 claim，不要为了“一句话”强行删掉其中一个；应判断它是否是联言命题、选言命题或嵌套假言命题。
```

极小正反例：

```text
Bad:
作者通过交易反应、流动性、价格信息含量和会计准则复杂度冲击等证据，论证投资者互动平台揭示并缓解普通投资者的信息整合困难。

Good:
普通投资者存在信息整合困难；投资者互动平台可以缓解这种困难。

Bad:
媒体报道会把股票推入基金经理买入视野；基金经理买入媒体报道股票的倾向越强，未来业绩越差。

Good:
基金经理受“有限注意力”影响越大，表现越差。

Also good:
如果基金经理更受“有限注意力”影响，那么其投资表现更差。

Better as full logical restoration:
基金经理受“有限注意力”影响；并且，如果基金经理受“有限注意力”影响越大，那么其投资表现越差。
```

完整来源案例保留在 `CASE-260521` 的 `Shall We Talk?` discussion outline 中；Skill 内只保留正反例，不复制完整案例。

第一轮之后，若用户继续追问，应继续更新 `discussion-outline.md`。模板见：

```text
templates/discussion-outline-template.md
```

## Discussion Outline

讨论提纲应是每篇文献协同阅读期间持续维护的核心文件。

推荐路径：

```text
2-task-readings/<TASKxx>-discussion-outline.md
```

若不属于特定 task，可使用：

```text
logs/discussion-outline.md
```

讨论提纲至少包含：

```text
Orientation Card Snapshot；
Discussion Agenda；
Discussion Ledger；
Agenda Details；
Appendix: Out-Of-Agenda Questions；
Review Snapshot。
```

### 维护原则

每轮对话后判断用户问题落在哪里：

```text
提纲中有，且用户已经讨论：
  更新对应 Agenda 项的状态、用户问题、Agent 回答、当前共识、未解决点和是否可提升为项目资产。

提纲中有，但用户还没讨论：
  保持 pending；不要假装已经完成；必要时提醒用户还有哪些提纲项未聊。

提纲中没有，但用户提出了：
  写入 Appendix: Out-Of-Agenda Questions；
  记录用户认知、Agent 回答和是否应提升为正式 Agenda 项。
```

状态词：

```text
pending = 提纲中有，但尚未讨论；
discussed = 已讨论，但可能还有问题；
settled-for-now = 当前形成暂定共识；
needs-source-check = 需要回到原文 / PDF / 表格核对；
promote-to-asset = 可写入 task-specific extraction / route map；
dropped = 暂不继续。
```

`discussion-outline.md` 不是最终摘要。它是未来 review 的入口：如果用户很久后回来，先读取该文件恢复当时讨论到哪里、形成了什么共识、还有什么不能复用。

## 对话规则

- 用“我目前的理解是”标记初步判断。
- 明确哪些来自已读段落，哪些是推断。
- 保持可追问，不要一次性铺满完整综述。
- 用户追问变量、机制、识别或文献对话时，按问题展开。
- 每轮对话后维护 discussion outline：更新 Agenda 项、Discussion Ledger 或 Appendix。
- 若讨论形成稳定共识，先在 discussion outline 标为 `promote-to-asset`，再决定是否写入 task-specific extraction / route map。
- 用户要求“写进去”或“沉淀下来”时，再回到 `research-literature-reader` 的文件产物规则。

## 何时写文件

只有在以下情况写文件：

- 用户明确要求保存；
- 用户确认某部分理解可以进入 task-specific extraction；
- 需要创建或更新 `discussion-outline.md` 以维护协同阅读进度；
- 当前对话已经形成稳定结论，需要更新 reading log / route map；
- 本轮从协同阅读转入 automatic-summary 或 design extraction。

写文件时必须标明：

```text
source substrate；
reading status；
哪些内容来自协同讨论；
discussion outline 的状态更新；
哪些问题仍待确认。
```

## 完成标准

- 用户能基于卡片继续追问。
- 已生成或维护 discussion outline，且每个用户问题都能映射到 Agenda 或 Appendix。
- 提纲中未讨论项保持 pending，没有被伪装成已完成。
- 提纲外问题已记录，并判断是否提升为正式 Agenda 项。
- 没有把用户尚未确认的理解直接沉淀成项目结论。
- 已保留底稿状态和剩余风险。
- 若后续写入文件，文件明确区分 first-pass orientation 与 task-specific extraction。

## 禁止事项

- 不在用户还没读论文时直接输出完整文献综述。
- 不把自动摘要当成协同阅读。
- 不把 Paper Orientation Card 写成无法互动的长报告。
- 不让协同阅读只停留在聊天记录里；需要维护 discussion outline。
- 不丢弃提纲外问题；先放入 Appendix，再判断是否提升。
- 不替用户决定下一步深读重点；只提出建议并等待选择。
