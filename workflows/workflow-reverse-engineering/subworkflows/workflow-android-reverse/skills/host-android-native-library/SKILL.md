---
name: host-android-native-library
description: 为经过授权的 Android Native 库设计最小自建宿主 App，按 ABI、库依赖、JNI 静态注册符号、Java 包名/类名和 Android 组件依赖评估能否脱离原 App 加载并调用目标 so。用于 Frida RPC 仍依赖原进程、算法难以移植、但目标库接口稳定且适合在 Android 环境重载的 R4 路线。不得重打包第三方应用、绕过许可或用于未授权服务调用。
---

# Android Native 库重载

## 目标

判断目标 so 是否能被最小宿主 App 调用，而不是默认“拷贝进去就能运行”。

## 工作流

1. 固定 APK/so 哈希、ABI 和目标 JNI 方法。
2. 按 `references/feasibility.md` 评估静态注册、动态注册、依赖库和环境依赖。
3. 静态注册时恢复原 Java 包名、类名、方法名和签名。
4. 动态注册时确认 `JNI_OnLoad/RegisterNatives` 所需类是否可在宿主中提供。
5. 复制目标 so 及必要依赖到对应 `jniLibs/<abi>/`。
6. 创建最小 Java/Kotlin 声明和单一调用入口。
7. 首个 Smoke 只验证 `System.loadLibrary`；第二个 Unit 才调用目标方法。
8. 缺类、资源、Context、签名、资产或系统服务时，只补当前报错所需的最小环境。
9. 与原 App fixture 比较固定输入输出。
10. 达到 Green 后把路线标记为 R4 Android-hosted，不得宣称纯 Python。

## Green 条件

- 库及依赖在目标 ABI 上成功加载；
- JNI 方法成功解析；
- 固定输入得到与原 App 一致的输出；
- 所需 Android 环境和缺失项有清单；
- 工程可重复构建。

## 路线选择

- 只需快速借用原 App：优先 Frida RPC。
- 目标库依赖少、JNI 边界稳定：考虑本 Skill。
- 环境依赖复杂且希望桌面自动化：考虑 Unidbg。
- 算法可移植：优先 Python 外部实现。

当前状态为 `learning`。本 Workflow 尚未完成 Android 宿主工程 forward-test；若只需要桌面自动化交付，优先评估 Unidbg CLI wrapper。

## 参考资料

- 可行性判断读取 `references/feasibility.md`。
- 创建任务时使用 `assets/android-host-checklist.md`。
