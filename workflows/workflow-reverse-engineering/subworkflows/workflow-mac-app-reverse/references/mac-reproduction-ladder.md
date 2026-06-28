# Mac Reproduction Ladder

## 路线

| 路线 | 形态 | 典型 Green | 不得误写 |
|---|---|---|---|
| M0 | 只读观察 UI、日志、文件、进程、网络 | 行为窗口和候选通道有证据 | 观察到请求不等于复现 |
| M1 | 外部脚本直接构造请求或输入 | 服务端或本地逻辑接受外部复现 | 借用 App 状态不能写成 M1 |
| M2 | 运行态代算字段、对象、中间值 | Frida/lldb oracle 可用 | oracle 可用不等于业务请求成功 |
| M3 | 离线 harness 调 Mach-O/dylib/framework | 离线函数稳定执行并有 parity | 本机能跑不等于服务端接受 |
| M4 | App 运行态代发业务动作 | `liveRequestSentByMacApp=true` | App 代发不能写成 Python 外发 |
| M5 | 长驻 action server/helper/XPC/Frida RPC | allowlist、health、dry-run、real smoke | attach 成功不等于业务 Green |

## 选择原则

优先选择最小满足目标和授权边界的路线。若目标依赖 Keychain、App Sandbox container、session、TLS client cert、WKWebView cookie、Electron IPC、XPC helper 或服务端运行态 envelope，M4/M5 可能比 M1 更正确。

## 必写字段

```text
route=M0/M1/M2/M3/M4/M5
externalRequestSentByPython=true/false
liveRequestSentByMacApp=true/false
runtimeStateOwner=App/Python/helper/human
businessOk=true/false
transportOk=true/false
sensitiveValuesStored=true/false
```

