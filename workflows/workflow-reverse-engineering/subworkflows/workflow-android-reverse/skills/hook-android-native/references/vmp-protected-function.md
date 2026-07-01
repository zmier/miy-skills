# VMP 保护函数分支参考路线

## 定位

本 reference 属于 `hook-android-native`，并与 `recover-android-dex`、`analyze-android-native-static`、`diagnose-android-instrumentation` 交叉使用。

它处理的是：目标函数、dex 或 native 入口已经定位，但真实算法语义被 VM dispatch、bytecode、handler 表和解释器循环隐藏。此时问题不再是“函数在哪里”，而是“函数语义被虚拟化后如何建立可验证映射”。

## 典型红灯

| 红灯 | 优先判断 | 看雪资料入口 |
| --- | --- | --- |
| dex/code item 已恢复，但目标函数主体像解释器循环 | 可能是 VMP，而不是 dump 失败 | 看雪第6章 课时1-3 |
| native 函数存在，但伪代码只有 dispatch、handler 表、状态寄存器或 bytecode 解释 | 不按普通 OLLVM 逐条读伪代码，先识别 VM 模型 | 看雪第6章 课时2-5 |
| 普通 Hook 只能看到入口和返回，无法解释中间语义 | 先建立输入输出 oracle，再决定是否构建 opcode/handler 映射 | 看雪第6章 课时2-3 |
| Stalker/Trace 日志巨大且大量重复解释器循环 | 收窄到 bytecode 读取、handler 分发、输出写入窗口 | 看雪第6章 课时9 |
| 反调试阻断 VMP 调试 | 先恢复可观察性，再谈 VMP 映射 | 看雪第6章 课时6；第13章 |
| 需要硬件断点或内核级观测 | 这是高侵入路线，只在授权设备和高价值目标中使用 | 看雪第6章 课时8-9 |

## 与相邻路线的区别

| 类型 | 主要表现 | 优先路线 |
| --- | --- | --- |
| 函数抽取壳 | dump 后函数体 nop、空实现、code item 缺失 | `recover-android-dex` / FART |
| OLLVM | 原函数仍在，但控制流、指令或字符串被混淆 | `native-trace-ollvm.md` |
| VMP | 原语义被自定义 VM bytecode 和 handler 解释执行 | 本 reference；必要时另开 VMP 专项 TASK |
| 反 Frida / 反调试 | 动态观察链被阻断 | `diagnose-android-instrumentation` |

## 推荐流程

```text
确认函数/入口已定位
→ 判断是否存在 VM dispatch、bytecode、handler 表或解释器循环
→ 用 Native Hook 固定输入、输出和触发动作
→ 静态标出 bytecode 读取点、handler 分发表和输出写入点
→ 运行时 trace 只覆盖目标窗口
→ 尝试建立 opcode / handler / 状态寄存器 / VM stack 映射
→ 若目标价值不足，只保留黑盒 oracle 或 RPC 调用
→ 若目标价值足够，另开 VMP 专项 TASK
```

## 升级门槛

只有同时满足以下条件，才从普通 native trace 升级到 VMP 专项：

1. 已排除 dex/code item 未恢复、普通 OLLVM 和普通反调试阻断；
2. 至少有一项 VM 结构证据：dispatch、bytecode、handler 表、VM stack、虚拟寄存器或解释器循环；
3. 已有输入输出 oracle，能验证每一步映射是否接近真实语义；
4. 目标业务价值足以承担高成本分析；
5. TASK 能接受 `partial mapping`，不把“未完整去虚拟化”视作失败。

## Green 边界

- `suspected-vmp`：出现 VM dispatch 或 handler 表迹象；
- `oracle-green`：输入输出可稳定采集并对拍；
- `mapping-partial`：部分 opcode/handler 与语义建立映射；
- `mapping-green`：目标业务路径所需 opcode/handler 已解释；
- `devirtualized`：能外部复现目标业务算法。

不要把“看到了 VM 循环”写成算法已还原。多数 VMP 场景中，黑盒调用、Frida RPC 或 Unidbg 调用可能比完整去虚拟化更划算。

## 看雪查字典入口

优先查看：

- 看雪第6章 课时1：加壳技术分类与初识 VMP；
- 看雪第6章 课时2-3：VMP 保护函数快速逆向；
- 看雪第6章 课时4-5：ADVMP 源码分析与样本构造；
- 看雪第6章 课时7-9：Hyperpwn、内存断点和 VMP 映射；
- workflow 顶层 `../../../references/kanxue-course-directory-index.md`。

采用后回写 workflow 顶层 `../../../references/course-provenance.md`。
