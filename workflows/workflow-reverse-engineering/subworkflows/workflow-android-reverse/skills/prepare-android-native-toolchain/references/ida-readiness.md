# IDA 就绪门槛

## 分级

1. `discovered`：发现安装包或应用路径。
2. `licensed`：用户确认软件来源和许可证有效。
3. `host-compatible`：CPU 架构、macOS、签名与依赖允许正常启动。
4. `so-openable`：能够打开目标 ABI 的 `.so` 并完成自动分析。
5. `scriptable`：IDAPython 或批处理脚本通过最小测试。
6. `mcp-available`：候选 MCP 与当前 IDA/Python API 兼容。
7. `validated`：MCP 能在课堂 fixture 上定位函数、交叉引用或导出伪代码，并保留证据。

不能从 `discovered` 直接跳到 `mcp-available`。

## 旧版安装包注意事项

Apple Silicon 主机遇到旧版分析器时至少检查：

- 主程序是否只有 `x86_64`；
- Rosetta 2 是否存在；
- 应用是否签名、公证；
- Qt 与 Python 插件运行时能否在当前 macOS 启动；
- 用户是否拥有合法许可证；
- 候选 MCP 是否支持该版本的 IDAPython API。

检查脚本只报告事实，不自动执行移除隔离、临时签名或修改系统安全设置。

具体工具版本和已验证案例应记录在调用方 TASK 与能力注册表，不写入本通用准备 Skill。静态分析交给 `analyze-android-native-static`。

## 降级路线

IDA 未就绪时仍可推进：

- `file`、`otool`、`nm`、`strings` 做基础 ELF/符号检查；
- Android NDK LLVM 工具做 ABI、段、符号和反汇编检查；
- 使用合法可用的 Ghidra 或新版 IDA 做 GUI 静态分析；
- 用 Frida 在运行时恢复模块基址、导出符号和真实参数。

MCP 是效率层，不是 JNI/Native 分析成立的前提。
