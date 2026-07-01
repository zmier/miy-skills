---
name: review-issue-priority-synthesizer
description: 综合审稿项目中的 issue ledger、审查产物和多 Agent findings，把分散问题去重、合并、排序为少数可写入最终审稿意见的 CRITICAL / MAJOR / MINOR 问题簇。用于最终审稿文本撰写前、审稿素材组装后或外部 referee benchmark 后；不新增未经证据支持的重大判断。
---

# Review Issue Priority Synthesizer

## 定位

本 Skill 是最终审稿文本撰写前的综合排序子 Skill。

它把前序审查中分散的疑问、脆弱点和 findings 转换为一份可供 `manuscript-final-review-drafting` 使用的优先级清单：

```text
issue ledger + review materials + audit outputs + optional external/multi-agent findings
-> deduplicated issue clusters
-> CRITICAL / MAJOR / MINOR ordering
-> final-review-ready issue plan
```

它借鉴 `AI-research-feedback` 的 severity ranking 思路，但不复制外部仓库内容；项目事实仍以本项目文件为准。

## 必读输入

- `notes/review-issue-ledger.md`
- `review/review-materials.md`
- `review/review-materials.zh.md`（若存在）
- 第 5-8 步产物中与当前终稿相关的 Markdown

按需读取：

- `tasks/TASK10-*/outputs/multi-agent-review-qa.md`
- `tasks/TASK10-*/subagents/*.log.md`
- 外部 workflow benchmark 或 test-run 输出
- restored manuscript Markdown 中的关键段落 / 表格

## 输出

默认输出到当前 TASK 的 outputs：

```text
tasks/TASK10-最终审稿文本撰写/outputs/final-review-issue-priority-plan.md
```

若用于其他 TASK，使用：

```text
tasks/TASKxx-*/outputs/review-issue-priority-plan.md
```

## 工作流

1. 收集候选问题：
   - 从 issue ledger 读取所有 unresolved / major-candidate / critical-candidate / clarification-needed 项；
   - 从 review materials 读取 major issue clusters；
   - 从 QA / benchmark findings 中读取 blocker / major findings；
   - 只保留与最终审稿意见相关的问题。
2. 去重合并：
   - 同一因果链上的问题合并为一个 issue cluster；
   - 不把同一问题分别写成变量问题、结果问题和贡献问题，除非它们需要不同的作者行动；
   - 保留所有原始 issue id。
3. 分级：
   - `CRITICAL`：若不修复，会使论文核心结论或发表判断无法成立；
   - `MAJOR`：审稿意见中必须要求作者实质回应；
   - `MINOR`：表达、清晰度、表格说明、引用或可低成本修复的问题。
4. 做 evidence boundary：
   - 每个 `CRITICAL / MAJOR` 必须有 issue id 或具体证据位置；
   - 若只有推测，降级为 `clarification request`；
   - 不把“未验证的新颖性/伦理/数据异常/抄袭”等写成确定指控。
5. 生成 final-review-ready plan：
   - 建议最终 author-facing major comments 3-5 条；
   - 每条 major comment 只承载一个核心问题；
   - 每条都写清 `concern -> why it matters -> requested author action`；
   - 标注是否适合放入 confidential comments。

## 输出结构

```markdown
# Final Review Issue Priority Plan

## Source Files

## Priority Summary

| Rank | Severity | Cluster | Issue IDs | Final Draft Destination |
|---|---|---|---|---|

## CRITICAL / MAJOR Clusters

### M1. [Cluster Name]

- Issue IDs:
- Evidence:
- Concern:
- Why it matters:
- Requested author action:
- Boundary:
- Suggested destination: author-facing / confidential / both

## MINOR / Polish Items

## Dropped Or Deferred Items

| Item | Reason |
|---|---|

## Drafting Notes
```

## 写作纪律

- 这是排序和综合，不是重新审稿。
- 若一个问题已经被第 8 步清楚合并，不要拆散。
- 若用户刚指出“某个重大问题漏了”，优先检查它是否在 ledger 中已有 issue id，再决定更新 cluster。
- 不因英文术语高级而提高 severity；severity 取决于它是否影响贡献、识别、变量、结果或可执行修改。
- 输出给最终撰写 Skill 使用，可以比最终审稿意见更内部化；但仍不得包含作者身份、期刊系统敏感信息或未验证指控。
