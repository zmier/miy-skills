---
date: 2026-06-21
type: reference
status: candidate
scope:
  - academic-arrow-repair-mapping
  - materials-device-engineering-papers
source:
  - J-260110 皮丘水伏论文 TASK03 与真实审稿意见对照
---

# Materials / Device Repair Menu

本文件是材料、器件、能源收集、传感器、柔性电子、可穿戴等工科实验论文的断箭头修复菜单。它不针对单篇水伏论文，而是把真实审稿意见中可迁移的补强逻辑抽象出来。

使用顺序：

```text
先固定 target_arrow_id: A -> B
再判断断点类型
再从本菜单选择 minimum / strong / fallback
```

## 通用原则

工科实验论文仍然遵循同一个问题：

```text
A 是否足以推出 B？
```

只是 A 常常是：

```text
SEM / XPS / XRD / EDS / zeta potential / EIS / contact angle / BET /
current density / power density / stability curve / prototype demo / SOTA table
```

B 常常是：

```text
材料结构成立 / 机制成立 / 性能更优 / 可穿戴可用 / 可规模化 / 贡献成立
```

## 常见修复映射

| arrow type | 常见断点 | minimum repair | strong repair | fallback if unavailable |
|---|---|---|---|---|
| synthesis/process -> material identity | 工艺描述不能证明材料结构或组分 | 补清楚样品命名、处理条件、对照样、关键参数 | 补 SEM/TEM、XRD、FTIR、XPS、EDS mapping、元素比例或形貌统计 | 降调为“制备得到目标样品并观察到若干特征”，不声称完整结构机制 |
| characterization -> structure/property | 单一表征不足以支撑结构/性能属性 | 补表征指标解释、图谱峰位/元素来源、对照样 | 多表征交叉验证，如 SEM + XPS + FTIR + BET/contact angle/capillary pressure | 降调为“表征结果与该属性一致”，不写成已充分证明 |
| characterization -> mechanism | 表征只证明现象存在，不能证明机制链 | 说明每个表征对应机制链哪一环 | 补 zeta potential、EIS、EDS ion mapping、in-situ/operando、对照实验、阻断实验；离子机制应考虑 operation 前后和蒸发前沿的 Na/Cl 空间分布 | 改为“可能机制/推测机制”，并说明仍需进一步验证 |
| control experiment -> causal factor | 对照不足，其他变量也变了 | 明确控制变量和唯一差异 | 增加空白对照、去除关键组分、替代材料、参数梯度、重复实验 | 降调为“结果提示该因素可能重要” |
| current density / voltage -> performance | 指标量纲、面积、负载、时间窗口不清 | 补公式、有效面积、负载条件、测试环境、重复次数 | 同条件报告 voltage/current/current density/power density、误差条、统计检验、长期曲线 | 降调为“在特定测试条件下表现较好” |
| normalized metric -> SOTA superiority | 与文献对比口径不同 | 补 SOTA 表并列明材料、面积、湿度、负载、测试方式 | 同口径 benchmark：current density、power density、stability、mechanical flexibility、condition | 降调为“与部分相关工作相比有潜力”，不写全面领先 |
| stability test -> durability | 短时曲线不足以证明长期耐久 | 补循环次数、环境条件、输出保持率 | 补时间梯度：minutes short-term、8 h、24-48 h、week-scale；再补洗涤、弯折、拉伸、汗液、重复使用后的输出保持 | 降调为“短期稳定”，不声称长期可穿戴耐久 |
| prototype demo -> application claim | 点亮 LED / 电容演示不能证明实用供能 | 补负载功率、持续时间、储能辅助、实际工作条件 | 补真实负载、动态佩戴、人工汗液、不同运动/湿度/温度、用户场景连续测试 | 降调为“概念验证原型（proof-of-concept）” |
| lab condition -> real-world deployability | 实验室条件不能推出真实场景 | 交代温度、湿度、汗液组成、机械扰动 | 补人工汗液组成和浓度，如 NaCl、urea、lactic acid、pH；补动态出汗、流速、汗液分布、纤维排列、织物集成、环境变化、洗涤/弯折 | 降调为“具有应用潜力，真实场景待验证” |
| coating/interface -> durable charge collection | 涂层存在或导电性不能证明潮湿/汗液条件下界面稳定集流 | 补涂层制备、界面接触、湿润前后电阻或输出保持说明 | 补 adhesion / interfacial bonding、湿度/汗液前后 coating morphology、电阻/EIS、剥离/弯折/洗涤后的导电保持、替代或去除涂层对照 | 降调为“涂层可能有助于电荷收集”，不声称稳定界面集流 |
| device series/parallel -> scale-up | 串并联提升不等于可规模化 | 补连接方式、内阻、接触电阻、等效电路 | 补 EIS、等效电路拟合、内阻/接触电阻、模块一致性、面积放大测试 | 降调为“模块化连接显示可扩展迹象” |
| citation/SOTA table -> contribution | 文献谱系不足或漏关键同类工作 | 补近年高质量同类论文和指标表 | 用同口径表格覆盖代表性 Nature/Science/PNAS/领域顶刊/高被引工作 | 降调贡献为“补充某一材料/场景/设计”，不写成开创性突破 |

## 真实审稿常见实验补强动作

这些动作通常用于增强机制、性能或应用箭头。使用时必须绑定具体 `target_arrow_id`：

