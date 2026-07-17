---
name: paper-extract
description: paper-reading 的论文结构化自动抽取层。用于在共同读、自动摘要、task-specific extraction 或 route mapping 之前，先基于可信 Markdown / PDF 底稿生成可复用的 automatic-extraction.md；必须按 A01-A08 抽取作者核心断言、形式逻辑结构、命题支、理论关系、proxy bridge、测量与数据、研究设计、结果、有效性威胁和项目迁移初判，并标明 source anchors、底稿状态和剩余不确定性。
---

# Paper Extract

状态：`seed / extraction-first`

## 定位

本 Skill 是 `paper-reading` 的结构化自动抽取层，不是对话讲解层。

它回答：

```text
在进入共同读或文件资产化之前，Agent 应先把论文抽成什么结构化阅读底稿？
```

核心产物是：

```text
automatic-extraction.md
```

该产物是后续 `paper-co-read`、automatic summary、task-specific extraction、route map、writing patterns 和 UAT 的共同输入。

## 与 paper-co-read 的关系

```text
paper-extract:
  负责结构化理解和抽取；
  产出 automatic-extraction.md；
  可独立作为文件资产。

paper-co-read:
  读取 automatic-extraction.md；
  生成 Paper Orientation Card 和 Discussion Agenda；
  维护 discussion-outline.md；
  与用户共同追问、纠偏、深化。
```

共同读不是跳过自动抽。若用户要求共同读但没有 `automatic-extraction.md`，应先运行本 Skill 生成最小可用抽取，再进入 `paper-co-read`。

## 输入

必须确认：

```text
source PDF / Markdown substrate；
reading substrate status；
当前 task / route；
用户本轮阅读目的；
已有 extraction / discussion-outline / route-map 是否存在。
```

若 Markdown substrate 是 `rough / degraded / table-leak high risk`，必须在输出中显著标注边界；empirical / table-heavy paper 不得在缺少表格 QC 时引用表格系数、样本量、R2 或显著性。

## 输出路径

推荐路径：

```text
2-task-readings/<TASKxx>-automatic-extraction.md
```

若不属于特定 task：

```text
logs/automatic-extraction.md
```

如果项目已有命名习惯，优先兼容现状，但文件名必须清楚表示这是结构化自动抽取底稿，而不是 discussion outline 或最终 design extraction。

模板见：

```text
templates/automatic-extraction-template.md
```

## 抽取主轴

不得按论文模块机械摘要。必须沿着：

```text
作者断言
-> 命题结构
-> 凭什么链
-> 研究方法链
-> 项目迁移
```

若核心发现是复合命题，先拆成 `P1 / P2 / P3`。后续 A02-A08 必须回挂 proposition IDs。

拆分命题支时必须先区分：

```text
core proposition branches:
  A01 本身需要读者相信的核心命题；
  删除后核心发现会变形或塌掉。

supporting branches:
  proxy bridge；
  mechanism / warrant；
  diagnostic implication；
  boundary condition；
  exclusion / alternative explanation；
  robustness / validity support。
```

机制、替代解释、排除性检验、robustness、diagnostic pattern 默认是 `S-Pi-*` 或 `P-all` 支撑分支，不得自动升级为 `P4 / P5` 核心命题。只有当论文的核心发现本身就是机制命题或边界命题时，才可升级为 core proposition，并必须说明理由。

核心命题准入测试：

```text
collapse test:
  如果删除该命题，一句话核心发现是否会变形、坍塌或失去主要贡献？
  是 -> 可列为 core proposition。
  否 -> 默认 supporting branch。

take-away test:
  论文最想让读者带走的是这个断言本身，
  还是用这个断言来证明另一个核心断言？
  若是后者 -> supporting branch。

independence test:
  该命题是否有独立的理论对象、理论关系和经验证明链？
  还是只是某个 Pi 的机制推导、诊断预测、边界条件或排除检验？
  若是后者 -> supporting branch。
```

