# Dex 恢复路线选择

## 来源背景

路飞 Day22 酒仙网笔记已经给出几类脱壳思路：

- 工具脱壳：Frida / Xposed / 内存特征寻找；
- Xposed 工具：Fdex2、dumpDex 等 Hook ClassLoader/loadClass 类方案；
- Frida 工具：`frida-dexdump`；
- 手动脱壳：动态调试 so，跟踪寄存器、内存偏移和 Dex 源文件地址；
- 自己定制脱壳机：例如基于 AOSP 或系统级插桩；
- 商业服务：如 armPro 等。

本 Skill 不把任何一种路线设为默认答案。先证明静态 Dex 缺失，再按侵入性、可回滚性、证据质量和目标壳强度选择。

## 路线表

| 路线 | 典型工具/实现 | 适用场景 | 主要产物 | 风险与边界 |
|---|---|---|---|---|
| R1 Frida 工具脱壳 | `frida-dexdump`、FRIDA-DEXDump | 壳不强、Frida 可注入、目标类运行时会加载 | 多个内存 Dex 文件 | 可能产出空壳/坏 Dex；受 Frida 检测影响 |
| R2 Xposed/ClassLoader 工具 | Fdex2、dumpDex、Hook ClassLoader/loadClass | 设备已有 Xposed/LSPosed，适合长驻或类加载时捕获 | 按 ClassLoader 或类加载时机 dump 的 Dex | 依赖模块环境；可能需要重启和作用域配置 |
| R3 ART DefineClass Hook | Hook `libart.so` 的 ClassLinker/DefineClass/DexFile 相关函数；可使用 `assets/upstream-dex-dump/` | 需要更贴近 Dex 定义时刻，普通工具漏 dump | Dex base/size、按加载时刻保存的 Dex | Android 版本差异大；符号匹配和参数位置需验证 |
| R4 自研 Frida 内存扫描 | 扫描内存 `dex\n035/037/038` magic、解析大小并保存 | 工具不可用但 Frida 可注入；需要定制过滤 | 符合 magic 的内存片段 | 容易误报/漏报；必须做质量筛选 |
| R5 手动调试/寄存器跟踪 | IDA/gdb/lldb/frida-trace，跟踪 so 解密/加载逻辑 | 壳强、工具 dump 不完整，需要定位 Dex 解密后地址 | 精确内存地址、size、dump 文件、调试记录 | 成本高；涉及汇编、寄存器、反调试、反读写 |
| R6 定制 AOSP 脱壳机 | 修改 ART/ClassLinker/DexFile 加载路径并刷机 | 需要稳定研究多个加固样本，且有专用设备 | 系统级自动 dump 产物 | 高侵入；需要独立设备、源码构建和回滚 |
| R7 商业/第三方服务 | armPro 等 | 教学或商业授权场景下节约时间 | 第三方返回 Dex | 许可证、隐私、样本外发和可复核性问题 |

FART、code item 修复、定制 JADX、AOSP/ART 改造的触发条件和边界见 `aosp-art-fart-routes.md`。这些路线属于高级恢复路线，不因课程目录中存在就自动成为当前 TASK 的 NEXT。

## 看雪查字典入口

当红灯集中在“壳识别、ClassLoader 替换、Dex 加载时机、普通 dump 路线漏类或产物质量差”时，可以把看雪第2章作为 Dex 恢复路线选择的参考入口。

优先查看：

- 看雪第2章 课时1-3：动态加载、双亲委派、ClassLoader 修正、加壳流程与壳识别；
- 看雪第2章 课时4-5：ART 下 dex 加载流程、类加载流程、通用脱壳点和抽取壳；
- workflow 顶层 `../../../references/kanxue-course-directory-index.md`。

使用边界：

- 看雪第2章用于解释“为什么当前 APK 静态 Dex 不完整”以及“下一条恢复路线怎么选”，不能替代当前 APK 的壳证据；
- 具体 Green 仍以当前 TASK 的目标类、目标方法、dump 质量和 JADX/Smali 可读性为准；
- 若问题已经进入 FART 主动调用、code item 修复、repaired dex 或定制 JADX，继续转 `aosp-art-fart-routes.md`。

## 推荐选择顺序

```text
壳证据成立
→ 先确认目标类何时加载
→ R1 frida-dexdump 或 R2 Xposed 工具
→ 若产物缺目标类或坏 Dex 多，尝试 R3 DefineClass Hook / R4 自研扫描
→ 若仍缺关键类，进入 R5 手动调试和寄存器/内存跟踪
→ 多样本长期研究才考虑 R6 AOSP 脱壳机
→ R7 只作外部服务选项，不作为 workflow 默认能力
```

## 触发动作

Dex 恢复不是“启动 App 就完事”。必须记录触发动作：

- 冷启动；
- 登录；
- 进入目标页面；
- 点击目标功能；
- 触发插件/动态模块加载；
- 触发 WebView/小游戏/小程序容器。

如果 dump 后没有目标类，先判断是否触发时机不对，不要直接判定工具失败。

## 质量门槛

每条路线产出的 Dex 都必须通过 `dump-quality.md`：

- Dex magic 和 version 合法；
- size 合理；
- 包含目标包、目标类或目标字符串；
- 可被 JADX/Smali 单独打开；
- 重复/空壳/损坏文件已隔离；
- 记录进程、ClassLoader、触发动作、工具版本和输出路径。

## 高侵入路线规则

以下路线不能作为默认 NEXT：

- 删除或 patch 壳 so；
- 绕过强反调试后手动跟踪；
- 定制 AOSP 或刷系统；
- 商业服务外发样本。

只有当低侵入路线无法得到目标业务类，并且授权、设备、回滚和证据需求都明确时，才升级到这些路线。