| repair action | 主要增强的箭头 |
|---|---|
| zeta potential | 表面电荷 / EDL / 离子选择性机制 |
| EIS / equivalent circuit / internal resistance | 电荷传输、接触电阻、串并联放大、器件损耗 |
| EDS Na/Cl mapping | 离子泵、离子迁移、蒸发前沿富集机制；优先比较 operation 前后，并定位 evaporation front / wet-dry interface |
| BET / pore size / porosity | 孔结构、比表面积、水传输、蒸发增强；常与 contact angle、capillary pressure、evaporation flux 组成水传输证据包 |
| contact angle / capillary pressure | 亲水性、毛细输运、水分布机制 |
| evaporation flux / fluid dynamics | 水蒸发驱动、电流密度机制 |
| artificial sweat composition | 可穿戴汗液场景的外部有效性；至少说明 NaCl、urea、lactic acid、pH、浓度和动态流动条件 |
| bending / stretching / washing cycles | 可穿戴耐久性和机械稳定性 |
| 8h / 24-48h / several-week stability | 长期稳定性和应用可靠性 |
| SOTA benchmark table | 性能优势、贡献定位、同口径比较 |

## 水伏 / Hydrovoltaic 机制链修复模板

水伏论文中不要把“有输出”直接写成“机制成立”。先拆成几根小箭头：

| mechanism sub-arrow | 当前常见弱证据 | minimum repair | strong repair |
|---|---|---|---|
| surface charge / EDL | 只画示意图或引用 EDL | 说明表面电荷如何进入电压形成链条 | zeta potential before/after treatment；不同处理时间或组分梯度；把 zeta 与 voltage/current 关联 |
| ion selectivity / ion pump | 只说离子迁移或蒸发诱导 | 说明 Na/Cl 或其他离子在机制中的角色 | operation 前后 EDS / ion mapping；蒸发前沿或 wet-dry interface 的 Na/Cl 分布；浓度梯度或阻断实验 |
| water transport / evaporation flux | 只展示水传输照片或定性吸水 | 说明水传输指标、测试条件和样品差异 | BET / pore-size distribution / porosity、contact angle、capillary pressure、evaporation flux、fluid dynamics 或微通道定量 |
| external circuit / charge collection | 只说涂层导电或 carbon black 有利 | 说明涂层、电极、导电路径各自作用 | conductivity、EIS / charge-transfer resistance / ohmic resistance、internal resistance、去除/替代 coating 或电极对照 |
| interface stability / recombination loss | 只说 reduced recombination 或 enhanced collection | 降调为可能解释 | adhesion / interfacial bonding、湿度/汗液前后 coating morphology、电阻保持、洗涤/弯折后输出保持 |

输出时要写成：

```text
当前机制 claim 包含哪些小箭头？
每根小箭头已有 A 是什么？
还缺哪类直接证据？
如果不补，机制应降调到 proposed / consistent with。
```

## Wearable Demo Load-Energy Accounting

可穿戴应用演示不能只看“点亮了 LED / 给电容充电 / 做成头带”。必须把能量账讲清楚：

| required field | why it matters |
|---|---|
| load resistance / load type | 区分开路电压、短路电流和真实带载输出 |
| output voltage/current under load | 判断是否真的驱动负载 |
| power / power density calculation | 避免把最大电压和最大电流跨条件相乘 |
| duration | 判断是否 continuous，而不是瞬时演示 |
| capacitor / storage path | 区分 direct-load 与 storage-powered |
| external assist | 排除外部电源、预充电、人工操作造成的误读 |
| sweat / humidity / motion condition | 判断是否接近真实可穿戴场景 |
| repeat / device number / textile arrangement | 判断 fabric integration 和模块一致性 |

若缺这些字段，应用结论应降调为：

```text
proof-of-concept wearable-format demonstrator
```

而不是：

```text
practical continuous wearable power supply
```

## Wearable Durability 五分法

稳定性和耐久性不要混成一个词。至少拆成：

| durability subtype | weak evidence | stronger evidence |
|---|---|---|
| short-term output stability | 600-900 s 曲线 | 明确测试条件、输出保持率、重复 |
| long-term operational stability | 只延长到几分钟 | 8 h、24-48 h、week-scale 或与领域文献对齐的时长，并说明恢复性和盐积累 |
| mechanical retention | 一张弯折照片 | bending / folding / stretching cycles 后 Voc/Isc/power retention |
| washing retention | 洗后形貌照片 | standardized washing cycles 后输出保持、coating morphology、导电保持 |
| sweat robustness | 单一人工汗液 pH | NaCl、urea、lactic acid、pH、浓度、动态出汗、汗液分布和纤维排列 |

如果只有短时曲线，最多支持：

```text
short-term stability under tested condition
```

不能支持：

```text
wearable durability / long-term practical use
```

## 输出提醒

不要只写：

```text
建议补充机制实验。
```

要写成：

```text
target_arrow_id: A012
当前箭头：XPS/SEM 结果 -> 作者声称 EDL 与 carbon black charge collection 是主要机制。
最低修复：说明每个表征对应机制链哪一环，并补充对照样。
强修复：补 zeta potential、EIS/等效电路、EDS Na/Cl mapping 或阻断实验，分别验证表面电荷、电荷传输和离子迁移。
降调方案：如果无法补实验，应改写为“这些表征与该机制解释一致”，不能写成机制已被证明。
```
