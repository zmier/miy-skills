---
name: workflow-mac-app-reverse
description: Mac App 逆向复合 Skill。用于在授权边界内编排 macOS .app/Mach-O/dylib/framework/Objective-C/Swift/Electron/XPC/CFNetwork/Keychain/TCC/沙箱/签名保护相关逆向任务，建立证据台账，组织静态/动态分析、Frida/lldb/hook/trace/replay/oracle、运行态代发、Red 分层、TASK 沉淀和迁移评测。
---

# Mac App Reverse Workflow

## Purpose

维护一套可迁移、可复用的 Mac App 逆向 Workflow。这里保存能力本体，不保存某次目标 App 的过程、证据、日志、样本、数据库、账号态或验收结果。

## Structure

```text
workflow-mac-app-reverse/
├── SKILL.md
├── skills/
├── integrations/
├── references/
├── scripts/
├── src/
├── tests/
├── third-party/
└── tools/
```

- `skills/`：总编排和可复用子 Skills。
- `integrations/`：MCP、Frida、lldb、mitmproxy、Reqable、IDA/Ghidra 等能力清单与适配决策。
- `references/`：workflow 级参考资料、路线阶梯、macOS 保护 Red 分类和跨 Skill 决策依据。
- `scripts/`：跨案例使用的确定性命令。
- `src/`：通用 Python/Node 工具。
- `tests/`：只测试 Workflow 自身，不读取真实 TASK。
- `third-party/`：外部工具、脚本和 Skill 的采用记录。
- `tools/`：由 workflow 管理且可重新获取的运行工具。

## Directory Boundary

```text
Mac 逆向 TASK
├── 目标、授权边界、状态、日志、证据、fixture、Evaluation、UAT
└── 案例专用 Hook、Frida 脚本、lldb 命令、harness 与构建命令
        ↓ 提炼稳定能力
workflow-mac-app-reverse
├── Skills、通用脚本、模板、依赖和中性测试
└── 不反向依赖任何具体 TASK
```

不复制目标 `.app`、Mach-O、dylib、framework、反编译数据库、Keychain dump、账号态、Cookie、Token、完整 HAR 或案例日志到 Workflow。Skill 可以保留去个案化的决策规则、最小示例和 checklist；原始证据必须留在调用方 TASK。

## Growth Rule

```text
遇到一个 Mac App TASK
→ 在 TASK 中独立复现 Red 与最小 Green
→ 记录 Evaluation、UAT、失败证据和授权边界
→ 识别可复用决策或操作
→ 更新或创建 Skill / reference / script
→ 运行 Workflow 自身回归
```

真实项目反哺时必须写清：

```text
之前 workflow 缺什么
本轮 TASK 观察到什么 Red
最小 Green 是什么
抽象后加入哪里
哪些内容仍然留在 TASK
迁移状态是 structural-green 还是 forward-test-green
```

## Mac Route Ladder

Mac App 逆向不只有“外部脚本复现成功”一种 Green。总编排时先声明当前路线：

| 路线 | Mac 形态 | Green | 典型 Skill |
|---|---|---|---|
| M0 观察 | UI、进程、文件、日志、网络、权限只读观察 | 目标行为和候选通道可证据化 | `inspect-mac-app-bundle` / `capture-mac-app-traffic` |
| M1 外部重放 | Python/Node/curl 直接构造 HTTP/RPC/本地输入 | 目标服务或本地逻辑接受外部请求 | `reproduce-mac-app-request` |
| M2 运行态代算 | Frida/lldb 调 App 内函数生成字段或状态 | 字段、对象或中间值 oracle 可用 | `hook-mac-app-frida` / `trace-mac-app-lldb` |
| M3 离线 harness | 本机加载 Mach-O/dylib/framework 或重建算法 | 离线函数可稳定执行 | `analyze-macho-static` / `build-mac-native-harness` |
| M4 App 运行态代发 | App 内 CFNetwork/WKWebView/Electron/XPC/自研通道代发 | App 发出业务动作，外部只调度和落盘 | `dispatch-via-mac-app-runtime` |
| M5 服务化封装 | Frida RPC、注入 dylib、本地 helper、XPC/LaunchAgent | 长驻、allowlist、可恢复、可观测 | `dispatch-via-mac-app-runtime` |

选择 M4 时不要写成 M1 成功。必须明确：

```text
externalRequestSentByPython=false
liveRequestSentByMacApp=true
login/keychain/cert/session/runtime state held by App
```

选择 M5 时必须先完成最小注入或 attach smoke，再进入 action server：

```text
Red smoke/UAT
-> process attach/inject smoke
-> target runtime ready
-> ObjC/Swift/C symbol resolved
-> action list / health / unknown reject
-> dry-run
-> low-frequency real smoke
```

M5 的 attach/inject Green 不等于业务 Green。P1 只证明工具能进入目标运行态；P2 证明受控 action server 可用；P3 才允许低频业务 smoke；P4 以后才能接请求池、dashboard、通知和长跑。

## Mac Protection Red 分类

Mac App 常见 Red 不应混成“hook 失败”：

