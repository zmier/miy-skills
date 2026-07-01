# 课程来源追溯

这个文件专门记录课程案例、老师脚本、原始笔记与 `workflow-android-reverse` 中通用能力之间的来源关系。

## 写作原则

- 普通领域 Skill 的 `SKILL.md` 只写可迁移流程、路线选择、输入输出、完成标准和边界。
- 课程名、Day 编号、老师脚本名、固定 App 名、固定 URL、固定输出值和案例过程，不写入普通 Skill 主流程。
- 课程相关引用信息不能删除，应集中写在这里，方便之后追溯“这个能力最初从哪里来、参考了什么、被清洗成了什么”。
- 通用脚本可以保留 upstream 原件；特定案例脚本只记录来源和 TASK 位置，不进入通用 Skill assets。
- TASK 记录复现过程，能力注册表记录能力摘要，本文件记录来源链路。

## 记录模板

```text
### TASKxx - 能力名

- 课程/案例：
- 来源材料：
- 对应 TASK：
- 影响位置：
- 证据角色：
- 清洗与泛化：
- 当前状态：
- 迁移/回归状态：
```

## 看雪课程资料索引记录

### 看雪安卓课程 - workflow 查字典索引

- 课程/案例：看雪安卓高级研修班（月薪三万计划 2024 春季网课班）。
- 来源材料：`看雪/安卓/README.md`、`看雪/安卓/课程资料迁移清单.json`、`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK02-视频转写必要性评估/outputs/P0转写提炼报告.md`、`P1转写提炼报告.md`、`全课程视频转写复核表.md`，以及原始视频目录 `/Users/narra/Downloads/看雪安卓高级研修班 月薪三万计划(2024春季网课班)`。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK02-视频转写必要性评估`。
- 影响位置：`references/kanxue-course-directory-index.md`；`SKILL.md` 的 `Reference Dictionary`。
- 证据角色：course index / lookup dictionary；不作为当前 APK 的 primary Green 证据。
- 清洗与泛化：只保留两级目录、问题到章节的路由、P0/P1/P2 转写状态和使用纪律；不写入固定案例地址、固定包名、老师结论或视频正文。
- 当前状态：`workflow-reference-integrated`。
- 迁移/回归状态：作为查字典索引可用；具体章节若被用于 Skill 反哺，仍需单独记录 provenance 和 forward-test 状态。

### 看雪安卓课程 - 高级分支查字典路由

- 课程/案例：看雪安卓高级研修班（月薪三万计划 2024 春季网课班）。
- 来源材料：看雪课程两级目录、P0/P1 转写提炼报告、`全课程视频转写复核表.md`。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK02-视频转写必要性评估`。
- 影响位置：
  - `recover-android-dex/references/aosp-art-fart-routes.md`
  - `diagnose-android-instrumentation/references/frida-svc-syscall-ladder.md`
  - `hook-android-native/references/native-trace-ollvm.md`
  - `map-android-jni/references/jni-address-anti-trace.md`
  - 上述子 Skill 的 `SKILL.md` 与相关 route/reference 入口。
- 证据角色：course lookup / route design；只说明遇到某类高级红灯时应去哪里查资料，不作为当前 APK 的 primary Green 证据。
- 清洗与泛化：把看雪课程章节映射为可迁移红灯：AOSP/ART/FART、Frida 特征检测与 SVC/syscall、OLLVM/Native Trace、JNI 地址绑定与防追踪；不写入固定案例地址、固定包名、老师脚本输出或具体样本结论。
- 当前状态：`branch-reference-integrated / structural-green`。
- 迁移/回归状态：`forward-test-pending`；后续若某分支在新案例中实际使用，需要在对应 TASK 中记录实验和 Green。

## 图灵课程反哺记录

### TASK09 - Day15 算法自吐模板化

- 课程/案例：图灵 Android 逆向训练营 Day15，算法助手/算法自吐。
- 来源材料：`图灵/课堂笔记与代码/Day15-算法助手开发/code/day15/3-hook-算法v1.js`。
- 对应 TASK：`图灵/PROJECT-图灵课程反哺AndroidWorkflow/tasks/TASK09-Day15算法自吐模板化`。
- 影响位置：`trace-android-java/assets/frida-crypto-probe.js`；`trace-android-java/assets/crypto-probe-config-template.json`；`reproduce-android-crypto/references/crypto-probe-fixtures.md`。
- 证据角色：source asset / confirmatory；本次独立性为 `prior-exposed`，教师脚本不能作为 primary 证据。
- 清洗与泛化：去掉固定包名、固定类名、固定输出和个案判断，改为可配置 crypto probe、JSONL 事件 schema、脱敏与候选 fixture 筛选规则。
- 当前状态：`workflow-integrated`。
- 迁移/回归状态：模板已落入 workflow，待新 App forward-test。

