# Research Literature Reader Log

## 2026-07-06 ReAct: CASE-260521 weekend effort substrate acceptance 反例

### Trigger

在基金经理研究项目 TASK01 中，`2025 (Not) Everybody's Working for the Weekend A Study of Mutual Fund Manager Effort` 的 PDF 粗抽取稿被整理进 `1-md/` 作为文献阅读入口。用户随后指出 `[para 191]` 等内容实际是 Table 2 的回归表行，而不是自然段。

### Observation

该论文属于 empirical / table-heavy paper。轻量 `pdfplumber` 粗抽脚本生成了 `manuscript_paragraphs.md` 和 page images，但没有：

```text
extraction-routing-qc.md
table-leak scan
table inventory
关键表 page-level visual QC
Docling / 多抽取器 second opinion
```

`research-literature-reader` 将该稿整理为文献资产入口时，虽然标注了 reading draft / pending visual QC，却没有拒收或降级为 candidate。这导致粗抽取稿看起来像可以进入 design extraction。

### Root Cause

本 Skill 缺少 Markdown Substrate Acceptance Gate。

```text
manuscript_paragraphs.md != primary reading substrate
```

特别是对 empirical / table-heavy paper，如果后续任务要学习变量、识别、结果表、机制表或 robustness 表，必须先检查 PDF restoration 的 routing / leak scan / table QC 状态。否则应停止 design extraction，回到 restoration。

### Rule Upgrade

已提升为稳定规则：

- 接收前必须检查 `extraction-routing-qc.md`、`restoration-qc.md`、`table-leak-qc.md` / `table-visual-qc.md`；
- 对 table-heavy empirical paper，若无 routing QC + table-leak scan + 关键表 QC，不得进入 design extraction；
- `extraction candidate`、`degraded reading draft`、`table-leak high risk` 不得作为主阅读底稿；
- 验收失败稿只能放入 `1-md/candidates/`，或在 `1-md/README.md` 显著标为 `not primary substrate`；
- `2-task-readings/TASKxx-design-extraction.md` 的 Source 必须写明底稿状态和不可引用边界；
- 若发现 table-leak，只能提取非表格性的研究问题 / 修复任务，不能引用 `[para]` 中的系数、样本量、R2 或显著性。

### Status Vocabulary

与 `scholar-pdf-markdown-restoration` 对齐：

```text
extraction candidate
rough reading draft
degraded reading draft
table-leak high risk
primary reading substrate
restored manuscript
```

### Lesson

`research-literature-reader` 的职责不是把所有抽取产物都整理得好看，而是决定哪些材料足够可信，可以进入研究阅读。资产整理必须包含拒收能力：不合格底稿要被降级、隔离或退回 restoration，而不是顺滑地进入 `1-md/`。

## 2026-07-06 ReAct: 区分协同阅读与自动摘要模式

### Trigger

在基金经理研究项目中试读 `Shall We Talk?` 时，用户指出 Agent 不应直接把文献读完并写文件。用户本人尚未读过论文，需要先在对话窗口获得一张可讨论的导览卡，再基于该卡追问、纠偏和选择深读方向。

### Observation

当前 Skill 只处理文献资产、底稿接收、task-specific extraction 和 route mapping，没有处理“读文献”的交互模式。它默认更接近自动文献摘要 / 自动提取，而不是协同阅读。

### Rule Upgrade

新增复合 Skill 结构：

```text
research-literature-reader/
├── SKILL.md
├── skills/
│   └── paper-reading/
│       ├── SKILL.md
│       └── skills/
│           ├── collaborative-reading/
│           │   └── SKILL.md
│           └── automatic-summary/
│               └── SKILL.md
```

其中：

```text
research-literature-reader = 项目级文献资产编排；
paper-reading = 单篇 / 一组文献阅读父 Skill；
collaborative-reading = 对话优先模式；
automatic-summary = 文件优先模式。
```

### Paper Orientation Card

协同阅读模式第一步必须在对话中返回：

```text
一句话核心发现；
主 X 及代理变量；
主 Y 及代理变量；
主机制；
文献 / 学术基础和对话；
research gap；
对当前项目的初步可迁移性；
建议下一步深读位置。
```

