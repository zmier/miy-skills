# Project-Embedded Paper Learning Boundary

## 背景

`workflow-paper` 管论文工作总路由，包括学论文、写论文、审稿/自审、返修和格式交付。但“学论文”有两种语境：

```text
独立学论文；
项目内学论文。
```

二者不能混同。

## 决定

独立学论文：

```text
目标是读懂论文、拆模板、学习写法或生成个人阅读资产；
不要求存在 task / route / node；
不强制项目回挂。
```

项目内学论文：

```text
目标是服务当前 research project / task / route / node；
需要判断文献对 claim、proxy、data need、design option、threat 或 writing pattern 的贡献；
应交给 workflow-research/skills/research-literature-reader 管资产沉淀和项目回挂。
```

## 路由边界

`workflow-paper` 只判断这件事属于“学论文”大类，以及是否嵌入研究项目。若嵌入研究项目，不由 `workflow-paper` 接管 task / route / node 回挂，而是转交 `research-literature-reader`。

## 迁移边界

该规则来自 `CASE-260521-基金经理研究` 的文献阅读 forward-test。它适用于学术研究项目中“带着实验设计、变量构造、识别策略或候选 route 去读文献”的场景；不适用于纯个人阅读、课程阅读或通用论文模板学习。