支撑分支类型：

```text
S-Pi-mechanism:
  解释为什么 Pi 成立。

S-Pi-diagnostic:
  若 Pi 成立，应该观察到的诊断性模式。

S-Pi-proxy:
  证明某个 proxy / measure 可以代表理论对象。

S-Pi-exclusion:
  排除替代解释或竞争性假设。

S-Pi-robustness:
  证明结果不是模型、样本、口径或窗口偶然造成。

S-Pi-boundary:
  说明 Pi 在哪些条件下更强、更弱或不成立。

S-Pi-measurement:
  支撑测量和数据构造可信。
```

如果某个分支重要但角色不确定，先标为：

```text
candidate S/P:
  重要，但暂不确定是 core proposition 还是 supporting branch；
  在 co-reading 中作为待确认问题提出。
```

不得因为某个机制、边界或诊断模式“很重要”就自动升格为 P3。重要 supporting branch 可以继续进入 A03-A07，但编号必须保留其支撑角色。

贯穿规则：

```text
core proposition:
  A02-Pi / A03-Pi / A04-Pi / A05-Pi / A06-Pi / A07-Pi。

supporting branch:
  A02-S-Pi-* / A03-S-Pi-* / A04-S-Pi-* / A05-S-Pi-* / A06-S-Pi-* / A07-S-Pi-*。
```

不要为了让后续 A03-A07 有内容而把 supporting branch 改名成 P3。编号的作用是保留论证角色，而不是压低重要性。

## A01 Core Claim And Logical Form

A01 抽取作者最想让读者相信的核心命题。

必须包含：

```text
一句话核心发现：理论纯净版；
一句话核心发现：读者导览版；
形式逻辑完整还原版；
简单 / 复合命题判断；
命题支 P1 / P2 / P3；
哪些只是 supporting branch 及其类型；
candidate S/P；
source anchors；
needs-source-check。
```

一句话核心发现必须是形式逻辑意义下可判断真假的命题，可为直言、假言、联言或选言命题。优先使用理论对象 / 抽象构念，而不是 empirical proxy。

一句话核心发现必须保存双版本：

```text
理论纯净版:
  用理论对象 / 抽象构念 / 理论关系表达；
  用于 A01、Proposition Registry、后续论证树；
  不写 proxy、变量名、数据字段、表格结果。

读者导览版:
  可以加入本文的关键 empirical implementation，帮助用户快速进入论文；
  用于 Paper Orientation Card 或口头导览；
  必须明确它是导览版，不得替代理论纯净版。
```

示例：

```text
理论纯净版：
  基金经理受有限注意力影响；且受影响越强，未来投资表现越差。

读者导览版：
  媒体报道把股票推入基金经理注意范围并诱发买入；这种买入倾向越强，未来基金业绩越差。
```

A01 不得把经验 proxy 写成理论核心断言。若候选句含 `media coverage`、`PROPENSITY_BUY_MEDIA`、alpha、table result 等经验对象，先问它们是否只是理论对象的操作化版本；若是，移到 A03/A04/A06。

理论纯度闸门：

```text
A01 的核心命题必须先写理论层：
  谁 / 什么抽象构念；
  影响什么抽象行为或后果；
  关系是存在、方向、条件、程度还是后果。

经验层只能在 A01 中作为短注出现：
  “作者后续用某 proxy 操作化”，但不得替代理论命题本身。
```

自检问题：

```text
如果一句话核心发现删掉所有变量名、数据库字段、回归构造和表格结果后就无法成立，
说明它可能还停留在 empirical summary，而不是 theory-level proposition。
```

命题角色自检：

```text
完成 A01 后逐项检查：
  P1 / P2 / P3 是否都通过 collapse test、take-away test 和 independence test？
  任何未通过的 P 都应降为 S-Pi-* 或 candidate S/P。

特别注意：
  “买入端强于卖出端”“某机制下应出现某模式”“某替代解释不成立”
  通常是 diagnostic / mechanism / exclusion supporting branch，
  不是默认 core proposition。
```

