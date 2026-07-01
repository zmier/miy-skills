# Xposed/Sekiro TASK 契约

## 必填

- 目标 App 包名、进程名、版本、设备；
- Xposed/LSPosed 作用域；
- Sekiro server、group、clientId 生成策略；
- action allowlist；
- forbidden endpoints；
- rate limit；
- raw/sensitive 字段保存策略；
- `externalRequestSentByPython`；
- module reload / App restart / server reconnect 流程。

## 状态

| 状态 | 含义 |
|---|---|
| `module-loaded` | Xposed 模块命中目标进程 |
| `classloader-ready` | 目标 ClassLoader 可定位目标类 |
| `process-routed` | 只在目标业务进程注册服务，其他进程明确 skip |
| `sekiro-online` | client 已连接 server |
| `action-registered` | allowlist action 已注册 |
| `dry-run-passed` | 外部调用未触发真实业务副作用 |
| `single-action-smoke-passed` | 单个低风险业务 action 低频返回预期响应 |
| `transport-ok` | App 运行态调用链或 RPC transport 成功 |
| `business-ok` | 服务端业务语义成功，不能只凭 transport 成功推断 |
| `business-failed-handled` | 业务失败样本返回 `ok=false` 且有可读原因 |
| `request-pool-adapted` | 既有请求池 worker 可显式切换到 Xposed transport |
| `small-window-passed` | 小窗口真实请求通过，且队列状态、raw/simplified 策略不变 |
| `state-changing-action-prepared` | 高危状态变更 action 已完成 prepare，尚未执行破坏性路径 |
| `state-changing-action-executed` | 高危状态变更 action 在 confirm 和 Red 证据下执行 |
| `post-reset-smoke-passed` | 状态变更后目标 runtime 和至少一个低风险业务 smoke 恢复 |
| `long-run-supervised` | supervisor、runtime heartbeat、bucket quota、checkpoint 和 human gate 已闭环 |
| `r4x-green` | 契约、护栏、日志和 UAT 全部满足 |

## 分期 Green

### P1 - module loaded

```text
module-loaded=true
classloader-ready=true
scope selected
restart smoke passed
businessRpcTriggered=false
```

### P2 - action server / Sekiro online

```text
process-routed=true
health/echo passed
unknown action rejected
allowlistOnly=true
sensitiveHeadersReturned=false
```

### P3 - single business action smoke

```text
Frida oracle linked
dry-run-passed=true
real=1 single smoke passed
transport-ok 与 business-ok 分开
有效样本返回核心业务字段
业务失败样本返回 ok=false
raw 默认关闭
```

### P4 - request pool transport adapter

```text
xposedActionListOk=true
transportSwitchExplicit=true
requestPoolWorkerUnchangedExceptTransport=true
smallWindowRealRunPassed=true
workerStatusMachineUnchanged=true
raw/simplified 策略保持一致
```

### P5 - supervised state-changing action

```text
stateChangingActionAllowlisted=true
preparePassed=true
executeRequiresConfirm=true
recentRedEvidenceRequired=true
businessRpcTriggered=false
sensitiveHeadersReturned=false
postResetSmokePassed=true
fallbackOrManualRecoveryDeclared=true
```

### P6 - supervised long run

```text
supervisorAlive=true
runtimeHeartbeat=true
networkHealthChecked=true
businessRuntimeReady=true
bucketQuotaPerInterface=true
checkpointPerEntity=true
redClassifierLayered=true
humanGateDeclared=true
dashboardUsesLiveEvidenceBeforeHistoricalError=true
```

## UAT

- 模块加载日志可见；
- Sekiro client 在线；
- action allowlist 生效；
- unknown action 被拒绝；
- 低风险 action 单条 smoke 通过；
- transport 成功与业务成功分开记录；
- 业务失败样本不会被误报为成功；
- 敏感字段扫描无命中；
- 停止/重启后能恢复或明确失败层。
- 请求池可显式切换 transport，且 Frida oracle/fallback 边界明确；
- 小窗口真实请求通过后才能扩大窗口；
- 高危状态变更 action 有 prepare/confirm/Red evidence/post-smoke；
- 长跑 dashboard 和 supervisor 先看活体证据，再解释历史错误；
- 新 App 未复验前只能标记 `forward-test-pending`。
