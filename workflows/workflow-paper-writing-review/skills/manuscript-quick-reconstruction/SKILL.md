---
name: manuscript-quick-reconstruction
description: 对学术手稿做快速通读和贡献链还原。用于外部审稿、投稿前自审、返修前诊断中，在已有 PDF/HTML/Markdown 底稿的基础上，提取研究问题、文献缺口、理论机制、核心变量、数据样本、识别策略、主要结果、贡献叙事和初步风险点，并输出可供后续文献定位、方法审查、变量审查和审稿素材组装使用的 Markdown 笔记。本 Skill 不生成最终审稿意见。
---

# Manuscript Quick Reconstruction

## 定位

本 Skill 是 workflow-paper-writing-review 中的第 3 步：快速通读。

它不负责判断文献缺口是否真实，也不负责完整方法审计或生成最终审稿意见。它负责先把作者声称的贡献链还原出来，让后续审稿判断有一个共同对象。

核心产物是项目内 Markdown 笔记，例如：

```text
notes/quick-read-contribution-chain.md
```

## 触发条件

当用户在论文审稿或自审项目中提出以下需求时使用：

- “先快速读一下这篇文章”
- “总结这篇稿件在做什么”
- “还原贡献链”
- “第 3 步快速通读”
- “提取研究问题、理论、变量、数据、方法和结论”
- “给后面的文献定位/方法审查打底”
- “先不要写审稿意见，只整理关键点”

## 输入

优先使用项目内已有材料：

- 段落编号 Markdown 或 restored Markdown；
- 原始 PDF 或 HTML；
- extraction/restoration log；
- 项目 README；
- 已有审读台账或 notes。

如果没有可靠 Markdown 底稿，应先调用或建议使用 `scholar-pdf-markdown-restoration`。若只有 PDF 也可以做快速通读，但输出必须标注定位精度较低。

## 输出

默认输出到项目 notes 目录：

```text
notes/quick-read-contribution-chain.md
notes/review-issue-ledger.md
```

## 语言策略

输出语言应服务后续人工审读，而不是机械跟随原稿语言。

- 如果原稿是英文：默认使用中文作为主体阐述语言，同时保留关键英文术语、变量名、核心原文短语、检索词和 evidence location。推荐格式是“中文判断 + 括号内英文关键词”，而不是大段中英并列。
- 如果原稿是中文：默认使用中文输出，不需要额外生成英文版本；英文术语、变量名、数据库名、期刊名和原文关键词可保留英文。
- 如果用户明确要求单语或双语，以用户要求为准。
- 不翻译变量名、模型符号、表格编号、段落编号、数据库名和引用条目中的专名。
- 中文解释应帮助审稿人快速判断，不应改写成最终审稿意见。
- 对难懂但必须保留的术语、缩写、变量、数据库、分类口径、方法名，应增加解释层。可以使用 Obsidian 注释 `%%解释说明：...%%` 做行内工作说明，并在 `Glossary and Knowledge Gaps` 中集中登记。

如果项目已有命名约定，可使用等价文件名，但应包含以下模块：

- metadata；
- reading status；
- core finding sentence / 一句话发现；
- observed vs claimed finding / 实际观测发现 vs 作者上升发现；
- one-paragraph synopsis；
- contribution chain table；
- section map；
- key constructs and variables；
- glossary and knowledge gaps / 术语解释与需补充知识；
- construct-to-variable mapping / 概念到变量映射；
- data and empirical design;
- headline findings；
- claimed contributions；
- Step 4 literature branch seeds；
- review issue ledger / 审稿疑点台账；
- initial reviewer questions；
- next-step routing。

## 阅读顺序

默认按以下顺序快速读取，不必一开始逐段精读：

1. Abstract：抓研究问题、对象、数据、方法、结果和贡献。
2. Introduction：抓动机、文献缺口、贡献声明和文章路线。
3. Theory / hypotheses：抓理论框架、机制和假设。
4. Data / variables / method：抓样本、变量定义、识别策略和模型。
5. Baseline results and robustness：抓主结果和作者如何支撑因果主张。
6. Mechanisms / heterogeneity / extensions：抓证据链是否围绕主问题展开。
7. Conclusion：抓作者最终的贡献叙事、政策含义和可能过度声称。

如果有段落编号，应优先记录关键证据位置，例如 `[para 7]`、`Table 2`、`Section 4.2.1`。

## 提取问题

### 研究问题

