---
name: process-android-traffic
description: 在经过授权的 Android 流量研究中使用 mitmproxy/mitmdump 脚本按目标 URL 观察、脱敏保存、标注或受控修改 HTTP 请求与响应，并为请求候选、字段归约和 G2 差异分析提供可重复的机器处理层。用于 GUI 抓包不足以批量结构化同一低频会话、需要自动提取字段或验证单变量修改的场景。不得用于代理池轮换、高频采集、隐藏来源或扩大授权范围。
---

# Android 流量脚本处理

## 目标

把流量处理写成窄作用域、可回放的 addon，而不是通用全流量篡改器。

## 工作流

1. 接收目标 host/path、允许动作、数据保留规则和 Green 条件。
2. 先以只读 observer 模式运行。
3. 使用 `scripts/mitmproxy-session.sh` 管理 mitmdump、USB reverse、代理切换和恢复。
4. 使用 `scripts/manage_android_ca.sh` 检查或部署 Magisk systemless CA；部署后需要重启。启动 mitmproxy 时必须复用已安装 CA 对应的 `confdir`，不要为了把产物放进 TASK 而覆盖 `MITM_RUNTIME_DIR` 生成另一套 CA。
5. 通用采集使用 `scripts/target_capture_addon.py`；特殊实验再从 `assets/mitm-addon-template.py` 创建 TASK 专用脚本。
6. 精确过滤 host、path、method 和时间窗口。首次探索允许 `host/path` 放宽，但 addon 必须兼容正向代理 absolute-form URL，例如 `http://example.com/a` 应归一化为 `/a` 后再过滤。
7. 默认只输出 header/query 字段名、长度和哈希，不输出字段值。
8. 需要修改时每次只改变一个变量，并保存 before/after manifest。
9. HTTPS 前先验证证书与代理链；证书问题返回设备/抓包 Skill。
10. 若系统 CA 已加载但特定 App 持续 TLS 失败，先确认当前 mitmproxy `confdir` 与已安装到系统信任库的 CA 是同一套；确认一致后仍失败，才记录为应用信任或 Pinning 候选，路由到 `diagnose-android-instrumentation`。ADB 本身不是 Pinning 绕过器。
11. 代理上游、连接策略或 TLS 行为会改变 G2 环境时，必须作为实验变量记录。
12. 若 mitmproxy 日志反复出现 HTTP/2 协议错误，例如请求头值不符合 HTTP/2 规范，可用 `MITM_HTTP2=false` 启动一轮对照实验，观察是否能降级到 HTTP/1.1 并进入 addon 事件文件。
13. 保存 addon 版本、mitmproxy 版本、启动命令和会话证据。
14. 完成后返回流量分析、参数归约或 G2 首差节点。

## Green 条件

- 只命中目标流量；
- 已确认 mitmproxy 运行时 `confdir` 与设备信任的 CA 一致；
- 观察或修改结果可重复；
- 没有敏感值泄漏到日志；
- 单变量差异与响应证据成对保存；
- 停止后网络环境可恢复。

## 边界

- 免费代理池与 IP 轮换不进入本 Workflow 默认能力。
- 上游代理仅可作为明确授权的网络路径实验，不用于规避限制。
- 已在 Pixel 4 XL / Android 11 上通过 USB reverse、Magisk systemless CA、Chrome HTTPS 和目标 App 启动流量评测。

## 参考资料

- 编写 addon 前读取 `references/addon-contract.md`。
- 配置 Android、USB reverse、systemless CA 与停止恢复时读取 `references/android-mitmproxy-runtime.md`。
- 使用 `assets/mitm-addon-template.py`。
