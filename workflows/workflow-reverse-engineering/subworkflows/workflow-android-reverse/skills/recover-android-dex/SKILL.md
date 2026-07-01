---
name: recover-android-dex
description: 诊断经过授权的 Android APK 是否因加固壳、动态加载或拆分 Dex 导致 JADX 只能看到壳代码，并设计从运行时内存、ClassLoader 或现有脱壳工具恢复可分析 Dex 的最小路线。用于静态搜索几乎无业务类、Application 指向代理壳、出现 shell/jiagu/proxyapplication 特征、运行时类存在但 APK Dex 中缺失的场景。不得对未授权应用脱壳或分发恢复出的代码。
---

# Android Dex 恢复

## 目标

先证明“代码缺失是壳/动态加载问题”，再选择恢复路线：

```text
APK 静态清点
→ 壳证据
→ 运行时加载时点
→ Dex 恢复
→ 质量筛选
→ JADX/Smali 可用性
→ 返回静态定位主线
```

## 工作流

1. 固定 APK 哈希、版本和授权范围。
2. 统计 Dex、业务包类数、Application、ClassLoader 与可疑 shell so/assets。
3. 若只是多 Dex、反编译错误或 Flutter/React Native，不直接判定加壳。
4. 按 `references/shell-diagnosis.md` 建立壳证据。
5. 读取 `references/route-selection.md` 选择恢复路线：frida-dexdump/内存特征扫描、ClassLoader/Xposed 工具、ART `DefineClass` Hook、自研 Frida dump、手动寄存器/内存恢复、定制 AOSP 脱壳机或商业服务。若问题进入 FART、code item 修复、定制 JADX 或 AOSP/ART 改造，继续读取 `references/aosp-art-fart-routes.md`。先选低侵入可回滚路线；高侵入路线必须有独立设备、授权和回滚方案。
6. 动态路线开始前先通过插桩 Smoke。
7. 触发目标业务代码加载后再 dump，避免只得到壳 Dex。
8. 按 `references/dump-quality.md` 去重、校验 magic/header、记录来源和加载顺序。
9. 单个 Dex 逐一导入 JADX，隔离损坏文件，不因一个坏 Dex 丢弃全部结果。
10. 以“目标类可检索且方法体可读”为 Green，返回 `locate-android-request-builder`。

## 结构核验案例

Day22 酒仙网 `9.1.13`：

- APK 含 `libshell-super.2019.so`、`libshella-4.2.0.10.so` 和 `.dat` 资产；
- JADX 仅恢复约 15 个壳/代理源码文件；
- `MyWrapperProxyApplication` 指向运行时业务 Application。

这支持“静态业务 Dex 不完整”的诊断，但本轮未实际执行内存 dump，因此状态为 `learning`。

## DefineClass Hook 资产

R3 ART `DefineClass` Hook 路线可从 `assets/upstream-dex-dump/` 复制 upstream 脚本到 TASK：

- `search.js`：只观察 DefineClass 捕获到的 Dex base/size，适合 smoke；
- `dumpdex.js`：模糊匹配 `ClassLinker::DefineClass` 并保存 Dex；
- `myfridadump.js`：更完整的 DefineClass dump 实现。

这些脚本只代表一种路线。使用后必须按 `references/dump-quality.md` 检查 magic、size、目标类、JADX 可读性和重复/损坏文件。

## Green 条件

- 至少恢复一个含目标业务类的有效 Dex；
- 记录 dump 工具、时间点、进程和 ClassLoader；
- 损坏/重复 Dex 已隔离；
- JADX 或 Smali 能定位目标类和方法；
- 恢复产物只存放在授权 TASK 证据目录。

## 参考资料

- 壳证据读取 `references/shell-diagnosis.md`。
- 路线选择读取 `references/route-selection.md`。
- FART、code item、定制 JADX、AOSP/ART 改造读取 `references/aosp-art-fart-routes.md`。
- Dump 质量读取 `references/dump-quality.md`。
- 使用 `assets/dex-recovery-manifest.md` 记录产物。
- 使用 ART DefineClass Hook 路线时，从 `assets/upstream-dex-dump/` 复制 upstream 脚本到 TASK。
