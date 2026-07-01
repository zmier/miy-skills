# TASK 写回契约

调用本 Skill 时必须提供需求 TASK 工作区。默认写入：

```text
tasks/TASK02-采集窗口/outputs/capture-index.md
tasks/TASK03-候选接口/outputs/candidate-matrix.md
tasks/TASK04-对照验证/validation-operation-manual.md
tasks/TASK04-对照验证/outputs/experiment-log.md
tasks/TASK05-目标接口/outputs/target-interface.md
tasks/TASK06-最小重放与路由/outputs/handoff.md
evidence/sanitized/
00-工作流状态.yaml
logs/LOG.md
```

## 更新顺序

1. 检查采集索引是否具有明确窗口。
2. 写候选矩阵，不覆盖尚未解决的反证。
3. 需要人类参与时，先生成只包含下一轮最小实验的验证操作手册。
4. 收到人类反馈后原样写入实验日志，再追加分析结论。
5. 达到证据要求后填写目标接口卡。
6. 将脱敏 fixture 链接到接口卡。
7. 更新工作流状态中的观察、证据、当前阶段、阻塞和下一步。
8. 在过程日志记录工具、时间、失败尝试和人工判断。

## 交接要求

若目标接口已确认：

- 在 `handoff.md` 列出所有阻塞重放的动态或未知字段；
- 为每个字段记录当前证据和下一 Skill。

若尚未确认：

- 列出剩余候选；
- 写明缺少的窗口、业务观察量或实验权限；
- 将复现等级标为 C，不伪造目标接口。

原始敏感流量只保留在 `evidence/raw/`，Markdown 和 `evidence/sanitized/` 仅保存脱敏结构。
