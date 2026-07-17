---
name: collaborative-reading
description: paper-reading 的协同阅读模式。用于用户还没读过论文、希望 Agent 先在对话窗口讲解论文、边读边问、共同判断重点、逐步决定是否沉淀文件的场景；必须先在对话窗口返回低假设 Paper Orientation Card，覆盖一句话核心发现、命题结构初判、按命题支组织的可观察对象 / proxy、机制、文献对话、research gap 和项目可迁移性；同时在文件侧创建或更新 discussion-outline.md，保存 Orientation Card Snapshot 和初始 Discussion Agenda，再等待用户追问或确认。
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

卡片采用低假设结构，不预设所有论文都能压成单一 `主 X / 主 Y`。优先包含：

```text
一句话核心发现；
形式逻辑结构初判；
命题支初判；
每个命题支的待证对象；
每个命题支中的可观察对象 / proxy；
主机制；
文献 / 学术基础和对话；
research gap；
对当前项目的初步可迁移性；
建议下一步深读位置。
```

如果论文确实是单一因果 / 相关关系，可以在对应命题支下标注 X/Y；如果 A01 是复合命题，不得预设全篇只有一组 X/Y。进入 Discussion Agenda 后，必须先回到 A01 的命题结构，再判断每个命题支分别需要哪些可观察对象、proxy、warrant 和 evidence。

即使在第一轮 Paper Orientation Card 中，也要把“命题支的理论待证关系”和“可观察对象 / proxy 初判”分成不同小段。命题支小段应优先写理论对象和理论关系；`media coverage`、`PROPENSITY_BUY_MEDIA`、alpha、具体表格结果等 proxy / measure / empirical result 应放到 `Argument-Scoped Observables / Proxies` 或 A03 草案中，避免第一轮就把 A02 和 A03 糊在一起。

### 一句话核心发现原则

`一句话核心发现` 应停留在 claim 层，回答：

```text
这篇文献最想让读者相信什么？
```

它要是一个简短有力的断言，足够锋利，更像“文献最想让人带走的那颗钉子”。优先表达最核心的理论对象、方向性关系或主张张力，而不是研究场景导览。

`一句话核心发现` 应优先使用作者主张中的理论对象 / 抽象构念，而不是直接使用经验 proxy。若摘要或结果段用 proxy 表达发现，必须先向上还原为理论命题；proxy 放到 A03 的 operationalization / proxy bridge 中。只有当论文的核心 claim 本身就是 measurement / proxy claim 时，才把 proxy 放进 A01，并显式标注它就是被论证对象。

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

如果一个候选句包含 `PROPENSITY_BUY_MEDIA`、`media-covered stocks buying tendency` 这类变量或代理指标，先检查它是否只是理论命题的经验版本。若是，应将 A01 写成理论层命题，把该变量留给 A03 解释其如何代理理论对象。

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
凭什么这么说？ -> 命题拆解 / proxy bridge / evidence；
怎么证明？ -> identification / empirical design；
为什么是这个机制？ -> mechanism / alternative explanations；
还可能是什么？ -> robustness / boundary conditions；
对当前项目有什么用？ -> transfer / route mapping。
```

不要把证据层、变量代理、识别设计、机制检验、robustness 或结果组合塞进一句话。代理变量和证据链应放到后续 Agenda 项，如命题拆解、proxy bridge、机制、识别、设计或证据讨论。

### 社会研究方法锚点：A01-A03

A01/A02/A03 可以用《社会研究方法》的标准研究链条校准，但不得因此改变本 Skill 的主结构：

```text
A01 = 命题 / 假设；
A02 = 概念、构念、理论关系、文献基础；
A03 = 概念操作化 / 指标选择 / proxy bridge。
```

这组锚点用于防止三个常见混淆：

```text
把主题当命题；
把 proxy 当理论概念；
把操作化、测量、研究设计和统计结果混成一段。
```

使用顺序：

```text
A01 先问：作者要读者相信的命题是什么？
A02 再问：这个命题涉及哪些理论概念 / 构念，它们之间是什么关系，既有文献知道什么、缺什么？
A03 再问：这些抽象概念和理论关系如何被操作化为可观察 proxy / measure / empirical relation？
```

注意：社会研究方法中的“概念 -> 变量 -> 指标”链条，主要服务 A03；不要把指标、变量名或数据构造提前塞进 A01/A02。

### A01 之后的论证结构规则

A02/A03 不是固定的“X/Y 填空题”。A01 负责识别作者核心断言、还原逻辑形态、拆出 core proposition branches，并建立 `P1 / P2 / P3` 编号；A02 负责追问作者如何论证每个 `Pi`。

核心要求：沿着“作者如何论证 A01”往下走。X、Y、proxy、warrant 和 evidence 都必须放回作者的论证任务中理解。若 A01 是复合命题，就不能预设全篇只有一组 X/Y；每个 `Pi` 都要先被还原成自己的论证结构。

同时要避免反向过度拆解：不是所有出现在摘要、introduction 或结果段里的判断都应升级为并列核心命题支。A02 必须先区分：

```text
core proposition branches:
  A01 本身需要读者相信的核心命题支；
  若删除该支，核心发现会变形或塌掉。

