# 路由规则

## 主决策路径

1. 确认授权并定义 UAT、G2、G1 与完成证据。
2. 声明 R1 Hook、R2 RPC、R3 纯外部或 R4 组合路线的输入边界与完成门槛；另行声明分析路线与 TASK 角色，三者不得混为一列。
3. 创建 Mermaid 终点链、请求树、测试状态和唯一 `NEXT`。
4. Smoke 未通过时先修复环境。
5. 对课程、历史经验或外部报告中的 Red，先在当前设备、版本、网络和同一动作窗口复现；未复现时标记 `not-reproduced` 并保留对照证据，不进入“修复已存在故障”的叙事。
6. Java 调用链已进入 `native` 或即将分析 `.so` 时，先调用 `prepare-android-native-toolchain` 完成 Smoke-Native；工具未就绪不能解释为算法失败。
7. 未确认目标接口时先看抓包 Red 分层：目标 host/path 明文可见时调用 `analyze-android-traffic`；普通代理只见非目标流量或只有底层网关而无业务语义时，调用 `identify-android-business-network-channel`。
8. 已确认 bridge/RPC 响应模型，且目标从单请求复现扩展为页面接口地图、复合业务接口、多入口 ID 语料或批量窗口验证时，调用 `build-android-rpc-data-corpus`。
9. 已确认单个目标接口后调用 `minimize-android-request`。
10. 对标识、随机数、时间和格式字段，先按 `substitute-construction-policy.md` 判断能否做低成本替代实验。
11. 当前交付只要求功能可用且替代值通过匹配范围验证时，标记 `substitute-valid`；要求真实还原时继续推进。
12. 从当前主路线选择尚未达到路线门槛的必要叶子，并将 `NEXT` 指向对应 TASK 或测试。
13. 未定位生成位置时调用 `locate-android-request-builder`。
14. 字段入口已定位，但缓存、持久化、首次生成或来源分支未闭环时调用 `resolve-android-dynamic-field`。若字段涉及 DID、UTDID、APDID、apdidToken、umidToken、devKeySet、miniwua、authorization、Sign、Cookie 或安全 SDK 设备注册，按设备态字段束处理，不把单个字段替换实验当作最终结论。
15. 静态链缺真实实参、动态配置或中间值时调用 `trace-android-java`。若红灯是算法入口未知，而非某个已定位业务方法缺实参，并且字段形态像摘要、HMAC、对称加密或 Base64/密文，优先调用 `trace-android-java` 的 crypto-probe 模式，生成 `crypto-probe-observed` 事件后再筛选为 `fixture-candidate`。
16. Java 声明进入 `native` 且映射未知时调用 `map-android-jni`；先恢复类、签名、模块、相对偏移与 Thumb 状态。
17. Native 映射已知后选择 static-first、dynamic-first 或 hybrid：只看 JNI 入口实参可直接 Hook；需要内部调用点、降低噪声或动态受阻时先静态分析。
18. 调用 `analyze-android-native-static` 时：窄目标选 objdump，复杂控制流选 IDA，教学或高置信度交付选 cross。
19. 输入分段、调用顺序或输出未知时调用 `hook-android-native`；有静态调用者偏移时优先用于收窄通用算法 Hook。
20. 已取得运行时值后先更新 `hook-available`，再判断当前路线是否仍需追上游。
21. 需要目标进程生成时建设 Frida RPC；需要脱离进程时继续追踪并调用 `reproduce-android-crypto`。
22. 每解开一层就展开新字段，增加必要 Unit fixture，并重新计算各路线必要性。
23. 服务端响应产生的字段必须回连到前置接口节点，并记录时效、持久化和绑定；多个前置接口按 DAG 拓扑顺序推进。
24. 必要叶子满足后路由到 G1。G2 前先对原始成功请求执行外部重算预检。
25. 预检一致而 G2 返回风控、TFS 或环境拒绝时，保留 G1 Green，转入运行态/设备态/TLS/连接态与服务端策略归因。
26. 按目标要求继续路由到 G2 和 UAT。

当当前红灯属于高级分支、现有子 Skill 证据不足、或需要课程脚本/样本/讲解语境来设计下一项最小实验时，读取 workflow 顶层 `../../../references/kanxue-course-directory-index.md`。课程索引只负责帮助定位资料，不改变当前 Green 条件；实际采用课程资料后，回写 `../../../references/course-provenance.md`。

## 叶子选择顺序

1. 未定义的授权、UAT 或完成边界；
2. 失败的 Smoke；
3. 阻止读取内部字段的不透明外层；
4. 当前主路线的公共依赖；
5. 当前主路线 required 且能力未达门槛的动态字段；
6. 当前主路线 conditional 且已触发的字段；
7. G1、G2、UAT 关口；
8. 其他路线的增强任务。

