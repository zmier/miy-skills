---
date: 2026-06-18
type: migration-audit
status: structural-green
scope:
  - workflow-reverse-engineering
  - workflow-android-reverse
---

# Android Workflow 资产审计

## 审计结论

本次迁移没有把 `workflow-android-reverse` 拆散，也没有丢弃核心工具链。当前更准确的状态是：

```text
Android 成熟 workflow 已作为 subworkflow 迁入
→ 父 workflow 已能承载跨平台骨架
→ Android 专属能力仍保留在 Android 子 workflow
→ 可迁移能力已经完成第一轮标注
→ 具体上提动作等待 JS 子 workflow 反向验证
```

这是一轮 `structural-green` 审计，不等于所有能力已经经过 JS / Windows / Unity 的 forward-test。

## 资产分层

### 1. 可上提到父 Workflow 的通用能力

这些能力不是 Android 独有，未来 JS、Windows、Unity 逆向也会遇到，只是工具不同。

| 能力 | Android 中的承载 | 父 workflow 里的抽象名称 | 上提建议 |
| --- | --- | --- | --- |
| 以终为始定义目标 | `android-request-reproduction` | target contract / UAT first | 可上提为父 workflow 默认入口 |
| TDD 式逆向 | `android-request-reproduction`、`validate-android-reproduction` | Red-Green reverse engineering | 可上提到 `references/tdd-reverse-engineering.md` |
| 证据台账 | request ledger、mermaid 任务树 | evidence ledger | 可上提模板 |
| 静态/动态交叉验证 | JADX + Frida、IDA + Hook | static-dynamic loop | 可上提为路线原则 |
| 参数/字段最小化 | `minimize-android-request` | input minimization | 可上提为通用实验方法 |
| oracle / replay / reproduction | Python、Frida RPC、Unidbg、App runtime | reproduction ladder | 可上提为跨平台复现阶梯 |
| 红灯分层 | 壳、混淆、反调试、网络不可见、环境缺失 | red-light taxonomy | 可上提为父 workflow 分类表 |
| 平行路线选择 | IDA vs objdump、Frida RPC vs Python 复现 | route portfolio | 可上提为决策参考 |
| 课程/案例反哺规则 | `extract-course-case-workflow` | feedback into workflow | 保留和 `course-driven-skill-engineering` 对齐 |
| 技术 Radar 机制 | 看雪/论文/社区 Radar | technology radar feedback | 父 workflow 只保留机制，不保留 Android 细节 |

建议：先上提文档和模板，不急着创建很多父级 Skills。父级 Skill 只负责路由和证据约束，具体动作仍交给平台子 workflow。

### 2. Android 专属能力

这些能力强依赖 Android 生态，应继续留在 Android 子 workflow。

| 能力 | 承载 Skill | 为什么不直接上提 |
| --- | --- | --- |
| 设备准备、ADB、Root、Magisk | `prepare-android-device` | Android 设备模型专属 |
| APK / DEX / ClassLoader / 脱壳 | `recover-android-dex` | Android Runtime 与 Dex 格式专属 |
| JADX 请求构造链定位 | `locate-android-request-builder` | Java/Kotlin APK 静态分析专属 |
| Frida Java Hook | `trace-android-java` | Android Java runtime 专属 |
| JNI 映射 | `map-android-jni` | JNI/ART/so 桥接专属 |
| Android Native Hook | `hook-android-native` | ELF/ARM/Android loader 组合专属 |
| Unidbg 加载 so | `prepare-unidbg-toolchain`、`run-so-with-unidbg`、`patch-unidbg-environment` | Android so 离线模拟专属 |
| App 运行态代发 | `dispatch-via-app-runtime`、`xposed-sekiro-runtime-dispatch` | 依赖 App 进程、账号态、设备态 |
| Android 网络通道识别 | `identify-android-business-network-channel` | mPaaS/mobilegw/Nebula/JSBridge 等 Android 容器生态强相关 |
| Reqable/mitmproxy/SocksDroid/VpnService | `capture-android-traffic`、`process-android-traffic` | 抓包工具可通用，但设备代理和 VPN 路线 Android 专属 |

建议：不要把这些内容塞进父 workflow。父 workflow 只记录“平台网络通道可能不走普通代理”“运行态代发是一种复现阶梯”，具体 Android 路径仍从子 workflow 读取。

