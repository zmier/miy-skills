# 验收状态语义

## 状态表

| 状态 | 含义 | 使用边界 |
|---|---|---|
| `not-run` | 尚未执行该关口 | 默认初始状态 |
| `passed` | 已达到预先声明的 Green 证据 | 必须有证据链接或可重复命令 |
| `failed` | 已执行且未达到 Green | 必须记录首个差异层级 |
| `blocked` | 存在明确外部条件阻塞 | 阻塞条件应可观察、可复查 |
| `not-required` | 当前路线或目标不需要该关口 | 必须说明为何不影响终点 |
| `not-reproduced` | 预期 Red 在当前环境没有复现 | 用于课程、历史经验或他人报告的故障对照 |
| `blocked-by-boundary` | 受授权、安全、账号、验证码或人工边界阻塞 | 不得为了通过而扩大授权边界 |
| `passed-with-scope` | 在声明范围内通过，但不覆盖更强结论 | 适合备用路径、阶段性 UAT 或环境差异结论 |
| `partial-validated` | 核心链路已跑通并有可重复证据，但仍缺少更强范围的对齐或端到端验证 | 适合 Unidbg 离线输出已成立、但真实设备态/账号态/服务端 G2 尚未验证 |
| `channel-confirmed` | 已确认目标业务的网络/容器/RPC 通道 | 只证明通道，不证明请求已可复现 |
| `bridge-request-confirmed` | 已确认页面动作对应的 bridge method、RPC operation 或 service name | 用于小程序、容器、RPC 场景 |
| `response-confirmed` | 已确认目标业务响应从回调或返回对象出现 | 需要同一动作窗口的请求/响应证据 |
| `network-exit-confirmed` | 已确认最终服务端出口、方法、关键头和 body 骨架 | 不等于外部 Python 可重放 |
| `response-model-confirmed` | 已提取响应 JSON 的主实体、分页和敏感字段边界 | 工具化前建议达到 |
| `app-internal-rpc-call-passed` | 已在目标 App 运行态主动调用目标 RPC 或方法成功 | 属于 R2，不自动推出 R3 |
| `frida-rpc-tool-passed` | 已封装成可重复调用的 Frida RPC 工具 | 应声明输入、输出、生命周期和敏感字段策略 |
| `app-runtime-dispatch-planned` | 已决定使用 App 运行态代发请求或消息 | 属于 R4；需要 allowlist、forbidden list、UAT 和 ReAct 纪律 |
| `app-runtime-dispatch-dry-run-passed` | R4-A/R4-M dispatcher 的 dry-run、语法和 payload 检查通过 | 不代表已发送或业务可用 |
| `app-runtime-dispatch-smoke-passed` | App 运行态代发 smoke 已成功并返回预期业务响应 | 证明 R4-A/R4-M 当前样本可用，不推出 R3 可复现 |
| `r3-precheck-complete` | 已完成纯外部重放可行性预检 | 可以结论为可行、不可行或边界阻塞 |
| `blocked-by-runtime-boundary` | 纯外部重放受运行态、设备态、TEE、签名、风控上下文阻塞 | 保留 R2 Green，不回滚通道或响应模型结论 |
| `blocked-by-connection-state` | 外部复现或消息代发受长连接 session、心跳、requestId、callback 或连接环境阻塞 | 用于 R4-M/长连接路线 |
| `blocked-by-server-window` | 服务端分页窗口、账号冷却、频控、验证码或压力反馈要求停止 | 不得通过提高并发、换账号或代理池继续 |

## 使用规则

1. 课程或经验中的红灯必须先在当前设备、版本和动作窗口中复现；未复现时标记
   `not-reproduced`，不要写成 `passed`，也不要把备用实验写成故障修复。
2. 技术链路可用但没有证明原始故障存在时，标记 `passed-with-scope`。例如备用
   抓包拓扑可用，但普通代理红灯未复现。
3. 授权、登录、验证码、短信码或真实账号边界阻塞时，标记
   `blocked-by-boundary`，不要把它混入算法失败。
4. `blocked` 需要下一步可执行恢复实验；`blocked-by-boundary` 需要用户改变授权或
   提供测试条件，否则不得继续突破。
5. 每次状态改变都要更新测试矩阵、Mermaid 节点、TASK 总表和 ReAct 日志。
6. R2 App 内主动调用、R4 App 运行态代发与 R3 纯外部重放必须分别标状态；`app-internal-rpc-call-passed` 和 `app-runtime-dispatch-smoke-passed` 不得改写成 `reproducible` 或 `target-request-green`。
7. `partial-validated` 必须说明“已验证什么”和“未验证什么”。例如 Unidbg 已离线输出 native token，只能证明声明 fixture 下的函数路径可执行；若设备态、账号态、真实请求或服务端接受尚未对齐，G2/UAT 仍保持 `not-run`、`blocked` 或 `not-required`。
