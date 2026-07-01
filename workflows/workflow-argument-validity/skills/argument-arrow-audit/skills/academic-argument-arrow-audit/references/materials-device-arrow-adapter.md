---
date: 2026-06-21
type: reference
status: candidate / forward-tested-once
scope:
  - academic-argument-arrow-audit
  - materials-device-paper
  - engineering-experimental-paper
source_case:
  - J-260110/Piqiu/TASK03-materials-hydrovoltaic-full-evidence-arrow-audit
---

# Materials / Device Arrow Adapter

## 定位

本 adapter 用于材料、器件和工科实验论文的学术验箭头。

它不针对某一篇水伏发电论文，而是把该案例中暴露出的可迁移失败模式范化为工科实验论文常见箭头。

适用论文包括：

```text
materials science
functional materials
nanomaterials
composite / biomass materials
energy harvesting devices
sensors
wearable electronics
flexible devices
environment / catalysis / electrochemical experimental devices
```

## 与“老王逻辑谬误”的关系

工科论文仍然遵循通用论证有效性逻辑：

```text
A 是否足以推出 B？
```

差别只在 A 和 B 的外壳：

```text
论效题：调查、销量、城市、政策、民意 -> 结论
实证论文：变量、模型、系数、识别 -> 因果/贡献
工科实验论文：制备、表征、性能、对照、稳定性、demo -> 机制/性能/应用/贡献
```

因此使用顺序不变：

```text
1. 固定 arrow_id: A -> B
2. 用 arrow-audit-core 判断 A 为什么不足以推出 B
3. 再翻译成材料/器件论文的审稿语言
```

不要在审稿意见里写“作者偷换概念、以偏概全”。应翻译为：

```text
characterization evidence does not yet establish the proposed mechanism
performance comparison is not normalized under comparable conditions
prototype demonstration does not yet support the claimed practical deployment
```

## 高频箭头

| arrow family | 作者常用 A | 作者想推出 B | 常见断点 |
|---|---|---|---|
| synthesis/process -> material identity | 制备流程、照片、尺寸、工艺参数 | 材料/器件被成功制备且可复现 | 缺少关键参数、批次、重复、产率、尺寸分布 |
| characterization -> structure/property | SEM/TEM/AFM、FTIR、XPS、Raman、XRD、BET、接触角、EIS | 结构、官能团、组成、孔道、导电性、亲疏水性已改变 | 表征只能证明局部/表面/存在，不能证明整体或功能 |
| characterization -> mechanism | 表征图谱、schematic、水传输、电荷分布、能级图 | 作者提出的机制真实发生 | plausibility 被写成 proof；缺少直接机制实验 |
| control experiment -> causal factor | 单因素对照、去掉组分、改变工艺、替换材料 | 某因素是性能提升原因 | 多因素同时改变；缺少等量/等结构/等面积对照 |
| lab metric -> performance claim | 电压、电流、灵敏度、效率、降解率、响应时间、功率 | 高性能 / 优异性能 | 量纲、负载、面积、质量、长度、湿度、电解质、光照等口径不清 |
| normalized metric -> SOTA superiority | current density、power density、specific capacity、per-area/per-mass/per-length 指标 | 优于 SOTA / superior | 分母定义不同，测试条件不同，绝对输出与归一化指标方向冲突 |
| stability test -> durability claim | 短时曲线、循环、洗涤、弯折、储存、环境测试 | 稳定、耐久、可穿戴、可长期使用 | 时间太短，循环太少，真实工况缺失，缺误差/重复 |
| prototype demo -> application claim | LED、手机、灯泡、手环、织物、传感展示、污染物处理 demo | 可实际应用 / practical / continuous / self-powered | demo 只证明 proof-of-concept，缺持续时间、真实负载、储能路径和功率预算 |
| lab condition -> real-world deployability | 人工汗液、模拟污水、标准光照、固定湿度、静态弯折 | 真实人体/环境/产业部署可行 | 模拟工况不能自动外推到真实环境 |
| citation/SOTA table -> contribution | SOTA 表、综述引用、领域痛点 | 新颖、高性能、填补 gap | 文献覆盖不全，比较口径不一致，已有近邻方案 |

## 通用追问

每条材料/器件箭头至少问：

```text
作者的 A 最直接证明了什么？
作者的 B 比 A 多上升了哪一步？
这一步需要什么额外证据？
该证据是本稿已有、需要 source QC、需要补实验，还是需要外部文献/SOTA 检索？
```

## 典型断点映射