### TASK10 - Day17 Frida RPC 模板化

- 课程/案例：图灵 Android 逆向训练营 Day17，Frida RPC 主动调用。
- 来源材料：`图灵/课堂笔记与代码/Day17-frida rpc自主调用/code/day17/01-rpc.js`；`图灵/课堂笔记与代码/Day17-frida rpc自主调用/code/day17/02-rpc调用.py`。
- 对应 TASK：`图灵/PROJECT-图灵课程反哺AndroidWorkflow/tasks/TASK10-Day17FridaRPC模板化`。
- 影响位置：`export-frida-rpc/assets/rpc-agent-template.js`；`export-frida-rpc/assets/rpc-client-template.py`；`export-frida-rpc/SKILL.md`；`dispatch-via-app-runtime/SKILL.md`。
- 证据角色：source asset / route comparison。
- 清洗与泛化：把课堂脚本抽象为 App 运行态主动调用模板，区分 R2 函数级 RPC 与 R4 App 内代发；Flask 包装只作为可选交付形态，不进入默认主流程。
- 当前状态：`workflow-integrated / template-green`。
- 迁移/回归状态：模板语法和结构已通过静态检查，待真实新案例 forward-test。

### TASK11 - Day23 RegisterNative 动态注册映射

- 课程/案例：图灵 Android 逆向训练营 Day23，RegisterNative 动态注册映射。
- 来源材料：`图灵/课堂笔记与代码/Day23-unidbg 案例实战/code/day23/hook_soname.js`。
- 对应 TASK：`图灵/PROJECT-图灵课程反哺AndroidWorkflow/tasks/TASK11-Day23RegisterNative动态注册映射`。
- 影响位置：`map-android-jni/assets/register-native-map.js`；`map-android-jni/references/register-native-parallel-routes.md`；`map-android-jni/SKILL.md`。
- 证据角色：parallel / confirmatory。
- 清洗与泛化：workflow 原本已有 `JNINativeMethod` 数组路线；课程脚本补充 ART `PrettyMethod + retval` 视角，作为平行路线、降级路线和交叉验证路线。
- 当前状态：`workflow-integrated / template-green`。
- 迁移/回归状态：待新 App 冷启动 forward-test。

### TASK12 - Day24 Unidbg Wrapper 与 Python Caller

- 课程/案例：图灵 Android 逆向训练营 Day24，Unidbg 打包、部署与 Python 调用。
- 来源材料：`图灵/课堂笔记与代码/Day24-unidbg 打包和部署/code/dc/*/*.java`；`图灵/课堂笔记与代码/Day24-unidbg 打包和部署/code/dc/zhxs/demo.py`。
- 对应 TASK：`图灵/PROJECT-图灵课程反哺AndroidWorkflow/tasks/TASK12-Day24UnidbgWrapperPythonCaller`。
- 影响位置：`run-so-with-unidbg/assets/UnidbgCliWrapperTemplate.java`；`validate-android-reproduction/assets/unidbg_subprocess_client.py`；`prepare-unidbg-toolchain/SKILL.md`；`patch-unidbg-environment/SKILL.md`；`host-android-native-library/SKILL.md`。
- 证据角色：source asset / delivery-shape。
- 清洗与泛化：Java wrapper 抽象为命令行入口模板；Python 样例抽象为 subprocess caller；真实业务请求、固定参数、固定路径和输出值不进入通用 Skill。
- 当前状态：`workflow-integrated / template-green`。
- 迁移/回归状态：Python 模板已通过 `py_compile`；Java 模板依赖 TASK-local Unidbg classpath，待后续案例编译验证。

### TASK13 - Day12 OkHttpLogger 原样纳入

- 课程/案例：图灵 Android 逆向训练营 Day12，OkHttpLogger-Frida。
- 来源材料：`图灵/课堂笔记与代码/Day12-frida hook java方法/code/OkHttpLogger-Frida-master/`；`图灵/课堂笔记与代码/Day12-frida hook java方法/notes/OkHttpLogger-Frida-master/README.md`。
- 对应 TASK：`图灵/PROJECT-图灵课程反哺AndroidWorkflow/tasks/TASK13-Day12OkHttpLogger原样纳入`。
- 影响位置：`trace-android-java/assets/upstream-okhttplogger-frida/`；`trace-android-java/SKILL.md`；`trace-android-java/references/request-boundary-probes.md`。
- 证据角色：upstream source asset。
- 清洗与泛化：本次按“通用脚本可保留 upstream 原件”的规则保留原始脚本，不改写实现；workflow 主流程只记录使用位置、风险边界和 TASK 交接规则。若后续提供 optimized 版本，应与 upstream 原件并存。
- 当前状态：`workflow-integrated / upstream-copied`。
- 迁移/回归状态：已复制上游脚本与 README；尚未在新 App forward-test。

