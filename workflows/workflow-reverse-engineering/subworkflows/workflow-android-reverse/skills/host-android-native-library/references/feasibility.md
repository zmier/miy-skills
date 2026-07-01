# so 重载可行性

| 条件 | 影响 |
|---|---|
| 导出 `Java_pkg_Class_method` | 宿主必须提供相同包、类、方法签名 |
| `RegisterNatives` | 必须恢复注册目标类和 `JNI_OnLoad` 前提 |
| 依赖其他 so | 同时提供并注意加载顺序 |
| 依赖 Context/Asset/签名/包名 | 需要最小补环境，可能不适合重载 |
| 自校验原 APK 或进程 | 优先 RPC/Unidbg 或继续分析 |
| ABI 不匹配 | 必须换设备/模拟器 ABI 或取得对应库 |

课程 Day21 的 `libCrypt.so` 属于“接口简单、静态 JNI 声明可重建”的候选类型，但本地 Workflow 尚未实跑。
