# 批量运行护栏

## 批量前

1. 写明授权范围、目标实体和请求上限。
2. 先执行 dry-run，只统计计划新增、重复、预计请求次数和预计耗时。
3. 先跑小 UAT，例如 1 个主题、1 个用户/入口实体、2 页或 5 条记录。
4. 默认输出 simplified；完整 raw 只有显式参数才保存。
5. 设计 checkpoint、resume、failure file 和 batch summary。

## 运行中

- 每次请求之间设置随机等待，默认 8-16 秒或更保守；
- 支持 `--limit`、`--offset`、`--max-pages`、`--max-items`；
- 定期落盘进度，不依赖内存状态；
- 跳过已完成实体，失败实体写入独立文件；
- 日志记录当前入口、页码、实体数、重复数、失败数和下一步。

## Frida RPC 长跑采集

当批量采集依赖 App 内 Frida RPC、bridge/RPC 主动调用或目标进程运行态时，单次 RPC Green 不等于批量 Green。长跑前必须额外验证：

0. **固定目标设备**：主机可能同时连接 iPhone、Android、模拟器或远程 Frida device。长跑前必须固定 Android serial，例如 `ALIB_ANDROID_SERIAL`、`ANDROID_SERIAL` 或脚本级 `--device-id`；`adb pidof` 与 `frida attach` 必须指向同一台设备。
1. **执行载体**：普通前台短批量、`nohup` 后台、伪终端、真实 TTY 的稳定性不同。若无交互后台环境导致 Frida/USB/App session 提前退出，优先使用真实 Terminal TTY，必要时为每个实体包一层 `script` 伪终端。
2. **单实体隔离与长会话复用分离**：长跑任务优先按“一个主题/一个用户/一个实体”拆分输出、状态和证据，避免一个实体的异常污染整批。但不要把“单实体隔离”误解为“每条请求都重建 Frida 会话”。若频繁 `attach/load/unload/detach` 会触发 App native crash 或 `script has been destroyed`，更稳的折中是：业务实体、输出文件和 DB 状态仍隔离；Frida session 在一次调度窗口内复用。窗口大小由 checkpoint 粒度、目标吞吐、App 稳定性和服务端窗口共同决定，可以从几十条起步，再用真实 UAT 调整；配额仍由业务 bucket 控制。
3. **可恢复状态**：目录序号、业务主键、offset、attempt、resultPath、错误摘要要落盘。恢复时从最后一个成功实体的下一 offset 继续，不能只依赖内存计数。
4. **失败继续与人工介入**：单实体失败可以记录后继续，但账号冷却、服务端压力、验证码、风控和授权边界变化必须停止整批。
5. **短批量到长跑的升级门**：至少经过 1 个实体、5 个实体、小窗口长跑三类验证，再进入完整候选集。小窗口长跑必须明确记录：窗口大小、是否复用 Frida session、是否出现 App crash、是否出现 `InvalidOperationError` / `script destroyed`、以及下一轮调度间隔如何从服务端窗口预算折算而来。
6. **全局汇总分离**：`batch-summary` 往往只表示当前批次。长跑结束后应基于所有实体目录重建全局 summary/report，避免把某个批次误当作全量结果。
7. **Frida 半健康烟测**：`frida-ps -Uai` 能列进程不等于 RPC 可用。长跑恢复前必须做一次最小 `device.attach(pid)` 烟测；如果 attach 报 `ServerNotRunningError: ... closed`、`TransportError: the connection is closed` 或 `create_script` 失败，应先停止 supervisor、重启手机端 frida-server、单实体复跑 Green 后再继续全量。
8. **运行态 crash sentinel**：如果 App/zygote native crash 会导致后续 RPC 进入假失败，长跑 supervisor 应周期性检查 `logcat -b crash` 或等价来源。发现目标进程或 zygote crash 后，应标记 `environment_failed`，停止业务请求，触发环境修复或人工通报；不得把 crash 期间的业务 item 记成普通请求失败。若条件允许，应额外保存 crash evidence 包：crash buffer、main logcat 尾部、前台 Activity、进程、网络、tombstone 列表、调度状态摘要和 fingerprint。
9. **Session 生命周期自愈**：`script has been destroyed`、`InvalidOperationError`、`TransportError`、`ProcessNotFoundError` 等优先视为执行载体问题。当前 item 回滚为 `pending`，已成功 item 保留 checkpoint；在同一轮中可自动重建 Frida session 并继续。只有连续重建超过阈值时，才升级为环境红灯。
10. **业务窗口与环境红灯分层**：服务端 `1009`、403、TFS、CloudWAF 等属于业务/服务端窗口；Frida server 断开、App crash、设备无网、目标 runtime 不存在属于环境红灯；设备态重置、登录、验证码或目标页面进入需要人工确认属于 human gate。三类状态必须在 DB、log、dashboard 或 batch report 中分开记录。
11. **分接口 bucket**：不同 RPC 的窗口和失败语义可能完全不同。详情、评论、回复、列表页等必须按 bucket 独立记录 success、server-limited、cooling、pending、failed、quota 和 nextRun。不得用一个全局 sleep 解释所有接口。
12. **给人类通报**：长跑系统应把 dashboard、机器日志和人类通知分层。dashboard 负责进度和下一轮；机器日志记录全部事件；人类通知只在环境红灯、修复失败、等待登录/验证码/授权确认、长跑完成或需要人工决策时触发，并应限频。
13. **到期任务队列化调度**：分接口 bucket 到期后，不应默认一次消耗完整 15m/30m 窗口或一个大批次。更稳的默认模型是：到期 bucket 只吐出一个或少量小任务进入队列，worker 按队列顺序执行，完成后立即 checkpoint，再回到调度器重新判断下一项。小任务大小应可配置，默认从 1 条实体/页起步；只有在 UAT 证明运行态、服务端窗口和 dashboard 都稳定后，才逐步增大。这样可以避免某个接口长期独占 worker，也能让不同 bucket 的进度、窗口和失败原因持续可见。
14. **公平性先于并发**：当多个 bucket 都到期时，先用 FIFO 或 round-robin 小任务保证每个接口都能推进；不要一开始就用多 worker 并发掩盖调度问题。并发只能在具备 DB 锁、运行态 session 隔离、窗口预算隔离、crash sentinel 和停止条件之后启用。

