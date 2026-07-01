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
6. GUI/图表/动态列表目标若发现 View 层 index 会漂，优先采用 model-marker-first，而不是继续硬改 draw/fill/cell：
   - 只读观察 model item 与 visible range；
   - 在授权副本或可恢复上下文中写临时 marker；
   - 在 render hook 中用 marker + visible offset 计算 local index；
   - 对目标样本和控制样本同时记录 candidate/patch；
   - UAT 覆盖滚动、缩放、懒加载、缓存刷新、数据补全和回看。
7. 导出 Frida RPC 时先做 dry-run，不触发真实业务动作。
8. 若要触发业务请求或动作，转入 `dispatch-via-mac-app-runtime`，并声明 M4/M5 边界。

## Model Marker First

当渲染层只有 local index、cell、layer、fill 或 color 时，修改 View 层通常只能得到短暂 Green。更稳的最小模式是：

```text
target business key -> model item marker
visible offset/range -> markerLocalIndexes
render hook -> shouldPatch = index in markerLocalIndexes
control business key -> shouldPatch must stay false
```

安全要求：

- marker key 使用任务命名空间，避免覆盖原字段；
- 先验证目标对象是可变容器或有可恢复 setter；
- 若对象不可变，先找 parser/property 层的可变副本；
- 修改前记录副作用和恢复方式；
- patch 事件必须携带当前 mapping，能证明 patched index 来自 marker；
- 控制样本必须持续观测，不能只看目标样本变色。

## Green

```text
fridaAttachOk=true
scriptLoadedOk=true
targetRuntimeReady=true
hookObservedInputOutput=true
rpcDryRunOk=true/false
businessRpcTriggered=false/true
sensitiveValuesStored=false
modelMarkerPathVerified=true/false
controlSampleStayedNegative=true/false
```

Frida hook 成功不等于业务 Green。
