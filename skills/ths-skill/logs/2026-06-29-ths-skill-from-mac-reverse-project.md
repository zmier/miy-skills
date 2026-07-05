# 2026-06-29 ths-skill From Mac Reverse Project

## 背景

用户在授权 Mac App 靶场中完成同花顺 K 线颜色和标注持久化实践后，提出将同花顺能力抽象为复合 Skill：

```text
OK，做个复合SKILL如何：ths-skill，这个当成他的子skill。
```

## 判断

按 `workflow-tao`，这不是大型 workflow，而是中型复合 Skill：

```text
父入口 ths-skill：同花顺任务边界、路由、证据协议、Green 标准；
子 skill ths-drawline-annotation：DrawLine XML 标注/画线的读取、写入、清理、UAT；
references：稳定 schema 和 provenance；
logs：保留抽象来源和迁移边界。
```

## 抽象边界

个案留在 PROJECT：

```text
具体股票 UAT；
完整 TASK ReAct 日志；
本机账号目录 raw diff；
靶场操作细节。
```

迁移到 Skill：

```text
DrawLine_New 路径；
GB2312 XML；
LineType 和 KeyPoint 画法；
write/list/remove 脚本；
dry-run / backup / native-load UAT 协议。
```

## 当前状态

```text
structural-green=true
textNativeLoadGreen=true
multiShapeDryRunGreen=true
cleanupToolGreen=true
marketPeriodMappingPartial=true
```

后续回归方向：

```text
对 note/rect/hline/up-arrow/down-arrow 执行 --write + App native load UAT；
补交易日序列 offset 自动计算；
补 periodCode 完整映射；
需要时新增更多同花顺子 skill。
```
