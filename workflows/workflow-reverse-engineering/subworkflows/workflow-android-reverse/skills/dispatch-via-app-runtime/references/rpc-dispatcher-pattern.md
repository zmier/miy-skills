# RPC / 网关 Dispatcher 模式

## 适用

适合：

```text
mobilegw / mPaaS
JSBridge rpc
自研 API gateway
App 内 HTTP facade
MTop / RpcInvoker / GatewayService
```

关键是存在统一入口：

```text
call(operationType, requestData)
executeRPC(operation, body, headersOrExt)
invoke(apiName, params)
request(service, method, payload)
```

## 最小结构

Agent：

```text
allowlist
forbidden list
get runtime service
normalize requestData
execute inside App
simplify response
return meta
```

Python client：

```text
parse operation/body
dry-run
attach
call exported function
save simplified
optional save raw
write summary
```

返回 meta 至少包含：

```json
{
  "route": "R4-A-app-rpc-dispatcher",
  "operationType": "...",
  "liveRequestSentByApp": true,
  "externalRequestSentByPython": false,
  "plaintextSensitiveValuesStored": false
}
```

## Allowlist 规则

新增 operation 前必须写：

```text
operationType
请求 fixture
是否低风险
是否有副作用
是否涉及个人信息
限速/停止条件
UAT Green
raw 保存策略
```

默认 forbidden：

```text
支付、交易、转账、下单、账号修改；
评论/回复/点赞/关注等可能产生副作用的接口；
已经触发服务端限制或账号冷却的接口；
未知 operation。
```

## TASK31 经验

`TASK31-R4A-App代发RPC原型` 的 smoke 证明：

```text
低风险 allowlist RPC 样本
-> App 内统一 RPC 入口代发
-> Python 收到业务响应
-> Python 不外发 HTTP
```

这是 R4-A 的最小 Green，不代表其他 operation 自动安全或可用。每个新增 operation 都要单独 allowlist 和 UAT。
