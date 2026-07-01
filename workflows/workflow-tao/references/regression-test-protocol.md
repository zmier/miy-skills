---
date: 2026-06-20
type: reference
status: structural-green
scope:
  - workflow-tao
  - skill-regression
  - forward-test
---

# Regression Test Protocol

## 一句话

workflow / 复合 Skill 的修改必须有回归测试意识。尤其是父 Skill、编排 Skill、主轴、路由、完成标准或子 Skill 分工发生变化时，不能只靠修改者主观判断“应该更好”，必须用实践样本回归。

## 触发条件

以下改动应触发回归测试：

- 父 Skill / workflow 入口改动；
- 子 Skill 路由改动；
- 主轴、状态机、产物写权限改动；
- Green / Red / 完成标准改动；
- evidence ledger、Mermaid、QC、issue selection 等输出契约改动；
- 新增或删除子 Skill；
- 把某个规则从 project / TASK 上提到 Skill 或 workflow；
- 把某个规则从父层下沉到子层；
- 修复一个已知退化问题。

## 测试分层

| 类型 | 目标 | 适用 |
|---|---|---|
| smoke regression | 确认没有明显跑偏 | 父 Skill 小改、路由小改 |
| UAT regression | 与真实案例目标质量对比 | 子 Skill 重要改动、输出契约改动 |
| migration test | 验证个案经验可迁移到新样本 | project 反哺 workflow |
| forward test | 验证 workflow 可在未来任务中独立工作 | 标记规则稳定前 |

## Route-only / Executed Capability

涉及外部数据库、浏览器、OCR、视觉、脚本、API 或本地工具链的回归测试，必须区分两种测试：

| 类型 | 证明什么 | 不能证明什么 |
|---|---|---|
| route-only test | workflow / Skill 知道应该调用哪个工具、数据库、子 Skill 或来源 | 不能证明工具真的跑通，不能证明数据库可用，不能证明登录、验证码、下载、解析成功 |
| executed-capability test | 工具链真的执行，并返回真实结果或机器可读的等待 / 失败状态 | 不能自动证明结果质量足够高，仍需后续筛选、QC 或人工判断 |

命名和汇报时必须显式写出：

```text
mode: route-only
```

或：

```text
mode: executed-capability
```

禁止把 route-only 测试汇报为“能力已跑通”。例如：

- `scholar-kit-literature-search` 路由到 WoS/CNKI，只能证明路线正确；
- 只有 `scholar-kit-wos-search` / `scholar-kit-cnki-search` 子 Skill 实际执行并写出结果、等待人工验证或失败原因，才算进入 executed-capability 测试；
- `status=scaffold` 不算数据库检索执行；
- 浏览器打开到高级检索页不算结果检索完成；
- 如果需要人工登录、验证码或确认，测试必须产出机器可读状态，如 `awaiting_human_verification / awaiting_manual_confirmation / failed_with_reason`，不能无声悬挂。

执行型测试的 pass / fail 应至少检查：

- 是否调用了真实执行入口，而不是 scaffold / dry-run；
- 是否写出原始产物；
- 是否写出状态文件或状态字段；
- 是否能区分 completed、true zero result、awaiting human、failed with reason；
- 是否避免把登录、验证码、浏览器占用、网络错误误判成“无结果”。

如果外部工具需要人工验证、机构登录、验证码或慢速页面 readiness，第一次短超时 run 可以标记为 `partial / awaiting-human / observability-issue`，但不能立即等同于工具能力失败。正确做法是：

```text
short-timeout run
-> 记录当前状态和缺失的机器可读状态
-> 完成人工验证或延长等待后 rerun
-> 若 rerun 产出 completed / result-ready，更新本轮结论
-> 保留短超时发现为 observability / waiting-state improvement
```

若后续 rerun 改变了结论，必须同步更新：

- run 级 `pass-fail.md`；
- `regression-log.md`；
- 已创建的 issue / Jira；
- 对用户的状态说明。

不要让早期 `FAIL` 结论滞留成过时事实。

## 纯净 subAgent 规则

如果回归是由 Skill / workflow 修改触发，优先开启环境纯净的 subAgent 来执行测试。

运行 subAgent 前，应先写一个轻量 `task-contract.md` 或等价说明，明确：

- 本次 run 的场景、模式和目标；
- 被测 Skill / workflow；
- 输入文件；
- 必读 Skill / references / assets；
- 禁读材料；
- 输出路径；
- smoke target / UAT target。

没有 task contract 的回归容易变成“让 subAgent 自己猜边界”，不适合作为可复用证据。

若被测 Skill / workflow 支持多个执行模式，`task-contract.md` 必须显式写：

```text
mode:
expected_steps:
allowed_external_tools:
forbidden_external_tools:
pending_outputs_allowed:
completion_standard_for_this_mode:
```

