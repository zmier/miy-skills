# 长连接 / 消息 Dispatcher 模式

## 适用

当业务不是请求-响应 RPC，而是：

```text
WebSocket
TCP 长连接
gRPC stream
MQTT
IM sync
自定义二进制协议
```

不要强套 `operationType + requestData`。要找：

```text
connection/session manager
sendMessage / sendFrame / publish / sync
encoder / serializer
callback / listener / event bus
message id / request id
```

## R4-M 结构

```text
Python:
  command/opcode/topic + payload
  requestId
  timeout
  save simplified/summary

App:
  使用现有 session 和 encoder
  send message/frame
  监听 callback 或 message bus
  返回匹配 requestId 的响应
```

## 证据链

至少证明：

```text
发送入口已定位；
消息编码由 App 执行；
session/connection 由 App 持有；
响应 callback 已定位或能关联 requestId；
没有保存 session key / token / 敏感连接凭据。
```

## 何时不做

- 找不到响应路径；
- 消息有真实副作用且无法在授权场景隔离；
- 服务端已限制或反馈压力；
- 需要绕过账号、验证码、支付、交易等访问控制。

## 与抓包关系

SocksDroid/mitmproxy/Reqable 可以帮助确认连接形态，但 R4-M 的核心证据是 App 内发送入口与回调路径，不是一定要在代理中看到明文业务包。
