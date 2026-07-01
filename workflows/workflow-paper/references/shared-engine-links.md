# Shared Engine Links

状态：`seed`

`workflow-paper` 当前只记录组合关系，不复制底层引擎规则。

## 通用引擎

| 引擎 | 用途 | 关系 |
|---|---|---|
| `../workflow-argument-validity` | 抽论文论证树、验箭头、修复映射、选问题、中文论证写作 | 组合调用 |
| `../workflow-md-to-word-formatting` | Markdown / Word / 期刊样式 / 学位论文样式交付 | 组合调用 |
| `../workflow-task-driven-project` | 项目与 TASK 组织 | 组合调用 |
| `/Users/narra/Documents/alib/Writer/.pytools/scholar-kit` | 文献检索、CNKI/WoS/OpenAlex、引用和全文获取相关能力 | 组合调用 |

## 原则

```text
跨领域复用能力保持为 shared engine；
论文领域专属路线放入 workflow-paper 的 subworkflows 或 skills。
```
