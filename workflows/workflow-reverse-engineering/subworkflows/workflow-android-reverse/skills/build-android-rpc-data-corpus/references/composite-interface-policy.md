# 复合接口策略

## 何时创建复合接口

满足任一条件时创建复合接口：

- UI 页面语义天然由多个 RPC 组成，例如详情、评论、评论的回复；
- 调用者每次都需要按相同顺序调用多个基础 RPC；
- 分页、展开更多或二级列表会让上层调用复杂且容易漏数据；
- 需要把 raw 和 simplified 输出策略固定下来。

不满足这些条件时，只保留基础 RPC 文档，避免把业务流程塞进一个难维护的巨型函数。

## 必填字段

复合接口文档必须包含：

- 业务语义：回答详情、问题详情、经理主页问答、专题问题列表等；
- 根实体 ID：questionId、answerId、publicId、themeId 等；
- 组件 RPC：operationType、入参、响应模型、证据；
- 分页策略：页码、cursor、haveNext、maxPages、终止条件；
- 子列表展开策略：默认预览、展开更多、pagingReplyList、二级评论；
- 输出模式：默认 simplified，显式 `--save-raw/includeRaw` 保存 raw；
- 完整性字段：`complete`、`hitMaxPages`、`partialReasons`、`componentStatus`；
- 失败语义：某个子 RPC 失败时返回 partial 还是整体失败。

## 高风险子列表

复合接口中常见的风险不是根详情 RPC 失败，而是某个子列表或展开分支更容易触发服务端窗口、账号冷却或 partial。例如：

```text
详情主数据
-> 顶层评论 / 子列表分页
-> 评论的评论 / 展开更多 / 二级分页
```

设计时必须把这些分支拆成组件状态：

- 主详情 RPC 成功不等于复合接口完整；
- `ok=true` 不等于 `complete=true`；
- 子列表失败时优先返回 partial，并明确 `partialReasons`；
- `componentStatus` 至少包含每个组件的 `ok`、`complete`、`callCount`；
- 重型展开分支必须提供关闭开关，例如 `--no-expand-nested`；
- 批量默认不应使用最重模式，应先定义轻量、中等、完整三档。

推荐分层：

| 层级 | 行为 | 适用场景 |
|---|---|---|
| L1 轻量 | 只取根详情和主列表，不展开重型子列表 | 健康检查、批量默认入口 |
| L2 中等 | 取少量子列表页，不展开二级列表 | 小窗口 UAT、限制排查 |
| L3 完整 | 拉满分页和展开更多 | 人工确认后的小样本，不作为默认批量 |

## 输出结构建议

```json
{
  "root": {"id": "answerId", "type": "answer"},
  "detail": {},
  "comments": [],
  "nestedReplies": {},
  "pagination": {
    "complete": true,
    "hitMaxPages": false,
    "partialReasons": []
  },
  "componentStatus": [
    {"name": "answerDetail", "ok": true},
    {"name": "commentPages", "ok": true}
  ],
  "sources": []
}
```

## UAT

复合接口的 UAT 不是“某个 RPC 返回 200”，而是：

- 根实体与 UI 选中的对象一致；
- 页面可见主数据在输出中能找到；
- 分页和展开规则达到声明边界；
- raw/simplified 与敏感字段策略符合契约；
- partial 时能解释哪一段缺失以及为什么。
