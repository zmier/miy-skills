---
date: 2026-06-18
type: reference
status: structural-green
scope:
  - workflow-reverse-engineering
---

# 平台与运行时路由

## 目的

父 workflow 不直接决定“用哪个工具干活”，而是先判断目标属于哪类运行时，再把任务路由给对应子 workflow。

核心原则：

```text
同一个逆向问题
→ 先抽象成目标、证据、红灯和 Green
→ 再根据平台选择工具
```

不要把 Android 的 Frida/JADX/Unidbg 直接套到 JS，也不要把 JS 的 DevTools/AST/Node 直接套到 Android。

## 路由表

| 目标形态 | 常见入口 | 首选子 workflow | 典型工具族 | 备注 |
| --- | --- | --- | --- | --- |
| Android App | APK、设备、抓包、App 运行态 | `subworkflows/workflow-android-reverse` | ADB、JADX、Frida、IDA、Unidbg、mitmproxy | Android 平台专属 |
| Web JS | URL、网页、bundle、接口请求 | `subworkflows/workflow-js-reverse` | DevTools、AST、Node、浏览器自动化、source map | 需要后续用图灵 JS 案例 forward-test |
| Hybrid / WebView / 小程序 | App 内页面、JSBridge、RPC | Android + JS 混合路由 | Frida + DevTools/Hook bridge | 先识别请求是否被 native 容器接管 |
| Windows Native | PE、DLL、桌面进程 | 未来 Windows 子 workflow | x64dbg、WinDbg、IDA、Frida | 尚未建立 |
| Unity | APK/EXE、GameAssembly、metadata | 未来 Unity 子 workflow | Il2CppDumper、IDA、Frida、dnSpy | 尚未建立 |
| WebAssembly | `.wasm`、JS 调 wasm | JS 子 workflow，必要时 native-like 分支 | wasm tooling、DevTools、runtime hook | 介于 JS 与 native 分析之间 |

## 判断顺序

1. 目标交付物是什么：请求、参数、算法、数据结构、交互动作、补环境结果，还是工具链？
2. 目标运行在哪里：App、浏览器、Node、WebView、native library、远程服务、混合容器？
3. 已知证据来自哪里：抓包、静态代码、动态日志、hook、调试器、运行态返回、服务端响应？
4. 当前红灯是哪一层：看不到流量、找不到代码、看不懂代码、hook 不上、复现不一致、服务端拒绝？
5. 该红灯是否平台专属：若是，路由到子 workflow；若不是，先用父级 reference/template 建立证据结构。

## Hybrid 特别规则

Hybrid 场景不能只按页面表象路由。

例如：

```text
页面看起来是 JS
→ 点击后 JS 调 native bridge
→ native 容器转成 RPC / mobile gateway / long connection
→ 普通 Web 抓包或 DevTools 可能看不到目标业务请求
```

这类任务应标为 `hybrid`，先建立父级证据台账，再同时考虑：

- JS 侧：定位 bridge 调用、入参、页面状态；
- Android 侧：定位 native bridge、RPC、App 运行态代发、网络通道。

## 完成标准

一次路由判断至少输出：

- `platform`: Android / JS / Hybrid / Windows / Unity / unknown；
- `runtime`: browser / node / app / webview / native / mixed；
- `goal`: 要复现或解释的终点；
- `current-red-light`: 当前卡点；
- `next-subworkflow`: 应进入的子 workflow 或父级通用模板；
- `reason`: 为什么这样路由；
- `fallback`: 如果这条路不通，下一条候选路线是什么。

