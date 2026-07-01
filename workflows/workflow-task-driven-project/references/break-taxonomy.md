# Break Taxonomy

## 项目断点分类

| 断点 | 表现 | 处理 |
|---|---|---|
| scope-blur | 用户目标/交付物变动，旧 TASK 装不下 | 重写目标，必要时开新顶层 TASK |
| evidence-hidden | 结论只在终端或 raw 文件里，没有 Markdown 摘要 | 提升为 `outputs/*.md` 证据摘要 |
| task-sprawl | 顶层 TASK 太多，主线不清 | 使用子 TASK，补 README 状态表 |
| orphan-output | 有输出但不知道来自哪一步 | 写 evidence ledger，回链 TASK/log |
| long-run-fragile | 长跑中断、状态丢失、无法恢复 | 增加 checkpoint/resume/failure file |
| partial-green | 某组件成功但整体不完整 | 显式 complete/partialReasons/componentStatus |
| review-missing | 项目完成阶段但没有复盘 | 在 `final_outputs/` 写阶段复盘 |
| workflow-feedback-lost | 项目学到的通用经验未反哺 | 写 feedback section 并更新目标 workflow/skill |
| sensitive-leak-risk | raw/敏感字段进入普通 Markdown | 改为脱敏摘要，raw 留受控 outputs |
| dashboard-drift | README、dashboard、Makefile、TASK 状态不一致 | 以 README/TASK 总说明为准同步状态 |

## 处理原则

项目断点不是失败，而是结构需要升级的信号。优先保留历史证据和任务编号，不为了整齐而重写历史。
