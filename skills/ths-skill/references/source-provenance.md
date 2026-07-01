# THS Skill Source Provenance

## 来源

本 Skill 来自授权项目：

```text
Writer/03 Projects/冒险者工会/PROJECT-MacApp同花顺K线涨停紫色K
```

核心 TASK：

```text
tasks/TASK09-股票K线标注持久化与自动生成
```

关键证据：

```text
before/after diff 定位 DrawLine_New XML；
手动标注唯一文本 MIY_TEST_ANNOTATION_001 命中 XML；
脚本写入 MIY_SCRIPT_ANNOTATION_001 后，用户确认重启 App 出现；
301217 日 K 样本用于采样矩形、水平线、箭头、文字工具、标注气泡。
```

## 迁移状态

| 能力 | 状态 |
|---|---|
| DrawLine 路径 schema | migrated |
| GB2312 XML 读写 | migrated |
| text 写入 | native-load-green |
| note/rect/hline/up-arrow/down-arrow | structure-dry-run-green |
| list 所有 KeyPoint | migrated |
| remove-text dry-run/write + backup | migrated |
| marketCode/periodCode 完整映射 | partial |

## 边界

保留在项目 TASK 中：

```text
具体靶场操作日志；
特定账号目录的完整 diff；
App UI 截图与用户 UAT 原话；
任何可能包含账号态或本机敏感路径的 raw dump。
```

提升到本 Skill：

```text
稳定路径 schema；
LineType / KeyPoint 语义；
脚本 dry-run / backup / UAT 协议；
market/period 的已确认和候选映射。
```
