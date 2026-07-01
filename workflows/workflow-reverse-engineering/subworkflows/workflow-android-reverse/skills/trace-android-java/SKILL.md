---
name: trace-android-java
description: 在经过授权的 Android 应用或课堂靶场中，基于 JADX 静态交接设计并执行最小 Java 运行时取证。用于静态 Find Usage 已能解释调用者但仍缺少真实实参、动态配置、运行时类型、中间值或返回字节时，通过 Frida Hook 建立“静态代码位置—运行时输入—运行时输出”的证据闭环。不得用于凭据窃取、未授权应用或隐藏恶意插桩。
---

# Android Java 运行时取证

## 目标

只观察静态分析无法证明的事实，不用宽泛 Hook 代替 JADX 阅读。输出可重复的运行时 fixture，并把证据交给算法复现 Skill。

## 何时继续 Find Usage

- 需要知道方法由谁调用、业务对象如何流动、生命周期在哪里触发；
- 参数类型和常量可以从调用链直接恢复；
- 当前问题是代码结构，而不是某次执行的真实值。

## 何时使用 Frida

- 需要确认本次调用的真实参数；
- 配置可能由远端下发，静态回退常量不一定生效；
- 需要获得加密前明文、盐、Key、IV 或返回 `byte[]`；
- 混淆、接口分派或运行时类型使静态调用链存在歧义。

Find Usage 与 Hook 不是二选一：前者解释“值从哪里来”，后者证明“这一次值是什么”。

## App 内 HTTP Client 观察

当普通代理、Reqable 或 mitmproxy 看不到目标业务请求，或者只能看到网络出口但无法解释 App 内请求形态时，可以使用 OkHttp 相关探针。

- 只想知道 App 添加了哪些拦截器时，用 `assets/okhttp-interceptor-probe.js`。
- 需要完整 OkHttpLogger 能力时，从 `assets/upstream-okhttplogger-frida/` 复制 upstream 原始脚本到 TASK 目录，并按 upstream README 使用。
- 上游 OkHttpLogger 支持 request/response 打印、`find()`、`switchLoader(...)`、`hold()`、`history()` 和 `resend(index)`；其中 `history/resend` 会产生业务副作用，必须在 TASK 中显式记录。
- OkHttpLogger 输出只能证明 App 内 HTTP client 边界出现过某个请求；目标接口确认仍要回到 `analyze-android-traffic` 的候选矩阵、行为窗口和必要验证。

## 算法探针模式

当目标字段表现为 `sign`、`token`、摘要、HMAC、AES/DES/RSA 或密文，但静态入口尚不明确，并且怀疑使用 Java 标准 Crypto API 时，可以从 `assets/frida-crypto-probe.js` 复制到 TASK 目录运行。

该模式的核心原理是 Hook 一组固定的标准函数，如 `MessageDigest`、`Mac`、`Cipher`、`SecretKeySpec`、`IvParameterSpec` 和 `KeyFactory`，观察算法名、输入摘要、key/iv 摘要和输出。它只生成候选 fixture，不证明请求构造链已完成。

使用规则：

- 先定义行为窗口和 `window_id`，再运行探针；
- 默认只观察并调用原实现，不修改返回值；
- 默认脱敏，只输出长度、预览和 hash；
- 输出 JSONL，状态先标 `crypto-probe-observed`；
- 只有按窗口、调用栈、算法类型和输入输出形态筛选后，才能标 `fixture-candidate` 或 `fixture-selected`；
- 有候选事件时交给 `reproduce-android-crypto`；无候选事件时回到业务边界 Hook、JNI/Native 或运行态路线。

## 工作流

1. 读取静态阶段的 `runtime-handoff.md`。
2. 明确每个 Hook 点要回答的唯一问题，避免全局打印。
3. 按 `references/environment-and-task-contract.md` 使用共享环境和 TASK 脚本。
4. 优先 Hook 已确定的业务边界方法，再按需要 Hook 一层算法方法。
5. 接口、抽象类或 Kotlin 顶层函数先确认运行时实现类型和真实类名，再写正式 Hook。
6. 只知道“谁调用了谁”时打印调用堆栈；需要知道参数如何构造时继续静态追踪或 Hook 参数，不能用堆栈替代数据流。
7. 对重载方法写出精确参数签名。
8. 原样调用旧实现并返回旧结果，不改变业务行为。
9. 将字节统一记录为十六进制，将事件写成 JSONL。
10. 每次只触发一次目标行为，避免重复上报。
11. 将运行时值与 JADX 字段、顺序和算法逐项对照。
12. 脱敏后形成 fixture，原始设备标识保留在本地证据目录。

## 编排交接

由总编排调用时：

- 接收 Mermaid 中具体字段、方法或 Unit fixture 的红灯；
- 每个 Hook 点只回答一个预先声明的问题；
- 把运行时输入、中间值和输出写入带环境信息的 fixture；
- 将 `observed`、`hook-available` 和 `validated` 严格区分；
- 更新证据侧枝、测试矩阵和 ReAct 日志后，由总编排重新计算 `NEXT`。

## 完成标准

- A：取得目标边界同一次执行的必要输入、中间值和输出，确认真实类/方法签名，并能与静态链逐项对应。
- B：取得目标方法实参和返回值，但某个关键来源分支、动态配置或算法中间值尚未直接观察。
- C：证明目标类或 Hook 点存在，但受附加、版本、ClassLoader、进程生命周期或触发条件阻塞。

对正文加密任务，A 级通常包括业务参数、签名输入/输出、Key/IV 和最终字节；对动态字段任务，A 级通常包括运行时实现类型、当前来源分支、生成输入和最终值。只看到“请求来了”不算完成。

## 参考资料

- 执行环境和 TASK 文件归属见 `references/environment-and-task-contract.md`。
- Frida 版本兼容与 Agent 规则见 `references/frida-compatibility.md`。
- 遇到接口分派、JADX 别名或需要打印调用栈时读取 `references/runtime-symbols-and-stack.md`。
- 需要观察 OkHttp Interceptor、Map/TreeMap 参数填充或 Base64/编码路径时，读取 `references/request-boundary-probes.md`，并从 `assets/` 复制对应模板到具体 TASK 后修改。
- 需要使用完整 OkHttpLogger 上游工具时，复制 `assets/upstream-okhttplogger-frida/` 到 TASK；保留原始脚本但在 TASK 日志中记录使用的函数、输出文件、脱敏策略和副作用。
- 算法入口未知但疑似 Java 标准 Crypto API 时，复制 `assets/frida-crypto-probe.js` 和 `assets/crypto-probe-config-template.json` 到 TASK，并按行为窗口输出 JSONL。
- 创建接口实现、Kotlin 文件类和运行时值探针时，从 `assets/runtime-symbol-probe-template.js` 复制到具体 TASK 后修改。