| 工科表达 | 对应通用 break_type | 审稿语言 |
|---|---|---|
| 表征不能证明机制 | mechanism-over-interpretation / hidden-premise-missing | The characterization results support structural or compositional changes, but they do not yet directly establish the proposed mechanism. |
| 归一化性能不可比 | comparison-mismatch / numerical-trap | The performance comparison requires consistent normalization and testing conditions before a superiority claim can be made. |
| 单因素优化不够稳健 | uncontrolled-comparison / hidden-premise-missing | The optimization tests vary or report only limited conditions, making it difficult to isolate the claimed causal factor. |
| demo 被上升成应用能力 | scope-expansion / overclaim | The demonstration supports prototype feasibility, but not yet practical or continuous operation under realistic load conditions. |
| 短时稳定性推出长期耐久 | extrapolation-mismatch / scope-expansion | The stability evidence is shorter or narrower than the durability claim requires. |
| SOTA 表支持不足 | comparison-mismatch / evidence-qc-gap | The benchmark needs comparable device geometry, normalization, environment, electrolyte, load, and reporting basis. |
| 缺补充图/原始图核验 | evidence-qc-gap | The claim cannot be assessed until the relevant figure panels or supplementary materials are available and checked. |

## Evidence Sufficiency Guide

### Characterization -> Mechanism

常见 A：

```text
SEM/TEM morphology
FTIR/Raman/XPS/XRD spectra
contact angle
water uptake / transport rate
conductivity / impedance
schematic mechanism diagram
```

这些通常能支持：

```text
结构变化存在；
组分或官能团变化存在；
界面或表面性质可能改变；
机制具有 plausibility。
```

通常不能单独支持：

```text
完整机制已被证明；
某路径是唯一主导机制；
电荷分离/传输/复合损失已被直接验证；
实际工作条件下机制仍成立。
```

常见补强证据：

```text
in-situ / operando measurement
zeta potential / surface charge
electrochemical impedance spectroscopy (EIS)
conductivity mapping
ion selectivity / diffusion tests
controlled electrode experiments
isotope / tracer / blocking experiment
finite element / mechanism model with validation
```

### Metric -> Performance

检查口径：

```text
voltage: open-circuit or under load?
current: short-circuit or load current?
current density: normalized by what area?
power density: calculated under which load and area?
response time / sensitivity: same analyte, same range, same environment?
efficiency: same input definition?
```

常见 Red flags：

```text
absolute current falls while current density rises;
area / mass / length denominator is unclear;
different tests use different contacts or device geometries;
comparison table mixes open-circuit, short-circuit and load outputs;
error bars, n, and repeatability are missing;
ambient humidity, electrolyte, light intensity, temperature, pressure, or flow rate differs.
```

### Demo -> Application

demo 可支持：

```text
prototype feasibility;
integratability;
proof-of-concept under selected conditions;
visual demonstration.
```

demo 不自动支持：

```text
continuous operation;
practical power supply;
real-world deployment;
commercial viability;
human-wearable durability;
system-level self-powered operation.
```

必须追问：

```text
真实负载功率是多少？
是否有 capacitor / battery / external storage assistance？
能持续多久？
是否在真实工况、人体/现场环境或仅模拟液中测试？
有多少循环、多少样本、多少佩戴/弯折/洗涤次数？
是否报告 failure mode？
```

## External Evidence Route

当箭头涉及 SOTA、文献 gap、机制标准或同类器件能力时，进入 `external-evidence-request.md`。

优先路线：

```text
English / international engineering literature:
  scholar-kit-literature-search -> OpenAlex
  WoS if user requests WoS/SCI traceability, venue filtering, or OpenAlex insufficient

Chinese engineering literature:
  CNKI when Chinese literature, Chinese material context, or domestic corpus claim matters

Mechanism / method standard:
  review articles, method papers, highly cited device papers, official standards if applicable

SOTA / benchmark:
  recent reviews, benchmark tables, top journal device papers, DOI/publisher metadata
```

web search can locate DOI or publisher pages, but should not replace database-level search when the arrow depends on literature coverage.

## QC Flags

Use these flags in audit tables:

```text
needs-panel-level-figure-qc
needs-supplementary-material
needs-raw-data
needs-metric-normalization
needs-load-condition-qc
needs-device-geometry-qc
needs-sota-comparison-qc
needs-mechanism-direct-evidence
needs-control-experiment
needs-durability-protocol
needs-real-world-condition-test
```

## Output Pattern

When writing `final_audit`, use this structure:

```text
A 支持较弱结论；
B 比 A 多上升了哪些前提；
这些前提当前是 missing / needs-qc / needs-external-evidence / externally confirmed weak；
建议补什么实验、补什么口径，或如何降调。
```

Example pattern:

```text
The SEM/XPS results support a structural or surface-composition change after treatment, but they do not directly establish the proposed charge-collection mechanism. That inference would require additional electrical/ionic transport evidence, such as EIS, conductivity mapping, ion-selectivity tests, or electrode-control experiments. The mechanism claim should therefore be framed as a proposed mechanism unless such evidence is added.
```

## 当前状态

本 adapter 来自一个水伏/竹纤维/可穿戴能源收集案例的 forward test，状态仍为：

```text
candidate / forward-tested-once
```

使用时可以作为材料/器件论文审计提示，但不要把其中任何具体水伏判断当作通用结论。
