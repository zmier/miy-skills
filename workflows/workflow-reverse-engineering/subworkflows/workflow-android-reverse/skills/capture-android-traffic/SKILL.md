---
name: capture-android-traffic
description: 根据经过授权的 Android 分析目标设计人机协作抓包实验，生成操作手册，并在 Reqable GUI、mitmproxy 自动化和 SocksDroid/VpnService 强制转发路线之间选择，配置设备代理、HTTPS 前置条件、USB ADB reverse、证据输出和停止恢复。用于把业务目标转为最小行为窗口，排查 App 忽略系统代理、直连 Socket、QUIC、证书信任或 Report Server 等“抓不到包”问题。不得用于未授权监听、凭据窃取或扩大采集范围。
---

# Android 流量抓取

## 目标

把分析目标转换成“人类可以无歧义执行、机器可以准确分析”的行为窗口，再把设备请求转换成可验证、可检索、可交接的证据。该 Skill 不负责确认接口因果关系、解释签名算法或绕过应用访问控制。

## 工作流

1. 确认目标是课堂靶场、自有应用或明确授权测试，并读取 TASK 中的目标行为、可观察结果与边界。
2. 把目标拆成基线、页面进入、目标动作等最小窗口；无法拆分时说明限制并设计重复窗口。
3. 按 `references/human-capture-manual.md` 生成 `human-operation-manual.md`，写清人类步骤、机器观察、成功信号、失败处理和恢复动作。
4. 在人类确认可以执行前，不开始正式采集。
5. 根据阶段选后端：首次探索和人工重放优先 Reqable；目标已收敛、需要可重复采集或单变量实验时优先 mitmproxy；浏览器可抓而 App 完全不进入代理时，读取 `references/forced-routing-socksdroid.md`。
6. Reqable 路线运行 `scripts/check_capture_readiness.sh <输出文件>`；mitmproxy 路线交给 `process-android-traffic`；强制转发路线使用 `scripts/socksdroid_capture.sh`。
7. 确认代理端口。Reqable 默认 `9000`，mitmproxy 默认 `9080`，但必须以实际监听结果为准。
8. USB ADB 在线时优先使用 USB reverse；只有无法使用 USB 时才走局域网。
9. Reqable 路线按 `references/reqable-adapter.md` 配置证书和 Report Server。
10. 代理后端、端口、CA `confdir`、HTTP/2 开关或 SocksDroid/VPN 路由发生变化后，优先设计一次“冷启动动作窗口”：让目标 App/WebView 进程在新代理已稳定后重新进入目标页面，避免旧连接、旧代理配置或页面缓存污染实验。
11. 由人类严格按手册触发动作；机器同步记录每个窗口。
12. 按 `references/evidence-contract.md` 输出证据并交给 `analyze-android-traffic`。
13. 停止采集后必须验证恢复：Android 全局代理、`adb reverse`、用户 VPN、mitmproxy/Reqable 监听和本轮临时端口。
14. 代理入口已通但首页空白、HTTPS 明文失败、日志出现 `Trust anchor for certification path not found` 或 `SSLHandshakeException` 时，读取 `references/https-mitm-diagnosis.md`。
15. 如果 App 业务 UI 正常、代理中也有流量，但目标业务 host/path、operation 或响应实体始终缺失，标记 `non-target-only`，把证据交给 `identify-android-business-network-channel`；不要继续把它当成代理端口、证书或 HTTP/2 的普通故障。
16. 已有证据指向 App 信任策略、Pinning、WebView SSL、Cronet 或 mTLS 时，才从 `assets/upstream-ssl-objection/` 复制 upstream 脚本到 TASK 做授权动态实验；使用脚本前必须记录目标窗口、脚本类型、预期 Green 和副作用。

## 抓包 Red 分层

不要把所有“业务没跑通”都写成“抓不到包”。按同一动作窗口逐层分类：

1. `zero-connection`：代理端完全没有目标 App 连接；
2. `proxy-entry-tls-failed`：代理端有连接，但 TLS 握手失败或只有 CONNECT；先检查 CA、confdir 和应用信任策略；
3. `proxy-entry-protocol-failed`：代理端有连接，但在 HTTP/2、HTTP/3、WebSocket 或自定义协议解析层失败；
4. `stale-window-no-new-flow`：代理配置正确、目标页面在前台，但当前动作窗口没有新连接；优先冷启动目标进程或改变动作窗口；
5. `non-target-only`：只有统计、静态、日志、统一网关底层流量或无关 host，没有目标业务 host/path、operation、bridge method 或响应实体；
6. `target-observed-no-business-ui`：目标 host/path 出现，但 UI 没有形成业务结果；
7. `target-request-non-2xx`：目标请求出现且明文可见，但服务端返回 `4xx/5xx`；
8. `target-request-2xx-business-failed`：HTTP `2xx`，但业务码或 UI 失败；
9. `target-request-green`：目标请求、响应与 UI/UAT 均满足契约。

只有第 1 类才可称为“完全没进代理”。第 2-8 类应回写到请求构造台账或接口复现 TASK，避免把服务端风控、字段构造、UI 操作误差误诊为代理问题。

`non-target-only` 的判断要特别保守：Reqable/mitmproxy 能看到普通 HTTP/TLS，不代表能直接看到容器桥、统一网关、长连接、QUIC/UDP、native socket 或自定义 RPC 的业务语义。只要目标页面能显示、动作能产生业务结果，而代理窗口里只有非目标流量，就优先转入业务网络通道识别。

## 编排交接

由总编排调用时：