supporting / boundary / exclusion branches:
  operationalization / proxy bridge：说明抽象对象如何被观察或测量；
  mechanism / warrant：解释核心命题为什么可能成立；
  boundary condition：说明核心命题在何处更强、更弱或适用；
  exclusion / alternative explanation：说明为什么不是别的原因；
  robustness / design support：说明结果不是口径、样本或模型偶然造成。
```

这些辅助分支仍然重要，但它们服务于论证核心命题，不应自动写成 A01 的并列 P1/P2/P3/P4。

特别注意：`operationalization / proxy bridge` 不得写入 A01 的 core logical form，也不得伪装成 A02 的 proof burden。凡是“A 通过某个 proxy 表现出来”“作者用变量 X 测量 A”“指标 M 代表理论对象 A”这类句子，默认属于 A03，而不是 A01 的核心命题支。只有当论文本身的核心贡献就是提出或验证一个 measurement construct 时，才可把 measurement claim 写入 A01，并显式标注。

### Proposition ID System

一旦 A01 识别出核心命题支，必须给每个核心命题支分配稳定编号 `P1`、`P2`、`P3`。这些编号不是一次性分析草稿，而是协同阅读的持久索引。

编号规则：

```text
P1 / P2 / P3:
  只分配给 core proposition branches。

S-Pi-*:
  分配给服务于 Pi 的 supporting branches，
  例如 operationalization、mechanism、boundary、exclusion、robustness。
```

后续 Agenda 必须尽量回挂这些编号：

```text
A03-P1 / A03-P2:
  每个核心命题支的 operationalization / proxy bridge。

A04-P1 / A04-P2:
  每个核心命题支的 measurement / data construction。

A05-Pi:
  每个核心命题支的 research design / identification strategy。

A06-Pi:
  每个核心命题支的 data analysis / empirical results。

A07-Pi:
  每个核心命题支的 alternative explanations / robustness / validity threats。

A08-Pi:
  项目迁移可复用哪个命题支的设计。
```

如果某个后续讨论服务整篇论文而非单一命题支，可标 `P-all`。若暂时无法判断，标 `P?`，并在 open questions 中保留回挂问题。

这套编号用于防止后续推进时断线：看到 A01 有 `P1`、`P2`，就知道 A03 至少要分别检查 `A03-P1`、`A03-P2`；A04/A05/A06/A07/A08 也应说明自己服务哪一个 `Pi`。

### A02 Proof Structure Rule

A02 不再重复拆 A01。A02 的任务是：对每个 core proposition `Pi`，还原作者要证明它时使用的理论层 proof structure，并说明该关系在既有文献中的知识基础。

特别注意：A02 必须停留在理论对象和理论关系层，不得让具体 proxy 提前登场。`media coverage`、`PROPENSITY_BUY_MEDIA`、具体 alpha 指标、具体表格结果等，默认属于 A03/A04/A06/A07，而不是 A02。

从社会研究方法视角看，A02 对应“概念 / 构念 / 变量关系 / 文献基础”的理论层工作。它不是测量，也不是变量表。A02 应先回答：

```text
Pi 中的核心概念 / 构念是什么？
这些概念之间被作者设定为什么关系？
既有文献已经支持到哪里？
尚未解决的研究缺口在哪里？
本文要把哪一段关系推进为可检验命题？
```

若 A02 中出现数据库字段、回归变量、样本口径、表格结果或具体统计系数，通常说明已经滑入 A03/A04/A05/A06/A07。

默认结构：

```text
Pi:
  Pi-X = 理论上的解释对象 / 触发对象 / 处理对象；
  Pi-Y = 理论上的被解释对象 / 行为结果 / 后果对象；
  Pi-R = Pi-X 与 Pi-Y 之间的方向性关系或可检验关系。
  Pi-KB = 既有文献对 Pi-X、Pi-Y、Pi-R 的知识基础、已知结论和缺口。
