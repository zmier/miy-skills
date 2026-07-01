---
name: patch-unidbg-environment
description: 为 Unidbg 执行过程做 signature-driven 最小补环境。用于 so 反向调用 Java、Android 系统对象或 App 自定义对象时，按 UnsupportedOperationException、callObjectMethod/callBooleanMethod/callStaticObjectMethod/newObject 等缺失签名判断真实性边界、选择真实调用/占位/fixture/替身对象、验证 Unit/G1，并在补环境过重时切换 Frida RPC、自建 Android 宿主或组合路线。
---

# Patch Unidbg Environment

## 核心原则

补环境不是维护 Android API 大全，也不是“随便返回一个不报错的值”。它只解决当前 Unidbg 目标函数路径上的最小缺口：

```text
缺失 signature
→ 判断该调用对目标输出是否有语义影响
→ 选择最小返回策略
→ 跑 Unit/G1 验证
→ 记录真实性边界
→ 若补环境开始模拟半个 Android，切换路线
```

Skill 要沉淀的是补环境方法、边界和停止条件，不是把常见 Android API 名单写全。

## 红灯处理

1. 复制完整报错签名，例如：
   ```text
   java/util/TreeMap->entrySet()Ljava/util/Set;
   ```
2. 判断这个 signature 所在的首个差异层：
   - 参数包装错误；
   - `JNI_OnLoad` 或 so 初始化缺失；
   - Unidbg 工具层或签名解析兼容缺口；
   - Java 标准对象需要真实方法调用；
   - JNI 调用形态差异，例如普通调用与 `callObjectMethodV/callStaticObjectMethodV` 的 VaList 形式；
   - Android 系统对象只需占位或固定语义值；
   - Android 设备态、调试态、权限态、`/proc` 或调用栈等运行环境值；
   - App 自定义对象需要最小等价类；
   - 目标函数实际依赖设备态、账号态、TEE 或服务端状态。
3. 判断该调用是否影响目标输出：
   - 不影响目标输出，只为代码继续走，可用占位对象；
   - 影响分支、签名、密文或设备绑定，必须使用真实值、fixture 或继续追来源；
   - 无法判断时，先标记 `unknown-impact`，用最小实验比较输出差异。
4. 在对应 `AbstractJni` 方法中按 `signature.equals(...)` 精准匹配。
5. 处理后保留 `super.*`，不要吞掉 Unidbg 默认实现。
6. 补完后必须回到 Unit/G1。`不再报错` 不是 Green，输出与 fixture 或目标对照通过才是 Green。

## 返回策略决策表

| 判断 | 返回策略 | 能力状态 | 风险 |
|---|---|---|---|
| 真实 Java 对象已在 `DvmObject.getValue()` 中 | 调用真实 Java 方法并包装返回 | `validated` 候选 | 低 |
| 只需维持对象身份或继续控制流 | 返回占位 DVM 对象 | `substitute-valid` 候选 | 中，需说明不影响输出 |
| 目标依赖包名、版本、设备字段等固定语义 | 使用 TASK fixture 或 APK 元数据 | `substitute-valid` 或 `validated` | 中高，可能有绑定 |
| 目标调用 App 自定义类方法或构造函数 | 复制最小等价类并返回真实对象 | `reproducible` 候选 | 中，需与 JADX/运行时对照 |
| 目标依赖 Telephony、权限、调试态、StackTrace、`/proc` 或时间/随机数 | 使用 TASK fixture 先跑通，并标记 device-assisted 对齐需求 | `partial-validated` 候选 | 高，不能直接用于真实请求 |
| Unidbg 自身解析或运行噪声导致无法进入目标逻辑 | 在 TASK 缓存源码做最小工具补丁，并记录为 tooling-gap | 不改变目标能力状态 | 中，不能污染通用源码或误归因给 App |
| 目标依赖账号态、设备态、TEE、服务端下发 | 不继续硬补，切换 R2/R4 | `blocked-by-runtime-boundary` | 高 |

每次只能改变一个 signature 或一组强绑定 signature，便于定位首差。

## 已验证包装模式

这些不是 API 大全，只是当前案例已验证的包装模式。遇到新 API 时按同一决策树处理。

### 真实 Java 对象

- 从 `DvmObject.getValue()` 取真实对象；
- 调用真实 Java 方法；
- 返回前包装为 DVM 对象。

示例链：

```text
TreeMap.entrySet()
Set.iterator()
Iterator.hasNext()
Iterator.next()
Map.Entry.getKey()
Map.Entry.getValue()
```

返回规则：

- 字符串：`new StringObject(vm, value)`；
- 普通对象：`ProxyDvmObject.createObject(vm, obj)`；
- boolean：在 `callBooleanMethod` 直接返回 `boolean`。

### 占位系统对象

当系统对象只承担上下文载体，可先返回占位对象：

