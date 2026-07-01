# 设备就绪等级

| 等级 | 含义 | 最低条件 |
|---|---|---|
| D0 | 未连接 | `adb devices` 没有目标设备 |
| D1 | 已发现但不可操作 | `unauthorized` 或 `offline` |
| D2 | 基础 ADB 就绪 | shell、设备信息、临时文件和包管理可用 |
| D3 | Root 分析就绪 | D2 + `su -c id` 返回 `uid=0` |
| D4 | 动态分析就绪 | D3 + Frida 客户端/服务端版本匹配且连通 |
| D5 | 请求复现实验就绪 | D4 + 目标 App、流量观察或课堂 fixture 已准备 |

等级只能根据实际检查结果提升，不能因为设备“已经刷过 Root”直接假定为 D3。

## 常见阻塞

| 状态 | 处理 |
|---|---|
| `unauthorized` | 解锁设备，确认 USB 调试授权，再重试 |
| `offline` | 重新连接 USB，重启 ADB Server，检查线材与 USB 模式 |
| 多台设备 | 使用 `--serial` 明确目标设备 |
| 找不到 `adb` | 安装 Platform Tools 或设置 SDK 路径 |
| `su` 不存在 | 记录为 D2，不自动 Root |
| Magisk 弹出授权 | 只授权明确的 `adb shell` Root 检查 |
