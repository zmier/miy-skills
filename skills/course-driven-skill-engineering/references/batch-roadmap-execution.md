# 批量 Roadmap 推进

用于用户明确要求“不要每个 TASK 等我确认，按 Roadmap 持续推进到交付”的场景。

## 前置条件

- Roadmap 或 TASK 列表清楚；
- 共享规则已经稳定；
- 不需要实时人工操作、真机配合或生产环境决策；
- 遇到高风险或外部依赖时允许降级为 `forward-test-pending`。

## 每个 TASK 的固定输出

- workflow 位置；
- 之前是什么样；
- 加入之后是什么样；
- 资产归类：`upstream / optimized / task-only / rejected`；
- Skill 变更；
- provenance；
- registry；
- Roadmap；
- log；
- UAT 或结构验收。

## 状态建议

| 状态 | 用法 |
|---|---|
| `workflow-integrated` | Skill 路由和文档已更新 |
| `upstream-copied` | 通用 upstream 原件已纳入 |
| `template-green` | 模板结构或静态检查通过 |
| `new-skill-valid` | 新 Skill 通过 quick validate |
| `structural-green` | TASK/Skill/provenance/registry/Roadmap/UAT 自洽 |
| `forward-test-pending` | 尚未在新案例真实迁移验证 |
| `blocked-by-environment` | 需要真机、账号、服务端或外部工具 |

## 禁止事项

- 不把结构 Green 写成迁移 validated；
- 不为完成 Roadmap 伪造设备、服务端或 UI 结果；
- 不把特定案例脚本原样塞进通用 Skill assets；
- 不把历史 cleanup debt 混同为本轮新增失败。
