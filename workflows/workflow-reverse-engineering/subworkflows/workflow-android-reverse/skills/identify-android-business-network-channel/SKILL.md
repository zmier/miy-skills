---
name: identify-android-business-network-channel
description: 识别经过授权的 Android 目标业务流量为什么没有出现在普通抓包中，并在系统代理、TLS/HTTP2、SocksDroid/VpnService、mPaaS/mobilegw、Nebula/XRiver、JSBridge/RPC、WebSocket/gRPC/QUIC、native socket 等通道之间选择下一步证据路线。用于 Reqable/mitmproxy 只能看到非目标流量、目标接口缺失、App 容器化小程序流量不可见、需要把“抓不到包”拆成可验证红灯时。
---

# Android 业务网络通道识别

## 目标

把“目标业务包没出现”拆成可验证的网络通道假设。该 Skill 不负责破解参数、重放接口或绕过访问控制；它只决定下一步应该回到普通抓包、走强制转发、做容器/RPC hook，还是下探到 native/协议层。

## 输入

开始前读取：

- 需求 TASK 的目标动作、UAT Green、授权边界；
- 最近一次抓包窗口和 Red 分层；
- 代理拓扑、CA、HTTP/2 开关、SocksDroid/VPN 状态；
- APK 路径、包名、版本、前台 Activity；
- 已有静态/JADX/strings/so 证据。

如果没有明确动作窗口，先返回 `capture-android-traffic` 生成人机操作手册。

## 工作流

1. 复核授权边界，只分析课堂靶场、自有 App 或明确授权目标。
2. 按 `capture-android-traffic` 的 Red 分层确认当前问题：
   - `zero-connection`：先修代理入口；
   - `proxy-entry-tls-failed`：先修证书信任或 Pinning 诊断；
   - `proxy-entry-protocol-failed`：先做 HTTP/2、HTTP/3、WebSocket、QUIC 对照；
   - `stale-window-no-new-flow`：先冷启动目标进程和页面；
   - `non-target-only`：进入本 Skill 的通道识别主流程。
3. 读取 `references/channel-taxonomy.md`，把候选分成入口层、传输/协议层、应用容器层和业务 RPC 层。
4. 做静态签名扫描。关键词和解释读取 `references/static-signature-scan.md`。
5. 将命中写成“证据强度”，不要把字符串命中直接当成已确认通道。
6. 选择下一步动态实验：
   - 普通代理可见目标 host/path：回到 `analyze-android-traffic`；
   - 普通代理只见非目标流量，但静态命中 Nebula/XRiver/bridge：优先 hook 容器桥和 RPC；
   - 普通代理完全无连接，浏览器/其他 App 可抓：用 SocksDroid/VpnService 做强制转发对照；
   - 进入代理但协议失败：做 HTTP/2 关闭、HTTP/3/QUIC/UDP、WebSocket/gRPC 对照；
   - Java 网络栈无明显命中：下探 `Socket.connect`、`SSL_write/SSL_read`、native `connect/send/recv`。
7. 读取 `references/dynamic-hook-playbook.md` 生成下一轮 hook 计划，不在没有证据时盲目 hook 全量类。
8. 对容器化小程序或统一网关，不要停在第一层 bridge 证据；按“bridge request → response callback → network exit → response model”的顺序补齐证据。
9. 若已确认业务走 RPC/统一网关/mobilegw，且外部 replay 被账号态、设备态、签名、风控 Header 阻塞，建议转入 `dispatch-via-app-runtime` 的 R4-A App 代发路线，而不是继续在普通代理里寻找不存在的业务 URL。
10. 若已确认业务走 WebSocket/TCP/gRPC stream/IM sync 等长连接，且找到 App 内发送入口或 session manager，建议转入 `dispatch-via-app-runtime` 的 R4-M App 代发消息路线。
11. 输出 `channel-identification-report.md`，并把下一步写回 TASK 的 Mermaid/ledger/log。

## 判断原则

- SocksDroid 只证明“流量是否进入代理拓扑”，不证明目标业务走哪个应用层通道。
- mPaaS/mobilegw、Nebula/XRiver、JSBridge/RPC 通常属于应用层或应用框架层，不是 OSI 网络层里的独立层。
- 看到 Nebula/XRiver/bridge 资源，优先怀疑“页面动作先进入容器桥，再转 RPC/内部网关”，而不是直接找普通 REST URL。
- 对 Alipay/小程序/RPC 场景，典型链路是：页面动作进入 XRiver/Nebula bridge，`name=rpc` 携带 `operationType/requestData`，再进入通用 RPC 栈，最终落到 `mobilegw` 统一出口。`mobilegw` 是网络出口，不等于业务 URL 已经完整暴露。
- 没有 `mobilegw` 或 `OperationType` 明文字符串，不代表不存在 RPC；可能被压缩、加密、混淆或在动态包中。
- 只有 `QUICKPAY` 这类业务名命中时，不要误判为 QUIC 协议。
- 通道识别必须产出“下一条最小实验”，不能停在“可能是某某框架”。
- `bridge-request-confirmed`、`response-confirmed`、`network-exit-confirmed` 和 `response-model-confirmed` 是递进状态。上层 bridge Green 不自动推出外部 Python 可重放。
- App 内发送入口 Green 也不自动推出 R3 可复现；如果继续借用 App 运行态，应明确标为 R4-A/R4-M，并由 `dispatch-via-app-runtime` 承载后续设计。

## 输出

至少产出：

- 当前 Red 分层；
- 已排除的代理/证书/协议问题；
- 静态签名表；
- 通道候选树；
- 推荐下一轮动态实验；
- bridge/RPC operation 或 service name；
- 响应回调或返回对象证据；
- 最终网络出口、方法、关键头和 body 骨架；
- response model 的最低结构；
- 需要人类操作的动作窗口；
- 证据链接和置信度；
- 写回 TASK 的 `NEXT`。

## 参考资料

- 解释通道分层和 SocksDroid 关系时读取 `references/channel-taxonomy.md`。
- 做 APK/JADX/strings 初筛时读取 `references/static-signature-scan.md`。
- 设计 Frida/Java/native 动态实验时读取 `references/dynamic-hook-playbook.md`。
- 定义验收与写回格式时读取 `references/uat-contract.md`。
