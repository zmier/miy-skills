---
name: android-request-reproduction
description: 以“以终为始、证据校正、测试推进”编排经过授权的 Android 请求复现任务。围绕一个目标 URL 建立 UAT、Smoke、Unit、G1、G2 测试契约，并用 Obsidian Mermaid 核心控制面从终点反推交付路线、请求构造依赖、当前红灯和下一 TASK；再路由抓包、参数归约、JADX、Frida、JNI、Native、Python、RPC、Unidbg 与 MCP 工具。用于自有应用、明确授权目标或课堂靶场中的接口确认、字段解释、请求复现、任务可视化、证据管理和完成判定。不得用于未授权访问、凭据窃取、规避第三方访问控制、隐藏有害行为或高频批量采集。
---

# Android 请求复现

## 目标

把一个经过授权的目标请求作为主任务。先定义最终验收，再从终点反推当前最小红灯；维护完整证据链，把任务路由到能够解决该红灯的最小子 Skill 或工具，并在每个分支完成后回到验证主线。

这是一个渐进生长的总编排 Skill。不得声称已经具备 `references/capability-registry.md` 中仍标记为 `planned` 的能力。

始终遵循：

> 以终为始，以证据校正，以测试推进。

## 启动流程

1. 确认目标属于课堂靶场、自有应用或明确授权测试。
2. 阅读 `references/evidence-driven-tdd.md` 和 `references/acceptance-statuses.md`。从 `assets/acceptance-contract-template.md` 创建验收与测试契约，先定义 UAT、G2、G1、交付路线和完成边界。
3. 按 `references/task-workspace-contract.md` 创建或定位该需求的独立 TASK 工作区。
   - 若任务核心是 Native/.so 算法离线复现、Unidbg 主动调用或补环境，优先使用 `assets/native-unidbg-task-template.md` 创建 TASK 骨架；该模板只负责任务结构，不替代具体课程证据。
4. 从 `assets/request-construction-ledger-template.md` 复制并创建 `request-construction-ledger.md`，登记终点链、目标 URL、请求头、请求体和当前可见字段。若目标 URL 尚不可见，先登记目标业务动作、UI/UAT 结果和抓包可见性红灯，不得虚构 URL。
5. 若业务请求依赖注册、Token、配置或设备签发接口，先把它们画成“前置接口 DAG”。服务端下发字段必须连接到产生它的响应节点，不能作为孤立常量处理。
6. 定义本次交付路线及输入边界：运行时 Hook、Frida RPC/目标进程借用、纯外部独立生成，或明确的组合路线。路线可以并行评估，但必须标记当前主路线。
7. 分别声明三个正交维度：交付路线 `R1-R4`、本轮分析路线、TASK 角色 `blocking/confirmatory/enhancement`。不得把“使用了某个工具”误写成“交付依赖该工具”。
8. 对每个不透明字段声明真实性要求：必须还原 App 原值，还是只需满足当前授权场景的服务端约束。按 `references/substitute-construction-policy.md` 判断是否先做替代构造实验。
9. 在台账顶部创建 Obsidian Mermaid 核心控制面：终点链负责从 UAT 反推 G2、G1 和路线门槛；请求树与真实 HTTP 请求同构；运行时证据、替代构造和破解 TASK 作为侧枝；使用唯一 `NEXT` 节点标明下一项最小实验。
10. 使用 `references/workflow-state.md` 创建或更新工作流状态。
11. 先运行或登记 Smoke。环境红灯未排除时，不得把无输出解释为算法或 Hook 点错误。
12. 阅读 `references/routing.md`，根据 Mermaid 中的终点链、当前路线和测试状态选择下一个必要且未解决的叶子节点。普通代理只见非目标流量时，优先路由到 `identify-android-business-network-channel`，先确认业务通道、bridge/RPC operation、响应路径和网络出口；若目标已经从“复现单个请求”转为“梳理页面接口、封装复合接口或构建多入口语料库”，路由到 `build-android-rpc-data-corpus`，不要继续把所有节点塞进单 URL 请求树。
13. 若当前红灯属于高级分支、现有子 Skill 证据不足，或需要寻找课程讲解、脚本、样本、平行路线时，读取 workflow 顶层 `../../../references/kanxue-course-directory-index.md`。该索引只作为查字典层和路由辅助，不构成当前 TASK 的 Green 证据；实际采用课程材料后必须回写 `../../../references/course-provenance.md`。
14. 为该红灯创建或定位 TASK，写明 Red、最小假设、实验、Green 条件和预期证据；只加载完成该实验所需的子 Skill 或参考资料。
15. 涉及人类操作时，要求子 Skill 先生成操作手册，再等待人类反馈；不得用对话中的临时指令替代 TASK 文档。
16. 每解开一层，都把新出现的字段追加到“被解开的参数或数据层”下面；TASK 和破解方法只能作为该参数的侧枝，不得按技术领域重新分类字段。
17. 子 Skill 返回后，先按 `references/evidence-provenance.md` 标注 primary、confirmatory、exploratory 或 superseded，并按 `references/acceptance-statuses.md` 选择状态，再同步更新 Mermaid、测试矩阵、节点表、工作流状态与 ReAct 日志。
18. 在切换路线或终点前，把原定义、新定义、证据、必要性变化和决策写回契约、台账与 TASK。
19. 使用 `references/evaluation-policy.md` 中的 A/B/C 等级验证阶段结果。
20. 所有必要叶子达到门槛后执行 G1。G2 前必须先用外部实现重算原始成功请求的签名、密文或关键派生值；若预检不一致，先修 G1，不发送网络请求。
21. 对以“可重发请求”“服务端接受”或“完整请求交付”为目标的路线，再执行一次受控 G2；目标包含业务结果时继续执行 UAT。

