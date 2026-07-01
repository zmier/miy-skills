---
name: post-flight-review-verifier
description: 对最终审稿意见草稿做提交前 post-flight verification。逐条检查重大评论、推荐理由和 confidential comments 是否有证据来源、是否越过证据边界、是否缺少读者背景桥、是否混入内部 workflow 内容，并输出 PASS / FIX / HUMAN_CHECK 验证表。用于 final-review-draft vNext 进入 ScholarOne 或发送给用户前。
---

# Post-Flight Review Verifier

## 定位

本 Skill 是最终审稿文本的提交前验收门。

它借鉴 `claude-code-my-workflow` 的 post-flight verification 思路：最终文本中越具体、越容易造成误导的判断，越要回到来源验证。

```text
final review draft + issue ledger + review materials + human gate
-> claim / comment verification table
-> required fixes
-> PASS / FIX / HUMAN_CHECK status
```

## 必读输入

- `review/final-review-draft*.md`
- `review/final-review-draft*.zh.md`（若存在）
- `notes/review-issue-ledger.md`
- `review/review-materials.md`
- `tasks/TASK09-终稿前人工复核门/outputs/human-pre-submission-gate.md`

按需读取：

- `tasks/TASK10-*/outputs/final-review-issue-priority-plan.md`
- `tasks/TASK10-*/outputs/multi-agent-review-qa.md`
- restored manuscript Markdown 中的关键段落 / 表格
- ScholarOne 表单捕获或 review form location notes

## 输出

默认输出：

```text
tasks/TASK10-最终审稿文本撰写/outputs/final-review-post-flight-verification.md
```

若发现必须修改的内容，输出状态为 `FIX`，并列出需要改的句子和原因。修改后的草稿应再次运行本 Skill 或明确记录未复核风险。

## 验证对象

逐条抽取并验证：

- 每个 major comment；
- 每个 confidential comment；
- recommendation rationale；
- 涉及变量、模型、统计量、表格、文献定位、因果识别、机制或伦理边界的具体判断；
- 中文版中比英文版更强或更弱的判断；
- 英文版中压缩到读者看不懂的技术句。

## 验证维度

1. Evidence grounding：
   - 是否能对应 issue id、review materials、原文段落或表格；
   - 若不能，标 `FIX` 或 `HUMAN_CHECK`。
2. Evidence boundary：
   - 是否把“需要作者澄清”写成“作者错误”；
   - 是否把“未验证的新颖性/数据/伦理风险”写成确定指控。
3. Reader bridge：
   - 是否缺少读者理解所需的背景桥；
   - 是否出现只有前序对话知道、最终读者不知道的术语或前提。
4. Actionability：
   - 作者是否知道要补什么、解释什么、重估什么或改写什么；
   - 是否只有批评，没有可执行请求。
5. Paste-ready boundary：
   - 可粘贴正文是否混入 workflow metadata、内部 checklist、subAgent logs、issue id 清单或 AI 使用过程；
   - author-facing 和 confidential/editor-facing 是否分开。
6. Bilingual parity：
   - 中文版是否只是直译而未解释；
   - 英文版是否比中文版更含糊；
   - 两个版本是否存在判断强度不一致。

## 输出结构

```markdown
# Final Review Post-Flight Verification

## Verdict

- Status: PASS / FIX / HUMAN_CHECK
- Draft checked:
- Checked at:

## Verification Table

| Item | Draft location | Source / evidence | Result | Required fix |
|---|---|---|---|---|

## Reader-Bridge Fixes

## Evidence-Boundary Fixes

## Paste-Ready Boundary Fixes

## Human Checks Remaining

## Re-Verification Needed
```

## 判定规则

- `PASS`：没有 blocking fix；剩余仅为审稿人最终偏好或人工责任确认。
- `FIX`：存在可由文本修改解决的问题，例如缺前提、证据边界过强、中文读不懂、英文过度压缩、内部 checklist 混入正文。
- `HUMAN_CHECK`：需要审稿人亲自确认原 PDF、表格、ScholarOne、COI、期刊 AI 政策或最终推荐意见。

## 写作纪律

- 本 Skill 不替代审稿人最终判断，只检查草稿是否可提交、可理解、可证据化。
- 对重大问题，优先要求“补证据/降调/改成澄清请求”，而不是直接删除。
- 不因为草稿读起来流畅就判 PASS；流畅但无证据边界也必须 FIX。
- 若发现终稿漏掉 priority plan 中的高优先级问题，标 `FIX`，要求回到 `review-issue-priority-synthesizer` 或重新起草 vNext。
