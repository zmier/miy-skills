# 2026-07-09 research-roadmap 子 Skill

## 来源

CASE-260521 基金经理研究的 TASK06 产生了一个管理问题：

```text
旧的任务谱系图能说明文件结构，却不能一眼说明研究如何从“初始发现”推进到“后续问题”。
```

具体表现为：

```text
TASK06-1 已发现：基金经理回答问题后，申购与赎回同时显著放大，但净 flow 不显著。
该结果自然引出 puzzle：为什么回答没有带来单向净流入，而是同时激活买和卖？
TASK06-2 / TASK06-3 是样本与识别口径诊断；
未来 TASK06-4 应是机制探索。
```

因此需要一种介于研究叙事与项目管理之间的 artifact：

```text
Research Roadmap / 研究路线图
```

## 新增规则

已新增：

```text
skills/research-roadmap/SKILL.md
```

该 Skill 的职责：

- 将 `initial empirical fact -> puzzle -> diagnostic branch + mechanism branch -> claim convergence` 画成 Mermaid roadmap；
- 区分 Research Roadmap、Task Lineage Map、Project Change Map 和 Technical Route；
- 使用 Mermaid `click` 将节点链接到稳定 Markdown 入口；
- 避免让 TASK 编号和目录结构支配研究叙事。

## 当前状态

```text
seed / forward-test-with-CASE-260521
```

该规则来自真实项目现场，但仍需通过 TASK06 README、coauthor email 和后续 TASK06-4 继续 forward-test。