- 作者研究的核心问题是什么？
- 问题的对象、场景、时间和单位是什么？
- 问题是否被写成因果问题、机制问题、测量问题或描述性问题？

### 实际观测发现 vs 作者上升发现

如果作者提出因果或贡献性发现，quick-read 必须先做一层“因果翻译”，用大白话拆开：

- actual observed finding / 实际观测发现：作者的数据和模型里真正比较的 X 和 Y 是什么；
- claimed finding / 作者上升发现：作者把这个关系解释成什么理论、经济或因果发现；
- match status / 是否匹配：matched / partly matched / overstated / unclear；
- bridge assumptions / 桥接假设：要让“实际观测发现”支撑“作者上升发现”，必须成立哪些前提；
- audit route / 后续路由：通常进入 `manuscript-causal-identification-audit`、变量测量审查或结果叙事一致性审查。

写法要直白：

```text
实际观测发现：数据里看到的是 A 与 B 相关。
作者上升发现：作者说这是 X 导致 Y。
中间桥：A 必须能代表 X，B 必须能代表 Y，还要排除反向因果和共同原因。
```

如果二者不完全匹配，应同步写入 `notes/review-issue-ledger.md`。

### 文献缺口

- 作者声称已有文献缺了什么？
- 缺口是主题缺口、机制缺口、数据缺口、方法缺口还是情境缺口？
- 作者用哪些文献来定位自己？

此处只还原作者声称，不做完整文献真实性判断；真实性判断交给“文献定位”模块。

### 理论机制

- 作者使用什么理论或概念框架？
- 机制链条是什么？
- 假设如何从机制推出？
- 有没有明显概念跳跃或机制重叠，需要后续检查？

### 核心变量

- 因变量是什么，如何定义？
- 核心解释变量或处理变量是什么，如何定义？
- 机制变量、异质性分组和拓展变量有哪些？
- 变量是否与理论概念一一对应，或需要后续测量审查？

### 数据和样本

- 数据来源是什么？
- 样本单位、时间跨度、行业/地区范围是什么？
- 样本合并、筛选、口径统一和缺失处理有哪些关键步骤？

### 识别策略 / 研究设计

- 主模型是什么？
- 使用了哪些固定效应、控制变量和标准误处理？
- 作者是否提出因果解释？
- 用了哪些内生性处理或稳健性设计？
- 是否需要进入 `manuscript-causal-identification-audit` 做 DAG、后门、前门、IV 和控制变量审查？

此处只描述设计，不给最终方法判决；判决交给“方法识别审查”模块。

### 主要结果

- 基准结果是什么？
- 稳健性检验支持了什么？
- 机制检验声称支持哪些机制？
- 异质性和拓展分析服务于哪条贡献叙事？

### 贡献叙事

- 作者声称的理论贡献、实证贡献、方法贡献或政策贡献分别是什么？
- 哪些贡献看起来可能成立？
- 哪些贡献需要后续文献或方法检查？

### 审稿疑点台账

快速通读时必须边读边初始化或更新 `notes/review-issue-ledger.md`。它不是最终审稿意见，而是后续模块共享的工作台账。

疑点来源包括两类：

- agent 自己在阅读中发现的脆弱点；
- 用户在对话中提出的困惑、追问、反问或质疑。

凡遇到以下情况，应登记为 issue：

- 作者核心概念与实证变量之间存在跳转；
- 变量构造依赖外部清单、代码表、concordance、数据库口径或作者未展开的处理；
- 关键术语读者不易理解，且影响贡献、变量、识别或结果解释；
- 因果语气强于识别设计当前能支持的程度；
- 文献缺口、理论机制或贡献声明需要外部文献核验；
- 表格、段落、变量名、样本期、数据口径存在不一致；
- 稳健性、机制、异质性或拓展分析可能没有服务于核心发现。

会话中的触发信号：

- 用户问“怎么算”“到底是什么依据”“作者有说明吗”；
- 用户指出“这类仍然看不懂”“我读不懂”；
- 用户区分两种可能解释，例如“是用了计算方法，还是直接用了 code/list”；
- 用户怀疑时间、样本、变量口径、文献结论或因果解释不一致；
- 用户要求总结“困惑”的本质。

触发后应执行：

1. 用原文或已知证据回答问题；
2. 判断它是否构成审稿 issue；
3. 若构成，立刻写入或更新 `notes/review-issue-ledger.md`；
4. 在给用户的回复中标明 issue id，例如“已记为 `VAR-001`”。

如果当前无法访问项目文件，也要在回复中给出待落账条目，格式为 `pending ledger item: ...`。

