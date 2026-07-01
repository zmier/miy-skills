# Xposed/LSPosed P1 module-loaded SOP

## 适用场景

当 Frida RPC 已经证明 App 运行态路线可行，但长跑稳定性、重启恢复或长期在线能力不足时，进入 A5/R4-X 服务化路线。

P1 的目标不是业务 RPC，也不是 Sekiro action，而是先证明：

```text
Xposed/LSPosed 模块能稳定加载进目标 App 的目标进程
```

## 边界

P1 不做：

- 不注册业务 action；
- 不连接 Sekiro；
- 不发送真实业务请求；
- 不读取或返回账号态、设备态、签名态字段；
- 不做设备态重置或高危 action。

P1 只做：

```text
module-loaded
classloader-ready
target package scoped
restart smoke
```

## TDD 顺序

必须先 Red，再 Green：

```text
写 ReAct plan
-> 写 P1 smoke/UAT 检查表
-> 写静态契约测试
-> 创建最小模块
-> 构建安装
-> 启用 LSPosed/scope
-> logcat smoke
-> P1 验收报告
```

如果 LSPosed、Zygisk、构建工具或 Manager 操作缺失，不要把 P1 写成 Green，应停在明确的 Red/gate。

## P1 Red 检查表

至少声明以下 Red：

```text
module source exists
AndroidManifest declares xposed metadata
assets/xposed_init declares module entry
entry implements IXposedHookLoadPackage
target package is declared
log tag is stable
module install evidence exists
LSPosed framework active
module enabled in LSPosed
target app scope selected
logcat contains module-loaded
logcat contains classloader-ready
restart smoke contains module-loaded again
```

## 最小模块骨架

P1 入口只做目标包判断和日志：

```java
public class Entry implements IXposedHookLoadPackage {
    private static final String TAG = "YourTag";
    private static final String TARGET_PACKAGE = "com.example.target";

    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam lpparam) {
        if (!TARGET_PACKAGE.equals(lpparam.packageName)) {
            return;
        }
        Log.i(TAG, "module-loaded package=" + lpparam.packageName
                + " process=" + lpparam.processName);
        Log.i(TAG, "classloader-ready process=" + lpparam.processName
                + " classLoader=" + lpparam.classLoader.getClass().getName());
    }
}
```

P1 不应出现：

```text
SekiroClient
executeRPC
真实 operationType
任意方法调用器
敏感字段读取
```

## Manifest 要点

必须有：

```xml
<meta-data android:name="xposedmodule" android:value="true" />
<meta-data android:name="xposeddescription" android:value="..." />
<meta-data android:name="xposedminversion" android:value="82" />
```

推荐声明 scope，减少 Manager 中误选：

```xml
<meta-data
    android:name="xposedscope"
    android:resource="@array/xposed_scope" />
```

```xml
<string-array name="xposed_scope">
    <item>com.example.target</item>
</string-array>
```

不要在 P1 申请危险权限。

## 构建环境 SOP

如果本机没有完整 Android Studio，可以使用命令行工具：

```text
JDK 17+
Gradle 8.x
Android commandline tools
platforms/android-xx
build-tools/xx
```

Xposed API 不一定存在于 Maven Central。若无法解析：

```text
de.robv.android.xposed:api:82
```

可使用本地 `compileOnly` stub jar 只满足编译。stub 不得打进 APK，运行时由 LSPosed 提供真实 API。

## 设备环境 SOP

1. 检查设备：

```bash
adb devices
adb shell su -c id
adb shell pm path <target.package>
```

2. 检查 Magisk/LSPosed：

```bash
adb shell su -c 'ls -la /data/adb/modules'
adb shell su -c 'ps -A | grep -Ei "lspd|lsposed|magisk"'
```

3. 若只有 Magisk 没有 LSPosed：

```text
安装 Zygisk 版 LSPosed
启用 Magisk Zygisk
重启设备
确认 lspd 进程存在
```

4. 安装模块 APK：

```bash
adb install -r app-debug.apk
```

5. 用 LSPosed Manager：

```text
确认框架已激活
进入“模块”
打开目标模块开关
勾选目标 App scope
重启目标 App 或重启设备
```

## 不推荐直接写 LSPosed DB

不优先手写：

```text
/data/adb/lspd/config/modules_config.db
```

原因：

- `lspd` 可能持有 DB；
- WAL/SHM 同步容易脏；
- SELinux 可能阻止 shell/root 上下文读写；
- APK 重装后路径可能变化，`apk_path` 过期会导致模块不加载；
- Manager/manifest scope 更可解释、更可复现。

只有在授权测试环境中、且 Manager 路线不可用时，才把 DB 写入作为临时救援手段，并必须记录 Red、备份 DB、回滚方式和 UAT。

## Smoke

推荐脚本逻辑：

```bash
adb logcat -c
adb shell am force-stop <target.package>
adb shell monkey -p <target.package> -c android.intent.category.LAUNCHER 1
sleep 20
adb logcat -d -v time | grep -E '<TAG>|LSPosed|Xposed'
```

P1 Green 证据：

```text
LSPosed: Loading xposed for <target.package>
LSPosed-Bridge: Loading legacy module <module.package>
LSPosed-Bridge: Loading class <entry.class>
<TAG>: module-loaded package=<target.package> process=<process>
<TAG>: classloader-ready process=<process> classLoader=<classloader>
```

必须做 restart smoke：

```text
force-stop/start 后再次出现 module-loaded
或设备重启后再次出现 module-loaded
```

## 多进程注意事项

大型 App 常会加载多个进程：

```text
主进程
:push
:gpu_process
:sandboxed_privilege_process*
:widgetProvider
```

P1 可以只记录多进程现象；P2 以后必须引入 `ProcessRouter`：

```text
只在目标业务进程注册 action server
其他进程只记录 module-loaded，不启动服务
```

否则会出现多个 action server、端口冲突、重复注册或状态混乱。

## P1 输出物

建议每个 TASK 至少保存：

```text
docs/P1-module-loaded-smoke.md
tests/unit/test_p1_static_contract.*
outputs/p1/device-probe.txt
outputs/p1/build.txt
outputs/p1/install.txt
outputs/p1/logcat-module-loaded.txt
outputs/p1/restart-smoke.txt
outputs/p1/P1验收报告.md
logs/log.md
```

## P1 Green Contract

```text
module-loaded=true
classloader-ready=true
targetPackage captured
processName captured
classLoader captured
scope selected
appRestartReloaded=true
liveBusinessRequest=false
```

若缺任一项，P1 仍为 Red 或 `passed-with-scope`，不能进入业务 action。

