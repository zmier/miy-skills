---
date: 2026-06-20
type: reference
status: structural-green
scope:
  - academic-argument-arrow-audit
---

# Method Knowledge Feedback

## 定位

本文件用于处理学术验箭头中不断出现的专用方法知识缺口，例如：

```text
DID / IV / PSM / RDD / event study
DAG / front-door / back-door
NPLR / nonlinear test / threshold model
SEM / mediation / moderation
材料科学实验表征 / 工程实验设计
```

这些知识属于 `academic-argument-arrow-audit` 的路由范围，但不要求主 Skill 一开始全部内置。

## 红灯原则

遇到拿不准的新方法、新统计检验、新实验设计、近期顶刊方法或跨学科技术时，不得硬验。

必须先标记：

```text
status: unclear / needs-qc
qc_flags: method-qc
break_type: evidence-qc-gap 或 method-knowledge-gap
```

然后进入“检索学习 -> 回填审计 -> 反哺沉淀”流程。

不要把“我暂时不知道怎么验”伪装成作者方法错误；也不要因为方法新、复杂或不熟悉就默认作者成立。

## 方法知识缺口处理流程

```text
1. 固定 target_arrow: A -> B
2. 标记 method_knowledge_gap
3. 判断缺口属于哪类箭头
4. 选择检索 / 联网 / scholar-kit 路线
5. 优先读取高质量来源
6. 提炼该方法的验收点
7. 回到 target_arrow 完成审计
8. 把学习过程留在 TASK
9. 把可迁移规则沉淀为 reference candidate
10. 高频复用后升级为子 Skill
```

第 7 步回填时，必须仍然回到原始问题：

```text
作者用 A 是否足以推出 B？
```

不能把方法综述写成脱离箭头的知识笔记。

## 检索与学习路线

若缺口涉及最新方法、近期顶刊、软件包版本、统计实践或高风险事实，应先检索核验。优先级：

```text
1. 方法原始论文
2. 顶刊应用论文，尤其是 FT50、UTD24、Nature、Science、PNAS 或领域顶刊
3. 作者 appendix、replication package、official code、package documentation
4. 综述、教材、handbook、权威课程资料
5. 普通网页或博客，只作辅助理解，不单独作为审稿判断依据
```

可调用能力：

| 场景 | 路线 |
|---|---|
| 文献 gap / 知识树 / 相近研究 | `academic-literature-gap-arrow-audit` -> `scholar-kit-literature-search` |
| 英文方法论文、顶刊应用 | OpenAlex / WoS / web search，优先原文与官方材料 |
| 中文方法、中文期刊谱系 | CNKI 相关检索 Skill |
| 软件包、统计命令、官方实现 | 官方文档、CRAN/PyPI/GitHub/作者主页 |
| 当前日期后可能变化的信息 | 联网核验，不依赖记忆 |

检索状态必须区分：

```text
not-searched
search-in-progress
true-zero-result
insufficient-result
manual-verification-needed
technical-failure
```

不得把登录、验证码、网络错误或数据库故障当成“没有文献/没有证据”。

## 记录格式

```text
method_knowledge_gap:
  case_id:
  method:
  target_arrow:
  arrow_type:
  current_claim:
  why_current_reference_insufficient:
  what_needs_to_be_checked:
  needed_source_or_skill:
  search_route:
  source_priority:
  learning_notes_path:
  return_to_arrow_audit:
  proposed_feedback_target:
  status: case-log / reference-candidate / subskill-candidate / validated
```

## 反哺规则

1. 第一次遇到：写入 case / TASK log 和 `method-knowledge-gap.md`，不急着写成通用规则；
2. 检索学习过程留在当前 TASK，包含检索式、来源、关键判断点和无法确认之处；
3. 能抽象出稳定判断路径：写入 reference；
4. 若属于既有子 Skill 范围，沉淀到对应子 Skill：
   - 因果识别方法 -> `academic-causal-arrow-audit`;
   - 统计/显著性/量纲/非线性方法 -> `academic-statistical-result-arrow-audit`;
   - 文献 gap / 知识树 -> `academic-literature-gap-arrow-audit`;
   - 通用学术审稿表达 -> `academic-fallacy-adapter.md`;
5. 需要反复执行、调用外部材料或生成专门 ledger：升级为子 Skill；
6. 每次升级后，按 `workflow-tao` 回归测试协议，用纯净 subAgent 跑一次相关 fixture；
7. 若新规则只适用于某学科、某方法传统、某期刊族或某数据结构，必须写明适用边界。

## 沉淀位置

| 内容 | 放置位置 |
|---|---|
| 当前案例的具体学习过程、检索式、失败记录 | 当前 TASK 的 `log.md` / `method-knowledge-gap.md` |
| 可迁移但尚未验证的方法审查点 | `references/*-method-audit.md` 或对应子 Skill reference |
| 因果识别方法 | `skills/academic-causal-arrow-audit` |
| 统计结果和非线性方法 | `skills/academic-statistical-result-arrow-audit` |
| 文献 gap、知识树、顶刊相近研究 | `skills/academic-literature-gap-arrow-audit` |
| 可复用审稿表达 | `references/academic-fallacy-adapter.md` |
| 高频、步骤稳定、需要专门输入输出的能力 | 新建 `skills/*-method-arrow-audit` |

## DAG 的位置

DAG 只用于验因果识别类箭头：

```text
design / model / identification -> causal claim
```

它不用于替代文献 gap、变量定义、统计显著性、贡献上升等审查。

DAG 审查至少回答：

```text
outcome Y 是什么？
treatment X 是什么？
可能的 common causes 是什么？
作者控制/固定效应/设计是否关闭后门路径？
是否存在反向因果？
是否误控中介或 collider？
前门路径是否被声称且是否成立？
```