不要把“解释性问题”和“审稿问题”混在一起：

- 只影响读懂文本、不影响判断的术语问题，可进入 glossary；
- 影响变量、方法、文献 gap、贡献或审稿建议的问题，应进入 issue ledger；
- 同一个问题可以同时进入 glossary 和 issue ledger，但职责要分清。

每条 issue 至少记录：

- issue id：如 `RQ-001`、`LIT-001`、`VAR-001`、`ID-001`、`RES-001`；
- short title / 简题；
- issue type：literature / theory / variable-measurement / identification / data-sample / results-narrative / writing-clarity / extraction-qc；
- evidence location：段落、表格、公式或章节；
- observed concern：现在看到的疑惑；
- why it matters：为什么影响审稿判断；
- status：`questioned / needs-verification / weak-supported / unsupported / overclaimed / resolved`；
- severity：`major-candidate / minor-candidate / clarification / watchlist`；
- route：后续交给哪个模块；
- next action：下一步怎么核验；
- reviewer-facing potential：是否可能升级为 author-facing 主要/次要意见。

不要把 issue 写成定罪式结论。快速通读阶段优先使用 `questioned` 或 `needs-verification`。

### 第 4 步文献分支种子

第 3 步必须显式输出第 4 步可直接使用的 literature branch seeds。不要让文献定位模块从散文式摘要里猜检索方向。

至少提取以下入口：

- research-question seed：由研究问题生成的主题检索入口；
- theory seed：理论源头、经典理论、概念框架；
- mechanism seed：论文声称的机制链条；
- treatment / explanatory-variable seed：核心解释变量、处理变量、冲击或技术；
- outcome / dependent-variable seed：因变量、结果变量、升级指标或绩效维度；
- data / setting seed：国家、行业、样本单位、数据库、时间跨度；
- method / identification seed：主模型、识别策略、工具变量、匹配方法、变量构造；
- benchmark seed：作者已经引用或必须面对的经典文献、关键作者、关键词组合；
- Chinese-literature seed：需要用中文高质量文献核验的中文概念、政策语境或本土研究线索。

每个 seed 应尽量包含：

- seed label；
- terms / aliases；
- evidence location；
- why it matters；
- suggested sources；
- priority；
- handoff note。

`suggested sources` 可以使用：

- `WoS`;
- `OpenAlex`;
- `CNKI`;
- `EBSCO`;
- `CNKI sentence search`;
- `CNKI cited-by`;
- `reference audit`。

`priority` 可以使用：

- `high`：直接决定文献 gap 或贡献判断；
- `medium`：影响机制、变量或情境定位；
- `low`：背景或表达层补充。

## 输出格式

建议使用 `templates/quick-read-contribution-chain-template.md`。

若没有模板，按以下结构输出：

```markdown
---
type: quick-read-contribution-chain
status: draft
---

# Quick Read Contribution Chain

## One-Paragraph Synopsis

For English manuscripts, include:

- Chinese working synopsis as the main text;
- key English terms in parentheses where needed.

## 一句话发现 / Core Finding Sentence

先抽出全篇论文的轴心关系：X 是谁，Y 是谁，X 如何影响 Y。机制、模型、方法、稳健性、异质性和进一步研究都应围绕这句话展开。

至少记录：

- X / 解释变量；
- Y / 被解释变量；
- Direction / 方向；
- Setting / 对象场景；
- Time / 时间；
- Mechanisms / 机制；
- Boundary / 异质性或边界；
- Evidence / 证据类型；
- One-sentence finding / 一句话发现。

同时必须把核心 X/Y 从简单标签拆成 construct 表，至少包括：

- role：X、Y、机制变量、异质性变量或拓展变量；
- concept / 概念：作者想讨论的理论或经济概念；
- meaning / 含义：该概念在本文语境中的意思；
- operationalization / 操作化指标：作者实际用什么变量、数据或口径测量；
- author justification with quote / 文中说明与辩护：作者如何说明该操作化是合理的，并用短引文锚定；
- evidence location：段落、表格、公式或章节位置；
- audit hook / 审查入口：后续应交给变量测量、方法识别、文献定位或结果叙事中的哪一项。

引用规则：

- 原稿是英文时，`author justification with quote` 应保留英文短引文，并可在引文前后用中文解释。
- 引文只取必要短句，避免长段复制。
- 引文格式使用 Markdown blockquote，例如 `> EPSijt is the export product structure...`。
- 如果作者没有明确辩护，只能写“未见充分辩护”，不要替作者补辩护。

## Glossary and Knowledge Gaps / 术语解释与需补充知识

快速通读产物必须处理“读者会卡住”的术语，而不是把所有缩写原样丢给后续模块。

应登记以下类型：

- 缩写或变量名：如 `EPS`、`CHF`、`ESI`、`ESQ`；
- 数据库或数据源：如 `ASIF`、`China Customs`、`IFR`；
- 分类口径：如 `HS6`、`HS8`、new product list；
- 方法或识别术语：如 `IV`、`PSM`、`firm FE`、`year#industry FE`；
- 作者自造或不常见表达：如 robot suitability、absorptive capacity indicator；
- 后续审稿必须理解、但当前稿件解释不足的概念。

