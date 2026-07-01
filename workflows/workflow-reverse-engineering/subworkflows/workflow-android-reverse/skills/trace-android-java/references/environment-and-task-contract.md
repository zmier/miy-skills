# 环境与 TASK 归属

## 共享环境

运行时依赖位于 `workflow-android-reverse/`：

- `.venv`：Frida Python bindings、frida-tools、算法复现依赖和测试；
- `node_modules`：Frida 17 Java Bridge 与 Agent 编译器；
- `Makefile`：初始化、编译、手机端 server 安装、启停和验证；
- `scripts/frida-device.sh`：单设备、Root 和 server 生命周期控制。

主机 `frida` 包与手机端 `frida-server` 必须严格同版本。

## TASK 脚本

具体类名、方法名和业务字段属于某个需求，放在该需求的 TASK 阶段目录：

```text
TASK-需求/tasks/TASKxx-Frida-动态取证/
├── hook_*.ts
├── run_hook.py
├── dist/
├── outputs/
└── log.md
```

运行器通过共享 `.venv` 执行，Agent 通过共享 `node_modules` 编译。迁移 Skill 时可迁移环境规范，不把某个 APK 的混淆符号硬编码进通用 Skill。

## 日志

ReAct 只记录可审计的操作理由，不记录私有思维过程：

- `Reason`：本轮要消除的证据缺口；
- `Action`：实际命令、Hook 或触发动作；
- `Observation`：工具原始结果摘要；
- `Decision`：由证据支持的阶段结论与下一动作。
