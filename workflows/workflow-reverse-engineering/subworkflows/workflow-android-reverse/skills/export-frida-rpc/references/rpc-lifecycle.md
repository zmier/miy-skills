# RPC 生命周期

- 明确 attach 或 spawn。
- 明确目标进程和 ClassLoader。
- 在导出函数内部等待 `Java.perform` 完成。
- App 重启、崩溃或切进程后 session 必须重建。
- 为每次调用记录输入摘要、输出摘要、耗时和异常。
- 不自动无限重试；session 丢失应显式失败。

## 单次 RPC 与批量 RPC 的区别

单次 RPC Green 不等于批量 Green。

`rpc-available` 只表示在当前 App 状态和当前 session 中，单次或少量调用可用；它不自动证明长时间批量采集稳定。

进入批量或语料库任务前，需要额外声明：

- 执行环境：前台短命令、后台命令、伪终端或真实 TTY；
- session 生命周期：App 切后台、进程重启、USB 抖动、脚本销毁时如何识别；
- 重建策略：是否能安全 detach、重新 attach、reload script，并重试当前实体；
- 批量边界：每个实体是否独立调用，失败是否继续，何时停止整批；
- 证据边界：RPC 可借用 App 运行态，不等于算法、签名、设备上下文已外部复现。

如果非交互后台执行出现提前退出、stdin EOF、`script has been destroyed`、进程仍在但 RPC 无响应等现象，先归入生命周期/执行载体问题，不要直接归因为业务接口失效或反调试。

## 半健康状态

Frida 可能出现“server 进程存在、`frida-ps -Uai` 能列应用，但 attach 或 create_script 失败”的半健康状态。典型错误包括：

- `frida.ServerNotRunningError: unable to connect to remote frida-server: closed`
- `frida.TransportError: the connection is closed`

这种状态说明 USB device 枚举链路仍可用，但注入会话链路已经坏掉。恢复流程：

1. 停止正在长跑的上层 supervisor，避免连续跳过实体。
2. 用最小 Python 脚本对目标 PID 执行 `device.attach(pid)` 烟测。
3. attach 失败时重启手机端 frida-server，而不是只重启 Python client。
4. attach 成功后先跑单实体 RPC，确认业务 agent 可以 load / call / detach。
5. 单实体 Green 后再恢复批量任务。
