# Timeline-Ex Node Contract

## 1. ID 与文件名

推荐格式：

```text
EVT-YYYYMMDD-SHORT-NAME
OBL-YYYYMM-SHORT-NAME
GATE-YYYYMM-SHORT-NAME
OUT-YYYYMM-SHORT-NAME
```

文件名使用相同前缀，允许在 ID 后添加中文标题：

```text
nodes/GATE-202701-第1轮预答辩.md
```

ID 一经被其他节点、日志、TASK 或提醒引用，不因标题润色而改变。

## 2. 结构化节点字段

最小 `timeline-data.js`：

```javascript
window.TIMELINE_EX_DATA = {
  meta: {
    title: "Project External Timeline",
    updatedAt: "2026-07-17",
    visualizationWindowNote: "近似日期仅用于布局。"
  },
  groups: [
    { id: "event", order: 1, label: "外部事件", code: "EVT" },
    { id: "obligation", order: 2, label: "外部义务", code: "OBL" },
    { id: "gate", order: 3, label: "资格门槛", code: "GATE" },
    { id: "outcome", order: 4, label: "外部结果", code: "OUT" }
  ],
  nodes: [],
  links: []
};
```

节点推荐字段：

| 字段 | 必需 | 含义 |
|---|---|---|
| `id` | 是 | 稳定节点 ID |
| `type` | 是 | `event / obligation / gate / outcome` |
| `group` | 是 | HTML 时间轴泳道 |
| `title` | 是 | 完整标题 |
| `shortTitle` | 是 | 时间轴短标题 |
| `start` | 有时间时 | ISO 日期；近似值只用于布局 |
| `end` | 时间窗时 | ISO 日期；按可视化库的区间语义处理 |
| `displayTime` | 是 | 权威来源中的原始时间表述 |
| `certainty` | 是 | 时间确定性 |
| `status` | 是 | 当前状态 |
| `statusLabel` | 是 | 人类可读状态 |
| `authority` | 是 | 决定或发布该节点的外部权威方 |
| `source` / `sourceEvents` | 是 | 来源事件 ID、文件或权威链接 |
| `summary` | 是 | 一句话说明节点意义 |
| `prerequisites` | Gate/OBL | 前置条件 |
| `affectedTasks` | 推荐 | 受影响的内部 TASK |
| `passUnlocks` | Gate | 通过后状态 |
| `failureEffect` | Gate/OBL | 失败、错过或驳回后果 |
| `nextAction` | 推荐 | 当前内部准备动作，不得冒充外部决定 |
| `document` | 是 | 节点 Markdown 档案路径 |

## 3. 类型状态

### EVT

```text
observed    = 已发生并已记录；
disputed    = 来源存在冲突，等待确认；
superseded  = 原通知仍保留，但口径已被新事件替代。
```

EVT 默认是追加式事实，不使用 `planned`。

### OBL

```text
planned / upcoming / due / submitted / accepted / rejected / missed / waived
```

### GATE

```text
planned / upcoming / ready / applied / under-review / passed / failed / blocked / superseded
```

### OUT

```text
conditional / received / confirmed / rejected / deferred / cancelled
```

状态词可以按领域扩展，但不要让颜色成为唯一状态信号。

## 4. 时间确定性

```text
exact            = 官方精确日期或时间；
confirmed-window = 官方确认的窗口，但没有精确日；
tentative        = 明确写有暂定、拟定或预计；
window           = 只给月份、季度或宽泛区间；
tbd              = 尚无时间；
conditional      = 仅在另一状态触发后出现。
```

示例：

```javascript
{
  start: "2027-01-01",
  end: "2027-01-11",
  displayTime: "暂定 2027 年 1 月初",
  certainty: "tentative"
}
```

`start/end` 是展示区间，`displayTime` 才是原始语义。任何日历或外部沟通都必须使用原始语义，除非后续 EVT 给出精确日期。

## 5. 箭线字段

```javascript
{
  id: "LINK-001",          // 可选；复杂项目推荐
  from: "EVT-001",
  to: "GATE-001",
  relation: "creates",
  label: "创建未来门槛",
  source: "EVT-001"        // 可选：为何存在这条关系
}
```

每条箭线必须满足：

- `from` 和 `to` 指向已存在 ID；
- `relation` 使用稳定枚举；
- `label` 用读者能理解的语言；
- 关键资格或失败关系可追溯到来源；
- 不用箭线表达含糊的“有关联”。

## 6. 节点 Markdown 档案

最小结构：

```markdown
# GATE-YYYYMM：节点标题

## 节点信息

| 字段 | 内容 |
|---|---|
| ID | `GATE-*` |
| 类型 | 资格门槛 `GATE` |
| 状态 | `planned` |
| 官方时间表述 | 暂定…… |
| 确定性 | tentative |
| 权威方 | …… |
| 来源事件 | [EVT-*](...) |
| 影响 TASK | TASKxx |

## 前置条件

## 状态转换

## 当前下一步

## 待确认
```

EVT 档案应优先保存原文和派生影响；OBL 档案应说明提交对象、材料、方式和完成证据；OUT 档案应说明触发条件和结果边界。

## 7. 数据完整性检查

交付前验证：

```text
node IDs unique
all link endpoints exist
all document paths exist
all nodes have type/status/certainty/source
all approximate windows retain displayTime
all gates name prerequisites and pass/fail effects when source provides them
```