### Lesson

协同阅读不是自动摘要的弱版本，而是不同的执行模式。它的第一产物是“共同理解界面”，不是文件。只有用户追问、确认或要求保存后，才进入 task-specific extraction、route map 或 writing patterns。

## 2026-07-06 ReAct: 协同阅读需要 discussion outline

### Trigger

用户进一步指出，协同阅读不能只是“Agent 先讲，用户再问”的对话流。它需要一个持续维护的讨论提纲，记录讨论准备围绕什么展开、用户实际问了什么、哪些已讨论、哪些仍 pending、哪些问题超出原提纲。

### Observation

`Paper Orientation Card` 适合作为第一轮导览，但不足以承载长周期协同阅读。用户隔很久回来 review 文献时，不能依赖零散聊天记录恢复上下文。

### Rule Upgrade

`collaborative-reading` 新增主工作台：

```text
discussion-outline.md
```

推荐路径：

```text
2-task-readings/<TASKxx>-discussion-outline.md
```

或非 task 场景：

```text
logs/discussion-outline.md
```

讨论提纲由 `Paper Orientation Card` 展开，并维护：

```text
Orientation Card Snapshot；
Discussion Agenda；
Discussion Ledger；
Agenda Details；
Appendix: Out-Of-Agenda Questions；
Review Snapshot。
```

### Handling Rules

```text
提纲中有，且用户已经讨论：
  更新状态、用户问题、Agent 回答、当前共识、未解决点。

提纲中有，但用户还没讨论：
  保持 pending，不假装完成。

提纲中没有，但用户提出了：
  放入 Appendix，记录用户认知和 Agent 回答，再判断是否提升为 Agenda 项。
```

### Lesson

协同阅读的主产物不是摘要，而是一个可恢复、可复盘、可继续推进的共同工作台。后续 task-specific extraction、route map 和 writing patterns 都应从已讨论并稳定的 outline 条目中提升。

## 2026-07-06 ReAct: 一句话核心发现应停留在 claim 层

### Trigger

在 `Shall We Talk?` 的 A01 讨论中，Agent 曾把一句话核心发现写成包含交易反应、流动性、价格信息含量和复杂度冲击等证据链的长句。用户指出，这过分展开了；最简发现应停留在 claim 层。

### Observation

`Paper Orientation Card` 中的 `一句话核心发现` 是进入协同阅读的第一抓手。如果它混入证据层，用户会难以区分：

```text
作者想让读者相信什么；
作者用什么证据来论证它。
```

这会让后续 Agenda 层级混乱。

### Rule Upgrade

新增规则：

```text
一句话核心发现应停留在 claim 层；
不要把证据层、变量代理、识别设计、机制检验、robustness 或结果组合塞进一句话；
证据链应放到后续 Agenda 项。
```

判断规则：

```text
如果一句话写成“作者通过 A/B/C/D 证据证明……”，通常已经过度展开。
```

### Minimal Example

来自 `Shall We Talk?` 协同阅读：

```text
Bad:
作者通过交易反应、流动性、价格信息含量和会计准则复杂度冲击等证据，论证投资者互动平台揭示并缓解普通投资者的信息整合困难。

Good:
普通投资者存在信息整合困难；投资者互动平台可以缓解这种困难。
```

### Lesson

协同阅读需要先把 claim 和 evidence 分层。A01 只负责最小 claim；A04/A07 等后续 Agenda 再讨论作者如何论证、证据强度和替代解释。

## 2026-07-06 ReAct: 从八股模块到“凭什么链”

### Trigger

在 `Does Media Coverage of Stocks Affect Mutual Funds' Trading and Performance?` 的协同阅读中，用户指出：文献综述、理论构建、变量构造、实验设计、替代解释、稳健性和项目迁移这些模块，本质上都应服务于回答“凭什么”。如果只是按论文八股模块罗列，得到的是形式摘要，不是实质论证线。

### Insight

论文阅读主线应从：

```text
文献综述 -> 理论 -> 数据 -> 变量 -> 识别 -> 结果 -> 稳健性
```

升级为：

