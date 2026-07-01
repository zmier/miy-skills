---
date: 2026-06-20
type: reference
status: seed
scope:
  - materials-science
  - hydrovoltaic-generation
  - device-paper
  - experimental-paper
---

# Materials Hydrovoltaic Adapter

## 定位

本 adapter 用于材料、器件和水伏发电类论文的 paper 抽树。

它不替代通用 claim/evidence 协议，而是告诉 `academic-paper-argument-tree-extraction` 在材料器件论文中应优先寻找哪些 claim 和 evidence。

核心问题通常不是：

```text
X 变量是否显著影响 Y
```

而是：

```text
材料 / 结构 / 界面设计
-> 电荷分离、离子迁移、水-固界面相互作用等机制
-> 输出电压 / 电流 / 功率密度 / 稳定性提升
-> 器件可用性、可扩展性或应用价值成立
```

## 何时读取

遇到以下内容时应读取本 adapter：

- hydrovoltaic generation / water-enabled electricity / moisture-electric generation;
- 材料水伏、蒸发发电、湿气发电、流动水发电；
- 纳米材料、多孔材料、碳材料、纤维素、氧化石墨烯、MXene、聚合物、凝胶、膜材料；
- device fabrication / prototype / power output / stability test;
- SEM / TEM / AFM / XRD / XPS / FTIR / Raman / BET / zeta potential / contact angle;
- I-V curve / V-t curve / current density / power density / load resistance / series-parallel device tests。

## 常见 Claim

材料水伏论文通常需要还原以下 claim：

```text
C-DESIGN: 新材料 / 结构 / 界面设计是有意义的
C-FAB: 材料或器件已被成功制备
C-STRUCT: 材料具有作者声称的形貌、孔结构、组成或表面性质
C-MECH: 水-固界面、离子迁移、电荷分离或蒸发过程解释了发电机制
C-PERF: 器件输出性能优于对照或已有工作
C-CONTROL: 对照实验支持作者归因，不是环境噪声或伪效应
C-STABILITY: 器件具有稳定性、循环性或长期可用性
C-SCALE: 器件可串并联、放大或用于实际场景
C-SOTA: 与已有材料 / 器件相比具有优势
C-CONTRIB: 材料设计和机制发现构成论文贡献
```

这些都是 claim，因为都可以继续问：

```text
为什么？
作者用哪些表征、性能测试、对照实验或理论说明支撑？
```

## 必抽 Evidence

### 材料与制备

```text
E-MAT-COMP: 材料组成、前驱体、掺杂/复合组分
E-MAT-FAB: 制备流程、温度、时间、浓度、pH、干燥/退火条件
E-MAT-GEOM: 器件尺寸、膜厚、面积、质量负载、孔径或通道尺寸
E-MAT-ELECTRODE: 电极材料、接触方式、封装方式
```

### 结构与表征

```text
E-CHAR-SEM: SEM / TEM / AFM 中的形貌和尺度
E-CHAR-XRD: XRD 峰位和相结构
E-CHAR-XPS: XPS 元素价态或官能团
E-CHAR-FTIR: FTIR 官能团变化
E-CHAR-RAMAN: Raman D/G 或结构信息
E-CHAR-BET: 比表面积、孔径分布
E-CHAR-ZETA: zeta potential / surface charge
E-CHAR-CA: contact angle / hydrophilicity
E-CHAR-CONDUCT: 导电率、离子电导或电阻
```

### 测试条件

```text
E-TEST-WATER: 水类型、盐浓度、pH、离子种类
E-TEST-FLOW: 水流速度、蒸发速率、液面高度、压力差
E-TEST-HUMID: 环境湿度、温度、光照、空气流动
E-TEST-LOAD: 外接电阻、负载条件、测试电路
E-TEST-AREA: 输出是否按面积、质量或体积归一化
E-TEST-N: 重复次数、样本数、误差棒
```

### 性能结果

```text
E-PERF-VOC: open-circuit voltage / 输出电压
E-PERF-ISC: short-circuit current / 输出电流
E-PERF-DENSITY: current density / power density
E-PERF-IV: I-V curve / load resistance curve
E-PERF-TIME: voltage-time / current-time curve
E-PERF-SERIES: 串联 / 并联器件输出
E-PERF-ENERGY: charging capacitor / powering LED / practical demo
```

### 对照与机制

```text
E-CTRL-BLANK: 空白材料 / 无功能组分 / 无水条件对照
E-CTRL-MATERIAL: 不同材料、不同孔结构、不同表面处理对照
E-CTRL-ION: 不同盐浓度、离子种类、pH 对照
E-CTRL-HUMID: 湿度 / 蒸发 / 流动条件变化
E-MECH-SCHEME: 机制示意图
E-MECH-MEASURE: 离子浓度梯度、电势分布、表面电荷、流动电位等机制测量
E-MECH-SIM: FEM / DFT / MD / theoretical model / simulation support
```

### 稳定性与可用性

```text
E-STAB-CYCLE: 循环次数和性能保持率
E-STAB-LONG: 长时间运行曲线
E-STAB-ENV: 不同湿度、温度、水质条件下稳定性
E-STAB-MECH: 弯折、拉伸、压缩或机械耐久性
E-SCALE-DEVICE: 面积放大、阵列、串并联、封装和应用 demo
```

### SOTA 对比

```text
E-SOTA-TABLE: 与已有工作对比表
E-SOTA-METRIC: 对比指标口径，如 voltage、current density、power density、area normalization
E-SOTA-CONDITION: 对比测试条件是否一致，如湿度、流速、盐浓度、面积、负载
```

## Claim / Evidence 边界

| 内容 | 类型 |
|---|---|
| 作者声称新材料结构能提升水伏输出 | claim |
| SEM 图显示多孔结构，孔径约 X nm | evidence |
| 作者声称表面官能团促进离子迁移 | claim |
| XPS / FTIR 显示某官能团变化 | evidence |
| 作者声称机制是电荷分离 / 离子梯度 | claim |
| zeta potential、离子浓度对照、机制示意图 | evidence |
| 作者声称输出性能优于对照材料 | claim |
| V-t 曲线、I-V 曲线、功率密度表格 | evidence |
| 作者声称器件可长期稳定运行 | claim |
| 24 h / 100 cycles 曲线和性能保持率 | evidence |

## Handoff to Arrow Audit

paper 抽树阶段只还原作者树和 evidence，不判断作者机制是否真的成立。若发现下列高风险点，只在 `extraction-qc.md` 标记 handoff：

```text
needs-performance-metric-qc
needs-sota-comparison-qc
needs-mechanism-evidence-audit
needs-control-experiment-audit
needs-stability-evidence-audit
```

后续 `academic-argument-arrow-audit` 可重点检查：

- 性能指标口径是否一致；
- 功率密度是否按同一面积 / 质量 / 体积归一化；
- 对照实验是否足以排除环境湿度、蒸发、接触电势或仪器噪声；
- 机制 evidence 是否真的支持机制 claim；
- 稳定性测试是否足以支撑应用价值；
- SOTA 对比是否同条件、同口径。

## Red Flags

- 只写“性能优异”，没有具体电压、电流、功率密度和测试条件；
- 只写“机制如图所示”，没有机制测量或对照 evidence；
- 对比 SOTA 时未记录湿度、流速、盐浓度、面积、负载等条件；
- 稳定性只展示短时间曲线，却上升到长期应用；
- 没有重复次数、误差棒或样本数，却做强性能 claim；
- 把表征结果直接当成器件性能提升的充分证明。