```java
return vm.resolveClass("android/app/Application").newObject(null);
```

若后续调用需要真实语义，再补具体方法，例如：

```text
android/app/Application->getPackageName()Ljava/lang/String;
```

包名优先使用 `vm.getPackageName()`，或 TASK 中已验证的固定包名。

### App 最小等价对象

如果 so 调用 App 自定义类方法或构造函数：

1. 从 JADX 复制最小等价类；
2. 保留字段、构造函数和被 native 调用的方法；
3. 在 `newObject` 或 `callStaticObjectMethod` 中创建真实 Java 对象；
4. 用 `vm.resolveClass(...).newObject(realObj)` 包回去。

### 设备态和运行环境 fixture

当 native 安全 SDK 读取设备态或运行环境时，可以先用 fixture 建立离线可执行路径，但必须降低验收范围：

```text
Context.checkSelfPermission
Context.getSystemService("phone")
TelephonyManager.getDeviceId / getSimSerialNumber / getSubscriberId
TelephonyManager.getNetworkOperator / getPhoneType / getSimState
Debug.isDebuggerConnected
Throwable.getStackTrace / StackTraceElement.getClassName
/proc/<pid>/status、/proc/version、/system/build.prop
```

处理规则：

1. 同一语义组可以一次补一小组强绑定 signature，例如 Telephony 的无参、带 slot 参数和 Unidbg 日志中的无括号变体；
2. 每个 fixture 都要写明来源：课程 fixture、APK 元数据、Hook 值、系统常量或人工构造；
3. 若 fixture 影响输出，状态最高只能先标 `partial-validated`，直到真机 Hook 或端到端 G2 对齐；
4. 若输出在固定 fixture 下仍不稳定，记录可能来源：时间、随机数、`/proc`、pid、线程、native 内部状态；
5. 可以为了可重复性在 TASK 缓存中固定 pid 或运行参数，但要标为 `tooling-gap` 或 `runner-control`，不要写成 App 逻辑。

### VaList 与签名变体

同一个 Java 方法可能通过普通 JNI 调用或 VaList 形态触发不同的 Unidbg 回调：

```text
callObjectMethod / callObjectMethodV
callStaticObjectMethod / callStaticObjectMethodV
callIntMethod / callIntMethodV
```

若一个 signature 已补但仍报同语义缺口，检查是否漏了 `*V` 版本。某些 Unidbg 日志还可能出现缺少 `()` 的 signature 变体，例如：

```text
android/telephony/TelephonyManager->getDeviceIdLjava/lang/String;
```

这类变体可以和规范签名共享同一 fixture，但记录时要保留原始报错文本。

### 工具层缺口

如果红灯来自 Unidbg 框架自身，而不是目标 App，例如签名 parser、路径资源定位或 pid 随机性：

1. 先证明目标 APK/so、签名和参数没有写错；
2. 只在 TASK 的运行副本或缓存源码中做最小补丁；
3. 记录补丁文件、原始错误、最小改动、是否影响其他样例；
4. 补丁通过后重新运行 smoke 或最小样例；
5. 不把工具层补丁写成目标 App 的补环境项。

## 停止条件

继续补环境前先问：

1. 这个 signature 是否位于当前目标函数必经路径？
2. 它是否影响目标输出，还是只影响日志、调试或无关分支？
3. 能否用固定 fixture 证明占位值不会改变输出？
4. 继续补下去是否在模拟半个 Android 系统？
5. 切换 Frida RPC、自建 Android 宿主 App 或真实 App 内调用是否更便宜？

出现以下情况，应停止无上限补环境并回到总编排路由：

- 连续多个 signature 都指向真实设备态、账号态、TEE、安全 SDK 或服务端下发状态；
- 占位值无法解释输出差异；
- Unit/G1 对照不稳定；
- 为了跑通一个函数需要大面积实现 Android framework；
- 当前交付路线其实允许 R2/R4 借用 App 或设备，不需要硬走纯桌面。

## 记录要求

每个补环境项都记录：

- 触发 signature；
- 报错阶段；
- 影响判断：`no-impact / affects-branch / affects-output / unknown-impact`；
- 返回策略：`real-java-call / placeholder-object / fixture-value / minimal-app-class / route-switch`；
- 返回值语义和来源；
- Unit/G1 对照结果；
- 迁移风险。

推荐记录片段：

```text
signature:
first-difference-layer:
impact:
strategy:
value-source:
why-minimal:
unit-or-g1-evidence:
route-risk:
next:
```

## 迁移状态

- 已覆盖集合迭代、Context/Application/PackageManager、系统服务、权限、调试态、StackTrace、压缩与流对象等常见补环境模式。
- 每个补环境项的具体来源、fixture、输出值和验收结论必须保留在 TASK，不写入通用 Skill 主体。
