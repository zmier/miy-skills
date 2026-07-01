---
name: build-android-rpc-data-corpus
description: 在经过授权的 Android bridge/RPC/统一网关通道已确认后，把单个 RPC 观察推进为业务接口地图、App 内 Frida RPC 工具、复合业务接口和多入口数据语料库。用于 queryQuestionList、详情、评论、主页 feed、历史专题、ID 去重、source/evidence 追踪、分页游标验证、raw/simplified 输出设计、批量限速、断点续跑和覆盖率声明。不得用于未授权批量采集、账号滥用、绕过访问控制或高频压测。
---

# Android RPC 语料库构建

## 目标

在 `identify-android-business-network-channel` 已确认业务通道、`model-android-rpc-response` 已理解响应结构、`export-frida-rpc` 已能主动调用目标 App 内 RPC 后，把“一个接口能调通”推进为“业务接口体系、复合接口和可追溯语料库能交付”。

本 Skill 不负责初始抓包、破解签名、寻找网络通道或绕过访问控制。它只处理授权范围内已经能观察或主动调用的业务 RPC。

## 输入

- TASK 工作区和授权边界；
- 已确认的 bridge method、operationType、service name 或 App 内 RPC 调用方式；
- 至少一份响应样本或一次 Frida RPC 调用结果；
- 已存在或计划创建的 Python/Frida RPC client；
- 业务目标：接口地图、复合接口、问题 ID 语料、回答语料、经理主页问答语料等；
- 预期覆盖率：只验证单页、某入口窗口、多入口语料库，还是有证据支持全量。

如果 operationType、response callback 或主业务实体尚未确认，返回总编排先调用 `identify-android-business-network-channel` 或 `model-android-rpc-response`。

## 工作流

1. 定义业务目标和覆盖率声明：`single-page`、`paged-window`、`multi-entry-corpus` 或 `full-claimed`。没有服务端 total、业务文档或独立校验时，不得声明全量。
2. 创建或定位 TASK 工作区，从 `assets/rpc-corpus-contract-template.md` 复制 `rpc-corpus-contract.md`。
3. 建立接口地图：页面动作、operationType、关键入参、主实体、分页字段、副作用 RPC、证据文件。
4. 对每个基础 RPC，交给 `export-frida-rpc` 封装最小可调用边界；默认输出 simplified JSON，只有显式 `--save-raw/includeRaw` 才保存完整响应。
   - 如果 R3 外部复现被运行态 Header、设备态、账号态、Sign、miniwua 或连接态阻塞，但 App 内可稳定发送，优先消费 `dispatch-via-app-runtime` 产出的 R4-A/R4-M dispatcher；本 Skill 只负责分页、队列、去重、限速、落盘和覆盖率声明。
5. 对每个响应，交给 `model-android-rpc-response` 补齐 schema、敏感字段、分页语义和 raw 策略。
6. 只有当页面语义天然跨多个 RPC、或调用者会反复组合同一组 RPC 时，才创建复合接口。复合接口必须记录组件 RPC、分页策略、展开规则、完整性字段和失败部分。
7. 对 ID 或实体语料库，定义主键、来源类型、原始证据、去重规则和合并策略。每条记录必须能追到至少一个 source/evidence。
8. 批量运行前先做 dry-run：估算新增数量、重复数量、预计请求次数、随机等待范围、停止条件和落盘路径。
9. 批量运行必须支持 limit、offset、checkpoint、resume、failure file、分桶窗口和随机等待；如果批量调用依赖 Frida RPC 或 App 运行态，先读取 `references/batch-safety-policy.md` 的“Frida RPC 长跑采集”小节，验证真实 TTY/伪终端、长会话复用、session 重建、runtime crash sentinel、人类通报和全局汇总策略；出现账号限制、验证码、403/418、服务端压力反馈或异常窗口时停止。
10. 对疑似服务端窗口单独标记：固定 100 页、约 1000 条、跨专题相同上限、终止空页、账号冷却、分页游标无效等。
11. 合并语料前生成增量报告：新增、重复、冲突、缺 source、缺 evidence、来源分布、覆盖率声明变化。
12. 写回总编排的台账、Mermaid、测试矩阵和 `logs/LOG.md`，明确这是“业务接口/语料库路线”，不是单个 URL 的请求构造树。

## 路由边界

- 初始代理看不到目标业务流量：先用 `capture-android-traffic` 和 `identify-android-business-network-channel`。
- 已确认响应但不知道字段语义：先用 `model-android-rpc-response`。
- 已确认 RPC 但还没有可重复主动调用：先用 `export-frida-rpc`。
- 已确认 App 运行态代发路线，且已有 R4-A/R4-M dispatcher：本 Skill 可直接把 dispatcher 作为数据源，但必须继承其 allowlist、forbidden list、限速和 ReAct log 纪律。
- 目标变成页面接口地图、复合接口、多入口 ID 语料、分页窗口或批量采集：使用本 Skill。
- 单个请求字段仍要破解 sign、密文、did、token：回到 `android-request-reproduction` 的请求构造主轴，不在本 Skill 内扩展。

## 输出

至少产出：

- `interface-map.md`：页面动作到 RPC 的接口地图；
- `interface-specs/*.md`：基础 RPC 和复合接口说明；
- `rpc-corpus-contract.md`：目标、授权、覆盖率、来源、批量护栏和 UAT；
- `outputs/source-coverage-report.md`：来源覆盖与疑似窗口；
- `outputs/corpus.json` 或 `outputs/*.jsonl`：语料主产物；
- `outputs/batch-summary.json` 和 `outputs/batch-report.md`：批量运行报告；
- `logs/LOG.md`：ReAct 过程、观察、决策和停止原因。

## 完成标准

- A：接口地图、基础 RPC、必要复合接口、语料来源、批量护栏和覆盖率声明均有证据；至少一次小批量 UAT 通过；每条语料可追到 source/evidence。
- B：主要接口和语料流程可用，但仍存在服务端窗口、账号限制、运行态长跑不稳定、部分来源未跑完或少量字段待补；覆盖率不得写成全量。
- C：只完成接口地图或单个复合接口原型，批量语料尚未稳定。

如果出现服务端限制、账号冷却或对方反馈压力增大，停止批量任务并记录 `blocked-by-server-window` 或等价状态；不得通过提高并发、换账号、代理池或规避策略继续推进。

## 参考资料

- 设计覆盖率和 source/evidence 时读取 `references/corpus-coverage-policy.md`。
- 设计复合接口时读取 `references/composite-interface-policy.md`。
- 设计批量运行和停止条件时读取 `references/batch-safety-policy.md`。
- 创建 TASK 契约时使用 `assets/rpc-corpus-contract-template.md`。