## A02 Proof Structure / Argument Plan

A02 是对 A01 核心命题的逆向概念拆解，不是继续摘要论文，也不是全篇概念清单。

社会研究方法中的正向研究过程通常是：

```text
现象 -> 概念化 -> 命题 / 假设 -> 操作化 -> 测量
```

读一篇已经写完的论文时，A02 采用逆过程：

```text
A01 已确定 Pi 命题
  -> A02 忠实形式逻辑化该命题
  -> A02 从命题逆拆顶层概念
  -> A02 系统拆分顶层概念的子概念 / 维度 / 构成要素 / 边界条件 / 机制候选
  -> A02 建立概念层级、共享概念复用和 relation IDs
  -> A02 还原概念之间的理论关系和文献基础
  -> A03 基于 A02 concept / relation IDs 进入操作化 / proxy bridge
```

A02 必须以 `P1 / P2 / P3` 为作用域。概念跟着命题走，不得先列一个全篇概念清单。

符号必须连续：

```text
A01:
  P1 / P2 / P3

A02:
  P1-C1 / P1-C1.1 / P1-R1；
  P2-C1 / P2-C1.1 / P2-R1；
  Shared-C1 / Shared-C1.1。

A03:
  A03-P1-C1；
  A03-P1-C1.1；
  A03-P1-R1；
  A03-Shared-C1。
```

不得让 A01 是一套命题编号、A02 是一套无来源概念清单、A03 又变成一套变量清单。

### A02.1 忠实形式逻辑化

每个 `Pi` 先从 A01 的命题登记表中取出原命题，改写为形式逻辑完整表述。

形式逻辑化只允许：

```text
补全省略；
还原指代词；
显式标注命题形式；
整理语序，使其成为可判断真假的命题。
```

形式逻辑化不得：

```text
添加机制；
添加 proxy；
添加诊断结果；
添加经验证据；
替作者补一个更强的理论故事。
```

命题形式必须显式标注：

```text
直言命题：X 是 Y。
假言命题：如果 X，那么 Y。
联言命题：X 且 Y。
选言命题：X 或 Y。
```

如果原命题是简写句，先做忠实补全。

示例：

```text
Bad:
  P2：双向互动沟通可以缓解这种困难。

Good:
  P2 原命题简写：双向互动沟通可以缓解这种困难。
  P2 形式逻辑完整表述：双向互动沟通是普通投资者公开信息整合困难的缓解机制。
  P2 命题形式：直言命题。
```

反例：

```text
Bad:
  如果双向互动沟通为普通投资者提供解释、澄清和纠偏，
  那么普通投资者的公开信息整合困难会降低。

问题：
  这不是原命题的形式逻辑化，而是添加了机制内容。
  “解释、澄清和纠偏”应进入机制 / warrant / 子概念候选，不应塞进 Pi 的形式逻辑完整句。
```

### A02.2 命题域概念拆解

从形式逻辑完整命题中直接拆出来的，才是该 `Pi` 的顶层概念。

每个 `Pi` 必须维护：

```text
Pi top-level concepts；
Pi concept internal decomposition；
Pi relation IDs；
Pi-KB / literature basis。
```

不要把顶层概念、子概念、机制、维度、状态变化、诊断结果和 proxy 平铺成同一层。

每个 top-level concept 必须检查是否需要继续拆分：

```text
父概念 / 所属更抽象概念；
理论维度；
构成要素；
边界条件；
状态变化；
机制候选；
与同一 Pi 中其他概念的关系；
停止拆分理由。
```

停止拆分只在以下情况成立：

