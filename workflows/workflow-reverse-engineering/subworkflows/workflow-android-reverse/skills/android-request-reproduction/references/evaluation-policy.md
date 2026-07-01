# 评测规则

仅使用课堂 fixture、自有应用或明确授权目标。

## 复现等级

- **A级：精确复现**。固定输入能够得到相同的中间值和最终值。
- **B级：等价复现**。动态值不同，但数据结构、处理顺序、算法和当前样本中的对应关系一致。
- **C级：阶段复现**。环境因素阻止最终请求，但已经恢复必要的阶段性证据，并能重复说明阻塞点。

## 两个验证关口

在 G1/G2 之前还必须维护：

- `smoke: passed/failed/blocked/not-run/not-reproduced/passed-with-scope`
- `unit: <test-id>: passed/failed/blocked/not-run/not-required/not-reproduced/passed-with-scope`

目标包含最终业务现象或研究交付时，还必须维护：

- `uat: passed/failed/blocked/not-run/not-required/blocked-by-boundary/passed-with-scope`

完整状态语义见 `acceptance-statuses.md`。

### G1 离线等价

回答：

> 在同一固定输入下，外部实现是否构造出与 App 相同的参数、中间值、请求头或最终字节？

至少记录：

- 使用的 fixture；
- 参数和动态字段来源；
- sign/编码/加密中间值；
- 最终请求体或序列化字节；
- 首个差异层级。

### G2 受控端到端

仅当目标明确包含“重发”“服务端接受”或“完整请求交付”时执行，回答：

> 由外部实现组装的完整请求是否被目标服务端接受？

要求：

1. 仅限课堂靶场、自有应用或明确授权目标；
2. 默认最多发送一次，不自动重试；
3. 请求方法、URL、必要 headers、body 和发送时间写入 manifest；
4. 保存 HTTP 状态、响应正文和可解析的业务码；
5. 网络错误和非成功响应也必须落盘；
6. 业务页面变化只作额外证据，不用来替代 HTTP/业务响应。

状态分别记录：

- `g1_offline_equivalence: passed/failed/not-run/partial-validated`
- `g2_controlled_e2e: passed/failed/not-required/not-run/blocked/partial-validated`

G1 通过但 G2 未运行时，只能报告“算法/请求构造已完成”，不得报告“完整请求已被服务端接受”。

G2 通过但目标要求 UAT 且 UAT 未通过时，只能报告“服务端已接受请求”，不得报告最终业务目标完成。

对于 native 安全 SDK 或 Unidbg 补环境，`partial-validated` 是常见合法状态：

- 离线 wrapper、JNI 入口和补环境链路已经跑完；
- 输出形态、长度、结构或固定 fixture 对照通过；
- 但仍未和真机设备态、账号态、时间/随机数、`/proc`、TEE 或真实 HTTP 请求对齐。

这种状态应保留 Green 证据，同时把后续 device-assisted 对齐、G2 或 UAT 明确列为新 TASK。

## 测试驱动判定

每项评测必须预先写明：

- Red：失败测试、未知叶子或未运行关口；
- Green：可审查的通过证据；
- fixture 或授权目标；
- 首个差异层级；
- 对应 Mermaid 节点和 TASK。

没有预先 Green 条件的实验只能作为探索性观察，不能直接升级完成状态。探索发现应先写回台账，再建立可验证测试。

## 能力标签

复现等级描述实验质量，能力标签描述实现性质，两者必须同时记录：

- `substitute-valid`：替代构造仅在声明范围内可用；
- `reproducible`：真实生成规则可从输入重建；
- `validated`：真实重建结果与 App 或 fixture 交叉验证。

替代构造即使达到 A 级精确的格式或行为验证，也不能自动升级为 `reproducible`。

## 必填记录

```yaml
课程_day:
目标:
fixture或目标:
环境:
使用的skills: []
使用的工具或mcp: []
预期证据: []
实际证据: []
证据角色:
  primary: []
  confirmatory: []
  exploratory: []
复现等级:
能力标签:
g1_offline_equivalence:
g2_controlled_e2e:
smoke:
unit_tests: {}
uat:
mermaid节点:
green条件:
真实性要求:
验证范围: []
未验证绑定: []
差异: []
人工判断: []
改进项: []
```

不能仅凭一段合理解释就判定评测通过。
