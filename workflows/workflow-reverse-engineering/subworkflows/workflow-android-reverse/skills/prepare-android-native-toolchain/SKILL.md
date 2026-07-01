---
name: prepare-android-native-toolchain
description: "检查并准备经过授权的 Android JNI/Native 逆向环境，识别主机架构、Rosetta、Android SDK/NDK、ELF 命令行工具、IDA/Ghidra 安装与 MCP 接入条件。用于请求构造链从 Java 进入 native 方法、排查分析器在 Apple Silicon 或当前系统上的兼容性，或在总编排进入 JNI 映射前建立 Smoke-Native 基线。不得自动安装来源或授权不明的商业软件，不得绕过签名、许可或系统安全机制。"
---

# Android 原生逆向环境准备

## 目标

在分析 `.so` 前先回答三个问题：

1. 当前主机是否具备读取、编译和检查 Android Native 文件的基础能力；
2. 候选 GUI 工具是否已安装、架构兼容、获得合法授权并能够打开目标 `.so`；
3. JNI 映射、Native 静态分析和运行时 Hook 分别由什么工具承担。

本 Skill 只建立环境和证据，不代替 `map-android-jni` 或 `hook-android-native` 的算法分析。

## 工作流

1. 确认目标属于自有应用、明确授权目标或合法教学环境。
2. 运行 `scripts/check_native_toolchain.sh <报告路径>`。
3. 阅读 `references/readiness-levels.md`，把结果写入总 TASK 的 Smoke-Native。
4. 若发现旧版分析器，先核验版本、CPU 架构、签名、系统兼容性和许可证，再决定是否安装。
5. IDA MCP 只作为可选适配器；GUI、batch、IDAPython 与 MCP 分别验证，不能互相替代状态。
6. 工具通过后，向总编排返回可用命令、应用路径、限制和下一项最小实验。

## 安装规则

- NDK 优先使用 Android SDK 已安装版本，不用来源不明的旧头文件覆盖 SDK。
- `jni-include` 只用于阅读 JNI 类型和函数表，不作为 Android NDK 的替代品。
- 商业软件必须由用户拥有合法许可证；来源或授权不明时只做只读清点。
- 未签名旧应用不得自动移除隔离属性、临时签名或修改 Gatekeeper。
- 不把 1GB 软件包、IDE 缓存、Gradle 构建目录或反编译数据库提交到 Skill。
- Miku 只添加已经通过本机启动 Smoke 的工具入口。

## 编排交接

由 `android-request-reproduction` 调用时：

- 接收 Mermaid 中 Smoke-Native 红灯、目标 ABI、目标 `.so` 和预期工具证据；
- 把环境缺失与算法未知严格分开；
- 工具准备完成后更新 Smoke、能力注册表和 ReAct 日志；
- Java 已进入 `native` 但映射未知时交给 `map-android-jni`；
- 映射已知但需要真实参数、返回值或加载地址时交给 `hook-android-native`；
- 映射已知且需要入口、伪代码、xref 或 Hook 候选时交给 `analyze-android-native-static`；
- 不因安装了 IDA 就把 JNI 映射或 Native 算法标为完成。

## 完成标准

- A：主机基础工具、NDK、目标 ABI 检查和至少一个 Native 分析器均通过 Smoke；工具路径与版本可复现。
- B：命令行与 NDK 就绪，课程源码可提取，但 GUI 分析器或 MCP 尚未验证。
- C：已明确阻塞在许可证、CPU 架构、系统兼容、缺少目标 `.so` 或插件运行时中的某一层。

## 参考资料

- IDA 安装与 MCP 的分级门槛，见 `references/ida-readiness.md`。
- Smoke-Native 等级，见 `references/readiness-levels.md`。
