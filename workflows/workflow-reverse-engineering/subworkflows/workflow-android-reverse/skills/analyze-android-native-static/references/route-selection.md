# Native 静态分析路线选择

| 问题 | 优先路线 |
|---|---|
| 已知一个窄偏移，只需确认入口、跳板或 `BL` 调用 | LLVM objdump |
| 需要理解复杂分支、循环、对象构造或查看 xref | IDA/Hex-Rays |
| 课程学习要求复现 IDA，或结论需要高置信度 | IDA + objdump 交叉验证 |
| 真实参数、缓冲区或动态 Key 未知 | 静态路线后接 Frida Hook |

IDA 内部选择：

- 要生成稳定 JSON、IDB 和 manifest：IDAPython batch。
- 要交互式提问、快速查看伪代码/xref：IDA MCP。
- 要让 MCP 结论进入 Green：将最小复核报告落盘，并记录输入哈希与关闭状态。

主流程完成后补做 IDA，可以标为“非阻塞增强分支”。它验证知识与工具能力，但不回滚已经通过的 G1/G2。
