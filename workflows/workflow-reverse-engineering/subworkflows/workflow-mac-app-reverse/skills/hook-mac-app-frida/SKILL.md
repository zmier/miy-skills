---
name: hook-mac-app-frida
description: 在授权 Mac App 目标中使用 Frida 做动态 attach、ObjC/Swift/C 函数 hook、Interceptor trace、参数/返回值观察、字段 oracle、Frida RPC 和最小 action prototype。用于 M2 运行态代算、M4 代发原型和 M5 服务化前验证。
---

# Hook Mac App With Frida

## 工作流

1. 确认授权允许 attach/hook，记录目标进程、架构、签名保护、Hardened Runtime 和是否需要 helper 进程。
2. 先做 attach smoke：进程可见、脚本加载、无 crash、能打印 runtime 信息。
3. ObjC 目标优先枚举 class/selector，再 hook 最小方法。
4. C/C++/Swift 目标优先从符号、地址、字符串邻近或 lldb 断点确认入口，再用 `Interceptor.attach`。
5. 只读观察先于修改返回值；修改行为前必须写明副作用和恢复方式。
6. 导出 Frida RPC 时先做 dry-run，不触发真实业务动作。
7. 若要触发业务请求或动作，转入 `dispatch-via-mac-app-runtime`，并声明 M4/M5 边界。

## Green

```text
fridaAttachOk=true
scriptLoadedOk=true
targetRuntimeReady=true
hookObservedInputOutput=true
rpcDryRunOk=true/false
businessRpcTriggered=false/true
sensitiveValuesStored=false
```

Frida hook 成功不等于业务 Green。