否则无法判断 subAgent 是漏做了外部检索、还是按 `internal-blind-audit / diagnose-only` 等模式正确产出了 pending ledger。

纯净 subAgent 应满足：

- `fork_context=false` 或等价方式，不继承当前讨论上下文；
- 只允许读取测试输入、被测 Skill、必要 references/assets 和测试目标；
- 明确禁读修改过程中的讨论、旧答案、人工期望、无关 TASK；
- 将产物写到独立测试 TASK 或 `tests/runs/`；
- 写 `log.md` 说明读取了哪些 Skill / references / inputs。

主 Agent 不应让修改者自己直接判断“质量变好了”。正确流程是：

```text
Skill 修改
-> 创建测试 TASK / run
-> 纯净 subAgent 执行
-> 产出 md
-> 与测试目标 md / baseline md 做质量对比
-> 记录 pass / fail / regression / improvement
```

## 质量对比

回归测试不是只看有没有文件，而是比较质量。

至少比较：

- 输出是否符合新契约；
- 输出是否符合本次 mode 的完成标准；
- 是否保留旧版关键能力；
- 是否新增了预期能力；
- 是否引入重复、过度复杂、跑偏或不适配；
- 是否减少了 hallucination / overclaim；
- 是否保留目标场景的速度和风格；
- 是否有 Red flag。
- 是否存在跨分支污染，例如父层规则把某个子场景不需要的术语、证据类型或输出形态带入了另一个子场景。

建议产出：

```text
regression-comparison.md
```

字段：

```text
test_id
changed_skill
baseline_output
new_output
target_quality_doc
expected_improvement
observed_improvement
observed_regression
pass_fail
next_action
```

如果本轮回归的主要风险是“父层规则污染子分支”，应增加 `contamination_check`，逐项列出应禁止或不应出现的框架、术语、证据类型和输出风格。例如：

```text
contamination_check
- branch-specific frame absent/present
- branch-specific evidence type absent/present
- output style preserved/drifted
- result
```

若对比发现新产物不仅没有退化，还补上旧 baseline 的已知缺口，应记录为 `observed_improvement`。回归测试不只是防坏，也可以发现子分支是否继承了后续规则升级。

## Baseline / Target

测试目标可以来自三类材料：

1. baseline md：旧版稳定产物；
2. target md：人工认可的目标质量说明；
3. gold fixture：经过 UAT 的最佳案例产物。

如果没有 gold fixture，先建立 smoke target：

```text
必须不退化的 3-7 条质量标准
```

baseline 可以是直接产物，也可以是代理入口指向的已完成 CASE 产物。若使用 proxy baseline，必须在 comparison 中写清真实 baseline 路径，避免以后误以为比较的是空壳文件。

## Pass / Fail

Pass:

- 被测 Skill 能被纯净 subAgent 独立调用；
- 输出符合契约；
- 与 baseline 相比没有关键能力退化；
- 目标改动带来可观察质量提升；
- 新 Red flag 已在 QC 中标出。

Fail:

- subAgent 需要读修改讨论才能完成；
- 输出缺必交付物；
- 旧版关键能力消失；
- 新规则污染无关子分支；
- 质量比较无法说明增强还是变弱；
- 只由修改者主观判断通过。

## 父 Skill 修改后的子分支回归

父 Skill 改动时，必须评估受影响子 Skill。

最小做法：

```text
changed parent skill
-> list child skills potentially affected
-> choose one smoke case per affected branch
-> run clean subAgent
-> compare with branch-specific target
```

例如抽树父 Skill 改动后：

- 学术论文分支：检查是否仍能 full-tree；
- exam 分支：检查是否没有被学术 full-tree 污染；
- GRE 分支：检查是否仍适配 GRE instruction。

如果父 Skill 承担“通用抽象 + 路由”，回归样本不应只选一个子分支。至少选择能代表主要分歧的 paired smoke cases：

```text
generic parent changed
-> branch A smoke: 检查 A 的核心能力仍在
-> branch B smoke: 检查 B 未被 A 污染
-> optional branch C smoke: 检查 adapter / prompt / platform 差异仍被识别
```

paired smoke 的目标不是穷尽测试，而是用最小成本验证父层抽象是否仍保持“高内聚、低耦合”。

## 放置位置

个案回归：

```text
projects/CASE-.../tasks/TASKxx-regression-.../
```

稳定回归样本：

```text
tests/fixtures/
tests/runs/
tests/regression-log.md
```

如果 workflow 还没有 tests 目录，可以先放在项目 TASK 中，等重复使用后再迁移为 fixture。

当一次临时小测证明会反复用作回归时，应升级为稳定测试资产。最小升级标准：

```text
tests/
├── README.md              # 说明有哪些稳定 fixture/run，何时重跑
├── regression-log.md      # 登记每次 run 的模式、结果、反哺点
├── fixtures/              # 小输入样本，不放整篇大材料，除非 UAT 需要
└── runs/YYYY-MM-DD-.../   # 每次实际运行和 pass/fail
```

