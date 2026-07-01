# Dex Dump Upstream Assets

这些脚本是 Dex 恢复路线中的 upstream 资产，使用前复制到具体 TASK 目录。

## 文件

- `dumpdex.js`：基于 `libart.so` 中 `ClassLinker::DefineClass` 模糊匹配的 Dex dump 脚本。
- `myfridadump.js`：基于 `DefineClass` 的较完整 Frida dump 实现，包含目录创建与包名识别。
- `search.js`：只搜索并打印 `DefineClass` 捕获到的 Dex base/size，不写文件，适合作为 smoke/probe。

## 使用边界

- 这些脚本属于 R3 ART `DefineClass` Hook 路线，不替代 frida-dexdump、Xposed/Fdex2、自研内存扫描、手动调试或 AOSP 脱壳机。
- 使用前先证明 APK 静态业务 Dex 缺失，并确认目标业务类的触发动作。
- Dump 结果必须经过 `references/dump-quality.md` 质量门槛，不因脚本输出文件就认定恢复完成。
- 恢复产物只能保存在授权 TASK 证据目录，不分发恢复出的业务代码。
