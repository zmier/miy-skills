---
name: research-literature-reader
description: workflow-research 的研究项目文献阅读编排子 Skill。用于在学术研究项目中，围绕当前 task、candidate research route、实验设计、变量构造、识别策略、数据需求、机制、稳健性、写作范式或期刊定位读取一篇或一组文献；把 PDF、Markdown、coauthor 备注和项目数据约束转化为可复用研究资产。需要按论文建立 raw PDF、restored Markdown、task-specific extraction、route mapping、writing patterns 和 reading logs，并可编排 scholar-pdf-markdown-restoration、workflow-paper-learning、workflow-argument-validity、scholar-kit 与 task-driven-project-manager。
---

# Research Literature Reader

状态：`seed / forward-test-with-CASE-260521`

## 定位

本 Skill 是 `workflow-research` 的项目级文献阅读编排层，不是 PDF 转 Markdown 工具，也不是通用 literature review 生成器。

它回答：

```text
在一个探索性研究项目中，如何带着当前 task / candidate route 去读文献，并把文献转化为后续可复用的研究资产？
```

核心原则：

```text
当前 task / route 决定读什么；
文献资产沉淀决定以后能否复用；
PDF 还原、论文学习、论证审计和 task 管理由相邻 Skill 承接。
```

阅读主轴：

```text
作者断言
-> 命题拆解
-> 凭什么链
-> 项目迁移
```

不要把文献阅读降成模块摘要。文献综述、理论构建、变量构造、识别设计、替代解释、稳健性和项目迁移等模块，本质上都应服务于回答：

```text
作者凭什么让我们相信核心断言？
```

如果核心发现是复合命题，必须先拆命题支，再分别寻找每个命题支所需的 proxy、warrant、evidence 和排除性检验。变量是证明 claim 的工具，不是独立于 claim 的填空栏目。

编排边界：

```text
research-literature-reader 决定文献资产结构、阅读问题和研究用途；
scholar-pdf-markdown-restoration 决定 PDF 还原质量标准和 QC provenance；
task-specific reading / route mapping / writing patterns 由本 Skill 收口。
```

因此，调用 PDF restoration 后必须做资产整理，不得让 PDF restoration 的 TASK 结构直接替代文献阅读资产结构。

## 项目语境与回挂边界

本 Skill 只在 project / task / route / node 语境中负责“回挂”。如果用户只是单独学习一篇论文、做个人摘要或通用模板拆解，不应为了形式完整而伪造 task、route 或 node；此时应转交 `paper-reading` 或 `workflow-paper` 的学论文路线，保留论文自身阅读产物即可。

项目型文献阅读的判断标准：

```text
存在当前 research project；
存在当前 task / route / node；
用户明确要求文献服务实验设计、变量构造、机制、识别、数据需求或写作迁移；
阅读产物需要进入项目复盘、路线取舍或后续 paper 化。
```

若满足项目语境，本 Skill 负责决定并执行阅读产出回挂：

```text
paper-reading 管“怎么读”和“读出了什么”；
research-literature-reader 管“这些产出如何进入项目资产图”。
```

项目型阅读完成后，应判断是否需要更新：

```text
当前 TASK 的 reading contribution ledger；
相关 route / node 的 linked papers、evidence、design options、data needs 或 threats；
文献文件夹的 README / reading-log；
项目级 logs/log.md；
workflow-research/logs 中的可迁移流程洞见。
```

没有 project / task / route / node 语境时，不强制回挂，只保留用户要求的 paper-level 产物。

## 内部结构

本 Skill 是复合 Skill。项目级父入口负责文献资产、task / route / provenance；单篇或一组文献怎么读，先路由到二级父 Skill：

```text
skills/paper-reading/SKILL.md
```

`paper-reading` 再编排单篇论文阅读管线：

