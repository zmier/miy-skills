# Dialogue Insight

状态：`workflow-integrated / skill-integrated / reference-integrated / template-integrated / forward-test-pending`

## 基本信息

- 标题：从“继续深挖还是盘点全部线头”到常驻 TASK00 项目治理层
- 日期：2026-07-13
- 触发类型：`dialogue-insight / field-discovery`
- 触发场域：`field-case`
- 关联 case / TASK / workflow：`Writer/03 Projects/260521-基金经理研究/`；`tasks/TASK00-project-governance/`
- 关联原始材料：项目根 README、TASK01--TASK08 roadmap、TASK00 首次 portfolio review
- 敏感边界：仅保留项目管理问题形状；领域估计、未公开文本、合作者信息与业务数据继续留在来源项目。

## 原始困惑

> 用户原始问题或关键表达：

```text
你是建议，继续朝这个方向挖掘下去吗？还是说，我们先回头再看下我们所有TASK的roadmap，看看目前的「线头」都有哪些，然后再评估下怎么探索
```

在确认需要跨 TASK 盘点后，进一步追问：

```text
你说的这个，应该开个新TASK来做吗？还是开个TASK0，用来统一管理所有task？
```

建立治理层概念后，又补充了跨层导航要求：

```text
那TASK00也应该有 roadmap 对吧？和子task的roadmap关联起来？
```

## 当时回答

> Codex 当时的核心回答或共同推进出的表达：

```text
先做跨 TASK 研究组合评审，而不是立即把一个稀疏但显著的局部候选升级为新主线。

TASK00 是常驻治理控制层，不是普通研究任务，也不是把其他 TASK 搬进去的父目录。它维护任务注册、研究线头组合、决策日志和带日期评审；TASK01+ 保留各自证据所有权。

TASK00 的 portfolio roadmap 表达为什么这样推进；task lineage map 表达任务如何组织。上层节点 click 到下级稳定入口，下级 README 再链接回 TASK00。
```

## 共同发现

已有的 Task Lineage Map 和 Project Change Map 能解释任务组织与结构变化，但还不能解决一个更高层问题：当多个 TASK 都已经产生证据，项目究竟应该把下一单位资源放在哪里？

由此发现需要一个新的治理对象：`workstream portfolio`。它比较的不是文件夹，而是彼此竞争的研究、产品或技术线头。该对象必须与 evidence owner 分离：治理层可以决定 `continue / monitor / hold / archive`，但不能重写下级 TASK 的事实和验收。

进一步形成三层结构：

```text
root README = 当前精简总览
TASK00 = 跨 TASK portfolio / registry / decision gate
TASK01+ = 详细证据与执行 source of truth
```

TASK00 的编号不是时间顺序，而是 standing control plane 的角色编码。它可以在项目进行到中途后补建，且不要求重编号历史 TASK。

## 候选方法论命题

```text
如果一个探索项目已经产生多个有证据支持、但成熟度和成本不同的竞争线头，
应当先建立常驻 TASK00 做跨 TASK portfolio review，
再决定是否开启下一实质 TASK，
因为直接沿着最近或最显著的结果继续，会把局部吸引力误当成项目优先级。
```

## 可迁移规则草案

- 输入信号：多个顶层 TASK、竞争线头、root README 过载、下一步需要比较而非顺序执行。
- 处理动作：建立 TASK00 registry、portfolio、decision log、dated reviews 和跨层 clickable roadmap。
- 输出要求：根 README 保持精简；TASK00 与下级 TASK 双向链接；下级证据不移动、不改写。
- 验收标准：读者能看出共同事实、全部候选、证据缺口、状态、下一 Gate 和决策历史。

## 反哺位置

| 目标 | 动作 | 状态 |
|---|---|---|
| workflow | 父级 `workflow-task-driven-project` 增加 standing governance / portfolio gate 路由 | workflow-integrated |
| Skill | `task-driven-project-manager/SKILL.md` 增加 TASK00 触发、边界与最小结构 | skill-integrated |
| reference | 新增 `references/standing-project-governance.md` | reference-integrated |
| asset/template | 新增 `assets/standing-task00-governance-template.md` | template-integrated |
| test/fixture | 来源案例完成结构评测；新项目迁移仍待执行 | forward-test-pending |

## 与 case 的关系

- case 是否只是触发场域：是；通用规则不依赖基金经理研究的领域结论。
- case 是否提供 primary evidence：提供 structural evidence。TASK00 已真实创建并关联八个顶层 TASK，完成首次 portfolio review。
- 哪些内容不能从 case 泛化：具体研究命题、显著性、样本数字、支付宝/外部数据库字段、合作者通信和下一条领域路线。

## 回顾判断

- 保留为 dialogue：保留“三次追问如何逐步形成治理层”的问题形状。
- 进入 reference：完整协议进入 standing project governance reference。
- 升级 workflow / Skill：升级跨 TASK portfolio gate 与脚手架规则。
- 需要 forward-test：需要在一个未参与提炼、同样出现多路线竞争的新项目中验证。

## 日志

- 2026-07-13：captured。
- 2026-07-13：reviewed and generalized。
- 2026-07-13：workflow-integrated / skill-integrated / reference-integrated / template-integrated。
- 2026-07-13：source-case structural-green / forward-test-pending。

