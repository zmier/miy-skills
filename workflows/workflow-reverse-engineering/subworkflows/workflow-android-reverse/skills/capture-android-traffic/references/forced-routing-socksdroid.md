# SocksDroid 强制转发

## 适用红灯

先建立以下对照：

1. 浏览器通过同一代理能够抓包；
2. 目标 App 能正常联网；
3. 目标 App 执行动作时，代理端没有 CONNECT、TLS 握手或目标连接；
4. Android 全局代理已正确设置。

四项同时成立时，优先怀疑 App 忽略系统 HTTP 代理、使用直连 Socket、
自定义 `ProxySelector` 或独立网络栈。此时使用 VPN/tun2socks 强制转发，
而不是直接进入 SSL Pinning。

若普通代理在同一动作窗口已经出现目标连接，则 Red 不成立，不应仅因课程、
历史版本或经验描述而强制切换 SocksDroid。记录“当前环境未复现”同样是有效
实验结论。

## 拓扑

```text
目标 App TCP
→ Android VpnService
→ SocksDroid tun2socks
→ 127.0.0.1:9081
→ adb reverse tcp:9081 tcp:9081
→ mitmproxy --mode socks5
→ 脱敏 addon
```

SocksDroid 使用 `VpnService` 和 `tun2socks` 将应用 TCP 流量送入 SOCKS5。
它解决“流量未进入代理”，不负责让目标 App 信任 mitmproxy CA。

## 执行

```bash
SOCKSDROID_APK=/absolute/path/SocksDroid.apk \
  scripts/socksdroid_capture.sh install

TARGET_PACKAGE=com.example.app \
MITM_TARGET_HOST=api.example.com \
  scripts/socksdroid_capture.sh start

scripts/socksdroid_capture.sh status
scripts/socksdroid_capture.sh stop
```

Root 设备上脚本会写入 SocksDroid 配置、尝试授权 `ACTIVATE_VPN` 并启动
服务。Android 首次 VPN 同意属于系统安全关口；若仍弹出，只允许人类确认
一次，不使用坐标点击脚本伪装同意。

## 诊断阶梯

| 观察 | 结论与下一步 |
|---|---|
| SOCKS5 无连接 | VPN 未建立、应用被排除、UDP/QUIC 或流量窗口错误 |
| 有 TCP 连接但无 TLS 明文 | 检查系统 CA、应用信任策略和 Pinning |
| TCP 路线可见，目标动作仍走 UDP | 记录 QUIC/HTTP3 候选；先做禁用或降级实验 |
| App 检测 VPN 后拒绝联网 | 把 VPN 检测作为独立环境红灯，转动态诊断 |
| 已见目标 HTTPS 请求 | 返回候选接口分析，不继续扩大采集范围 |

## 边界

- 同一时刻 Android 只能有一个用户 VPN；
- 默认仅路由目标包；没有目标包时才允许全应用短时 Smoke；
- 首次 VPN 系统授权需要人类确认一次，后续可由脚本重复启动；
- SocksDroid 不替代 CA、Pinning、QUIC 或 App 内代理检测的诊断；
- 结束后必须停止 VpnService、移除 reverse 并恢复原代理。

## 已验证边界

在 Pixel 4 XL / Android 11、拼多多 v6.32.0 上，SocksDroid 路线已取得
可解密 HTTPS 与 200 响应；但普通全局代理在同一环境也可抓取冷启动流量，
所以这次验证证明的是“备用拓扑可工作”，不是“反代理 Red 已复现并修复”。
