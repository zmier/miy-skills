# 能力注册表

初始化阶段只有总编排 Skill 处于可用状态。学完并复现对应课程内容后，再逐个创建子 Skills。

课程来源、老师脚本、原始笔记与通用能力之间的详细追溯关系，集中记录在 `../../../references/course-provenance.md`。本表只保留能力摘要、首次来源和验证状态，避免把课程案例过程塞进普通 Skill 主流程。

| 能力 | 计划中的子 Skill | 首次来源 | 状态 | 已验证案例 |
|---|---|---|---|---|
| 终点驱动的逆向 TDD 与 Mermaid 控制面 | `android-request-reproduction` | Day 17-20 实践复盘 | validated | UAT/G1/G2、请求构造树、前置接口 DAG、原始请求预检、三轴路由、证据角色、红灯与 NEXT |
| 课程案例到 workflow 的迁移评估 | `extract-course-case-workflow` | Day15 识货复盘 | experimental | 老师脚本可运行性预检、历史假设识别、integrate-now/case-evidence/defer 分类 |
| Android 实验设备准备 | `prepare-android-device` | Day 17 前置 | validated | Pixel 4 XL、ADB、Root、Magisk |
| Android 流量采集、Reqable 与强制转发 | `capture-android-traffic` | Day 17 前置、Day 26、Day27 网络专题、Day16 | validated | USB/局域网代理、Reqable MCP；SocksDroid/VpnService + mitmproxy SOCKS5；冷启动窗口、`non-target-only` 分层与通道识别交接；SSL/Objection upstream assets 已纳入，待 forward-test |
| Android 业务网络通道识别 | `identify-android-business-network-channel` | Day27 网络专题 | validated | 支付宝小程序/XRiver bridge/RPC/mobilegw：从普通代理非目标流量推进到 operationType、响应回调、网络出口和 R2 路线 |
| 流量与请求形态分析 | `analyze-android-traffic` | Day 17 | validated | click2 候选漏斗、低频重放、UI 观察与目标接口证据卡；来源案例评级 B，迁移需新 App forward-test |
| 目标请求参数归约 | `minimize-android-request` | Day 17 | validated | 二进制正文阻塞定位；来源案例评级 C，完整逐字段归约仍需新 App forward-test |
| 请求构造链静态定位 | `locate-android-request-builder` | Day 17-18 | validated | H7 正文链；Day18 header 注入链与 fp 算法 |
| Java 追踪与运行时取证 | `trace-android-java` | Day 17-18、Day15、Day12 | validated | H7 参数；接口实现；Kotlin `DataKt` 真实符号；OkHttp Interceptor、OkHttpLogger upstream、Map/TreeMap、Base64 探针模板已迁移；crypto-probe 与 OkHttpLogger 迁移状态待 forward-test |
| 动态字段来源与生命周期闭环 | `resolve-android-dynamic-field` | Day 17-20 | validated | DID、BUVID、session_id、fp_local、vcspToken 服务端下发与持久化 |
| 面向混淆代码的分析 | `analyze-android-obfuscation` | Day 17-18、Day 23 | learning | 司小宝 `p0/s0/n1` 双重符号结构已静态核验，未真机 Hook |
| JNI/Native 工具链准备 | `prepare-android-native-toolchain` | Day 13 前置、Day 19 准备 | validated | B站 6.24.0 armeabi-v7a `libbili.so`、IDA 与 LLVM 反汇编 Smoke |
| JNI 注册与映射恢复 | `map-android-jni` | Day 19、图灵 Day23 | validated | 冷启动捕获 `LibBili.s` 动态注册到 `libbili.so+0x1c97`，ARM32 Thumb；图灵 Day23 RegisterNative 映射模板已纳入 assets，补充 `JNINativeMethod` 数组路线与 ART `PrettyMethod + retval` 平行视角 |
| Native 静态分析与路线选择 | `analyze-android-native-static` | Day 19 | validated | IDA batch + MCP、LLVM objdump；Thumb 函数恢复、地址语义、伪代码、xref 与 JNI 返回链 |
| Native 运行时观察 | `hook-android-native` | Day 19-20 | validated | `libbili.so` 分段取证；唯品会 so 延迟加载与 Java/Native Key/IV 双边界 |
| 算法与编码复现 | `reproduce-android-crypto` | Day 17 以后、图灵 Day15 | validated | AES/sign、双 SHA1、IV 前缀封装、原始成功请求预检与 G1/G2 首差分类；支持从 crypto-probe JSONL 筛选候选 fixture 后进入 comparison ladder |
| 环境与动态插桩诊断 | `diagnose-android-instrumentation` | Day 21-23 | learning | Root/模拟器、Frida 特征、ptrace、attach/spawn 故障树已迁移，未真机评测 |
| Frida RPC 导出 | `export-frida-rpc` | Day 21、Day27 网络专题、图灵 Day17 | validated | RPC 类型桥接与生命周期规则；支付宝 SimpleRpcService App 内主动调用、PID fallback、默认简化 JSON 与显式 raw 保存已真机通过；长跑采集时补充真实 TTY/伪终端、session 销毁识别和单实体重试边界；图灵 Day17 JS/Python 模板已纳入 assets，迁移状态待 forward-test |
| 借用 App 运行态代发请求/消息 | `dispatch-via-app-runtime` | Day27 网络专题 TASK29-02/TASK31、图灵 Day17 | validated | R4-A 路线：当 `authorization/Did/Ts/Sign/miniwua` 等运行态字段阻塞 R3 时，使用 App 内统一 RPC/发送入口代发低风险 allowlist 样本，Python 只调度并接响应；TASK31 smoke 已验证 Python 不外发；图灵 Day17 用于说明 Frida RPC 何时停留 R2、何时升级 R4 |
| Xposed/Sekiro 长驻运行态服务化 | `xposed-sekiro-runtime-dispatch` | Day25-Day29 | learning | 新增 R4-X 路线：Xposed/LSPosed 模块命中目标进程，Sekiro action allowlist 暴露 App 内方法/RPC/请求入口；模板与契约已创建，待 forward-test |
| RPC/bridge 响应建模 | `model-android-rpc-response` | Day27 网络专题 | validated | queryQuestionList 响应模型：顶层状态、分页、feedViewItems、question、answerList、敏感字段与工具输出 schema |
| 业务 RPC 接口地图与数据语料库 | `build-android-rpc-data-corpus` | Day27 网络专题探索项目 | experimental | 支付宝“基金经理请回答”：页面接口地图、复合接口、latest questions 1000 窗口、历史专题 7751 去重、经理 publicId 候选扩展、source/evidence、服务端窗口、限速护栏、长跑批量采集的单实体隔离与全局汇总边界 |
| Android 宿主重载 so | `host-android-native-library` | Day 21 | learning | JNI 包名/类名/ABI/依赖可行性规则已迁移，未构建宿主 App |
| 交互式验证关口 | `handle-interactive-verification` | Day 22 | learning | 图片验证码、短信码、人工接力和时效绑定规则已迁移 |
| 运行时 Dex 恢复 | `recover-android-dex` | Day 22、Day18 | learning | 酒仙网壳结构已静态核验；DefineClass Hook upstream dumpdex 资产已纳入，未执行新 App forward-test |
| 脚本化代理流量处理 | `process-android-traffic` | Day 23 | validated | Pixel 4 XL USB reverse、Magisk systemless CA、Chrome HTTPS、B站启动流量与停止恢复 |
| Unidbg 工具链准备 | `prepare-unidbg-toolchain` | Day 24 | validated | JDK8 + `mvnw` + ASCII 工作副本；`SignUtil` smoke 输出稳定 |
| Unidbg 执行 so | `run-so-with-unidbg` | Day 24、图灵 Day24 | validated | DYM `encrypt_data`；ShiHuo `heracles([BII)[B` 离线明文；Java CLI wrapper 模板已纳入 assets，迁移状态待 forward-test |
| Unidbg 补环境 | `patch-unidbg-environment` | Day 25-26 | validated | Vip2 `TreeMap/Set/Iterator/Map.Entry`；ShiHuo `ActivityThread/Application/PackageManager/getPackageName`；PDD `DeviceNative.info2` 复杂 Android/App/Telephony fixture，desktop-only `partial-validated` |
| 结果验证与 CLI/Jar 交付 | `validate-android-reproduction` | Day 26、图灵 Day24 | learning | 已沉淀 Unit/G1/G2/UAT、`partial-validated`、`java -jar` 参数与 Python subprocess 规则；Unidbg subprocess caller 模板已纳入 assets；Jar 打包仍待专门 TASK forward-test |

Unidbg 类 TASK 的创建模板位于 `assets/native-unidbg-task-template.md`。该模板由总编排 Skill 持有，用于把 Native/.so 离线复现拆成工具链 Smoke、JNI 边界、基础执行、最小补环境、结果验证和 Skill 回填；具体 Day 或 App 的 APK、so、fixture、输出值必须保留在对应 TASK 中，不写入通用 Skill。

状态值保持为机器可读英文：

- `planned`：已规划，尚未学习和实现；
- `learning`：正在学习和定义边界；
- `experimental`：已有实现，尚未稳定通过评测；
- `validated`：已通过课堂案例评测；
- `retired`：已停用或被其他能力取代。
