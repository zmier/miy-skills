# TASK04 说明

## 任务

对 J-260110 手稿执行未读取欣媛意见的 blind `full-tree` 两步抽树：

- 2A：只还原作者证据树。
- 2B：只显影后续需要验箭头的可疑证据组合，不写最终审稿意见。

## 输入边界

仅读取白名单输入、Skill 文件及其直接 references/assets。未读取欣媛审稿意见、TASK01 输出、TASK02 已有 blind/full-v2/xinyuan-comparison/arrow-audit/selected-issues 输出。

## 输出

本任务输出位于：

```text
tasks/TASK04-subagent-full-tree-blind/
```

核心文件：

- `outputs/paper-argument-tree.md`
- `outputs/evidence-ledger.md`
- `outputs/evidence-expanded-mermaid.md`
- `outputs/review-sensitivity-map.md`
- `outputs/sensitivity-expanded-mermaid.md`
- `outputs/obsidian-link-map.md`
- `outputs/extraction-qc.md`
- `logs/log.md`