如果无法确认授权，或任务要求提取真实凭据、绕过第三方访问控制、隐藏有害活动，或将采集扩大到授权靶场之外，立即停止。

## 主流程

沿以下主线推进：

```text
目标与授权
→ UAT / G2 / G1 验收契约
→ 目标 URL 与请求样本
→ 若目标 URL 不可见：抓包可见性分层与业务网络通道识别
→ bridge/RPC/容器通道确认（按需）
→ 响应路径与网络出口确认（按需）
→ 目标接口确认
→ 展开注册、Token、配置与设备签发的前置接口 DAG
→ 建立 Mermaid 核心控制面与请求构造依赖台账
→ Smoke 环境检查
→ 参数归约与最小请求
→ 展开不透明层
→ 追加新暴露字段
→ 选择交付路线与输入边界
→ 评估替代构造与真实性要求
→ Red：选择当前路线的必要叶子
→ Green：最小实验取得预定证据
→ Refactor：整理脚本、fixture、TASK 或 Skill
→ 响应模型提取（按需）
→ 业务接口地图、复合接口与语料库构建（按需）
→ 按路线构造请求
→ G1 离线等价
→ 原始成功请求签名/密文预检
→ G2 受控端到端（按目标）
→ UAT 最终验收（按目标）
→ 工具交付
```

仅在出现相应证据时进入阻塞分支：

