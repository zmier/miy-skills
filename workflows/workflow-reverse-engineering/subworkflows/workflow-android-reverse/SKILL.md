---
name: workflow-android-reverse
description: Android 逆向请求复现复合 Skill。用于在授权边界内维护可迁移、可复用的 Android 请求复现能力，编排 APK/DEX/SO/ART/JNI、Frida Java、ADB、Unidbg、抓包、hook、trace、replay、oracle、证据台账、课程来源追溯、TASK 回归和迁移测试。
---

# Android Reverse Workflow

## Purpose

维护一套可迁移、可复用的 Android 请求复现 Workflow。这里保存能力本体，不保存某次课程案例的过程、证据、日志与验收结果。

## Structure

```text
workflow-android-reverse/
├── SKILL.md
├── Makefile
├── pyproject.toml
├── package.json
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
- `integrations/`：MCP 能力清单与适配决策。
- `references/`：workflow 级参考资料、课程来源追溯、课程目录索引和跨 Skill 决策依据。
- `scripts/`：跨案例使用的确定性命令。
- `src/`：通用 Python 工具。
- `tests/`：只测试 Workflow 自身，不读取课程 TASK。
- `third-party/`：外部 Skills、MCP 与工具的采用记录。
- `tools/`：由 Makefile 管理且可重新获取的运行工具。

## Directory Boundary

```text
课程案例 TASK
├── 目标、状态、日志、证据、fixture、Evaluation、UAT
└── 案例专用 Hook、复现脚本与构建命令
        ↓ 提炼稳定能力
