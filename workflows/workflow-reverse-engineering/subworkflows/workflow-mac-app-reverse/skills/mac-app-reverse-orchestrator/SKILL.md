---
name: mac-app-reverse-orchestrator
description: Mac App 逆向总编排 Skill。用于在授权边界内把目标 .app/Mach-O/Objective-C/Swift/Electron/XPC/网络/Keychain/TCC 任务路由到 Mac 子 Skills，选择 M0-M5 路线，维护证据台账、Red 分层、UAT、TASK 沉淀和迁移状态。
---

# Mac App Reverse Orchestrator

## 工作流

1. 确认目标、授权边界、禁止动作、完成标准和停止条件。
2. 建立 TASK 证据台账，声明 raw 证据、脱敏摘要、UAT 和日志位置。
3. 读取 `references/mac-reproduction-ladder.md`，选择 M0-M5 路线。
4. 先调用 `inspect-mac-app-bundle` 建立 bundle、Mach-O、helper、XPC、entitlement、sandbox 基线。
5. 若目标是协议或业务请求，调用 `capture-mac-app-traffic` 建立通道候选树。
6. 若需要定位代码，调用 `analyze-macho-static` 和 `analyze-objc-swift-runtime`。
7. 若需要运行态 oracle，调用 `hook-mac-app-frida` 或 `trace-mac-app-lldb`。
8. 若 M1/M3 被运行态阻塞，转入 `dispatch-via-mac-app-runtime`，不要强行写成外部复现。
9. 若遇到签名、沙箱、TCC、Keychain、Hardened Runtime、anti-debug 或注入失败，调用 `diagnose-macos-protection`。
10. 阶段 Green 后沉淀去个案化规则到 workflow，原始证据留在 TASK。

## Green 分层

```text
bundleBaselineOk
channelCandidateOk
staticLocationOk
runtimeOracleOk
requestReplayOk
appRuntimeDispatchOk
serviceModeOk
corpusSchedulerOk
```

不得把低层 Green 冒充高层 Green。