- 无法理解流量：进入流量与数据形态分析。
- 普通代理有流量但目标业务 host/path、operation 或响应实体缺失：进入业务网络通道识别；不要继续停留在代理端口、证书或 HTTP/2 排查。
- 无法在 Java 中定位目标值：进入静态搜索、调用栈追踪或运行时类型确认。若当前红灯是 `sign`、`token`、摘要、HMAC、AES/DES/RSA 或密文字段的算法入口未知，且怀疑使用 Java 标准 Crypto API，先走 `trace-android-java` 的 crypto-probe 模式生成候选 JSONL fixture；有候选后交给 `reproduce-android-crypto`，无候选再回到业务边界 Hook、Native/JNI 或运行态代发路线。
- 逻辑进入 JNI：先用 `prepare-android-native-toolchain` 通过 Smoke-Native，再用 `map-android-jni` 恢复注册映射；随后按问题在 objdump、IDA 或交叉验证中选择静态路线，再用 `hook-android-native` 观察真实输入、分段、调用者与输出。
- 动态插桩无法附加：先诊断 so 加载时机、环境检测、Frida 检测或 ptrace，不要立即推翻算法假设。
- 已定位算法但难以移植：根据依赖选择 Python、Frida RPC、自建 Android 应用重载 so 或 Unidbg。
- 已确认算法位于 `.so` 且目标是脱离真机反复执行：进入 Unidbg 路线。先用 `prepare-unidbg-toolchain` 做桌面 Smoke；再用 `run-so-with-unidbg` 建立 G1；遇到 Java/Android 对象缺失时用 `patch-unidbg-environment` 最小补环境；最后用 `validate-android-reproduction` 声明交付等级和未覆盖边界。
- Unidbg 已离线输出 token、签名或密文，但补环境包含设备态、账号态、StackTrace、`/proc`、TEE 或时间/随机数 fixture：保留离线 Green，状态写为 `partial-validated`，再按目标决定是否新开 device-assisted 对齐 TASK；不得把 fixture 输出直接升级为真实请求可用。
- 静态代码可见但符号短且 JADX 别名无法 Hook：进入混淆符号映射。
- JADX 只见壳代码、运行时业务类缺失：进入 Dex 恢复。
- G2 被图片验证码、短信码或人工确认阻塞：进入交互式验证关口，不把验证码当普通算法字段。
- GUI 抓包无法完成可重复字段提取或单变量修改：进入脚本化流量处理。
- 容器化小程序、统一网关或 RPC 证据出现时：先按 `identify-android-business-network-channel` 确认 bridge request、response callback、network exit 和 operationType，再决定是否进入参数归约或主动调用。
- 已确认 RPC/bridge 响应模型且目标变成页面接口地图、复合业务接口、ID 去重、多入口语料或批量窗口验证时：进入 `build-android-rpc-data-corpus`；该分支必须声明覆盖率，不得把单入口 `hasNext=false` 写成业务全量。
- 浏览器代理正常而目标 App 完全没有连接进入代理：先进入 VPN/tun2socks 强制转发；流量进入后再分别判断 TLS 信任、Pinning、QUIC 或 VPN 检测。
- 课程或历史经验声称存在抓包红灯，但当前普通代理同窗口已可抓到目标连接：标记 `not-reproduced`，不要把备用路径验证写成“已绕过反抓包”。
- 已定位字段读取入口但不清楚缓存、持久化、首次生成和来源分支：进入动态字段来源闭环。
- 字段来自前置接口响应：先展开接口 DAG、响应字段、时效、持久化和后续绑定，再决定能否外部获取或替代。
- G1 已通过而 G2 返回风控、TFS 或环境拒绝：进入运行态/设备态/传输上下文归因，不得无证据回滚算法 Green。
- G2 返回 `403/406/418`、CloudWAF 或业务空结果时，读取 `references/g2-rejection-taxonomy.md` 做首差分层；不要把服务端拒绝直接归因到代理或算法。
- Unidbg 出现环境缺失：进入最小补环境流程。

不得把所有分支都设置为固定必经步骤。

## 证据规则

每项结论至少记录：

- 目标与授权范围；
- 原始请求或离线 fixture；
- 实际观察到的输入和输出；
- 代码位置、类/方法、JNI 签名、模块或偏移；
- 使用的工具、命令或 MCP；
- 当前置信度和仍未排除的解释；
- 下一步操作及完成条件。

对“目标 URL 起初不可见”的任务，还必须记录：

- 目标业务动作和 UI/UAT 结果；
- 普通代理可见的 host、方法、连接形态和缺失的业务语义；
- 已排除的代理入口、证书、HTTP/2/HTTP3/QUIC、冷启动窗口问题；
- bridge/RPC operation、响应回调、最终网络出口和 response model 的状态。

同时按 `references/evidence-provenance.md` 标注证据角色。工具曾经参与探索，不代表其输出自动成为 Green 证据。

优先采用实际运行值，不要仅根据代码外观猜测语义。保留指向课程原始小标题、代码、截图或生成产物的链接。

## 请求构造依赖台账

`request-construction-ledger.md` 是每个目标 URL 的主轴文件，不是某个阶段的临时清单。所有子 Skills 都必须读取并更新自己处理的节点。

Mermaid 是该台账的核心控制面，不是装饰性结果图。总编排每次选择下一步之前必须先读取图和节点表；图中唯一 `NEXT` 节点就是当前要执行的最小实验。若图、表、测试矩阵与证据不一致，以最低状态为准。

节点的“取值能力状态”必须区分：