推荐的最小长跑产物：

- `progress.jsonl`：每个实体一次事件；
- `checkpoint.json`：最近处理位置；
- `failed.json` 或 `failed-offsets.json`：失败实体和错误摘要；
- `rate-state.json` 或等价状态：每个 bucket 的窗口、冷却、下一轮和最近限制；
- `due-task-state.json` 或等价状态：到期 bucket、小任务大小、当前 worker、队列为空/被阻塞原因；
- `human-notify.log` 或机器日志事件：通知发送、限频和失败记录；
- `outputs/entities/<index>-<id>/...`：每个实体独立证据目录；
- `harvest-summary.json` / `harvest-report.md`：全局重建结果。

## 停止条件

出现以下情况立即停止并写入日志：

- 账号、设备或 IP 出现限制、冷却、验证码、403、418、TFS、CloudWAF；
- 服务端或同事反馈压力过大；
- 响应开始大面积为空或结构异常；
- UI 需要人工验证或授权边界变化；
- 预计请求量超过契约；
- 出现高风险敏感字段落盘。

不得通过提高并发、换账号、代理池、绕过验证码或隐藏流量来继续。

## 批量后

生成报告：

- 总请求数、成功数、失败数、跳过数；
- 新增实体、重复实体、冲突实体；
- source/evidence 覆盖；
- 疑似服务端窗口；
- 覆盖率声明；
- 下一轮建议和是否需要人类确认。
