# Dialogue Insight: Literature-Data-Design Handshake

状态：`captured / reference-integrated / template-integrated / forward-test-pending`

## 基本信息

- 标题：文献-数据-设计握手机制
- 日期：2026-07-09
- 触发类型：`dialogue-insight`
- 触发场域：`field-case`
- 关联 case / TASK / workflow：`CASE-260521-基金经理研究`; `workflow-research`
- 关联原始材料：基金经理研究项目 TASK01/TASK03/TASK04/TASK05 邮件、数据字典、P0 flow review、项目数据地图
- 敏感边界：不记录具体数据库账号、下载权限、raw 数据内容；只记录 workflow 方法论

## 原始困惑

> 用户原始问题或关键表达：

```text
我们本次先做文献、核心数据，然后去 CSMAR 探索并下载补充数据，
再基于数据和文献设计实验。这个过程，你认为有什么经验总结可以反哺 workflow-research 吗？
基于 workflow-tao、course-driven-skill-engineering。
是否应该开子 SKILL 或者什么？
比如最好有两个同学配合：一个获取数据的同学、一个研究设计的同学（我们），
两个人通过 miy-mail 来沟通？
```

## 当时回答

> Codex 当时的核心回答或共同推进出的表达：

```text
这次案例抓到了 workflow-research 现在最缺的一块：
文献、数据可得性、研究设计之间的协作闭环。

先不要急着直接改 workflow-research/SKILL.md 主流程，
也不要马上造一个很大的新 workflow。
更好的做法是先作为 field-discovery / dialogue-insight 写入 workflow-research/logs/，
再沉淀成 reference 或 template。
如果后续第二个研究项目也复用成功，再升级成子 Skill。
```

## 共同发现

真实研究项目中，很多卡点不是“有没有文献”或“有没有数据”，而是：

```text
文献提出的变量 / 机制 / 识别需求
如何变成数据侧可执行请求；
数据侧交付的字段 / 字典 / QC / coverage
如何反向锁定研究设计。
```

这个过程需要显式的协作协议，而不是把沟通散落在聊天中。

## 候选方法论命题

```text
如果以后一个研究项目已经有强参考文献和核心数据，
但仍需要外部数据库补充变量、机制或 outcome，
应当启动 research-side ↔ data-side handshake：
研究侧发起 data request，数据侧交付 inventory/dictionary/QC，
研究侧 scope-lock，数据侧交付 processed panel，
研究侧 acceptance 后再进入 research design v1。

因为这样能防止两种常见漂移：
1. 文献需求变成无限制数据下载；
2. 数据已下载但研究设计仍无法使用。
```

## 可迁移规则草案

- 输入信号：强参考文献 + 核心数据 + 外部数据缺口。
- 处理动作：request -> delivery -> review -> scope-lock -> processed panel -> acceptance。
- 输出要求：邮件 ledger、字段/代码字典、QC、coverage、review memo、scope-lock 决策。
- 验收标准：研究侧能明确 accepted / accepted-with-exceptions / blocked，并说明 route/design 影响。

## 反哺位置

| 目标 | 动作 | 状态 |
|---|---|---|
| workflow | 在 `workflow-research/SKILL.md` 加最小路由 | structural-green / forward-test-pending |
| Skill | 暂不创建正式子 Skill；候选名 `research-data-design-handshake` | pending |
| reference | 新增 `references/literature-data-design-handshake.md` | reference-integrated |
| asset/template | 新增数据请求邮件、交付 review memo、handshake tracker 模板 | template-integrated |
| test/fixture | 等下一个研究项目 forward-test | pending |

## 与 case 的关系

- case 是否只是触发场域：不是。它也提供了 primary field evidence，因为完整走过文献、数据探索、字典、scope-lock、processed panel、acceptance。
- case 是否提供 primary evidence：提供结构证据，但只是一例。
- 哪些内容不能从 case 泛化：CSMAR/RESSET、基金 flow 字段、基金经理研究变量、具体邮件命名和时间戳。

## 回顾判断

- 保留为 dialogue：是，保留原始困惑和共同发现。
- 进入 reference：是，作为 `literature-data-design-handshake`。
- 升级 workflow / Skill：只轻量进入 workflow 路由；不创建正式子 Skill。
- 需要 forward-test：是，至少一个新研究项目。

## 日志

- 2026-07-09：captured, reference-integrated, template-integrated; forward-test-pending。
