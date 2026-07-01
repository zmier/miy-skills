---
name: resolve-android-dynamic-field
description: 在经过授权的 Android 请求复现任务中，闭环单个动态字段的读取、缓存、持久化、首次生成、来源分支、编码转换、替代构造和字段绑定。用于请求体或请求头中的 did、device-id、buvid、fp_local、session_id、时间戳、安装标识等字段已经定位到 Java 方法，但仍需回答“当前值从哪里读取、清数据后如何生成、能否用替代值、怎样用 Frida 与 Python 交叉验证”。协调 JADX、Frida 和算法复现，并把字段子树写回 request-construction-ledger.md。不得用于提取真实凭据、规避第三方访问控制或未授权设备指纹伪造。
---

# Android 动态字段来源闭环

## 目标

把“已经找到字段取值方法”推进为可审计的字段生命周期：

```text
请求字段
→ 当前读取入口
→ 内存缓存
→ 本地持久化或服务端下发
→ 首次生成条件
→ 原始来源与分支
→ 编码或变换
→ 当前值、替代值和真实重建的验证
```

本 Skill 不代替静态分析、Hook 或算法实现，而是定义它们围绕单个字段如何协作。

## 输入

- TASK 工作区和 `request-construction-ledger.md`；
- 字段节点 ID、请求位置和必要性；
- 当前交付路线与真实性要求；
- JADX 中的读取入口或最接近的已定位方法；
- 可用的运行时 fixture、持久化样本或授权设备。

读取入口尚未定位时返回 `locate-android-request-builder`。需要真实实参或分支确认时调用 `trace-android-java`。已知算法需要外部实现时调用 `reproduce-android-crypto`。

## 工作流

1. 从 `assets/dynamic-field-ledger-template.md` 复制字段子任务说明。
2. 按 `references/field-lifecycle.md` 区分“读取当前值”和“首次生成新值”。
3. 按 `references/common-field-patterns.md` 判断它属于多来源稳定标识、持久化会话随机值、复合设备指纹还是其他模式。
4. 若字段涉及 DID、UTDID、APDID、apdidToken、umidToken、devKeySet、miniwua、authorization、Sign、Cookie、设备注册或服务端风控，读取 `references/device-state-bundle.md`，先判断它是否属于设备态字段束。
5. 若入口通过接口或门面返回值，先确认运行时实现类型，再静态追踪实际实现。
6. 静态追踪返回顺序：内存、SharedPreferences/数据库/文件、系统 API、服务端响应、随机或算法生成。
7. 若来自服务端响应，建立前置接口节点：请求输入、响应字段、过期时间、刷新条件、持久化位置和全部下游消费者。
8. 记录清空内存、清应用数据、重装和换设备分别会影响哪一层；不得为了观察首次生成而直接破坏用户数据。
9. 为每个分支声明输入、触发条件、规范化规则、输出和持久化位置；map key 的语义以运行时值和采集函数为准，不按名称猜测。
10. 判断真实性要求：
   - 只要求当前授权场景功能等价时，可评估替代构造；
   - 要求指定设备原值或完整移植时，必须恢复真实生成链。
11. 按交付路线分别判断必要性：R1/R2 可由 App 运行态提供的字段，不自动阻塞；R3 纯外部重放需要的字段必须继续追踪或标记边界阻塞。
12. 用最小 Frida 只读调用或 Hook 确认当前分支、原始来源和最终返回值。
13. 用 Python 或其他外部实现复现可移植的规范化、编码和算法。
14. 随机或时间参与时，把随机字节和时间设计为可注入输入，用同一次 App fixture 做确定性比较。
15. 至少完成一次 `source → generated value` 对照；算法可逆时再做反向解释。
16. 检查字段与账号、Cookie、其他设备字段、安装状态、前置 Token 和历史状态的绑定。
17. 按 `references/writeback-contract.md` 更新字段任务、请求台账 Mermaid、节点表、工作流状态和 ReAct 日志。

## 状态判断

- `observed`：只取得一次当前值。
- `located`：定位到读取或生成方法。
- `understood`：缓存、持久化、生成分支和输入已解释。
- `substitute-valid`：替代值仅在声明范围内可用。
- `bundle-bound`：字段属于多字段设备态、会话态或安全 SDK 字段束；单独替换不可信。
- `do-not-substitute`：字段可读取，但当前证据显示替换会破坏字段束一致性、登录态或授权边界。
- `app-runtime-provided`：当前路线借用目标 App 运行态时由 App 自动提供；适用于 R1/R2，不代表外部可生成。
- `must-reverse-for-r3`：若目标是纯外部 Python/CLI 重放，该字段仍需继续逆向。
- `blocked-by-runtime-boundary`：字段依赖登录态、设备态、TEE、风控上下文、真实账号或授权边界，当前不适合继续外部复现。
- `reproducible`：真实生成规则可从声明输入重建。
- `validated`：重建结果与 App、持久化、fixture 或授权行为交叉验证。

不得因为能读取持久化值就宣称首次生成逻辑已复现，也不得因为随机替代值可用就覆盖真实生成分支。`app-runtime-provided` 只能说明当前 App 内路线可用；如果切换到 R3，必须重新计算该字段是否 required。

## 完成标准

- A：读取链、首次生成链、来源分支和变换均已解释，外部实现与 App 当前值或新生成值一致。
- B：当前值读取和编码已验证，但某个首次生成来源受设备或系统版本限制。
- C：已定位字段入口并明确唯一缺失层，例如持久化实现、运行时分支或系统来源。

完成后必须说明结论适用于当前值读取、首次生成、替代构造还是完整真实重建。

若字段只在 R3 中阻塞，完成说明必须写成：

```text
R2: app-runtime-provided / not-blocking
R3: must-reverse-for-r3 或 blocked-by-runtime-boundary
证据: 对应 Hook、响应、请求或框架调用链接
```

## 参考资料

- 拆解字段生命周期时读取 `references/field-lifecycle.md`。
- 识别 BUVID、session_id、fp_local 一类常见字段结构时读取 `references/common-field-patterns.md`。
- 识别 DID、UTDID、APDID、apdidToken、umidToken、miniwua、authorization、Sign 与设备态绑定时读取 `references/device-state-bundle.md`。
- 写回 TASK 与请求构造台账时读取 `references/writeback-contract.md`。
