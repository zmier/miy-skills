# Dialogue Insight

状态：`skill-integrated / template-integrated / forward-test-pending`

## 基本信息

- 标题：项目变更谱系图与 clickable Mermaid 导航
- 日期：2026-07-09
- 触发类型：`dialogue-insight`
- 触发场域：`field-case`
- 关联 case / TASK / workflow：`Writer/03 Projects/260521-基金经理研究/tasks/TASK06-rte01-a01-a04-empirical-design/`
- 关联原始材料：TASK06 重构讨论、`outputs/task06-project-change-map.md`
- 敏感边界：不记录基金研究的业务细节、co-author 邮件内容或数据字段，只记录项目治理洞见。

## 原始困惑

> 用户原始问题或关键表达：

```text
OK，是不是有项目管理的什么工具，可以体现出这种项目变更的路径的变化呢？甘特图或者什么mermaid支持的图吗？我不知道我表达的是否清晰，请帮我总结下我的困惑
```

随后进一步追问：

```text
此外，mermaid可以写超链接吗？就点一下就能跳转到对应md文档的那种？
```

在看到 TASK06 的图后进一步判断：

```text
OK。这个「任务谱系图」还挺清楚的。以后在 task-driven-project-manager 中，我们是不是可以默认开启这个图
```

## 当时回答

> Codex 当时的核心回答或共同推进出的表达：

```text
这里最适合的不是单纯甘特图，而是 Task Lineage / 任务谱系图、Change Path / 变更路径图、Traceability Matrix / 追踪矩阵。
Mermaid 支持 click 超链接，但不同渲染器支持不稳定，因此图里放 click，图下面再放普通 Markdown 链接表。
```

## 共同发现

探索性研究项目中的一次“目录重构”往往不只是工程挪文件，而是研究设计口径变化。项目管理文档需要同时回答：

- 旧结果如何保留；
- 新信息如何触发任务结构变化；
- 这些结构变化分别在什么时候发生；
- 新旧路径怎么跳转；
- 后续正式任务从哪里接上；
- 哪些解释边界已经改变。

甘特图表达排期，不适合承载这些问题。更适合的是 lineage graph、change-path graph、traceability table 和 migration table。

进一步共识是：任务谱系图不应只在发生变更后才出现。对多 TASK、嵌套 subtask 或探索性项目，它应作为轻量默认导航面存在；发生结构变更时，再升级为 project change map。

## 候选方法论命题

```text
如果以后遇到多 TASK / 嵌套 subtask / 探索性项目，
应当默认生成 task lineage map；
如果 TASK 被降级、冻结、拆成父任务和修正子任务，
再生成 project change map，
因为 README 文字难以同时表达任务谱系、触发证据、旧结果边界和路径迁移。
```

## 可迁移规则草案

- 输入信号：项目有多个 TASK、嵌套 subtasks、多 agent workstreams，或新证据改变任务结构。
- 处理动作：默认创建 task lineage map；发生结构含义变化时创建 project change map，包含 Mermaid lineage/change-path、关键日期标注、Markdown fallback links、traceability table、migration table。
- 输出要求：默认图放在 `docs/task-lineage-map.md`；变更图放在 parent task 的 `outputs/` 或项目 `final_outputs/`，并从 parent README/log/index 链接。
- 验收标准：读者能从图和表直接找到项目入口、任务树、父任务、冻结旧结果、新修正任务、关键变更日期、迁移路径和下一步 gate。

## 反哺位置

| 目标 | 动作 | 状态 |
|---|---|---|
| workflow | 不新建 workflow；沿用 task-driven project 管理能力 | not-needed |
| Skill | 更新 `task-driven-project-manager/SKILL.md`，新增 Default Task Lineage Map 和 Project Change Maps | skill-integrated |
| reference | 更新 `references/source-provenance.md` | integrated |
| asset/template | 更新 `references/templates.md`，新增 Default Task Lineage Map Template 和 Project Change Map Template | template-integrated |
| test/fixture | 下一新案例验证 | forward-test-pending |

## 与 case 的关系

- case 是否只是触发场域：是，本 case 提供项目治理触发，不把基金研究结论写入通用 Skill。
- case 是否提供 primary evidence：提供 structural evidence，即 TASK06 已按该方法完成重构和导航落盘。
- 哪些内容不能从 case 泛化：邀请制、基金流量、P1-P5 命题、具体数据字段和 co-author 邮件。

## 回顾判断

- 保留为 dialogue：保留原始困惑和“甘特图是否合适”的判断过程。
- 进入 reference：进入 source provenance。
- 升级 workflow / Skill：升级 `task-driven-project-manager` 的默认规则和模板。
- 需要 forward-test：需要在新的探索性项目结构变更案例中验证。

## 日志

- 2026-07-09：captured; skill-integrated; template-integrated; forward-test-pending。
- 2026-07-09：根据用户反馈，将 task lineage map 从变更后产物提升为多任务项目的轻量默认导航图。
