# CASE-260521-基金经理研究

## Case Root

```text
/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究
```

## Why This Case Matters

这个案例用于反哺 `workflow-research`：它不是从一开始就收束成 paper 的项目，而是同时包含选题孵化、数据可得性、移动端采集路线、文献定位、技术失败路线和潜在多篇论文方向。

## Forward-Test Goal

当前 `workflow-research` 仍是 `0.1-beta / seed / structural-draft`。本案例的新增目标是测试：

```text
学术研究项目是否应从线性 R0-R7 阶段模型
转向探索性论证树 / candidate research routes 组合模型。
```

关键构思日志：

```text
../../logs/2026-07-05-从线性阶段到探索性论证树.md
```

在基金经理研究项目完成 route portfolio、子论证、数据补充、文献定位、识别设计和 paper 化取舍的真实试跑之前，不应把当前 `workflow-research` 视为稳定可用规则。

## Current Lessons

- `task-driven-project-manager` 适合执行层工程化，但不应定义学术项目顶层逻辑。
- `workflow-paper` 适合 paper 化之后的学习、写作、自审、返修和交付，但不足以覆盖项目孵化阶段。
- 学术项目需要先维护研究问题、证据链、数据可得性和路线取舍，再决定 TASK 树如何服务它们。
- R0-R7 更适合作为诊断面板，而不是线性推进阶段。
- 大 research 可能应管理多个 candidate routes；每条 route 都有自己的问题、文献、数据、设计、证据、威胁和贡献。
- 强参考文献与核心数据之间需要一套 research-side ↔ data-side 握手机制。研究侧把文献启发的变量、机制和识别需求转成数据 request；数据侧交付 inventory / dictionary / QC / processed panel；研究侧再做 scope-lock 和 acceptance。
- `miy-mail` 在这个案例中有效承担了 correspondence ledger：它保存 request、reply、scope-lock、review 和 next action，避免数据需求在聊天中漂移。
- 当 route portfolio 已有稳定 anchors 和大量负证据时，下一步不应继续扩张规格；应先通过 multi-role seminar 选择一项 high-information Gate，再升格为独立 evidence-owning TASK。
- 冻结分析协议必须由实现级 sample/key/mapping assertions 保护；协议文档正确不代表代码真的执行了 primary design。
- `pattern -> location -> mechanism compatibility -> causality` 是四个不同结论层级；定位共同量出现在哪个经济层级，不等于已经解释 why。
- 同一 case 同时影响多个 Skills 时，应指定 single semantic owner；其他 Skills 只保留职责内路由，避免规则复制和漂移。

## Evidence To Watch

- 项目 README 与 docs 的主线是否清晰；
- `tasks/TASK01` 和 `TASK02` 是否应降级为历史技术路线证据；
- `99-文献与项目管理` 是否应拆成核心文献、项目文献和技术课程支线；
- 数据下载完成后，项目是否能建立 route portfolio，而不是只建立 R0-R7 地图；
- `literature-data-design-handshake` 是否能在另一个研究项目中复用，而不是只适用于 CSMAR/RESSET 和基金经理案例；
- 哪些 route 成为 paper 主干、机制、稳健性、附录、弃用路线或另一篇 paper；
- 试跑后哪些规则可以提升到 `workflow-research/references`、`templates` 或父入口 `SKILL.md`。
- `evidence-gated-route-adjudication` 是否能在一个未参与提炼的新研究项目中完成 route promotion、protocol audit 和 portfolio sync。

## 2026-07-14 Skill Feedback Package

- [Dialogue insight](../../references/dialogues/002-evidence-gated-route-adjudication.md)
- [Central route adjudication reference](../../references/evidence-gated-route-adjudication.md)
- [Research Route Gate Review template](../../templates/research-route-gate-review-template.md)
- [Source provenance](../../references/source-provenance.md)
- [Source-case structural evaluation](evaluations/2026-07-14-evidence-gated-route-adjudication.md)

当前结论：不创建新的 `research-route-governance` Skill。先完成跨 Skill structural integration，并等待新项目 forward-test。
