# REQ: Markdown email and reply correspondence management

## Summary

`tool-jira` 已经能把工具/Skill 问题整理成可追踪 issue；研究项目还需要一个相邻能力，用统一命名和 metadata 管理 Markdown 邮件、回复、会议 note 与后续确认。

## Metadata

| Field | Value |
|---|---|
| Date | 2026-07-08 |
| Reporter | TASK03-research-design-v0 |
| Target | /Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira |
| Type | REQ |
| Severity | P3 |
| Evidence status | complete |
| Status | fixed |
| Fixed date | 2026-07-08 |
| Fix log | /Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/fix-log.md |

## Environment

| Field | Value |
|---|---|
| Working directory | /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究 |
| Command / tool | local Markdown project management |
| Input | TASK03 CSMAR data request correspondence |
| Output path | /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails |

## Reproduction

```text
1. 研究 task 需要给数据同学写一封外部数据需求邮件。
2. 邮件后续会收到回复，并可能有多轮追问。
3. 当前项目里已有 J-* 邮件草稿，但缺少稳定 thread、direction、recipient、reply-to 和状态命名规则。
4. 用户询问是否应在 task 下新建 EMAIL 文件夹，以及如何从文件名体现回复了谁和日期时间。
```

## Expected Behavior

希望有一个 Markdown correspondence 管理能力，可以复用 `tool-jira` 的结构化思路，但面向邮件和回复：

- 为 task 创建 `emails/` 或 `correspondence/` 目录；
- 按 thread 聚合往来；
- 生成 outgoing email、reply、note 的文件名；
- 在文件头写入 From / To / CC / Date / Subject / Reply to / Status；
- 在 README 中维护 thread index；
- 能区分 draft、sent、replied、closed；
- 能生成一个适合复制发送的正文草稿。

## Actual Behavior

`tool-jira` 当前只覆盖 BUG / REQ / DOC / REG issue 的创建和验收，不能直接管理邮件、回复与 thread 级 correspondence。

## Evidence

- /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails/README.md
- /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails/THREAD-20260708-csmar-fund-manager-data/EMAIL-20260708-1543-to-data-colleague-csmar-fund-manager-data-request.md

## Downstream Impact

如果没有统一规则，研究项目中的数据确认、coauthor 往来和字段回复会散落在 task 根目录，后续很难判断：

- 哪封邮件对应哪个 task；
- 哪个回复对应哪封请求；
- 哪些问题已经 closed；
- 哪些数据口径仍在等待确认；
- 文件名中的日期、收件人和主题如何排序。

## Suspected Area

| File / Module | Why suspicious |
|---|---|
| /Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/SKILL.md | 可扩展为 correspondence 模式，或抽出 sibling skill |
| /Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills | 更适合新增 `tool-correspondence` / `tool-email-thread` skill |

## Regression Requirement

新增或改造后，需要能在一个临时 task 下执行以下 UAT：

```text
1. 创建 emails/README.md。
2. 创建 THREAD-YYYYMMDD-topic-slug/。
3. 创建一封 EMAIL-YYYYMMDD-HHMM-to-recipient-topic.md。
4. 创建一封 REPLY-YYYYMMDD-HHMM-from-sender-re-topic.md。
5. README thread index 能正确记录 status 和初始邮件。
```

Pass 标准：

- 文件名包含 direction、date-time、participant 和 topic；
- 每个文件有统一 metadata；
- reply 能通过 `Reply to` 字段指向原始 email；
- 不要求用户阅读聊天记录也能理解上下文。

## UAT / Acceptance Run

当前已在真实研究 task 中做了一次手工样例：

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails/
```

后续修复方应基于该样例或新建 fixture 补一次自动/半自动生成验证，并在 `fix-log.md` 中记录输出路径和 pass/fail。

修复完成后已新增 `miy-mail` sibling Skill，并补充 UAT fixture：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/uat/TASK-miy-mail-smoke/emails/
```

验证记录见：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/tool-jira/issues/REQ-2026-07-08-markdown-email-correspondence/fix-log.md
```

## Resolution

Fixed by creating sibling Skill `miy-mail` under `tools-skill`, updating parent routing, linking it into `/Users/narra/.codex/skills/miy-mail`, and validating both Skill structure and UAT fixture.

## Acceptance Criteria

- [x] 明确该能力是并入 `tool-jira`，还是作为 sibling skill 新建。
- [x] 提供 thread folder、email、reply、note 的命名规范。
- [x] 提供 outgoing email 和 inbound reply 的 Markdown 模板。
- [x] 提供 README thread index 更新规则。
- [x] 给出一条 UAT 流程和 pass/fail 标准。
