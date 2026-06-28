---
name: capture-mac-app-traffic
description: 根据授权 Mac App 目标设计可重复的流量观察实验，选择系统代理、Reqable/mitmproxy、Network Instruments、Frida/lldb 网络 hook 或进程级通道识别，排查 CFNetwork、NSURLSession、WKWebView、Electron、XPC/helper、WebSocket/gRPC、QUIC、native socket、TLS pinning 和 mTLS。
---

# Capture Mac App Traffic

## 工作流

1. 确认目标动作、授权边界、采集窗口、停止条件和是否允许修改系统代理或证书信任。
2. 把目标拆成基线、启动、登录态确认、目标动作和恢复窗口。
3. 优先建立只读网络基线：进程树、host 候选、端口、协议、日志和 UI 结果。
4. 普通 HTTP/HTTPS 先用系统代理或 Reqable/mitmproxy；Electron/WKWebView 要记录是否继承系统代理。
5. 若代理只看到非目标流量，按 `references/mac-network-channel-map.md` 分类，不继续扩大采集范围。
6. 若目标可能在 helper/XPC 进程发出，先定位发送进程，再决定 hook 主进程还是 helper。
7. 若 TLS/pinning/mTLS 阻断，交给 `diagnose-macos-protection` 或运行态 hook；不要直接宣称接口失败。
8. 输出脱敏请求样本、通道候选树和下一步路由。

## Red 分层

```text
zero-connection
proxy-entry-tls-failed
proxy-entry-protocol-failed
non-target-only
xpc-helper-sent-not-main-app
wkwebview-or-electron-hidden-channel
target-request-green
```

## 输出

至少产出目标动作手册、采集窗口、代理拓扑、发送进程、脱敏样本、失败层级和下一步 Skill。

