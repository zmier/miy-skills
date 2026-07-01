# IDA MCP 使用与降级

IDA MCP 适合交互式定位、快速反编译和独立复核；稳定批量产物优先使用 IDAPython batch。

## 操作顺序

1. 打开 `.i64/.idb`，记录 IDB 对应输入文件的 SHA-256。
2. 检查分析状态、处理器、位数和函数数量。
3. 对最小目标执行 decompile、xref 或 address query。
4. 将结论整理为 TASK 报告，标明 `primary/confirmatory/exploratory`。
5. 显式关闭 IDB，释放锁。

## 降级条件

- MCP 无法识别 Thumb 函数边界：先用 IDAPython 修复并重建 IDB。
- 查询超时或输出过大：缩小地址范围，或改用 batch 导出。
- 需要可重复、可测试的批量证据：使用 `run_static_analysis.py`。
- MCP 结果未落盘：只能作为探索或确认，不作为唯一 Green。
