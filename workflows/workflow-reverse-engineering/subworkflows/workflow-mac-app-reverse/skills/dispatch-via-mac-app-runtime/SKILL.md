---
name: dispatch-via-mac-app-runtime
description: 在授权 Mac App 中，当外部复现被登录态、Keychain、App Sandbox、TCC、证书、session、WKWebView cookie、Electron IPC、XPC helper、TLS/mTLS 或服务端运行态 envelope 阻塞时，设计“借用 Mac App 真实运行态代发请求/动作，外部脚本只做调度、限速、落盘和验收”的 M4/M5 路线。
---

# Dispatch Via Mac App Runtime

## 触发条件

- 外部 HTTP/RPC replay 被登录态、Keychain、证书、session、cookie、设备态或风控上下文阻塞；
- 已定位 App 内 CFNetwork/NSURLSession/WKWebView/Electron/XPC/native socket 发送入口；
- App 内动作可成功，但外部脚本无法独立构造完整 envelope；
- 目标是授权研究、自有 App、课堂靶场或明确授权测试。

## 路线分类

| 路线 | 形态 | 适用 |
|---|---|---|
| M4-A App 代发请求 | 外部传 action/body，App 内发送，外部接响应或观察结果 | CFNetwork/NSURLSession/自研 RPC |
| M4-W Web runtime 代发 | WKWebView/Electron 持有 cookie/session/bridge | WebView/Electron 容器 |
| M4-X XPC/helper 代发 | 业务由 helper/XPC service 发出 | 多进程 App |
| M5-S 服务化封装 | Frida RPC、注入 dylib、本地 helper、XPC action server | 长驻、allowlist、可恢复 |

## 工作流

1. 声明授权边界、目标业务动作、服务端压力、禁止接口和停止条件。
2. 明确哪些状态必须留在 App：Keychain、cookie、client cert、session、sandbox container、XPC connection。
3. 建立 allowlist 和 forbidden list。默认拒绝未知 action、账号修改、支付、交易、破坏性动作和高频采集。
4. 先做 dry-run，不触发真实业务。
5. 单 action 低频 smoke：有效样本和业务失败样本都要验证。
6. 分开返回 `transportOk` 与 `businessOk`，不得把请求发出误报为业务成功。
7. 通过后才能接 request pool、checkpoint、dashboard、通知和 human gate。

## Green

```text
dryRunPassed=true
liveRequestSentByMacApp=true
externalRequestSentByPython=false
allowlistOnly=true
forbiddenActionsDeclared=true
sensitiveValuesStored=false
transportOk 与 businessOk 分开
validSampleBusinessOk=true
invalidSampleBusinessOk=false
```

