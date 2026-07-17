# Skill 变更提案

- 来源案例：`CASE-260521-基金经理研究` 的 TASK00-1、TASK09-22、TASK11
- 触发证据：多角色 seminar 选择唯一 Gate；冻结主样本实现偏离后修复；独立实现复现；结果改变下一数据对象
- 当前 Skill：`workflow-research`、`research-brainstorm`、`research-roadmap`、`task-driven-project-manager`、`workflow-tao`
- 问题类型：`missing-rule / template-gap / new-capability`
- 建议：`update-existing`

## 泛化判断

- 可复用问题：多个竞争 research routes 如何从脑暴进入可审计实证并回写全局研究路线。
- 触发条件：存在 frozen anchors、negative evidence、route competition 和 information-gain decision。
- 停止条件：route 已完成 Gate、父级验收、portfolio sync，或被明确 queue/hold/archive。
- 不适用范围：单一路线的普通回归、无稳定事实的早期 idea 发散、小型线性 TASK。
- 是否含个案固定值：`no`

## 实现

- 修改文件：五个目标 Skill / workflow 的入口路由与质量检查。
- 新增 reference/script/asset：中央 reference、dialogue、source provenance、Gate review template、structural evaluation。
- 总编排路由变化：`route competition -> brainstorm -> Chair Gate -> substantive TASK -> audit -> portfolio sync`。
- 模板变化：新增 promotion contract、protocol-conformance 与 claim ladder。

## 验证

- 来源案例回归：TASK00-1、TASK09-22、TASK11 artifacts 能完整映射到新协议。
- 既有案例回归：不改变普通 brainstorm、普通 subtask、普通 roadmap 和小型线性项目路径。
- 新案例 forward-test：pending。
- 迁移状态：`partial / structural-green / forward-test-pending`

