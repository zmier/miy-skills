# HTTPS MITM 诊断

用于代理入口已经建立，但页面空白、App 报网络异常、代理只有 CONNECT、日志出现 TLS/证书错误，或系统网络验证变成 `PARTIAL_CONNECTIVITY` 的场景。

## 首差分层

| 现象 | 首差层 | 下一步 |
|---|---|---|
| `Trust anchor for certification path not found` | CA 未被系统或 App 信任 | 先确认 Reqable/mitmproxy CA 是否进入系统信任锚，再看 App 网络配置 |
| 浏览器 HTTPS 可抓，目标 App HTTPS 失败 | App 信任策略或 Pinning 候选 | 读取 APK `network_security_config`，再转动态 TrustManager/Pinning 诊断 |
| 只有 CONNECT，无 HTTP 明文 | TLS 解密未成功 | 对比浏览器、系统探针、目标 App 三个窗口 |
| 强制转发后仍无明文 | 入口已恢复，TLS 层失败 | 不回滚 SocksDroid Green，另开 TLS/Pinning TASK |
| 服务端要求客户端证书或出现双向认证迹象 | mTLS 候选 | 在授权范围内考虑客户端证书导出，证据只保留本地 |
| HTTP 探针成功，HTTPS 探针失败 | CA/TLS 问题，不是底层断网 | 保留 `NetworkMonitor` 证据 |
| 目标接口 HTTP `403/406/418` | 服务端拒绝或风控 | 转总编排的 G2 拒绝分层，不继续归因代理 |
| 目标使用 Cronet/libsscronet 且 Pinning/OLLVM 痕迹明显 | Cronet/native TLS 栈或 native pinning 候选 | 仍按 Android 当前样本取证；看雪第14章课时5-6只作方法论弱参考 |

## 最小对照

1. 关闭代理，确认手机默认网络和目标 App 基线是否可用。
2. 开启代理但不解密目标 host，确认 CONNECT 能否通过。
3. 开启 HTTPS 解密，分别测试浏览器 HTTPS、系统网络验证日志和目标 App。
4. 若浏览器 Green、目标 App Red，读取 Manifest 与 `network_security_config`。
5. 若 App 不信任用户 CA，优先选择系统 CA、Magisk systemless CA 或测试包网络配置；不要一上来宣称 Pinning。
6. 若系统 CA 仍失败，再进入 Pinning/TrustManager/OkHttp/WebView/Cronet/mTLS 证据链。
7. 需要动态实验时，复制 `assets/upstream-ssl-objection/` 到 TASK；先记录脚本类型、目标窗口和副作用，再运行。
8. 若是 Cronet/libsscronet/OLLVM pinning，课程中的 iOS libsscronet 案例只能作为方法论参考；Android 样本的模块、符号、调用链和证据必须重新建立。

## 证据

每次诊断至少落盘：

- 当前代理：全局代理、`adb reverse`、VPN 状态、监听端口；
- 系统网络验证：`dumpsys connectivity` 中 `VALIDATED/PARTIAL_CONNECTIVITY`；
- 日志原文：`SSLHandshakeException`、`CertPathValidatorException`、`Trust anchor`、`Pinning` 等；
- APK 网络配置：`network_security_config` 和 debug/base config；
- 对照结果：无代理、代理不解密、代理解密、强制转发。

## 交接

- 入口未通：返回 `capture-android-traffic` 继续修代理拓扑。
- 入口已通但 TLS 不明文：记录为 `tls-mitm-red`。
- 已证实 App 信任策略或 Pinning：转 `trace-android-java` 或专门 Pinning TASK。
- 使用 upstream SSL assets 后若明文恢复：只标记抓包观察链 Green，目标接口仍交给 `analyze-android-traffic`。
- 目标接口已经明文可见但业务失败：转 `android-request-reproduction` 的 G2 拒绝分层。
