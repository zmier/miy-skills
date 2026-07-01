---
name: dispatch-via-app-runtime
description: 在经过授权的 Android 目标中，当纯外部复现被账号态、设备态、签名态、风控态、TEE、TLS/连接态或长连接 session 阻塞时，设计“借用 App 真实运行态代发请求/消息，Python 只做调度、限速、落盘和验收”的 R4 路线。用于 mobilegw/mPaaS RPC、JSBridge RPC、自研网关、App 内 HTTP、WebSocket/TCP/gRPC/IM sync 等场景的 App 代发 RPC、App 代发 envelope 或 App 代发长连接消息。不得用于未授权服务、凭据提取、规避访问控制、高频批量采集或绕过服务端风控。
---

# 借用 App 运行态代发

## 目标

当 R3 纯 Python/外部复现被运行态字段或连接态阻塞时，不默认硬破所有算法，而是先评估：

```text
Python 外部调度
→ App/设备真实运行态生成 Header/envelope/session/message
→ App 内代发请求或消息
→ Python 接收响应、限速、落盘、验收
```

本 Skill 是方法 Skill。总编排负责判断是否进入本路线；本 Skill 负责把路线设计成安全、可测、可迁移的 App 运行态代发工具。

## 触发条件

进入本 Skill 前通常已出现至少一个证据：

- R3 预检发现 `authorization`、`Did`、`Ts`、`Sign`、`miniwua`、设备指纹、TEE、账号态或风控上下文难以外部生成；
- App 内 RPC、bridge、网关、native 网络栈或长连接发送入口已定位；
- App 内主动调用可成功，但外部 HTTP replay 被运行态边界阻塞；
- 普通代理看不到业务语义，但已确认业务走 JSBridge/RPC/mobilegw 或长连接；
- 任务目标是授权研究、课堂靶场、自有 App 或明确授权测试。

若尚未确认通道，先回到 `identify-android-business-network-channel`。若只是封装一个已定位方法为 Frida RPC，先用 `export-frida-rpc`；本 Skill 用于把它上升为 R4 交付路线。

Frida RPC 可作为 R2/R4 分界样例：

- 只导出一个签名、加密或工具函数：停留在 `export-frida-rpc`，状态是 `rpc-call-passed` 或 `rpc-available`。
- Python 只调度，App 内部负责生成 envelope、发送请求或发送长连接消息：升级到本 Skill，状态进入 R4-A/R4-M。
- Flask/HTTP 包装不是默认路线；只有在 allowlist、限速、日志、脱敏和授权边界都明确时，才作为受控 wrapper。

云手机或远程真机场景中，HTTP wrapper 常被用来把设备旁边的 Frida RPC 暴露给外部脚本。它本身只解决“调用入口”问题，不自动解决运行态代发的工程边界。满足以下任一条件时，应从临时 wrapper 升级为本 Skill 管理的 R4 工程：

- 外部脚本需要持续调用，而不是一次性调试；
- wrapper 不只是返回 sign/hash，而是触发 App 内请求、RPC 或长连接消息；
- 需要分页、限速、断点续跑、去重、落盘或 UAT；
- 需要 allowlist/forbidden list 和敏感字段扫描；
- 需要声明 `externalRequestSentByPython=false` 或确认是否由 App 发出请求。

## 路线分类

| 路线 | 形态 | 适用 | 默认建议 |
|---|---|---|---|
| R4-A App 代发 RPC/请求 | Python 传 operation/body，App 内发送，Python 接响应 | mobilegw/mPaaS、自研 RPC、App 内 HTTP | 首选 |
| R4-B App 签发 envelope，Python 外部发送 | App 返回短时 envelope，Python 发 HTTP | 已证明 envelope 可跨连接/进程复用 | 谨慎 |
| R4-C 字段级签发服务 | App 分别返回 Sign/Did/miniwua 等字段 | 字段彼此独立且无敏感泄漏 | 默认不推荐 |
| R4-M App 代发长连接消息 | Python 传 command/payload，App 用现有 session 发送帧/消息 | WebSocket/TCP/gRPC stream/IM sync | 可迁移路线 |

默认优先 R4-A。不要把字段级签发当默认方案。

## 工作流

1. 确认授权边界、目标业务动作、服务端压力和禁止接口。
2. 读取 `references/route-selection.md`，选择 R4-A、R4-B、R4-C 或 R4-M。
3. 创建 TASK 工作区；从 `assets/app-runtime-dispatch-contract-template.md` 复制验收契约。
4. 明确运行态边界：哪些由 Python 管，哪些必须留在 App/设备/账号/连接态。
5. 建立 allowlist 和 forbidden list。默认拒绝未知 operation、评论/回复高风险接口、支付/交易/账号修改类接口。
6. 设计最小 dispatcher：
   - RPC/网关：`operationType + requestData`；
   - App HTTP：`apiName/path + body`，但 Header/envelope 由 App 管；
   - 长连接：`command/opcode/topic + payload`，由 App session 发。