```

`Pi-KB` 不得只写成 open question。第一轮即使不能完整展开，也必须给出 first-pass knowledge-base 判断：

```text
已有文献大致知道什么；
已有文献尚未解决什么；
本文试图推进哪一段关系。
```

若底稿证据不足，写 `needs-source-check`，但仍要说明需要回到 introduction / literature paragraphs 核对哪一条文献基础。

不是所有 `Pi` 都必须是因果命题；可以是相关、存在性、差异、后果、机制或边界命题。但 A02 必须把它改写成“作者需要证明什么关系 / 差异 / 存在性”：

```text
存在性命题：
  Pi-X 是否存在于研究对象中？
  经验上应出现什么可观察模式？

关系 / 因果命题：
  Pi-X 是什么？
  Pi-Y 是什么？
  Pi-R 是正向、负向、条件关系还是异质性关系？
  Pi-KB 中已有研究支持到哪里，本文要推进哪里？

后果命题：
  Pi-X 是某种行为 / 特征 / 暴露；
  Pi-Y 是后果；
  Pi-R 是 Pi-X 对 Pi-Y 的预测、关联或因果影响。
```

A02 只做 proof structure，不做 proxy bridge 细节，不罗列统计结果，也不把 diagnostic pattern / exclusion test 当成第一层 proof burden：

```text
A02:
  还原 Pi-X / Pi-Y / Pi-R；
  说明作者要证明的理论关系是什么；
  说明相关文献基础中什么已知、什么未知。

A03:
  Pi-X / Pi-Y 如何被 proxy / observable measurement 捕捉。

A04:
  proxy / measure 在数据中如何被具体量出来。

A05:
  研究设计如何把变量组织成对 Pi-R 的检验。

A06:
  资料分析和结果如何支持或不支持 Pi-R。

A07:
  diagnostic pattern、robustness、exclusion test、validity threats 放在这里或挂回相应 Pi。
```

错误信号：

```text
在 A02 中直接写 media coverage、PROPENSITY_BUY_MEDIA、future alpha、Table 9 等具体 proxy / 指标 / 结果；
把“如果媒体覆盖把股票推入注意力集合……”写成 A02-P1，而不是等到 A03-P1 才讨论 media coverage 如何代理 attention trigger；
把“买入端强于卖出端”直接写成 P1 的 proof burden，而不是 P1-R 的 diagnostic pattern；
把 RPI、flow-catering、tone/content 直接写成 P1 的 proof burden，而不是 alternative explanation / exclusion；
把 PROPENSITY_BUY_MEDIA 的构造直接写成 P2 的 proof burden，而不是 A03-P2 的 proxy bridge；
只列一串作者“需要论证的点”，却没有还原 Pi-X / Pi-Y / Pi-R。
```

最小例：

```text
P1：基金经理受有限注意力影响。

合格 A02-P1：
  P1-X = 有限注意力 / 注意力约束；
  P1-Y = 基金经理交易行为 / 投资选择；
  P1-R = 有限注意力会系统性影响基金经理交易行为；
  P1-KB = 既有文献支持有限注意力会影响投资者行为 / 市场反应，
          但专业基金经理是否同样受影响仍是本文要推进的问题。

不合格 A02-P1：
  P1-X = 媒体覆盖；
  P1-Y = 基金买入；
  P1-R = 媒体覆盖股票更容易被买入。

