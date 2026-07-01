---
name: diagnose-macos-protection
description: 诊断授权 Mac App 逆向中的 macOS 保护和环境 Red，包括 SIP、AMFI、Hardened Runtime、Library Validation、code signing、notarization、entitlements、App Sandbox、TCC、Keychain、anti-debug、task_for_pid、TLS pinning、mTLS 和 helper/XPC 边界。
---

# Diagnose macOS Protection

## 工作流

1. 读取 `references/macos-protection-reds.md`。
2. 收集只读证据：`codesign`、entitlements、`otool`、`spctl`、`log stream`、crash log、进程树、sandbox container、TCC 状态。
3. 将 Red 归类到保护层，不把所有失败都写成 hook 失败。
4. 判断授权内的最小缓解：只读观察、换 attach 进程、helper 定位、重签名、禁用 library validation、Frida Gadget、lldb、harness 或 human gate。
5. 每个缓解动作都必须有恢复方式、post-smoke 和业务 Green 分离。

## Debug 副本重签

若 Frida/lldb attach 被 Hardened Runtime、Library Validation、缺少 `get-task-allow`、task_for_pid 或签名策略阻断，且用户授权允许修改实验环境，优先使用 TASK cache 中的副本做调试重签：

```text
原始 .app 只读保留
→ 复制到 TASK cache
→ 记录原签名、entitlements、bundle id 和 Mach-O hash
→ 生成最小 debug entitlements
→ 对副本 codesign
→ attach smoke
→ 业务 hook/UAT 单独验证
```

禁止把“副本可 attach”写成业务 Green。若证书、license、GUI 授权或 TCC 需要人类操作，使用 human gate/通知记录，不在 workflow 保存密钥或真实 license。

## Green

```text
protectionLayerIdentified=true
readOnlyEvidenceCaptured=true
authorizedMitigationDeclared=true
postMitigationSmokePassed=true
businessGreenSeparatelyVerified=true/false
originalAppUntouched=true/false
debugCopyPathRecordedInTask=true/false
```

不得把保护缓解成功写成业务复现成功。