### 3. 可迁移但需要平台适配的能力

这些能力很有价值，但迁移时不能复制 Android 工具名，要抽象成“同构问题”。

| Android 能力 | JS 可能对应 | Windows / Unity 可能对应 | 迁移方式 |
| --- | --- | --- | --- |
| JADX 查 URL / 字段 / 调用链 | AST、source map、webpack bundle 搜索 | IDA/Ghidra 查字符串/xref | 抽象为 static locator |
| Frida Hook Java 方法 | DevTools breakpoint、Node inspector、浏览器 hook | Frida/WinDbg/x64dbg Hook API | 抽象为 runtime observation |
| Native Hook so 函数 | wasm hook、WebAssembly trace | DLL/API hook、GameAssembly hook | 抽象为 native boundary observation |
| 参数归约 | 删除 header/body/query 字段 | 删除 API 参数/结构体字段 | 抽象为 minimization experiment |
| Python 纯复现算法 | JS/Node/Python 复现 | Python/C#/C++ 复现 | 抽象为 external reproduction |
| Frida RPC 借运行态 | 浏览器 automation / extension bridge | injected agent / debugger eval | 抽象为 in-runtime dispatcher |
| Unidbg 离线跑 so | Node vm / wasm runtime / jsdom | wine/emulator/harness | 抽象为 offline harness |
| Mermaid 请求构造树 | 任意平台任务树 | 任意平台任务树 | 父级模板可直接复用 |

建议：这些能力可以先上提为父 workflow 的 reference 和 template，再等 JS 子 workflow 做 forward-test。

## 工具与运行资产

### 已迁移并可用

- `tools/`：Frida server 多版本，包括 `16.0.19`、`16.7.19`、`17.12.0` 的 Android arm64 版本。
- `.venv/`：已在新路径下重建，验证 `frida==16.0.19`、`frida-tools==12.3.0`、`requests==2.32.4`、`pytest==9.0.2` 可用。
- `scripts/frida-device.sh`：保留。
- `scripts/validate-mermaid.mjs`：保留，但 Node 依赖尚未重建。
- `pyproject.toml`、`uv.lock`：保留，可重建 Python 环境。
- `package.json`、`package-lock.json`：保留，可重建 Node 环境。
- `Makefile`：保留。
- `tests/`：保留，含 unit/e2e/uat。

### 有意不迁移或未重建

- 旧 `.venv/`：未复制，已在新路径重建。
- 旧 `node_modules/`：未复制，体积约 502M，可用 `npm ci` 重建。
- `.pytest_cache/`：未迁移。

### 可清理噪声

迁移后仍可见少量缓存文件：

- `.DS_Store`
- `__pycache__/`

这些不是知识资产，也不是运行必需。建议在下一轮清理中删除并确保 `.gitignore` 覆盖。

## 父 Workflow 的当前边界

父 workflow 当前应做：

1. 定义目标、授权边界、UAT 和 Green。
2. 识别目标平台与运行时。
3. 建立证据台账和 Mermaid 任务树。
4. 路由到 Android / JS / Windows / Unity 子 workflow。
5. 维护通用红灯分类、复现阶梯、迁移状态和 Radar 反馈。

父 workflow 当前不应做：

1. 直接写 Android ADB、JADX、Frida Java、Unidbg 的操作细节。
2. 把 Android 课程案例路径写进总编排主流程。
3. 把一次 Android 成功经验宣称为跨平台能力。
4. 在 JS 子 workflow 没 forward-test 前，大量上提具体 Skills。

## 下一步建议

1. 创建父级 `references/` 与 `templates/`：
   - `references/red-light-taxonomy.md`
   - `references/reproduction-ladder.md`
   - `references/static-dynamic-loop.md`
   - `templates/evidence-ledger-template.md`
   - `templates/mermaid-evidence-tree-template.md`
2. 小幅增强 `skills/reverse-workflow-orchestrator/SKILL.md`，只加入路由和证据约束，不复制 Android 细节。
3. 选择图灵 JS 模块的一个小案例，验证父 workflow 的抽象是否真能落到 JS。
4. 再决定哪些 Android reference/template 可以正式上提。

## 状态标记

```text
asset-audit: structural-green
android-subworkflow: migrated-and-runtime-partial-green
parent-orchestrator: draft
node-tooling: rebuild-pending
cross-platform-forward-test: pending
```