### TASK14 - Day16 SSL/Objection 抓包对抗

- 课程/案例：图灵 Android 逆向训练营 Day16，Objection 使用和抓包对抗。
- 来源材料：`图灵/课堂笔记与代码/Day16-Objection使用和抓包对抗/code/byssl.js`；`key-strore.js`；`ssluningping.js`；`newhunan.py`；`notes/笔记.md`。
- 对应 TASK：`图灵/PROJECT-图灵课程反哺AndroidWorkflow/tasks/TASK14-Day16SSLObjection抓包对抗模板`。
- 影响位置：`capture-android-traffic/assets/upstream-ssl-objection/`；`capture-android-traffic/SKILL.md`；`capture-android-traffic/references/https-mitm-diagnosis.md`；`diagnose-android-instrumentation/SKILL.md`。
- 证据角色：upstream source asset / route enhancement。
- 清洗与泛化：`byssl.js` 与 `key-strore.js` 作为通用 upstream 保留；`ssluningping.js` 以 aggressive reference 保存；`newhunan.py` 判定为特定案例请求脚本，不进入通用 assets。
- 当前状态：`workflow-integrated / upstream-copied`。
- 迁移/回归状态：已复制 upstream 脚本与 README；尚未在新 App forward-test。

### 看雪第5章 - OLLVM 分支参考路由