- `observed`：只看到一次运行时值；
- `substitute-valid`：非 App 原始生成值，但在明确范围内通过格式、结构或受控行为验证；
- `hook-available`：可通过稳定 Hook 再次取得；
- `rpc-available`：可调用目标进程中的方法再次生成；
- `located`：已定位生成位置或输入来源；
- `understood`：已解释完整生成逻辑及依赖；
- `reproducible`：可在目标进程外或约定执行环境中独立生成；
- `validated`：生成值已与 App、fixture 或服务端结果对照；
- `not-required`：经归约证明不影响目标请求；
- `blocked`：存在明确环境或证据阻塞。

通道与交付阶段还必须区分：

- `channel-confirmed`：已确认目标业务走容器、RPC、统一网关、长连接或 native 等通道；
- `bridge-request-confirmed`：已确认页面动作对应的 bridge method、RPC operation 或 service name；
- `response-confirmed`：已确认响应回调或返回对象携带目标业务实体；
- `network-exit-confirmed`：已确认最终服务端出口、方法、关键头和 body 骨架；
- `response-model-confirmed`：已提取顶层状态、分页字段、主业务实体和敏感字段边界；
- `app-internal-rpc-call-passed`：已在目标 App 运行态主动调用目标 RPC 或方法；
- `frida-rpc-tool-passed`：已封装为可重复调用的 Frida RPC 工具；
- `app-runtime-dispatch-planned`：已决定使用 App 运行态代发请求或消息；
- `app-runtime-dispatch-dry-run-passed`：App 运行态代发 dry-run、语法和 payload 检查通过；
- `app-runtime-dispatch-smoke-passed`：R4-A/R4-M App 代发 smoke 已成功；
- `r3-precheck-complete`：已完成纯外部重放可行性预检；
- `blocked-by-runtime-boundary`：纯外部重放受登录态、设备态、TEE、签名、风控或人工边界阻塞。
- `crypto-probe-observed`：已观察到标准 Java Crypto API 事件，但尚未证明该事件属于目标字段；
- `fixture-candidate`：探针事件与目标字段形态、窗口或调用栈相符，仍需筛选；
- `fixture-selected`：已选择一组探针事件作为 Unit/G1 复现输入。

必要性必须按路线分别记录。一个字段可以同时是“替代值当前可用”“Hook 可稳定取得”“纯 Python 真实生成链仍未还原”。`substitute-valid` 只证明当前范围可用，不等于 `reproducible` 或 `validated`。详细规则见 `references/substitute-construction-policy.md`、`references/execution-route-policy.md` 和 `references/request-construction-ledger.md`。

Mermaid 图、测试矩阵与节点表是同一台账的三个视图：

- Mermaid 图：展示“UAT → G2 → G1 → 路线门槛”的终点链，以及“请求参数 → TASK → 破解方法 → 解析结果 → 新叶子”的递归过程；
- 测试矩阵：保存 Smoke、Unit、G1、G2 和 UAT 的 Red/Green 条件、状态与证据；
- 节点表：保存生成逻辑、依赖、证据、置信度和下一动作。

每次节点状态、路线必要性、测试状态、终点定义发生变化，或发现新叶子、创建子 TASK 时，必须同步更新三者。Mermaid 规范见 `references/mermaid-request-tree.md`。

## 测试驱动规则

每个工具动作必须指向 Mermaid 中的一个红灯或测试关口，并在执行前声明预期证据。

按 `references/evidence-driven-tdd.md` 使用：

- Smoke：验证实验环境和观察链；
- Unit：验证单个字段、算法和边界条件；
- G1：固定输入下验证外部实现与 App 离线等价；
- G2：按授权和副作用约束发送一次完整请求；
- UAT：验证最终业务或研究交付。

每轮在 `logs/LOG.md` 记录 Reason、Action、Observation、Decision。先记录观察，再更新假设。测试失败时先定位首个差异层级，不得同时改动多个独立变量。

## 工具规则

用与具体 MCP 实现无关的方式表达任务意图。例如提出“恢复 Java Native 方法到 so 函数的映射”，再根据当前条件选择 Frida、JADX、IDA、Ghidra 或 Unidbg 集成。

调用工具前：

1. 检查工具是否可用以及版本是否兼容。
2. 明确本次调用应该产生什么证据。
3. 避免破坏性操作和不必要的宽范围操作。
4. 将结果写入工作流状态。
5. MCP 不可用时，使用人工操作或脚本作为降级方案。

通用工具契约见 `references/mcp-contract.md`。

