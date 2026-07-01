# Crypto Probe Fixtures

`crypto-probe` 事件来自 `trace-android-java/assets/frida-crypto-probe.js`。它们用于在算法入口未知时生成候选 Unit/G1 fixture。

## 使用位置

```text
sign / ciphertext unknown
→ trace-android-java crypto-probe mode
→ crypto-probe JSONL
→ filter candidate events
→ reproduce-android-crypto comparison ladder
```

## 先筛选再复现

探针事件不能直接等同于目标字段。进入复现前先按以下条件筛选：

- 行为窗口是否匹配；
- 事件时间是否落在目标请求构造附近；
- 算法类型是否符合字段形态；
- 输入/输出长度是否符合请求字段；
- 调用栈是否包含目标包、请求构造类或拦截器；
- 是否有 key、iv、mode 与同一次 `Cipher.doFinal` 对齐；
- 是否存在多个候选，需要建立候选矩阵。

## 证据状态

| 状态 | 含义 |
|---|---|
| `crypto-probe-observed` | 已观察到标准 Java Crypto API 事件 |
| `fixture-candidate` | 事件和目标字段形态相符，但未证明属于目标字段 |
| `fixture-selected` | 已选择某组事件作为 Unit/G1 输入 |
| `reproducible` | 外部实现可复现同一 fixture |
| `validated` | 复现值与 App、原始请求或服务端验证对齐 |

`crypto-probe-observed` 不等于算法已还原。它只是说明“有一条可能相关的标准加密事件”。

## raw 策略

默认使用脱敏事件：

- 保存长度、预览和 hash；
- 摘要/密文输出可保存完整 hex；
- key、iv、明文默认不保存完整 raw。

只有 TASK 明确声明 raw 允许，且目标属于课堂靶场、自有 App 或明确授权样本时，才允许保存完整 key、iv 或明文。raw 必须留在 TASK 证据目录，不进入 Skill。

## 失败解释

无事件不等于无算法，常见原因：

- 算法在 native/so；
- 使用自定义 Java 实现而非标准 Crypto API；
- Hook 时机晚于目标行为；
- 行为窗口没有触发目标请求；
- 目标字段来自服务端下发或缓存；
- 加密过程拆在多个线程或多次调用中。

此时回到总编排重新路由：业务边界 Hook、`locate-android-request-builder`、`map-android-jni`、`hook-android-native` 或运行态代发。