- 课程/案例：看雪安卓高级研修班第5章，彻底搞懂 OLLVM。
- 来源材料：看雪课程目录与 P1 转写提炼；重点课时包括课时1-3 LLVM/Pass/OLLVM 基础，课时4 控制流程平坦化，课时5 虚假控制流，课时6 指令替换，课时7 字符串加密，课时8 NDK 中使用 OLLVM，课时9-10 逆向 OLLVM 算法的通用/非通用方法。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK06-第5章OLLVM分支路由评估`。
- 影响位置：`hook-android-native/references/native-trace-ollvm.md`；既有 `analyze-android-native-static/SKILL.md` 的 OLLVM 交接规则。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - 课时1-3 只作为理解 OLLVM 生成物和 Pass 表现的背景入口，不进入默认 workflow；
  - 课时4-7 抽象为 OLLVM 分型红灯：控制流平坦化、虚假控制流、指令替换、字符串加密；
  - 课时8 只作为构造最小 OLLVM 对照样本的弱触发入口；
  - 课时9-10 用于区分通用 trace/oracle 方法与非通用专项 TASK；
  - 不写入课程固定地址、样本输出或老师结论。
- 双价值四象限复评：
  - 课时1-3：Codex 执行价值中、用户学习价值高，不进入默认 workflow；
  - 课时4：Codex 执行价值高、用户学习价值高，进入控制流平坦化分型与 trace 升级规则；
  - 课时5-6：Codex 执行价值中高、用户学习价值高，进入虚假控制流和指令替换的证据收束规则；
  - 课时7：Codex 执行价值高、用户学习价值高，进入字符串加密动态观测规则；
  - 课时8：Codex 执行价值中、用户学习价值中高，作为对照样本弱触发；
  - 课时9-10：Codex 执行价值高/中高、用户学习价值高，进入通用方法与专项路线边界。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 OLLVM 样本 forward-test；当前仅作为疑难红灯的课程参考入口。

### 看雪第6章 - VMP 分支参考路由

- 课程/案例：看雪安卓高级研修班第6章，高级调试之 VMP。
- 来源材料：看雪课程目录；重点课时包括课时1 VMP 初识，课时2-3 VMP 保护函数快速逆向，课时4-5 ADVMP 源码分析和样本构造，课时6 定制 ART 绕过反调试，课时7-9 Hyperpwn、内存断点和 VMP 映射。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK07-第6章VMP分支路由评估`。
- 影响位置：`hook-android-native/SKILL.md`；`hook-android-native/references/vmp-protected-function.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - 把第6章抽象为 VMP 红灯识别和路线升级规则；
  - 不把 Hyperpwn、硬件断点、定制 ART 写成默认步骤；
  - 不承诺自动去虚拟化，只定义 `suspected-vmp`、`oracle-green`、`mapping-partial`、`mapping-green` 等证据边界；
  - 课程中的固定样本、工具界面、地址和老师结论不作为当前 TASK 证据。
- 双价值四象限复评：
  - 课时1：Codex 执行价值中高、用户学习价值高，进入 VMP 与壳/OLLVM 的边界判断；
  - 课时2-3：Codex 执行价值高、用户学习价值高，进入 VMP 快速逆向和 oracle/mapping 路线；
  - 课时4-5：Codex 执行价值中、用户学习价值高，只作 VM 模型和对照样本参考；
  - 课时6：Codex 执行价值中高、用户学习价值高，作为反调试高侵入路线远期参考；
  - 课时7-9：Codex 执行价值中到高、用户学习价值中高到高，作为 Hyperpwn/内存断点/VMP 映射高阶参考。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 VMP 样本 forward-test；当前仅作为分支参考路由，暂不升级为独立 Skill。

### 看雪第7章 - Unicorn / Unidbg 离线执行路线参考

- 课程/案例：看雪安卓高级研修班第7章，unicornunidbg。
- 来源材料：看雪课程目录；重点课时包括课时1-2 Capstone/Unicorn/Keystone 与 Unicorn 上手，课时3-5 Unicorn 调用 so、JNI 和 JNI_OnLoad，课时6-7 AndroidNativeEmu 调用 JNI 与 Java 交互，课时8-9 Unidbg 加载 so 和模拟 Java 交互。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK08-第7章UnicornUnidbg分支路由评估`。
- 影响位置：`prepare-unidbg-toolchain/SKILL.md`；`prepare-unidbg-toolchain/references/emulation-route-selection.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - 把第7章抽象为 Unicorn、AndroidNativeEmu、Unidbg 的路线选择边界；
  - 不把课程固定工程、固定 so、固定输出写入通用 Skill；
  - Unidbg 仍是默认 JNI/Android so 离线执行路线；
  - Unicorn 作为裸函数或低层 CPU 模拟平行路线；
  - AndroidNativeEmu 作为平行/历史参考，不进入默认 workflow。
- 双价值四象限复评：
  - 课时1-2：Codex 执行价值中高、用户学习价值高，进入路线选择 reference；
  - 课时3：Codex 执行价值高、用户学习价值高，作为裸 native 函数低层路线；
  - 课时4-5：Codex 执行价值中高、用户学习价值高，作为 JNI 初始化复杂度背景；
  - 课时6-7：Codex 执行价值中、用户学习价值中高/高，作为 AndroidNativeEmu 平行参考；
  - 课时8-9：Codex 执行价值高、用户学习价值高，已由 Unidbg 执行和补环境 Skills 承接。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待新的 so/JNI 离线执行案例 forward-test；当前仅作为路线选择参考。

### 看雪第8章 - 非标准算法还原上分支参考

- 课程/案例：看雪安卓高级研修班第8章，非标准算法还原（上）。
- 来源材料：看雪课程目录；重点课时包括课时1 常用算法简介，课时2-3 Base64/CRC32/MD5，课时4-5 OLLVM_MD5/OLLVM_SHA1，课时6 HMAC，课时7-9 OLLVM_Base64、OLLVM_RC4、Frida Stalker OLLVM AES。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK09-第8章非标准算法上分支路由评估`。
- 影响位置：`reproduce-android-crypto/SKILL.md`；`reproduce-android-crypto/references/nonstandard-native-crypto.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - 标准算法案例抽象为 comparison ladder 内可复现路径；
  - OLLVM/魔改算法案例抽象为 native oracle 回退条件；
  - 不写入课程固定输入、固定 key、固定输出或老师结论；
  - 与 `hook-android-native/references/native-trace-ollvm.md` 形成交接。
- 双价值四象限复评：
  - 课时1：Codex 执行价值中、用户学习价值高，作为算法识别背景；
  - 课时2-3：Codex 执行价值高、用户学习价值高，进入标准算法复现路径；
  - 课时4-5：Codex 执行价值高、用户学习价值高，进入 OLLVM 摘要算法分流；
  - 课时6：Codex 执行价值高、用户学习价值高，进入 HMAC key/message/encoding 边界；
  - 课时7-9：Codex 执行价值高、用户学习价值高，进入动态表、RC4、Stalker OLLVM AES 的 native oracle 路线。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实非标准/native 魔改算法样本 forward-test。

### 看雪第9章 - 非标准算法还原下分支参考

- 课程/案例：看雪安卓高级研修班第9章，非标准算法还原（下）。
- 来源材料：看雪课程目录；重点课时包括课时1-2 OpenSSL 特征与手动编译，课时3 动态编码表，课时4-5 MD5/SHA1 加盐、更改常量及 OLLVM，课时6 魔改 OLLVM HMAC-MD5，课时7 BPO 插件，课时8 Frida 辅助 Android SO 算法还原和自动化黑盒调用。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK10-第9章非标准算法下分支路由评估`。
- 影响位置：`reproduce-android-crypto/references/nonstandard-native-crypto.md`；间接关联 `export-frida-rpc/SKILL.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - OpenSSL 特征只作为候选，不作为算法完成证据；
  - 动态编码表、salt、魔改常量和 OLLVM 组合算法被抽象为 native oracle 证据需求；
  - BPO/插件型路线只作为平行解释工具；
  - Frida 黑盒调用抽象为 R2/RPC，不能写成 R3 纯外部复现；
  - 不写入课程固定样本、固定表、固定 key 或老师结论。
- 双价值四象限复评：
  - 课时1-2：Codex 执行价值中高、用户学习价值高，进入 OpenSSL 特征候选规则；
  - 课时3：Codex 执行价值高、用户学习价值高，进入动态表证据规则；
  - 课时4-6：Codex 执行价值高、用户学习价值高，进入 salt/常量/OLLVM 组合算法 oracle-first 路线；
  - 课时7：Codex 执行价值中高、用户学习价值中高，作为插件型平行路径；
  - 课时8：Codex 执行价值高、用户学习价值高，作为 Frida RPC 黑盒调用边界。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 OpenSSL 特征、动态表、魔改摘要或 R2 黑盒调用样本 forward-test。

### 看雪第10章 - Frida_Fart 脱壳去重补强

- 课程/案例：看雪安卓高级研修班第10章，Frida_Fart脱壳。
- 来源材料：看雪课程目录；重点课时包括课时1-9 FART 主线，课时10-11 fdex2 与高版本实现，课时12 FART 与定制 JADX，课时13-14 Stalker/ART 解释器 trace，课时15 JNI 地址绑定与定制 JADX，课时16-17 Frida 检测与 OLLVM 反 Frida。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK11-第10章FridaFart脱壳分支路由评估`。
- 影响位置：`recover-android-dex/references/aosp-art-fart-routes.md`；间接关联 `map-android-jni`、`diagnose-android-instrumentation`、`hook-android-native/references/native-trace-ollvm.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - 与第2章 FART 主线、第4章 ART 定制、第13章反检测去重；
  - fdex2、高版本适配、定制 JADX、ART 解释器 trace 被抽象为 Dex 恢复高侵入路线的组合红灯；
  - JNI 地址绑定和 Frida 检测只路由到已有分支，不重复写入 Dex 恢复主流程；
  - 不写入课程固定脚本、样本 dex、地址或老师结论。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 FART/fdex2/定制 JADX 或 ART trace 样本 forward-test。

### 看雪第11章 - eBPF 高级观测参考

- 课程/案例：看雪安卓高级研修班第11章，eBPF环境搭建与热门项目源码赏析。
- 来源材料：看雪课程目录；课时1 Android 上 eBPF 现状，课时2 eBPF 手机开发环境搭建，课时3 eBPF 项目源码原理解析。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK12-第11章eBPF分支路由评估`。
- 影响位置：`diagnose-android-instrumentation/references/kernel-ebpf-observability.md`；`diagnose-android-instrumentation/references/frida-svc-syscall-ladder.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - eBPF 被定位为系统事件观测能力，不是默认 Hook、绕过或算法复现路线；
  - 只保留升级门槛、设备授权、可回滚、事件 schema 和证据边界；
  - 不写入课程固定内核版本、设备、项目输出或老师结论。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 kernel/eBPF 观测样本 forward-test。

### 看雪第12章 - FART10_12 版本迁移参考

- 课程/案例：看雪安卓高级研修班第12章，Fart10_12。
- 来源材料：看雪课程目录；课时1 实战 FART10 源码移植与脱壳实战。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK13-第12章Fart10_12分支路由评估`。
- 影响位置：`recover-android-dex/references/aosp-art-fart-routes.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - FART10/FART10_12 被定位为 FART 路线族的源码移植和版本适配参考；
  - 编译、刷机、样例运行只算 environment/toolchain Green；
  - 目标 dex/code item/repaired dex 可用才算 Dex 恢复 Green；
  - 不写入课程固定源码路径、设备、补丁或输出。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 FART10/FART10_12 迁移样本 forward-test。

### 看雪第13章 - SVC 与 JNI 地址防追踪参考

- 课程/案例：看雪安卓高级研修班第13章，内核模块绕过Frida检测。
- 来源材料：看雪课程目录；课时1-3 SVC/syscall，课时4 内存动态释放代码，课时5 JNI 地址防追踪，课时6 硬件断点分析 JNI 地址防追踪。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK14-第13章内核模块绕过Frida检测分支路由评估`。
- 影响位置：`diagnose-android-instrumentation/references/frida-svc-syscall-ladder.md`；`map-android-jni/references/jni-address-anti-trace.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - SVC/syscall 作为用户态 Hook 失效后的定位路线；
  - 内存动态释放代码抽象为短生命周期代码窗口；
  - JNI 地址防追踪抽象为绑定时机、跳板/主体、地址类型和执行证明；
  - 硬件断点只作为高侵入确认手段；
  - 不写入课程固定地址、断点、设备或老师结论。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 SVC、短生命周期代码或 JNI 地址防追踪样本 forward-test。

### 看雪第14章 - iOS 章节边界与 Cronet 弱参考

- 课程/案例：看雪安卓高级研修班第14章，iOS设备指纹开发与逆向。
- 来源材料：看雪课程目录；课时1 iOS 逆向指南，课时2 ObjC/Frida，课时3-4 iOS 反调试，课时5-6 OLLVM obfuscated libsscronet.so SSL pinning bypass。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK15-第14章iOS章节边界评估`。
- 影响位置：`capture-android-traffic/references/https-mitm-diagnosis.md`。
- 证据角色：boundary note / future workflow seed。
- 清洗与泛化：
  - iOS 逆向、ObjC Hook、iOS 反调试不进入 Android workflow；
  - libsscronet/SSL pinning 只作为 Android Cronet/native TLS 方法论弱参考；
  - Android 当前样本必须重新建立模块、符号、调用链和证据；
  - 本章可作为 future iOS workflow 的独立素材。
