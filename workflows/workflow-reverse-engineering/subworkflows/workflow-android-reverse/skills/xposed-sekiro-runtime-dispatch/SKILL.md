---
name: xposed-sekiro-runtime-dispatch
description: 在经过授权的 Android 目标中设计 Xposed/LSPosed + Sekiro 的长驻 App 运行态服务化路线。用于 Frida RPC 适合临时研究但需要长期在线、模块随 App 启动、远程 action 调用、批量低频调度、云手机/远程真机旁路调用，或需要把 App 内方法/RPC/签名/请求入口暴露成受控 Sekiro action 的场景。不得用于未授权服务、高频采集、凭据提取、规避访问控制或绕过服务端风控。
---

# Xposed/Sekiro 运行态代发

## 目标

把一次性的 Frida RPC 或手动 Hook，升级为可安装、可重启、可长期在线的 R4-X 运行态服务：

```text
Xposed/LSPosed 模块
→ 目标 App 进程加载
→ 注册 SekiroClient
→ 注册 allowlist action
→ 外部脚本低频调用 action
→ App 内真实运行态执行
→ 返回脱敏响应
```

## 何时使用

- Frida RPC 已证明可行，但需要长期稳定调用；
- 目标运行态依赖账号、设备、ClassLoader、连接态或 App 初始化；
- 需要云手机/远程真机旁边常驻一个调用入口；
- 需要把 App 内方法、RPC 或请求入口封装成少量 allowlist action。

如果只是临时导出一个函数，先用 `export-frida-rpc`。如果 Python 仍直接外发请求，由 `dispatch-via-app-runtime` 判断是否应该升级到 R4-X。

## 工作流

1. 确认授权边界、目标 App、目标进程、作用域和禁止接口。
2. 读取 `references/xposed-sekiro-contract.md`，写 TASK 契约。
3. 读取 `references/xposed-lsposed-p1-sop.md`，先做 P1 Xposed/LSPosed smoke：模块加载、目标进程命中、日志可见、ClassLoader 可用。
4. 从 `assets/XposedSekiroEntryTemplate.java` 和 `assets/SekiroActionHandlerTemplate.java` 创建模块入口和 action。
5. 只注册 allowlist action；禁止通配 action、动态执行任意类名/方法名。
6. 配置 Sekiro group、clientId、server、port、action 名称和超时；这些都留在 TASK 配置，不写进 Skill。
7. action 内部只调用明确的 App 内方法或请求入口；不要返回敏感 header/token/device id。
8. 外部调用端执行 dry-run，再低频 smoke；记录 `externalRequestSentByPython=false` 或实际发送边界。
9. 若进入批量调度，限速、断点续跑、覆盖率和服务端反馈交给 `build-android-rpc-data-corpus` 或具体 TASK。

## P4 请求池 Transport 接入

P4 的目标不是重写业务 worker，而是把已验证的 Xposed action 接成一个可切换 transport：

```text
已有 Frida/App runtime oracle
-> Xposed action_list / health
-> XposedActionTransport
-> 原请求池 worker 增加 --transport xposed
-> 小窗口真实请求
-> 与 Frida 输出结构、SQLite 状态和 raw/simplified 策略对齐
```

P4 不应改变：

- 业务主键、分页游标和 importer 语义；
- raw/simplified 保存边界；
- partial、not-found、deleted、business-failed 的失败分类；
- 每实体 checkpoint 和断点续跑策略。

P4 必须验证：

```text
transportSwitchExplicit=true
fridaTransportStillUsableOrFallbackDeclared=true
xposedActionListOk=true
smallWindowRealRunPassed=true
workerStatusMachineUnchanged=true
businessRpcTriggered=true
sensitiveHeadersReturned=false
```

若 P4 小窗口失败，按以下顺序排查：

```text
action server 是否在线
operation/action 名称是否在 allowlist
Xposed client 协议是否解析出 transportOk/businessOk
业务样本是否失效、删除或服务端拒绝
SQLite 队列是否残留 running/failed 状态
```

## P5 受控状态变更 Action

设备态、缓存态、登录态、安全 SDK 状态或运行态环境变更 action 属于高危 action。它们可以作为恢复手段，但不能和普通业务 action 混在一起。

最低契约：

```text
prepare 与 execute 分离
execute 需要显式 confirm
需要 recentRedEvidence 或人工授权
businessRpcTriggered=false
sensitiveHeadersReturned=false
执行前备份或声明可重装恢复
执行后必须 post-smoke
失败时 fallback 或 human gate 明确
```

推荐状态机：

```text
检测到 Red
-> 判断 Red 是否属于可恢复设备态/缓存态
-> prepare-state-reset
-> human/auto policy gate
-> execute-state-reset(confirm=...)
-> 拉起目标 runtime
-> post-reset smoke
-> 恢复请求池
```

不得用这类 action：

- 绕过服务端明确拒绝、验证码、授权边界或压力反馈；
- 任意删除目标 App 数据而不记录证据和恢复边界；
- 返回设备态 token、签名材料、账号态凭据；
- 在没有 Red 证据时循环执行。

## P6 生产长跑状态机

P6 才能称为长跑 Green。它要求 action server、请求池、限速、恢复和人工门形成闭环。

必须分层记录状态：

```text
runtime heartbeat：目标 App/模块/action server 是否活着；
business runtime：目标页面、小程序、bridge/RPC 初始化是否可用；
network health：设备网络、USB 转发、代理/VPN 或目标通道是否可用；
bucket quota：每个业务接口独立窗口，不混用预算；
checkpoint：每个实体成功即落库，失败保留可重试语义；
red classifier：1009、业务 not-found、transport error、App crash、网络红灯分开；
human gate：登录、交互验证、状态变更确认等需要人类时明确停机或等待；
post-gate smoke：人类动作或自动修复后必须验证再恢复长跑。
```

