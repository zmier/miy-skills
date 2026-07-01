# RPC 语料库契约

## 目标

- 业务问题：
- 主实体：
- 授权范围：
- 非目标边界：

## 接口地图

| 页面/动作 | operationType | 入参 | 主实体 | 分页 | 证据 |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 覆盖率声明

- 当前状态：`single-page | paged-window | multi-entry-corpus | full-claimed`
- 支撑证据：
- 尚未排除的窗口：
- 不得宣称的内容：

## 基础 RPC

| 名称 | operationType | 输入 | 输出 | raw 策略 | 状态 |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 复合接口

| 名称 | 根实体 | 组件 RPC | 分页/展开规则 | 完整性字段 | UAT |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 语料 Schema

```json
{
  "entityId": "",
  "entityType": "",
  "payload": {},
  "sources": []
}
```

## 批量护栏

- dry-run：
- limit/offset：
- checkpoint：
- 长跑载体：`foreground | nohup | pty | real-tty | not-required`
- 单实体隔离：
- session 失效处理：
- 随机等待：
- failure file：
- raw 保存：
- 停止条件：
- 全局汇总：

## 合并策略

- 主键：
- 去重：
- 冲突：
- source/evidence：
- dry-run diff：

## UAT

- GIVEN：
- WHEN：
- THEN：
- 证据：

## 日志

- TASK：
- `logs/LOG.md`：
- batch summary：
