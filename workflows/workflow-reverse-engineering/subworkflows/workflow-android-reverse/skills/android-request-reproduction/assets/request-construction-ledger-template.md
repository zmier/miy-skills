# `<METHOD> <URL>` 请求构造依赖台账

> 核心原则：以终为始，以证据校正，以测试推进。

## 目标、授权与输入边界

- 授权范围：
- 最终业务或研究目标：
- 目标请求：
- 业务输入：
- 业务副作用：
- 允许发送次数：
- 当前主路线：`R1 / R2 / R3 / R4`
- 当前分析路线：
- 当前 TASK 角色：`blocking / confirmatory / enhancement`
- 真实性要求：`functional-equivalent / app-authentic`
- 验收契约：[[acceptance-contract]]

## 终点与测试状态

| 层级 | 通过条件 | 状态 | 证据 |
|---|---|---|---|
| Smoke | 设备、代理、进程、插桩和脚本环境满足本轮实验 | `not-run / failed / blocked / passed` | |
| Unit | 当前字段或算法固定 fixture 通过 | `not-required / not-run / failed / blocked / passed` | |
| G1 离线等价 | 固定输入下关键中间值和最终字节与 App 一致 | `not-run / failed / blocked / passed` | |
| G2 受控端到端 | 一次完整请求获得预期 HTTP 与业务响应 | `not-required / not-run / failed / blocked / passed` | |
| UAT 最终验收 | 最终现象满足验收契约并记录归因边界 | `not-required / not-run / failed / blocked / passed` | |

## 当前红灯与 NEXT

- 当前红灯节点或测试 ID：
- 为什么阻塞终点：
- 下一项最小实验：
- Green 条件：
- 预期证据：
- 对应 TASK：

## 交付路线矩阵

| 路线 | 运行环境与输入边界 | 状态 | 完成门槛 | 当前缺口 |
|---|---|---|---|---|
| R1 运行时 Hook | App + Frida；从稳定 Hook 点取值 | `not-started` | 必要字段均 `hook-available`，组合结果验证通过 | |
| R2 Frida RPC | App + Frida；调用目标方法生成 | `not-started` | 必要输出均 `rpc-available`，结果验证通过 | |
| R3 纯外部独立生成 | 不依赖目标进程；从声明业务输入开始 | `not-started` | 必要叶子均 `reproducible`，组合结果 `validated` | |
| R4 组合路线 | 明确设备端与外部端的责任边界 | `not-started` | 每个环节达到约定能力门槛 | |

## 分析路线与证据角色

| 分析路线或工具 | TASK 角色 | 证据角色 | 目标问题 | 落盘产物 | 状态 |
|---|---|---|---|---|---|
| | `blocking/confirmatory/enhancement` | `primary/confirmatory/exploratory/superseded` | | | |

## Mermaid 核心控制面

```mermaid
flowchart TB
  UAT["⏳ UAT：最终业务或研究目标"]
  G2["⏳ G2：完整请求被服务端接受"]
  G1["⏳ G1：固定输入离线等价"]
  ROUTE["🟡 当前路线：R?"]
  SMOKE["⏳ Smoke：环境与观察链"]

  REQ["🟡 METHOD /target"]
  HEADERS["请求头"]
  BODY["请求体"]
  HEADER_A["⚪ Header-A = ?"]
  BODY_RAW["⚪ body = 当前可见形态"]
  PRE_API["⚪ 前置接口：注册/Token/配置"]
  SERVER_FIELD["⚪ 服务端下发字段"]
  RECOVERY_RED["❌ 环境/静态/交互红灯"]
  RECOVERY_TASK("恢复 TASK")
  RECOVERY_SKILL{{"诊断或恢复 Skill"}}
  RECOVERY_GREEN(["✅ 观察链恢复"])

  TASK_DECODE("TASK-N：解开 body")
  METHOD_DECODE{{"方法：JADX + Frida + 解码/解密"}}
  RESULT_DECODE(["解析结果"])
  P_A["⚪ paraA = ?"]

  UNIT_A["⏳ U-01：paraA 固定 fixture"]
  TASK_HOOK("TASK-M：运行时取值")
  HOOK_RESULT(["🟣 Hook 可稳定取得 paraA"])
  TASK_UPSTREAM("TASK-K：追 paraA 上游（仅 R3 必需）")
  NEXT{{"NEXT：执行当前最小实验"}}

  UAT -->|"需要协议成功"| G2
  G2 -->|"需要完整构造"| G1
  G1 -->|"按路线计算必要叶子"| ROUTE
  ROUTE -.->|"约束请求树"| REQ
  SMOKE -.->|"环境前提"| REQ

  REQ --> HEADERS
  REQ --> BODY
  PRE_API -->|"响应产生"| SERVER_FIELD
  SERVER_FIELD -.->|"供业务请求使用"| BODY
  REQ -.->|"主流程受阻"| RECOVERY_RED
  RECOVERY_RED --> RECOVERY_TASK --> RECOVERY_SKILL --> RECOVERY_GREEN
  RECOVERY_GREEN -.->|"返回原节点"| REQ
  HEADERS --> HEADER_A
  BODY --> BODY_RAW

  BODY_RAW -.->|"为了解开"| TASK_DECODE
  TASK_DECODE -->|"采用"| METHOD_DECODE
  METHOD_DECODE -->|"解出"| RESULT_DECODE
  RESULT_DECODE -->|"发现字段"| P_A
  P_A -.->|"验证生成规则"| UNIT_A
  P_A -.->|"运行时取值"| TASK_HOOK
  TASK_HOOK --> HOOK_RESULT
  P_A -.->|"R3 独立生成"| TASK_UPSTREAM

  NEXT ==>|"解决当前红灯"| TASK_DECODE

  click UAT "tests/uat/UAT-01.md" "打开 UAT"
  click G1 "tests/e2e/G1-offline-equivalence.md" "打开 G1"
  click G2 "tests/e2e/G2-controlled-request.md" "打开 G2"
  click SMOKE "tests/smoke/S-01.md" "打开 Smoke"
  click UNIT_A "tests/unit/U-01.md" "打开单元测试"
  click TASK_DECODE "tasks/TASK-N/TASK-N-说明.md" "打开解码任务"
  click TASK_HOOK "tasks/TASK-M/TASK-M-说明.md" "打开运行时取值任务"
  click TASK_UPSTREAM "tasks/TASK-K/TASK-K-说明.md" "打开上游追踪任务"

  classDef validated fill:#d8f3dc,stroke:#2d6a4f,color:#1b4332;
  classDef hookAvailable fill:#f3e8ff,stroke:#7e22ce,color:#581c87;
  classDef rpcAvailable fill:#dbeafe,stroke:#2563eb,color:#1e3a8a;
  classDef reproducible fill:#dcfce7,stroke:#16a34a,color:#14532d;
  classDef inProgress fill:#fff3bf,stroke:#f08c00,color:#5f3c00,stroke-width:3px;
  classDef pending fill:#f1f3f5,stroke:#868e96,color:#495057;
  classDef failed fill:#ffe3e3,stroke:#c92a2a,color:#7f1d1d;
  classDef notRun fill:#fff9db,stroke:#e67700,color:#7c2d12;
  classDef notRequired fill:#f8f9fa,stroke:#adb5bd,color:#6c757d,stroke-dasharray:5 5;
  classDef task fill:#f3f0ff,stroke:#7048e8,color:#3b2f75,stroke-width:2px;
  classDef method fill:#e3fafc,stroke:#1098ad,color:#0b5965;
  classDef result fill:#fff9db,stroke:#f59f00,color:#664d03;
  classDef next fill:#ffe3e3,stroke:#c92a2a,color:#7f1d1d,stroke-width:4px;
  classDef gate fill:#e7f5ff,stroke:#1971c2,color:#0b3d66,stroke-width:2px;

  class REQ,ROUTE inProgress;
  class HEADER_A,BODY_RAW,P_A pending;
  class UAT,G2,G1,SMOKE,UNIT_A notRun;
  class TASK_DECODE,TASK_HOOK,TASK_UPSTREAM task;
  class RECOVERY_TASK task;
  class METHOD_DECODE method;
  class RECOVERY_SKILL method;
  class RESULT_DECODE result;
  class RECOVERY_GREEN validated;
  class RECOVERY_RED failed;
  class HOOK_RESULT hookAvailable;
  class NEXT next;
```