Hook 已稳定取得的字段，在 R1 中不应继续阻塞；同一字段在 R3 中仍可保持 required。上游追踪任务标注“仅 R3 必需”或相应路线，不得标成全局阻塞。

## 执行方案选择

| 条件 | 优先路线 |
|---|---|
| 需要快速复现课堂运行过程，App 可稳定附加 | R1 运行时 Hook |
| 算法强依赖目标进程初始化状态 | R2 Frida RPC |
| 输入明确且目标是可迁移实现 | R3 Python/外部独立生成 |
| 只要求授权场景功能可用，字段无已知绑定 | R3/R4 替代构造候选，先低频验证 |
| 部分设备值难移植、算法适合外部实现 | R4 Hook/RPC + Python |
| 依赖真实 Android 组件且适合重载 | R4 自建 Android 应用重载 so |
| 需要脱离设备反复执行 Native | R3/R4 Unidbg |

## Native / Unidbg 路由

当红灯来自 `.so` 内算法、JNI wrapper 或 Native 安全 SDK 时，不要默认只有“真机 Hook”或“纯 Python 改写”两条路。先判断交付目标和依赖边界：

```text
Java 调用链进入 native / 已定位 so 算法
→ JNI 边界清楚？
  → 否：map-android-jni / analyze-android-native-static / hook-android-native
  → 是：继续
→ 目标是否需要脱离真机反复执行？
  → 是：创建 Native/Unidbg TASK，使用 assets/native-unidbg-task-template.md
  → 否：优先 R1 Hook 或 R2 Frida RPC
→ Unidbg 工具链 Smoke 通过？
  → 否：prepare-unidbg-toolchain
  → 是：run-so-with-unidbg
→ 报 Java/Android/App 对象缺失？
  → 是：patch-unidbg-environment，按 signature 最小补环境
  → 否：进入 Unit/G1
→ 补环境是否包含设备态、账号态、StackTrace、/proc、TEE、时间或随机数 fixture？
  → 是：先标 partial-validated；若目标要求真实请求，创建 device-assisted 对齐 TASK
  → 否：继续按声明目标验证
→ G1 通过后是否要求完整 HTTP 或业务效果？
  → 是：validate-android-reproduction 后继续 G2/UAT
  → 否：声明 G2/UAT not-required，交付离线工具或课堂复现
```

路线选择规则：

| 观察 | 优先路线 | 说明 |
|---|---|---|
| 只需要看真实入参、分段和返回 | R1 Hook | 最短路径，不必先移植 |
| App 内方法可稳定调用，外部依赖重 | R2 Frida RPC | 借用原进程生成 |
| `.so` 接口稳定、fixture 明确、Android 依赖可补齐 | R3/R4 Unidbg | 桌面反复执行，适合 Unit/G1 |
| JNI 包名、类名或系统组件依赖强，Unidbg 补环境过重 | R4 自建 Android 宿主 App | 复用真实 Android Runtime |
| 算法简单且输入完全明确 | R3 Python/外部实现 | 交付最轻，但要证明中间值一致 |
| 控制流复杂、入口或对象构造不清 | IDA/objdump + Frida cross | 先取得结构证据，再决定运行路线 |

Unidbg 通过时只能标记当前声明输入下的 `reproducible` 或 `validated`。如果完整请求还依赖登录态、设备态、TEE、TLS 指纹、服务端风控或前置接口，继续按 G2 首差分层，不回滚 Unidbg G1。

如果 Unidbg 输出依赖 Telephony、权限、调试态、StackTrace、`/proc`、时间、随机数或 App 自定义设备值 fixture，优先使用 `partial-validated`，并把后续工作拆成 device-assisted 对齐：

```text
Frida Hook 真机入口入参/返回
→ Hook 或记录设备态/运行态来源
→ 回灌 Unidbg fixture
→ 固定原始请求预检
→ 受控 G2
```

## 阻塞分支

