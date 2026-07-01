---
name: multi-agent-academic-review-qa
description: 用多 subAgent 或多角色独立审查方式，对学术审稿意见、投稿前自审报告、返修信或关键论文写作稿进行最终质量复核。适用于用户要求“多Agent方案”“冷读者检查”“交叉审查”“终稿前复核”“读者是否看得懂”“技术内容是否说清楚”“审稿意见是否可执行”等场景；重点发现主写作者因上下文过多而遗漏的背景桥、技术推理断裂、证据边界和语气问题。
---

# Multi-Agent Academic Review QA

## 定位

本 Skill 是论文写作 / 审稿 workflow 的共享终稿复核子能力。

它不负责首次发现论文问题，也不替代具体审查模块。它负责在已有草稿之后，用多个相互独立的视角做 QA：

```text
draft + minimal task context
-> independent role reviews
-> QA synthesis
-> revision plan
-> optional revised draft
```

核心目的：制造“认知距离”。主写作者通常知道太多背景，容易写出只有自己和聊天记录能懂的句子；多 Agent QA 用冷读、技术复核、证据边界和表达复核来暴露这些断点。

## 触发场景

优先使用本 Skill，当用户提出：

- 多 Agent / subAgent / 多角色 / 交叉审查；
- “这句话没头没尾”“读者未必 get 到”“为什么写得难懂”；
- 最终审稿意见、返修信、投稿前自审报告、review response 或技术段落进入终稿前复核；
- 需要检查变量、识别、统计、机制、DAG、IV、PSM、DiD、F-statistic、R2、robustness、heterogeneity 等技术判断是否讲清楚；
- 需要确认 author-facing / editor-facing / confidential materials 是否分开；
- 主 Agent 已经参与长对话，可能被上下文污染。

## 边界

允许：

- 开启多个 subAgent 做独立审查；
- 如果工具环境没有 subAgent，则用串行多角色审查作为降级方案，并明确标注 `simulated-role-review`；
- 对草稿提出修改建议、风险等级和重写片段；
- 生成 QA 报告和 vNext 修改计划；
- 协助主 Agent 整合生成新版草稿。

不允许：

- 让 subAgent 直接提交审稿意见或最终推荐；
- 把 subAgent 输出机械拼接成终稿；
- 向冷读者 Agent 泄露主 Agent 的预设答案、用户私下判断或完整聊天历史；
- 新增未经 issue ledger、草稿证据或原文证据支持的重大指控；
- 将具体稿件、作者身份、期刊系统链接、登录信息或保密审稿内容写入 workflow / Skill 本体。

## 输入

最小输入：

- 待复核草稿，例如 `review/final-review-draft.md`、`review/final-review-draft.zh.md`、返修信或投稿前自审报告。

按角色增加：

- `notes/review-issue-ledger.md`；
- `review/review-materials.md` / `.zh.md`；
- human gate 或 submission checklist；
- 与技术问题直接相关的表格、段落或前序 TASK 产物。

不要默认把全部项目材料都给所有 Agent。冷读者尤其应只读最终草稿和最少元信息。

## 输出

默认输出：

```text
review/multi-agent-review-qa.md
```

若用于具体 TASK，可同步保存：

```text
tasks/TASKxx-*/outputs/multi-agent-review-qa.md
```

每次真实 subAgent 或模拟多角色 QA 都应保留 role-level log：

```text
tasks/TASKxx-*/subagents/cold-reader.log.md
tasks/TASKxx-*/subagents/technical-clarity.log.md
tasks/TASKxx-*/subagents/evidence-boundary.log.md
tasks/TASKxx-*/subagents/actionability.log.md
```

如需改稿，再由主 Agent 输出新版草稿，例如：

```text
review/final-review-draft-v3.md
review/final-review-draft-v3.zh.md
```

## Agent 角色

### 1. Cold Reader Agent

目的：模拟没有参与前序讨论的编辑、作者或审稿人自己隔天重读。

只给：

- 最终草稿；
- 最少 metadata，如稿件主题、目标文本类型。

不直接给：

- 完整聊天历史；
- 主 Agent 的判断理由；
- issue ledger；
- 预期答案。

检查：

- 哪些句子需要前文知识才能懂；
- 哪些术语、年份、方法、变量、文献名突然出现；
- 哪些因果链、证据链或修改请求缺少中间桥；
- 中文和英文版本是否各自能独立读懂；
- 是否有“我们自己知道，但读者不知道”的背景假设。

输出字段：

```markdown
## Cold Reader Findings

| severity | location | confusing text | why confusing | suggested bridge |
|---|---|---|---|---|
```

### 2. Technical Clarity Agent

目的：检查技术判断是否把推理链说完整。

给：

- 最终草稿；
- 相关 issue ledger 条目；
- 必要的 review materials 或技术证据位置。

检查：

- 变量定义、量纲、操作化指标是否说清；
- 统计量、系数、显著性、F-statistic、R2、balance、common support 等是否解释其含义和局限；
- 识别策略、DAG、IV、PSM、DiD、固定效应、控制变量是否只贴标签而没解释；
- 是否区分 actual observed finding 与 author-claimed/upscaled finding；
- 是否遵循：

