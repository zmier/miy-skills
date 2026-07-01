---
name: diagnose-android-instrumentation
description: 诊断经过授权的 Android 动态分析为何无法启动、附加或稳定运行，区分普通进程未启动、Root/模拟器检测、Frida 特征检测、版本或 ABI 不匹配、so 加载时机、ptrace 占坑及其他环境红灯，并设计单变量最小恢复实验。用于 App 启动即退出、Hook 后闪退、process not found、unable to access process、attach 失败或 spawn/attach 行为不一致的场景。不得把绕过策略用于未授权应用或隐藏恶意插桩。
---

# Android 插桩故障诊断

## 目标

把“Frida 不工作”拆成可证伪的失败层：

```text
进程与包名
→ 主机/设备版本和 ABI
→ Root/模拟器环境检测
→ Frida 文件、端口、线程或进程特征
→ ptrace 占坑
→ 类/so 加载时机
→ Hook 本身的签名或递归错误
→ 非交互后台、TTY/stdin、USB 抖动或 session 生命周期
```

## 工作流

1. 接收总编排中的 Smoke 红灯、错误原文、启动方式和预期事件。
2. 按 `references/failure-taxonomy.md` 分类，不把所有 attach 错误都称为“反调试”。
3. 建立正常启动、仅启动 server、attach、spawn 四组最小对照。
4. 先确认包名、PID、前台应用、Frida 两端版本和 ABI。
5. App 在无 Frida 时也拦截运行，检查 Root、模拟器和环境安全判断。
6. 仅在 Frida 存在时退出，检查 server 名称、端口、文件、线程、maps 和模块特征。
7. attach 失败而 spawn 可用，检查 ptrace 占坑和保护进程；记录进程树与 `TracerPid`，不要仅凭“两条进程”下结论。
8. 脚本加载后才崩溃，缩减到空脚本，再逐个恢复 Hook，排除签名、重载和递归调用问题。
9. 短窗口稳定但长跑或后台采集失败时，单独检查执行载体：前台、`nohup`、伪终端、真实 TTY、stdin 保活、USB 连接、App 前后台状态、Frida session 生命周期和 App/zygote crash。必要时把业务实体状态与 Frida session 生命周期分离：实体 checkpoint/resume 由上层批量任务负责，session 丢失则优先就地重建。
10. 按 `references/recovery-ladder.md` 从低侵入路线选择最小实验。
11. 当 Red 指向 Frida 环境特征、maps/status/readlink、libc 无证据、SVC/syscall 或 linker/JNI 早期检测时，读取 `references/frida-svc-syscall-ladder.md`；必要时再去 workflow 顶层看雪课程索引查对应章节。
12. 达到 Green 后只报告“观察链恢复”，返回原业务 TASK；不得顺便宣称算法完成。

SSL/TLS 抓包失败、证书不信任、Pinning、WebView SSL error、Cronet pinning 或 mTLS 不属于本 Skill 的首要红灯；先由 `capture-android-traffic` 的 HTTPS MITM 诊断分层。只有绕过脚本本身导致进程退出、Frida attach/spawn 失败、Root/Frida 检测触发时，才进入本 Skill。

## Frida 与 so 加载观察链

当目标是“确认哪个 so 参与检测、加密或网络保护”时，先把观察链跑稳，再讨论绕过：

1. 先做四组对照：普通启动、只启动 Frida server、PID attach 空脚本、spawn 空脚本。
2. Red 没有出现时，写 `not-reproduced`，不要为了贴合课程叙事而继续声明“已绕过反 Frida”。
3. 非交互执行 Frida CLI 时要保持 stdin 存活；例如用 `(sleep 15) | frida ...` 做观察窗口。否则脚本可能刚加载就因 stdin EOF 退出，误判为没有事件。
4. Android 10+ 上不要假定 linker 导出名一定是 `android_dlopen_ext`。先枚举 `linker64`/`linker` 导出，常见可用点包括 `__loader_android_dlopen_ext` 与 `__loader_dlopen`。
5. `dlopen` 观察链只证明“某 so 在该窗口被加载”，不直接证明它就是检测点。后续还要通过删除/替换、函数 Hook、调用栈或行为差异做 confirmatory 证据。
6. 删除 so、改 APK、改系统分区属于高侵入路线，只能作为可回滚平行实验，不能覆盖低侵入 Hook/观测证据。

