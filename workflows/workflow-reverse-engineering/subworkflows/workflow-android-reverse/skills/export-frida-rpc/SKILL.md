---
name: export-frida-rpc
description: 在经过授权的 Android 目标进程中，把已定位的 Java 或 JNI 方法封装为最小 Frida RPC，并验证参数桥接、进程生命周期、确定性和错误传播。用于算法难以静态移植、强依赖 App 初始化状态、但可以借用目标进程生成签名或密文的 R2 路线。不得把 RPC 可用误报为纯外部算法已复现，也不得导出真实凭据或面向未授权服务批量调用。
---

# Frida RPC 导出

## 目标

建立明确的远程调用边界：

```text
声明输入
→ JSON 可序列化传输
→ Java 类型重建
→ App 内目标方法
→ JSON 可序列化输出
→ 固定 fixture 对照
```

## 工作流

1. 确认 `diagnose-android-instrumentation` 的 Smoke 已通过。
2. 声明 R2 输入边界、App/设备依赖、预期输出和不可移植状态。
3. 选择最窄的目标方法，不把整个业务流程塞进一个 RPC。
4. 从 `assets/rpc-agent-template.js` 创建 Agent；从 `assets/rpc-client-template.py` 创建单次调用 client。
5. 按 `references/type-bridge.md` 转换 byte[]、Map、对象与异常。
6. 若目标是 App 内 RPC、容器 RPC 或统一网关调用，读取 `references/app-internal-rpc.md`，优先封装最小业务 operation，不导出整个页面流程。
   - 若目标不只是单个方法借用，而是要把 App 运行态作为请求/消息代发通道，由 Python 做调度、限速、落盘和验收，转入 `dispatch-via-app-runtime`，按 R4-A/R4-M 设计 allowlist dispatcher。
7. 固定时间、随机数或业务输入，连续调用至少两次。
8. 与 App 原始调用、bridge 响应或已知 fixture 对照。
9. 默认输出简化 JSON 或脱敏摘要；只有显式参数如 `includeRaw/saveRaw` 才保存完整原始响应。
10. 记录 attach/spawn、目标进程、ClassLoader、初始化前提和 session 失效行为。
11. RPC 稳定后标记 `rpc-available` 或 `app-internal-rpc-call-passed`，不得标记 `reproducible`。
12. 若交付需要脱离设备，返回总编排选择 Python、Android so 重载、Unidbg 或 R3 可行性预检。

## Frida RPC 模板化

最小 Frida RPC 链路是：

```text
JS rpc.exports 暴露 App 内方法
-> Python attach/load
-> script.exports_sync.method(input)
-> 可选把结果用于后续请求
```

模板化时必须清洗掉固定 PID、固定类名、固定业务参数、host、header 和设备 ID。默认使用 `rpc-agent-template.js` 与 `rpc-client-template.py` 做单次可审计调用；Flask/HTTP 包装只作为受控调试或后续服务化路线的可选层，不是默认模板。

## HTTP wrapper 与云手机场景

Flask/FastAPI 这类 HTTP wrapper 的价值是把 Frida RPC 从“当前 Python 进程内可调用”包装成“同机或受控网络内可请求的小服务”：

```text
外部脚本 / 云手机管理端
-> HTTP wrapper
-> Python Frida client
-> Frida RPC
-> App 内目标方法
```

这在云手机、远程真机、容器化设备或跨语言调用场景中有用，因为调用方可能不能直接持有 Frida session，只能访问一个本地或内网 HTTP 入口。

但 HTTP wrapper 不是逆向核心能力，也不是默认交付形态。使用前必须满足：

- 只监听 `127.0.0.1` 或受控内网；
- 明确 allowlist method/action；
- 有限速、日志、超时和停止条件；
- 不记录敏感 header、token、device id 或原始账号态；
- 不把一次 `rpc-call-passed` 伪装成长驻服务稳定性。

如果 wrapper 要长期运行、被外部系统持续调用或承载批量任务，应转入 `dispatch-via-app-runtime` 或 Xposed/Sekiro 长驻路线，而不是继续停留在临时 Flask 脚本。

## Green 条件

- 相同输入在相同状态下得到预期输出；
- 类型桥接和异常可审计；
- session 重建步骤明确；
- 进程退出时不会返回陈旧成功；
- 已与一个 App fixture 对照。

## 边界

- Python 的 bytes/bytearray 先转整数列表；Java 侧用 `Java.array('byte', values)`。
- Map 必须显式重建为目标 Java 类型，不能假定 JS object 自动转换。
- App 内 RPC 不一定能在主线程调用；出现 `IllegalThreadStateException`、线程检查或 Looper 约束时，用 Frida worker thread 或目标框架允许的后台执行方式。
- Python 按包名 attach 失败但 `adb pidof` 能看到进程时，用 PID fallback attach，并把包名、PID 和失败原因写入日志。
- RPC 依赖真机、App 和 Frida，不适合作为无设备 CLI 的最终交付。
- 模板中的 `rpc-call-passed` 只代表一次主动调用成功；连续批量任务需要额外生命周期评估。
- HTTP wrapper 只是 Frida RPC 的调用入口适配层，常见于云手机/远程设备/跨语言脚本调用；它不改变 R2/R4 证据等级。
- R2 只证明可借用 App 运行态生成或获取结果，不证明签名、设备态、TEE、风控上下文已经外部复现。
- R4-A App 代发 dispatcher 不是普通 R2 方法导出：它的交付边界是“App 负责运行态发送，Python 负责工程化调度”。遇到该目标时使用 `dispatch-via-app-runtime`，本 Skill 只提供 Frida RPC 基础能力。
- 当前状态为 `learning`。

## 参考资料

- 类型转换读取 `references/type-bridge.md`。
- 生命周期读取 `references/rpc-lifecycle.md`。
- 封装 App 内 RPC、SimpleRpcService、统一网关 operation 时读取 `references/app-internal-rpc.md`。
- Agent 起点使用 `assets/rpc-agent-template.js`。
- Python 单次调用起点使用 `assets/rpc-client-template.py`。
