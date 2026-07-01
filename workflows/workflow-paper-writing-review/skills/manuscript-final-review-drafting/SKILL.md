---
name: manuscript-final-review-drafting
description: 编排并起草外部审稿最终文本。用于审稿素材组装和终稿前人工复核门之后，把 reviewer-owned materials 转换为可供审稿人人工确认、修改并填入期刊系统的 author-facing comments、可选 confidential editor-facing comments、recommendation rationale 和表单字段草稿。会调用问题优先级综合、多 Agent QA 和 post-flight verification；必须读取第 8 步素材包和第 9 步人工 gate，不重做前序审查，不替审稿人提交或确认最终推荐意见。
---

# Manuscript Final Review Drafting

## 定位

本 Skill 是 workflow-paper-writing-review 中的第 10 步：最终审稿文本撰写。

它负责把第 8 步的审稿素材包和第 9 步的人工 gate，转换为审稿人可编辑的最终文本草稿：

```text
review materials + human gate
-> issue priority synthesis
-> author-facing / editor-facing draft
-> multi-agent QA when needed
-> post-flight verification
-> paste-ready vNext
```

它不重新发现问题，不替代第 3-8 步审查，也不替审稿人提交 ScholarOne。

## 边界

允许：

- 起草 `Comments to the Author`；
- 起草可选 `Confidential Comments to the Editors`；
- 起草 recommendation rationale；
- 把 major/minor issues 改写成礼貌、清楚、可执行的审稿文字；
- 标注哪些句子需要人工确认；
- 输出 ScholarOne 字段映射。
- 编排 `review-issue-priority-synthesizer`、`multi-agent-academic-review-qa` 和 `post-flight-review-verifier`。

不允许：

- 跳过第 9 步 gate；
- 把 `review-materials.md` 原样粘贴成最终审稿报告；
- 新增没有 issue id 或证据来源的重大指控；
- 绕过问题排序、QA 或 post-flight verification 直接宣布终稿可提交；
- 夸大伦理、抄袭、数据造假、重复发表等问题；
- 代替审稿人作最终推荐或点击提交。

## 输入

必须读取：

- `review/review-materials.md`
- `review/review-materials.zh.md`（若存在）
- `tasks/TASK09-终稿前人工复核门/outputs/human-pre-submission-gate.md`
- `notes/review-issue-ledger.md`
- `sources/scholarone-review-page-capture.md` 或 `notes/review-form-location.md`

按需回读：

- restored manuscript Markdown；
- 第 3-7 步 notes；
- 关键表格 Markdown；
- 项目 README。

## 输出

默认输出：

```text
review/final-review-draft.md
review/final-review-draft.zh.md
```

项目 TASK 中同步保存：

```text
tasks/TASK10-最终审稿文本撰写/outputs/final-review-draft.md
tasks/TASK10-最终审稿文本撰写/outputs/final-review-draft.zh.md
```

## 写作顺序

1. 确认第 9 步 gate 状态：
   - 若 `ready_for_human_drafting` 不是 yes / conditional yes，先返回 gate；
   - 若 `ready_for_submission` 是 no，也可以起草，但必须标注 `draft-not-ready-to-submit`。
2. 调用或执行 `review-issue-priority-synthesizer`：
   - 读取 issue ledger、第 8 步 materials、前序审查产物和已有 QA / benchmark findings；
   - 输出 `final-review-issue-priority-plan.md`；
   - 把分散问题去重为 3-5 个 major comment 候选和少数 minor items；
   - 对没有证据来源的 candidate 降级为 clarification 或 deferred。
3. 读取第 8 步 major issue cluster map 和 priority plan，不机械复制 ledger。
4. 写 author-facing comments：
   - 开头先准确承认稿件问题意识和潜在贡献；
   - major comments 以 3-5 个问题为宜；
   - 每个 major comment 包含 concern、why it matters、actionable request；
   - minor comments 简短列点；
   - 语气保持同行对话：温柔、犀利、可证据化。
5. 写 editor-facing confidential comments：
   - 只放推荐理由、可修复性、是否有不宜直接给作者的风险；
   - 没有证据时，不写伦理/造假/抄袭指控。
6. 写 recommendation field：
   - recommendation 只写 draft/provisional；
   - 标注 confidence 和可能改变推荐的条件。
7. 做技术推理清晰度审校：
   - 所有语言版本都必须解释技术判断的推理链，不只给结论；
   - 英文版保持正式审稿语气，但也要写清 `claimed definition -> expected values/assumptions -> observed text/table -> ambiguity/risk -> requested clarification`；
   - 中文版在英文版基础上更大白话，必要时用一句短解释补充术语含义；
   - 如果一个判断涉及变量、识别、统计量、机制、中介、量纲、对数、指数、dummy、share、coefficient、F-statistic、R2、PSM balance、common support、heterogeneity difference 等，不得只写术语标签。
8. 必要时调用 `multi-agent-academic-review-qa`：
   - 用户明确要求多 Agent / subAgent / 冷读者 / 交叉审查；
   - 草稿涉及复杂技术判断，且读者可能不知道前序讨论；
   - 用户指出“这句话读不懂”“没头没尾”“读者未必 get 到”；
   - 中英文版本都需要独立可读；
   - 终稿准备进入 vNext 或 ScholarOne 字段映射前。
