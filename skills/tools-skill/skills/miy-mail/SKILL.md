---
name: miy-mail
description: 管理研究项目或工作任务中的 Markdown 邮件、回复、会议 note 和后续确认。Use when a task needs tracked correspondence folders, email/reply/note filenames, thread metadata, copy-ready outgoing email drafts, inbound reply records, README thread indexes, record-level draft/sent/received/recorded/superseded status, or thread-level draft/waiting/replied/needs-followup/closed status tracking.
---

# Miy Mail

把项目沟通整理成可追踪的 Markdown correspondence ledger。使用本 Skill 创建或维护 task 下的 `emails/` 或 `correspondence/` 目录、thread 文件夹、邮件草稿、回复记录、会议/飞书/电话 note，以及 README thread index。

## 边界

- 只管理 Markdown 记录、命名、metadata、状态和可复制正文；不负责真实发送邮件。
- 不把邮件往来写成 `tool-jira` issue；只有工具缺陷、契约缺口、回归要求才交给 `tool-jira`。
- 不声称邮件已发送、已收到或已 closed，除非用户、证据文件或上下文明确说明。
- 不把验证码、登录、权限申请、真零结果和技术失败混写；在 metadata 或 note 中分开记录。
- 不要求后续读者阅读聊天记录才能理解 thread。

## 输入

尽量收集：

- task 或项目目录；
- 沟通主题和稳定 topic slug；
- 发件人、主收件人、CC、参与人；
- 方向：`outbound`、`inbound` 或 `note`；
- 渠道：`email`、`meeting`、`feishu`、`phone`、`other`；
- 时间，默认使用当前本地时区 `Asia/Shanghai`；
- subject；
- 被回复的源文件；
- 当前状态和下一步行动；
- 邮件正文、原始回复、会议纪要或用户口述内容。

信息不全时，用 `unknown` 或 `none` 明确标出，不要编造。

## 核心状态模型

把状态分成两套独立模型：

- Record status：只写在单个 `EMAIL`、`REPLY`、`NOTE` 文件的 metadata 里，描述这条记录本身。
- Thread status：只写在 `README.md` 的 thread index 里，描述整组往来的当前进展。

不要混用两套状态。不要把 `waiting`、`replied`、`needs-followup`、`closed` 写进单封邮件的 `Status`；不要把 `sent`、`received`、`recorded`、`superseded` 写进 README thread index 的 `Status`。

常见映射：

| Event | Record status | Thread status |
|---|---|---|
| 起草首封邮件 | `draft` | `draft` |
| 用户确认已发送 | `sent` | `waiting` |
| 收到对方回复 | `received` | `replied` 或 `needs-followup` |
| 记录会议/飞书/电话 note | `recorded` | 保持当前 thread status，或按内容更新为 `needs-followup` / `closed` |
| 问题已处理完 | 保持最后一条记录的 record status | `closed` |

## 目录

优先放在具体 task 下：

```text
<task>/
└── emails/
    ├── README.md
    └── THREAD-YYYYMMDD-topic-slug/
        ├── EMAIL-YYYYMMDD-HHMM-to-recipient-topic-slug.md
        ├── REPLY-YYYYMMDD-HHMM-from-sender-re-topic-slug.md
        └── NOTE-YYYYMMDD-HHMM-channel-topic-slug.md
```

选择目录名：

- 主要是邮件往来时，用 `emails/`。
- 同时包含会议、飞书、电话和邮件时，可以用 `correspondence/`。
- 如果项目里已有其中一个目录，沿用现有目录，不并行创建第二套。

## 命名规则

Thread 文件夹：

```text
THREAD-YYYYMMDD-topic-slug
```

- `YYYYMMDD` 用 thread 首次创建或首封邮件日期。
- `topic-slug` 使用稳定英文或拼音短横线 slug，尽量不随每封回复变化。

单条记录：