## 子 Skills

委派任务前先阅读 `references/capability-registry.md`。只有在学完对应视频 Day，并通过课堂 evaluation 明确能力边界后，才创建相应子 Skill。

每次委派必须指定 TASK 工作区、目标阶段、对应红灯、Green 条件和预期证据。子 Skill 返回后，先更新 Mermaid、测试矩阵和节点表，再更新阶段 output、`00-工作流状态.yaml` 和 `logs/LOG.md`。

人机协作循环：

```text
总编排定义目标
→ capture-android-traffic 生成抓包操作手册
→ 人类执行、机器采集
→ analyze-android-traffic 形成候选
→ analyze-android-traffic 生成验证操作手册
→ 人类反馈、机器判定
→ 确认接口或返回下一轮采集
→ minimize-android-request 归约必要参数
→ 形成最小请求并路由动态字段
→ resolve-android-dynamic-field 闭环字段生命周期
```

目标 URL 不可见时的通道识别循环：

```text
目标业务动作和 UAT
→ capture-android-traffic 形成抓包 Red 分层
→ non-target-only
→ identify-android-business-network-channel
→ bridge/RPC operation
→ response callback
→ network exit
→ response model
→ 选择 R2 App 内主动调用、R3 外部重放或 R4 组合路线
```

业务 RPC 语料分支：

```text
bridge/RPC operation 已确认
→ model-android-rpc-response 建立响应模型
→ export-frida-rpc 建立可重复 App 内主动调用
→ build-android-rpc-data-corpus 建立接口地图、复合接口、source/evidence 与批量护栏
→ 按 single-page / paged-window / multi-entry-corpus / full-claimed 声明覆盖率
→ 回写 TASK、日志、UAT 和最终交付边界
```

恢复分支循环：

```text
Smoke 或静态分析 Red
→ diagnose-android-instrumentation / analyze-android-obfuscation / recover-android-dex
→ 明确失败层与最小恢复实验
→ Green 后返回原请求节点
```

交付路线补充：

```text
Native 算法难以移植
→ export-frida-rpc（借用原 App）
→ host-android-native-library（自建 Android 宿主）
→ run-so-with-unidbg（桌面模拟）
→ 根据交付环境选择，不把路线混报
```

Unidbg 桌面离线路线：

```text
Native/.so 算法节点
→ assets/native-unidbg-task-template.md 创建 TASK
→ prepare-unidbg-toolchain：JDK、Maven、ASCII 工作副本 Smoke
→ run-so-with-unidbg：APK/so/JNI_OnLoad/签名主动调用
→ patch-unidbg-environment：按报错 signature 补 Java、Android 或 App 对象
→ validate-android-reproduction：Unit、G1、可选 G2/UAT 与交付边界
→ 回写台账、能力注册表与课程评测
```

Unidbg 的 Green 只说明声明输入下的离线函数或算法复现通过。若目标是完整外部 HTTP 请求，还必须继续走原始成功请求预检、G2 与 UAT；若目标只是课堂算法、离线工具或本地 Jar/CLI，G2 可以明确标为 `not-required`。

复杂安全 SDK 的 Unidbg 结果要额外声明：

- 哪些值来自真实 Java 调用；
- 哪些值来自 Android/App fixture；
- 是否存在工具层补丁或 runner 控制；
- 输出是否稳定；
- 是否需要真机 Hook 对齐后才能进入 G2。

Native 分支循环：

```text
Java native 声明
→ prepare-android-native-toolchain 验证 ABI、模块与工具
→ map-android-jni 恢复类、签名、模块、偏移与 Thumb
→ 按问题选择 static-first / dynamic-first / hybrid
→ analyze-android-native-static 确认结构和窄 Hook 候选（按需）
→ hook-android-native 获取同次输入分段、调用顺序与输出
→ reproduce-android-crypto 建立 Unit 与 G1
→ 总编排更新 Mermaid、测试矩阵与唯一 NEXT
```

静态分析不是固定必经同一种工具：

- 偏移窄、只需调用指令时，选择 objdump；
- 需要复杂控制流、伪代码、xref 或 JNI 对象构造时，选择 IDA；
- 教学复现、高置信度交付或工具边界不一致时，选择 cross；
- 主路线已完成后补做 IDA，作为非阻塞增强 TASK，不回滚已通过的 G1/G2。
- 只需 JNI 入口参数或返回值时可 dynamic-first；需要内部调用点、降低通用算法噪声或动态附加困难时 static-first；静态结构和真实参数互相校正时 hybrid。

