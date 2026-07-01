---
name: workflow-paper-writing-review
description: 论文写作与审稿复合 Skill。用于学术论文写作、自审、外部审稿、文献定位、贡献链还原、方法识别、变量数据审查、结果叙事一致性、审稿素材组装和最终审稿意见撰写；编排 workflow-paper-writing-review 下的子 Skills，并在需要判断论据是否支撑贡献/因果/理论结论时调用 argument validity adapter。
---

# Paper Writing Review Workflow 总流程

## 审稿的知识增量原则

审稿不只是挑错或给出录用建议。更底层地说，审稿是借一篇稿件进入一个研究领域，让我们对这个世界多一点了解。

一篇稿件像一个有点话唠的旅伴：它带着自己的问题、文献、变量、方法、结果和叙事来到我们面前。workflow 的任务不是先急着裁判它，而是先跟着它走进那片知识地形，重建这个领域的概念、源头文献、共识、争议和方法边界；然后再回头和作者对话，判断他声称自己站在哪里、实际上更像站在哪里、还需要补哪些证据。

因此，外部审稿应遵循：

```text
稿件作为入口
-> 重建领域知识树
-> 更新审稿人自己的概念、文献、变量和方法体系
-> 判断作者稿件在知识谱系中的实际位置
-> 以同行对话方式组织贡献边界、证据缺口和修改建议
```

这条原则约束所有审稿模块：先理解领域，再评价稿件；先建立知识，再组织审稿意见。

语气上，审稿应保持“感谢作者带来的风景，但认真校准地图”：珍惜稿件让我们看到的新问题、新场景和新材料，同时清醒检查概念、文献、变量、识别和叙事是否画准。最终回应应温柔、犀利、可证据化。

## 审稿姿态层

审稿 workflow 分为四层：

- 技术层：检查变量、识别、模型、数据、引用、表格和稳健性；
- 流程层：归档材料、还原文本、重建贡献链、定位文献、组织审稿素材；
- 判断层：判断贡献、gap、识别、测量和叙事是否成立；
- 姿态层：决定我们为什么审稿，以及以什么方式进入一篇稿子。

本 workflow 默认采用 `reviewer-stance: knowledge-travel-companion`：

```text
先感谢风景
再重建地图
然后校准路线
最后和作者对话
```

这个姿态不是降低标准，而是让严谨性更有人味：感谢稿件带来的知识入口，同时温柔又犀利地指出概念滑移、文献夸大、测量风险、因果识别不干净和叙事越界。

## 双向流程

```mermaid
flowchart LR
  Q[研究问题] --> L[文献缺口]
  L --> T[理论机制]
  T --> I[识别策略 / 研究设计]
  I --> D[数据与变量]
  D --> R[结果与稳健性]
  R --> C[贡献叙事]
  C --> E[表达、引用与投稿]

  E -.审稿逆向验收.-> C
  C -.-> R
  R -.-> D
  D -.-> I
  I -.-> T
  T -.-> L
  L -.-> Q
```

## 写作方向

```text
目标期刊 / 读者 / 贡献类型
-> 研究问题
-> 文献缺口
-> 理论机制
-> 假设或命题
-> 识别策略 / 研究设计
-> 数据、变量和样本
-> 结果与稳健性
-> 贡献叙事
-> 表达、引用和投稿材料
```

## 审稿方向

```text
成稿
-> 还原作者声称的贡献链
-> 检查研究问题是否重要
-> 检查文献缺口是否成立
-> 检查理论机制是否自洽
-> 检查识别 / 数据 / 变量是否支持结论
-> 检查结果叙事是否越过证据
-> 检查引用、表达和结构
-> 形成可执行审稿意见
```

## 外部审稿编排模块

外部审稿使用 `skills/paper-workflow-orchestrator/SKILL.md` 作为总编排 Skill，并以 `references/external-peer-review-orchestration.md` 作为路线 reference。

论证有效性能力已拆出为独立通用 workflow：

```text
../workflow-argument-validity/
```

本 workflow 在审稿场景调用其中的学术适配 Skill：

```text
../workflow-argument-validity/skills/academic-review-argument-audit/
```

调用边界：凡是要判断“作者的论据、变量、识别、结果是否足以推出其贡献/因果/理论结论”的问题，交给该 adapter；本 workflow 只负责审稿业务编排、证据台账和最终审稿材料组织。

```text
项目归档
-> 文本底稿
-> 快速通读
-> 文献定位
-> 方法与识别审查
-> 变量、数据与测量审查
-> 结果叙事一致性
-> 审稿素材组装
-> 终稿前人工复核门
-> 最终审稿文本撰写
```

其中，文本底稿、文献定位、方法审查、变量审查可在同一审稿项目内并行推进；所有判断必须回填到 project / TASK 层的台账或笔记，workflow 本体只保存通用路线和质量边界。

第 9 步“终稿前人工复核门”不是再做一次审稿，也不是最终提交文本；它是在审稿素材包之后、正式写入期刊系统或提交前，对关键证据、推荐意见、ScholarOne 实时页面、期刊政策提示和人工责任做最后校验。典型检查包括：人工读过关键段落和表格、核过核心变量与模型/统计表、确认利益冲突、伦理/重复发表/数据异常风险、区分 author-facing 与 editor-facing 材料，并确认最终推荐意见由审稿人承担。

