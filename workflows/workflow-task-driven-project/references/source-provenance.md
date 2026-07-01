# Source Provenance

## 来源

本 workflow 首版来自真实项目反哺：

```text
Writer/03 Projects/.../PROJECT-Android目标业务网络通道识别
```

触发经验：

- 顶层 TASK 从 1 个项目自然增长到 30+；
- 一个大型 TASK 内出现子任务、请求池、限速学习器、设备态实验；
- 需要将 terminal/raw 证据提升为 Markdown；
- 需要项目级 final_outputs 复盘；
- 需要 Obsidian 双链从复盘回到证据；
- 项目经验反哺 Android reverse workflow 和 task-driven-project-manager。

## 迁移状态

```text
status: structural-green
forward-test: partial
```

## 边界

项目中的业务细节、真实响应、设备标识、服务端限制数字和案例日志不进入本 workflow。本 workflow 只保留项目组织方法。

## 2026-06-22 分形 task-driven 升级

来源项目：

```text
Writer/03 Projects/冒险者工会/PROJECT-小红书云手机自动发布
```

触发经验：

- 用户指出 `task-driven` 不是只适用于“完成项目”的执行阶段，而是一个分形结构。
- “评估要不要做这个项目”本身也应是 task-driven project。
- 外包项目尤其需要先有机会评估 project，再决定是否创建实际执行 project。
- `task-driven-project-manager` 应作为 scaffold 子能力，而不是总入口的全部。
- 通用 workflow 应配合专用场景 adaptor：外包、学术研究、论文研究、软件工具等。

迁移内容：

- 新增 `references/fractal-task-driven.md`。
- 新增 `references/stage-gates.md`。
- 新增 `references/project-type-adaptors.md`。
- 新增 `templates/opportunity-evaluation-project-template.md`。
- 新增 `skills/outsourcing-project-adaptor/SKILL.md`。
- 更新父入口和 orchestrator。

边界：

飞源信息客户的具体账号、平台细节、API 文档和业务材料留在项目 TASK 中；workflow 只吸收“机会评估也是 task-driven”的通用结构。
