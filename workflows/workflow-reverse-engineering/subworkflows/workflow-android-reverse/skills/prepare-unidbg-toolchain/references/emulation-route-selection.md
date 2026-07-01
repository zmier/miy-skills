# Unicorn / AndroidNativeEmu / Unidbg 路线选择

## 定位

本 reference 属于 `prepare-unidbg-toolchain`，用于在 Android native 算法准备离线执行前判断工具层级。

不要把所有“跑 so”都默认叫 Unidbg。实际有三层：

```text
Unicorn：CPU 指令级模拟
AndroidNativeEmu：Python 生态 Android native 模拟框架
Unidbg：面向 Android JNI / DalvikVM / so 的 Java 生态模拟框架
```

## 路线选择

| 场景 | 优先路线 | 原因 |
| --- | --- | --- |
| 裸 native 函数、依赖少、参数和内存布局明确 | Unicorn | 模拟面最小，可手动布寄存器、内存和 hook 指令 |
| 需要理解 CPU 指令、Capstone/Keystone/Unicorn 关系 | Unicorn 学习/对照 | 适合构造最小样本，不适合直接模拟完整 Android 环境 |
| JNI_OnLoad、DvmObject、Java 对象、AndroidResolver、so 依赖较多 | Unidbg | 默认 Android JNI 离线执行路线 |
| so 会反向调用 Java 或 Android API | Unidbg + `patch-unidbg-environment` | signature-driven 最小补环境 |
| 课程或历史项目已有 AndroidNativeEmu 工程 | AndroidNativeEmu 平行参考 | 可迁移思想，不作为默认路线 |
| Unidbg 补环境变成模拟半个 Android | 路线回退 | 考虑 Frida RPC、自建 Android 宿主 App 或真实 App 内调用 |

## 决策流程

```text
目标是裸函数还是 JNI 方法？
→ 裸函数：先评估 Unicorn 是否足够
→ JNI 方法：默认 Unidbg
是否依赖 JNI_OnLoad / Java / Android API？
→ 是：Unidbg + patch-unidbg-environment
→ 否：Unicorn 或 Unidbg 都可，优先选择成本低、证据清晰者
是否已有 AndroidNativeEmu 现成工程？
→ 有：可作为平行验证，不替代默认路线
补环境是否失控？
→ 是：切换 Frida RPC / Android 宿主 / App 内代发
```

## 看雪查字典入口

优先查看：

- 看雪第7章 课时1-2：Capstone、Unicorn、Keystone 与 Unicorn 上手；
- 看雪第7章 课时3-5：Unicorn 调用 so、JNI 接口和 JNI_OnLoad；
- 看雪第7章 课时6-7：AndroidNativeEmu 调用 JNI 与 Java 交互；
- 看雪第7章 课时8-9：Unidbg 加载 so、模拟 Java 交互；
- workflow 顶层 `../../../references/kanxue-course-directory-index.md`。

采用后回写 workflow 顶层 `../../../references/course-provenance.md`。

## Green 边界

- `route-selected`：已说明选择 Unicorn、AndroidNativeEmu 或 Unidbg 的原因；
- `toolchain-green`：工具链 smoke 可运行；
- `call-green`：目标函数或 JNI 方法可调用；
- `environment-partial`：补环境仅覆盖当前路径；
- `validated`：输出与真机 Hook、原 App、fixture 或端到端请求对齐。

工具能启动不等于目标算法已复现；AndroidNativeEmu 或 Unicorn 平行路线能跑通，也不自动推翻 Unidbg 主路线。