原因：
  这已经进入 A03-P1 / A05-P1 / A06-P1 / A07-P1；
  media coverage 是 P1-X 的 proxy，不是 A02 的理论对象。
```

处理顺序：

```text
1. 还原 A01 的逻辑形态：
   直言 / 假言 / 联言 / 选言 / 嵌套复合命题。

2. 若 A01 = P1 且 P2：
   在 A01 中拆出 P1/P2，并在 A02 中分别还原 P1/P2 的 proof structure。

3. 标注每个分支的角色：
   core proposition / operationalization / mechanism / boundary / exclusion / robustness。

4. 建立 Proposition Registry：
   为 core branches 分配 P1/P2/P3；
   为 supporting branches 标明其服务的 Pi。

5. 若某个核心命题支是 Bx -> By：
   分别还原 Bx 和 By 的理论对象、可观察 proxy、warrant 和 evidence。

6. 再填写变量：
   变量不是从论文格式中机械摘出来的，而是服务于证明某个命题支。
```

推荐把 A01/A02/A03 理解为：

```text
A01 Core Claim And Logical Form:
  A01 包含哪些 core proposition branches？
  哪些内容只是 operationalization / mechanism / boundary / exclusion / robustness support？
  为 core branches 分配哪些稳定 Proposition IDs？

A02 Proof Structure / Argument Plan:
  每个 Pi 要被证明为什么理论关系 / 差异 / 存在性？
  Pi-X / Pi-Y / Pi-R 分别是什么？
  哪些 diagnostic / exclusion / robustness 只是后续支撑，而不是 Pi 的第一层结构？

A03 Operationalization / Proxy Bridge:
  每个 Pi-X / Pi-Y 中的抽象对象如何落到可观察变量？
  proxy 凭什么能代表理论对象？
  这个 proxy bridge 依赖哪些 warrant / evidence / 排除性检验？
```

A03 必须承接 A02 的 proof structure，不得凭空列 proxy。对每个 `Pi`，至少拆成：

```text
A03-Pi-X:
  Pi-X 如何被 observable / proxy 捕捉？
  作者凭什么说这个 proxy 能代表 Pi-X？
  该 proxy 的主要威胁或竞争解释是什么？

A03-Pi-Y:
  Pi-Y 如何被 observable / measurement 捕捉？
  作者凭什么说这个 measurement 能代表 Pi-Y？
  该 measurement 的主要误差、遗漏或边界是什么？

A03-Pi-R:
  Pi-R 如何被经验化为可检验关系？
  这个 empirical relation 为什么对应理论关系 Pi-R，而不是偷换问题？
  作者准备用哪些 design / evidence / diagnostic pattern 支撑该关系？
```

在 `discussion-outline.md` 的 A03 detail table 中，只要 A02 已经写出 `Pi-R`，就必须显式保留 `A03-Pi-R` 行。不能只列 `A03-Pi-X` 和 `A03-Pi-Y`，否则会把“概念如何测量”与“理论关系如何被经验检验”断开。

每个 A03 条目至少包含四列：

```text
A02 object / relation；
empirical proxy / measure / relation；
why credible；
remaining threats / competing interpretations。
```

从社会研究方法视角看，A03 对应“概念操作化”：把 A02 的抽象概念、构念和理论关系转成可观察、可测量的经验对象。A03 的核心不是“变量叫什么”，而是：

```text
抽象概念如何进入经验世界？
proxy / measure 与理论对象之间的对应关系是什么？
这个对应关系的效度凭什么成立？
哪些测量误差、替代解释或构念效度威胁仍然存在？
```

A03 可以提到 measure / proxy，但不要展开完整数据构造、样本筛选、变量计算细节或回归设计。那些应在后续 Agenda 中处理：

```text
A04 Measurement / Data Construction:
  数据来源、分析单位、样本范围、时间窗口、变量计算、信度 / 效度 / 测量误差。

A05 Research Design / Identification Strategy:
  变量如何组成检验、研究方式、控制逻辑、时间顺序、识别威胁。

A06 Data Analysis / Empirical Results:
  估计结果、方向、显著性、经济意义、异质性、机制性结果如何回答 Pi-R。