9. 若已完成多 Agent / 冷读者 QA，必须生成 vNext 或明确说明不生成：
   - 读取 `multi-agent-review-qa.md` 和 `subagents/*.log.md`；
   - 主 Agent 对每条 `blocker / major` finding 做 `adopt / partial / reject` 裁决；
   - 将采纳项整合为新版草稿，例如 `final-review-draft-v3.md` / `.zh.md`；
   - paste-ready 版本只保留可提交字段：recommendation、comments to author、optional confidential comments；
   - workflow metadata、ScholarOne mapping、human checklist 和 subAgent logs 留在 TASK / reviewer-owned notes，不混入可粘贴正文；
   - 若因人工 gate 未完成而不能生成 paste-ready 终稿，应输出 `draft-not-ready-to-submit` 并列明 pending gate。
10. 调用或执行 `post-flight-review-verifier`：
   - 对每个 major comment、confidential comment 和 recommendation rationale 做证据验证；
   - 检查是否缺少读者背景桥；
   - 检查中英文版本判断强度是否一致；
   - 检查 paste-ready 版本是否混入内部 workflow notes；
   - 若 verdict 是 `FIX`，先生成修订版，再重新说明剩余风险；
   - 若 verdict 是 `HUMAN_CHECK`，明确列出需要审稿人确认的事项。
11. 做提交前自检：
   - 是否每个 major comment 都能回到 issue id 或 evidence；
   - 是否没有新增未经证据支持的指控；
   - 是否 author-facing 和 editor-facing 分开；
   - 是否保留人工确认标记。

## 输出结构

~~~markdown
# Final Review Draft

## Metadata

## Submission Status

## Recommendation Draft

## Comments to the Author

### Summary

### Major Comments

### Minor Comments

## Confidential Comments to the Editors

## ScholarOne Field Mapping

## Human Finalization Checklist
~~~

中文版本使用同样结构，标题可译为：

~~~markdown
# 最终审稿文本草稿 / Final Review Draft
~~~

## 写作纪律

- 中文主体版本用于审稿人阅读和改写；英文版本用于粘贴前人工修改。
- 所有 final review draft 都必须补出技术推理链；这不是中文版独有要求。英文版不能只写 “the scaling is unclear” 或 “the exclusion restriction is weak”，也要解释为什么。
- 技术推理遵循“作者声称是什么 -> 正常应是什么 / 需要什么假设 -> 文中或表中实际是什么 -> 二者为何不匹配 -> 这会影响什么 -> 要求作者补什么”的顺序。例如 share 正常应在 0-1 之间；若 Table 中均值大于 1，应明确说明这意味着它不是普通份额，可能经过转换，因此系数含义无法判断。
- 中文主体版本不能只是英文审稿稿直译；遇到变量、识别、统计量、机制、中介、量纲、对数、指数、dummy、share、coefficient 等术语时，必须用更大白话补出中间推理，让审稿人能快速看懂“为什么这是问题”。
- 对变量测量问题，先承认作者已经说了什么，再指出没说清楚的部分。不要把“作者说得不够清楚”写成“作者完全没说”。例如 Robot 若作者已说是 robot imports，就应进一步问这是金额、数量、强度、log 还是标准化指标，以及 imports 如何对应 adoption。
- 如果主写作者已经参与长对话，最终草稿应优先接受 `multi-agent-academic-review-qa` 的冷读者检查，专门找“只有我们知道、读者不知道”的背景桥缺失。
- 不把作者称为“the author is wrong”；用 “I encourage the authors to clarify / provide / temper / distinguish”。
- 不把 `major revision` 写成不可改变的最终裁决；除非用户明确确认。
- 每条重大意见只讲一个核心问题，不把所有 issue 堆在同一段。
- 如果第 9 步仍有 pending human gate，在输出顶部写明 `draft-not-ready-to-submit`。

## 共享 QA 子 Skill

最终撰写由三个子 Skill 共同支撑：

```text
skills/review-issue-priority-synthesizer/SKILL.md
skills/multi-agent-academic-review-qa/SKILL.md
skills/post-flight-review-verifier/SKILL.md
```

本 Skill 是总编排器：

- `review-issue-priority-synthesizer` 负责综合、去重和排序；
- `multi-agent-academic-review-qa` 负责用冷读者、技术清晰度、证据边界和可执行性视角复核草稿；
- `post-flight-review-verifier` 负责最终文本的证据边界、读者背景桥、paste-ready 边界和中英文一致性验收。

主 Agent 必须裁决和整合，不得机械拼接 subAgent 输出。

当 `multi-agent-academic-review-qa` 已经产出 `multi-agent-review-qa.md` 时，本 Skill 的下一步默认是生成 vNext 草稿，而不是停在 QA 报告。vNext 应把 subAgent 的 findings 转化为审稿文本改进，尤其处理：

- 读者背景桥；
- 技术推理链；
- 证据边界；
- paste-ready 文本与内部 workflow notes 的分离。

技术推理清晰度暂时仍作为本 Skill 和 `multi-agent-academic-review-qa` 的共同检查项；若之后在写作、返修、引用补充或数据解释等多个场景稳定复用，再拆成独立 `technical-reasoning-clarity-audit`。