```text
paper-extract：
  结构化自动抽取层；
  先生成 automatic-extraction.md。

paper-co-read：
  协同共读层；
  读取 automatic-extraction.md，生成 Paper Orientation Card 和 discussion-outline.md。

paper-finalize：
  核验定稿层；
  回到 PDF / restored manuscript / tables / figures / source anchors；
  生成 final-literature-note.md / verified-claims.md / source-check-log.md。

automatic file output：
  文件资产化输出；
  基于 automatic-extraction.md 生成 task-specific extraction / route map / writing patterns。
```

不要把 `collaborative-reading` 和 `automatic-summary` 直接当作项目级平行能力。新的默认关系是：

```text
PDF / Markdown substrate
  -> paper-extract
     automatic-extraction.md
  -> paper-co-read / paper-finalize / automatic file output
     discussion-outline.md / final-literature-note.md / task-specific extraction / route map / writing patterns
```

验证期暂保留旧 `collaborative-reading` 和 `automatic-summary` Skill，不删除；新共同读任务优先走 `paper-extract -> paper-co-read`，最终可引用任务走 `paper-extract -> paper-finalize`。

三条正式路线：

```text
默认推荐：
  paper-extract -> paper-co-read -> paper-finalize

用户明确要求先核验：
  paper-extract -> paper-finalize -> paper-co-read

批量 / 正式文献库：
  paper-extract -> paper-finalize
```

`paper-finalize` 是核验定稿层，不是 first-pass 抽取层。若没有 `automatic-extraction.md`，必须先运行 `paper-extract`。若没有 `discussion-outline.md` 但用户要求先核验，必须标记为 `cold-start finalization`。

## 底稿状态词

本 Skill 接收 PDF restoration 产物时必须沿用明确状态词：

```text
extraction candidate = 机器抽取候选，只能辅助定位，不可作为主阅读底稿；
rough reading draft = 正文可粗读，但表格、公式、图像和关键页仍需回 PDF；
degraded reading draft = 已知存在明显缺陷，只能降级使用；
table-leak high risk = 表格行/图注/表注被编号为普通 [para]，不能作为经验设计阅读底稿；
primary reading substrate = 已通过 routing / leak scan / 基础 QC，可进入文献阅读；
restored manuscript = 完成逐章还原和必要视觉 QC 的可信稿。
```

`manuscript_paragraphs.md` 不自动等于 `primary reading substrate`。

## 输入

优先定位：

- project README、docs、logs 和 tasks；
- 当前 task 说明、task log、coauthor 备注、候选 routes；
- 原始 PDF 或 PDF 目录；
- 已有 Markdown / restored Markdown / extraction logs；
- 主数据链接、字段说明、数据缺口和合规边界。

若用户只给出 PDF 目录，先列出论文清单，并判断哪些文献和当前 task / route 关系最直接。

## 阅读管线路由

当用户要“读一篇 / 一组文献”时，先路由到 `skills/paper-reading/SKILL.md` 判断阅读管线。

管线判断：

```text
用户还没读、要求先讲解、边读边讨论、需要继续追问
  -> paper-extract -> paper-co-read

用户明确要求最终文献笔记、可引用结论、source-check、核表格、核公式
  -> paper-extract -> paper-finalize

用户明确要求先核验再共同读
  -> paper-extract -> paper-finalize -> paper-co-read

用户明确要求自动总结、批量整理、直接生成文件产物
  -> paper-extract -> automatic file output 或 paper-finalize

用户明确要求批量 / 正式文献库 / 可引用文献条目
  -> paper-extract -> paper-finalize

用户要从文献服务某个 task / route
  -> 先 paper-extract，再按用户意图进入 co-read、finalize 或资产沉淀
```

协同共读模式的第一轮必须基于 `automatic-extraction.md` 在对话窗口返回 Paper Orientation Card：

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

在 `paper-co-read` 模式下，第一轮应同时创建或更新 `discussion-outline.md`，保存 Orientation Card Snapshot、初始 Agenda、首轮 Discussion Ledger 和 pending 项。未经用户确认，不要直接写满 `TASKxx-design-extraction.md`、`route-map.md` 或 `writing-patterns.md`。

如果没有可用 `automatic-extraction.md`，必须先运行 `paper-extract` 生成最小结构化抽取底稿，再进入共同读。

