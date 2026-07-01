# App 内 RPC 封装

用于目标请求强依赖 App 运行态、登录态、设备态、容器上下文或统一网关签名，而当前交付允许使用 R2 Frida RPC 的场景。

## 适用信号

- 已确认 bridge/RPC operation、service name 或 Java 方法；
- 响应模型已确认，能判断调用是否返回目标业务实体；
- 外部 Python replay 需要 `Sign`、`miniwua`、`Did`、登录态、TEE 或风控上下文；
- 目标是授权研究、课堂靶场或自有 App 的低频受控调用。

## 最小封装原则

只封装一个业务 operation 或一个已定位方法：

```text
输入 options
→ 重建目标框架需要的 Java 参数
→ 调用 App 内方法/RPC
→ 解析返回 JSON
→ 输出简化模型
```

不要把“打开页面、点击、等待、解析 UI”整体塞进 RPC。页面流程可以作为证据来源，交付工具应尽量落在已确认的业务调用点上。

封装前要区分“页面入口参数”和“业务接口参数”：

- 页面 URL、scheme、deep link 负责把 App 带到某个页面；
- 业务 RPC 可能使用列表 item 中的另一个实体 id；
- 例如详情页 URL 中的 `questionId` 可能只是页面入口，而主详情接口实际使用 `answerId/commentId`。

因此，Frida RPC agent 的参数应来自已确认的 RPC `requestData`，而不是直接照搬页面 URL query。

## SimpleRpcService 模式

Alipay/mPaaS 一类场景常见路线：

```text
LauncherApplicationAgent
→ getMicroApplicationContext()
→ findServiceByInterface(RpcService)
→ getRpcProxy(SimpleRpcService)
→ executeRPC(operationType, requestBody, extParams)
```

注意：

- `findServiceByInterface(SimpleRpcService)` 可能返回空；先取 `RpcService` 再 `getRpcProxy` 往往更稳。
- App 内 RPC 可能禁止主线程调用；用 worker thread 执行。
- `extParams` 明确为空时也要传目标框架期望的 Java Map 类型。
- body 通常保持 App 观察到的 JSON array/string 形态，不要随意改序列化。

## 输出策略

默认输出简化 JSON：

- 顶层：`success`、`traceId`、`hasNext`、`count`；
- 主实体：业务 id、标题/正文、时间、分页字段；
- 嵌套实体：只保留学习或研究需要的字段；
- 用户、头像、主页、Cookie、Token、授权头默认脱敏或不落盘。

只有显式参数启用时才保存 raw response，例如：

```text
includeRaw=true
saveRaw=true
--save-raw
```

raw 文件路径必须写入结果摘要，并标明含敏感字段的本地保存边界。

## Python Client 约定

- 默认使用 workflow `.venv` 中的 `python` 与 `frida`。
- 先尝试按包名 attach；失败且 `adb pidof <package>` 有结果时，fallback 到 PID attach。
- 输出 summary JSON，包含 `ok`、`count`、第一条业务实体摘要、raw 文件路径。
- 进程退出、session detach 或 RPC 异常不得返回陈旧成功。

## 状态边界

成功后标记：

- `app-internal-rpc-call-passed`：一次或多次 App 内调用成功；
- `frida-rpc-tool-passed`：agent、client、runner 和输出策略稳定；
- `r3-precheck-complete`：另行完成纯外部重放可行性预检。

不得把 R2 成功写成 `reproducible`。如果用户要求无设备 CLI、云端部署或脱离目标 App，必须回到总编排评估 R3/R4。
