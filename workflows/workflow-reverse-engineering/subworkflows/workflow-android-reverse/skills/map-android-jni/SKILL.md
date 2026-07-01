---
name: map-android-jni
description: 在经过授权的 Android 逆向任务中，恢复 Java native 声明到目标 so 实现函数的映射，区分静态导出与动态 RegisterNatives 注册，并记录类名、方法名、JNI 签名、模块、运行时地址、文件偏移和 ARM Thumb 状态。用于 JADX 已确认逻辑进入 native、IDA 中找不到 Java 风格导出名、需要从冷启动捕获动态注册表，或为后续 Native Hook 提供可靠偏移。不得用于未授权应用、凭据窃取或规避访问控制。
---

# Android JNI 映射恢复

## 目标

把“Java 中存在一个 `native` 方法”推进为可复核的 Native 地址证据：

```text
Java 类 + 方法 + JNI 签名
→ 注册方式
→ 目标模块
→ 运行时实现地址
→ 模块相对偏移
→ 指令集状态
```

本 Skill 只负责映射，不把函数地址猜测为算法结论。

## 前置条件

- 目标属于课堂靶场、自有应用或明确授权测试；
- APK、包名、目标 Java 类与 `native` 声明已经固定；
- Frida 主机端与设备端版本一致；
- 目标进程可冷启动，或能在动态注册发生前附加；
- Native 工具链 Smoke 已由 `prepare-android-native-toolchain` 通过。

## 工作流

1. 从当前 APK 的 JADX 结果记录类名、方法名与完整 JNI 签名。
2. 按 `references/registration-modes.md` 判断静态导出与动态注册两条路线。
3. 先检查目标 `.so` 导出符号；没有 `Java_包名_类名_方法名` 时，不要据此断言函数不存在。
4. 动态注册场景使用 `scripts/run_register_natives_probe.py` 冷启动目标进程。
   - 需要人工拷贝到 TASK 或探索全部注册项时，可使用 `assets/register-native-map.js`；它输出 JSONL，并同时给出 `raw_offset`、`code_offset`、`thumb` 和 `arch`。
   - 需要交叉验证或主路线受阻时，读取 `references/register-native-parallel-routes.md`，评估 ART `PrettyMethod + retval` 平行路线；通用模板优先读取 `JNINativeMethod` 数组。
5. 只保留目标类的注册项，记录：
   - `class_name`
   - `method_name`
   - `signature`
   - `module_name`
   - `implementation`
   - `module_base`
   - `offset`
   - `thumb`
6. 对 ARM32 地址同时保存原始函数指针和去除最低位后的代码偏移；IDA、objdump 与 Frida 使用偏移时明确是否需要补回 Thumb 位。
7. 用反汇编检查该偏移附近是否是合理函数入口或跳板。
8. 按 `references/evidence-contract.md` 写入 TASK、请求构造台账与 ReAct 日志。
9. 根据问题选择交接：
   - 只需 JNI 入口实参或返回值：直接交给 `hook-android-native`；
   - 需要入口跳板、内部主体、xref 或窄 Hook 候选：交给 `analyze-android-native-static`；
   - 需要高置信度：静态与动态交叉验证。
10. 若出现 JNI 地址绑定、防追踪、动态释放、跳板或 RegisterNatives/PrettyMethod 证据不一致，读取 `references/jni-address-anti-trace.md` 后再决定是否进入 linker/JNI 生命周期、硬件断点、IDA Trace 或 Stalker。
11. 算法仍未知时保持对应字段红灯。

## 快速运行

```bash
WORKFLOW=/path/to/workflow-android-reverse
"$WORKFLOW/.venv/bin/python" \
  "$WORKFLOW/skills/map-android-jni/scripts/run_register_natives_probe.py" \
  --package com.example.app \
  --class-name com.example.NativeBridge \
  --output /path/to/TASK/outputs/register-natives.jsonl
```

该脚本默认使用 USB 设备、冷启动并覆盖输出文件。目标 App 若必须保留登录态，冷启动不会清除数据。

## 判断规则

- Java `native` 声明只能证明存在 JNI 边界，不能证明实现位于哪个模块。
- stripped `.so` 没有业务符号很常见，动态注册表是更直接的运行时事实。
- `RegisterNatives` 运行时捕获可以直接给出模块和偏移，减少在 so 中手工猜入口；但它只定位入口，不解释算法语义。
- 函数指针最低位为 `1` 时通常表示 ARM32 Thumb 状态；文件偏移用于静态工具时要清除最低位。
- 注册项可能指向短跳板。映射完成后仍需反汇编或最小 Hook 确认真实执行链。
- 只捕获到模块加载地址，不等于捕获到方法映射。
- 课程笔记中的地址会受版本与 ASLR 影响，不能复用为当前 APK 的完成证据。

## 输出

- 原始 JSONL 注册事件；
- 目标方法映射表；
- APK、模块哈希与 ABI；
- 反汇编交叉检查；
- 当前置信度、未排除解释与下一 Hook 点。

## 编排交接

由 `android-request-reproduction` 调用时：

- 接收 JNI 映射红灯、目标类、目标方法和 Green 条件；
- 成功后把节点从 `unknown` 更新为 `located`；
- 只有运行时注册表与当前模块证据一致时才标记 `validated`；
- 将唯一 `NEXT` 移到 Native 静态结构或运行时输入、输出取证；
- 不得因映射已知就提前通过 sign、加密或完整请求测试。

## 完成标准

- A：当前 APK 冷启动实测到目标方法的类、签名、模块、偏移与 Thumb 状态，并经反汇编确认入口合理。
- B：已得到运行时模块和偏移，但加载时机或跳板后的真实函数尚未确认。
- C：仅有 Java 声明或静态猜测，明确记录缺少动态注册证据的原因。

## 参考资料

- 选择静态导出或动态注册路线时读取 `references/registration-modes.md`。
- 对比 `JNINativeMethod` 数组路线与 ART `PrettyMethod + retval` 路线时读取 `references/register-native-parallel-routes.md`。
- JNI 地址绑定、防追踪、跳板、动态释放或硬件断点路线读取 `references/jni-address-anti-trace.md`。
- 记录、规范化和交付映射证据时读取 `references/evidence-contract.md`。
- 人工 TASK 模板可复制 `assets/register-native-map.js`；兼容旧 runner 的模板仍为 `assets/register-natives-probe.js`。