- 当前状态：`boundary-recorded / structural-green`。
- 迁移/回归状态：`not-applicable-to-android / future-ios-workflow-seed`。

### 看雪第1章 - Frida 高级逆向分支参考路由

- 课程/案例：看雪安卓高级研修班第1章，Frida高级逆向。
- 来源材料：看雪课程目录与 P0/P1 转写提炼；重点课时包括课时1-4 Java Hook、课时5-6 Native Hook、课时7-12 Frida 辅助 OLLVM、课时13-16 IDA Trace / Stalker。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow` 的课程目录映射与分支路由审计。
- 影响位置：`trace-android-java/references/runtime-symbols-and-stack.md`；`hook-android-native/references/minimal-hook.md`；`hook-android-native/references/native-trace-ollvm.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - 课时1-4 只作为 Java Hook 基础补课入口，未写入 `trace-android-java` 主流程；
  - 课时5-6 只作为 Native Hook 基础补课入口，未改变 `hook-android-native` 的最小 Hook 纪律；
  - 课时7-16 已由 `native-trace-ollvm.md` 承接为 OLLVM、IDA Trace、Stalker 的高级红灯参考；
  - 课程中的固定脚本、地址、样本输出和老师结论不作为当前 TASK 证据。
- 双价值四象限复评：
  - 课时1-4：Codex 执行价值中低、用户学习价值高，保留为弱触发补课入口；
  - 课时5-6：Codex 执行价值中、用户学习价值高，保留为 Native Hook 基础卡点补课入口；
  - 课时7-12：Codex 执行价值高、用户学习价值高，进入 OLLVM 动态辅助分析分支；
  - 课时13-16：Codex 执行价值高、用户学习价值高，进入 IDA Trace / Stalker 高级取证分支。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 Java Hook 卡点、Native Hook 卡点或 OLLVM/Trace 样本 forward-test；当前仅作为分支参考路由。

