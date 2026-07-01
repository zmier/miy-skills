---
name: analyze-android-obfuscation
description: 在经过授权的 Android APK 中分析 R8/ProGuard 等混淆造成的短类名、短方法名和 JADX 阅读别名，建立“源码职责、JADX 别名、Dex/Frida 真实符号、方法签名”的双重符号映射，并用调用关系、常量、类型和运行时证据恢复职责。用于静态代码可见但命名难读、JADX 反混淆名称无法直接 Hook、同名短类大量冲突的场景。不得把混淆与加固壳混为一谈。
---

# Android 混淆分析

## 目标

同时维护两个世界：

- 阅读世界：JADX 别名、反混淆名称和推测职责；
- 运行世界：Dex 中真实类名、方法名、重载签名和 ClassLoader。

## 工作流

1. 先判断代码是否真实存在；业务 Dex 缺失时返回 `recover-android-dex`。
2. 从 URL、稀有字段、常量、注解和类型签名定位候选，而不是只搜 `sign`。
3. 记录真实符号和 JADX 别名，使用 `assets/symbol-map-template.md`。
4. 通过 Find Usage、接口实现、构造器和返回类型恢复职责。
5. Hook 时始终使用 Dex/运行时真实符号。
6. 同名短类冲突时使用完整包名、精确 overload 和 ClassLoader。
7. 若真实符号仍不确定，用 `trace-android-java` 枚举运行时类与签名。
8. Green 后把职责名称作为注释保留，但不重命名原始证据。

## Green 条件

- 目标职责映射到唯一真实类、方法和签名；
- JADX 别名与真实符号不会混用；
- 静态调用链与一次运行时解析相符；
- 下游 Hook 模板使用真实符号。

## 结构核验案例

Day23 司小宝中，JADX 可把 `p0.a` 显示为更易读的 `GatewaySign4Customer` 别名，但 APK 运行时真实符号仍是 `cmt.chinaway.com.lite.q.p0.a`。本地 JADX 结构检查确认该真实类、`s0` 和 `n1` 均存在。

当前状态为 `learning`。

## 参考资料

- 映射规则读取 `references/symbol-discipline.md`。
- 使用 `assets/symbol-map-template.md`。
