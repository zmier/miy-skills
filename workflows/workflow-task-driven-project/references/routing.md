# Routing

## 一句话

任务驱动项目的核心路由问题是：

```text
当前目标属于哪个阶段？
需要创建哪类 task-driven project？
是否需要专用场景 adaptor？
Green 后进入下一阶段、终止，还是反哺 workflow/skill？
```

## 阶段路由表

| 当前目标 | 项目类型 | 动作 | Green |
|---|---|---|---|
| 判断要不要做 | 机会评估型 project | 归档材料、识别真实需求、评估风险、设计 PoC、做决策 | 接 / 不接 / 先 PoC / 改范围 |
| 完成已确认交付 | 执行型 project | 建 TASK 树、实现、测试、UAT、交付 | 交付物验收通过 |
| 阶段结束总结 | 复盘型 project 或 final_outputs | 证据地图、边界、经验候选 | 可解释、可追溯、可迁移候选明确 |
| 抽象通用能力 | 能力工程 project | 更新 workflow/skill/template，做 forward test | 规则有 provenance 和迁移状态 |

## 项目内部路由表

| 情况 | 放置位置 | 动作 |
|---|---|---|
| 项目尚未成形 | project root | 创建 README、TASK 总说明、Makefile、tests、tasks |
| 新阶段有独立目标 | `tasks/TASKxx-*` | 创建顶层 TASK |
| 同一阶段内部新问题 | `tasks/TASKxx/subtasks/TASKxx-yy-*` | 创建子 TASK |
| 多个已有 TASK 留下竞争路线，需决定下一步 | `tasks/TASK00-project-governance/` | 建 registry、portfolio、dated review 和 decision gate；暂不开新实质 TASK |
| 局部证据或实验结果 | `tasks/TASKxx/outputs/` | 写 Markdown 证据摘要 |
| 局部方法或 runbook | `tasks/TASKxx/docs/` | 写 task-local docs |
| 跨 TASK 的解释、Q&A、决策树 | project `docs/` | 写 project reference |
| 阶段总结或对外交付 | `final_outputs/` | 写 phase review/final report |
| 可复用项目组织规则 | `workflow-task-driven-project` | 更新 references/templates |
| 领域方法规则 | 对应领域 workflow/skill | 更新对应 workflow，不塞进项目管理 workflow |

## Cross-TASK Portfolio Governance

当项目的问题从“下一个已知动作是什么”变成“哪条已有路线更值得下一单位资源”时：

1. 冻结本轮参与比较的 workstream 集合；
2. 从各 evidence-owning TASK 拉取 accepted facts、威胁、输入边界和最小下一动作；
3. 使用 standing TASK00 比较 goal value、evidence maturity、feasibility、information gain per cost 和 risk；
4. 对每条路线标记 `continue / diagnostic / monitor / hold / archive`；
5. 只有通过 portfolio gate 的路线才取得下一 substantive TASK 编号。

TASK00 是 sibling control plane，不是所有 TASK 的新物理父目录。完整协议读取：

```text
../../../skills/task-driven-project-manager/references/standing-project-governance.md
```

## Adaptor 路由

| 信号 | Adaptor | 默认动作 |
|---|---|---|
| 客户聊天、报价、接单、需求咨询 | `outsourcing-project-adaptor` | 先建机会评估型 project |
| 学术研究、论文选题、研究设计 | `academic-research-adaptor` | 待创建，先用通用机会评估结构 |
| 论文写作、审稿修改、投稿 | `manuscript-project-adaptor` | 待创建，路由到 paper/manuscript workflow |
| 软件工具、产品开发、脚本系统 | `software-tool-adaptor` | 待创建，先用执行型 project + TDD |
| 数据分析、报告、可视化 | `data-analysis-adaptor` | 待创建，先用通用 project + notebook |

## 外包项目默认路由

当输入是外包/客户需求时，不默认创建执行型 project。默认先创建：

```text
PROJECT-机会评估-*
```

机会评估 Green 后再决定：

```text
accept -> PROJECT-执行-*
poc-first -> PROJECT-PoC-*
reject -> final_outputs/不接单说明.md
rescope -> 回到 TASK04 客户追问与确认
pending-client -> 输出客户材料请求清单
```

## 新 TASK vs 子 TASK

创建新顶层 TASK，如果：

- 交付对象变了；
- 需要新的验收契约；
- 一个读者可以从该 TASK 独立理解目标；
- 它代表项目主线的新阶段。

创建子 TASK，如果：

- 它仍服务于父 TASK 的主产物；
- 它共享父 TASK 的状态机、数据库、队列、语料库或日志语境；
- 它是故障排查、工程补强、局部 UAT 或风险实验。

## 项目 Review 触发

满足任一条件时，应创建 `final_outputs/*复盘.md`：

- 原始问题已经发生明显升级；
- 完成一个可解释的 Phase；
- 得到新的稳定路线或 Green；
- 发现反复出现的工程坑；
- 准备迁移经验到 workflow/skill。

## 脚手架调用规则

`task-driven-project-manager` 是 scaffold 子能力。当路由已经确定“该创建某类 project”时使用它；不要让 scaffold 取代阶段判断。