Dashboard 或 supervisor 不能只相信旧状态文件。显示/决策优先级应为：

```text
真实 worker 进程 / 最近 DB 推进 / action server health
> SQLite running 行和队列状态
> scheduler nextRunAt、quota、boundary
> 历史 lastErrorMessage
```

如果显示“可运行但不动”或“上次失败但实际在跑”，优先检查：

```text
worker 进程是否存在
目标 bucket 最近更新时间
是否被其他 bucket 长批次串行占用
quota/window guard 是否满额
状态文件是否残留旧 cooling/error
```

P6 迁移状态应保守声明：

```text
当前项目长跑通过 = current-case forward-test-green
新 App 未验证 = forward-test-pending
```

## P3 单 Action 业务 Smoke

从 Frida RPC 迁移到 Xposed/Sekiro 时，不要把“Frida 已经跑通”直接视为 Xposed Green。P3 必须先迁移一个明确 allowlist action，完成单条低频 smoke，再扩展到第二个 action 或请求池。

推荐顺序：

```text
选一个已由 Frida oracle 验证的 action
-> 写 action contract 和静态测试
-> 默认 dry-run，确认 businessRpcTriggered=false
-> 显式 real=1，单条低频真实 smoke
-> 对齐 Frida oracle 的 operationType / requestData / options-map
-> 输出脱敏简化响应
-> 用有效样本和业务失败样本分别验收
```

这里的 Frida oracle 必须来自当前 TASK 的可重复证据，例如已跑通的 agent、requestData、响应结构和输出文件。不要把课程笔记、猜测字段或旧版本请求当成 oracle。

P3 常见 Red 与处理：

| Red | 优先判断 | 最小 Green |
|---|---|---|
| 空响应 / App crash | action worker 未兜底 `Throwable` 或 App 运行态崩溃 | action server 返回结构化异常，不让 App 因 smoke 崩溃 |
| 找不到 App 类 | action 线程 ClassLoader 不对 | 从 Xposed entry 注入目标 App `lpparam.classLoader` |
| RPC proxy / 方法签名失败 | 反射 exact signature 不稳 | 扫描兼容 overload，或改用稳定接口 |
| RPC 业务异常 | requestData 与 Frida oracle 不一致，或样本业务状态不同 | 先完全对齐 oracle 请求体，再换有效样本复验 |
| transport 成功但业务失败 | 把“请求发出”误判为业务成功 | `transportOk` 与 `businessOk` 分离，业务失败返回 `ok=false` |

P3 action 输出必须保留边界：

```text
allowlistOnly=true
dryRun 默认不触发业务
real=1 才触发业务
sensitiveHeadersReturned=false
operationType 固定
componentStatus 可读
raw 默认关闭
```

P3 Green 不等于长跑 Green。只有所有目标基础 action 都通过单 action smoke 后，才进入 SQLite 请求池、miku dashboard、飞书通知和批量限速。

## P1 SOP 摘要

进入 action server 之前，必须先完成 P1：

```text
ReAct plan
-> Red smoke/UAT
-> 静态契约测试
-> 最小 Xposed 模块
-> 构建安装
-> LSPosed/Zygisk/Manager 启用
-> 目标 App scope
-> logcat module-loaded
-> restart smoke
```

P1 只证明模块加载，不做业务请求。Green 证据必须包含：

```text
LSPosed-Bridge: Loading class <entry.class>
<TAG>: module-loaded package=<target.package> process=<process>
<TAG>: classloader-ready process=<process> classLoader=<classloader>
```

大型 App 常会多进程加载模块。P2 以后必须增加 `ProcessRouter`，避免在 `:push`、`:gpu_process`、sandbox 进程重复注册 action server。

不要优先手写 `/data/adb/lspd/config/modules_config.db`；优先使用 `xposedscope` 与 LSPosed Manager。若手写 DB，必须记录备份、WAL/SHM/SELinux 风险和回滚方式。

## 和 Frida RPC 的关系

| 维度 | Frida RPC | Xposed/Sekiro |
|---|---|---|
| 使用阶段 | 临时研究、快速验证 | 长期运行态服务化 |
| 生命周期 | attach/spawn session | 随 App/模块加载 |
| 工程成本 | 低 | 高 |
| 稳定性 | 受 Frida session 影响 | 适合云手机/远程真机常驻 |
| 默认用途 | R2 函数导出或 R4 原型 | R4-X 生产化/长期化路线 |

## 安全护栏

必须满足：

```text
allowlistOnly=true
forbiddenEndpointsDeclared=true
externalRequestSentByPython=false（App 内代发默认）
sensitiveHeadersReturned=false
rateLimitDeclared=true
moduleScopeDeclared=true
```

不得：

- 暴露任意方法调用器；
- 返回账号态、设备态、签名态敏感字段明文；
- 用高风险接口做通用 smoke；
- 通过提高频率、换账号或代理池突破服务端限制。

## 资源

- `assets/upstream-xposed-sekiro/`：upstream 代码，只作参考和迁移来源。
- `assets/XposedSekiroEntryTemplate.java`：通用入口模板。
- `assets/SekiroActionHandlerTemplate.java`：通用 action handler 模板。
- `references/xposed-sekiro-contract.md`：TASK 契约、状态和验收。
- `references/xposed-lsposed-p1-sop.md`：Xposed/LSPosed P1 module-loaded SOP。
