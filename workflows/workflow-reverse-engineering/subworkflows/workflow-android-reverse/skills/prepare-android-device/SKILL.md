---
name: prepare-android-device
description: 检查并准备经过授权的 Android 实验设备，建立可供后续抓包、Frida、JNI/Native 分析和课堂案例复现使用的设备能力基线。用于定位 adb、确认 USB 调试授权、采集设备型号、Android/API/ABI、SELinux、Root 与 Magisk 状态，验证 /data/local/tmp 文件操作和包管理能力，并生成结构化设备报告。默认只执行只读检查和可清理的临时文件测试；不得自动刷机、修改系统分区、安装 Magisk 模块或改变安全配置。
---

# Android 实验设备准备

## 目标

在动态分析前建立稳定、可重复的设备连接，并向总编排 Skill 输出设备能力报告。

## 执行流程

1. 确认设备属于用户并用于授权测试或课堂复现。
2. 定位 `adb`；优先使用 `ANDROID_SDK_ROOT`、`ANDROID_HOME` 和标准 SDK 路径。
3. 运行 `adb devices -l`，区分 `device`、`unauthorized`、`offline` 和无设备。
4. 设备未授权时，提示用户在设备上确认 USB 调试，不继续执行 shell。
5. 设备可用后运行 `scripts/check_device.sh`。
6. 阅读报告，按 `references/readiness-levels.md` 判断当前就绪等级。
7. 将报告路径和阻塞项交回 `android-request-reproduction`。

## 编排交接

由总编排调用时：

- 接收 Mermaid 中对应的 Smoke 红灯、Green 条件和预期证据；
- 只检查本轮实验需要的设备能力，不扩大环境改动；
- 将结果写回 Smoke 测试记录；
- 通过时把节点标为 `passed`，失败时记录具体阻塞层；
- 交回后由总编排重新计算唯一 `NEXT`，本 Skill 不自行推进算法分析。

## 操作分级

| 等级 | 类型 | 默认策略 |
|---|---|---|
| L0 | 读取设备、系统和连接信息 | 可直接执行 |
| L1 | 创建并删除临时文件、读取包列表 | 可直接执行并清理 |
| L2 | `su`、启动服务、推送分析二进制 | 明确目标后执行 |
| L3 | 刷机、修改系统分区、安装模块、安全配置变更 | 不自动执行 |

Root 已存在不等于默认使用 Root。普通 ADB 足够时不要升级权限。

## 完成标准

基础设备准备完成需要：

- ADB 状态为 `device`；
- 能读取型号、Android 版本、API 和 ABI；
- 普通 shell 可执行；
- `/data/local/tmp` 临时文件测试成功；
- 包管理命令可用；
- Root/Magisk 状态已经明确记录。

Frida、代理与证书属于后续能力，不是本 Skill 基础通过的必要条件。

## 输出

生成 Markdown 设备报告，至少包含：

- 主机端 ADB 路径与版本；
- 设备序列号、型号、Android/API/ABI；
- 启动验证状态、SELinux 与 shell 身份；
- Root 与 Magisk 版本；
- 临时目录和包管理测试；
- 就绪等级、阻塞项和下一步。

不得在报告中保存私人账号、应用数据、密钥或设备中的真实凭据。