```text
下一层已经是 empirical proxy / observable measure / data field；
论文没有提供更细理论结构，继续拆分只能靠 Agent 推断；
该子概念对当前 Pi 的证明链没有实质作用；
该内容应进入 A03 / A04 / A05 / A06 / A07。
```

若继续拆分来自 Agent 推断而非作者文本，必须标注 `inferred`；若需要回原文核对，标注 `needs-source-check`。

示例：

```text
P2 形式逻辑完整表述：
  双向互动沟通是普通投资者公开信息整合困难的缓解机制。

P2 顶层概念：
  P2-C1：双向互动沟通；
  P2-C2：普通投资者公开信息整合困难。

P2 概念关系：
  P2-C1 是 P2-C2 的缓解机制。

P2 子概念 / 机制候选：
  P2-C1.1：解释；
  P2-C1.2：澄清；
  P2-C1.3：纠偏。

P2 支撑 / 诊断分支：
  S-P2-diagnostic-liquidity；
  S-P2-diagnostic-price-informativeness。
```

A02 子概念不是 proxy。判断标准：

```text
A02 子概念:
  概念内部的理论维度、构成部分、边界条件、机制候选或状态变化。

A03 proxy:
  作者用来观察 / 测量该概念或关系的经验对象、变量、文本分类、模型结果或诊断模式。
```

### A02.3 共享概念复用

如果多个命题使用同一个理论对象，必须建立 `Shared Concept Registry` 并让各 `Pi` 引用它。

不要在不同命题中重复发明同一概念的不同写法。

示例：

```text
Shared-C1：普通投资者；
Shared-C2：公开信息；
Shared-C3：公开信息整合困难；
Shared-C4：普通投资者公开信息整合困难。

P1 使用 Shared-C4 来证明该困难存在；
P2 使用 Shared-C4 来证明该困难可被缓解。
```

共享概念的作用是让全文论证树紧密：同一概念可以在不同命题中承担不同论证角色，但应保持同一个 concept ID。

共享概念也可以有子概念：

```text
Shared-C3：信息整合困难；
Shared-C3.1：awareness costs；
Shared-C3.2：acquisition costs；
Shared-C3.3：integration costs；
Shared-C3.3.1：理解公开信息；
Shared-C3.3.2：组合多源信息；
Shared-C3.3.3：转化为投资判断。
```

若某个 Shared-C 在不同 Pi 中角色不同，必须写明：

```text
P1 中：待证明其存在；
P2 中：待证明其可被缓解。
```

关系摘要默认结构：

```text
Pi-Rk = 某个 Pi 内的概念关系 ID；
linked concept IDs = 该关系连接哪些 Pi-C / Shared-C；
relation statement = 用自然语言忠实表达概念关系；
relation type = categorical / causal / association / mechanism / boundary；
Pi-KB = 既有文献对这些概念和关系的知识基础、已知结论和缺口。
```

`Pi-X / Pi-Y / Pi-R` 这类写法只可作为临时理解辅助，不是 A02 的主表结构。A02 主表必须使用 `Concept ID`、`Child Concept ID`、`Relation ID` 和 `linked concept IDs`。

A02 必须停留在理论对象和理论关系层。`media coverage`、`PROPENSITY_BUY_MEDIA`、具体 alpha、表格结果等默认不属于 A02。

A02 的常见错误：

```text
Bad:
  P1-X = media coverage；
  P1-R = media coverage -> fund buying。

Good:
  P1-X = 有限注意力 / 注意力约束 / 搜索成本；
  P1-Y = 基金经理交易行为；
  P1-R = 有限注意力会系统性影响基金经理交易行为；
  A03 再说明 media coverage 如何代理 attention trigger。
```

若必须在 A02 提到 empirical proxy，只能作为括号提示 `proxy later in A03`，不能替代理论对象。

A02 越界检测：

