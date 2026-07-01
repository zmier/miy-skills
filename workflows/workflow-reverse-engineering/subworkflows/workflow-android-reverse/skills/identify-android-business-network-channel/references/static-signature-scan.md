# 静态签名扫描

## 最小扫描词

```text
mobilegw
mpaas
nebula
xriver
rpc
operationtype
h5rpc
jsbridge
bridge
okhttp
websocket
grpc
quic
cronet
native-v8bridge
v8jsbridge
```

## 解释规则

- `assets/mpaas_*`：说明 App 使用或打包了 mPaaS 生态资源，但不直接等于目标业务走 mobilegw。
- `nebulaPreset`、`nebulapresetinfo`、`NEBULA-METAINFO.MF`：强提示 H5/小程序容器。
- `libxriver-*`：强提示 XRiver 容器或相关 native 组件。
- `nebula-bridge.js`、`web-bridge.js`、`libv8jsbridge*`、`libnative-v8bridge.so`：强提示 JSBridge/V8 bridge 路线。
- `OperationType`、`RpcService`、`mobilegw`、`H5Rpc`：强提示业务 RPC/mobilegw 路线。
- `okhttp`、`URLConnection`：普通 Java HTTP 栈候选。
- `websocket`、`grpc`、`quic`、`cronet`：协议或网络库候选。

## 误判提醒

- `QUICKPAY`、`quick login` 不等于 QUIC 协议。
- 随机二进制字符串命中 `rpc` 不能单独作为 RPC 证据。
- APK 未命中明文关键词，不代表运行时不会动态加载相关类、bundle 或 so。

## 输出格式

```markdown
| 线索 | 证据 | 强度 | 解释 | 下一步 |
|---|---|---|---|---|
| Nebula | assets/nebulaPreset/... | 强 | 存在小程序/H5 容器资源 | hook JSBridge/XRiver |
```