A07 Alternative Explanations / Robustness / Validity Threats:
  替代解释、排除性检验、robustness、内部 / 外部 / 构念 / 统计结论有效性威胁。
```

注意区分：

```text
Pi-X proxy:
  理论解释对象如何被观察。

Pi-Y proxy:
  理论结果对象如何被观察。

Pi-R empirical relation:
  理论关系如何被经验检验。
```

不要把 `Pi-X proxy`、`Pi-Y proxy` 和 `Pi-R empirical relation` 混成一段。若在 A03 中出现“X 影响 Y 的统计结果”，应标明这是 `Pi-R empirical relation`，但详细数据构造、研究设计、统计结果和有效性威胁应分别放到 A04/A05/A06/A07。

A03 的数量跟随 A01 的 `core proposition branches`，不跟随论文格式中的 `X/Y` 字段：

```text
如果 A01 = P1：
  A03 = A03-P1。

如果 A01 = P1 且 P2：
  A03 = A03-P1 + A03-P2。

如果 A01 = P1 且 P2 且 P3：
  A03 = A03-P1 + A03-P2 + A03-P3。

如果某个 Pi 不是 core proposition branch，
而是 operationalization / mechanism / boundary / exclusion / robustness，
则不要生成 A03-Pi；
把它挂回它服务的 core branch。
```

每个 `A03-Pi` 至少回答：

```text
Pi 的 abstract objects 是什么？
哪些对象不可直接观察？
作者用哪些 observable / proxy 表示它们？
proxy bridge 的 warrant 是什么？
有哪些 evidence 支撑这个 bridge？
有哪些 competing interpretations 必须排除？
如果 Pi 是条件命题或关系命题，Bx / By 分别如何观察，Bx -> By 如何被估计？
```

若已经有 A02 的 `Pi-X / Pi-Y / Pi-R`，以上问题必须分别对应到 `Pi-X`、`Pi-Y`、`Pi-R`，不能只写一个全局 `A03-Pi` 段落。

反例：

```text
不合格：
X = 媒体覆盖；Y = 基金业绩。

合格：
A01 = P1 且 P2。
P1 需要证明“基金经理受有限注意力影响”：
  X1 = 股票媒体覆盖 / attention exposure；
  Y1 = 基金买入行为；
  warrant = 媒体覆盖降低搜索成本，把股票推入注意力集合。
P2 需要证明“受有限注意力影响越大，表现越差”：
  X2 = PROPENSITY_BUY_MEDIA；
  Y2 = future alpha / performance；
  warrant = 若交易由注意力驱动而非信息优势驱动，应不产生超额收益，甚至伤害表现。
```

这条规则用于防止把复合命题偷换成单组 X/Y。合格的协同阅读应把变量放回论证树：变量是证明某个 claim 的工具，不是独立于 claim 的栏目。

### A04-A07 Research Methods Chain

A03 之后，Agenda 应沿《社会研究方法》的经验研究链条继续推进。默认结构为：

```text
A04 Measurement / Data Construction
A05 Research Design / Identification Strategy
A06 Data Analysis / Empirical Results
A07 Alternative Explanations / Robustness / Validity Threats
```

这四项不是论文八股栏目，而是继续回答 A01 的“凭什么”。它们必须回挂 `P1 / P2 / P3`，说明自己服务哪个核心命题支。

#### A04 Measurement / Data Construction

A04 的任务是回答：A03 选出的 proxy / measure 在数据中到底如何被量出来。

默认检查：

```text
数据来源是什么？
分析单位是什么：个体、基金、基金-股票、基金-季度、公司-年等？
样本范围和排除规则是什么？
时间窗口如何定义，是否与 Pi-R 的时间顺序匹配？
变量如何计算，聚合层级是什么？
测量客体、测量内容、测量法则分别是什么？
信度、效度、缺失值、测量误差、频率错配风险是什么？
```

A04 与 A03 的边界：

```text
A03:
  为什么这个 proxy / measure 能代表理论对象？

A04:
  这个 proxy / measure 在数据中如何被具体构造和量化？