| 证据 | 路由方向 |
|---|---|
| 行为窗口中目标请求尚未确认 | `analyze-android-traffic` |
| 普通代理有流量但只有统计、静态、无关 host、底层网关或 CONNECT，没有目标业务 host/path、operation、bridge method 或响应实体 | `identify-android-business-network-channel` |
| 小程序、WebView、Nebula、XRiver、JSBridge、RPC、mobilegw 等静态或动态证据出现 | 先确认 bridge/RPC operation、response callback 和 network exit，再进入接口分析或 R2/R3 路线选择 |
| 已确认 bridge/RPC/HTTP 响应携带目标业务实体，但尚未整理字段、分页、敏感字段和工具输出 schema | `model-android-rpc-response` |
| 已确认 bridge/RPC 响应模型和 App 内主动调用，目标变成页面接口地图、复合接口、多入口 ID 语料、分页窗口或批量采集 | `build-android-rpc-data-corpus`；声明 `single-page/paged-window/multi-entry-corpus/full-claimed`，维护 source/evidence、dry-run、checkpoint、随机等待和停止条件 |
| 已确认接口但必要参数未知 | `minimize-android-request` |
| 二进制正文阻止查看内部字段 | `locate-android-request-builder` + `trace-android-java` |
| Hook 已取得全部实参 | 更新能力矩阵；R1 可进入组合验证，R3 再追上游 |
| 格式等价值通过当前低频验证 | 标记 `substitute-valid`；根据真实性要求决定停止或继续 |
| 替代值跨会话失败或出现字段绑定 | 取消替代路线，进入真实来源和绑定链追踪 |
| 已定位 Java 方法但希望借用 App 生成 | R2 Frida RPC |
| 已确认 RPC operation 和响应模型，但外部字段依赖登录态、设备态、签名或风控上下文 | 优先评估 R2 Frida RPC 工具化；若目标是通用调度/批量/工程化交付，进入 `dispatch-via-app-runtime` 设计 R4-A App 代发；R3 另开可行性预检，不回滚 R2/R4 Green |
| R3 被 `authorization`、`Did`、`Ts`、`Sign`、`miniwua`、TEE、设备指纹、账号态或连接态阻塞，但 App 内可稳定发送 | `dispatch-via-app-runtime`；默认 R4-A App 代发 RPC/请求，Python 只调度，不拆敏感字段 |
| 业务走 WebSocket/TCP/gRPC stream/IM sync 等长连接，普通 replay 被 session/心跳/连接态阻塞，但已定位 App 内 sendMessage/sendFrame | `dispatch-via-app-runtime` 的 R4-M App 代发消息路线 |
| 已定位动态字段读取方法，但不清楚缓存、持久化或首次生成 | `resolve-android-dynamic-field` |
| DID/UTDID/APDID/apdidToken/umidToken/devKeySet/miniwua/Sign/authorization/Cookie 疑似绑定，或单独替换字段导致 `1006`、登录异常、上下文不一致 | `resolve-android-dynamic-field`，读取 `references/device-state-bundle.md`；采集任务优先 R2/R4 App 运行态，R3 外部重放另开研究路线 |
| 已取得参数、盐、Key、IV 与密文且需外部实现 | `reproduce-android-crypto` |
| `sign`、`token`、密文或摘要字段存在，但生成函数未知，且疑似 Java 标准 Crypto API | `trace-android-java` 的 crypto-probe 模式；输出 JSONL 后筛选候选事件，再进入 `reproduce-android-crypto` |
| crypto-probe 无目标事件或只有无关噪声 | 回到业务方法 Hook、`locate-android-request-builder`、`map-android-jni` 或 `hook-android-native`；不得据此断言无加密 |
| 业务字段来自注册、Token 或配置接口响应 | 展开前置接口 DAG，并调用 `resolve-android-dynamic-field` 记录服务端来源、时效、持久化和绑定 |
| 原始成功请求可重算一致，但外部请求被 TFS/风控拒绝 | 保留 G1；读取 `g2-rejection-taxonomy.md`，建立运行态、设备态、TLS/连接态与服务端策略的归因 TASK |
| App 内目标请求返回 `406/403`，课堂脚本或外部预检返回 `418/CloudWAF` | 不回滚抓包 Green；按 `g2-rejection-taxonomy.md` 标为服务端拒绝/上下文红灯 |
| JADX 显示 `renamed from Kotlin metadata`、接口实现未知或 `FooKt` 无法加载 | `trace-android-java` 的运行时符号确认 |
| R8/ProGuard 导致真实 Java 类/方法符号压缩且职责不明 | `analyze-android-obfuscation` |
| JADX 只见 wrapper/stub、业务类运行时才出现 | `recover-android-dex` |
| 不知道 Java 调用者 | 调用栈追踪 |
| Java 声明进入 native，但主机工具、NDK 或分析器状态未知 | `prepare-android-native-toolchain` |
| 不知道 Java native 方法对应哪个模块与偏移 | `map-android-jni` 冷启动捕获动态注册，或验证静态导出 |
| 已知 Native 偏移，只需确认入口、跳板或少量调用 | `analyze-android-native-static` 的 objdump 路线 |
| 需要复杂控制流、伪代码、xref 或 JNI 对象构造 | `analyze-android-native-static` 的 IDA 路线 |
| 需要复现课堂 IDA 过程或提高结论置信度 | `analyze-android-native-static` 的 cross 路线 |
| 已知 Native 映射但不清楚真实缓冲区、长度、分段或调用者 | `hook-android-native` 最小运行时取证 |
| Attach、spawn、启动稳定性或 Root/Frida/ptrace 红灯 | `diagnose-android-instrumentation` |
| 目标方法可在 App 内稳定调用但不适合移植 | `export-frida-rpc` |
| 目标 so 接口稳定且 Android 依赖可补齐 | `host-android-native-library` |
| 目标 so 接口稳定、fixture 明确且希望桌面离线回归 | `prepare-unidbg-toolchain` → `run-so-with-unidbg` → `patch-unidbg-environment` |
| Unidbg 工具链受 JDK、Maven、中文路径或资源路径影响 | `prepare-unidbg-toolchain`，优先 JDK8、课程 `mvnw`、ASCII 工作副本 |
| Unidbg 运行时报 `UnsupportedOperationException` 或缺失 Java signature | `patch-unidbg-environment`，按 signature 最小补环境，不一次性泛化全部 Android |
| Unidbg 已跑出 token 形态但 fixture 包含设备态、StackTrace、`/proc` 或 App 自定义设备值 | 标为 `partial-validated`；若目标是完整请求，进入真机对齐 TASK，不把离线输出直接当 G2 |
| Unidbg 红灯来自框架 parser、资源路径、pid 或运行副本问题 | 先归入 `prepare-unidbg-toolchain` 或 `patch-unidbg-environment` 的 tooling-gap；只修 TASK 运行副本，不归因到目标 App |
| Unidbg G1 已通过但外部 HTTP 未验证 | `validate-android-reproduction`，将 G2/UAT 明确标为 required、not-required 或 blocked |
| G2 被图片验证码、短信码或人工确认阻塞 | `handle-interactive-verification` |
| 登录、真实账号、验证码或授权边界阻止继续 | 标记 `blocked-by-boundary`，生成需要人类或测试账号补充的前置条件，不扩大采集 |
| 需要按 URL 自动观察、脱敏或单变量修改流量 | `process-android-traffic` |
| 浏览器可抓而目标 App 完全没有连接进入代理 | `capture-android-traffic` 的 SocksDroid/VpnService 强制转发路线 |
| 普通代理同窗口已能抓到目标 App 连接 | 标记 `not-reproduced`，可将 SocksDroid 作为 `passed-with-scope` 的备用路径验证 |
| 强制转发后出现连接但 TLS 无明文 | 证书信任/Pinning 诊断，不回滚“流量入口已恢复” |
| 强制转发后目标动作仍只有 UDP/QUIC | 建立协议降级实验，不把它误判为 Pinning |
| Unidbg 报告环境缺失 | 最小补环境 |
| 高级分支卡住且现有子 Skill 证据不足，例如 OLLVM、FART/code item、SVC syscall、JNI 地址防追踪、VMP、eBPF | 读取 workflow 顶层 `../../../references/kanxue-course-directory-index.md` 找课程章节、source、P0/P1 提炼或 P2 候选；采用后写 provenance |