```text
EMAIL-YYYYMMDD-HHMM-to-<recipient-slug>-<topic-slug>.md
REPLY-YYYYMMDD-HHMM-from-<sender-slug>-re-<topic-slug>.md
NOTE-YYYYMMDD-HHMM-<channel>-<topic-slug>.md
```

约定：

- 文件名只放主收件人或主要回复人；完整收件人写入 metadata。
- `YYYYMMDD-HHMM` 使用 24 小时制和 `Asia/Shanghai`。
- 如果实际收发时间未知，用记录时间命名，并在 `Date` 中写 `unknown, recorded at ...`。
- 文件名使用 ASCII 小写 slug，不使用空格和中文。

## Metadata 模板

每个文件开头放一个 metadata 表：

```markdown
| Field | Value |
|---|---|
| Thread | THREAD-YYYYMMDD-topic-slug |
| Direction | outbound / inbound / note |
| Channel | email / meeting / feishu / phone / other |
| From | <sender> |
| To | <recipient or participants> |
| CC | <cc or none> |
| Date | YYYY-MM-DD HH:MM Asia/Shanghai |
| Subject | <subject or note title> |
| Related task | <task id or path> |
| Reply to | <source file path or none> |
| Status | <record status only: draft / sent / received / recorded / superseded> |
| Next action | <next action or none> |
```

## Outbound Email

创建主动邮件时：

1. 创建或复用 thread 文件夹。
2. 创建 `EMAIL-...md`。
3. `Direction` 写 `outbound`，`Status` 初始通常写 `draft`。
4. 正文放在 `## Sendable Body` 下，确保可以直接复制发送。
5. 如果邮件真正发出后用户要求更新，把该文件 `Status` 改成 `sent`，并更新 README thread status。

推荐结构：

```markdown
# <subject>

| Field | Value |
|---|---|
| Thread | THREAD-YYYYMMDD-topic-slug |
| Direction | outbound |
| Channel | email |
| From | <sender> |
| To | <recipient> |
| CC | <cc or none> |
| Date | YYYY-MM-DD HH:MM Asia/Shanghai |
| Subject | <subject> |
| Related task | <task id or path> |
| Reply to | none |
| Status | draft |
| Next action | send / wait for reply / revise |

## Sendable Body

主题：<subject>

<copy-ready email body>

## Context Notes

- <optional internal note>
```

## Inbound Reply

记录回复时：

1. 创建 `REPLY-...md`。
2. `Direction` 写 `inbound`，`Status` 写 `received`。
3. `Reply to` 指向被回复的邮件或上一条 reply 文件。
4. 保留原始回复摘要或全文来源；不要把自己的解释混进原始回复。
5. 在 `## Extracted Commitments / Decisions` 中整理承诺、口径、缺口和下一步。
6. 更新 README 中的 `Latest item`、`Status` 和 `Next action`。

推荐结构：

```markdown
# <reply subject>

| Field | Value |
|---|---|
| Thread | THREAD-YYYYMMDD-topic-slug |
| Direction | inbound |
| Channel | email |
| From | <sender> |
| To | <recipient> |
| CC | <cc or none> |
| Date | YYYY-MM-DD HH:MM Asia/Shanghai |
| Subject | Re: <subject> |
| Related task | <task id or path> |
| Reply to | <EMAIL-...md or REPLY-...md> |
| Status | received |
| Next action | <follow-up or none> |

## Received Content

<quoted or summarized reply content>

## Extracted Commitments / Decisions

- <decision, field answer, promised file, or blocker>

## Next Action

<what to do next>
```

## Notes

会议、飞书、电话或口头同步写成 `NOTE-...md`：

- `Direction` 写 `note`。
- `Channel` 写真实渠道。
- `From` 可以写记录人，`To` 写参与人。
- `Reply to` 指向相关 email/reply 或 `none`。
- `Status` 写 `recorded`，除非该 note 取代了旧记录则写 `superseded`。

## README Thread Index

