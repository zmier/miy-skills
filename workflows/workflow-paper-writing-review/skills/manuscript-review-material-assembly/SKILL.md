---
name: manuscript-review-material-assembly
description: 组装学术手稿审稿素材包。用于外部审稿、投稿前自审和论文质量诊断的最后阶段，在快速通读、文献定位、因果识别、变量数据、结果叙事和 issue ledger 完成后，整理贡献简述、重大问题、次要问题、可执行修改建议、编辑判断依据和推荐意见倾向。本 Skill 只生成 reviewer-owned materials，不替审稿人生成最终提交给期刊的审稿报告。
---

# Manuscript Review Material Assembly

## 定位

本 Skill 是 workflow-paper-writing-review 中的第 8 步：审稿素材组装。

它负责回答一个朴素问题：

```text
现在已经知道这篇稿子哪里好、哪里弱、哪里要改；这些材料应该如何组织，方便审稿人自己写最终意见？
```

它负责全局去重、合并和排序：把第 3-7 步产物与 `notes/review-issue-ledger.md` 中的 issue 对齐，合并重复问题，区分 major/minor/clarification/defer，并说明哪些问题已经进入审稿素材、哪些只保留为后台判断。它不重做各模块审查。

输出语言按稿件和用户需求决定。默认保留一份英文素材包；如果用户需要中文阅读版，必须同时生成中文主体版，并在关键术语后补英文括注，例如“工具变量（IV）”“排除限制（exclusion restriction）”“重大修改（major revision）”。issue id、段落号、表号和 recommendation label 应保持原样可追踪。

## 边界

本 Skill 生成的是审稿素材包，不是最终提交文本。

允许：

- 整理贡献、问题、证据和修改请求；
- 形成 major / minor issue 候选；
- 给出 provisional recommendation rationale；
- 区分 author-facing 和 editor-facing material；
- 标注哪些判断需要人工确认。

不允许：

- 冒充审稿人作最终推荐；
- 生成可直接提交的完整审稿报告，除非用户明确要求且期刊政策允许；
- 写入 ScholarOne 或其他审稿系统；
- 把期刊系统敏感链接、作者身份、登录信息或最终 confidential comments 写入 workflow 层。

## 触发条件

当用户提出以下需求时使用：

- “审稿素材组装”
- “整理审稿意见”
- “major/minor issues”
- “推荐意见怎么判断”
- “给编辑的判断依据”
- “第 8 步”
- “把前面结果收束一下”

## 输入

主入口必须读取：

- `notes/results-narrative-consistency-audit.md`
- `notes/review-issue-ledger.md`
- 项目 `README.md` 中的期刊、截止日期、AI 使用边界和提交表单信息

其中 `notes/results-narrative-consistency-audit.md` 必须优先读取其中的：

```text
## Cross-Module Intake Summary
## Cross-Module Issue Lineage
```

这两个区块是第 8 步的主要桥梁：它们告诉本 Skill 每个问题来自哪个前置模块、是否已经被结果叙事承接、是否应进入审稿素材。若该文件还没有这两个区块，应先回到第 7 步补齐，而不是直接组装最终素材。

按需回读前置模块证据，不默认完整串读：

- 需要重述稿件问题、数据和贡献时，回读 `notes/quick-read-contribution-chain.md`。
- 需要确认文献 gap、benchmark 或 Y 的文献层级时，回读 `notes/literature-positioning-and-genealogy.md`。
- 需要确认 IV、DAG、PSM、bad controls 或因果语气时，回读 `notes/causal-identification-audit.md`。
- 需要确认 X/Y/样本/数据/量纲/构造请求时，回读 `notes/variable-data-measurement-audit.md`。
- 需要 evidence location 或原文措辞时，再读段落编号 manuscript Markdown。

第 8 步不做第 7 步那种完整串读；它使用第 7 步产出的 lineage 作为压缩索引，只在写具体审稿素材时回查必要证据。

必要时读取：

- restored manuscript Markdown；
- review form / score sheet notes；
- journal-specific review instructions。

## 输出

默认输出到：

```text
review/review-materials.md
```

如用户要求中文对应版本，同时输出：

```text
review/review-materials.zh.md
```

中文版本规则：

- 主体用中文大白话；
- 关键方法、变量、审稿术语首次出现时补英文括注；
- 保留 issue id、表号、段落号、变量名和 recommendation label；
- 不删减英文版中的实质判断；
- 不把中文版本写成最终提交稿，仍然是 reviewer-owned materials。

建议使用模板：

```text
templates/review-materials-template.md
```

同时更新：

```text
tasks/TASK08-审稿素材组装/TASK08-说明.md
```

## 分析顺序

### 1. 审稿状态快照

列明：

- manuscript id、title、journal、deadline；
- 已完成的 workflow steps；
- 未完成或需要人工确认的 gate；
- AI / confidentiality boundary。

### 2. 跨模块 issue lineage intake

