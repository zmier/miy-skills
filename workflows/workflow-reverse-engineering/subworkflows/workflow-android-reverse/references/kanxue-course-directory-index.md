# 看雪安卓课程资料索引

## 用途

这是 `workflow-android-reverse` 的“查字典层”，用于在 workflow 遇到难解红灯时，快速判断看雪课程资料中可能对应哪一章、哪一节。

它不是主流程，也不是完成证据：

- 主流程仍以当前 TASK 的 Red、实验、Green 和证据为准；
- 看雪课程目录只用于路由、补课、寻找脚本/样本/讲解语境；
- 课程中的固定地址、固定包名、固定输出和老师结论不能直接作为当前案例证据；
- 若某节课被实际用于反哺 Skill，需要在 `course-provenance.md` 记录来源链。

## 资料位置

- 归档后的课程目录：`/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/看雪/安卓`
- 课程反哺项目：`/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/course-notes/看雪/安卓/PROJECT-看雪课程反哺AndroidWorkflow`
- 原始视频资料：`/Users/narra/Downloads/看雪安卓高级研修班 月薪三万计划(2024春季网课班)`
- P0/P1 转写提炼：
  - `PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK02-视频转写必要性评估/outputs/P0转写提炼报告.md`
  - `PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK02-视频转写必要性评估/outputs/P1转写提炼报告.md`
  - `PROJECT-看雪课程反哺AndroidWorkflow/tasks/TASK02-视频转写必要性评估/outputs/全课程视频转写复核表.md`

## 按问题查资料

| 当前 workflow 红灯 | 先查课程位置 | 用法 |
| --- | --- | --- |
| Java/Native Hook 基础不熟 | 第1章 Frida高级逆向 课时1-6 | 只作基础补课，workflow 已有 Hook 子 Skill |
| OLLVM 后伪代码不可读 | 第1章 课时7-12；第5章 课时9-10；第8-9章 OLLVM 算法案例 | 优先看 P1 课时9；具体混淆类型再补对应课时 |
| 需要 IDA Trace / Stalker 还原 native 算法 | 第1章 课时13-16；第8章 课时9；第9章 课时8 | 对应 `hook-android-native` / `analyze-android-native-static` 高级分支 |
| ARM/C/C++ 语义卡住 | 第3章 ARM/C++算法还原原理 | 作为基础补课，不默认进入 Skill 主流程 |
| ART、ClassLoader、动态加载、加壳流程不清 | 第10章 课时1-5；第4章 ART相关课时 | 对应 `recover-android-dex` 的 ClassLoader/FART 分支 |
| frida-dexdump 不够，函数体为空或 nop | 第10章 课时6-12 | 对应 FART 三组件、code item 修复、repaired dex |
| dump 出 dex 但 JADX 不可读 | 第10章 课时12、15 | 查 code item、bin 五元组、定制 JADX、dex 重构 |
| Frida 一启动就退、检测 Frida 特征 | 第10章 课时16-17；第13章 课时1-3 | 对应 `diagnose-android-instrumentation` 的反检测恢复阶梯 |
| libc hook 看不到检测，怀疑 SVC/syscall | 第13章 课时1-3；第3章 课时17 | 先按 P0/P1 提炼走 libc -> SVC 升级路径 |
| JNI 动态注册、JNI 地址绑定、防追踪 | 第10章 课时15；第13章 课时5-6 | 对应 `map-android-jni` 与 native trace 交叉验证 |
| VMP 保护函数或需要构建映射 | 第6章 课时1-9；第10章 课时9 | 目前只作为 P2 专项，遇到真实 VMP 再展开 |
| Unidbg/Unicorn/AndroidNativeEmu 离线执行 | 第7章 课时1-9 | 对照已有 `run-so-with-unidbg`、`patch-unidbg-environment` |
| 非标准算法、魔改 MD5/SHA1/HMAC/AES/RC4 | 第8章、第9章 | 作为算法案例库和评测集候选 |
| 需要 kernel/eBPF 观察 syscall | 第11章；第13章 | 远期高级观测路线，不进入默认路径 |
| iOS 逆向、iOS Frida、libsscronet SSL pinning | 第14章 | 不属于本 Android workflow；后续可单独开 iOS workflow |

## 当前转写优先级状态

### 已完成 P0

- 第1章 课时13：Frida + IDA Trace 分析算法（上）
- 第1章 课时14：Frida + IDA Trace 分析算法（中）
- 第1章 课时15：Frida + IDA Trace 分析算法（下）
- 第1章 课时16：Frida Stalker Trace 算法
- 第10章 课时2：加壳 APP 的运行流程与 ClassLoader
- 第13章 课时1：深入探索 Android 逆向中的 SVC syscall
- 第13章 课时3：实战之多种姿势定位 SVC syscall

### 已完成 P1

- 第5章 课时9：逆向 OLLVM 算法的通用方法
- 第10章 课时6：FART 框架简介与脱壳点的选择
- 第10章 课时12：FART 与定制版 JADX 带来如丝般顺滑体验
- 第10章 课时16：Frida 常见特征检测与对抗

