# RegisterNatives 平行路线

## 目的

动态 JNI 注册的目标是把 Java `native` 声明映射到 so 中的实现地址。不要在 stripped so 中盲猜入口，优先使用运行时注册事实。

## 路线 A：读取 `JNINativeMethod` 数组

这是默认主路线。

```text
Hook RegisterNatives(env, clazz, methods, count)
-> 读取 methods[i].name
-> 读取 methods[i].signature
-> 读取 methods[i].fnPtr
-> 计算 module / raw_offset / code_offset / thumb
```

优点：

- 字段完整；
- 直接得到 `method_name`、`signature` 和函数指针；
- 适合输出结构化 JSONL；
- 版本适配性通常比 ART 内部符号路线更稳。

局限：

- 必须在注册发生时命中；
- 部分 ROM/Android 版本上 RegisterNatives 符号筛选可能需要调整；
- 如果目标类过滤过窄，可能错过先于脚本加载完成的注册事件。

## 路线 B：ART `PrettyMethod + retval`

这是平行/交叉验证路线，不作为默认主路线。

```text
Hook ART 内部注册回调
-> 从 ArtMethod* 用 PrettyMethod 得到 Java 方法可读名
-> 从返回值/注册结果得到 native 函数指针
-> 用 ModuleMap 找到 so 与 offset
```

优点：

- 从 ART 最终绑定视角看方法和 native 函数；
- 输出方法名直观；
- 可作为主路线证据不足时的交叉验证。

局限：

- 依赖 ART 内部符号与函数签名；
- Android 版本、架构和 ROM 差异更敏感；
- 可能只能得到 pretty method 和地址，缺少完整 JNI signature；
- 需要额外确认返回值语义是否确实是目标 native implementation。

看雪第4章课时9“ART 定制跟踪 JNI 函数绑定”属于这条路线的高侵入版本：它从定制 Runtime 视角观察最终绑定关系，适合长期研究、批量样本或普通 `RegisterNatives` Hook 证据不足的场景。它不能替代默认 `JNINativeMethod` 数组路线；只有在版本差异、早期注册、包装注册或防追踪导致低侵入路线不稳定时，才作为参考入口。

## 使用顺序

默认：

```text
静态导出检查
-> JNINativeMethod 数组路线
-> 反汇编确认入口/跳板
-> Native Hook 验证目标动作中执行
```

交叉验证或 fallback：

```text
JNINativeMethod 事件缺失/不完整/符号不稳定
-> ART PrettyMethod + retval 路线
-> 对齐 class/method/offset
-> 回到反汇编或 Native Hook 验证
```

如果两条路线都出现缺失、不一致、跳板、动态释放或调试时地址变化，读取 `jni-address-anti-trace.md`，不要继续把问题归类为普通动态注册。

## 看雪查字典入口

优先查看：

- 看雪第4章 课时9：ART 定制跟踪 JNI 函数绑定；
- 看雪第10章 课时15：JNI 函数地址绑定与定制 JADX；
- workflow 顶层 `../../../references/kanxue-course-directory-index.md`。

采用后回写 workflow 顶层 `../../../references/course-provenance.md`。

## 证据等级

- A：两条路线或一条路线加反汇编/Native Hook 交叉验证一致。
- B：只有运行时 RegisterNatives 映射，但入口/跳板尚未确认。
- C：只有静态猜测或课程示例地址。

无论哪条路线，JNI 映射只证明入口位置，不证明算法已复现。
