# JNI 映射证据契约

每条完成证据至少包含：

| 字段 | 说明 |
|---|---|
| APK | 包名、版本、SHA-256 |
| 模块 | 文件名、ABI、SHA-256、Build ID |
| Java | 类名、方法名、完整 JNI 签名 |
| 注册 | 静态导出或动态 `RegisterNatives` |
| 运行时 | 实现地址、模块基址、原始相对偏移 |
| 指令集 | ARM/Thumb/AArch64，是否清除最低位 |
| 静态交叉检查 | objdump、IDA 或 Ghidra 中的入口与跳板 |
| 动态交叉检查 | 目标动作中是否执行 |
| 证据路径 | JSONL、反汇编报告与 ReAct 日志 |

地址表达建议：

```text
implementation = module_base + raw_offset
code_offset = raw_offset & ~1    # ARM32 Thumb
hook_address = module_base + code_offset | 1
```

ASLR 下绝对地址不可跨进程复用，稳定交付物应保存模块哈希与相对偏移。