### 看雪第2章 - Frida_FART 全自动脱壳分支参考路由

- 课程/案例：看雪安卓高级研修班第2章，Frida_FART全自动脱壳机。
- 来源材料：看雪课程目录；重点课时包括课时1-3 动态加载、ClassLoader、壳识别，课时4-5 ART dex 加载和类加载，课时6-8 FART 框架、主动调用和 Frida 增强，课时9 FART 修复和辅助 VMP 还原。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow` 的课程目录映射与双价值四象限复评。
- 影响位置：`recover-android-dex/references/route-selection.md`；`recover-android-dex/references/aosp-art-fart-routes.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - 课时1-5 进入 Dex 恢复路线选择层，用于壳证据、ClassLoader 替换、ART dex 加载时机和 DefineClass Hook 路线判断；
  - 课时6-9 进入 AOSP/ART/FART 高级路线，用于主动调用、code item 修复、repaired dex 和强壳/VMP 辅助还原；
  - 课程中的固定脚本、地址、样本输出和老师结论不作为当前 TASK 证据；
  - 看雪第2章与第10章、第12章构成 FART 路线族：第2章偏完整主线入门，第10章偏扩展强化，第12章偏 FART10_12 移植实战。
- 双价值四象限复评：
  - 课时1-3：Codex 执行价值中高、用户学习价值高，进入 `route-selection.md`；
  - 课时4-5：Codex 执行价值高、用户学习价值高，进入 `route-selection.md`；
  - 课时6-8：Codex 执行价值高、用户学习价值高，进入 `aosp-art-fart-routes.md`；
  - 课时9：Codex 执行价值中高、用户学习价值高，作为强壳/VMP 场景触发的高级参考。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实加壳、函数抽取壳、code item 缺失或 FART 修复样本 forward-test；当前仅作为分支参考路由。

### 看雪第3章 - ARM/C/C++ 静态语义分支参考路由

