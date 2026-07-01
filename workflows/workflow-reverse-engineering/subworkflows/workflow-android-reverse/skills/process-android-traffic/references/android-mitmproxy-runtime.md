# Android mitmproxy 运行时

## 自动化边界

ADB 可以自动完成：

- 检查唯一在线设备；
- 建立 USB `adb reverse`；
- 设置和恢复 Android 全局代理；
- 在 Root/Magisk 设备上部署或移除 systemless CA；
- 启动 Frida Server，为后续应用信任诊断准备运行时。

ADB 不能仅凭“设备已 Root”自动消除 App 自身的证书绑定。浏览器可解密而
特定 App 失败时，应先保存 TLS 失败证据，再路由到动态 Hook、应用补丁或
自定义网络栈分析。

## 生命周期

```bash
make mitm-start MITM_TARGET_HOST=example.com MITM_TARGET_PATH=/
make mitm-status
make mitm-stop
```

会话启动前保存手机原代理；停止时恢复原代理和对应 USB reverse。Reqable
使用 `9000`，mitmproxy 使用 `9080`，两个后端不得同时占用手机全局代理。

### TASK 产物与 confdir

`MITM_RUNTIME_DIR` 同时决定 mitmproxy 的 `confdir`、CA 证书位置、状态文件和
默认输出目录。不要为了把事件文件写进某个课程 TASK 而随意覆盖
`MITM_RUNTIME_DIR`；否则 mitmproxy 会在新目录生成一套新 CA，手机系统里已
信任的旧 CA 不会匹配，日志会出现类似：

```text
Client TLS handshake failed. The client does not trust the proxy's certificate
```

推荐做法：

```bash
make mitm-start \
  MITM_EVENT_FILE=/absolute/task/outputs/events.jsonl \
  MITM_LOG_FILE=/absolute/task/outputs/mitmdump.log \
  MITM_TARGET_HOST=example.com \
  MITM_TARGET_PATH=/
```

也就是复用默认 `MITM_RUNTIME_DIR`/`confdir`，只覆盖 `MITM_EVENT_FILE` 和
`MITM_LOG_FILE`。只有明确要换一套 CA 并准备重新安装、重启手机时，才覆盖
`MITM_RUNTIME_DIR`。

### HTTP/2 对照实验

如果日志中大量出现类似：

```text
HTTP/2 protocol error: Received header value surrounded by whitespace b'Bearer '
```

说明请求已经进入代理，但 mitmproxy 在 HTTP/2 层因为头部规范问题拒绝了解析。
此时不要把它归为 `zero-connection`。可以启动一轮 HTTP/2 关闭的对照实验：

```bash
MITM_HTTP2=false make mitm-start \
  MITM_EVENT_FILE=/absolute/task/outputs/events-h1.jsonl \
  MITM_LOG_FILE=/absolute/task/outputs/mitmdump-h1.log
```

若关闭 HTTP/2 后同一动作窗口出现更多明文请求，则把 `MITM_HTTP2=false` 记录为
该案例的 G2 实验变量；若仍失败，再转向应用自定义网络栈、证书绑定或请求头构造
问题。

## CA

```bash
make mitm-ca-status
make mitm-ca-install
make mitm-ca-remove
```

安装和移除 Magisk 模块后均需重启。CA 与私钥保存在：

```text
~/Library/Application Support/workflow-android-reverse/mitmproxy/config
```

不得提交到课程知识库或 Git 仓库。

如果 `make mitm-ca-status` 显示 `system_store=loaded`，但 mitmproxy 仍报设备
不信任证书，优先检查本次运行的 `confdir` 是否就是上面这个默认目录。

## 数据保留

- 默认不保存 `.mitm` 原始流；
- 目标 host/path 必须尽量收窄；
- JSONL 只保存字段名、长度、哈希、状态码和最小路由信息；
- 只有 TASK 明确要求本地短期回放时，才设置 `MITM_SAVE_FLOWS=1`；
- 完成实验后检查日志中不存在 Cookie、Token、账号或完整设备标识。

## Addon 过滤

正向代理下，mitmproxy 有时会以 absolute-form 保存明文 HTTP 请求路径，例如：

```text
http://example.com/generate_204
```

通用 addon 过滤 path 前必须先归一化为：

```text
/generate_204
```

否则 `MITM_TARGET_PATH=/` 这样的首次探索窗口会误过滤掉基础连通性请求。
