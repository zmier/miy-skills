# User-Facing Agenda Language Upgrade

- Date: 2026-07-07
- Scope:
  - `skills/paper-reading/SKILL.md`
  - `skills/paper-reading/skills/paper-co-read/SKILL.md`
  - `skills/paper-reading/skills/paper-co-read/templates/discussion-outline-template.md`

## Trigger

在正式共同读 `Does Media Coverage of Stocks Affect Mutual Funds' Trading and Performance?` 后，回复中直接写了：

```text
A01：settled-for-now
A02：discussed
A03：next
A04-A06：pending
```

用户指出：普通用户未必知道 A01-A09 的含义。该反馈正确。

## Upgrade

新增规则：

- 内部可以使用 A01-A09、P1/P2、S-Pi-* 和状态词；
- 对用户汇报进度时，必须写成“编号 + 自然语言任务名 + 当前含义”；
- 若用户不熟悉编号，优先使用无编号口语版；
- `discussion-outline-template.md` 新增 `User-Facing Progress Summary`，专门保存可直接对用户说的进度摘要。

## Principle

共同读工作台可以有内部结构，但对话窗口要服务读者理解，而不是暴露 Skill 的实现细节。
