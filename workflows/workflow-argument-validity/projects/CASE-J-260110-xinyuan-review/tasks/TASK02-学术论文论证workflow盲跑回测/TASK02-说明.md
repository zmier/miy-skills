# TASK02 学术论文论证 Workflow 盲跑回测

## 目标

测试 `workflow-academic-argument-validity` 在 paper 线上的主链条：

```text
读稿抓论证
-> 画作者论证树
-> 全量验箭头
-> 选审稿问题
-> 与欣媛审稿意见对照
```

## 边界

本轮先只读取：

```text
../../inputs/manuscript.md
```

不读取：

```text
../../inputs/xinyuan-review.txt
../../inputs/xinyuan-review.docx
```

直到 blind-run 产物完成后，再解冻欣媛意见做对照。

## 盲测等级

```text
review-frozen / manuscript-only / annotation-contaminated
```

说明：

- 本轮输入不读欣媛审稿意见；
- 但 `manuscript.md` 内含既有批注、标记和疑问脚注，因此不是完全纯净原稿；
- 本 case 历史上已经 prior-exposed，不能声称模型完全不知道欣媛意见；
- 本 TASK 只测试 workflow 的分层产物是否合理，不声称全新 blind discovery。

## 产物

| 文件 | 阶段 |
|---|---|
| `outputs/paper-argument-tree.blind.md` | 抽作者树 |
| `outputs/academic-arrow-audit-table.blind.md` | 全量验箭头 |
| `outputs/academic-selected-issues.blind.md` | 选问题 |
| `outputs/xinyuan-comparison.md` | 解冻后与欣媛意见对照 |
| `logs/log.md` | 过程记录 |