- 接收 Mermaid 中“目标接口尚未确认”或“采集证据不足”的红灯；
- 在操作手册中写明 Green 条件、采集窗口和预期证据；
- 将代理与采集 readiness 写入 Smoke 测试；
- 采集完成后更新对应 TASK、测试矩阵和证据链接；
- 不自行把候选请求标为目标接口；由总编排重新计算 `NEXT`。

## HTTPS 判断

按以下决策树定位问题：

1. 完全没有连接：检查设备代理、`adb reverse --list`、Reqable 是否监听。局域网模式还要检查同网段、防火墙和 Wi-Fi 客户端隔离。
2. 有 CONNECT 或 mitmproxy `client connect` 但无明文：检查 CA 是否安装、当前 mitmproxy `confdir` 是否与已安装 CA 一致、是否被 Android 或目标 App 信任。
3. 浏览器可抓而目标 App 在代理端完全没有连接：先验证 App 是否忽略全局代理、直连或走 UDP/QUIC；以 SocksDroid/VpnService 强制转发做单变量实验。
4. 强制转发后有连接但无明文：记录为应用信任策略或证书绑定候选，不得直接宣称“已确认 SSL Pinning”。
5. 强制转发后目标动作仍无连接：检查 SocksDroid VPN 是否真实建立、目标包是否在 per-app 列表、动作窗口是否正确、目标是否走 UDP/QUIC 或检测 VPN。
6. 普通代理在同一动作窗口已经有目标连接：Red 未复现，记录 `not-reproduced`；可继续验证备用路径，但结论写成 `passed-with-scope`。
7. 普通代理有流量但目标业务接口没有 Green：记录为 `non-target-only`、`target-observed-no-business-ui` 或 `target-request-non-2xx`，再决定是否用 SocksDroid 做强制转发对照。
8. 强制转发后目标接口出现但返回 `406/403` 等业务拒绝：抓包入口已恢复，后续转接口构造、前置接口、设备态或风控诊断，不继续把它当代理故障。
9. Reqable 中有流量但 MCP 中没有：检查 Report Server、`/health`、上报规则和采集时间窗口。

如果同一冷启动窗口中反复出现 `non-target-only`，下一步不是继续扩大抓包范围，而是形成一份通道识别输入：目标动作、UI 结果、可见 host、缺失的业务实体、是否出现统一网关、是否出现 WebView/小程序容器痕迹，以及已排除的代理/证书/协议问题。

当手机能通过 ADB 操作，但访问 Mac 局域网地址返回 `Destination Host Unreachable` 时，说明 USB 控制链路正常而 Wi-Fi 数据链路被隔离。切换到 USB 反向代理，不要继续排查证书。

涉及系统证书、目标 App 补丁或运行时绕过时，先保留失败证据，再路由到后续诊断 Skill。

使用 SSL/Objection upstream assets 恢复明文，只表示抓包观察链 Green；目标接口确认、参数归约和请求复现仍由后续 Skill 负责。

## 输出

至少产出：

- 与目标对应的《人类抓包操作手册》；
- 授权范围、设备序列号、目标包名与采集时间窗口；
- 抓包拓扑和实际代理地址；
- readiness 报告；
- Reqable 会话筛选条件；
- MCP 接收状态或 HAR 文件位置；
- 一个经过脱敏的目标请求样本；
- 当前失败层级、置信度和下一步。
- 停止后的恢复状态，包括代理、reverse、VPN 和监听端口。

若总编排 Skill 提供了需求 TASK 工作区，则同时：

- 更新采集阶段的 `capture-index.md`；
- 把 `human-operation-manual.md` 放入采集阶段目录；
- 把可共享样本写入 `evidence/sanitized/`；
- 把环境变化、失败尝试和恢复动作追加到 `logs/LOG.md`；
- 不在该子 Skill 中替代候选接口分析或目标接口结论。

不得提交含真实 Cookie、Token、账号、个人数据或完整敏感响应体的 HAR。共享前先脱敏；原始文件只保留在本地受控目录。

## 完成标准

- A：目标请求同时出现在 Reqable 与 `reqable-mcp` 中，关键方法、URL、头部和请求体结构可核对。
- B：目标请求已在 Reqable 中确认，但 Report Server 暂未同步；已通过 HAR 成功补录到 MCP。
- C：尚未得到目标请求，但已用可重复证据定位到代理、证书、应用信任策略或 MCP 上报中的具体阻塞层。
- D：mitmproxy 路线在精确 host/path 过滤下得到成对的脱敏请求与响应记录，且停止后恢复原代理和 USB reverse。
- E：目标 App 忽略系统代理时，经 SocksDroid/VpnService 强制转发后连接进入 SOCKS5 代理；后续 TLS、QUIC 或 VPN 检测红灯被单独分类。

没有目标化操作手册，或仅看到 Reqable 启动、设备联网，不算完成。

## 参考资料

- 配置 Reqable 与 MCP 时读取 `references/reqable-adapter.md`。
- 浏览器可抓、目标 App 却完全不进入代理时读取 `references/forced-routing-socksdroid.md`。
- 代理入口已通但 HTTPS、证书、Pinning 或首页空白时读取 `references/https-mitm-diagnosis.md`。
- 需要授权 SSL/Pinning/mTLS 动态实验时，从 `assets/upstream-ssl-objection/` 复制 upstream 脚本到 TASK。
- 根据目标设计实验和生成操作手册时读取 `references/human-capture-manual.md`。
- 创建任务产物或交接样本时读取 `references/evidence-contract.md`。