### P2 候选

这些不建议现在全量转写，只在真实问题触发时处理：

- 第13章 课时2：三种 SVC syscall 指令追踪技巧总结横评
- 第10章 课时17：如何快速绕过被 OLLVM 混淆的 Frida 检测
- 第10章 课时15：JNI 函数地址绑定奇技淫巧以及定制 JADX 解决 dex 无法反编译问题
- 第10章 课时13-14：Stalker 使用与 trace ART 解释器引擎
- 第6章 课时2-3：VMP 保护函数的快速逆向分析
- 第6章 课时7/9：Hyperpwn 调试 VMP 并构建映射

## 两级课程目录

### 第1章 Frida高级逆向

- 课时1：Frida Hook Java（上）
- 课时2：Frida Hook Java（下）
- 课时3：Frida Hook Java（上）
- 课时4：Frida Hook Java（下）
- 课时5：Frida Hook Native（上）
- 课时6：Frida Hook Native（下）
- 课时7：Frida 辅助分析 OLLVM 字符串加密（上）
- 课时8：Frida 辅助分析 OLLVM 字符串加密（下）
- 课时9：Frida 辅助分析 OLLVM 控制流程平坦化（上）
- 课时10：Frida 辅助分析 OLLVM 控制流程平坦化（下）
- 课时11：Frida 辅助分析 OLLVM 指令替换（上）
- 课时12：Frida 辅助分析 OLLVM 虚假控制流程（下）
- 课时13：Frida + IDA Trace 分析算法（上）
- 课时14：Frida + IDA Trace 分析算法（中）
- 课时15：Frida + IDA Trace 分析算法（下）
- 课时16：Frida Stalker Trace 算法

### 第2章 Frida_FART全自动脱壳机

- 课时1：动态加载与双亲委派
- 课时2：加壳 APP 的运行流程与 ClassLoader 修正
- 课时3：APP 加壳技术发展与识别
- 课时4：ART 下 dex 加载流程和通用脱壳点
- 课时5：ART 下类加载流程与抽取壳实现
- 课时6：FART 框架简介与脱壳点的选择
- 课时7：FART 主动调用组件设计和源码分析
- 课时8：使用 Frida 增强 FART 脱壳能力
- 课时9：FART 修复组件与辅助 VMP 还原

### 第3章 ARM_C++算法还原原理_Frida

- 课时1：ARM 可执行文件的生成过程
- 课时2：GDB 调试 ARM 汇编
- 课时3：ARM 常见汇编指令
- 课时4：ARM 寻址方式与 ARM 汇编程序开发
- 课时5：ARM 架构参考手册
- 课时6：ARM 汇编指令集
- 课时7：Thumb 汇编指令集与 IT 指令
- 课时8：AArch64 汇编指令集与 R8
- 课时9：C 程序逆向分析：数据类型与运算符
- 课时10：C 程序逆向分析：分支跳转与循环
- 课时11：C 程序逆向分析：函数与结构体
- 课时12：C 程序逆向分析：数组与位操作
- 课时13：C++ 程序逆向分析：类与对象的内存布局
- 课时14：C++ 程序逆向分析：类的虚函数与虚表
- 课时15：C++ 程序逆向分析：类的继承、重载、覆盖
- 课时16：C++ 程序逆向分析：RTTI 和异常
- 课时17：内联汇编与 syscall
- 课时18：Android Studio 汇编开发

### 第4章 C++11_art打造动态分析沙箱

- 课时1：C++11 对于 ART 的重要性和初步认识
- 课时2：类型推导和访问权限相关
- 课时3：模板函数和模板类
- 课时4：模板函数和 lambda
- 课时5：ART 中 C++ 对象内存布局
- 课时6：ART 中 C++ 对象内存布局实践篇
- 课时7：ART 中的函数 inline
- 课时8：ART 定制方案比较和流程
- 课时9：ART 定制跟踪 JNI 函数绑定

### 第5章 彻底搞懂OLLVM

- 课时1：LLVM 简介与 LLVM 编译、调试 LLVM
- 课时2：LLVM Pass
- 课时3：OLLVM 简介与移植
- 课时4：OLLVM 控制流程平坦化源码解析
- 课时5：OLLVM 虚假控制流程源码解析
- 课时6：OLLVM 指令替换源码解析
- 课时7：字符串加密
- 课时8：NDK 中使用 OLLVM
- 课时9：逆向 OLLVM 算法的通用方法
- 课时10：逆向 OLLVM 的非通用方法

### 第6章 高级调试之VMP

- 课时1：Android APP 加壳技术分类与初识 VMP
- 课时2：VMP 保护的函数的快速逆向分析方法理论篇
- 课时3：VMP 保护的函数的快速逆向分析方法实践篇
- 课时4：ADVMP 源码分析与 VMP 壳简单上手（上）
- 课时5：ADVMP 源码分析与 VMP 壳简单上手（下）
- 课时6：定制 ART，绕过所有反调试
- 课时7：Hyperpwn 的安装和使用
- 课时8：定制内核体验内存断点的威力
- 课时9：使用 Hyperpwn 调试 VMP 并构建映射