```text
完成 A02 后逐项检查形式逻辑完整表述、top-level concepts、concept internal decomposition、Shared-C、Relation IDs 和 Pi-KB：
  是否出现可观察变量、数据字段、回归变量、统计构造、表格结果、具体数据库口径？

若出现，判断它是否为论文真正讨论的理论对象本身。
  如果不是，必须移动到 A03 / A04 / A06 / A07。

是否把机制、诊断结果或 proxy 加进了 Pi 形式逻辑完整表述？
  如果是，必须移到 warrant / supporting branch / A03 / A06 / A07。

是否把子概念、机制、状态变化和诊断结果与顶层概念平铺？
  如果是，必须改成 concept hierarchy。

是否在 P1/P2/P3 中重复命名同一概念？
  如果是，必须抽到 Shared Concept Registry 并让各 Pi 引用。
```

常见移动规则：

```text
empirical proxy / observable measure -> A03；
变量如何计算、数据来源、样本窗口 -> A04；
变量为何进入模型、控制变量 / 固定效应的设计功能 -> A05；
表格结果、系数方向、显著性、经济意义 -> A06；
排除解释、robustness、诊断检验 -> A07。
```

## A03 Operationalization / Proxy Bridge

A03 抽取 A02 的理论对象和关系如何被经验化。

每个 A03 bridge 必须回挂一个 A02 node。A02 node 可以是：

```text
Pi-Ck 顶层概念；
Pi-Ck.n 子概念；
Shared-Ck / Shared-Ck.n 共享概念；
Pi-Rk 概念关系；
S-Pi-* supporting branch。
```

不得出现没有 A02 Node ID 的 proxy 行。若阅读 A03 时发现一个 proxy 对应的概念尚未在 A02 登记，必须先回到 A02 增补概念，或在 A03 标记 `A02-revision-needed`。

Bridge ID 必须继承 A02 node ID：

```text
A03-P1-C1；
A03-P1-C1.1；
A03-Shared-C4；
A03-P2-R1；
A03-S-P2-diagnostic-liquidity。
```

两类 bridge 要分清：

```text
Concept-to-proxy bridge:
  某个 A02 概念 / 子概念如何被 observable / proxy 捕捉。

Relation-to-diagnostic bridge:
  某个 A02 关系或 supporting branch 如何通过诊断性经验模式得到支持。
```

每个 bridge 至少包含：

```text
A02 Node ID；
A02 Node Type；
A02 concept / relation；
empirical proxy / measure / relation；
why credible；
remaining threats / competing interpretations；
source anchors。
```

`why credible` 不得只写一句“作者使用该变量”。每个 proxy bridge 必须回答四问：

```text
1. 这个 proxy 代理哪个 A02 理论对象或理论关系？
2. 为什么这个 proxy 有资格代表该理论对象或关系？
3. 作者用了哪些 evidence / diagnostic pattern / exclusion test 支持这个 proxy bridge？
4. 仍有什么测量误差、构念效度风险或竞争解释？
```

A03 只回答“为何可代理 / 如何操作化”，不回答“变量如何在数据中计算”。变量计算、窗口、聚合层级、数据库和样本口径进入 A04。

A03 与 A07 的边界：

```text
A03:
  某个检验如何提高 proxy bridge 的可信度。

A07:
  同一个检验如何排除替代解释、稳健化核心结论或处理有效性威胁。
```

同一项检验可以在 A03 和 A07 同时出现，但必须写清角色不同。

## File Artifact Completeness

当生成、更新或在对话中展示 `automatic-extraction.md` 草案时，必须保持文件产物结构完整。

最小完整草案必须保留：

```text
来源；
抽取状态；
A01 核心断言与形式逻辑；
A01 核心命题准入测试表；
A01 命题登记表；
A02 论证结构 / 理论关系表；
A03 Proxy Bridge 表；
A04 Measurement / Data Block 表；
A05 Design / Identification Block 表；
A06 资料分析 / 经验结果表；
A07 替代解释 / 稳健性 / 有效性威胁表；
A08 迁移到当前项目；
开放问题。
```

