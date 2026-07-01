# Native 地址语义

同一个调用链至少可能出现四种地址，必须带类型记录：

| 类型 | 含义 | ARM32 Thumb 示例 |
|---|---|---|
| `runtime_function_pointer` | 运行时可调用函数指针，可能包含 Thumb 位 | `0x1c97` |
| `static_code_address` | 静态工具中的代码地址 | `0x1c96` |
| `call_instruction_address` | `BL/BLX` 指令自身地址 | `0x3130` |
| `return_address` | 调用完成后继续执行的位置 | `0x3134` |

判断差异前先比较地址类型。Thumb 指针与静态地址差 1、调用指令与返回地址差一条指令，通常是表示方式不同，不是证据冲突。

报告中不要只写“偏移”，至少写：

```yaml
address:
address_type:
module:
abi:
thumb:
source:
```
