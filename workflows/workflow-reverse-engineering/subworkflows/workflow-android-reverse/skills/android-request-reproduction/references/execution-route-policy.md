# 交付路线与必要性

## 核心判断

字段“已经取到值”和“还需要追上游”不是同一问题。先声明交付路线，再判断该字段是否仍是必要叶子。

| 路线 | 输入边界 | 字段完成门槛 | 上游追踪 |
|---|---|---|---|
| R1 运行时 Hook | App 正常运行，Hook 可附加 | 每次需要时可稳定捕获，至少 `hook-available` | 若 Hook 点稳定且值可直接交给下游，通常不需要 |
| R2 Frida RPC/进程借用 | App 进程与目标方法可调用 | RPC 可重复返回目标值或完整正文，至少 `rpc-available` | App 内部已负责生成时通常不需要 |
| R3 纯外部独立生成 | 不依赖目标进程 | 从声明的业务输入重新生成，至少 `reproducible` | 对动态输入通常需要 |
| R4 组合路线 | 明确哪些值由设备取得、哪些在外部生成 | 每个字段达到其负责环节的门槛 | 仅追踪组合边界以外仍缺失的部分 |

不得把 R1、R2 的完成结论外推到 R3。也不得因为 R3 尚未完成，就把已经稳定可用的 R1 标为失败。

Unidbg 属于 R3/R4 的一种执行承载方式，不是单独的交付路线：

- 当输入 fixture、APK、so 和必要 Android/Java 环境都可在桌面模拟时，Unidbg 可以完成 R3 的 Unit/G1；
- 当部分输入仍来自真机 Hook、Frida RPC、前置接口或设备状态时，Unidbg 是 R4 的外部计算环节；
- Unidbg G1 通过只证明声明输入下的算法或函数可离线执行，不自动证明完整 HTTP G2；
- 若 Unidbg 补环境需要大量真实系统状态、TEE、账号态或服务端状态，应重新评估 Frida RPC、自建宿主 App 或保留 R4，而不是无上限补环境。

可复制的 Native 路线选择：

```text
目标是课堂算法 / 固定字段 / 本地工具
→ Unidbg G1 可作为主交付，G2/UAT 标为 not-required

目标是完整请求外部重放
→ Unidbg 只解决 sign/加密/正文等叶子
→ 仍需原始成功请求预检、G2 和首差分层

目标强依赖运行态
→ 优先 R2 Frida RPC 或 R4：设备生成 + 外部调度
```

## 双轴记录

每个字段同时记录：

1. **取值能力**：`unknown`、`observed`、`hook-available`、`rpc-available`、`located`、`understood`、`reproducible`、`validated`。
2. **路线必要性**：对 R1/R2/R3/R4 分别标记 `required`、`conditional`、`not-required` 或 `unknown`。

示例：

| 字段 | 取值能力 | R1 Hook | R2 RPC | R3 纯外部 |
|---|---|---|---|---|
| `aid` | `hook-available` | 上游追踪 `not-required` | 若 H7 内部取参则 `not-required` | 上游生成链 `required` |

## 路线切换

切换主路线前记录：

- 切换原因；
- 新的运行环境与输入边界；
- 原路线已验证的能力；
- 哪些叶子从必要变为非必要；
- 哪些叶子重新成为必要；
- 新路线的最终验证方式。

路线切换只改变必要性，不抹去既有证据和能力状态。

## R3 外部重放预检

从 R2 Frida RPC 切到 R3 纯外部请求前，不得只因为“App 内 RPC 已成功”就假定 Python 可直接重放。至少补齐以下预检：

1. 固定一个 R2 成功 fixture，记录业务输入、operationType、分页游标、响应摘要和完成边界。
2. 目标化确认网络出口：URL、Method、Content-Type、RPC version、关键 Header、Body 原始字节形态、自加密/内容加密标记。
3. 生成脱敏 replay manifest，把字段分为 `known-static`、`known-runtime`、`sensitive-redacted`、`unknown-required`。
4. 先做 Python dry-run，只构造请求摘要，不发送网络。
5. 真实 G2 前必须明确授权、样本、限速、凭据处理和停止条件。

若旁路监听脚本和主动 RPC 脚本并行时捕获不到目标 operation，优先使用“同会话探针”：在同一个 Frida agent 内安装网络 hook、标记当前 operation、主动调用目标 RPC，并返回脱敏后的网络出口证据。这样可以避免双 attach、时序窗口或代理对象绕过造成的误判。

R3 预检成功只说明请求形态可构造，不等于外部发送可被服务端接受。若 Header 中仍有 `authorization`、`Did`、`Ts`、`Sign`、`miniwua`、设备态或风控上下文，R3 状态应写为 `shape-ready / g2-not-executed` 或 `blocked-by-runtime-boundary`，而不是 `reproducible`。

当 R3 受运行态边界阻塞时，优先评估 R4：

```text
设备低频签发/上下文借用
→ 外部调度、去重、断点续跑、限速
→ 将设备占用降为必要的最小环节
```

