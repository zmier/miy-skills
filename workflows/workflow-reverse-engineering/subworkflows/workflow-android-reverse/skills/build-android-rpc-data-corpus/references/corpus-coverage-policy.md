# 语料覆盖率与证据策略

## 覆盖率状态

| 状态 | 含义 | 可说的话 | 不可说的话 |
|---|---|---|---|
| `single-page` | 只验证一页或一次调用 | 该调用返回结构已理解 | 该业务入口已完整 |
| `paged-window` | 某入口分页跑到当前可访问终点 | 该入口当前窗口结束 | 业务全量结束 |
| `multi-entry-corpus` | 多入口合并去重形成语料 | 已获得一批可追溯实体 | 已覆盖全部实体 |
| `full-claimed` | 有额外证据支持全量 | 全量已取得 | 只凭 `hasNext=false` 宣称全量 |

`full-claimed` 必须至少满足一个条件：

- 服务端返回可信 total，并且请求数量与 total 对齐；
- 官方业务文档说明该接口就是全量出口；
- 多个独立入口交叉验证没有新增；
- 人工 UI 或业务后台可验证总数。

## Source/Evidence 模型

每条主实体记录至少保留：

```json
{
  "entityId": "questionId-or-answerId",
  "entityType": "question",
  "sources": [
    {
      "sourceType": "topic-list | manager-feed | detail | search | manual-ui",
      "operationType": "RPC_OPERATION",
      "input": {"pageNo": 1, "topicId": "xxx"},
      "evidenceFile": "outputs/raw/topic_xxx_page_001.json",
      "firstSeenAt": "2026-06-16T12:00:00+08:00"
    }
  ]
}
```

简化输出可以隐藏敏感字段，但 source/evidence 不能丢。

## 疑似服务端窗口

遇到以下现象时，把覆盖率降为 `paged-window` 或 `multi-entry-corpus`，并记录窗口假设：

- 每个入口都停在 99/100 页或约 1000 条；
- 第 101 页空，`haveNext=false`，但其他入口仍能发现更早实体；
- 同一账号短时间内详情或列表开始返回空、拒绝或限流；
- 游标字段存在但不生效；
- UI 能看到更多入口，但当前 RPC 只返回固定窗口。

窗口假设要写成“尚未排除的解释”，不能写成服务端事实。

## 合并规则

1. 先按主键去重，再合并 sources。
2. 字段冲突时保留所有冲突值和 evidence，不静默覆盖。
3. 合并前输出 dry-run diff：新增、重复、冲突、缺 source、缺 evidence。
4. 主语料只接收通过 schema 校验和 source/evidence 校验的记录。