不能仅根据表面症状选择分支。先确认当前路线、能力缺口和最小证据。

## 三轴路由

| 维度 | 回答的问题 | 示例 |
|---|---|---|
| 交付路线 | 最终结果依赖什么运行环境 | R1 Hook、R2 RPC、R3 外部实现、R4 组合 |
| 分析路线 | 本轮用什么取得知识证据 | JADX、objdump、IDA batch、IDA MCP、Frida |
| TASK 角色 | 本轮失败是否阻塞终点 | blocking、confirmatory、enhancement |

例如 Day19 的主交付是 R3；objdump + Frida 是主分析路径；IDA batch 是 enhancement 的 primary 证据；IDA MCP 是 confirmatory 证据。MCP 不因此成为 R3 的运行依赖。

## Native 静态/动态顺序

| 条件 | 优先顺序 |
|---|---|
| 已知 JNI 入口，只需参数或返回值 | dynamic-first |
| 需要找到内部算法函数或调用者过滤 | static-first |
| Hook 通用函数噪声过大 | static-first 后窄 Hook |
| 动态附加失败但二进制可读 | static-first |
| 静态伪代码语义不确定 | dynamic-first 校正 |
| 教学复现或高置信度交付 | hybrid/cross |

每次路由必须输出：

- Mermaid 中的红灯节点或测试 ID；
- 该节点为何阻塞终点；
- 下一项最小实验；
- Green 条件；
- 预期证据与落盘位置；
- 负责的子 Skill；
- 实验结束后需要更新的图、表和日志。
