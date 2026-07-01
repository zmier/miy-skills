# 请求构造依赖台账

## 定位

每个目标 URL 维护一份 `request-construction-ledger.md`，回答：

> 为了达到预先声明的 UAT、G2 和 G1，在选定交付路线和输入边界下，哪些值已经可取得，哪些仍需解释或生成，下一项最小实验是什么？

从 `assets/request-construction-ledger-template.md` 复制初始文件。台账必须包含：

1. 终点与测试状态；
2. 交付路线矩阵；
3. Obsidian Mermaid 核心控制面；
4. Smoke、Unit、G1、G2、UAT 测试矩阵；
5. 节点明细表；
6. 按路线划分的未解决叶子与完成门槛；
7. 唯一 `NEXT` 和 ReAct 当前循环。

## 节点字段

| 字段 | 含义 |
|---|---|
| 节点 ID | 稳定标识，如 `BODY.SIGN.DID` |
| 父节点 | 请求结构中的真实父层 |
| 名称与位置 | 请求头、请求体、签名输入或算法配置 |
| 当前形态 | 抓包、解密或 Hook 中看到的表示 |
| 取值能力 | `unknown`、`observed`、`substitute-candidate`、`substitute-valid`、`hook-available`、`rpc-available`、`located`、`understood`、`reproducible`、`validated` |
| 路线必要性 | R1/R2/R3/R4 各自的 `required`、`conditional`、`not-required`、`unknown` |
| 真实性要求 | `functional-equivalent` 或 `app-authentic` |
| 绑定风险 | 与账号、Cookie、设备注册、其他字段和历史状态的已知或未知关系 |
| 验证范围 | 格式、结构、低频行为、稳定性和绑定验证覆盖到哪一级 |
| 生成逻辑 | 当前已证实的构造方法 |
| 直接依赖 | 生成该节点所需的其他节点 |
| 原始证据 | Reqable、JADX、Frida、IDA、代码、测试或课程锚点 |
| 下一动作 | 只针对当前主路线的最小操作 |

`observed` 只表示一次取值。`substitute-valid` 表示替代值只在声明范围内成立。Hook/RPC 必须经过重复触发或等价稳定性验证，才能分别标记 `hook-available` 或 `rpc-available`。`reproducible` 表示 App 的真实生成规则可从声明输入重新生成。

## 更新规则

1. 先登记 UAT/G2/G1 和路线，再登记请求结构。
2. 运行时 Hook 取得字段时，在 Mermaid 中增加“运行时证据”侧枝，并更新取值能力；不要直接删除纯外部路线的上游 TASK。
3. 解开编码、序列化、压缩或加密层后，把新字段挂到真实解析结果下面。
4. 字段由其他接口响应产生时，把该接口作为前置父节点，记录请求依赖、响应字段、时效、持久化和后续绑定；多个接口使用 DAG，不压成一条无条件线性链。
5. 每次路线变化，重新计算必要叶子，但保留所有历史能力与证据。
5. 总编排只选择“当前主路线 required/触发中的 conditional 且未达到路线门槛”的叶子，并将唯一 `NEXT` 指向对应 TASK 或测试。
6. 最终结论必须写成“R1 已完成”“R3 进行中”等路线化表述，不得只写“请求已破解”。
7. 替代构造与真实生成链可以并列保留；替代值成功不能覆盖真实生成 TASK。
8. 子 Skill 返回后，先更新 Mermaid、测试矩阵和节点表，再更新状态与日志。
10. G2 前在台账中保存原始成功请求预检；预检通过但网络失败时，新增 `RUNTIME_OR_TRANSPORT_CONTEXT` 节点，不回滚已通过的算法节点。
11. 图、表和证据不一致时采用最低状态；没有证据链接的 `passed` 按未通过处理。

## 完成判断

- R1：必要值可稳定 Hook，组合请求通过约定验证。
- R2：必要方法可稳定 RPC 调用，输出通过约定验证。
- R3：全部必要叶子至少 `reproducible`，最终组合达到 `validated`。
- R4：每个环节达到预先声明的能力门槛，组合边界有验证证据。

算法达到 A 级、一次 Hook fixture 完全一致，都不自动等于任意路线的整条 URL 已完成。

完成声明还受测试关口约束：

- G1 未通过，不得声明离线构造等价；
- 目标要求真实重发而 G2 未通过，不得声明服务端接受；
- 目标要求业务结果而 UAT 未通过，不得声明最终目标完成。
