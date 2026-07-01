# 插桩失败分类

| 直接观察 | 优先假设 | 最小实验 | Green |
|---|---|---|---|
| `process not found` | App 未启动、名称不等于进程名、保护导致早退 | 枚举 application 与 process，使用包名/PID | 找到稳定 PID |
| 无 Frida 也弹安全提示 | Root、模拟器或设备环境检测 | 对照真实设备属性、目标判断方法与调用栈 | 仅修改单个判断后正常启动 |
| 仅启动 Frida 后闪退 | Frida 特征检测或版本问题 | 空脚本、改端口/名称、核对 tombstone | 空脚本稳定 |
| attach 失败、spawn 成功 | ptrace 占坑或启动早期保护 | 记录进程树、`/proc/<pid>/status`、spawn 对照 | spawn session 稳定 |
| Android 任务中出现 iOS DDI、非目标设备或包名不存在 | 多 USB Frida 设备误选 | `frida.enumerate_devices()`、`adb devices`、固定 Android serial | `frida.get_device(serial).attach(pid)` 成功 |
| session 成功但类不存在 | 类尚未加载、多进程或真实符号错误 | 枚举 ClassLoader、确认进程、真实 Dex 名 | 目标类可解析 |
| 脚本加载后崩溃 | Hook 签名、重载、递归或返回类型错误 | 空脚本后逐个恢复 Hook | 最小 Hook 稳定触发 |

错误文本只是线索。`unable to access process` 不能单独证明 ptrace 占坑，必须增加进程或 `/proc` 证据。
