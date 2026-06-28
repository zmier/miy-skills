# Mac Network Channel Map

## 候选通道

- CFNetwork / `NSURLSession`
- WebKit / `WKWebView`
- Electron / Chromium net stack / IPC
- XPC service 或 helper 代发
- WebSocket / gRPC / HTTP/2
- HTTP/3 / QUIC / UDP
- native socket / libcurl / custom TLS
- CLI helper / login item / LaunchAgent

## Red 分层

```text
zero-connection
proxy-entry-tls-failed
proxy-entry-protocol-failed
non-target-only
target-observed-no-business-ui
target-request-non-2xx
target-request-2xx-business-failed
target-request-green
xpc-helper-sent-not-main-app
wkwebview-or-electron-hidden-channel
```

## 原则

普通系统代理能看到流量，不代表业务通道已确认。若 UI 业务成功但代理中只有统计、静态资源或统一底层流量，优先转入运行态 hook 或 XPC/helper 进程识别。