## 阅读产出回挂

在项目语境中，文献阅读结束不等于“文件已经生成”。还需要把阅读产出登记回项目上下文，使后续可以回答：

```text
为了哪个 task 读了这篇文献；
读出了哪些产物；
这些产物贡献到哪些 route / node；
它对 claim、proxy、data need、design option、evidence 或 threat 的影响是什么；
哪些内容只是阅读草稿，哪些已经 source-checked；
哪些判断仍需要用户讨论或后续核验。
```

推荐在当前 task 的说明文件或专门 ledger 中维护：

```markdown
## 文献阅读产出回挂

| Ref | 文献 | 阅读产出链接 | 贡献到哪些 Node / Route | 对本 Task 的作用 | 状态 |
|---|---|---|---|---|---|
```

回挂粒度：

```text
task ledger：记录本 task 为什么读、读出了什么、链接在哪里；
node / route：记录这篇文献怎样改变 claim / proxy / design / threat；
paper folder：记录该文献自身的 extraction / co-read / finalize / logs；
project log：只记录跨 node 的路线判断、重大取舍或 workflow 反哺。
```

不要把完整读书笔记塞回 task 文件。task 文件只保留索引、贡献说明和状态，详细内容留在单篇文献文件夹。

## 文献资产结构

一篇文献建议对应一个文件夹。若项目已有目录结构，优先兼容现状；若需要新建，使用下列形状：

```text
<paper-slug>/
├── 0-raw/
│   └── <title>.pdf
├── 1-md/
│   ├── manuscript_raw.md
│   ├── manuscript_paragraphs.md
│   ├── manuscript_restored.md
│   ├── sections/
│   ├── sections-restored/
│   ├── page-images/
│   ├── tables-restored/
│   └── figures-restored/
├── 2-task-readings/
│   ├── TASK01-automatic-extraction.md
│   ├── TASK01-discussion-outline.md
│   ├── TASK01-final-literature-note.md
│   ├── TASK01-verified-claims.md
│   └── TASK01-design-extraction.md
├── 3-route-mapping/
│   └── route-map.md
├── 4-writing-patterns/
│   └── writing-patterns.md
├── tasks/
│   ├── TASK01-PDF转分章Markdown/
│   └── TASK02-Docling抽取对比/
└── logs/
    ├── extraction-routing-qc.md
    ├── restoration-qc.md
    ├── table-visual-qc.md
    ├── figure-visual-qc.md
    ├── TASK01-source-check-log.md
    └── reading-log.md
```

最小可接受结构：

```text
raw source；
restored reading substrate；
automatic extraction；
discussion outline；
final literature note / verified claims / source-check log；
task-specific extraction；
route / claim mapping；
writing-pattern extraction；
logs / provenance。
```

不要把所有阅读笔记塞进一个总文件。要能回答：

```text
这篇文献的原文在哪里；
可信 Markdown 底稿在哪里；
本 task 当时从中提取了什么；
它支持或威胁哪条 candidate route；
后续写作时可复用哪些范式；
哪些判断仍未核验。
```

## PDF Restoration 产物适配

当本 Skill 调用 `scholar-pdf-markdown-restoration` 时，分两阶段处理：

```text
先提取：由 scholar-pdf-markdown-restoration 产出 PDF restoration / extraction / QC 产物；
再整理：由 research-literature-reader 把产物映射回文献资产结构，并继续做 task-specific reading。
```

### 提取阶段

提取阶段可以由主 Agent 执行，也可以在合适时开 subAgent / worker。无论谁执行，都必须遵守 `scholar-pdf-markdown-restoration` 的 QC 标准。

提取阶段常见产物：

```text
tasks/TASKxx-PDF转分章Markdown/
├── outputs/
│   ├── manuscript_raw.md
│   ├── manuscript_paragraphs.md
│   ├── manuscript_restored.md
│   ├── sections/
│   ├── sections-restored/
│   ├── page-images/
│   ├── tables-restored/
│   ├── figures-restored/
│   ├── comparison-report.md
│   └── metadata.json
└── logs/
    ├── extraction-log.md
    ├── extraction-routing-qc.md
    ├── restoration-qc.md
    ├── table-visual-qc.md
    └── figure-visual-qc.md
```

