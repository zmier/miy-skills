# 恢复路线阶梯

按侵入性由低到高：

1. 修正包名、PID、进程、Frida 版本、ABI 和端口。
2. attach/spawn 切换，提前安装最小 Hook。
3. 对目标 App 自身的 Root、模拟器或环境判断做窄 Hook。
4. 在空 Frida session 已稳定时，可以把 `objection` 这类 Frida 封装工具作为快速探针或通用绕过脚本来源；若 Frida server/attach 本身触发退出，不要把 `objection` 当作更底层的绕过方案。
5. 在授权实验设备上使用可回滚的 Root 隐藏配置。
6. 使用与主机客户端严格匹配的替代 Frida server，验证空脚本后再迁移 Hook。
7. 恢复 Dex 或定位 Native 检测点，实施目标化 Hook。
8. 定制 AOSP 作为专用分析设备。

若红灯表现为 Frida 特征检测、libc hook 无证据、SVC/syscall、linker/JNI 早期检测，先读取 `frida-svc-syscall-ladder.md`，再决定是否升级到第 7 或第 8 级。

每次只升级一级。Green 只证明当前环境可观察，不证明该方案对其他 App 通用。
