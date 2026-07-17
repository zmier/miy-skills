# Skill 变更提案

- 来源案例：`Writer/03 Projects/260521-基金经理研究/tasks/TASK06-rte01-a01-a04-empirical-design/`
- 触发证据：TASK06 因“邀请制”新信息从单一实证设计任务重构为父任务 + frozen first-pass subtask + invited-universe amendment subtask；用户反馈任务谱系图清楚，建议以后在 `task-driven-project-manager` 中默认开启。
- 当前 Skill：`task-driven-project-manager`
- 问题类型：`missing-rule / template-gap`
- 建议：`update-existing`

## 泛化判断

- 可复用问题：多任务项目需要默认可视化任务树；探索性项目中，任务结构因新证据变化后，还需要表达旧结果冻结、新任务接续、关键变更日期和路径迁移。
- 触发条件：项目有多个 TASK、嵌套 subtasks、多 agent workstreams；或 TASK 降级为 subtask、新开 sibling amendment、父任务变成 umbrella、旧结果仍需引用但解释边界变化、文件路径实际迁移。
- 停止条件：已有 README、task lineage map；若发生结构变更，还应有 change map、migration table 和 log，能让读者追踪新旧路径及关键变更时间。
- 不适用范围：纯排期问题优先用甘特图；纯小修小补不需要 project change map；个案业务结论不进入 Skill。
- 是否含个案固定值：`no`

## 实现

- 修改文件：`SKILL.md`
- 新增 reference/script/asset：`references/dialogues/001-project-change-lineage-map.md`
- 总编排路由变化：多任务项目默认生成 task lineage map；探索性项目变更时新增 project change map。
- 模板变化：`references/templates.md` 新增 Default Task Lineage Map Template 和 Project Change Map Template。

## 验证

- 来源案例回归：TASK06 已生成 `outputs/task06-project-change-map.md`，并更新父 README/log。
- 既有案例回归：未执行；该变更不修改已有 multi-agent acceptance 规则。
- 新案例 forward-test：pending。
- 迁移状态：`structural-green / forward-test-pending`
