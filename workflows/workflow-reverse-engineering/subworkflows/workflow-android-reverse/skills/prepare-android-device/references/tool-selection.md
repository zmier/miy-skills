# 工具选择

## 本地脚本

使用 `scripts/check_device.sh` 建立可审计的设备基线。它适合首次接入、环境排错和 evaluation 留档。

## Android 设备 MCP

设备达到 D2 后，可评估 Android-MCP、mobile-mcp 或 scrcpy-mcp，用于：

- UI 状态读取；
- 点击、滑动和文本输入；
- 截图与页面层级；
- 启动应用；
- 受控 shell 与文件操作。

MCP 不替代设备基线检查。采用前必须确认：

- 是否支持指定序列号；
- shell 命令范围；
- 是否会自动操作第一台设备；
- 截图和日志是否可能包含隐私；
- 是否具有清晰许可证和活跃维护。

## Frida 准备

Frida 安装与版本匹配应由后续专用 Skill 负责。可以借鉴第三方 `setup-frida.sh`，但需先审阅下载来源、版本锁定和设备写入动作。
