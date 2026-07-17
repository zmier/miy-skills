# REQ: clarify record status vs thread status

## Summary

`miy-mail` 已经可以管理 Markdown 邮件、回复和 note，但需要进一步明确“单条记录状态”和“thread 状态”是两套状态，并加入一个真实项目样例迁移 UAT，降低后续误用概率。

## Metadata

| Field | Value |
|---|---|
| Date | 2026-07-08 |
| Reporter | TASK03-research-design-v0 |
| Target | /Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail |
| Type | REQ |
| Severity | P3 |
| Evidence status | complete |
| Status | fixed |
| Fixed date | 2026-07-08 |
| Fix log | /Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/fix-log.md |

## Environment

| Field | Value |
|---|---|
| Working directory | /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究 |
| Command / tool | local Markdown correspondence management |
| Input | TASK03 CSMAR data request correspondence |
| Output path | /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails |

## Reproduction

```text
1. Use miy-mail to create or review a task-level emails/ directory.
2. Compare record-level metadata Status with README thread index Status.
3. Observe that SKILL.md lists both status sets, but does not explicitly warn that they are two different state machines.
4. Existing TASK03 CSMAR sample was created before miy-mail was finalized, so it lacks Channel, Next action and Sendable Body, and its README index is simpler than the current miy-mail template.
```

## Expected Behavior

`miy-mail` should make the two status levels explicit:

```text
Record status:
draft / sent / received / recorded / superseded

Thread status:
draft / waiting / replied / needs-followup / closed
```

The skill should also include or reference a UAT that migrates an existing correspondence sample to the current template.

## Actual Behavior

Current `SKILL.md` documents both status sets, but the distinction is implicit. A caller may mistakenly put thread status such as `waiting` or `closed` into a single email record, or use record status such as `received` as a thread status.

The existing TASK03 CSMAR correspondence sample is usable but not fully aligned with the finalized `miy-mail` template.

## Evidence

- /Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/SKILL.md
- /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails/README.md
- /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails/THREAD-20260708-csmar-fund-manager-data/EMAIL-20260708-1543-to-data-colleague-csmar-fund-manager-data-request.md

## Downstream Impact

This is not blocking, but unclear status semantics can create messy correspondence ledgers:

- a single email record may be marked `waiting` even though waiting is a thread-level state;
- a thread may be marked `received` even though received is a record-level state;
- README thread index and per-file metadata may drift;
- future agents may be unsure whether a correspondence item is awaiting send, awaiting reply, already replied, or closed.

## Suspected Area

| File / Module | Why suspicious |
|---|---|
| /Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/SKILL.md | Needs one explicit paragraph separating record status from thread status |
| /Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails | Real sample can serve as UAT fixture for migration |

## Regression Requirement

After the documentation update, run a UAT using the TASK03 CSMAR sample or a temporary copied fixture:

```text
1. Ensure the outbound email record has Channel, Status, Next action, and Sendable Body.
2. Ensure README thread index has Topic, Participants, Initial item, Latest item, Status, and Next action.
3. Confirm the email record uses only record-level status values.
4. Confirm the README thread uses only thread-level status values.
5. Confirm a future REPLY item can set Reply to the original EMAIL file and update README Latest item / Status / Next action.
```

Pass standard:

- record metadata does not use `waiting`, `replied`, `needs-followup`, or `closed`;
- README thread status does not use `sent`, `received`, `recorded`, or `superseded`;
- outbound email has a copy-ready `## Sendable Body`;
- no one needs to read the chat history to understand the thread state.

## UAT / Acceptance Run

Suggested real sample:

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/tasks/TASK03-research-design-v0/emails/
```

If modifying the real project sample is not desired during skill repair, copy that directory into a temporary fixture, run the migration there, and record the copied path and pass/fail result in `fix-log.md`.

修复时未修改真实项目样例，已复制到以下 UAT fixture 并完成迁移验证：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/uat/TASK03-csmar-migrated/emails/
```

验证记录见：

```text
/Users/narra/Documents/alib/Writer/00 信息/miy-skills/skills/tools-skill/skills/miy-mail/issues/REQ-2026-07-08-clarify-status-model/fix-log.md
```

## Resolution

Fixed by making record status and thread status explicit in `miy-mail/SKILL.md`, adding misuse warnings and migration UAT guidance, and validating a migrated TASK03 fixture with separate record-level and thread-level status checks.

## Acceptance Criteria

- [x] Add an explicit note that record status and thread status are separate state models.
- [x] Add a misuse example or short warning about not mixing the two status sets.
- [x] Add or reference a migration UAT for an existing correspondence sample.
- [x] Ensure the UAT pass standard checks both per-file metadata and README thread index.
