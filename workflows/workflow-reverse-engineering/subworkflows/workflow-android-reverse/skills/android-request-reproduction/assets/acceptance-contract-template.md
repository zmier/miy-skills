# `<目标行为>` 验收与测试契约

## 目标、授权与副作用

- 授权范围：
- 最终目标：
- 目标请求：
- 业务副作用：
- 允许发送次数：
- 禁止动作：

## 以终为始

### UAT 最终验收

- 最终可观察结果：
- 操作前基线：
- 操作步骤：
- 通过条件：
- 因果归因方式：
- 状态：`not-required / not-run / failed / blocked / blocked-by-boundary / passed / passed-with-scope`
- 证据：

### G2 受控端到端

- 是否要求：`yes / no`
- 原始成功请求预检：
- 预检的 sign/密文/关键派生值：
- 完整请求的输入边界：
- HTTP 通过条件：
- 业务码通过条件：
- 请求 manifest：
- 响应证据：
- 状态：`not-required / not-run / failed / blocked / blocked-by-boundary / passed / passed-with-scope`

### 前置接口 DAG

| 接口节点 | 产生的字段 | 时效/生命周期 | 持久化位置 | 下游消费者 | 状态 |
|---|---|---|---|---|---|
| | | | | | |

### G1 离线等价

- 固定 fixture：
- 固定输入：
- 必比中间层：
- 最终字节比较：
- 首差报告：
- 状态：`not-run / failed / blocked / passed / passed-with-scope`

## 交付路线

- 当前主路线：`R1 / R2 / R3 / R4`
- 允许依赖的运行环境：
- 业务输入边界：
- 真实性要求：`functional-equivalent / app-authentic`
- 当前路线完成门槛：

## 测试矩阵

| ID | 层级 | 对象 | Red/通过条件 | 状态 | 证据 |
|---|---|---|---|---|---|
| `S-01` | Smoke | 设备与工具链 | ADB、代理、进程和插桩链可用 | `not-run` | |
| `S-RED-01` | Smoke | 预期红灯复现 | 课程或经验中的 Red 在当前同窗口复现；未复现写 `not-reproduced` | `not-run` | |
| `U-01` | Unit | `<字段或算法>` | 固定输入与 App fixture 一致 | `not-run` | |
| `G1` | G1 | 完整构造链 | 中间值和最终字节离线等价 | `not-run` | |
| `G2` | G2 | 完整 HTTP 请求 | HTTP 与业务响应满足契约 | `not-required` | |
| `UAT-01` | UAT | 最终目标 | 最终现象满足契约且可归因 | `not-required` | |

## 当前红灯

- 节点或测试 ID：
- 为什么阻塞当前路线：
- 下一项最小实验：
- 预期产生的证据：
- 对应 TASK：

## 终点变更记录

| 日期 | 原终点或路线 | 新终点或路线 | 新证据与原因 | 受影响测试和叶子 |
|---|---|---|---|---|
