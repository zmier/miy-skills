---
name: analyze-objc-swift-runtime
description: 在授权 Mac App 中分析 Objective-C runtime、Swift 符号、selector、class、method、block、delegate、notification、KVO、WKWebView bridge 和 Electron/JS bridge 候选，用于把静态候选映射到运行态 hook 点。
---

# Analyze ObjC Swift Runtime

## 工作流

1. 从静态分析接收 class、selector、Swift mangled symbol、字符串和调用链候选。
2. 判断运行时类型：ObjC、Swift mixed、SwiftUI/AppKit、Electron、WKWebView、Qt 或 native C++。
3. ObjC 优先枚举 class、method、protocol、delegate、notification 和 category。
4. Swift 优先做 demangle、符号残留、字符串邻近、调用点和断点验证；不要假设 selector 稳定存在。
5. WebView/Electron 目标要同时寻找 native bridge、IPC、JS bundle 和网络层。
6. GUI/图表/动态列表目标要观察运行态对象身份，而不只观察 selector 是否命中：
   - model item 是否带 date/id/code/key；
   - view-model/property 是否带 visible offset、length、total、axis、layout cache；
   - render 方法参数里的 index 是否只是 local index；
   - 对象是否会被复用、懒加载、缓存刷新或数据补全替换。
7. 输出可 hook 的最小点：入参、返回值、线程、对象生命周期和副作用。

## 运行态身份恢复

对 Objective-C 容器对象，优先用只读探针恢复结构：

```text
NSDictionary/NSMutableDictionary: keys, date/id/code, nested array/dict
NSArray/NSMutableArray: count, target item index, control item index
NSNumber/NSString: business key 与 range/offset 字段
```

如果 View 层只提供 `index`，必须追问：

```text
index 是 global index 还是 visible local index？
local index 对应哪个 model item？
visible offset 叫什么？
数据补全后 global index 是否变化？
控制样本是否紧邻目标，且能持续保持非命中？
```

无法回答这些问题时，不要把 View 层 hook 结论写成稳定 Green。

## Green

```text
runtimeEntryCandidateOk=true
hookPointType=objc/swift/c/electron/webview/xpc
inputOutputObservationPlan=true
sideEffectsDeclared=true
modelIdentityObserved=true/false
viewIndexStabilityChecked=true/false
```