这些 `tasks/` 目录保存可复现过程、中间候选和实验性抽取结果；它们不是文献阅读的最终入口。

### 整理阶段

提取后，主 Agent 必须整理出文献阅读入口：

- 将原始 PDF 纳入 `0-raw/`，或用相对链接记录其当前位置；
- 将可读 Markdown 底稿、段落稿、restored 稿、section 文件和图表资产同步或索引到 `1-md/`；
- 将 restoration / extraction / visual QC 日志同步或索引到 `logs/`；
- 在 `2-task-readings/` 中记录本 task 读到了什么，而不是把 restoration 报告当阅读笔记；
- 在 task-specific extraction 的 `Source` 中明确写出 Markdown substrate 和 restoration status；
- 若 Markdown 仍是 rough draft / degraded / pending visual QC，则阅读产物也必须标记为 reading draft / degraded。

推荐整理规则：

```text
tasks/ = 可复现过程、候选抽取器输出、Docling comparison、QC 原始记录；
1-md/ = 文献阅读使用的稳定 Markdown substrate 和资产入口；
2-task-readings/ = 当前 task / route 的设计提取；
3-route-mapping/ = 文献与 candidate route / claim 的映射；
4-writing-patterns/ = 可复用写作范式；
logs/ = 跨阶段 provenance 和剩余风险。
```

### 软链 / 索引组织原则

若 PDF restoration 已经在 `tasks/` 下产生了较完整的过程产物，整理阶段优先使用相对软链或索引文件建立稳定入口，而不是复制一份新的大文件或 Markdown：

```text
0-raw/source.pdf -> ../inputs/<source>.pdf
1-md/manuscript_paragraphs.md -> ../tasks/TASKxx-PDF转分章Markdown/outputs/manuscript_paragraphs.md
1-md/sections -> ../tasks/TASKxx-PDF转分章Markdown/outputs/sections
1-md/page-images -> ../tasks/TASKxx-PDF转分章Markdown/outputs/page-images
logs/restoration-qc.md -> ../tasks/TASKxx-PDF转分章Markdown/logs/restoration-qc.md
logs/extraction-routing-qc.md -> ../tasks/TASKxx-Docling抽取对比/logs/extraction-routing-qc.md
```

这样做的目标是把“阅读入口”和“过程证据”分开：

```text
稳定入口：0-raw / 1-md / 2-task-readings / 3-route-mapping / 4-writing-patterns / logs
过程证据：tasks / inputs / extractor outputs / comparison candidates
```

使用软链时遵守：

- 优先使用相对路径，保证整个 paper folder 移动时仍尽量可用；
- 软链只指向同一篇文献目录内部的文件，不跨项目乱链；
- `README.md` 或 `1-md/README.md` 必须说明哪些入口是 reading substrate、哪些只是 candidate / comparison；
- 若软链指向的是 rough draft / candidate extraction，不得命名为 `manuscript_restored.md`，除非已经达到 restoration 完成标准；
- 若目标是外部交付、归档打包、跨机器同步或上传到不保留 symlink 的系统，应改为复制稳定产物，或在 README 中明确软链依赖；
- 不用软链掩盖 provenance：原始 `tasks/` 仍应保留，除非用户明确要求清理且已确认无复盘价值。

不要把 `scholar-pdf-markdown-restoration` 的完整 TASK 输出原样当作 `research-literature-reader` 的完成产物。PDF restoration 完成只说明“阅读底稿准备好了或降级准备好了”，不说明文献阅读已经完成。

## Markdown Substrate Acceptance Gate

主 Agent 在把 PDF restoration 产物接入 `1-md/` 之前，必须执行接收验收。验收失败时，不能把该 Markdown 放为主阅读底稿。

接收前检查：