- 课程/案例：看雪安卓高级研修班第3章，ARM_C++算法还原原理_Frida。
- 来源材料：看雪课程目录；重点课时包括课时3-8 ARM/Thumb/AArch64 指令集，课时9-12 C 逆向语义，课时13-16 C++ 对象、虚表、继承、RTTI 和异常，课时17 内联汇编与 syscall。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow` 的课程目录映射与双价值四象限复评。
- 影响位置：`analyze-android-native-static/SKILL.md`；`analyze-android-native-static/references/cxx-object-semantics.md`；已有 `diagnose-android-instrumentation/references/frida-svc-syscall-ladder.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - 课时1-12 主要作为 native 静态阅读基础和用户学习参考，不进入默认 workflow；
  - 课时13-16 抽象为 C++ 对象语义卡点：vtable、`this` 指针、多层间接调用、RTTI、构造/析构和异常痕迹会影响 Hook 点和调用关系判断；
  - 课时17 已由 SVC/syscall 分支承接，不重复写入；
  - 课程中的固定样本、地址、老师结论不作为当前 TASK 证据。
- 双价值四象限复评：
  - 课时1-2：Codex 执行价值中低、用户学习价值中高，不补进分支 Skill；
  - 课时3-8：Codex 执行价值中、用户学习价值高，现有地址语义和 Thumb 恢复规则已覆盖执行面；
  - 课时9-12：Codex 执行价值中、用户学习价值高，只作 C 伪代码阅读参考；
  - 课时13-16：Codex 执行价值中高、用户学习价值高，进入 C++ 对象语义卡点 reference；
  - 课时17：Codex 执行价值高、用户学习价值高，已由 SVC/syscall reference 承接；
  - 课时18：Codex 执行价值低中、用户学习价值中，作为构造最小 native/汇编对照样本的弱参考。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 C++ native 对象派发、vtable/RTTI、异常路径或 syscall 样本 forward-test；当前仅作为分支参考路由。

### 看雪第4章 - ART 动态分析沙箱分支参考路由

- 课程/案例：看雪安卓高级研修班第4章，C++11_art打造动态分析沙箱。
- 来源材料：看雪课程目录；重点课时包括课时1-4 C++11/模板/lambda 作为 ART 源码阅读前置，课时5-6 ART C++ 对象内存布局，课时7 ART 函数 inline，课时8 ART 定制方案比较和流程，课时9 ART 定制跟踪 JNI 函数绑定。
- 对应 TASK：`看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow` 的课程目录映射与双价值四象限复评。
- 影响位置：`recover-android-dex/references/aosp-art-fart-routes.md`；`map-android-jni/references/register-native-parallel-routes.md`。
- 证据角色：course-directory route / branch-reference enhancement。
- 清洗与泛化：
  - 课时1-4 主要作为阅读 ART 源码的背景学习，不进入默认 workflow；
  - 课时5-8 进入 AOSP/ART/FART 高侵入恢复路线，用于 ART 对象字段、inline、hook 点失效、版本差异和定制 Runtime 方案选择；
  - 课时9 进入 JNI 映射平行路线，用于 ART `PrettyMethod + retval` 或定制 Runtime 观察最终 JNI 绑定关系；
  - 课程中的固定源码版本、符号地址、构建环境和老师结论不作为当前 TASK 证据。
- 双价值四象限复评：
  - 课时1-4：Codex 执行价值中低、用户学习价值中高，不进入默认 workflow；
  - 课时5-6：Codex 执行价值高、用户学习价值高，进入 ART 对象布局和读值稳定性参考；
  - 课时7：Codex 执行价值中高、用户学习价值高，进入 ART inline/hook 点失效参考；
  - 课时8：Codex 执行价值高、用户学习价值高，进入高侵入路线升级门槛和方案选择；
  - 课时9：Codex 执行价值高、用户学习价值高，进入 ART 定制跟踪 JNI 绑定参考。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：待真实 ART hook 点失效、AOSP/ART 定制、PrettyMethod/retval 或 JNI 绑定追踪样本 forward-test；当前仅作为分支参考路由。

### TASK15 - Day18 Dex 恢复路线与 dumpdex

- 课程/案例：图灵 Android 逆向训练营 Day18，Frida Hook so / dumpdex；并对齐既有路飞 Day22 Dex 恢复路线。
- 来源材料：`图灵/课堂笔记与代码/Day18-frida hook so文件/code/dumpdex.js`；`myfridadump.js`；`search.js`；个案脚本与日志作为 TASK 证据。
- 对应 TASK：`图灵/PROJECT-图灵课程反哺AndroidWorkflow/tasks/TASK15-Dex恢复路线与Dumpdex模板`。
- 影响位置：`recover-android-dex/assets/upstream-dex-dump/`；`recover-android-dex/SKILL.md`；`recover-android-dex/references/route-selection.md`。
- 证据角色：upstream source asset / route enhancement。
- 清洗与泛化：`dumpdex.js`、`myfridadump.js`、`search.js` 作为通用 ART DefineClass Hook upstream 保留；个案业务 Hook、Python 请求脚本和登录参数日志不进入通用 assets。
- 当前状态：`workflow-integrated / upstream-copied`。
- 迁移/回归状态：已复制 upstream 脚本与 README；尚未在新 App forward-test。

