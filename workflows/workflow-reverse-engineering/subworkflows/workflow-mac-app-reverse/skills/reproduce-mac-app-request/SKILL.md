---
name: reproduce-mac-app-request
description: 在授权 Mac App 逆向任务中，将已确认的目标 HTTP/RPC/WebSocket/gRPC/XPC 业务动作最小化并尝试外部复现，区分 algorithmOk、requestConstructedOk、transportOk、businessOk、runtimeStateBlocked 和服务端窗口。
---

# Reproduce Mac App Request

## 触发条件

- 已有脱敏目标请求样本或运行态 hook 证据；
- 已确认目标动作、method/path/body/header/cookie/response 或 RPC action；
- 授权允许对目标 endpoint 做低频 smoke；
- 已声明停止条件和服务端压力边界。

## 工作流

1. 建立 request construction ledger：URL、method、query、body、headers、cookies、response、动态字段和证据来源。
2. 先用固定样本验证解析和最小化，不直接猜完整算法。
3. 字段级算法、签名、加密、时间戳、nonce、cookie 和 client cert 分开建证据。
4. 外部请求前写明是否 live、频率、样本、停止条件和敏感字段处理。
5. 分开记录：

```text
algorithmOk
requestConstructedOk
transportOk
businessOk
runtimeStateBlocked
serverWindowBlocked
```

6. 若外部复现被 Keychain、client cert、WKWebView cookie、XPC session、App Sandbox container 或服务端运行态 envelope 阻塞，转入 `dispatch-via-mac-app-runtime`。

## Green

```text
externalRequestSentByPython=true
runtimeStateBorrowedFromApp=false
transportOk=true
businessOk=true
sensitiveValuesStored=false
```

如果需要从 App 实时取 header、cookie、cert、session 或 envelope，不能写成纯 M1 Green。

