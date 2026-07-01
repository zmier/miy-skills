# Fractal Task-Driven Philosophy

## 一句话

`task-driven` 不是“项目执行阶段”的技巧，而是一种可以递归套用的工作哲学：

```text
任何复杂目标
-> 都可以被拆成 TASK
-> 每个 TASK 都应有证据、日志、验收和复盘
-> 阶段 Green 后再进入下一层目标
```

## 分形结构

同一个外部项目可能自然拆成多个 task-driven project：

```text
机会评估 project
  目标：判断要不要做。

执行交付 project
  目标：完成已确认范围。

复盘沉淀 project
  目标：把经验变成可迁移规则。

能力工程 project
  目标：更新 workflow / skill / template 并做回归。
```

这些不是一条线上的“普通步骤”，而是每一层都有独立目标、TASK 树、证据边界和完成标准。

## 与 task-driven-project-manager 的关系

`task-driven-project-manager` 负责当某个阶段已经决定要落地成项目文件夹时，创建 README、Makefile、dashboard、tasks、tests、final_outputs 等骨架。

本 workflow 负责更上层的判断：

```text
现在的目标是什么？
这是哪个阶段？
应该创建哪类 task-driven project？
是否需要场景 adaptor？
Green 后进入哪一层？
```

## 禁止事项

- 不要把“评估要不要做”当成闲聊，它也需要 TASK、证据和验收。
- 不要把机会评估和实际执行混在同一个报价或 TASK 里。
- 不要把阶段 Green 偷换成最终 Green。
- 不要让脚手架动作替代目标判断。

