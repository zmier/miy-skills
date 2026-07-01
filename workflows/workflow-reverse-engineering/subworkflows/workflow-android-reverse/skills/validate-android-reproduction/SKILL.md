---
name: validate-android-reproduction
description: 验证 Android 逆向复现结果并设计 CLI/Jar/Python 交付形态。用于 Unidbg、Frida RPC、Python 算法或宿主 App 已能产生结果后，需要区分 Unit/G1/G2/UAT、保存输出证据、处理 java -jar 参数传递、Python subprocess 调用、raw/summary 输出和迁移验收时使用。
---

# Validate Android Reproduction

## 验证层级

- `Unit`：固定输入下单个函数输出稳定；
- `G1`：离线复现值与同一 fixture 的 App/课程输出一致；
- `G2`：完整请求或运行态调用通过业务接口；
- `UAT`：用户目标可操作、可复跑、可迁移，且边界清晰。

不要用 G1 代替 G2；遇到风控、TFS、状态绑定或服务端限制时，保持算法 Green，另开运行态归因。

## 阶段性验证

`partial-validated` 用于表达“已经跑通核心链路，但还不能外推到更强目标”：

- Unidbg 已能离线调用目标 JNI/native 方法；
- 输出形态、结构、长度或固定 fixture 对照成立；
- 但真实设备态、账号态、时间/随机数、`/proc`、TEE、服务端 G2 或 UAT 尚未验证。

写结论时必须拆成两句：

```text
已验证：<当前 fixture/运行环境下的可重复证据>
未验证：<真实设备态、真实请求、端到端业务效果等边界>
```

## Unidbg 交付规则

1. Java wrapper 的 `main(String[] args)` 支持命令行传参；
2. 参数含 `&`、空格或 JSON 时，调用方必须整体加引号；
3. Python 只能向 Java 传字符串，复杂结构用 JSON 字符串、文件路径或 stdin；
4. Jar 不自动包含 APK/so，交付包必须声明 `apks/` 相对路径；
5. 如果使用 `java -jar`，manifest 需要 `Main-Class` 和依赖 `Class-Path`；否则用 `java -cp` 更透明；
6. Python `subprocess` 默认取最后一行作为业务结果，完整 stdout/stderr 可另存 raw。
7. Python 调用模板可从 `assets/unidbg_subprocess_client.py` 复制到 TASK，再按当前 Java classpath、工作目录和输入参数调整。

## 输出纪律

- TASK 内保存 raw 输出；
- 对用户默认显示摘要；
- 若输出含真实账号、token、头像 URL 或用户资料，默认脱敏；
- 提供显式参数才保存完整 raw。

对安全 SDK、token、签名或风控字段，默认摘要只保存：

- 输出长度；
- 前缀或 hash 摘要；
- 结构判断，例如 base64-like、JSON、hex；
- 固定 fixture 是否稳定；
- 原始 raw 的 TASK 路径。

## 完成标准

- 可重复命令写入 TASK Makefile 或脚本；
- 记录 Java/Jar/Python 三层入参与出参；
- 记录失败时的首个差异层：参数、包装、补环境、so 初始化、业务请求、服务端状态；
- 交付物不依赖当前对话上下文。

## 迁移状态

- 已覆盖 Java wrapper、Jar/classpath、Python subprocess、raw/summary 输出和 `partial-validated` 结论边界。
- 具体案例输出值、命令和资源路径保留在 TASK 与能力注册表，不写入通用 Skill 主体。