如果 `README.md` 不存在，创建：

```markdown
# <task> Correspondence

本目录保存 <task> 的邮件、回复、会议 note 和后续确认。

## Thread Index

| Thread | Topic | Participants | Initial item | Latest item | Status | Next action |
|---|---|---|---|---|---|---|
| `THREAD-YYYYMMDD-topic-slug` | <topic> | <people/roles> | `EMAIL-...md` | `EMAIL-...md` | draft | send |
```

更新规则：

- 新 thread：新增一行，`Initial item` 和 `Latest item` 先指向首个文件。
- 新 reply 或 note：更新 `Latest item`、thread-level `Status`、`Next action`。
- 多轮往来：不要改 thread slug，除非主题实质变化；主题变化时新开 thread，并在旧 thread note 中交叉引用。

## 状态

单条文件状态。只允许出现在 `EMAIL`、`REPLY`、`NOTE` 的 metadata `Status` 字段中：

| Status | 用途 |
|---|---|
| `draft` | 已起草，尚未确认发送 |
| `sent` | 用户或证据明确说明已发送 |
| `received` | 已记录对方回复 |
| `recorded` | 已记录会议、飞书、电话或口头 note |
| `superseded` | 被后续记录替代，保留历史 |

Thread 状态。只允许出现在 `README.md` thread index 的 `Status` 字段中：

| Status | 用途 |
|---|---|
| `draft` | 初始邮件还在起草 |
| `waiting` | 已发出，等待对方 |
| `replied` | 已收到回复，尚需判断是否继续 |
| `needs-followup` | 需要补问、补材料或二次确认 |
| `closed` | 本 thread 的问题已经处理完 |

误用示例：

```text
错误：EMAIL metadata Status = waiting
正确：EMAIL metadata Status = sent；README thread Status = waiting

错误：README thread Status = received
正确：REPLY metadata Status = received；README thread Status = replied 或 needs-followup
```

## UAT / Acceptance Run

验证本 Skill 创建新 correspondence 时，在临时 task 下执行：

```text
1. 创建 emails/README.md。
2. 创建 THREAD-YYYYMMDD-topic-slug/。
3. 创建 EMAIL-YYYYMMDD-HHMM-to-recipient-topic-slug.md。
4. 创建 REPLY-YYYYMMDD-HHMM-from-sender-re-topic-slug.md，并让 Reply to 指向原始邮件。
5. 更新 README thread index 的 status、initial item 和 latest item。
```

Pass 标准：

- 文件名包含 direction、date-time、participant 和 topic。
- 每个文件都有统一 metadata。
- outbound email 有可复制的 `## Sendable Body`。
- inbound reply 能通过 `Reply to` 指向源文件。
- README 能看出 thread 当前状态和下一步。
- 不读聊天记录也能理解上下文。

迁移旧 correspondence 样例时，使用真实样例的副本，不直接改原项目，执行：

```text
1. 复制旧 emails/ 到 issue 或临时 UAT 目录。
2. 给 outbound email metadata 补 `Channel`、record-level `Status` 和 `Next action`。
3. 把可发送正文移动到 `## Sendable Body` 下。
4. 把 README index 升级为 `Thread / Topic / Participants / Initial item / Latest item / Status / Next action`。
5. 如需验证 reply 链路，新增一条 `REPLY-...md`，让 `Reply to` 指向原始 `EMAIL-...md`，并把 README `Latest item` 与 thread status 更新为 `replied` 或 `needs-followup`。
```

迁移 pass 标准：

- 单条记录 metadata 的 `Status` 只使用 `draft`、`sent`、`received`、`recorded`、`superseded`。
- README thread index 的 `Status` 只使用 `draft`、`waiting`、`replied`、`needs-followup`、`closed`。
- outbound email 有 `Channel`、`Next action` 和 copy-ready `## Sendable Body`。
- reply 记录能通过 `Reply to` 指向源文件。
