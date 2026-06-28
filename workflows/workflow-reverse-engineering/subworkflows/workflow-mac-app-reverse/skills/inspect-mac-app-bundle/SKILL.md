---
name: inspect-mac-app-bundle
description: 在授权 Mac App 逆向任务中建立 .app bundle、Info.plist、Mach-O、framework、dylib、helper、XPC service、LaunchAgent、entitlements、sandbox、签名和进程基线。用于 M0 只读观察和后续静态/动态分析路由。
---

# Inspect Mac App Bundle

## 工作流

1. 确认目标路径、版本、来源、授权边界和是否允许启动目标。
2. 记录 bundle 树：`Contents/MacOS`、`Frameworks`、`PlugIns`、`XPCServices`、`Helpers`、`Resources`。
3. 读取 `Info.plist`：bundle id、executable、URL scheme、document type、helper 声明。
4. 对主程序和关键二进制运行 `file`、`otool -L`、`otool -l`、`nm` 或等价工具。
5. 读取签名和 entitlement：`codesign -dv --verbose=4`、`codesign -d --entitlements :-`。
6. 判断是否 sandbox、hardened runtime、library validation、network entitlement、automation/keychain 权限。
7. 启动后记录进程树、helper/XPC、打开文件、网络连接和 unified logging baseline。
8. 输出候选运行时：ObjC、Swift、C/C++、Rust、Electron、Qt、Java、Python、Go、WebView。

## 输出

```text
bundleBaselineOk=true/false
mainExecutable=<path>
runtimeCandidates=[...]
helperProcesses=[...]
xpcServices=[...]
entitlementsSummary=<redacted>
protectionCandidates=[...]
nextSkills=[...]
```

不得把 bundle 基线写成业务 Green。

