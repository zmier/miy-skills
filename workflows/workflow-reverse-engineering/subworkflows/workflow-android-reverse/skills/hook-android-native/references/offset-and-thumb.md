# 模块偏移与 Thumb

## ASLR

运行时地址随进程变化：

```text
runtime_address = module_base + relative_offset
```

跨运行稳定的是“模块哈希 + 相对偏移”，不是绝对地址。

## ARM32 Thumb

ARM32 函数指针最低位可表示 Thumb 状态：

```text
code_offset = raw_offset & ~1
hook_pointer = module_base.add(code_offset).or(1)
```

- IDA、objdump 查找代码通常使用清除最低位后的 `code_offset`。
- Frida `Interceptor.attach` 到 Thumb 入口时通常需要保留或补回最低位。
- 计算调用者偏移时先清除返回地址最低位，再减模块基址。

AArch64 不使用这一最低位规则。

## 交付记录

报告中同时写明：

- ABI；
- 原始 JNI 函数指针；
- 模块基址；
- 原始偏移；
- 规范化代码偏移；
- Hook 时是否补 Thumb 位。