R4 不只有一种形态。若 Header/envelope 中包含 `authorization`、`Did`、`Ts`、`Sign`、`miniwua` 这类账号态、设备态、签名态和风控态字段，默认优先选择 **R4-A：App 代发 RPC，Python 只拿响应**：

```text
Python:
  负责任务队列、分页、去重、断点续跑、限速、落盘、UAT；

App/Frida:
  负责在同一运行态中生成 Header/envelope；
  负责实际调用 mobilegw/RPC；
  不把敏感 Header 明文暴露给 Python。
```

只有在证明 envelope 可跨进程、跨连接或短时复用后，才评估 **R4-B：App 签发 envelope，Python 外部发送**。一般不推荐把 R4 设计成字段级服务：

```text
getAuthorization()
getDid()
getTs()
getSign()
getMiniwua()
```

因为这些字段可能彼此绑定，单独拆开容易破坏 `Ts`、`Sign`、`Did`、`miniwua` 和账号态的一致性。

具体设计、allowlist/forbidden list、RPC dispatcher 与长连接消息 dispatcher 模板由 `dispatch-via-app-runtime` 承载。总编排只负责在 R3 受运行态边界阻塞时路由到该 Skill，不在自身展开 agent/client 细节。

若原目标接口已经出现服务端限制、账号冷却、验证码或 `RPCException [1009]`，不要继续用该接口研究通用网关签发能力。可选择同一网关、同一 RPC 栈、低风险且已通过 UAT 的兄弟接口做 R4 签发边界实验，并明确：

- 该实验只验证通用 envelope / Header / 运行态字段边界；
- 不声明已经恢复原目标业务接口；
- 原目标接口保持冷却，后续迁移需单独验证。

对 R4、R3 或任何可能触发真实服务端请求的实验，必须在 TASK `logs/LOG.md` 中先写 ReAct 的 `Reason` 和 `Action`，执行后再补 `Observation` 和 `Decision`。不得只在实验结束后补记。`Action` 至少写明样本、命令、是否 live、是否外部发送、频率和停止条件。

## 风控参数与逆向边界

Java / `.so` 逆向可以用于定位、解释和借用风控参数，但不能默认推出这些参数已经可被纯 Python 外部复现。对 `Did`、`Ts`、`Sign`、`miniwua`、`authorization`、设备指纹、账号态或风控上下文，先按层级判断：

| 层级 | Java / `.so` 逆向价值 | 交付路线含义 |
|---|---|---|
| 业务参数与 RPC envelope | 很高，可定位构造链、operationType、body、分页游标 | 通常可推进 R2/R3 dry-run |
| 网关 Header 与签名入口 | 很高，可 Hook 入口、打印调用栈、定位上游输入 | R2/R4 通常可用；R3 需继续证明可外部生成 |
| 设备指纹、账号态、Token、缓存态 | 中高，可追来源、时效和存储位置 | 常见为 R4 边界：可借用，不一定可移植 |
| native 安全 SDK / TEE / 系统环境 | 中等，可分析或借用，移植成本高 | 优先评估 Frida RPC、宿主 App、Unidbg 或 R4 |
| TLS 指纹、连接态、服务端频控/风控 | 低，客户端逆向只能提供部分线索 | 不得把服务端拒绝直接回滚为算法失败 |

判断规则：

1. 找到生成函数只表示 `located`；能 Hook 到值表示 `hook-available`；能在 App 内重复调用表示 `rpc-available`；只有脱离目标进程仍能从声明输入生成并验证，才是 `reproducible`。
2. 风控参数常是“算法 + 状态 + 环境”，而不是孤立算法。即使签名算法可见，也要继续确认输入、时效、账号绑定、设备绑定、连接绑定和服务端策略。
3. 若 App 内可稳定生成但外部复现成本高，优先把该节点标为 R4 `conditional`，不要为了追求 R3 把 TEE、设备态或服务端策略硬写成算法叶子。
4. 若 G2 出现 `403/406/418`、CloudWAF、RPCException `[1009]` 或业务拒绝，保留已通过的 G1/R2 证据，新增运行态/设备态/传输上下文任务。
5. R4 的目标不是放弃逆向，而是把逆向用于确定“哪些部分必须留在 App/设备内，哪些部分可以交给 Python 调度”。

可使用的最小决策表：

| 观察 | 推荐动作 | 不要做 |
|---|---|---|
| 只知道字段值 | Hook 来源或出口，记录 `observed` | 宣称可复现 |
| 找到 Java 构造入口 | 打印调用栈和真实输入，做字段分层 | 直接复制静态代码外发 |
| 进入 native 安全 SDK | 先确认能否 Frida RPC 借用；必要时再评估 Unidbg | 默认必须完整移植 `.so` |
| App 内成功、外部失败 | 做首差分层：Header/body/登录态/设备态/TLS/频率 | 把所有失败归因到 sign |
| 已出现服务端拒绝 | 降频、停止重复探测、记录护栏 | 继续撞外部 G2 |