```text
SIP / AMFI / Hardened Runtime
code signing / notarization / entitlements
App Sandbox / container / group container
TCC privacy permission
Keychain access group / Secure Enclave
Library Validation / DYLD_* ignored
anti-debug / ptrace / sysctl / task_for_pid denied
Swift symbol stripped / ObjC selector dynamic
XPC service boundary / helper process boundary
TLS pinning / mTLS / custom trust
login/session/cookie/window/rate limit
```

先把 Red 归层，再决定是只读观察、签名重打包、Frida attach、lldb trace、dylib injection、App 运行态代发，还是保持 human gate。不要为了证明 M1 而破坏授权边界或服务端压力条件。

## Business Network And Corpus Mode

当目标从“复现一个请求”变成“理解一组页面动作、App 内 RPC 或持续构建数据/语料”时，进入项目模式：

```text
代理可见性基线
→ 网络通道候选树
→ CFNetwork / NSURLSession / WKWebView / Electron / XPC / WebSocket / gRPC / native socket 出口确认
→ 页面或动作接口地图
→ 单 action 工具化
→ 业务复合动作
→ 分接口 request pool
→ 批量限速与断点恢复
→ 覆盖率和服务端窗口声明
```

接口 Green 之后，不要立刻吃完整窗口。先建立：

```text
request pool: pending/running/done/failed/partial
bucket quota: 每个接口独立窗口和冷却
due task queue: 到期 bucket 只吐出一个或少量小任务
worker: 按队列顺序执行，可复用 App 运行态 session
checkpoint: 每个实体或每页完成后立即落盘
dashboard: 展示 live evidence，而不是历史错误
human gate: 登录、TCC、验证码、Keychain、前台 UI 等人类确认点
```

## Evidence Promotion

案例 TASK 的 raw 数据、日志和真实业务 ID 不进入 Workflow，但以下内容必须在阶段 Green 后抽象：

- Red 的可复用分类；
- 从 Red 到 Green 的最小实验；
- 路线选择规则；
- macOS 保护、运行态、服务端边界；
- Frida/lldb/hook/injection 的工程坑和恢复 runbook；
- 可迁移模板或 checklist；
- 人机合作状态机、通知触发条件和 dashboard 摘要原则。

## Project Reverse Knowledge Base

长周期 Mac App 逆向项目不应只依赖 TASK log 和 raw outputs 回看。若分析会持续跨多个阶段，项目目录应建立 living knowledge base，例如：

```text
docs/reverse-knowledge/
├── README.md
├── 01-static-inventory.md
├── 02-runtime-data-model.md
├── 03-hook-points-and-decisions.md
└── 04-open-questions.md
```

推荐承接内容：

- class、selector、property、ivar、framework、字符串和资源候选；
- Mach-O/ObjC/Swift 静态地址、IMP offset、IDA/Ghidra 观察摘要；
- 运行态对象结构、model/view-model/view 分层、字段语义和数据路径；
- hook 点、trace 点、已否定路线、UAT 必检项和恢复方式；
- open questions、置信度、来源文件和下一步探针。

边界要求：

```text
raw evidence -> TASK
整理后的事实/候选/状态 -> docs/reverse-knowledge
可迁移规则 -> workflow/reference/skill
```

知识库必须显式区分 `confirmed`、`static`、`runtime`、`candidate`、`open`、`deprecated`，避免把候选写成已确认事实。不要复制目标 app、反编译数据库、完整日志、账号态、真实 token、完整 HAR 或案例专用大样本。

## GUI / Chart Rendering Pattern

AppKit、CorePlot、SwiftUI、WKWebView canvas 或自研图表这类动态渲染目标，不要默认把 View 层坐标、cell index、visible index、draw index 当作业务身份。总编排时先要求静态和运行态共同回答：

```text
business identity: date/id/key/item
model layer: 原始数据项或可变中间对象
view-model/property layer: visible range、offset、length、axis、layout cache
view/render layer: draw call、fill、color、cell reuse、layer reuse
```

若 View 层 index 会随滚动、缩放、懒加载、缓存刷新或数据补全变化，优先选择 model-marker 路线：

```text
静态确认 MVC/MVVM/渲染链路
→ 动态只读观察 model item 与 visible range
→ 在授权副本中给目标 model item 写临时 marker
→ 渲染层按 marker + visible offset 计算 local index
→ 控制样本持续验证 shouldPatch=false
→ UAT 覆盖滚动、缩放、数据补全和回看
```

详细规则见 `references/mac-ui-rendering-model-patterns.md`。这条规则目前为 `structural-green`：已在一个授权 TASK 中达到最小 Green 和人工 UAT Green，但尚未跨第二个 Mac App forward-test。

## Shared Environment

优先使用系统自带只读工具建立基线：

```bash
file <target>
otool -L <target>
codesign -dv --verbose=4 <target>
plutil -p <Info.plist>
log stream --predicate 'process == "Target"'
```

动态工具按 TASK 需要声明版本和来源。Frida、lldb、IDA/Ghidra、mitmproxy/Reqable、class-dump、jtool2、Hopper 等工具的真实输出留在 TASK；workflow 只保存中性脚本和规则。
