# 产物模板

## 目录

1. 首次学习指南
2. 增量知识地图
3. 永久知识卡片
4. 案例或材料 README
5. Frontmatter 字段

保持用户知识库的既有格式。以下模板只提供默认结构。

## 1. 首次学习指南

```markdown
---
type: learning-guide
source_course: 来源名称
source_case: 案例或书名
source_units:
  - 学习单元
status: learning
---

# 案例或书名：学习单元 首次学习指南

## 使用方法

说明本单元的能力主线、第一轮和第二轮范围。

## 开始前应具备

- [[前置知识]]

## 今天要形成的组块

组块 A → 组块 B → 组块 C

## 组块一：完整问题

### 要解决的问题

### 学习步骤

1. [[完整来源路径#精确标题]]
2. [[永久知识卡片]]

### 观察材料

- [[示例、图表、论文证据或代码]]

### 小练习

### 通过标准

- [ ] 能解释……

## 最小复述

不看资料回答若干关键问题。
```

技术课程可使用 `source_days`；书籍和论文主题更适合 `source_units`。不要为了统一而丢失来源语义。

## 2. 增量知识地图

```markdown
---
type: knowledge-map
source_course: 来源名称
source_case: 案例或书名
source_units:
  - 学习单元
status: learning
---

# 案例或书名：学习单元 增量知识地图

## 定位

## 增量卡片

### 领域一

- [[新建或更新的卡片]]

## 复用已有卡片

- [[只复用的旧卡]]

## 上下位关系

## 推荐复习顺序

## 完成标准
```

论文主题集可以追加：

```markdown
## 一致证据

## 分歧与边界

## 尚未解决的问题
```

## 3. 永久知识卡片

```markdown
---
type: knowledge-card
knowledge_level: concept
topic:
  - 主题
source_course: 来源名称
source_case: 案例或书名
source_units:
  - 学习单元
parent: "[[直接上位卡片]]"
evidence_level: L2-runtime
status: learning
---

# 卡片名称

## 核心问题

## 核心结论

## 原理

## 适用场景

## 操作或推理流程

## 来源与证据

- [[完整来源路径#精确标题]]
- [[代码、图表或论文证据]]

## 相关卡片

- 上位：[[上位概念]]
- 下位：[[下位方法]]
- 前置：[[前置知识]]
- 并列：[[相关知识]]

## 局限

## 掌握标准

- [ ] 能解释核心原理。
- [ ] 能识别适用条件。
- [ ] 能迁移到新问题。
```

并非每张卡都必须保留所有小节。删除不适用的小节，不写空标题。

## 4. 案例或材料 README

```markdown
# 材料集合学习入口

## 定位

## 学习单元一

- 首次学习：[[指南]]
- 复习地图：[[地图]]
- [[增量卡片]]

原始材料：

- [[原始笔记或章节]]

## 建议顺序
```

README 只承担入口和整体定位，不复制指南的教学正文。

## 5. Frontmatter 字段

推荐字段：

| 字段 | 含义 |
|---|---|
| `type` | `learning-guide`、`knowledge-map`、`knowledge-card` |
| `knowledge_level` | `concept`、`method`、`pattern`、`technique`、`detail` |
| `source_course` | 课程、作者或材料集合 |
| `source_case` | 案例、书名或研究主题 |
| `source_days` | 按 Day 组织时使用 |
| `source_units` | 章节、视频模块或论文主题时使用 |
| `parent` | 直接上位知识 |
| `children` | 直接下位知识 |
| `evidence_level` | L1-L4 证据强度 |
| `status` | `seed`、`learning`、`verified`、`mastered` |

不要把普通相关关系写入 `parent`。