先从第 7 步的 `Cross-Module Issue Lineage` 和 `notes/review-issue-ledger.md` 生成 major issue cluster map。这个 map 是后续 major/minor 分级的入口，不要直接复制 ledger。

推荐 cluster 结构：

| Cluster | Included Issues | Source Modules | Reviewer-Facing Theme | Draft Severity | Include? |
|---|---|---|---|---|---|

合并规则：

- 同一构念问题合并，例如 Y 的文献层级、变量操作化和 HS 匹配可合并为一个 major cluster。
- 同一因果链问题合并，例如 actual observed finding vs claimed causal finding、IV 排除限制、bad controls 可合并为一个 identification cluster。
- 机制和拓展若共同体现“结论越过证据”，可合并为一个 narrative overreach cluster。
- 只把影响贡献、核心变量、识别、主结果解释或推荐意见的问题列为 major。
- 对只作为后台判断、证据不足或重复的问题，标为 `defer` 或 `exclude`，并说明原因。

每个 cluster 进入 major/minor 组装前，执行最小证据回读：

```text
cluster -> issue ids -> source modules -> only the necessary paragraphs/tables/requests
```

如果无法从第 7 步 lineage 和 issue ledger 直接定位证据，先补 issue ledger 或回到对应前置模块，不要在第 8 步临时发散审查。

### 3. 贡献简述

用审稿人自己的话重述：

- 研究问题；
- 作者声称的贡献；
- 数据和方法；
- 主要发现；
- 值得肯定的地方。

不要一开始就攻击；先准确承认稿件想做什么。

### 4. issue 分级

从 `notes/review-issue-ledger.md` 中筛选：

- major issue candidates；
- minor issue candidates；
- clarification requests；
- already resolved or low-priority items。

分级原则：

- major：影响贡献、核心变量、识别、主结果解释或推荐意见；
- minor：表达、编号、定义补充、表格清晰度、可局部修复问题；
- clarification：需要作者说明，但未必改变结论；
- do not include：尚无证据、重复或只属于聊天解释的问题。

### 5. 重大问题组装

每个 major issue 应包含：

- issue id；
- reviewer-facing title；
- plain-language concern；
- evidence location；
- why it matters；
- actionable request；
- possible severity if unresolved。

同类问题可以合并，不要机械复制 ledger。

### 6. 次要问题组装

整理：

- 表号、变量名、公式符号、样本量、术语、表达清晰度；
- 可操作小修建议；
- 不要把 minor 写成 major 的重复。

### 7. 作者可执行修改请求

把问题转为作者能做的动作：

- provide / clarify / report / add / reframe / temper / test / discuss；
- 每条请求应对应至少一个 issue 或 evidence location。

### 8. 编辑判断依据和推荐意见倾向

整理给审稿人自己判断用的材料：

- contribution potential；
- fatality / fixability；
- what must be fixed before publication；
- provisional recommendation：accept / minor revision / major revision / reject / unsure；
- confidence level；
- conditions that could change the recommendation。

不要把这部分写成最终 confidential comments，除非用户明确要求。

### 9. 生成第 9 步人工复核门清单

列出最终提交前仍需人工确认的 gate，供 workflow 第 9 步执行。第 8 步只生成清单和证据索引，不宣称这些 gate 已完成：

- 是否已在提交前核对 ScholarOne 实时页面和期刊政策提示；
- 是否人工读过关键段落和表格；
- 是否检查了利益冲突、伦理、重复发表、数据造假或抄袭嫌疑；
- 是否把 author-facing comments 和 editor-facing comments 分开；
- 是否需要在 ScholarOne 保存草稿。

## 输出结构

~~~markdown
# Review Materials

## Review Status Snapshot

## Contribution Summary

## Provisional Recommendation

## Major Issue Cluster Map

| Cluster | Included Issues | Source Modules | Reviewer-Facing Theme | Draft Severity | Include? |
|---|---|---|---|---|---|

## Major Issue Candidates

| Issue | Reviewer-Facing Concern | Evidence | Why It Matters | Actionable Request |
|---|---|---|---|---|

## Minor Issue Candidates

## Actionable Author Requests

## Editor-Facing Rationale Notes

## Items to Exclude or Defer

## Human Submission Checklist
~~~

中文对应版本使用同样结构，标题可写为：

~~~markdown
# 审稿素材包 / Review Materials
~~~

## 判断纪律

- 不把 issue ledger 原样复制成审稿意见；要合并、排序、降噪。
- 不把所有 major-candidate 都强行写成 major；要判断是否影响推荐意见。
- 不生成最终提交版审稿报告，除非用户明确要求进入该阶段。
- 对当前证据不够的判断标注 `needs human confirmation`。
- 推荐意见只能是 provisional，最终由审稿人决定。
- 中文版不得替代英文版；英文稿件的关键术语、变量名和推荐意见标签必须保留英文括注，方便回到原稿和 ScholarOne 表单。
