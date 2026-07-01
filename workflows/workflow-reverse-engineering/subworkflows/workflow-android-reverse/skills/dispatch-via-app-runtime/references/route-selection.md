# App 运行态代发路线选择

## 决策表

| 观察 | 推荐路线 | 说明 |
|---|---|---|
| App 内 `executeRPC(operation, body)` 可调用，外部 Sign/miniwua/Did 不可复现 | R4-A | Python 只调度，App 代发 |
| 网关 envelope 可观察，但字段绑定账号/设备/TEE | R4-A | 不拆字段 |
| envelope 已证明短时可复用，且外发环境不被校验 | R4-B | 研究分支，谨慎 |
| 只找到单个 Sign 函数，但 Did/miniwua/authorization 仍不明 | R4-A 或继续字段分层 | 不要把 Sign 函数当完整复现 |
| 长连接已有稳定 session，找到 sendMessage/sendFrame | R4-M | App 代发消息 |
| 目标是无设备 CLI 工具 | R3/Unidbg/宿主 App | R4 只能作为过渡或混合路线 |

## R4-A 首选原则

当字段彼此可能绑定时，优先保持 App 内一致性：

```text
Ts 与 Sign 同步；
Did 与 miniwua 同源；
authorization 与账号态一致；
TLS/连接/session 与发送环境一致。
```

不要默认创建：

```text
getAuthorization()
getDid()
getTs()
getSign()
getMiniwua()
```

除非已经证明这些字段独立、可安全传输、无敏感泄漏且不破坏服务端校验。

## 失败回退

| 失败 | 先查 | 下一步 |
---|---|---|
| Attach/Frida timeout | 设备、进程、frida-ps、session 重建 | `diagnose-android-instrumentation` |
| App 内 RPC 返回业务拒绝 | 入参、账号态、服务端窗口、频率 | 降频或停止 |
| Python 外发失败而 App 内成功 | Header/body/账号态/设备态/TLS/连接态首差 | 不回滚算法 Green |
| 长连接没有响应 | callback/listener/message id/session state | 继续 R4-M 追响应路径 |

## 状态命名

建议写入 ledger：

```text
app-runtime-dispatch-planned
app-runtime-dispatch-dry-run-passed
app-runtime-dispatch-smoke-passed
blocked-by-runtime-boundary
blocked-by-connection-state
blocked-by-server-window
```
