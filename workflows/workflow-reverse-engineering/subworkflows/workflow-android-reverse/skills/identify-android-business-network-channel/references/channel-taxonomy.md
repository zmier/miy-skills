# 通道分层速查

## 四层分类

1. 入口层：系统代理、USB reverse、局域网代理、SocksDroid/VpnService。
2. 传输/协议层：TLS、HTTP/2、HTTP/3、QUIC、WebSocket、gRPC、长连接、UDP。
3. 应用容器层：WebView、Nebula、XRiver、H5 容器、JSBridge、V8 bridge。
4. 业务 RPC 层：mPaaS/mobilegw、OperationType、RpcService、H5Rpc、业务内部网关。

## 与 OSI 的关系

- SocksDroid/VpnService 更接近网络入口/路由改造，用于让流量进入代理。
- TLS/HTTP2/QUIC 属于传输层之上的协议栈问题。
- Nebula/XRiver/JSBridge/RPC 是应用层框架。它们决定“业务动作如何被封装成请求”，不等同于底层网络链路。

## 决策要点

- 普通代理有非目标 HTTPS 明文：代理和 CA 不应被判为全局失败。
- 普通代理只有非目标流量：优先判断目标业务是否走容器/RPC/长连接。
- 浏览器或其他 App 能抓、目标 App 完全无连接：用 SocksDroid/VpnService 验证是否忽略系统代理。
- SocksDroid 后出现连接但无明文：转 TLS/Pinning/证书信任诊断。
- SocksDroid 后仍无目标业务：继续检查动作窗口、UDP/QUIC、native socket、VPN 检测和容器离线缓存。