## 测试矩阵

| ID | 层级 | 对象 | Red 或未完成状态 | Green 条件 | 当前状态 | 证据 |
|---|---|---|---|---|---|---|
| `S-01` | Smoke | 设备与观察链 | 环境尚未确认 | 本轮需要的 ADB、代理、进程和插桩链可用 | `not-run` | |
| `U-01` | Unit | `BODY.PARA_A` | 生成规则未知或 fixture 不一致 | 固定输入与 App 中间值一致 | `not-run` | |
| `G1` | G1 | 完整请求构造链 | 尚未完成离线对照 | 必要中间值和最终字节与 App 一致 | `not-run` | |
| `G2` | G2 | 完整 HTTP 请求 | 尚未获得服务端证据 | HTTP 与业务响应满足契约 | `not-required` | |
| `UAT-01` | UAT | 最终目标 | 最终现象尚未验收 | 结果满足契约并可说明归因边界 | `not-required` | |

## 字段能力与路线必要性

| 节点 ID | 父节点 | 名称与位置 | 当前形态 | 取值能力 | 真实性要求 | 绑定风险 | 验证范围 | R1 | R2 | R3 | R4 | 生成逻辑与依赖 | 原始证据 | 下一动作 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `BODY.PARA_A` | `BODY` | `paraA` | `?` | `unknown` | `app-authentic` | `unknown` | - | `required` | `required` | `required` | `required` | | | |

## 前置接口 DAG

| 接口节点 | 方法与 URL | 输入依赖 | 响应字段 | 时效/生命周期 | 持久化 | 下游节点 | 状态 |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## G2 原始请求预检

- 原始成功请求：
- 外部重算字段：
- 预期：
- 实际：
- 若预检一致但 G2 失败，新增的运行态/设备态/传输上下文节点：

## 替代构造候选

| 字段 | 替代公式 | 适用前提 | 已验证范围 | 未验证绑定 | 失败后路线 | 状态 |
|---|---|---|---|---|---|---|
| | | | | | | `substitute-candidate` |

## 当前未解决叶子

### R1 运行时 Hook

-

### R2 Frida RPC

-

### R3 纯外部独立生成

-

### R4 组合路线

-

## ReAct 当前循环

### Reason

- 当前红灯：
- 为什么优先：

### Action

- 最小实验：
- 只改变的变量：

### Observation

- 直接观察：
- 证据链接：

### Decision

- Green 条件是否达到：
- 更新的节点和测试：
- 新 `NEXT`：

## 终点与路线决策记录

| 日期 | 原终点或路线 | 新终点或路线 | 新证据与原因 | 必要性变化 | 保留证据 |
|---|---|---|---|---|---|

## 完成结论

- Smoke：
- Unit：
- G1：
- G2：
- UAT：
- R1：
- R2：
- R3：
- R4：
- 当前允许声明的完成范围：
- 未验证边界：
