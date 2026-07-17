# paper-extract: A04/A05 按 Pi-R / design block 组织

## 背景

在拆出 `paper-extract` 后，需要进一步明确 A04/A05 的边界。

关键问题：

```text
A04 是跟着 A03 的 proxy / measure 走，还是跟着命题支 / design block 走？
控制变量应放 A04 还是 A05？
```

## 结论

更稳的组织是：

```text
A04 = A04-Pi-R Measurement / Data Block
A05 = A05-Pi-R Design / Identification Block
```

其中：

```text
A04 管变量如何进入数据；
A05 管变量为何进入模型。
```

## A04 的完整定位

A04 承接 A03，但外壳按 `Pi-R / design block` 组织。

每个 A04 block 包含：

```text
linked proposition / relation:
  服务哪个 Pi-R。

linked A03 bridges:
  承接哪些 A03-Pi-X / A03-Pi-Y / A03-Pi-R。

core measures:
  A03 中核心 X / Y / relation 对象如何量。

design-support measures:
  该 Pi-R 设计中的控制变量、固定效应变量、分组变量、样本筛选变量、滞后项、权重等如何量。

measurement risks:
  缺失值、频率错配、构念效度、测量误差、样本选择、聚合误差、窗口设定风险。
```

这避免了一个错误暗示：

```text
全篇论文共享一套统一 controls。
```

不同命题支 / 设计块可以有不同的 controls、FE、样本、窗口和支撑变量。

## A05 的完整定位

A05 与 A04 对齐，也按 `Pi-R / design block` 组织。

每个 A05 block 包含：

```text
linked proposition / relation:
  检验哪个 Pi-R。

empirical test / model / comparison logic:
  回归、事件研究、面板设计、预测设计、实验、准实验、分组比较等。

time order:
  X / exposure / treatment 是否先于 Y。

design function of variables:
  核心 X / Y 如何进入模型；
  控制变量为什么进入模型；
  固定效应控制什么；
  分组 / decile / matching / weights 服务什么比较逻辑。

identification claim:
  支持相关、预测、机制解释还是因果解释。

key assumptions and threats:
  混淆、反向因果、遗漏变量、选择偏误等剩余问题。
```

## 控制变量的放置

控制变量不能完全丢到 A05，也不能只放 A04。

```text
A04:
  控制变量的数据身份：是什么、从哪里来、怎么量。

A05:
  控制变量的设计功能：为什么控制它、放进哪个模型、缓解什么混淆。
```

## 对模板的修改

`paper-extract/templates/automatic-extraction-template.md` 中：

- A04 从逐个 A03 bridge 的 measurement table 改成 block table；
- A05 增加 `Linked A04 Block` 和 `Design Function Of Variables`；
- 明确不要暗示全篇统一 controls。

