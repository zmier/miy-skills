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
6. 输出可 hook 的最小点：入参、返回值、线程、对象生命周期和副作用。

## Green

```text
runtimeEntryCandidateOk=true
hookPointType=objc/swift/c/electron/webview/xpc
inputOutputObservationPlan=true
sideEffectsDeclared=true
```

