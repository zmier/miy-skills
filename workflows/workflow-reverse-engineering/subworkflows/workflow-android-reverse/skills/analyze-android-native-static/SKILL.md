---
name: analyze-android-native-static
description: 对经过授权的 Android ELF/.so 做可复核的静态分析，在 LLVM objdump、IDA/Hex-Rays 与双路线交叉验证之间选择合适路径，恢复 ARM32 Thumb 函数边界、入口跳板、调用关系、伪代码、JNI 函数表调用和后续 Native Hook 候选。用于 JNI 映射已知但 Native 主体、算法调用或返回对象构造仍不清楚，或需要复现课程中的 IDA 分析过程。不得把静态猜测当作运行时实参证据。
---

# Android Native 静态分析

## 目标

把已验证的“模块 + 相对偏移 + 指令集状态”推进为静态结构证据，并为最小 Native Hook 提供候选点。

## 路线选择

| 路线 | 适用情况 | 主要产物 |
|---|---|---|
| A：LLVM objdump | 目标窄、偏移已知、只需入口/调用指令 | Thumb 反汇编 |
| B：IDA/Hex-Rays | 控制流复杂、需要伪代码/xref/JNI 构造链 | IDB、伪代码、交叉引用 |
| C：交叉验证 | 教学复现、高置信度交付、工具表现有差异 | A+B+运行时证据与差异解释 |

IDA 内部还需区分 batch 与 MCP：batch 适合正式可重复导出，MCP 适合交互探索和独立复核。详细选择条件见 `references/route-selection.md`。

## 工作流

1. 固定 `.so` 哈希、ABI、模块相对偏移和 Thumb 状态。
2. 从 TASK 的红灯问题反推所需证据，避免无目标地浏览整个二进制。
3. 创建 targets JSON；可复制 `assets/targets-template.json`。
4. 选择 `ida`、`objdump` 或 `cross` 路线：

```bash
python scripts/run_static_analysis.py \
  --route cross \
  --binary /path/to/libtarget.so \
  --targets /path/to/targets.json \
  --output-dir /path/to/TASK/outputs/static \
  --force
```

5. 检查 `static-analysis-manifest.json`，确认工具版本、命令、哈希和各适配器均成功。
6. 从 `ida-evidence.json` 记录函数范围、伪代码、xref 与 JNI 函数表偏移；从 `objdump-thumb.txt` 核对真实指令。
7. 使用 MCP 时按 `references/ida-mcp-lifecycle.md` 记录输入哈希、证据角色并关闭 IDB。
8. 按 `references/native-address-semantics.md` 区分函数指针、静态代码地址、调用指令和返回地址。
9. 若 IDA 合并包装入口与跳转主体，按控制流语义解释，不要求界面必须与旧版本完全同形。
10. 静态结果只用于解释结构和设计 Hook。真实缓冲区、长度、分段顺序与动态配置仍交给 `hook-android-native`。
11. 若 Hex-Rays 或反汇编出现 vtable、`this` 指针、多层间接调用、RTTI、构造/析构或异常痕迹，读取 `references/cxx-object-semantics.md`；先恢复对象语义和真实实现候选，再决定 Hook 点。
12. 若目标函数受 OLLVM 或强混淆影响，静态分析只负责确认函数窗口、返回点、调用者和 trace 边界；后续按 `../hook-android-native/references/native-trace-ollvm.md` 进入 IDA Trace、Stalker 或输入/输出追踪。遇到控制流平坦化、虚假控制流、指令替换、字符串加密或 NDK OLLVM 样本构造问题时，先查看 workflow 顶层 `../../references/kanxue-course-directory-index.md` 中“第5章 彻底搞懂OLLVM”的课时4-10，把课程材料作为解释和路线选择参考，不作为当前样本证据。
13. 把结论、证据角色、差异和下一 Hook 候选写回请求构造台账、TASK 与 ReAct 日志。

## 判断规则

- ARM32 函数指针最低位为 Thumb 状态位，静态代码地址通常需清除最低位。
- IDA 自动分析可能漏掉 Thumb 函数边界；应先设置 `T=1`、创建指令和函数，再判断 Hex-Rays 是否失败。
- IDA 将入口跳板与主体合并，不代表分析错误；比较控制流、调用点和输出语义。
- 函数外观像 MD5/AES 只形成候选；标准常量、数据流、xref 与运行时输入共同提高置信度。
- JNI 函数表偏移应对照当前 ABI 的 `jni.h`，不能只凭数字猜函数名。
- 静态分析能回答“可能怎样构造”，不能单独回答“本次运行传入了什么”。
- MCP 返回与 batch 伪代码一致时属于独立确认；只有落盘并满足预设 Green 时才可承担 primary。

## 编排交接

- 接收 `map-android-jni` 输出的模块、规范化偏移、ABI 和 Thumb 状态。
- 输出入口/主体关系、算法候选、JNI 构造链、xref 与最小 Hook 候选。
- 需要真实参数时交给 `hook-android-native`；需要外部实现时再交给 `reproduce-android-crypto`。
- 本 Skill 可作为主路线，也可作为已完成动态路线的非阻塞学习增强分支。

## 完成标准

- A：当前 `.so` 的 IDA/objdump 证据与运行时映射一致，关键调用关系和 Hook 候选可复核。
- B：至少一条静态路线成功，但伪代码、函数边界或 JNI 语义仍需动态验证。
- C：工具不兼容或反编译失败，但已保存版本、命令、失败层和可执行降级路线。

## 参考资料

- 选择 A/B/C 路线时读取 `references/route-selection.md`。
- IDA 漏识别 ARM32 Thumb 函数时读取 `references/ida-thumb-function-recovery.md`。
- 比较 IDA、objdump 与 Frida 时读取 `references/cross-validation.md`。
- 使用 IDA MCP 时读取 `references/ida-mcp-lifecycle.md`。
- 比较 Thumb 指针、调用点和返回地址时读取 `references/native-address-semantics.md`。
- 遇到 C++ 对象、虚表、RTTI、继承或异常语义卡点时，读取 `references/cxx-object-semantics.md`。
- OLLVM 或静态伪代码不可读时，读取 `../hook-android-native/references/native-trace-ollvm.md` 确定 trace 边界与运行时取证路线。
- 需要补 OLLVM 类型、生成原理或具体混淆形态时，读取 workflow 顶层 `../../references/kanxue-course-directory-index.md` 的第5章索引；采用课程材料反哺时回写 `../../references/course-provenance.md`。
