# 动态实验路线

## 容器桥优先

静态命中 Nebula/XRiver/JSBridge 时，优先观察：

- JSBridge 调用名；
- bridge 入参和回调；
- RPC operation 或 service 名；
- H5 页面 URL、appId、bundle id；
- 请求构造前后的 JSON/二进制形态。

优先 hook 高层桥函数，再根据调用栈向下追 RPC 或 native。

## RPC/mobilegw

如果出现 `mobilegw`、`OperationType`、`RpcService`、`H5Rpc`：

- hook RPC 调用入口；
- 打印 operationType、requestData、headers、extParams；
- 打印调用堆栈；
- 记录目标动作窗口内的唯一 RPC。

确认 RPC operation 后，不要立刻跳到外部重放。先补响应侧证据：

- hook bridge callback，例如 `DefaultBridgeCallback.sendJSONResponse`；
- hook response helper，例如 `BridgeResponseHelper.executeSendBack`、`sendBridgeResult`；
- 若存在 RPC response 对象，hook `RVRpcResponse.getResponse` 或实际调用入口返回值；
- 将请求和响应按同一 operation/action 窗口写入请求构造账本；
- 如果响应已经能在 App 内完整观察，先标记为 `A+：App 内 hook 观察完整请求与响应`，再决定是否继续追 mobilegw/transport 出口或做外部重放。

对小程序容器 RPC，常见推进顺序是：

```text
bridge name=rpc
  -> operationType/requestData
  -> callback/response helper
  -> result 结构
  -> RpcInvoker/HttpCaller/HttpManager/HttpWorker/mobilegw 出口
  -> 最小复现分级
```

## 动作窗口与真实 UI 行为

对 H5/小程序页面，不要默认认为 deep link、scheme 或 `adb am start` 与人工点击完全等价。

如果自动跳转出现白屏、半加载、缓存页、缺少前置上下文或只触发部分 RPC，应将证据等级下调，并切换为人工动作窗口：

```text
先启动 Frida hook 窗口
  -> 人类从真实列表页/入口手动点击目标 item
  -> 记录该窗口内 bridge/RPC 请求和响应
  -> 再把最小业务调用抽成 App 内 RPC 工具
```

自动 deep link 可以用于辅助发现页面 URL、appId、query 参数和候选 RPC，但不能单独证明真实页面行为已经完整复现。

另外，页面入口参数不一定就是主接口的最小关键参数。例如详情页 URL 可能使用 `questionId` 打开页面，但主详情正文接口可能实际依赖列表 item 里的 `answerId/commentId`。动作窗口中应同时记录：

- 页面 URL 参数；
- 列表 item 的业务 id；
- RPC `operationType`；
- RPC `requestData`；
- 响应主实体 id。

定位 mobilegw/transport 出口时，优先从“实际干活”的类下手，而不是只挂抽象接口：

- `RpcInvoker.invoke`：确认 service class、method 和业务参数是否进入通用 RPC 调用器；
- `HttpCaller.call`：记录 contentType、rpcVersion、reqDataDigest、signData、extParam；
- `HttpManager.execute`：观察 `HttpUrlRequest` 或 `RpcUrlRequest`，拿到 URL、method、headers、body；
- `RpcHttpWorker.call/executeRequest/executeHttpClientRequest/executeExtClientRequest`：确认 `operationType`、targetUri、targetHost、`isRpcRequest`、`isUseSelfEncrypt`、`isUseContentEncrypt`；
- `HttpUrlRequest.getUrl/getHeaders/getReqData`：记录最终出网请求骨架。

如果 `RVRpcProxy`、`IRpcCaller` 没有命中，不要立刻判定没有 RPC。小程序容器可能绕开这些抽象层，直接进入 Alipay 通用 RPC 栈。此时用 bridge action window 作为时间门控，向下挂 `RpcInvoker -> HttpCaller -> HttpManager -> RpcHttpWorker` 往往更稳。

判断标准：

- 拿到 `Operation-Type`、`mobilegw` URL、body 和加密标志时，标记为 `network-exit-confirmed`；
- 如果 `isUseSelfEncrypt=false` 且 `isUseContentEncrypt=false`，说明该层观察到的 body 不是自加密密文，但外部重放仍可能受登录态、设备态、签名、风控、TEE 或时间戳约束；
- 不要把“定位出网请求”直接等同于“Python 可重放”。外部重放需要单独建立 UAT。

## 普通网络栈

若无容器/RPC 证据：

- Java：`okhttp3.Request$Builder`、`OkHttpClient.newCall`、`HttpURLConnection.connect`；
- Socket：`java.net.Socket.connect`；
- TLS/native：`SSL_write`、`SSL_read`、`connect`、`send`、`recv`。

## 协议对照

- HTTP/2 报错时，做 `http2=false` 对照；
- 怀疑 HTTP/3/QUIC 时，观察 UDP、Cronet、native 连接；
- WebSocket/gRPC 应记录握手、stream/message，而不是只看普通 HTTP 请求。

## 完成标准

动态实验至少回答：

1. 目标动作是否触发该通道；
2. 该通道是否携带业务实体；
3. 能否得到 host/path、operation 或 bridge method；
4. 能否得到响应回调与响应结构；
5. 下一步进入接口漏斗、参数解析、App 内等价调用，还是继续下探网络出口。