增加子 Skill 时：

1. 使用 `skill-creator/scripts/init_skill.py` 初始化。
2. 只赋予它一项能够产生证据的职责。
3. 定义输入、输出、完成标准和交接方式。
4. 在调用方课程 TASK 的 `evaluations/` 中增加对应评测，模板使用 `assets/evaluation-template.md`。
5. 更新能力注册表。

## 完成标准

阶段评测可以达到 A/B/C。整条 URL TASK 只能相对于明确路线报告完成：

1. 已声明路线、运行环境和输入边界；
2. 已定义 UAT、G2、G1 和各层通过证据；不需要的关口明确标为 `not-required`；
3. Smoke 通过，或与最终交付无关的缺项有明确说明；
4. 台账中该路线的所有必要叶子达到对应门槛：Hook 路线至少 `hook-available`，RPC 路线至少 `rpc-available`，纯外部路线至少 `reproducible`；
5. 请求方法、URL、必要请求头、序列化、签名、加密和正文均有证据；
6. 离线等价关口通过：固定 fixture 的关键中间值和最终请求字节与 App 一致；
7. 若目标包含真实重发，受控端到端关口通过：单次低频请求取得预期 HTTP 状态和业务响应，并保存请求清单与响应证据；
8. 若目标包含业务效果，UAT 通过且记录因果归因边界；
9. 当前路线不存在未解释的必要节点，Mermaid 中不存在未处置的 `NEXT` 或 required 红灯。
10. 若交付目标包含业务接口地图、复合接口或数据语料库，必须额外给出 source/evidence、批量护栏、覆盖率状态和未覆盖边界；除非有独立 total 或交叉验证，不得声明全量。

阶段复现等级：

- A：固定输入能够精确复现课堂或目标应用的结果；
- B：动态值不同，但结构、算法和当前样本中的对应关系等价；
- C：环境阻塞导致无法完成最终请求，但已经复现必要的阶段性证据，并可重复说明阻塞原因。

取得一次运行时值只能标为 `observed`。稳定 Hook 可以完成运行时取值路线，但不能据此宣称纯 Python 路线完成；调用 App 内方法的 RPC 路线也不能宣称算法已独立移植。

离线密文完全一致不能自动推出服务端已接受完整 Python 请求。相反，服务端返回成功也不能单独证明算法真实还原；两个关口必须分别记录。

G2 失败也必须按首差分层：

1. 原始成功请求能否由外部实现重算出相同 sign/密文；
2. 外部请求的 URL、方法、头部、正文原始字节是否一致；
3. 前置 Token、did、Cookie 和时间状态是否有效且相互绑定；
4. 仍失败时，才登记运行态、设备态、TLS/连接态或服务端策略上下文。

只有第 1 层失败时才能直接回滚算法 Green。

替代构造可以完成明确声明的“功能可用路线”，但不能据此宣称已还原 App 本质。若目标涉及登录、支付、风控、设备注册、历史连续性或多标识绑定，不得默认采用替代值。

## 参考资料

- 开始任务、定义测试层和选择红灯时读取 `references/evidence-driven-tdd.md`。
- 创建和更新请求主轴时读取 `references/request-construction-ledger.md`。
- 判断 Hook 后是否仍需追上游、选择交付路线时读取 `references/execution-route-policy.md`。
- 评估随机值、格式等价值或伪设备字段能否替代真实生成链时读取 `references/substitute-construction-policy.md`。
- 创建或更新可视化任务树时读取 `references/mermaid-request-tree.md`。
- 创建 TASK 目录时读取 `references/task-workspace-contract.md`。
- 创建 Native/.so/Unidbg 类 TASK 时读取并复制 `assets/native-unidbg-task-template.md`。
- 选择下一未解决叶子时读取 `references/routing.md`。
- 区分工具参与、正式证据和独立复核时读取 `references/evidence-provenance.md`。
- 需要按课程资料查找高级分支讲解、脚本、样本或平行路线时，读取 workflow 顶层 `../../../references/kanxue-course-directory-index.md`；采用后回写 `../../../references/course-provenance.md`。
