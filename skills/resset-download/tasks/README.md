# RESSET Download Tasks

`tasks/` 用于承接 `$resset-download` 的技能工程、forward test、接口复现和 UAT 证据。

| Task | Goal | Status | Human Gate |
|---|---|---|---|
| `TASK01-interface-first-replay` | 评估并验证 RESSET 从 UI-first 升级为 hybrid interface-first 的可行性 | active; partial Green | direct POST 与 zip retrieval 涉及验证码和真实下载任务，需要授权或人工接力 |

## 任务边界

- 项目业务数据 inventory 不放在这里，仍由各项目自己的 `tasks/` 管理。
- 可复用到 `$resset-download` 的方法、请求构造 ledger、WebVPN 状态、验证码前置检查和 UAT 结果放在这里。
- 跨 skill 的问题用目标 skill 自己的 `issues/` 记录，并在本任务中只保留链接。