7. Python client 默认只保存 simplified JSON 或脱敏摘要；只有显式 `--save-raw/includeRaw` 才保存 raw。
8. live 前写 TASK `logs/LOG.md` 的 ReAct `Reason/Action`，说明是否 live、是否外发、频率、停止条件。
9. 先 dry-run，再用低风险 allowlist 样本做 smoke。不要用已被服务端限制的接口研究通用能力。
10. Smoke Green 后，输出接口卡片、UAT 结果、运行态边界、扩展规则和未覆盖风险。
11. 若进入批量或语料采集，把调度、分页、去重、限速和覆盖率交给 `build-android-rpc-data-corpus`。

## 设备态刷新与自洽 bundle

当 R3/R4 请求出现设备态限制，并且观察到“同账号换设备可用、同设备换账号仍受限”时，优先把问题建模为设备态画像，而不是账号态。

不要默认后置扰动 `Did`、`apdidToken`、`Cookie`、`miniwua`、`Sign` 或 `authorization`。这些字段可能是同一组设备态 bundle 的不同投影：

```text
本地安全 SDK 缓存
-> 设备态 DID / apdidToken / devKeySet
-> miniwua / wua / Sign / authorization / Cookie
-> App 内 RPC envelope
-> 服务端设备画像
```

若只在请求临发前改显式字段，可能导致：

```text
显式设备字段=B；
签名、安全字段和服务端注册状态仍是 A；
服务端返回 1006 或等价“不合法请求”；
```

更稳的路线是：

1. 先只读溯源设备态来源，确认普通 XML、加密 SharedPreferences、native KV、TEE 或服务端下发层。
2. 若存在 native KV 或加密偏好存储，清理/替换必须可备份、可恢复、可验证 owner/mode。
3. 启动 App 后用真实业务动作触发安全 SDK，而不是只调用空参数初始化。
4. 以 token 长度、关键方法调用链和后续业务 smoke 作为 Green，不把“字段变化”本身当 Green。
5. 后续采集必须分接口小批量验证，再恢复保守窗口。

在授权靶场中，如果已证明完整重装 App 能让 `1009` 恢复，并且后置单字段替换只会造成 `1006` 或不稳定结果，可以新开“设备态根换代”任务，尝试比完整重装更小的 destructive reset。该路线必须满足：

1. 明确授权、可重装恢复、可备份关键本地状态；
2. 只在 TASK 中记录真实路径、操作日志和回滚方式，通用 Skill 只记录抽象层级；
3. 重置后必须通过 App 首启/登录/业务动作让安全 SDK 自行重建 bundle；
4. Green 标准是同一业务 smoke 从 `1009` 回到 success，且未使用后置字段 override。

典型 Green 证据：

```text
apdidToken 或等价设备 token 从空变为有效长度；
App 内业务 RPC get/detail/comment smoke 成功；
无 1009/1006；
敏感值不落普通日志；
旧状态有 restore 命令或备份路径。
```

## 安全护栏

必须满足：

```text
allowlistOnly=true
externalRequestSentByPython=false（R4-A/R4-M 默认）
sensitiveHeadersStored=false
forbiddenEndpointsDeclared=true
ReActBeforeLive=true
```

不得：

- 保存 `authorization`、`Did`、`Ts`、`Sign`、`miniwua` 等敏感 Header 明文；
- 把 App 内成功写成 R3 `reproducible`；
- 使用高风险接口做通用签发实验；
- 通过提高频率、换账号、代理池等方式突破服务端限制；
- 将工具用于未授权服务。

## 验收

最小 Green：

```text
dry-run 通过；
App 内 smoke 返回业务响应；
route 标记为 R4-A/R4-M；
liveRequestSentByApp=true；
externalRequestSentByPython=false；
敏感字段扫描无命中；
allowlist/forbidden list、UAT、log.md 完整。
```

若是 R4-B，还必须额外证明 envelope 可跨连接/进程/时间窗口复用，并声明凭据处理和失效策略。没有这个证据时，回退 R4-A。

## R4-X 长驻服务化

当 Frida RPC 原型已证明可行，但需要模块随 App 启动、重启后恢复、云手机/远程真机旁路调用、长期在线 action 或更稳定的服务化入口时，转入 `xposed-sekiro-runtime-dispatch`。

R4-X 不替代 R4-A/R4-M 的边界判断。它只是把 App 内代发或 App 内方法调用从“临时 session”升级为“Xposed/LSPosed + Sekiro 长驻服务”。仍必须满足 allowlist、forbidden list、限速、敏感字段扫描和 `externalRequestSentByPython` 声明。

## 参考资料

- 路线选择读取 `references/route-selection.md`。
- 设计 RPC/网关 dispatcher 读取 `references/rpc-dispatcher-pattern.md`。
- 设计长连接消息 dispatcher 读取 `references/message-dispatcher-pattern.md`。
- 创建 TASK 契约使用 `assets/app-runtime-dispatch-contract-template.md`。
- 需要长期化、模块化或 Sekiro action 时，转入 `xposed-sekiro-runtime-dispatch`。
