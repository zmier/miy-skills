# Skill 变更提案

- 来源案例：`Writer/03 Projects/260521-基金经理研究/tasks/TASK00-project-governance/`
- 触发证据：项目已有 TASK01--TASK08 与多条竞争机制线索；用户提出先盘点全部 roadmap，再追问应开新 TASK 还是建立 TASK00，并要求 TASK00 roadmap 与各 TASK 稳定入口关联。
- 当前 Skill：`task-driven-project-manager`
- 问题类型：`missing-rule / template-gap / new-capability`
- 建议：`update-existing`

## 泛化判断

- 可复用问题：复杂探索项目需要一个不拥有下级证据、但能跨 TASK 比较 workstream、维护决策历史并控制下一任务开启的 standing governance layer。
- 触发条件：多个顶层 TASK；证据状态分化；下一步需比较路线；root README 过载；普通新 TASK 会掩盖当前工作其实是元决策。
- 停止条件：TASK00 registry/portfolio/decision log/dates reviews 建立；跨层链接通过；当前下一 Gate 和 re-review trigger 明确。
- 不适用范围：小型线性项目、普通 parent/subtask、单次状态汇报、纯排期问题。
- 是否含个案固定值：`no`

## 实现

- 修改文件：`SKILL.md`；父级 `workflow-task-driven-project/SKILL.md`、`references/routing.md`、`references/core-loop.md`。
- 新增 reference/script/asset：`references/standing-project-governance.md`、`assets/standing-task00-governance-template.md`、dialogue note、structural evaluation。
- 总编排路由变化：当项目进入 cross-TASK portfolio arbitration 时，父 workflow 先执行 portfolio gate，再决定是否创建下一 substantive TASK。
- 模板变化：新增 TASK00 README、registry、portfolio、decision log、dated review、ReAct log 和 backlink 模板。

## 验证

- 来源案例回归：TASK00 已真实落地，含两张跨层 roadmap、八个顶层 TASK 注册、研究线头组合、决策日志和首次带日期评审；相对链接检查通过。
- 既有案例回归：规则为条件触发，不改变小型项目、普通 lineage map、project change map 和 multi-agent acceptance 的既有行为。
- 新案例 forward-test：pending。
- 迁移状态：`structural-green / forward-test-pending`

