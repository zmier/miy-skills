# macOS Protection Reds

## Red 分类

- `sip-amfi-blocked`：SIP、AMFI 或系统策略阻止注入、调试或写入。
- `hardened-runtime-blocked`：Hardened Runtime 拦截 dylib 注入、JIT、debug 或 unsigned executable memory。
- `library-validation-blocked`：Library Validation 拒绝未签名或签名团队不匹配的 dylib。
- `code-signature-invalid`：重打包、patch 或修改 bundle 后签名失效。
- `entitlement-missing`：缺少 `com.apple.security.*`、network、automation、keychain access group 等 entitlement。
- `sandbox-container-boundary`：App Sandbox 或 group container 导致文件、网络、helper 访问不同。
- `tcc-permission-blocked`：Accessibility、Automation、Screen Recording、Files and Folders、Full Disk Access 等 TCC 权限阻断。
- `keychain-access-denied`：Keychain access group、Secure Enclave 或 user presence 约束阻断。
- `anti-debug-detected`：`ptrace`、`sysctl`、`task_for_pid`、debugger 检测或 timing 检测。
- `symbol-resolution-failed`：Swift 符号 stripped、ObjC 动态 selector、C++ name mangling 或 ASLR 处理失败。
- `xpc-boundary-missed`：真实业务在 XPC service/helper/login item，而不是主进程。
- `network-trust-blocked`：TLS pinning、mTLS、自定义 trust store 或 HTTP/3/QUIC 导致代理不可见。

## 处理原则

先做只读证据：`codesign`、`otool`、`plutil`、`log stream`、进程树、打开文件、网络连接和 UI 状态。只有在 TASK 授权边界明确时，才进入重签名、patch、注入或绕过类实验。

保护 Red 的 Green 必须是分层的：

```text
protectionLayerIdentified=true
minimalReadOnlyEvidence=true
authorizedMitigationDeclared=true
postMitigationSmokePassed=true
businessGreenSeparatelyVerified=true/false
```

