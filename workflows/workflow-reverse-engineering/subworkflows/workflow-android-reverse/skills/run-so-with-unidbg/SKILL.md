---
name: run-so-with-unidbg
description: 使用 Unidbg 加载 Android APK/so 并主动调用 JNI 方法。用于已知 JNI 类名、方法签名和输入参数，需要选择 32/64 位 emulator、设置 AndroidResolver、加载 so、callJNI_OnLoad、包装 String/byte[]/Map 等参数并取得返回值的授权逆向任务。
---

# Run SO With Unidbg

## 输入

- 目标 APK 与目标 so；
- so ABI 或目录信息；
- JNI 类名、方法名和签名；
- 固定输入 fixture；
- TASK 级输出路径和 Green 条件。

## 基础流程

1. 按 so ABI 选择：
   - `armeabi-v7a` → `AndroidEmulatorBuilder.for32Bit()`
   - `arm64-v8a` → `AndroidEmulatorBuilder.for64Bit()`
2. 设置进程名，优先目标包名；未知时用稳定占位值。
3. 设置 resolver；常见起点是 `new AndroidResolver(23)`，最终以目标 APK 兼容性为准。
4. 用 APK 创建 VM：`emulator.createDalvikVM(new File("apks/x/app.apk"))`。
5. `vm.setJni(this)`；调试阶段可开 `vm.setVerbose(true)`，回归阶段关闭。
6. 加载 so：`vm.loadLibrary(new File("apks/x/libxxx.so"), false)`。
7. 若目标依赖动态注册或 JNI_OnLoad 初始化，执行 `dm.callJNI_OnLoad(emulator)`。
8. `vm.resolveClass("a/b/C")` 找 JNI 类。
9. 使用完整 JNI 签名调用，例如：
   ```text
   encrypt_data(JLjava/lang/String;J)Ljava/lang/String;
   ```
10. 包装参数：
   - `String` → `new StringObject(vm, value)`
   - `byte[]` → `new ByteArray(vm, bytes)`
   - `Map/Object` → `ProxyDvmObject.createObject(vm, value)`
   - `Context` 先试 `vm.resolveClass("android/content/Context").newObject(null)`
11. 解包返回值：`obj.getValue()`。

## 复杂安全 SDK 入口

对于 `deviceInfo`、`anti-token`、风控 header、native 安全 SDK 这类入口，第一次跑出结果不等于真实请求可用：

1. 入口链要写清楚，例如“请求头字段 → Java wrapper → native 方法 → so”；
2. 固定输入必须包括时间戳、业务参数、Context、设备态 fixture 或 Hook 值；
3. 如果 `Context` 展开出权限、系统服务、Telephony、调试态、StackTrace、`/proc` 等环境读取，应立即转入 `patch-unidbg-environment`；
4. 输出只做形态验证时，记录长度、前缀、是否 base64-like、是否稳定，不要宣称与真机一致；
5. 若固定 pid、固定时间或修改 Unidbg runner 才能降低差异，写入 TASK，不写成目标算法的一部分。

## 记录要求

- 记录 emulator 位数、resolver 版本、APK/so 路径；
- 记录 JNI 类、签名、输入和输出；
- 区分 primary 证据与课程笔记描述；
- 输出纳入 TASK 的 Makefile 或脚本。
- 需要 CLI 交付时，从 `assets/UnidbgCliWrapperTemplate.java` 复制 wrapper 到 TASK-local Unidbg 工程，并保证 stdout 最后一行是业务结果。

## Green

- so 可加载；
- 目标 JNI 方法可调用；
- 输出稳定；
- 若失败，能归因到 ABI、路径、缺少 JNI_OnLoad、参数包装或待补环境。

## 迁移状态

- 已覆盖 String、byte[]、Map、Context 等常见 JNI 参数包装规则。
- 已覆盖复杂安全 SDK 入口的 `partial-validated` 边界。
- 具体课程案例、输出值和 APK/so 资源保留在 TASK 与能力注册表，不写入通用 Skill 主体。