### TASK16 - Day25-Day29 Xposed/Sekiro 新 Skill

- 课程/案例：图灵 Android 逆向训练营 Day25-Day29，Xposed API 与 Sekiro RPC。
- 来源材料：`图灵/课堂笔记与代码/Day29-xposed rpc相关技能使用/code/java/com/example/luov2/hookRpc.java`；`handler/*.java`；Day25/Day28 Xposed 示例。
- 对应 TASK：`图灵/PROJECT-图灵课程反哺AndroidWorkflow/tasks/TASK16-XposedSekiro新Skill`。
- 影响位置：`xposed-sekiro-runtime-dispatch/`；`dispatch-via-app-runtime/SKILL.md`；能力注册表。
- 证据角色：new skill / upstream source asset / route enhancement。
- 清洗与泛化：upstream 代码保留在 `assets/upstream-xposed-sekiro/`；通用模板去掉固定 server IP、group、action、业务类名和包名；用契约文件承载 R4-X 状态与 UAT。
- 当前状态：`workflow-integrated / new-skill-valid`。
- 迁移/回归状态：Skill quick_validate 通过；尚未在真实 Xposed/Sekiro 环境 forward-test。

### TASK27-12 - DID/APDID 设备态字段束与 1006/1009 归因

- 课程/案例：网络与抓包专题，授权靶场中的 RPC 采集、设备态风控与字段束实验。
- 来源材料：`PROJECT-Android目标业务网络通道识别/tasks/TASK27-回答详情请求池与采集调度/subtasks/TASK27-12-设备态风控字段实验`；真实实验日志、只读 Hook 证据和状态码对照。
- 影响位置：`resolve-android-dynamic-field/references/device-state-bundle.md`；`resolve-android-dynamic-field/SKILL.md`；`android-request-reproduction/references/routing.md`；`android-request-reproduction/references/g2-rejection-taxonomy.md`。
- 证据角色：field-tested workflow feedback / device-state bundle reference。
- 清洗与泛化：
  - DID/UTDID 链路抽象为“稳定根标识读取链”，不保存真实设备 ID；
  - APDID/apdidToken/umidToken/devKeySet 抽象为“安全 SDK 设备画像与本地存储字段束”，只保留长度、hash、类名层级和绑定关系；
  - 将单字段替换后出现 `1006` 归纳为“字段束一致性被破坏”的证据，不把它写成可绕过方案；
  - 将 `1009` 归纳为账号态、设备态、频率窗口、权限或上下文拒绝，采集路线优先 R2/R4 App 运行态与窗口限速；
  - 通用 workflow 不记录原始 token、Cookie、真实账号、真实设备标识或可复用敏感值。
- 当前状态：`workflow-integrated / field-tested-in-authorized-lab`。
- 迁移/回归状态：已写入设备态字段束 reference；后续遇到 DID/APDID/miniwua/authorization/Sign 绑定或 `1006/1009` 切换时 forward-test。

### TASK27-15 - 设备态根换代解除 1009

- 课程/案例：网络与抓包专题，授权靶场中的 Answer Detail RPC 长跑采集、设备态限制与恢复实验。
- 来源材料：`PROJECT-Android目标业务网络通道识别/tasks/TASK27-回答详情请求池与采集调度/subtasks/TASK27-15-设备态受控爆破最小换代`；真实 Big-Knife dry-run/destructive run、字段束 before/after、同 answerId 业务 smoke 与 miku 调度日志。
- 影响位置：`resolve-android-dynamic-field/references/device-state-bundle.md`；`dispatch-via-app-runtime/SKILL.md`；miku `--clear-1009-cooldown` 本地调度恢复语义。
- 证据角色：field-tested workflow feedback / destructive reset as reinstall-substitute in authorized lab。
- 清洗与泛化：
  - 将“完整重装 App 解除 1009”抽象为“设备态字段束换代后服务端重新接受请求”；
  - 将 Big-Knife 抽象为“授权靶场下的设备态根换代实验”，而不是通用绕过方案；
  - Green 标准必须包含业务 smoke：同一业务样本从 `1009` 回到 success，且未使用后置字段 override；
  - 通用 workflow 只保留 DID/UTDID/APDID/token bundle 层级、before/after hash/长度/变化关系和证据路径，不保留真实 token、Cookie、设备 ID 或完整删除清单。
- 当前状态：`workflow-integrated / field-tested-in-authorized-lab / destructive-authorized-only`。
- 迁移/回归状态：后续遇到设备态限制时，先走只读归因和 R2/R4 App 运行态；只有授权、可恢复、已有重装 Green 对照时，才考虑设备态根换代任务。
