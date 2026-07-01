---
name: hook-android-native
description: 在经过授权的 Android 逆向任务中，基于已验证的模块相对偏移设计最小 Frida Native Hook，采集函数参数、缓冲区字节、长度、调用者偏移与返回值，并把同一次运行结果固化为算法复现 fixture。用于 JNI 映射已完成、Java Hook 看不到 so 内部输入、需要确认签名或加密分段、或要用运行时证据校正 IDA 反编译。不得用于未授权应用、秘密提取真实凭据或扩大业务副作用。
---

# Android Native 运行时取证

## 目标

在“不扩大 Hook 面”的前提下回答一个明确问题：

```text
哪个已映射 Native 函数
在目标动作中
读取了哪些字节
以什么长度和调用顺序
产生了什么输出
```

本 Skill 以当前进程的运行时事实校正静态分析，并为 Python、RPC 或 Unidbg 路线提供固定 fixture。

## 前置条件

- `map-android-jni` 已给出模块、ABI、偏移与 Thumb 状态；
- 已有可靠 JNI 映射；若目标是内部函数或通用算法过滤，还应由 `analyze-android-native-static` 提供候选函数、参数位或调用点；
- TASK 已定义红灯、Green 条件与预期事件；
- 目标动作可低频触发；
- Smoke 已证明 Frida 可附加或冷启动。

## 工作流

1. 阅读 `references/minimal-hook.md`，把实验压缩成一个问题。
2. 固定 APK 与 `.so` 哈希，不复用其他版本的绝对地址。
3. 使用模块相对偏移计算地址；ARM32 按 `references/offset-and-thumb.md` 处理最低位。
4. 优先 Hook 业务函数内部的窄入口；只有它确实是当前算法的汇合点时才 Hook 通用 MD5/AES 函数。
5. 目标 so 尚未加载时，监听 `dlopen/android_dlopen_ext`，命中模块后再安装 Hook；不要用固定睡眠代替加载事件。
6. Key/IV 或参数表示跨越 Native 与 Java 边界时，可同时 Hook Native 生产函数和 Java 消费构造器，形成双边界夹取。
5. 通用函数可能被全进程调用时，用调用者模块与返回地址偏移过滤。
6. 对缓冲区同时记录长度、Hex 和可选 UTF-8，不只记录“看起来像字符串”的文本。
7. 同一次调用链记录：
   - 模块基址和 Hook 地址；
   - 调用者偏移；
   - 参数字节与长度；
   - 调用次序；
   - 业务函数返回值或上层输出。
8. 使用 `scripts/run_native_buffer_probe.py` 进行通用缓冲区观察；目标专用触发逻辑留在 TASK 脚本。
9. 将事件保存为 JSONL，并用 IDA/objdump 静态证据解释为什么这些调用属于目标算法。
10. 把固定输入交给 `reproduce-android-crypto` 做 Unit 与 G1。
11. 若静态伪代码因 OLLVM、控制流平坦化、指令替换或虚假控制流不可读，读取 `references/native-trace-ollvm.md`，选择 IDA Trace、Stalker 或输入/输出追踪路线；不要把“读不懂伪代码”直接写成算法无法复现。
12. 若目标函数主体呈现 VM dispatch、bytecode、handler 表、虚拟寄存器/栈或解释器循环，读取 `references/vmp-protected-function.md`；先区分 VMP、函数抽取壳和普通 OLLVM，再决定是否另开 VMP 专项 TASK。

## 快速运行

```bash
WORKFLOW=/path/to/workflow-android-reverse
"$WORKFLOW/.venv/bin/python" \
  "$WORKFLOW/skills/hook-android-native/scripts/run_native_buffer_probe.py" \
  --package com.example.app \
  --module libtarget.so \
  --offset 0x22b0 \
  --thumb \
  --caller-offset 0x3134 \
  --caller-offset 0x314a \
  --output /path/to/TASK/outputs/native-buffer.jsonl
```

脚本默认附加正在运行的 App；加 `--spawn` 可冷启动。加载后在等待时间内由人类或 TASK 脚本触发目标动作。

## 判断规则

- 绝对地址只在当前进程有效，交付时保存模块相对偏移。
- ARM32 Thumb 函数的代码偏移与可调用指针不是同一个数值。
- 静态工具记录的是调用指令地址，Frida 常记录返回地址；比较前按 `analyze-android-native-static/references/native-address-semantics.md` 标注地址类型。
- Hook 到通用算法函数后出现大量事件，说明过滤条件不足，不说明目标算法复杂。
- Native 输出与 Java 构造器输入一致，能够证明字节表示跨边界未发生额外 Hex/Base64 转换。
- 只看到输入不等于恢复了输出；只看到输出也不能证明输入顺序。
- 多次 `update` 后一次 `final` 的算法必须保留分段顺序，不能仅拼接后声称等价。
- Frida 显示 UTF-8 失败时仍应保存原始 Hex。
- 课程示例偏移、Key 或盐不能替代当前 APK 的运行时证据。

## 输出

- 可重复运行的 TASK Hook 脚本；
- JSONL 原始事件；
- 模块、偏移、Thumb 与调用者过滤说明；
- 输入分段、调用顺序和输出对照报告；
- 面向 Unit/G1 的脱敏 fixture；
- 未解释分支与下一实验。

## 编排交接

由 `android-request-reproduction` 调用时：

- 接收 Native 输入或输出红灯及 Green 条件；
- 只观察足以判定该红灯的数据；
- 捕获一次值标记为 `observed`，稳定脚本可重复取得时标记 `hook-available`；
- 算法输入与输出经同一 fixture 对照后，交给外部复现并等待 Unit/G1；
- R3 纯外部路线未完成前，不能因 Hook 可用就把字段标为 `reproducible`。

## 完成标准

- A：当前模块偏移、调用者过滤、输入分段和业务输出在同一次 fixture 中闭环，脚本可重复执行。
- B：已稳定观察目标函数输入或输出，但另一侧或调用顺序仍不完整。
- C：只证明候选地址会执行，明确记录缺少的参数语义或过滤条件。

## 参考资料

- 设计窄 Hook 与停止条件时读取 `references/minimal-hook.md`。
- 处理模块偏移、ASLR 与 ARM32 Thumb 时读取 `references/offset-and-thumb.md`。
- OLLVM、IDA Trace、Stalker、输入处理/输出回溯路线读取 `references/native-trace-ollvm.md`。
- VMP 保护函数、VM dispatch、bytecode/handler 映射和 Hyperpwn/硬件断点参考读取 `references/vmp-protected-function.md`。
