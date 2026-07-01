# Kernel / eBPF 高级观测路线

## 定位

本 reference 属于 `diagnose-android-instrumentation`。

它只在用户态观测链不足时使用：

```text
Frida / libc hook / SVC scan / Stalker
→ 仍无法解释文件、网络、进程、线程或 syscall 行为
→ 评估 kernel/eBPF 观测
```

## 触发条件

| 红灯 | 可能含义 | 动作 |
| --- | --- | --- |
| libc hook 没有证据，但系统调用确实发生 | 可能绕过 libc 或使用内联 syscall | 先走 SVC/syscall；仍不足再评估 eBPF |
| 用户态 Hook 一装就被检测 | 用户态探针自身被识别 | 先做 Frida 恢复阶梯；eBPF 只作为远期观测 |
| 需要跨进程、跨线程、网络或文件全局视角 | 单进程 Hook 证据不够 | 评估 kernel/eBPF |
| 需要长期观测 syscall 或网络事件 | 用户态 trace 成本过高 | 评估专用实验设备和 eBPF 环境 |

## 升级门槛

只有同时满足以下条件才进入：

1. 当前 TASK 明确授权 kernel/eBPF 级观测；
2. 有专用实验设备、Root/内核支持、可回滚方案；
3. 用户态 Frida/libc/SVC/Stalker 路线已尝试或有明确不适用证据；
4. 目标问题确实是系统事件观测，不是普通算法复现；
5. 能保存 eBPF 程序、加载命令、内核版本、事件 schema 和日志。

## Green 边界

- `environment-green`：设备支持 eBPF，最小程序可加载；
- `event-observed`：观察到目标 syscall/网络/文件/进程事件；
- `correlated`：事件与 App 行为窗口、线程或进程可对齐；
- `diagnosis-green`：解释了用户态看不到的原因；
- 不得把 eBPF 事件观察写成请求参数、算法或反调试已完成。

## 看雪查字典入口

优先查看：

- 看雪第11章 课时1：Android 上 eBPF 现状；
- 看雪第11章 课时2：eBPF 手机开发环境搭建；
- 看雪第11章 课时3：eBPF 实用项目源码技术原理；
- workflow 顶层 `../../../references/kanxue-course-directory-index.md`。

采用后回写 workflow 顶层 `../../../references/course-provenance.md`。
