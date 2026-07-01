# JNI 注册方式

## 静态导出

静态注册通常能在导出表中看到 `Java_包名_类名_方法名`。优先核对：

- Java 方法是否重载；
- JNI 名称中的下划线转义；
- 目标 ABI 是否与当前设备一致；
- 导出函数是否只是跳板。

## 动态注册

动态注册通常在 `JNI_OnLoad` 或初始化函数中调用 `RegisterNatives`，把 `JNINativeMethod` 数组交给 ART。每项包含：

```c
typedef struct {
    const char *name;
    const char *signature;
    void *fnPtr;
} JNINativeMethod;
```

目标 `.so` 被 stripped 后，业务方法可以完全没有可读导出名。此时冷启动 Hook `libart.so` 中非 CheckJNI 的 `RegisterNatives`，按目标类过滤，比在二进制中猜函数更可靠。

## 选择顺序

1. 固定当前 APK、ABI 与模块哈希。
2. 查导出表和 `JNI_OnLoad`。
3. 有静态导出时建立候选映射。
4. 无导出或证据不足时冷启动捕获 `RegisterNatives`。
5. 用反汇编确认偏移附近的入口或跳板。
6. 用最小 Native Hook 验证该函数确实在目标动作中执行。
