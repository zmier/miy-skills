# Xposed/Sekiro Upstream Assets

这里保存课程中的 Xposed/Sekiro upstream 代码，作为迁移来源和对照材料。

## 文件

- `java/com/example/luov2/hookRpc.java`：Xposed 入口中启动 SekiroClient 并注册 handler。
- `java/com/example/luov2/handler/*.java`：Sekiro action handler 示例。

## 注意

- upstream 中包含固定 group、server IP、action 名称和业务类名，不能直接作为通用模板使用。
- 新 TASK 应优先复制 `XposedSekiroEntryTemplate.java` 和 `SekiroActionHandlerTemplate.java`，再按 upstream 对照修改。
