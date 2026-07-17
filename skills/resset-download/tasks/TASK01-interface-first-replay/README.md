# TASK01 Interface-First Replay

本任务承接 `$resset-download` 的接口化探索与技能反哺。

## 当前状态

截至 2026-07-08：

- `dataSearch.jsp` 表页元数据 GET：partial Green。
- `downloadTaskUser.action` 下载中心列表 GET：partial Green。
- Chaojiying preflight：Green；默认使用 workflow `.venv` 运行 `preflight --no-network --json`。
- `dataSearch.action` direct POST 创建下载任务：未 Green；两个 RESSET 主 tab 的新表页导航均跳到四川大学统一身份认证，需先恢复 WebVPN/RESSET 登录态。
- `/verifyDownload?token=<tid>` browserless zip 保存：未 Green，当前仍需浏览器 iframe/navigation 或 download event。

## 当前入口

- 任务说明：`TASK01-说明.md`
- 验收边界：`acceptance-contract.md`
- 可行性文档：`outputs/resset_direct_interface_replay_feasibility.md`
- 过程日志：`logs/log.md`

## 下一步

1. 恢复 RESSET/WebVPN 登录态，避免新表页导航跳到四川大学统一身份认证。
2. 在 Chaojiying preflight Green 后，做 `FDSHRCHG` 单基金 direct POST forward test。
3. 对已完成任务测试 `/verifyDownload?token=<tid>` 是否能返回 zip magic `PK`。
4. 只把 Green 的规则写回 `SKILL.md`，未 Green 的留在本任务。