每个术语至少记录：

- term / 术语；
- plain Chinese explanation / 白话解释；
- author's explanation / 作者是否说明；
- evidence location；
- why it matters / 为什么重要；
- next action / 后续动作。

行内说明规则：

- 如果某个术语第一次出现在 quick-read 正文中且可能阻碍理解，可在句后加一条 Obsidian 注释：`%%解释说明：HS8 = 用 8 位 HS 海关编码更细地识别机器人产品。%%`
- 注释应短，只解释“读懂这句话需要知道什么”。
- 如果解释依赖外部知识而非作者说明，应标记 `需后续核查`。
- 不要用行内解释替代术语表；行内解释用于顺读，术语表用于审查。

## Construct-to-Variable Mapping / 概念到变量映射

如果核心发现中的 X、Y、机制变量、IV 或拓展变量不是直接可观测对象，quick-read 必须把“理论概念如何变成实证变量”的链条展开。

这与术语表不同：

- glossary 解释“HS6 是什么”；
- construct-to-variable mapping 解释“HS6 如何参与 EPS 的构造”。

至少覆盖：

- core X / 解释变量；
- core Y / 被解释变量；
- identification variables / IV、treatment timing、matching variables；
- mechanism variables；
- extension outcomes。

每条链至少记录：

- construct / 理论或经济概念；
- mapping steps / 构造步骤；
- plain explanation / 白话解释；
- author basis / 作者依据或引用；
- evidence location；
- weak link / 可能断点；
- audit route / 后续审查模块。

如果某一步依赖外部文献、数据库、代码表、concordance 或作者未展开的处理，标记为 `needs verification`。

## Contribution Chain

For English manuscripts, prefer:

| 节点 | 中文主体阐述（保留关键英文术语） | Evidence Location | 初步风险 | Next Module |
|---|---|---|---|---|

## Section Map

## Key Constructs and Variables

## Data and Empirical Design

## Headline Findings

## Claimed Contributions

## Step 4 Literature Branch Seeds

## Initial Reviewer Questions

这些问题必须同步或迁移到 `notes/review-issue-ledger.md`；quick-read 文档中只保留摘要性问题清单。

## Next-Step Routing
```

## 判断纪律

- 先还原作者声称，再记录初步疑问。
- 不把初步疑问写成最终审稿结论。
- 不生成可直接提交的 author-facing 或 editor-facing 审稿意见。
- 不因摘要或引言写得漂亮就接受贡献声明；只标为待核查。
- 不因机器抽取文本有问题就批评论文本身；抽取问题应回到文本底稿 QC。
- 对需要外部文献核验、方法细读或数据核查的问题，明确路由到后续模块。
- 如果期刊政策限制 AI 使用，输出只作为私人阅读组织材料，并按项目敏感边界处理。

## 完成标准

- 已形成一页到数页的贡献链还原 Markdown。
- 已先抽出 `一句话发现 / Core Finding Sentence`，明确 X、Y、方向、场景、机制、边界和证据。
- 研究问题、文献缺口、理论机制、变量、数据、识别策略、主要结果和贡献叙事均有明确记录。
- 每个核心判断尽量带段落、表格或章节位置。
- 英文稿应以中文主体阐述，同时保留关键英文术语、变量名、核心原文短语和 evidence location；中文稿默认不强制英文版本。
- 已显式输出 `Step 4 Literature Branch Seeds`，使文献定位模块可以直接生成检索分支。
- 已初始化或更新 `notes/review-issue-ledger.md`，把疑惑点、脆弱点和可能断点从聊天/散文摘要中落到账上。
- 初步风险被标注为问题或待核查项，而非最终结论。
- 明确下一步应进入文献定位、方法审查、变量审查、结果叙事检查中的哪一项。