```text
作者声称是什么
-> 正常需要什么定义 / 假设 / 数值含义
-> 文中实际呈现什么
-> 二者哪里不匹配
-> 这影响什么
-> 要作者补什么
```

输出字段：

```markdown
## Technical Clarity Findings

| severity | issue_id | location | missing reasoning step | proposed rewrite |
|---|---|---|---|---|
```

### 3. Evidence Boundary Agent

目的：防止终稿越过已有证据。

给：

- 最终草稿；
- issue ledger；
- review materials；
- human gate。

检查：

- 每个 major comment 是否能追溯到 issue id 或 manuscript evidence；
- 是否把 clarification 写成了 confirmed flaw；
- 是否新增伦理、造假、抄袭、重复发表等未经证据支持的指控；
- recommendation rationale 是否与 major comments 强度匹配；
- author-facing 与 editor-facing / confidential 内容是否分开。

输出字段：

```markdown
## Evidence Boundary Findings

| severity | location | claim | evidence status | required action |
|---|---|---|---|---|
```

### 4. Author-Facing Actionability Agent

目的：检查审稿文字是否像可执行的同行意见，而不是内部分析笔记。

给：

- 最终草稿；
- 可选 review materials。

检查：

- 每条 major comment 是否包含 concern、why it matters、actionable request；
- 语气是否专业、温和、清楚；
- 是否避免“作者错了”式表达；
- minor comments 是否过长或混入 major；
- 给编辑的话和给作者的话是否各司其职。

输出字段：

```markdown
## Actionability Findings

| severity | location | problem | suggested edit |
|---|---|---|---|
```

## 执行顺序

1. 确认待复核草稿和目标：
   - `final review draft`；
   - `review response`；
   - `pre-submission audit`；
   - `technical paragraph`；
   - 其他学术文本。
2. 判断是否真的需要多 Agent：
   - 若只是简单错别字或格式问题，不启动；
   - 若涉及终稿、技术推理、读者理解、证据边界或用户明确要求，启动。
3. 准备 role packets：
   - 冷读者最少上下文；
   - 技术和证据 Agent 按需给证据；
   - 不给任何 Agent “请证明我对”这样的诱导。
4. 并行启动可用 subAgent；若不可用，串行模拟角色并标记降级。
5. 将每个角色的输入范围、上下文限制、原始输出摘要和完成状态写入 `subagents/*.log.md`。
6. 汇总 outputs，按 severity 去重：
   - `blocker`：提交前必须修；
   - `major`：建议进入新版；
   - `minor`：可改可不改；
   - `note`：仅供人工判断。
7. 主 Agent 做裁决：
   - 采纳；
   - 部分采纳；
   - 暂不采纳并说明理由。
8. 如用户要求或 workflow 需要，生成 revised draft。

## SubAgent Log 结构

每个 role log 至少包含：

~~~markdown
# SubAgent Log: Role Name

## Metadata

| Field | Value |
|---|---|
| qa_run_id |  |
| agent_id | real id / simulated |
| role |  |
| status | completed / failed / skipped |
| source_draft |  |

## Role Packet

### Files Given

### Files Withheld

### Task Prompt Summary

## Findings

## Main Agent Notes
~~~

log 的目的不是保存全部聊天上下文，而是回答三件事：

- 这个角色看了什么；
- 它发现了什么；
- 主 Agent 后续如何采纳、部分采纳或拒绝。

## QA 报告结构

~~~markdown
# Multi-Agent Academic Review QA

## Metadata

| Field | Value |
|---|---|
| project_id |  |
| source_draft |  |
| qa_mode | real-subagents / simulated-role-review |
| target_output |  |

## Role Packets

| Role | Files Given | Files Withheld | Reason |
|---|---|---|---|

## Executive Summary

## Findings by Role

### Cold Reader Findings

### Technical Clarity Findings

### Evidence Boundary Findings

### Actionability Findings

## Integrated Revision Plan

| priority | location | action | rationale | owner |
|---|---|---|---|---|

## Main Agent Decisions

| finding | decision | reason |
|---|---|---|

## Follow-Up Outputs
~~~

## 质量标准

一次合格的多 Agent QA 应满足：

- 冷读者能在不知道前序讨论的情况下指出读者断点；
- 技术 Agent 不只说“unclear”，而说明缺了哪一步推理；
- 证据 Agent 能把 major comments 与 issue/evidence 对上；
- 表达 Agent 能把内部判断改造成作者可执行请求；
- 主 Agent 明确裁决，不机械拼接；
- 中英文版本分别可独立阅读；中文主体可更大白话，英文也必须讲清技术推理。

## 与其他 Skills 的关系

- `manuscript-final-review-drafting`：第 10 步生成最终审稿草稿后，应调用本 Skill 做终稿 QA，尤其在用户要求多 Agent 或发现读者理解断点时。
- `technical-reasoning-clarity-audit`：如果未来拆出独立 Skill，可由 Technical Clarity Agent 调用；当前先作为本 Skill 内的角色职责。
- `manuscript-review-material-assembly`：提供 reviewer-owned materials，但不替代本 Skill 的终稿读者视角 QA。
- `paper-workflow-orchestrator`：负责判断何时在第 9-10 步之间或第 10 步之后调用本 Skill。
