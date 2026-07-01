# Smoke-Native 就绪等级

| 等级 | 条件 | 可推进范围 |
|---|---|---|
| N0 | 只确认目标文件存在 | 清点目标、设计环境 |
| N1 | `adb`、`file`、`nm`、`otool`、`strings` 可用 | APK/so 基础清点 |
| N2 | Android SDK/NDK 可定位，LLVM 工具可用 | 编译 JNI fixture、检查 Android ELF |
| N3 | 至少一个 GUI Native 分析器能打开目标 `.so` | JNI 映射与静态 Native 分析 |
| N4 | Frida Native Hook 或分析器脚本化通过 | 运行时交叉验证 |
| N5 | MCP 在授权 fixture 上完成打开、查询、落盘复核与关闭 | 交互式自动化编排与独立确认 |

进入 JNI/Native 复现前建议至少达到 N2；进行 GUI 静态分析前达到 N3。MCP 是效率层，不应成为首次复现的强制依赖。