不得用自由段落或项目符号替代上述关键表格。若信息不足，保留表格骨架并填写：

```text
needs-source-check；
not yet extracted；
inferred；
unknown from current substrate。
```

允许在对话窗口只展示压缩版 Orientation Card；但一旦展示“会写入本地文件的 automatic-extraction.md 草案”，必须按模板保留表格结构。

## A04 Measurement / Data Construction

A04 抽取“为了检验某个 `Pi-R`，作者需要哪些变量和数据对象，以及这些变量和数据对象在数据中如何被具体量化”。

A04 的组织单位不是全篇变量表，也不是全篇统一 controls，而是：

```text
A04-Pi-R Measurement / Data Block
```

每个 A04 block 服务一个命题关系或 design block，并回挂：

```text
linked proposition / relation:
  它服务哪个 Pi-R。

linked A03 bridges:
  它承接哪些 A03-Pi-Ck / A03-Pi-Ck.n / A03-Pi-Rk / A03-Shared-Ck。

core measures:
  A03 中的 concept proxy / relation diagnostic 如何量；
  数据来源、分析单位、样本、时间窗口、变量计算、聚合层级、滞后 / 分组 / 窗口。

design-support measures:
  为该 Pi-R 设计服务的控制变量、固定效应变量、分组变量、样本筛选变量、滞后项、权重等如何量；
  注意：这些不是全篇统一 controls，而是该 design block 自己的一套支撑变量。

measurement risks:
  缺失值、频率错配、构念效度、测量误差、样本选择、聚合误差、窗口设定风险。
```

边界：

```text
A03:
  为什么这个 proxy / measure 能代表理论对象？

A04:
  这个 proxy / measure 以及该 design block 需要的支撑变量，在数据中如何被量出来？

A05:
  这些变量为什么这样进入模型 / 比较逻辑，以检验 Pi-R？
```

一句话：A04 管“变量如何进入数据”。

输出要求：

```text
automatic-extraction.md 的 A04 必须使用 A04-Pi-R block 表；
不得只列 Media / Funds / Stocks / Controls 这种全局数据清单；
每个 block 必须说明 linked A03 bridges、core measures、design-support measures、measurement risks。
```

## A05 Research Design / Identification Strategy

A05 抽取作者如何把 A04 中构造出来的变量组织成对 `Pi-R` 的检验。

A05 的组织单位是：

```text
A05-Pi-R Design / Identification Block
```

每个 A05 block 应与对应的 A04 block 衔接：

```text
linked proposition / relation:
  它检验哪个 Pi-R。

empirical test / model / comparison logic:
  回归、事件研究、面板设计、预测设计、实验、准实验、分组比较或其他方式。

time order:
  X / exposure / treatment 是否先于 Y；
  滞后窗口、预测窗口如何支持理论顺序。

design function of variables:
  核心 X / Y 如何进入模型；
  控制变量为什么进入模型；
  固定效应控制什么；
  分组 / decile / matching / weights 服务什么比较逻辑。

identification claim:
  支持相关、预测、机制解释还是因果解释；
  作者实际能声称到什么程度。

key assumptions and threats:
  设计依赖什么假设；
  还有什么混淆、反向因果、遗漏变量、选择偏误没有完全解决。
```

不要把所有论文都叫“实验设计”。只有真实使用实验 / 准实验时才使用 experiment / quasi-experiment。

一句话：A05 管“变量为何进入模型，以及模型凭什么检验 Pi-R”。

输出要求：

```text
automatic-extraction.md 的 A05 必须使用 A05-Pi-R block 表；
不得只列 Aggregate regressions / Panel regressions / Alternative tests 这种全局设计清单；
每个 block 必须关联 A04 block，并说明变量的 design function。
```

核心边界：

```text
A04 = data identity:
  变量如何进入数据。

A05 = design function:
  变量为何进入模型。
```

