# Reqable 适配说明

## 数据路径

```text
Android App
→ Android 全局代理
→ USB adb reverse（优先）或局域网（降级）
→ Reqable 代理端口
→ Reqable 会话
→ Report Server
→ reqable-mcp 本地 SQLite
→ MCP 查询工具
```

Reqable 负责代理、TLS 解密和会话查看。`reqable-mcp` 不控制 Reqable GUI，也不替代代理与证书配置；它只接收 Reqable 上报的 HAR JSON，并把数据暴露为 MCP 工具。

## Android 到 Reqable

优先使用 USB：

```bash
adb reverse tcp:9000 tcp:9000
adb shell settings put global http_proxy 127.0.0.1:9000
```

拓扑：

```text
Android 127.0.0.1:9000
→ USB adb reverse
→ macOS Reqable :9000
```

这条路径不依赖手机和 Mac 在 Wi-Fi 中互相可达，可避开校园网客户端隔离、VPN 地址变化和局域网地址切换。

局域网模式只作为降级方案：

```bash
adb shell settings put global http_proxy <Mac局域网地址>:9000
```

若手机对 Mac 地址执行 `ping` 时返回 `Destination Host Unreachable`，不要使用局域网模式。

结束抓包：

```bash
adb shell settings put global http_proxy :0
adb reverse --remove tcp:9000
```

## 固定版本与启动

项目当前固定使用：

```bash
npx -y reqable-mcp@0.3.2
```

Codex MCP 注册：

```bash
codex mcp add reqable -- npx -y reqable-mcp@0.3.2
```

仅启动接收端进行排查：

```bash
npx -y reqable-mcp@0.3.2 collector
```

健康检查：

```bash
curl -fsS http://127.0.0.1:18765/health
```

## Report Server

在 Reqable 的“添加报告服务器”中填写：

- 名称：`reqable-mcp-local`
- 匹配规则：课堂验证可先用 `*`，正式采集应收窄到目标域名
- 服务器 URL：`http://127.0.0.1:18765/report`
- 压缩：无，或确保与接收端兼容

保存后产生少量测试流量，再检查接收计数。接收端离线期间的失败推送不会自动重试。

## 数据与隐私

- 默认数据库：`~/Library/Application Support/reqable-mcp/requests.db`
- 默认单条 body 最多保存 `102400` 字节
- 默认数据保留 `7` 天
- 实时推送漏采时从 Reqable 导出 HAR，再使用 MCP 的 `import_har`
- 不把真实 HAR、Cookie、Token 或个人数据提交到 Git

## 能力边界

`reqable-mcp` 可查询请求、域名、API 结构和 WebSocket 数据，也能从已抓请求生成示例代码。生成代码只是请求形态草稿，不能代替签名算法验证、动态字段解释或授权检查。