## Green 条件

- 目标进程在约定窗口内稳定运行；
- Frida session 可建立；
- 最小心跳脚本产生一次预期事件；
- 恢复动作、适用范围和副作用已记录；
- 原业务红灯重新成为唯一 `NEXT`。

## 重要边界

- 通用 Anti-Root 脚本、隐藏型 server、Magisk 模块和定制 AOSP 都是候选路线，不是通用答案。
- `objection` 这类 Frida 封装工具只适合在“空 Frida session 已经稳定”的前提下作为快速探针或通用脚本来源；如果 App 仅因 Frida server、端口、线程、maps 或 attach 行为就退出，`objection` 不能绕过这个前置红灯，仍需先按本 Skill 恢复观察链。
- 不自动安装模块、刷机、改系统分区或删除目标 so。
- 课堂中“删除检测 so”只作为历史策略；优先定位判断点或使用可回滚环境隔离。
- 如果当前设备未复现课程中的反调试 Red，本 Skill 的完成结论应是“Red 未复现，观察链已恢复”，而不是“反调试已解决”。
- 本 Skill 当前状态为 `learning`，尚未完成 Day21-Day23 真机迁移评测。

## 编排交接

输出失败层、最小实验、Green 证据、恢复方案等级和残余风险，并更新 Smoke、Mermaid 环境侧枝及 ReAct 日志。

对长跑采集类红灯，交接时要明确这是“运行载体/session 生命周期”问题，还是“业务接口/服务端窗口”问题。前者交给 `export-frida-rpc` 和批量任务调整 TTY、伪终端、重连和单实体隔离；后者交给 `build-android-rpc-data-corpus` 降速、停止或更新覆盖率声明。

如果观察到 App 反复 crash 或系统 zygote 相关 crash，不要只看 Frida 报错文本。应增加 runtime crash sentinel：

```text
adb logcat -b crash -d -t <last-check-time>
确认 Fatal signal 是否属于目标包、zygote 或相关 native runtime
若命中，标记 environment_failed
停止业务请求并触发环境修复或人工通报
修复后用最小 attach + 低风险业务 smoke 恢复
```

runtime crash sentinel 的职责是防止“App 已崩但队列仍在请求”的假失败；它不负责解释业务 1009、签名错误或服务端限制。

## 多 USB 设备误选

当主机同时连接 iPhone、Android、模拟器或多个远程 Frida device 时，`frida.get_usb_device()` 可能选择到非目标设备。若 Android 任务中出现类似 iOS Developer Disk Image、目标包名不存在但 adb 可见、或 attach 错误与业务无关的文本，不要先判断为反调试。

最小恢复：

```text
frida.enumerate_devices()
adb devices
adb -s <android-serial> shell pidof <package>
frida.get_device("<android-serial>").attach(pid)
```

工程要求：

```text
脚本应支持 --device-id；
或读取 ALIB_FRIDA_DEVICE / ALIB_ANDROID_SERIAL / ANDROID_SERIAL；
adb pidof 与 frida attach 必须使用同一个 serial。
```

## 参考资料

- 错误分类读取 `references/failure-taxonomy.md`。
- 选择恢复路线读取 `references/recovery-ladder.md`。
- Frida 特征检测、libc 到 SVC/syscall 升级路线读取 `references/frida-svc-syscall-ladder.md`。
- 创建 TASK 时复制 `assets/instrumentation-diagnosis-template.md`。
