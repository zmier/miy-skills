# AOSP / ART / FART 高侵入恢复路线

## 定位

这条 reference 只用于 `recover-android-dex` 的高级分支。

当 frida-dexdump、ClassLoader dump、DefineClass Hook、自研内存扫描等低侵入路线无法恢复目标业务类或真实函数体时，才考虑 AOSP/ART/FART 类路线。

它不是默认路径，也不是普通请求复现任务的必经步骤。

## 典型红灯

| 红灯 | 可能含义 | 看雪资料入口 |
| --- | --- | --- |
| 普通 ClassLoader / frida-dexdump 路线能看到类，但函数体缺失或关键方法不可用 | 抽取壳或 code item 未恢复 | 看雪第2章 课时5-9；第10章 课时6、12 |
| 需要理解 FART 为什么要主动调用 | 仅 dump dex 结构不够，需要触发方法恢复真实 code item | 看雪第2章 课时6-8；第10章 课时6-8 |
| JADX 只能看到壳代码，业务类运行时才出现 | 加壳、动态加载、ClassLoader 替换 | 看雪第10章 课时1-5；P0 ClassLoader 提炼 |
| dump 出 dex，但目标函数全是 nop 或空实现 | 函数抽取壳，只拿到 dex 结构，没拿到真实 code item | 看雪第10章 课时6、12；P1 FART/code item 提炼 |
| frida-dexdump 得到大量重复/坏 dex，目标类不可用 | dump 时机不对，或壳在 ART 生命周期更深处处理 | 看雪第10章 课时4-8 |
| 目标函数运行时指向另一片 code item 区域 | 修改偏移型抽取壳 | 看雪第10章 课时12 |
| FART 路线成本过高或版本不匹配 | 可评估 fdex2 / 高版本 fdex2 平行路线 | 看雪第10章 课时10-11 |
| repaired dex 仍然无法被 JADX 正常阅读 | 需要 code item/bin 五元组或定制 JADX 后处理 | 看雪第10章 课时12、15 |
| 需要观察 ART 解释器执行路径 | 高侵入执行观测，不是默认脱壳步骤 | 看雪第10章 课时13-14 |
| 需要长期、多样本、稳定地观察 dex/load method/code item | 单次 Frida 脚本成本过高或时机不稳 | 看雪第10章 课时6-12；第12章 Fart10_12 |
| FART 源码能编译/刷入但目标 dex 仍不可用 | 这只是 environment/toolchain Green，不是 Dex 恢复 Green | 看雪第12章 Fart10_12 |
| 需要在 ART 解释器、ClassLinker、LoadMethod、LinkCode 等点观测 | 必须改 ART 或使用定制 Runtime | 看雪第4章；第10章；第12章 |
| ART 内部 hook 点找到了但结构体字段、对象布局或 inline 导致读值不稳 | ART C++ 对象语义或版本差异未处理 | 看雪第4章 课时1-7 |
| 需要比较 Frida Hook、ART 定制、AOSP 修改等方案成本 | 进入高侵入路线前需要方案选择 | 看雪第4章 课时8 |

## 路线含义

所谓 AOSP/ART 改造，不是改目标 App，而是改 Android Runtime：

```text
AOSP 源码
→ 修改 ART / ClassLinker / DexFile / Interpreter 等关键路径
→ 编译 system/boot 等镜像
→ 刷入专用实验设备
→ 用定制 Runtime 观察类加载、方法初始化、code item、解释执行或 dump dex
```

它可以用于：

- 在 dex 定义或类加载时 dump；
- 在 `LoadMethod` / `LinkCode` / `Execute` 等点拿到 `ArtMethod`、`DexFile`、`code item`；
- 配合 FART 主动调用组件恢复函数抽取壳；
- 生成 bin / repaired dex，供定制 JADX 或普通反编译工具使用。

## 与普通 dump 路线的区别

| 路线 | 观察位置 | 成本 | 适合场景 |
| --- | --- | --- | --- |
| frida-dexdump / 内存扫描 | 进程内存中的 dex magic | 低 | 壳不强、目标类已加载 |
| DefineClass Hook | libart 中 dex 定义时刻 | 中 | 普通 dump 漏类或时机不准 |
| ClassLoader / Xposed | 类加载和 loader 视角 | 中 | 需要知道哪个 loader 承载业务 dex |
| FART / ART 改造 | Runtime 生命周期内部 | 高 | 函数抽取壳、code item 修复、批量研究 |
| 定制 JADX / repaired dex | dump 后处理 | 中 | dex 已有，但函数体不可读 |

## 升级门槛

只有同时满足以下条件，才升级到 AOSP/ART/FART 路线：

1. 当前 TASK 明确授权脱壳和系统级实验；
2. 低侵入路线已尝试或有明确不适用证据；
3. 目标 Green 需要恢复真实业务类或真实 code item，而不仅是证明存在壳；
4. 有独立实验设备、刷机能力和回滚方案；
5. 能接受编译 AOSP、版本适配和长时间构建成本；
6. 产物只留在授权 TASK 目录，不进入通用 workflow。

## Green 边界

AOSP/ART/FART 路线的 Green 不是“系统能刷起来”，而是：

- 能稳定捕获目标 dex 或目标类；
- 目标函数的 code item 已恢复或能解释为何仍缺失；
- repaired dex 或 smali 能被工具打开并定位目标方法；
- 目标方法的静态可读性与运行时行为通过一次独立证据交叉验证；
- 课程来源和本次改动写入 TASK 与 `course-provenance.md`。

如果只完成编译、刷机或工具启动，应标为 `environment-green`，不能写成 Dex 恢复完成。

FART10/FART10_12 这类源码移植路线还要额外记录：

- ART 版本、设备系统版本和源码分支；
- 修改点、补丁文件和构建命令；
- 刷入方式、回滚方式和实验设备隔离；
- 本次目标 dex/code item/repaired dex 是否真正可用；
- 若只是样例运行成功，标记为 `toolchain-green` 或 `environment-green`。

## 看雪查字典入口

优先查看：

- 看雪第4章：C++11 / ART 打造动态分析沙箱，尤其课时5-8；
- 看雪第2章：Frida_FART全自动脱壳机，尤其课时4-9；
- 看雪第10章：Frida_Fart脱壳；
- 看雪第10章课时10-15：fdex2、高版本适配、定制 JADX、ART 解释器 trace、JNI 地址绑定；
- 看雪第12章：Fart10_12；
- P1：FART 框架简介与脱壳点的选择；
- P1：FART 与定制版 JADX；
- workflow 顶层 `../../../references/kanxue-course-directory-index.md`。

采用后回写 workflow 顶层 `../../../references/course-provenance.md`。