- 是否存在 `logs/extraction-routing-qc.md`；
- 是否存在 `logs/restoration-qc.md`；
- 是否存在 `logs/table-leak-qc.md` 或 `logs/table-visual-qc.md`，尤其是 empirical / table-heavy paper；
- `restoration-qc.md` 是否声明 `rough`、`degraded`、`table-leak high risk`、`pending visual QC`；
- 研究任务是否会使用变量定义、系数、样本量、R2、机制表、robustness 表；
- 关键表 / 图是否至少 `page-level visual checked`；
- 是否有 Docling / 多抽取器 comparison report 或明确说明为何不需要；
- 是否存在 table rows、figure captions、references、appendix 被普通 `[para]` 编号的迹象。

### 接收规则

```text
primary reading substrate:
  可软链到 1-md/manuscript_paragraphs.md 或 1-md/manuscript_restored.md。

rough / degraded / table-leak high risk:
  只能放到 1-md/candidates/ 或在 1-md/README.md 显著标注为 not primary substrate。

table-heavy empirical paper:
  若无 routing QC + table-leak scan + 关键表 QC，不得进入 design extraction。
```

若必须先保留降级稿以便后续修复，应：

- 在 `README.md` 和 `1-md/README.md` 写明 `not primary substrate`；
- 在 `2-task-readings/TASKxx-design-extraction.md` 的 `Source` 写明不得引用表格行；
- 在 `logs/reading-log.md` 记录接收失败原因和下一步 restoration blocking task；
- 对需要的关键表优先回到 `scholar-pdf-markdown-restoration` 修复。

## SubAgent 使用原则

subAgent 是可选加速器，不是默认流程。开 subAgent 会增加 token 消耗，因为 subAgent 需要读取 Skill / PDF / logs，主 Agent 后续还需要读取其 summary / metadata / QC 产物。

适合开 subAgent 的情况：

- 批量文献的 PDF restoration、Docling comparison、page image rendering 或 metadata 生成；
- 单篇 PDF 很长、表格多、工具运行耗时长；
- restoration 任务边界清楚，能限制写入范围，例如只写 `tasks/TASKxx-Docling抽取对比/`；
- subAgent 可以输出短小、结构化、可追溯的 `metadata.json` / `comparison-report.md` / QC log；
- 主 Agent 后续只需读 summary、metadata、QC 和与当前 task 相关的段落 / 表格，而不必重读全部 raw extraction。

不适合开 subAgent 的情况：

- 只有一篇短文，主 Agent 接下来必须逐段深读；
- 当前 research route 仍很模糊，需要边读边形成问题；
- subAgent 输出会很长，主 Agent 仍需重新校验大部分内容；
- 本轮目标是研究判断、实验设计和 route mapping，而不是工具型抽取。

分工原则：

```text
subAgent / restoration worker：
  负责“抽”和“核”：PDF -> markdown substrate + QC provenance。

main Agent / research-literature-reader：
  负责“归档”和“读”：把 substrate 整理进文献资产结构，
  再围绕当前 task / route 完成 design extraction、route mapping 和 writing-pattern extraction。
```

如果使用 subAgent，主 Agent 给出的任务必须包含：

- 明确写入范围；
- 不得覆盖已有 TASK 或用户文件；
- 需要读取的 Skill / reference；
- 需要生成的固定产物；
- 最终必须用 compact report 汇报状态；
- 明确声明是否 `not_full_restoration`、`pending visual QC` 或 `degraded`。

## 执行协议

1. 明确本轮阅读目的和阅读管线：
   - 设计实验；
   - 找变量 / 数据；
   - 学识别策略；
   - 学机制和异质性；
   - 找 robustness；
   - 学写作范式；
   - 判断 candidate route 是否值得推进。
