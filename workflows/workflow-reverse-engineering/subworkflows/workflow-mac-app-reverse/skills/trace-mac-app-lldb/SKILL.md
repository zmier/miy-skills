---
name: trace-mac-app-lldb
description: 在授权 Mac App 目标中使用 lldb 做 attach、breakpoint、watchpoint、expression、调用栈和寄存器/内存观察，验证 Mach-O/ObjC/Swift/C/C++ 候选入口，辅助定位 anti-debug、符号缺失和运行态状态。
---

# Trace Mac App With LLDB

## 工作流

1. 确认授权允许调试，记录是否需要关闭或诊断 anti-debug。
2. 先做 attach smoke：进程、架构、符号加载、断点命中和无 crash。
3. 对候选地址、selector、C 函数、Swift 符号或系统 API 设置最小断点。
4. 记录调用栈、线程、参数、返回值、对象摘要和触发 UI/网络动作。
5. 用 watchpoint 或条件断点收窄字段生成链。
6. 若 lldb 被阻断，交给 `diagnose-macos-protection`。
7. 若需要自动化 oracle，迁移到 `hook-mac-app-frida` 或 harness。

## Green

```text
lldbAttachOk=true
breakpointHitOk=true
callStackCaptured=true
inputOutputObserved=true
nextHookOrHarnessPlan=true
```