workflow-android-reverse
├── Skills、通用脚本、模板、依赖和中性测试
└── 不反向依赖任何具体课程 TASK
```

当前案例材料归属：

- B站 Day17/18：`../笔记包/Day 17-19 B站/TASK-Day17/`
- B站 Day19：`../笔记包/Day 17-19 B站/TASK-Day19/`
- Day21-Day23 知识迁移：`../笔记包/TASK-Day21-23知识迁移/`
- Day27 网络与抓包专题探索项目：`../笔记包/Day 27及以后/网络与抓包专题/PROJECT-Android目标业务网络通道识别/`
- Day24-Day26 Unidbg：`../笔记包/Day 24-26 unidbg/TASK-Day24-26-Unidbg复现/`

## Growth Rule

```text
学习一个 Day
→ 在对应课程 TASK 中独立复现
→ 记录 Evaluation 与失败证据
→ 先复现 Red；若 Red 未复现，记录环境差异而不是虚构修复
→ 识别可复用决策或操作
→ 更新或创建 Skill
→ 运行 Workflow 自身回归
```

不复制课程图片、APK、so、反编译数据库或案例日志到 Workflow。Skill 可以保留经过抽象的决策规则和最小示例，但原始证据必须留在调用方 TASK。

探索性项目中的真实反馈也可以反哺 Workflow，但必须先在 TASK 中留下证据，再抽象成规则。例如服务端分页窗口、账号冷却、同事反馈压力、非交互 Frida session 不稳定、长跑采集需要真实 TTY/伪终端、批量任务需要单实体隔离与断点恢复，以及 R3 被账号态、设备态、签名态、风控态或连接态阻塞时转向 `dispatch-via-app-runtime` 的 R4-A/R4-M App 运行态代发路线，属于可迁移的操作护栏；具体账号、offset、业务 ID、真实响应和日志文件仍留在 TASK。

真实项目反哺时必须写清：

```text
之前 workflow 缺什么
本轮 TASK 观察到什么 Red
最小 Green 是什么
抽象后加入哪里
哪些内容仍然留在 TASK
迁移状态是 structural-green 还是 forward-test-green
```

若发现来自对话中的共同判断，例如“长跑不应每条都重建 Frida session，而应长会话复用并单条 checkpoint”，先按 `course-driven-skill-engineering` 的 `dialogue-insight / field-discovery` 处理：TASK 保存原始讨论和证据，workflow 只接收去个案化后的状态机、护栏和验收标准。

体系级 TDD 与回归测试遵循 `references/tdd-regression-test-system.md`。修改 workflow、子 Skill、miku 运行面板或真实 TASK 长跑策略时，应先区分三圈测试边界：

```text
workflow tests：通用能力契约；
miku tests：工具面板和运行状态；
TASK tests：真实业务目标、SQLite 队列、UAT 和证据。
```

默认测试不得发送真实业务请求或保存真实 raw 响应；需要真机、登录、服务端窗口或人工确认的验证必须写入对应 TASK 的 Manual UAT。

## Android Route Ladder

Android 请求复现不只有“Python 外部请求成功”一种 Green。总编排时先声明当前路线：

| 路线 | Android 形态 | Green | 典型 Skill |
|---|---|---|---|
| A0 观察 | 抓包、UI、日志、hook 只读事件 | 目标行为和候选通道可证据化 | `capture-android-traffic` / `identify-android-business-network-channel` |
| A1 外部重放 | Python/Node 直接构造 HTTP/RPC | 服务端接受外部请求 | `android-request-reproduction` |
| A2 运行态代算 | Frida RPC 调 Java/JNI 生成字段 | 字段 oracle 可用 | `export-frida-rpc` / `resolve-android-dynamic-field` |
| A3 离线 harness | Unidbg/自建 Android host 跑 so/jar | 离线函数可用 | `run-so-with-unidbg` / `host-android-native-library` |
| A4 App 运行态代发 | App 内 bridge/RPC/mobilegw/长连接代发 | App 发出业务请求，Python 调度落盘 | `dispatch-via-app-runtime` |
| A5 服务化封装 | Xposed/Sekiro/受控 RPC 服务 | 长驻、allowlist、可恢复 | `xposed-sekiro-runtime-dispatch` |

选择 A4 时不要写成 A1 成功。必须明确：

```text
externalRequestSentByPython=false
liveRequestSentByApp=true
账号态/设备态/签名态/连接态由 App 运行态持有
```

选择 A5 时必须先完成 P1 module-loaded smoke，再进入 action server：

```text
Red smoke/UAT
-> 最小 Xposed 模块
-> LSPosed/Zygisk/Manager/scope
-> logcat module-loaded
-> classloader-ready
-> restart smoke
```

A5 的 P1 Green 不等于业务 Green。P1 只证明模块能加载到目标 App 运行态；P2 以后才能做 `health/echo/unknown reject`，P3 以后才能做低频业务 smoke。若目标 App 多进程加载模块，P2 必须先加入 `ProcessRouter`，避免 action server 在 `:push`、`:gpu_process` 或 sandbox 进程重复注册。

进入 A5/Xposed 模块构建时，默认使用 workflow 固定工具链，不从系统 PATH 临时猜版本。TASK 里的 Xposed/LSPosed 模块 `Makefile` 应优先声明：

```makefile
WORKFLOW_TOOLS ?= /Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering/subworkflows/workflow-android-reverse/tools
JAVA_HOME ?= $(WORKFLOW_TOOLS)/jdk17/Contents/Home
GRADLE ?= $(WORKFLOW_TOOLS)/gradle-8.7/bin/gradle
ANDROID_HOME ?= /opt/homebrew/share/android-commandlinetools
ANDROID_SDK_ROOT ?= $(ANDROID_HOME)
```

不要因为 `gradle` 不在系统 PATH 就重新安装或到处搜索；先检查 `workflow-android-reverse/tools/gradle-8.7/bin/gradle` 和对应 `jdk17`。若 TASK 需要升级 Gradle/JDK，必须在 TASK 记录 Red/Green 证据，再反哺 workflow 工具链版本。

A5 的 P3 也不等于长跑 Green。把 Frida RPC 或临时 Hook 迁移为 Xposed/Sekiro action 时，必须先做“单 action 低频 smoke”，不要直接接 SQLite 请求池、dashboard 或批量调度：

```text
Frida oracle
-> allowlist action
-> dry-run 不触发业务请求
-> real=1 单条低频 smoke
-> App ClassLoader / RPC proxy / requestData / business-ok 四层排错
-> 有效样本 + 业务失败样本双验收
-> 再迁移下一个 action 或接请求池
```

其中 Frida oracle 指已经在当前 TASK 中独立跑通的 `operationType + requestData + options/map + 响应结构`，不是课程笔记或猜测。迁移时优先完全对齐 oracle，再重构为 Java/Kotlin/Xposed 代码。若 real smoke 失败，按层分诊：

- action server 空响应或 App crash：先补 `Throwable` 兜底和进程稳定性，不判定业务失败；
- `ClassNotFoundException` / 类型找不到：检查目标 App `ClassLoader` 是否注入到 action 线程；
- 反射签名失败：不要硬编码 exact signature，扫描兼容 overload 或改用稳定接口；
- RPC 异常或服务端业务码：回到 requestData、运行态上下文和业务样本，不先接长跑；
- transport 成功但业务 `success=false`：必须返回业务 `ok=false`，不能把请求发出误报为业务成功。

单 action P3 的 Green 至少包含：

```text
dryRunPassed=true
businessRpcTriggered=true
sensitiveHeadersReturned=false
transportOk 与 businessOk 分开
有效样本返回核心业务字段
业务失败样本能保持 ok=false
```

只有当每个基础 action 都完成上述 smoke 后，才允许进入请求池 adapter、miku 状态面板、飞书通知和长跑限速策略。

A5 的 P4/P5/P6 必须继续分层，不得把 P3 单 action 成功冒充为生产长跑成功：

```text
P4 request-pool adapter：已有业务 worker 支持 transport switch，Xposed 只替换 App 内代发通道；
P5 supervised state-changing action：设备态/缓存态/登录态等高危变更必须 prepare/execute 分离、显式 confirm、可回滚或可重装恢复，并在真实 1009 或等价 Red 后才允许触发；
P6 production long-run：supervisor、runtime heartbeat、业务 runtime、网络、bucket quota、SQLite checkpoint、human gate、post-reset smoke 和通知全部纳入状态机。
```

P4 Green 至少包含：

```text
fridaOracleStillAvailable=true
xposedActionListOk=true
transportSwitchExplicit=true
requestPoolWorkerUnchangedExceptTransport=true
smallWindowRealRunPassed=true
raw/simplified 策略不因 transport 改变
```

P5 Green 至少包含：

```text
stateChangingActionAllowlisted=true
preparePassed=true
executeRequiresConfirm=true
recentRedEvidenceRequired=true
businessRpcTriggered=false
sensitiveHeadersReturned=false
postResetSmokePassed=true
fallbackOrManualRecoveryDeclared=true
```

P6 Green 至少包含：

```text
supervisorAlive=true
runtimeHeartbeat=true
networkHealthChecked=true
businessRuntimeReady=true
bucketQuotaPerInterface=true
checkpointPerEntity=true
1009/deviceReset/humanGate 分层
dashboardReadsLiveEvidenceBeforeHistoricalError=true
newRedCreatesTASKOrLogBeforeWorkflowChange=true
```

如果 P6 长跑依赖设备态重置、App 前台保活或目标 runtime 入口，不要写成“完全无人值守”。应声明：

```text
machineSelfRepairable=哪些红灯可自动修；
humanGate=哪些状态需要人类确认；
postGateSmoke=人类动作后必须跑什么 smoke；
stopCondition=服务端压力、授权边界、验证码或明确拒绝时停止。
```

## 业务网络与语料项目编排

当目标从“复现一个接口”变成“理解一组页面接口或构建语料库”时，进入业务网络项目模式：

```text
代理可见性基线
→ 网络通道候选树
→ bridge/RPC/mobilegw/长连接/native 出口确认
→ 页面接口地图
→ 单 RPC 工具化
→ 业务复合接口
→ 分接口请求池
→ 批量限速与断点恢复
→ 覆盖率和服务端窗口声明
```

此时不要用单个 `request-construction-ledger` 承载全部内容。应拆分：

- 页面接口地图：页面动作、operationType、入参、主实体、证据；
- 接口卡片：基础 RPC 和复合接口；
- corpus contract：主键、source/evidence、去重、覆盖率；
- request pool：状态机、partial reasons、failure policy；
- batch report：成功、失败、跳过、窗口、服务端压力和下一步。

如果采集依赖 App 运行态、Frida RPC、bridge/RPC 或长连接，必须额外拆出运行态长跑层：

- runtime heartbeat：App 进程、前后台、目标 runtime、网络和 Frida server 是否健康；
- session lifecycle：`attach/load/call` 是否可持续，`script destroyed` 是否能就地重建；
- business bucket：每个接口独立窗口、冷却、失败原因和恢复策略；
- human gate：登录、验证码、设备态重置后等待人工确认等需要人类介入的门；
- human notify：环境红灯、修复失败、等待人工、长跑完成等必须通报给操作者；
- dashboard：只展示进度、下一轮、窗口压力和关键摘要，不把机器详细日志直接铺给人看。

### 容器 RPC 的短窗口插桩

当普通代理只看到统一网关、CONNECT、静态资源、埋点或非目标流量，而目标业务疑似运行在小程序、WebView、Nebula、XRiver、mPaaS 或 mobilegw 容器内时，不要先把问题理解成“抓包失败”。优先进入 A0 只读观察，使用“短窗口插桩 + 人类单动作”的方式把页面动作映射到 RPC operation。

推荐节奏：

```text
确认 App / 小程序页面可用
-> 开 10-15 秒 Frida/Xposed 只读窗口
-> 人类只做一个目标动作：进入页面、点击 tab、下拉刷新、点详情、点查看更多
-> 记录 bridge request / RPC request / compact response hint
-> 提取 operationType、requestData、主实体 ID、分页字段和响应结构
-> 再决定是否进入接口卡片、App 内主动调用或请求池
```

短窗口要遵循“小、准、可复现”：

- 每个窗口只验证一个页面动作，不把多个动作混在一起；
- 默认 10-15 秒，动作完成后立刻停，不长时间挂全量 hook；
- 输出写入调用方 TASK 的 `outputs/*window*.log`，并在 `logs/LOG.md` 记录 ReAct；
- 只打印必要结构和脱敏摘要，不把 Cookie、session、token、Did、utdid、miniwua、Sign 等完整值写入 workflow 或总结文档；
- 如果人类动作可能触发多条 RPC，先按时间、operationType、requestData、响应主实体和 UI 变化做候选排序，再进入响应侧或主动调用验证。

优先 hook 层级：

```text
DefaultNativeBridge.sendToNative
BridgeDispatcher.dispatch
RpcBridgeExtension.rpc
DefaultBridgeCallback.sendJSONResponse
SimpleRpcService.executeRPC
```

如果抽象 bridge/RPC 层不命中，或只看到 `name=rpc` 但没有最终出网信息，再向下追：

```text
RpcInvoker.invoke
HttpCaller.call
HttpManager.execute
RpcHttpWorker.call / executeRequest / executeHttpClientRequest
```

对 mobilegw/mPaaS 类业务，要特别区分：

```text
统一 URL = https://mobilegw.alipay.com/mgw.htm
业务接口 = Operation-Type / operationType
业务请求体 = requestData / JSON body
业务成功 = 响应中的 success/resultCode/核心业务字段
```

拿到 `mobilegw` URL 只说明出网链路确认，不等于 A1 外部重放成功。若登录态、设备态、签名态、风控态或连接态由 App 运行态持有，应把 Green 写成：

```text
route=A4-observed
externalReplayReady=false
operationTypeConfirmed=true
requestDataShapeConfirmed=true
responseShapeConfirmed=按实际证据填写
```

短窗口之后的最小交付物：

```text
页面动作 -> operationType 映射
入参字段与分页字段
响应主实体与关键 ID
候选接口排序与排除理由
下一步 Green：接口卡片 / App 内主动调用 / 请求池 / 网络出口定位
```

### 接口 Green 后的调度层

单个 App 内 RPC 或 Xposed/Sekiro action 跑通后，不要立刻把一个接口的一整个窗口吃满。长跑语料任务应先建立“请求池 -> 到期任务队列 -> worker -> checkpoint -> dashboard”的调度层：

```text
request pool: pending/running/done/failed/partial
bucket quota: 每个接口独立窗口和冷却
due task queue: 到期 bucket 只吐出一个或少量小任务
worker: 按队列顺序执行，可复用运行态 session
checkpoint: 每个实体或每个页完成后立即落盘
dashboard: 展示 live evidence，而不是历史错误吓人
```

默认策略是“公平性先于并发”：先用小任务 FIFO/round-robin 让 answer detail、top comment、nested reply 等 bucket 都有机会推进；只有在 UAT 证明稳定后，再提高单任务批量或引入并发。否则一个 bucket 的大窗口会长期独占 worker，让其他已到期接口看起来“可运行但不调度”。

小任务大小应可配置，默认可以是 1 条实体/页；提高吞吐时再按真实 crash、1009、checkpoint 成本和服务端压力调整。调度器必须把以下状态分开：

```text
bucket due but another worker running
bucket blocked by own quota
bucket blocked by environment red
bucket blocked by human gate
historical 1009 already cleared
```

不要把这几层混成一个 `failed`。例如：

```text
业务 1009 / 服务端窗口 != Frida session lost
App native crash != 请求参数错误
设备态重置后等待登录 != 批量任务失败
接口 A 的窗口 != 接口 B 的窗口
```

如果普通代理只看到非目标流量，不要停在抓包工具排障。优先判断：

```text
是否系统代理不可见
是否 WebView / 小程序 bridge
是否 mPaaS / mobilegw
是否长连接 / gRPC / WebSocket
是否 UDP / QUIC
是否 native socket / Cronet / 自研网络栈
```

## 服务端窗口与设备态

服务端拒绝不自动等价于算法错误。Android 项目中常见限制维度：

```text
账号态
设备态
安装实例
安全 SDK 缓存
Cookie / session
Did / apdidToken / utdid
miniwua / Sign / authorization
连接态 / 长连接 session
频率窗口 / 分页窗口
```

判断优先级：

1. 先最小化业务参数，确认不是普通入参错误。
2. 再判断同账号换设备、同设备换账号、重启 App、重装 App、清理缓存等对照。
3. 若字段可能属于同一设备态 bundle，不要后置乱改单个字段；应只读溯源并让 App/安全 SDK 自刷新。
4. 若进入批量采集，必须分接口 bucket 记录限制，不把 answer detail、comment、nested reply 混成一个窗口。
5. 服务端压力反馈、验证码、明确拒绝或授权边界变化时停止，不通过提高频率、换账号、代理池继续推进。

对频率窗口的探索只允许作为受控研究策略，不作为绕过策略。可以记录窗口假设、最小实验、冷却时间、按接口分桶的安全预算和停止条件；但一旦收到服务端压力反馈、明确拒绝、验证码或授权边界变化，应停止或降级为离线分析。

当需要人为协作时，总编排应优先设计“人机合作状态机”：

```text
机器能自修 -> 自动修复并继续
机器不能自修但可诊断 -> 给人类通报需要做什么
人类完成后 -> smoke / probe 恢复
恢复失败 -> 回到对应 Red 分支，而不是盲目重试
```

## 交互验证与滑块处理

滑块、验证码和交互验证不是普通请求失败。它们通常位于服务端风控状态、App UI、运行态代发和长跑 supervisor 的交叉处。遇到 `1009`、`interactive_verification_waiting`、验证页、滑块页或评论/详情采集突然停在人工验证时，先把它归入独立 Red：

```text
business RPC ok before
-> service requires interactive verification
-> App presents H5/WebView/native verification UI, or server only returns waiting state
-> solve / human gate / post-smoke
-> resume request pool
```

不要把这类 Red 混成参数错误、普通限速、Frida session 丢失或 App crash。处理顺序：

1. 先识别验证形态：
   - H5/WebView 滑块；
   - native View 滑块；
   - 系统 WebView / 小程序容器内验证页；
   - 服务端返回验证态，但前台暂未出现可操作页面。
2. 先做只读证据：
   - UI dump、截图、logcat、Activity/Fragment 路径；
   - Xposed/Frida hook `Activity.onResume`、`onWindowFocusChanged` 或 WebView/bridge 入口；
   - ViewTree 文案、资源 ID、控件 bounds、当前进程和当前前台页面；
   - 记录是否真的进入验证页，不能只因接口返回验证码就假设 UI 可解。
3. 再做最小 Green：
   - ADB swipe / tap / input 先证明人工动作可被机器复现；
   - 若是 native View，优先迁移到 Xposed App 内 `MotionEvent`，避免坐标受分辨率、前后台和输入焦点影响；
   - 若是 H5/WebView，优先定位 DOM、JS bridge、WebView 输入或容器控件；
   - 若没有可见 UI，则保留为 human gate 或回到服务端/设备态分支，不伪造已解决。
4. 接入长跑前必须有状态机：

```text
detected -> notify human
autoSolve enabled -> solve attempt
solve ok -> clear local interactive waiting / cooldown -> post-smoke -> continue
solve failed -> notify and pause
autoSolve disabled -> notify and pause
```

5. 接入 miku/supervisor 时，必须把以下状态分开显示和记录：

```text
slider detected
slider solve attempted
slider solved
slider solve failed
interactive verification returned by business RPC
waiting human
post-smoke passed / failed
```

6. 交互验证自动处理不得默认等同于“绕过”。它只在授权靶场、课程练习或明确允许的测试环境中，把人类可完成的 UI 验证动作工程化为可观察、可暂停、可回滚的恢复动作。遇到服务端压力反馈、明确拒绝、授权边界变化或验证码题目超出授权时停止。

测试边界：

```text
unit: 识别规则、配置开关、wrapper rc 分支、通知 key；
e2e: action_list/slider_status/solve_slider 存在，脚本能调用但不真实打业务；
manual UAT: 真实滑块出现后，通知 -> 自动处理 -> 通知 -> 业务 post-smoke -> 请求池继续推进。
```

迁移状态必须分开写：

```text
structural-green: workflow、TASK、miku wrapper、测试和 provenance 已落盘；
current-case forward-test-green: 当前案例真实滑块已自动处理并恢复采集；
new-case forward-test-pending: 新 App、新滑块形态或新容器尚未验证。
```

## Evidence Promotion

案例 TASK 的 raw 数据、日志和真实业务 ID 不进入 Workflow，但以下内容必须在阶段 Green 后抽象：

- Red 的可复用分类；
- 从 Red 到 Green 的最小实验；
- 路线选择规则；
- 运行态/服务端边界；
- 工程坑和恢复 runbook；
- 可迁移模板或 checklist；
- 人机合作状态机、通知触发条件和 dashboard 摘要原则。
- A5/Xposed 路线的 P1 module-loaded SOP、LSPosed/scope Red 分类和多进程 ProcessRouter 前置规则。
- A5/Xposed 路线的 P3 单 action smoke SOP、Frida oracle 迁移、ClassLoader/proxy/requestData/business-ok 四层排错和 transport/business 成功语义分离。
- 交互验证/滑块处理的 UI 类型识别、最小 Green、自动处理状态机、post-smoke 和 human gate 规则。

推荐每个探索性 Android 项目至少产生：

```text
final_outputs/*完整方案.md
final_outputs/*阶段复盘.md
final_outputs/*完整历程复盘.md
```

复盘文档应使用 Obsidian 双链连接 TASK 证据，但 workflow 只保留抽象规则。

## Reference Dictionary

课程资料可以作为“查字典层”，帮助在难解红灯时寻找讲解、脚本、样本或平行路线，但不直接构成当前 TASK 的 Green 证据。

- 看雪安卓课程目录索引：`references/kanxue-course-directory-index.md`
- 课程来源追溯：`references/course-provenance.md`
- 真实项目反哺追溯：`references/field-provenance.md`

使用顺序：

```text
当前 TASK Red
→ 先按总编排 Skill 路由到子 Skill
→ 子 Skill 证据不足或遇到高级分支
→ 查课程目录索引找可能章节
→ 读取已提炼报告、source 或必要视频转写
→ 抽象成 reference/template/asset
→ 在 course-provenance.md 记录来源链
```

## Shared Environment

```bash
make init
make frida-install-device
make frida-start
make test
```

- Python 固定在工程 `.venv`，依赖由 `pyproject.toml` 与 `uv.lock` 管理。
- Agent 编译依赖由 `package.json` 与 `package-lock.json` 管理。
- Android/Xposed 构建优先使用 workflow 固定工具链：`tools/jdk17/Contents/Home` 与 `tools/gradle-8.7/bin/gradle`。如果系统 `gradle` 或 `JAVA_HOME` 不存在，不要先排查 PATH；先按 TASK Makefile 的 `WORKFLOW_TOOLS` 约定调用本 workflow 的 tools。
- 具体 Hook 脚本与构建命令放在需求 TASK。
- Frida 是 CLI 与手机服务；Miku 只提供共享环境的可视化启停入口。