```text
作者断言 C
-> 凭什么 C 值得问
-> 凭什么 X 会影响 Y
-> 凭什么 proxy 能代表理论对象
-> 凭什么实验 / 识别能支持结论
-> 凭什么不是竞争性解释
-> 凭什么结果稳健可信
-> 凭什么能迁移到当前项目
```

### Status

详见独立 log：

```text
logs/2026-07-06-从八股模块到凭什么链.md
```

### Lesson

八股模块是论文呈现的形式秩序；“凭什么链”是论文成立的实质论证秩序。`research-literature-reader` 后续应考虑把 `claim-warrant map` 提升为协同阅读和自动摘要的共同产物。

### Patch

已根据 `Does Media Coverage...` 的复合命题 case 修补 `collaborative-reading`：

```text
A02: Main X and proxies -> Claim decomposition
A03: Main Y and proxies -> Operationalization and proxy bridge
```

这样后续 Agenda 会先拆 A01 的命题结构，再为每个命题支寻找 X/Y/proxy/warrant/evidence，避免把复合命题偷换成单组 X/Y。

### UAT Patch

SubAgent 只读 UAT 结论为 PASS；随后根据其提示补了轻微歧义：

```text
research-literature-reader/SKILL.md
automatic-summary/SKILL.md
collaborative-reading/SKILL.md
collaborative-reading/templates/discussion-outline-template.md
```

核心补丁：父层和自动摘要也必须输出或承认 `claim-warrant map`；Orientation Card 中的 Main X / Main Y 只作为 first-pass orientation，不能替代 A02/A03 的命题拆解和 proxy bridge。

### UAT Anti-Cheating Follow-up

用户指出：如果 UAT prompt 直接泄露 `A01 / P1 / P2 / Bx / By / proxy bridge` 等预期结构，就不是干净验收，而是在让 subAgent 复述标准答案。

已新增：

```text
skills/miy-uat/SKILL.md
```

用于约束 black-box / gray-box / white-box UAT，核心原则是：不要把预期答案、已知 bug、修复方案和关键输出结构泄露给验证者。

干净 UAT 进一步暴露出 `collaborative-reading` 的残余问题：Agenda 已能自然走向命题拆解和 proxy bridge，但 A01 仍可能把经验 proxy 句子当成理论核心发现。因此补充规则：A01 优先写理论对象 / 抽象构念；proxy 只在 A03 解释其如何代理理论对象，除非论文的核心 claim 本身就是 measurement / proxy claim。

## 2026-07-08 ReAct: 项目型文献阅读的回挂边界

### Trigger

在 `CASE-260521-基金经理研究` 中，用户要求把已读文献产出链接回 `TASK01-说明.md`。随后进一步指出：`paper-reading` 可以单独使用，不能要求所有论文阅读都必须回挂到 task / node；回挂规则应由上层 Skill 在项目语境中约定。

### Observation

原先容易把三件事混在一起：

```text
paper-reading：一篇论文怎么读；
research-literature-reader：项目中为什么读、读完如何沉淀；
workflow-paper：这件事属于学论文、写论文、审稿、返修还是格式交付。
```

如果在 `paper-reading` 层强制“不得让阅读资产成为孤岛”，会误伤独立读论文场景。用户只是想读懂一篇论文或生成个人笔记时，不应该伪造 task / route / node。

### Rule Upgrade

边界改为：

```text
paper-reading：
  管阅读管线和 reading output handoff；
  可以独立使用；
  不强制项目回挂。

research-literature-reader：
  管 project / task / route / node 语境下的文献资产沉淀；
  若存在项目语境，负责把阅读产出回挂到 task ledger、node、paper folder 和 project log；
  若无项目语境，不伪造回挂对象。

workflow-paper：
  只判断是独立学论文还是项目内学论文；
  项目内学论文交给 research-literature-reader。
```

### Lesson

更准确的规则不是“不得让阅读资产成为孤岛”，而是：

```text
项目型文献阅读不得让阅读资产与项目上下文断链。
```

独立学论文可以只保留 paper-level 产物；项目型学论文必须说明这些产物如何服务当前 task / route / node。