### 第7章 unicornunidbg

- 课时1：Capstone、Unicorn、Keystone 三兄弟
- 课时2：Unicorn 初识与上手
- 课时3：Unicorn 调用 so 中函数
- 课时4：Unicorn 模拟调用 JNI 接口函数
- 课时5：Unicorn 模拟调用 JNI_OnLoad
- 课时6：AndroidNativeEmu 调用 JNI 函数
- 课时7：AndroidNativeEmu 模拟与 Java 函数交互
- 课时8：Unidbg 加载 so 并调用 so 中函数
- 课时9：Unidbg 模拟与 Java 交互

### 第8章 非标准算法还原（上）

- 课时1：常用加解密算法简介
- 课时2：算法还原案例1：Base64
- 课时3：算法还原案例2 CRC32 与案例3 MD5
- 课时4：算法还原案例4：OLLVM_MD5
- 课时5：算法还原案例5：OLLVM_SHA1
- 课时6：算法还原案例6：HMAC
- 课时7：算法还原案例7：OLLVM_Base64
- 课时8：算法还原案例8：OLLVM_RC4
- 课时9：算法还原案例9：Frida Stalker OLLVM AES

### 第9章 非标准算法还原（下）

- 课时1：常见算法特征及手动编译 OpenSSL
- 课时2：常见算法特征及手动编译 OpenSSL（下）
- 课时3：动态编码表的内存动静态比对还原
- 课时4：MD5 加盐更改常量及 OLLVM
- 课时5：SHA1 加盐更改常量及 OLLVM
- 课时6：魔改 OLLVM HMAC-MD5 算法还原
- 课时7：BPO 插件还原 OLLVM 非标准算法
- 课时8：Frida 辅助 Android SO 算法还原和自动化黑盒调用

### 第10章 Frida_Fart脱壳

- 课时1：动态加载与双亲委派
- 课时2：加壳 APP 的运行流程与 ClassLoader
- 课时3：APP 加壳技术发展与识别
- 课时4：ART 下 dex 加载流程和通用脱壳点
- 课时5：ART 下类加载流程与抽取壳实现
- 课时6：FART 框架简介与脱壳点的选择
- 课时7：FART 主动调用组件设计和源码分析
- 课时8：使用 Frida 增强 FART 脱壳能力
- 课时9：FART 修复组件与辅助 VMP 还原
- 课时10：fdex2 脱壳原理及拓展
- 课时11：高版本 Fdex2 实现
- 课时12：FART 与定制版 JADX 带来如丝般顺滑体验
- 课时13：优秀学员作业点评以及 Stalker 使用
- 课时14：优秀学员作业点评以及编写 Frida 脚本 trace ART 下的解释器引擎
- 课时15：JNI 函数地址绑定奇技淫巧以及定制 JADX 解决 dex 无法反编译问题
- 课时16：Frida 常见特征检测与对抗
- 课时17：如何快速绕过被 OLLVM 混淆的 Frida 检测

### 第11章 eBPF环境搭建与热门项目源码赏析

- 课时1：2023 年 eBPF 在 Android 上的现状
- 课时2：eBPF 手机开发环境搭建与项目开发
- 课时3：eBPF 实用项目核心源码的技术原理解析

### 第12章 Fart10_12

- 课时1：实战 FART10 源码移植与脱壳实战

### 第13章 内核模块绕过Frida检测

- 课时1：深入探索 Android 逆向中的 SVC syscall
- 课时2：三种 SVC syscall 指令追踪技巧总结横评
- 课时3：实战之多种姿势定位 SVC syscall
- 课时4：内存动态释放代码技术实战应用
- 课时5：JNI 函数地址防追踪技术实战对抗
- 课时6：利用硬件断点快速分析某加壳 APP 的 JNI 函数地址防追踪技巧

### 第14章 iOS设备指纹开发与逆向

- 课时1：2023 年的 iOS 逆向指南
- 课时2：ObjC & Frida hook 和主动调用
- 课时3：iOS 反调试技术与 Frida 绕过（上）
- 课时4：iOS 反调试技术与 Frida 绕过（下）
- 课时5：OLLVM obfuscated libsscronet.so SSL pinning bypass（上）
- 课时6：OLLVM obfuscated libsscronet.so SSL pinning bypass（下）

## 使用纪律

1. 先按 workflow 当前红灯定位问题，再查本索引；不要为了用课程而改变当前 TASK 目标。
2. 优先读取已经整理的 P0/P1 报告；只有证据不足时再回到原始视频、source 或转写。
3. 如果课程资料提供的是通用脚本，先判断能否清洗为 Skill asset；如果绑定具体 App，则只留在 TASK。
4. 如果课程内容只是基础知识补课，不要升级 Skill；只有形成可迁移 `X -> ✅` 路线时才反哺。
5. 每次实际采用课程资料，都要回写 `references/course-provenance.md`。
