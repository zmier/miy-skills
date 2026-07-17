# Dialogue Insight

状态：`workflow-integrated / skill-integrated / reference-integrated / template-integrated / forward-test-pending`

## 基本信息

- 标题：从“多个 Skill 都能反哺”到证据门控的研究路线仲裁
- 日期：2026-07-14
- 触发类型：`dialogue-insight / field-discovery`
- 触发场域：`field-case / hybrid`
- 关联 case / TASK / workflow：[CASE-260521](../../projects/CASE-260521-基金经理研究/README.md)、TASK00-1、TASK09-22、TASK11、`workflow-research`
- 关联原始材料：seminar Chair adjudication、protocol repair、independent implementation audit、TASK00 portfolio sync
- 敏感边界：通用规则不保留合作者身份、私有数据、完整字段或领域结论；精确估计只留在来源 TASK。

## 原始困惑

> 用户原始问题或关键表达：

```text
回顾这次实践过程，基于 course-driven-skill-engineering，是否可以反哺 task-driven-project-manager、research-roadmap、research-brainstorm、workflow-research、workflow-tao 等等相关 SKILL？我不知道我表达的是否清晰，请帮我总结下我的困惑。
```

这背后还包含一个隐含问题：同一案例产生的规则横跨项目管理、学术脑暴、路线图和 workflow 元编排时，应该由谁定义，怎样避免五个 Skill 复制同一套内容？

## 当时回答

> Codex 当时的核心回答或共同推进出的表达：

```text
这不是分别给五个 Skill 添加几段心得，而是一次跨 Skill 的案例反哺工程。

先区分个案证据、可迁移规则和迁移状态；
再为每条规则指定语义所有者；
其他 Skill 只保留自己职责范围内的路由和验收；
来源案例只能证明 structural-green，需新案例 forward-test 后再决定是否抽新 Skill。
```

## 共同发现

本次实践把一条此前分散的链路完整跑通：

```text
frozen empirical anchor
-> multi-role seminar
-> Chair selects one high-information Gate
-> substantive TASK promotion
-> frozen protocol
-> protocol implementation repair
-> independent audit
-> portfolio / roadmap / next-data-object update
```

新的方法论对象不是普通 brainstorm，也不是普通 task management，而是 `evidence-gated research route adjudication`。

进一步发现：

- Brainstorm 的 Green 不是候选多，而是能明确 `promote-now / queue-data / theory-boundary / archive`；
- 实证 Gate 的 Green 不只是得到结果，还包括协议与代码一致、父级验收和 claim boundary；
- Roadmap 应区分“结果在哪里出现”和“为什么出现”；
- 新证据可以改变下一步的数据经济对象，而不只改变显著性描述；
- 跨 Skill 反馈应采用 single semantic owner，避免重复规则漂移。

## 候选方法论命题

```text
如果一个探索性研究项目已有稳定事实和多条竞争解释，
应当先通过 seminar 选择一项信息增量最高、可冻结、可证伪的 Gate，
再把它升格为独立 evidence-owning TASK，并经过协议一致性与必要的独立审计，
因为“故事数量”和“显著规格数量”都不能替代能重排 DGP 的证据。
```

## 可迁移规则草案

- 输入信号：稳定 anchor、负证据、多路线竞争、规格扩张边际收益下降。
- 处理动作：冻结候选集合，交叉批评，Chair 仲裁，promotion contract，协议审计，父级验收，全局同步。
- 输出要求：明确 route 状态、唯一 Gate、stop rule、claim ladder、next data object。
- 验收标准：读者能追踪“为什么选这条路线、代码是否执行冻结协议、结果改变了什么、仍不能说什么”。

## 反哺位置

| 目标 | 动作 | 状态 |
|---|---|---|
| `workflow-research` | 新增 route lifecycle 和中央 reference | workflow-integrated |
| `research-brainstorm` | Chair final adjudication 与 promotion contract | skill-integrated |
| `task-driven-project-manager` | promotion closeout、protocol-conformance、independent acceptance | skill-integrated |
| `research-roadmap` | claim ladder、audit node、next-data-object transition | skill-integrated |
| `workflow-tao` | 跨 Skill single semantic owner / provenance 规则 | workflow-integrated |
| template | 新增 Research Route Gate Review | template-integrated |
| test/fixture | 来源案例结构评测；新案例待测 | forward-test-pending |

## 与 case 的关系

- case 是否只是触发场域：同时是触发场域和 source-case structural evidence。
- case 是否提供 primary evidence：提供一次完整 lifecycle 的真实运行证据。
- 哪些内容不能泛化：基金、平台、数据库、具体 treatment/outcome、估计值、样本数和下一条领域假说。

## 回顾判断

- 保留为 dialogue：保留“多个 Skill 都能反哺时怎样分层”的问题形状。
- 进入 reference：完整 route adjudication 协议进入中央 reference。
- 升级 workflow / Skill：只升级默认路由和验收，不创建新子 Skill。
- 需要 forward-test：需要在未参与提炼的新研究项目中完成一次 route promotion 与 audit closeout。

## 日志

- 2026-07-14：captured。
- 2026-07-14：reviewed and generalized。
- 2026-07-14：reference/template/workflow/skill integrated。
- 2026-07-14：source-case structural-green / forward-test-pending。