2. 若目标是读单篇或一组文献，先调用 `skills/paper-reading/SKILL.md`，编排 `paper-extract -> paper-co-read` 或 `paper-extract -> automatic file output`。
3. 若目标是读单篇或一组文献，先确认或生成 `automatic-extraction.md`；这是共同读和文件资产化输出的上游结构化底稿。
4. 在 `paper-co-read` 模式下，基于 `automatic-extraction.md` 先在对话窗口返回 Paper Orientation Card；同一轮在文件侧创建或更新 `discussion-outline.md` 作为协同阅读工作台；等用户追问、确认或要求保存后，再继续 task-specific extraction、route map 或 writing patterns 等资产沉淀。
5. 读取当前 project / task / route 材料，写出本轮文献阅读问题清单。
6. 定位 PDF 与已有 Markdown。若没有可信 Markdown，转入 `scholar-pdf-markdown-restoration`；执行前读取该 Skill，并按其 routing / table-leak / QC 规则产出 restored Markdown、primary reading substrate 或明确降级状态。
7. 若 PDF restoration 较重，判断是否开 subAgent。只有工具型、边界清楚、可产出 compact QC 的任务才交给 subAgent；研究阅读判断不得完全外包。
8. 建立或补全文献文件夹。不要移动用户已有文件，除非用户明确要求；可用索引或相对软链先把原始 PDF 纳入资产图。
9. 执行 Markdown Substrate Acceptance Gate。若底稿是 `extraction candidate`、`degraded reading draft` 或 `table-leak high risk`，不得作为主阅读底稿进入 design extraction。
10. 将 restoration 产物整理回文献资产结构：`tasks/` 保存过程，`1-md/` 保存阅读底稿入口，`logs/` 保存 QC / provenance；若使用软链，需确认软链可解析，并在 README 中说明入口状态。验收失败稿放入 `1-md/candidates/` 或显著标为 `not primary substrate`。
11. 做 task-specific extraction。面向实验设计时，至少提取：
   - one-sentence core finding / 作者断言；
   - claim decomposition / 命题拆解；
   - claim-warrant map / 凭什么链；
   - research question；
   - empirical setting / data；
   - treatment / exposure / event；
   - outcome variables；
   - key explanatory variables；
   - identification strategy；
   - controls / fixed effects；
   - mechanism and heterogeneity；
   - robustness / placebo；
   - contribution claim；
   - what maps to current project；
   - what does not transfer；
   - data needed beyond current project data；
   - threats and unresolved questions。
12. 做 route mapping：
   - 这篇文献支持哪条 candidate route；
   - 它提供的是主干设计、机制、变量、robustness、写作范式还是反例；
   - 它要求补充哪些数据；
   - 它暴露哪些识别威胁。
13. 若本轮目标包含写作，单独写 `4-writing-patterns/writing-patterns.md`。不要把写作范式混进实验设计提取里。
14. 若存在 project / task / route / node 语境，更新当前 task 的 reading contribution ledger，并把关键产出回挂到相关 route / node。
15. 更新 task log，记录本轮读文献的目的、模式、输入、产物、回挂对象、未解决风险和下一步。
16. 将可能可迁移的流程洞见先写入 `workflow-research/logs` 或项目 log，不直接提升为稳定 reference。

## TASK01 设计提取模板

用于 `TASK01-coauthor-literature-to-design` 这类“从 coauthor 文献到第一版实验设计”的阅读：

```markdown
# <Paper Title> - TASK01 Design Extraction

## Source

- PDF:
- Markdown substrate:
- Restoration / reading status:
- Read date:
- Current task:
- Candidate route:

## Why This Paper Matters For This Task

## Claim-Warrant Map

- Core claim:
- Logical form:
- Proposition branches:
- For each branch:
  - abstract object:
  - observable proxy:
  - warrant:
  - evidence:
  - competing explanations:

## Core Design

- Research question:
- Setting and sample:
- Data:
- Treatment / exposure / event:
- Outcomes:
- Key variables:
- Identification:
- Controls / fixed effects:
- Mechanism:
- Heterogeneity:
- Robustness:

## Transfer To 基金经理请回答

- Directly reusable:
- Requires adaptation:
- Not transferable:
- Data we already have:
- Data we need:
- Measurement idea:
- Identification threat:

## Route Mapping

- Main route supported:
- Possible branch route:
- Could become:
- Current confidence:

## Open Questions
```

## 输出

