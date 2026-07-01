---
name: model-android-rpc-response
description: 将经过授权的 Android bridge/RPC/统一网关响应建模为可交付的数据 schema、字段说明、分页语义、敏感字段边界和默认简化 JSON 输出。用于已确认 operationType、bridge method、HTTP 响应或 App 内 RPC 返回值后，需要从原始 JSON 中提取主业务实体、设计 Frida RPC/Python client 输出、制定 raw response 保存策略、或判断响应是否满足 UAT 的场景。
---

# Android RPC 响应建模

## 目标

把“已经能看到响应”推进为“知道响应里哪些字段有用、哪些敏感、工具默认应该输出什么”。

本 Skill 不负责找接口、破签名、发送请求或绕过访问控制。它只处理已经在授权范围内取得的响应样本。

## 输入

- TASK 工作区；
- operationType、bridge method、URL 或 App 内方法名；
- 一份或多份响应样本，优先使用脱敏样本；
- 当前 UAT：用户到底需要验证 UI、提取列表、分页、详情，还是只证明调用成功；
- 交付路线：R1 Hook、R2 Frida RPC、R3 外部 Python 或 R4 组合。

没有响应样本时，返回总编排继续做 `identify-android-business-network-channel` 或 `android-request-reproduction`，不要凭字段名猜 schema。

## 工作流

1. 确认样本来源和授权边界：bridge callback、RPC 返回对象、HTTP 明文响应、App 内主动调用，或 fixture。
2. 从 `assets/response-model-template.md` 创建 response model 文档。
3. 记录顶层状态字段：`success`、`code`、`message`、`traceId`、`result` 等。
4. 识别主业务实体：列表项、详情对象、答案、评论、订单、商品、配置等。
5. 识别分页和游标字段：`pageNo`、`pageSize`、`hasNext`、`lastFlag`、`cursor`、`nextToken` 等。
6. 识别业务主键和关联键：问题 id、回答 id、feed id、topic id、用户 id、tenant id 等。
7. 展开一层到两层关键嵌套对象；超过 UAT 需要的深层字段只记录路径和样例类型。
8. 标记敏感字段：用户标识、头像、主页、手机号、Cookie、Token、设备标识、精确定位、原始授权头、完整风控字段。
9. 设计默认简化 JSON：只保留 UAT 和工具使用需要的字段。
10. 设计 raw response 策略：默认不保存；只有显式 `includeRaw/saveRaw/--save-raw` 才落盘完整响应。
11. 对列表或批量采集类接口，声明覆盖率语义：`single-page`、`paged-window`、`multi-entry-corpus` 或 `full-claimed`。没有额外证据时不得把 `hasNext=false` 直接写成真实全量。
12. 记录疑似服务端窗口：例如固定 100 页、约 1000 条、账号限流、时间窗口、结果截断、空页终止或不同入口互补。
13. 为批量采集设计操作护栏：随机等待、断点续跑、失败记录、dry-run 增量报告、默认脱敏/简化输出、服务端压力停止条件。
14. 如果响应里有字符串化 JSON，例如 `referenceMap`、`relatedEntitiesJson`，单独记录“二次解析字段”。
15. 写回请求构造台账、测试矩阵和 ReAct 日志，状态可标记为 `response-model-confirmed`。

## 输出

至少产出：

- response model 文档；
- 顶层状态字段表；
- 主实体字段表；
- 分页字段表；
- 嵌套对象和二次解析字段；
- 敏感字段与脱敏策略；
- 默认简化 JSON schema；
- raw response 保存策略；
- 覆盖率声明和服务端窗口观察；
- 批量采集护栏和停止条件；
- UAT 是否可由该响应直接判断。

## 完成标准

- A：有至少两份响应样本或一次主动调用结果，主实体、分页、敏感字段和简化 schema 均已验证。
- B：有一份可靠响应样本，足以设计工具输出，但分页或异常响应仍需后续样本补齐。
- C：只确认响应存在和顶层成功状态，主业务实体结构尚不完整。

完成后不得声称请求已可重放；响应建模只证明“返回数据可理解、可交付”。

列表接口完成后也不得默认声称“全量已取得”。若只观察到某入口分页结束，应写成“该入口当前可访问窗口已结束”。只有跨入口、服务端总数字段、业务文档或独立验证能支撑时，才允许声明 `full-claimed`。

## 参考资料

- 创建 response model 文档时使用 `assets/response-model-template.md`。