最小正反例：

```text
Bad A04:
  controls = size, B/M, turnover, age, expense, style...

问题：
  暗示全篇共享一套控制变量；
  没有说明这些变量服务哪个 Pi-R；
  混淆了变量如何测量与变量为什么进入模型。

Good A04-P1-R:
  serves P1-R；
  linked A03 = A03-P1-C1 / A03-P1-C1.1 / A03-P1-R1；
  core measures = media coverage、fund buys/sells 的数据构造；
  design-support measures = P1 交易反应设计中的 stock controls、quarter FE、fund FE 等如何量；
  risks = media coverage 是否混入 public information；季度持仓只能观察 net trades。

Good A04-P2-R:
  serves P2-R；
  linked A03 = A03-P2-C1 / A03-P2-C2 / A03-P2-R1；
  core measures = PROPENSITY_BUY_MEDIA、future performance 的数据构造；
  design-support measures = P2 业绩预测设计中的 fund controls、decile ranks、style variables 等如何量；
  risks = propensity 是否混入 skill/style/public-information reliance。

Good A05-P1-R:
  解释为什么 lagged media coverage、stock controls、FE、买入/卖出比较能检验 P1-R。

Good A05-P2-R:
  解释为什么 propensity deciles、future alpha、fund controls 能检验 P2-R，以及该设计是预测、相关、机制解释还是因果解释。
```

## A06 Data Analysis / Empirical Results

A06 抽取结果如何支持或不支持每个 `Pi-R`。

必须说明：

```text
结果服务哪个 Pi；
方向是否符合理论；
统计意义；
经济 / 实质意义；
是否跨模型、样本、窗口、指标稳定；
是主证据、机制证据、诊断证据、异质性还是辅助支撑。
```

不得只罗列表格。

## A07 Alternative Explanations / Robustness / Validity Threats

A07 抽取作者如何处理替代解释、稳健性和有效性威胁。

必须说明：

```text
替代解释；
作者的排除 / robustness / diagnostic test；
内部有效性、外部有效性、构念有效性、统计结论有效性风险；
威胁影响哪个 Pi 或 P-all；
剩余风险。
```

## A08 Transfer To Current Project

A08 抽取对当前项目可迁移的内容。

至少包含：

```text
可直接迁移；
需要改造；
不可迁移；
需要的数据；
当前项目已有数据；
measurement idea；
identification threat；
route mapping 初判；
下一步深读 / 修复位置。
```

## Source Anchors

每个重要判断必须尽量标注 source anchors：

```text
section / table / equation / page / paragraph；
若只来自推断，标 inferred；
若底稿不可靠，标 needs-source-check。
```

自动抽取产物可以有不确定性，但必须把不确定性写出来。

## 完成标准

- 已生成或更新 `automatic-extraction.md`。
- A01-A08 至少有 first-pass 内容。
- A01 同时包含“一句话核心发现：理论纯净版”和“一句话核心发现：读者导览版”。
- A01 包含核心命题准入测试表和命题登记表。
- A02/A03/A04/A05/A06/A07 保留模板表格结构；信息不足时用 `needs-source-check` 或 `not yet extracted` 标注。
- 所有核心命题支都有稳定 proposition IDs。
- A02/A03/A04/A05/A06/A07 不混层。
- 结果、robustness、替代解释都回挂到 Pi。
- 标明 source anchors、reading status、不可引用边界和剩余风险。
- 可作为 `paper-co-read` 的输入。

## 禁止事项

- 不把 automatic extraction 写成普通摘要。
- 不把 discussion-outline 当 automatic-extraction。
- 不把 Paper Orientation Card 当完整抽取产物。
- 不把复合命题压成单组 X/Y。
- 不把 proxy 写成 A01/A02 的理论对象。
- 不在 table-leak high risk 时引用表格细节。
- 不把自动抽取结论直接提升为 project-level 稳定结论。
