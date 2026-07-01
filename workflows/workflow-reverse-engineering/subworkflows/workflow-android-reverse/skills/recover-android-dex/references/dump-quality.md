# Dex Dump 质量

每个文件记录：

- SHA-256、大小、Dex magic/version；
- 来源进程、ClassLoader、触发动作和时间；
- 是否包含目标包/类；
- 是否与其他文件重复；
- JADX/Smali 打开结果；
- 是否只有空壳或损坏片段。

先逐个导入，再组合导入。一个坏 Dex 导致 JADX 失败时隔离该文件，不要盲目删除未知产物。