稳定 fixture 应尽量“小而尖”：

- 测视觉 QC，就截取相关页图和对应 restored table；
- 测外部证据路由，就给 3-5 条 miniature request；
- 测数据库执行，就给一个最小 query；
- 测子分支污染，就给 paired smoke cases。

不要把全量 UAT 当作所有单元回归的唯一入口；全量 UAT 成本太高，容易让回归纪律失效。

建议结构：

```text
tests/
├── README.md
├── regression-log.md
└── runs/
    └── YYYY-MM-DD-meaningful-regression/
        ├── README.md
        ├── branch-a/
        │   ├── task-contract.md
        │   └── outputs/
        │       ├── result.md
        │       └── log.md
        ├── branch-b/
        │   ├── task-contract.md
        │   └── outputs/
        │       ├── result.md
        │       └── log.md
        └── regression-comparison.md
```

`regression-comparison.md` 写在 run 根目录，负责跨分支判断；各分支自己的 `log.md` 只记录执行边界和本分支产物。

## Provenance

每次回归都应记录：

- 被测 Skill 路径；
- 变更原因；
- 测试样本；
- subAgent 是否纯净；
- baseline / target；
- 结果；
- 是否将发现反哺到 Skill / reference / template。

父 Skill 和子 Skill 都有 regression log 时，应双向留痕：

- 子 Skill log 记录本分支是否通过；
- 父 Skill log 记录本次父层改动影响了哪些分支、哪些已测、哪些仍 pending；
- 如果某个分支已由项目 TASK 或此前 clean run 覆盖，应在父层 log 中引用该证据，而不是重复跑或留下含混 pending。

## Cross-skill Issue Reporting

如果回归或执行过程中发现问题属于另一个 Skill / workflow / 工具链，而不是当前 Skill 自己能闭环解决的问题，应调用：

```text
tools-skill -> tool-jira
```

并把问题写到目标对象自己的 `issues/` 目录下，而不是只写在当前 task log 里。

典型场景：

- 当前 workflow 发现下游 Skill 没有履行输出契约；
- 外部工具链实际行为与 Skill 文档不一致；
- route-only / executed-capability / scaffold / handoff / completed 状态混淆；
- 等待人工、验证码、登录、真零结果、技术失败无法区分；
- 修复方需要复现命令、证据路径和回归标准。

报 issue 后，当前 workflow 的回归 log 只引用该 issue 路径和本轮影响；修复方应读取 issue、修复目标 Skill，并按 issue 中的 regression requirement 回归。

如果 issue 在后续复测中被重新定性，例如：

```text
执行能力失败 -> 人工验证慢导致的等待态可观测性不足
```

必须更新 issue 标题、Summary、Actual Behavior、Regression Requirement 和 Evidence，而不是另开一个相互矛盾的新 issue。issue 记录的是问题演化，不只是第一次误判。

## Practice Note: 2026-06-20 Exam Tree Smoke Regression

本协议中的以下规则来自 `argument-tree-extraction` 父 Skill 修改后的 exam / GRE smoke regression：

- 先写 run 级 README 和每个分支的 `task-contract.md`，再开纯净 subAgent；
- 对一个父 Skill 改动同时测中文论效和 GRE 两个代表性子分支；
- 禁读旧 outputs 和 reference answers，让 subAgent 只按新 Skill 独立产出；
- 主 Agent 事后读取 baseline / UAT / reference comparison 做质量比较；
- comparison 中显式写 `observed_improvement`、`observed_regression` 和 `contamination_check`；
- 将结果同时记入子 Skill regression log 和父 Skill regression log。

这次实践说明：回归测试既要防止退化，也要验证父层抽象是否仍能保护不同子分支的边界。

## Practice Note: 2026-06-21 Tool-backed Evidence Regression

本协议中的以下规则来自 `workflow-argument-validity` 验箭头阶段对外部证据能力的回归：

- route-only 小测只能证明路线选择，不能证明 WoS / CNKI / 视觉 / 官方来源真的跑通；
- executed-capability 小测必须调用真实入口并写结果或状态；
- CNKI / WoS 这类浏览器型检索可能需要人工验证，短超时失败不能直接判成工具不可用；
- 若人工验证后 rerun 成功，应把结论更新为 PASS，并保留短超时暴露出的 waiting-state / observability 改进；
- 临时小测一旦会反复使用，就要迁移到 `tests/fixtures`、`tests/runs`、`tests/regression-log.md`；
- 跨 Skill 问题应通过 `tools-skill -> tool-jira` 写到目标 Skill 的 `issues/` 下，并在问题重新定性后同步更新 issue。

这次实践说明：复杂 workflow 的回归不只是验证“文本质量”，还要验证它依赖的工具链能力、状态可观测性和跨 Skill 工单闭环。
