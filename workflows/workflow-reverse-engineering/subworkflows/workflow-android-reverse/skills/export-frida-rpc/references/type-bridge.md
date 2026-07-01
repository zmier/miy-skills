# RPC 类型桥接

| Python 输入 | RPC 传输 | Java 重建 |
|---|---|---|
| `str/int/float/bool/None` | 原生 JSON | 按目标重载直接传入或显式装箱 |
| `bytes/bytearray` | `[0..255]` | `Java.array('byte', values)`，注意大于 127 的有符号表示 |
| `dict` | object | 显式创建 `HashMap/TreeMap` 并逐项 `put` |
| 复杂对象 | 稳定字段 DTO | 在 Agent 内调用构造器或 Builder |

返回值同样只允许 JSON 可序列化类型。Java 对象先转换为字符串、字段字典或字节列表。
