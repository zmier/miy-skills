# Third-Party Adoption Register

Treat every external Skill or MCP as a candidate implementation.

| Project | Capability | License reviewed | Classroom evaluation | Decision | Notes |
|---|---|---:|---|---|---|
| ElonJask/reqable-mcp | Reqable Report Server 接收、流量检索、HAR 补录与代码草稿生成 | yes, MIT | passed, Bilibili Day17 | wrap | 固定 `0.3.2`；真实链路新增 105 条请求；Reqable 仍负责代理、证书和 GUI；不得提交真实 HAR、Cookie 或 Token |
| hyperb1iss/hyperdroid-skill | ADB、Fastboot 与 Android 设备调试知识 | yes, MIT | not run | research | 借鉴设备诊断分层，不直接引入刷机能力 |
| CursorTouch/Android-MCP | ADB、UI、截图与 shell 控制 | yes, MIT | not run | research | 候选设备 MCP，达到 D2 后评测 |
| mobile-next/mobile-mcp | Android/iOS 真机自动化 | not yet | not run | research | 候选跨平台设备 MCP |
| JuanCF/scrcpy-mcp | ADB、scrcpy、视觉与设备控制 | yes, MIT | not run | research | 适合后续 UI 操作与截图 |
| incogbyte/android-reverse-engineering-claude-skill | ADB 与 Frida 环境准备 | not yet | not run | research | 借鉴 setup-frida.sh 的版本匹配流程 |
| Fausto-404/ai-mobile-reverse-skills | workflow architecture | no | not run | research | Review stage artifacts and routing |
| Rudra-ravi/frida-skills | Frida atomic skills | no | not run | research | Review relevant skill per Day |
| incogbyte/android-reverse-engineering-claude-skill | APK/API reconnaissance | no | not run | research | Compare with Day17-18 |
| mrexodia/ida-pro-mcp | Native static analysis MCP | no | not run | research | Candidate tool adapter |
| zinja-coder/jadx-ai-mcp | Android static analysis MCP | no | not run | research | Candidate tool adapter |
| zhkl0228/unidbg | Native emulation MCP/debugger | no | not run | research | Evaluate after Day24 |

Decision values: `research`, `depend`, `wrap`, `rewrite`, `reject`.
