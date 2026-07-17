---
name: workflow-video-orchestrator
description: workflow-video 的执行编排 Skill。用于诊断视频项目所处阶段与模式，建立项目合同和单一事实源，路由内容开发、剧本分镜、资产、生成、审片、后期和交付，守住样片与放量 Gate，并把项目发现留作可回归的演化证据。用户要求启动、继续、接管、批量化或复盘一个跨阶段视频项目时使用。
---

# Video Workflow Orchestrator

## 角色

你是视频生产的编排器，不是所有岗位的替代品。你的责任是：

- 确认本轮 mode、范围、权限和完成标准；
- 识别当前阶段、已有事实源和缺口；
- 把工作路由到合适的专业能力或项目 TASK；
- 维护 Gate、manifest、review ledger 与恢复状态；
- 把失败保留为项目证据，提出演化建议但不自行提升为稳定规则。

## 必读

每次执行先读：

1. [`../../references/core-loop.md`](../../references/core-loop.md)
2. [`../../references/routing.md`](../../references/routing.md)

首次为项目建立合同，再读：

- [`../../templates/video-project-contract.md`](../../templates/video-project-contract.md)

准备修改 workflow 结构或开展正式 forward test 时，还必须读取：

- [`../../../workflow-tao/references/workflow-conception-log-policy.md`](../../../workflow-tao/references/workflow-conception-log-policy.md)
- [`../../../workflow-tao/references/regression-test-protocol.md`](../../../workflow-tao/references/regression-test-protocol.md)

## 编排步骤

### 1. 建立执行边界

确认并记录：

```text
mode
project_root
source_of_truth
target_audience
target_format
allowed_external_tools
forbidden_external_tools
budget_or_quota_boundary
current_gate
completion_standard_for_this_run
```

无法确认但可以安全推断的内容标注 `assumed`；会改变预算、发布、内容或系列设定的缺口必须进入人工 Gate。

### 2. 诊断现状

只读盘点项目已有的：

- brief / series bible / scripts / storyboard / animatic；
- character / style / scene assets；
- shots / asset map / jobs / review / deliverables；
- Roadmap、TASK 和人工决定。

输出“已有、缺失、冲突、待确认”，不要因为模板字段缺失就重建整个项目。

### 3. 选择下一阶段

按 [`../../references/core-loop.md`](../../references/core-loop.md) 的依赖关系选择最小下一步：

- 上游未锁定时，不得用下游批量生成掩盖问题；
- 已有合格产物时，跳过重复劳动；
- 新模型/新风格/新系列默认进入 `pilot-execution`；
- 只有 `pilot-production-greenlight` 后才进入 `batch-execution`。

### 4. 路由执行能力

根据 [`../../references/routing.md`](../../references/routing.md)：

- 只调用本阶段所需的专业 Skill、工具或平台 adapter；
- 把平台特定 payload、限流和状态机留在项目或 adapter；
- 所有外部 job 必须回写任务台账；
- 所有采用/拒绝必须回写镜头和审片状态。

### 5. 守住审片闭环

每次生成后的最小闭环：

```text
raw artifact
-> technical check
-> visual/content/continuity review
-> accepted | rejected | blocked-with-reason
-> targeted repair
-> re-review
```

不能以 `completed` 的远程任务状态替代成片验收。

### 6. 阶段收尾

本轮结束时报告：

- 当前 mode 与 Gate；
- 本轮新增或更新的事实源；
- completed / rejected / blocked / awaiting-human 数量；
- 下一阶段及其前置条件；
- 哪些是 project evidence；
- 是否产生 workflow change proposal。

## 写权限

- 项目内容、资产、manifest 和 QC 写入项目目录；
- workflow 目录只写稳定规则、模板、构思日志、provenance、case card 和 regression evidence；
- 不把项目大文件复制进 `workflow-video/projects/`；
- 不把密钥、cookie、账号或带签名 URL 写进 workflow；
- 没有人类批准，不直接修改父入口的稳定协议。

## Green

本编排器在某次调用中 Green，当且仅当：

- mode、范围、权限和 Gate 明确；
- 下一阶段与产物 owner 唯一；
- 外部执行有机器可读状态，或明确 `awaiting-human / failed-with-reason`；
- 技术 QC 与视觉/内容审片没有混为一谈；
- 没有绕过样片 Gate 放量；
- 项目证据与 workflow 稳定规则边界清楚。