```

如果 A04 直接讨论“这个估计能否支持因果解释”，通常已经进入 A05/A07。

#### A05 Research Design / Identification Strategy

A05 的任务是回答：作者如何把 A04 中构造出的变量组织成对 `Pi-R` 的检验。

默认检查：

```text
研究方式是什么：实验、准实验、面板回归、事件研究、预测设计、调查、现存统计资料分析？
核心检验式或比较逻辑是什么？
时间顺序是否清楚：X / exposure / treatment 是否先于 Y？
控制变量、固定效应、匹配、分组、对照逻辑是什么？
估计支持的是相关、预测、机制解释，还是因果解释？
设计最关键的识别假设是什么？
哪些命题支有独立设计，哪些只是辅助诊断？
```

注意：不要把所有论文都称为“实验设计”。只有当论文确实使用实验或准实验逻辑时，才使用 experiment / quasi-experiment；否则用更通用的 research design / identification strategy。

#### A06 Data Analysis / Empirical Results

A06 的任务是回答：资料分析和结果是否支持 `Pi-R`。

默认检查：

```text
主要结果回答哪个 Pi-R？
结果方向是否与理论预测一致？
统计显著性与经济意义分别如何？
结果是否跨模型、样本、时间窗口或指标保持一致？
异质性、机制性结果或诊断性模式服务哪个 Pi？
哪些结果只是辅助支撑，不应升级为新的 core proposition？
```

A06 不应只是罗列表格。每个结果都要说明它回答哪一个“凭什么”。

#### A07 Alternative Explanations / Robustness / Validity Threats

A07 的任务是回答：为什么不是别的原因，为什么结果不是口径、样本、模型或测量偶然造成的。

默认检查：

```text
作者排除了哪些替代解释？
robustness 检验改变了什么口径、样本、模型或变量？
diagnostic pattern 是否与理论机制一致？
还有哪些未被排除的竞争解释？
内部有效性、外部有效性、构念有效性、统计结论有效性分别有什么风险？
这些风险影响的是 P1、P2、P3，还是整篇论文的 P-all？
```

A07 与 A05 的边界：

```text
A05:
  研究设计如何试图识别 / 检验 Pi-R？

A07:
  这个设计和结果还有哪些有效性威胁，作者如何排除或缓解？
```

#### Mechanism / Literature / Gap 的位置

机制、文献对话和 research gap 仍然重要，但不再默认占用 A04-A06 的主编号。它们应作为支撑信息挂回相应位置：

```text
机制 / warrant:
  可写入 A02 的 Pi-R 理论关系、A05 的设计逻辑、A06 的机制性结果，或 A07 的 diagnostic pattern。

文献对话 / knowledge base:
  优先写入 A02 的 Pi-KB；若需要项目资产化，可在 A08 中总结。

research gap:
  优先写入 A02 的 Pi-KB 和 A08 的迁移判断；若服务整篇论文，可标 P-all。
```

这样做不是削弱机制、文献和 gap，而是把它们放回“作者如何论证核心命题”的链条中。

错误信号：

```text
看到论文后直接问“本文的 X/Y 是什么”，而不是先问“作者要证明哪个命题支”；
把一个复合断言压成单组 X/Y；
把边界条件、替代解释、robustness 或机制检验直接升级为并列核心命题；
把“理论对象如何被 proxy 观察到”写成 A01 的并列核心命题；
把 proxy 当成核心 claim，而不说明它服务于哪个命题支的论证；
把 evidence 罗列成结果摘要，而不说明它回答的是哪一个“凭什么”。
```

判断规则：

```text
如果一句话写成“作者通过 A/B/C/D 证据证明……”，通常已经过度展开。
如果一句话必须依赖“用什么变量代理 / 在什么样本检验 / 做了哪些 robustness”才成立，通常还不够 claim-level。
如果一句话把“proxy 越高，Y 越低”直接当作核心发现，先问它是否应还原为“理论对象越强，Y 越低”。
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

Proxy note:
`买入媒体报道股票的倾向` / `PROPENSITY_BUY_MEDIA` 是经验 proxy，应在 A03 说明它如何代理“受有限注意力影响越大”，而不是直接替代理论层 A01。
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
