# Frida 特征检测与 SVC/syscall 升级路线

## 定位

本 reference 属于 `diagnose-android-instrumentation`。

它处理的不是“目标算法怎么还原”，而是“动态观察链为什么被拦住，以及如何恢复最小可观察性”。

## 典型红灯

| 红灯 | 优先判断 | 看雪资料入口 |
| --- | --- | --- |
| Frida server 开着时 App 启动即退 | 默认端口、协议、进程、maps、线程特征 | 看雪第10章 课时16 |
| attach 空脚本也退 | 环境特征检测，不是 Hook 逻辑错误 | P1 Frida 常见特征检测 |
| 改端口后恢复 | 默认端口检测成立 | 看雪第10章 课时16 |
| libc hook 能看到 open/readlink/connect/maps/status | 检测通过 libc API 实现 | 看雪第10章 课时16 |
| libc hook 无证据但仍退 | 可能内联 SVC/syscall 或 native 混淆检测 | 看雪第13章 课时1-3 |
| 检测 so 在 init/init_array/JNI_OnLoad 期间触发 | 需要 linker 生命周期和早期 Hook | 看雪第13章 课时1、3 |
| 定位到 SVC 指令但不知道参数 | 需要 syscall number 与寄存器约定 | 看雪第13章 课时1-3；第3章 课时17 |
| SVC 定位方法不确定 | 需要横评 Memory.scan、Stalker、IDA/kernel/eBPF | 看雪第13章 课时2 |

## 恢复阶梯

```text
普通启动正常？
→ 否：先查 Root/模拟器/环境，不直接归因 Frida
→ 是：继续
只开 Frida server 是否触发？
→ 是：端口/协议/server 特征
→ 否：继续
attach 空脚本是否触发？
→ 是：maps/线程/内存/文件特征
→ 否：继续
具体 Hook 后才触发？
→ 是：Hook 签名、递归、函数头改写或业务副作用
→ 否：继续
libc API 是否有证据？
→ 是：open/read/readlink/connect 等窄 patch
→ 否：进入 SVC/syscall 分支
```

## SVC/syscall 分支

升级到 SVC 前，需要先有证据：

- libc 路线没有看到对应文件、端口或线程访问；
- App 仍在同一窗口退出或上报；
- 目标 so 或检测时机已基本确认；
- 低侵入环境特征绕过不够。

SVC 定位路线按侵入性排序：

1. 已知模块未加壳：IDA/objdump 直接找 SVC 指令；
2. 模块已加载且可读：`Memory.scan` 扫描模块或 `r-x` 区间；
3. 时机敏感：hook linker / `dlsym` / `JNI_OnLoad` 后扫描；
4. 路径复杂：Stalker 或 IDA Trace 记录目标窗口中的指令；
5. 高级观测：kernel/eBPF 记录 syscall 进入点。

若走到第 5 级，读取 `kernel-ebpf-observability.md`；eBPF 只用于系统事件观测和归因，不代表反调试绕过或目标算法完成。

## 参数与 patch 纪律

- AArch64 syscall number 通常在 `x8`；ARM32 常见在 `r7`；
- 文件路径类检查优先观察 `open/openat` 的 path；
- fd 被替换后，要同时考虑 `readlink/readlinkat` 对 fd 路径的反查；
- path 指针写入要控制长度，避免覆盖相邻内存；
- 每次只 patch 一个检测点，然后重跑四组对照。

## Green 边界

- `observation-green`：Frida session 已恢复，能继续业务观察；
- `bypass-green`：已证明某个检测点被绕过；
- `not-reproduced`：课程或历史 Red 当前环境未复现；
- 不得因为 App 不退出就宣称所有反调试已解决；
- 不得把绕过检测写成目标请求算法已完成。

## 看雪查字典入口

优先查看：

- 看雪第10章 课时16：Frida 常见特征检测与对抗；
- 看雪第10章 课时17：如何快速绕过被 OLLVM 混淆的 Frida 检测；
- 看雪第13章 课时1-3：SVC/syscall 定位；
- 看雪第11章：eBPF 作为远期 kernel 观测路线；
- 本目录 `kernel-ebpf-observability.md`：kernel/eBPF 升级门槛和证据边界；
- workflow 顶层 `../../../references/kanxue-course-directory-index.md`。

采用后回写 workflow 顶层 `../../../references/course-provenance.md`。
