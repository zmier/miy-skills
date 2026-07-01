# Frida 兼容与 Agent 规则

## 版本选择

默认先验证当前稳定版，但主机 `frida` 与手机端 `frida-server` 必须严格同版本。若 Agent 在脚本加载前崩溃，应先用 tombstone 区分：

- 目标应用自己的反插桩退出；
- Frida Agent 的平台兼容崩溃；
- Hook 脚本加载后的 JavaScript 异常。

Day17 的 B站 6.24.0 是 32 位旧应用。在 Pixel 4 XL / Android 11 上：

- Frida 17.12.0 注入时于 `frida-agent-32.so` 内 SIGSEGV；
- Frida 16.7.19 可以附加，但 Java Bridge 建模时出现 `invalid instruction`；
- 课程提供并验证过的 Frida 16.0.19 能覆盖该 App 与系统组合。

因此该 fixture 固定使用 Frida 16.0.19 兼容通道。

## Agent

Frida 16 提供全局 `Java`。项目仍通过 `frida-compile` 将 TASK 中的 TypeScript Agent 打成单文件 JavaScript：

1. 使用精确 overload。
2. 调用保存的 overload，避免递归。
3. 原样返回结果。
4. 二进制以 hex 记录。
5. 事件使用稳定的 `event` 名称和 JSON 字段。
6. 业务 Hook 期间才采集底层通用算法，减少噪声。

迁移到 Frida 17 时，Agent 应显式引入 `frida-java-bridge` 并重新完成真机 evaluation，不直接修改已经通过的 fixture 环境。