第 10 步“最终审稿文本撰写”不是单纯润色，而是一个小型编排：先调用 `review-issue-priority-synthesizer` 把 issue ledger、第 8 步素材和可选外部 benchmark / QA findings 去重排序为少数 major/minor 问题簇，再由 `manuscript-final-review-drafting` 转换为可编辑的 `Comments to the Author`、可选 `Confidential Comments to the Editors`、recommendation rationale 和 ScholarOne 字段映射。它可以生成草稿，但不得跳过人工确认；若第 9 步仍有 pending gate，输出必须标注 `draft-not-ready-to-submit`。

第 10 步内部可以调用共享子 Skill `multi-agent-academic-review-qa` 做终稿 QA。它用冷读者、技术清晰度、证据边界和可执行性四类视角交叉审查草稿，专门发现主写作者因知道太多前序上下文而遗漏的背景桥、术语解释、推理步骤和语气问题。subAgent 输出只作为 QA 材料，最终整合和提交责任仍由主 Agent 与审稿人承担。生成 vNext 后，应调用 `post-flight-review-verifier` 检查每条重大评论、推荐理由和 confidential comments 是否有证据来源、是否越过证据边界、是否缺少读者背景桥、是否混入内部 workflow 内容；验收结果为 `FIX` 或 `HUMAN_CHECK` 时不得声称终稿可提交。

## 分层职责

- workflow：定义质量系统、总编排、子 Skill 路由和证据边界；
- Skill：执行具体写作、审读、引用、表达或方法审计；
- project / TASK：保存具体论文、稿件、批注、审稿意见和证据；
- reference：保存稳定质量标准；
- template：保存写作台账、审稿台账、返修台账和报告模板。

## 能力地图

当前 workflow 的已实现、seed、candidate 和 external Skills 登记在 `references/skill-registry.md`。

核心建设原则：

```text
真实项目 / TASK
-> 留下证据、失败模式、验收结果
-> 抽象为 workflow 规则、子 Skill、模板和测试
-> workflow 只保存可迁移能力
-> 不反向依赖具体案例
```

写论文是正向构造贡献链；审稿是逆向验收贡献链。二者共享同一套 paper quality ladder，只是调用方向不同。

## 基础设施子 Skill

### scholar-pdf-markdown-restoration

位置：`skills/scholar-pdf-markdown-restoration/SKILL.md`

用途：在逐段审读、审稿、投稿前自审和写作逆向分析前，将 PDF 抽取、分章节还原为 Markdown，并使用模型能力逐章修复正文、公式、图表和段落编号，使其成为可直接审读的 restored Markdown。

它处理的是材料准备层问题：

```text
PDF 手稿
-> 原文还原 Markdown
-> 分章节 Markdown
-> 模型逐章还原公式/图表/正文
-> 分段与还原 QC
-> 可信审读底稿
-> 贡献链还原 / 逐段审读 / 问题台账
```

它不替代论文质量判断，只保证后续判断所依据的 Markdown 文本、公式、图表和 `[para N]` 有可靠来源。

### scholar-docx-markdown-restoration

位置：`skills/scholar-docx-markdown-restoration/SKILL.md`

用途：在逐段审读、审稿、投稿前自审和论证树抽取前，将 DOCX / Word 手稿转换、清理并还原为 Markdown，保留正文、标题、脚注、尾注、图片、公式和参考文献，并给正文自然段增加连续 `[para N]` 定位，使其成为可直接审读和抽树的 restored Markdown。

它处理的是 DOCX 材料准备层问题：

```text
DOCX 手稿
-> Pandoc / OOXML 粗转换
-> media / footnote / endnote 提取
-> 段落编号 `[para N]`
-> 图像与公式 QC
-> 可信审读底稿
-> 贡献链还原 / 论证树抽取 / 逐段审读
```

它是 `scholar-pdf-markdown-restoration` 的兄弟 Skill，不替代 PDF 视觉还原。若用户提供的是 DOCX，正式审稿或 full-tree 抽树前优先调用本 Skill；若只做临时 quick read，可先粗转文本，但必须说明不是完整 restored 底稿。

### manuscript-quick-reconstruction

位置：`skills/manuscript-quick-reconstruction/SKILL.md`

用途：在已有 PDF/HTML/Markdown 底稿后，快速通读并还原作者声称的贡献链，输出 `notes/quick-read-contribution-chain.md` 或同类 Markdown 笔记，回答研究问题、文献缺口、理论机制、变量、数据、识别策略、主要结果、贡献叙事和初步风险点。

它处理的是“理解论文声称在做什么”的问题，不替代文献定位、方法审查、变量审查或最终审稿意见。

### manuscript-literature-genealogy

位置：`skills/manuscript-literature-genealogy/SKILL.md`

用途：在快速通读贡献链之后，编排 scholar-kit 的 OpenAlex、WoS、CNKI、EBSCO、被引和句子检索能力，读取摘要和元数据，用高质量文献重建知识树/文献谱系，输出文献定位矩阵与 Mermaid 知识树。

它处理的是“这篇稿件在文献树上到底挂在哪里”的问题。主干文献优先限定 FT50、UTD24/领域顶刊、`Nature`、`Science`、`PNAS` 等综合顶刊；中文文献最低使用川大社科 B 以上。它不替代方法审查，也不生成最终审稿意见。