一次完成的文献阅读应至少更新：

- 单篇文献文件夹的 `0-raw/`、`1-md/` 和 `logs/` 入口；
- 单篇文献文件夹中的 task-specific extraction；
- route mapping 或 task 输出文件；
- 若有 project / task / route / node 语境，更新 task reading contribution ledger 和相关 route / node；
- task log；
- 若有 PDF 转 Markdown，更新 restoration QC；
- 若有 Docling / 多抽取器 forward-test，更新 comparison report 和 metadata，并在阅读入口标明不是 full restoration；
- 若使用相对软链组织资产，确认链接可解析，并在 README / `1-md/README.md` 说明 provenance 和适用边界；
- 若底稿未通过 acceptance gate，输出 restoration blocking note，而不是继续做 design extraction；
- 若有可迁移 workflow 洞见，更新 project log 或 `workflow-research/logs`。

## 完成标准

- 本轮阅读问题来自当前 task / route，而不是无目标摘抄。
- 已判断是否存在 project / task / route / node 语境；没有项目语境时，不伪造回挂对象。
- 已判断阅读管线；共同读时先有 automatic-extraction.md，再返回 Paper Orientation Card；自动文件输出时标明文件产物范围。
- 原始文献、Markdown 底稿、阅读产物和日志可追溯。
- 稳定入口和过程产物已区分；若用软链组织，链接可解析，且不会把 candidate extraction 误标为 restored manuscript。
- Markdown substrate 已通过接收验收；若未通过，已降级为 candidate / degraded，并停止依赖该稿做实验设计提取。
- 若调用了 PDF restoration，已将 restoration 产物整理为文献资产结构；不能只留下 restoration TASK。
- 若使用 subAgent，主 Agent 已读取 compact report / metadata / QC，并完成资产整理与研究阅读判断。
- 明确说明哪些设计可迁移到当前项目，哪些不可迁移。
- 明确列出当前主数据已经满足什么、还缺什么数据。
- 明确记录识别威胁和下一步实验设计问题。
- 若存在 project / task / route / node 语境，已把阅读产物链接回 task ledger，并更新相关 route / node 的证据、设计或风险状态。
- 如果 Markdown 底稿未完成可靠还原，最终产物必须标为 reading draft / degraded，不得声称已完成精读。
- 对 empirical / table-heavy paper，若存在 `table-leak high risk`，不得完成 design extraction，除非本轮只提取非表格的研究问题和下一步修复任务。

## 禁止事项

- 不把 PDF 转 Markdown 当成文献阅读完成。
- 不在用户要求共同读时跳过 automatic-extraction.md。
- 不在用户要求共同读时直接进入自动摘要或完整文件沉淀。
- 不把 Paper Orientation Card 当成最终精读结论。
- 不把 discussion-outline.md 当成 automatic-extraction.md。
- 不把 `scholar-pdf-markdown-restoration` 的 TASK 结构直接当成文献资产结构完成。
- 不复制或移动大文件制造多套不一致版本；优先用相对软链 / 索引建立入口，除非外部交付或跨机器归档需要真实副本。
- 不把 `manuscript_paragraphs.md` 自动当作主阅读底稿；没有 routing QC / table-leak scan / restoration status 的稿件必须先验收。
- 不在 `table-leak high risk` 状态下引用 `[para]` 中的表格行、系数、显著性、样本量或 R2。
- 不默认开 subAgent；不要为了并行而让主 Agent 和 subAgent 重复阅读全文。
- 不把 subAgent 的 restoration summary 当成研究判断或 route mapping。
- 不把单篇文献读成泛泛摘要，而忽略当前 task / route。
- 不把 task-specific 阅读笔记当成永久稳定的 project-level 结论。
- 不在没有项目语境时强制创建 task / route / node 回挂。
- 不把完整读书笔记塞回 task ledger；task ledger 只保存索引、贡献说明和状态。
- 不在没有数据和识别检查时宣称某条 route 已经成立。
- 不把写作范式、实验设计、变量构造和引用信息混在同一个不可复盘文件里。
