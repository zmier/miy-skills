---
type: reference
status: structural-green / forward-test-pending
source_case: CASE-260521-基金经理研究
related:
  - workflow-research
  - miy-mail
  - task-driven-project-manager
---

# Literature-Data-Design Handshake

## 一句话

当一个研究项目已经有强参考文献和核心数据，但还需要外部数据库补充变量、机制或 outcome 时，应建立“研究侧 ↔ 数据侧”的握手机制，把文献需求转成可执行取数任务，再把数据交付反向转成 research design scope-lock。

## 适用场景

使用本 reference，当项目出现以下信号：

- 文献已经指出关键变量、proxy、识别窗口或机制，但本项目数据还不完整；
- 需要外部数据库 inventory、字段字典、代码字典、样本覆盖或下载计划；
- 研究侧不应直接把“想要变量”写成模糊请求，而需要给数据侧可执行口径；
- 数据侧已交付 raw / sample / dictionary / processed panel，但研究侧需要判断是否 accepted；
- 数据交付会改变 route portfolio、research design、table shell 或 paperization。

## 双角色协议

| 角色 | 主要责任 | 不应承担 |
|---|---|---|
| Research side | 文献到变量需求的转译；required/optional/deferred 判断；scope-lock；delivery acceptance；route/design 更新 | 不替数据侧猜数据库细节；不在未看 QC 前承诺设计 |
| Data side | 数据库 inventory；raw download；字段/代码字典；parser/QC；coverage report；processed analytical table | 不替研究侧决定理论贡献；不把 P1/P2/P3 无边界铺开 |
| `miy-mail` | 记录 request、reply、scope-lock、acceptance、next action | 不负责真实发送；不替代 TASK 或数据 QC |
| TASK layer | 下载、解析、脚本、台账、日志、产物 | 不定义研究路线本身 |
| Node / route layer | claim、data、design、evidence、threat、contribution 的回挂 | 不保存 raw zip 或执行细节 |

## 状态机

```text
literature signal
→ data need sketch
→ inventory request
→ inventory reply / opportunity scan
→ first-pass download or sample
→ field/code dictionary
→ research-side review
→ scope-lock
→ processed analytical table
→ acceptance / exception
→ research design v1
```

不要把这个状态机理解成所有研究项目的固定线性阶段。它是 R2/R3/R4 交界处的一条 tree-like 子流程，可以被 route portfolio 中的一个或多个 route 调用。

## 产物契约

### 研究侧发起数据请求

至少写清：

- 研究问题或 candidate route；
- 参考文献启发了哪些变量、机制、样本或窗口；
- `required / optional / deferred`；
- 目标粒度；
- 期望交付物；
- 不需要做什么；
- 回复后由谁 review。

推荐模板：

```text
templates/data-side-request-email-template.md
```

### 数据侧交付

至少包含：

- raw / source provenance；
- field dictionary；
- code dictionary 或 unresolved code list；
- sample or full table；
- coverage report；
- QC report；
- known blockers；
- recommended next action。

### 研究侧 review

至少给出：

- short verdict；
- reviewed inputs；
- accepted / accepted-with-exceptions / blocked；
- route/design impact；
- remaining data gaps；
- next request or scope-lock。

推荐模板：

```text
templates/data-delivery-review-memo-template.md
```

## Scope-Lock 原则

当数据侧已经完成 first-pass 与字典/QC 后，研究侧必须从开放式探索切到 scope-lock：

```text
keep: required P0 / selected P1
park: P1C / P2 / P3 / expensive full text / low-priority tables
ask: processed analytical table + QC + coverage
accept: explicit review memo
```

scope-lock 的目标不是停止探索，而是避免数据侧在研究设计尚未吸收已有证据前继续扩大下载面。

## Green 标准

一次 handshake 达到 `structural-green`，至少满足：

- request 和 reply 有 correspondence ledger；
- data-side 交付物有 raw/source provenance；
- 字段/代码字典或 unresolved 列表已交付；
- QC 和 coverage 足够判断研究用途；
- research-side 有 review memo；
- 研究侧明确 accepted / accepted-with-exceptions / blocked；
- 下一步是 processed panel、P1 priority、research design v1 或停止。

达到 `forward-test-green`，需要在未参与本 reference 提炼的新研究项目上复用并通过。

## 常见红灯

| 红灯 | 处理 |
|---|---|
| 文献需求直接变成大而全下载 | 先做 inventory / sample / dictionary，再 scope-lock |
| 数据侧交付 raw table 但无字典/QC | 要求 field/code dictionary + coverage |
| 研究侧只说“看起来可以” | 必须写 acceptance memo，说明 route/design 影响 |
| P1/P2/P3 一起铺开 | 按 required / priority / deferred 分层 |
| 数据沟通只在聊天里 | 用 `miy-mail` 保存 request/reply/decision |
| processed panel 无 exception rows | 保留 QC exception 或审计附录 |

## 子 Skill 升级条件

暂不创建正式子 Skill。若后续至少一个新项目复用成功，可考虑：

```text
skills/research-data-design-handshake/SKILL.md
```

升级前需证明：

- 模板不依赖金融数据库；
- 单人项目和双人协作都能适用；
- 状态机能自然嵌入 route portfolio；
- 至少一个新案例达到 forward-test-green。
