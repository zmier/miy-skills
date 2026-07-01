# 真实项目反哺追溯

这个文件记录真实项目、探索性课程项目和对话洞见如何反哺 `workflow-android-reverse`。

普通领域 Skill 的主流程只保留去个案化规则；真实账号、业务 ID、响应、日志、服务端反馈细节和具体操作过程留在对应 TASK。

## 记录模板

```text
### TASKxx - 能力名

- 项目/案例：
- 对应 TASK：
- 触发 Red：
- 最小 Green：
- 影响位置：
- 证据角色：
- 清洗与泛化：
- 当前状态：
- 迁移/回归状态：
```

## Day27 网络与抓包专题探索项目

### TASK34 - Xposed/LSPosed P1 module-loaded 服务化路线

- 项目/案例：授权 Android 业务网络项目中，从 Frida App 运行态代发升级到 Xposed/LSPosed 长驻服务化的 P0-P1。
- 对应 TASK：`笔记包/Day 27及以后/网络与抓包专题/PROJECT-Android目标业务网络通道识别/tasks/TASK34-XposedSekiro运行态服务化`。
- 触发 Red：
  - Frida 长会话在长跑中出现 native crash / `frida-agent` 参与崩溃链路；
  - 需要验证 A5/R4-X 路线是否能稳定加载到目标 App 运行态；
  - 初始设备只有 Magisk，没有 LSPosed；
  - Magisk Zygisk 未启用；
  - 手写 LSPosed `modules_config.db` 会遇到 `lspd` 持有、WAL/SHM、SELinux、APK 重装后路径过期等问题；
  - 模块会加载到目标 App 多个进程，后续 action server 存在重复注册风险。
- 最小 Green：
  - 先写 P1 Red 文档和静态契约测试；
  - 构建最小 Xposed 模块，只记录 `module-loaded` 和 `classloader-ready`；
  - 安装 LSPosed Zygisk 并启用 Zygisk；
  - 使用 LSPosed Manager 启用模块并勾选目标 App scope；
  - logcat 中出现 `LSPosed-Bridge: Loading class ...`、`module-loaded`、`classloader-ready`；
  - restart smoke 仍能复现模块加载。
- 影响位置：
  - `skills/xposed-sekiro-runtime-dispatch/SKILL.md`；
  - `skills/xposed-sekiro-runtime-dispatch/references/xposed-lsposed-p1-sop.md`；
  - `SKILL.md` 的 A5 服务化封装路线说明。
- 证据角色：`field-primary / workflow-gap / forward-test-green`。
- 清洗与泛化：
  - 不写入真实业务接口、账号、响应或目标业务数据；
  - 保留通用 P1 状态机、构建/安装/scope/smoke 顺序、Red 分类和 LSPosed Manager 优先策略；
  - 把目标 App 多进程加载泛化为 P2 `ProcessRouter` 前置要求。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：`forward-test-green for P1`。已在真实设备完成一次 P1 module-loaded smoke；P2 action server 尚待新的 forward test。

### TASK34-03 - A5/Xposed 首个真实业务 action P3 smoke

- 项目/案例：授权 Android 业务网络项目中，把已由 Frida RPC 跑通的单个 App 内业务 RPC 迁移为 Xposed action server 的 allowlist action。
- 对应 TASK：`笔记包/Day 27及以后/网络与抓包专题/PROJECT-Android目标业务网络通道识别/tasks/TASK34-XposedSekiro运行态服务化/subtasks/TASK34-03-AnswerDetailActionSmoke`。
- 触发 Red：
  - Frida RPC 单次可用，但长跑稳定性不足，需要迁移到 A5/Xposed 长驻服务化；
  - 初始 Xposed action worker 未兜底 `Throwable`，真实 smoke 出现空响应；
  - action 线程默认 ClassLoader 找不到目标 App 类；
  - RPC 接口反射 exact signature 不稳定；
  - 业务请求体若不完全对齐 Frida oracle，会触发 RPC/业务错误；
  - transport 成功不等于业务成功，删除/失效业务样本不能包装成 `ok=true`。
- 最小 Green：
  - 先写 P3 action contract 和 unit Red；
  - 只迁移一个 allowlist action；
  - 默认 dry-run 不触发业务请求；
  - `real=1` 单条低频 smoke 能在 App 运行态调用目标 RPC；
  - 从 Xposed entry 注入目标 App ClassLoader；
  - 反射调用采用兼容 overload 扫描；
  - 请求体完全对齐 Frida 成功版 oracle；
  - 有效样本返回核心业务字段；
  - 业务失败样本返回 `ok=false`，不误报成功。
- 影响位置：
  - `SKILL.md`：A5 P3 单 action smoke、四层排错、transport/business ok 分离；
  - `skills/xposed-sekiro-runtime-dispatch/SKILL.md`：P3 单 Action 业务 Smoke SOP；
  - `tests/unit/test_skill_contracts.py`：A5 P3 迁移规则契约测试。
- 证据角色：`field-primary / workflow-gap / forward-test-green for P3 single-action`。
- 清洗与泛化：
  - 不写入真实业务接口名、真实 answerId、真实响应正文、账号或设备字段；
  - 把个案错误泛化为 action server、ClassLoader、RPC proxy、requestData、business-ok 五类 Red；
  - 把 Frida 成功 agent 抽象为 oracle，不把具体 JS/Python 代码复制进 workflow；
  - 把业务失败样本抽象为 transport/business 成功语义分离。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：`forward-test-green for one P3 action`。已在真实设备完成一次 P3 单 action smoke；多 action、请求池 adapter 和 miku 长跑接入仍为 `forward-test-pending`。

### TASK27-16 - App 运行态长跑抗崩溃、会话重建与人类通报

- 项目/案例：授权 Android 业务网络与 Frida RPC 语料采集探索项目。
- 对应 TASK：`笔记包/Day 27及以后/网络与抓包专题/PROJECT-Android目标业务网络通道识别/tasks/TASK27-回答详情请求池与采集调度/subtasks/TASK27-16-长跑抗崩溃与会话重建机制`。
- 触发 Red：
  - App 内 RPC 单次可用，但长跑中会出现 Frida session 丢失、`script has been destroyed`、App/native crash、环境红灯、业务服务端限制和设备态重置后等待登录等多类状态；
  - 早期 workflow 容易把这些状态混成一个 `failed`，导致队列语义、恢复动作和人类介入边界不清楚。
- 最小 Green：
  - 当前 item 可在 session 丢失时回滚为 `pending`；
  - 已成功 item 保留 checkpoint；
  - worker 可重建 Frida session 后继续；
  - runtime crash sentinel 能把 App/zygote crash 升级为环境红灯；
  - 人类通知只在环境红灯、修复失败、等待登录/授权确认等关键节点触发并限频；
  - dashboard 只展示摘要，不直接铺机器日志。
- 影响位置：
  - `SKILL.md`：业务网络与语料项目编排、服务端窗口与设备态、Evidence Promotion；
  - `skills/build-android-rpc-data-corpus/SKILL.md`；
  - `skills/build-android-rpc-data-corpus/references/batch-safety-policy.md`；
  - `skills/diagnose-android-instrumentation/SKILL.md`。
- 证据角色：`field-primary / dialogue-insight / workflow-gap`。
- 清洗与泛化：
  - 不写入目标 App、账号、业务 ID、真实接口名、真实响应或固定配额；
  - 泛化为 App 运行态长跑状态机：runtime heartbeat、session lifecycle、business bucket、human gate、human notify、dashboard；
  - 把“长会话复用”和“实体状态隔离”拆成两个层级，避免用每条请求重建 session 来换取表面隔离。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：`forward-test-pending`。本案例已提供回归样本，但仍需在新的 App 运行态语料项目中验证迁移性。

### TASK34-05/P4 - Xposed transport 接入请求池

- 项目/案例：授权 Android 业务网络项目中，把已通过 P3 的 Xposed action 接入既有 SQLite 请求池和批量 worker。
- 对应 TASK：`笔记包/Day 27及以后/网络与抓包专题/PROJECT-Android目标业务网络通道识别/tasks/TASK34-XposedSekiro运行态服务化`，重点证据为 `outputs/p4/P4-xposed-transport-smoke-report.md` 和 `outputs/p4/P4-xposed-production-small-window-report.md`。
- 触发 Red：
  - P3 单 action smoke 已 Green，但还不能证明请求池、分页、raw/simplified 保存、失败分类和断点续跑能在 Xposed transport 下保持一致；
  - 需要避免为了接入 Xposed 重写业务 worker，导致队列语义和 Frida oracle 丢失；
  - 小窗口前 action server、action list 和业务样本必须重新确认。
- 最小 Green：
  - `XposedActionTransport` 接入既有 worker；
  - worker 通过显式 `--transport xposed` 切换，不隐式替换 Frida；
  - `answer_detail` 与 `top_comment` 小窗口真实请求通过；
  - SQLite `done/pending/skipped` 语义保持；
  - raw/simplified 保存策略不因 transport 改变；
  - 业务请求仍由 App 运行态发出，Python 只做调度。
- 影响位置：
  - `SKILL.md`：A5 P4 request-pool adapter；
  - `skills/xposed-sekiro-runtime-dispatch/SKILL.md`：P4 请求池 Transport 接入；
  - `skills/xposed-sekiro-runtime-dispatch/references/xposed-sekiro-contract.md`：P4 Green 和 UAT。
- 证据角色：`field-primary / workflow-gap / forward-test-green for current field case`。
- 清洗与泛化：
  - 不写入真实 action、业务 ID、operationType 或响应；
  - 泛化为“transport adapter 层替换 App 内代发通道，业务 worker 状态机保持不变”；
  - 明确 Frida oracle/fallback 的边界。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：`current-case forward-test-green / new-case forward-test-pending`。

### TASK34-P5 - Xposed 内部受控状态变更 Action

- 项目/案例：授权 Android 业务网络项目中，把设备态/缓存态恢复能力从宿主侧脚本迁移为 Xposed 内部受控 action。
- 对应 TASK：`笔记包/Day 27及以后/网络与抓包专题/PROJECT-Android目标业务网络通道识别/tasks/TASK34-XposedSekiro运行态服务化`，重点证据为 `outputs/p5/P5内部BigKnife验收报告.md` 与 TASK34 log 中 P5.4 miku Big-Knife 模式接入记录。
- 触发 Red：
  - 服务端 1009 与设备态/安装实例/安全 SDK 缓存相关；
  - 宿主侧状态重置可作为恢复手段，但不够运行态内聚；
  - 状态变更 action 风险高，不能和普通业务 action 同等对待；
  - 状态重置后可能出现登录页、网络红灯或业务 runtime 未就绪。
- 最小 Green：
  - 提供 `prepare` 与 `execute` 两段；
  - `execute` 需要显式 confirm 和近期 Red 证据；
  - action 本身不触发业务 RPC、不返回敏感字段；
  - 执行后必须拉起目标 runtime 并做 post-smoke；
  - miku/adaptive 层可配置 `external` 或 `xposed-internal`，并声明 fallback。
- 影响位置：
  - `SKILL.md`：A5 P5 supervised state-changing action；
  - `skills/xposed-sekiro-runtime-dispatch/SKILL.md`：P5 受控状态变更 Action；
  - `skills/xposed-sekiro-runtime-dispatch/references/xposed-sekiro-contract.md`：P5 Green 和 UAT。
- 证据角色：`field-primary / operational-safeguard / workflow-gap`。
- 清洗与泛化：
  - 不写入真实 DID、apdidToken、文件路径、App 包名或业务响应；
  - 泛化为“高危状态变更 action 必须有 prepare/confirm/Red evidence/post-smoke/fallback”；
  - 明确不得用于突破授权边界或服务端明确拒绝。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：`current-case forward-test-green / new-case forward-test-pending`。

### TASK34-P6 - Xposed transport 受监督长跑状态机

- 项目/案例：授权 Android 业务网络项目中，Xposed transport 接入 miku/adaptive supervisor 后开始真实请求池长跑。
- 对应 TASK：
  - `笔记包/Day 27及以后/网络与抓包专题/PROJECT-Android目标业务网络通道识别/tasks/TASK34-XposedSekiro运行态服务化/logs/log.md`；
  - `.../TASK34-XposedSekiro运行态服务化/outputs/p6/P6-Xposed长跑回顾与workflow反哺.md`；
  - `.../TASK27-回答详情请求池与采集调度/subtasks/TASK27-06-自适应限速与Probe恢复/logs/log.md`。
- 触发 Red：
  - P4 小窗口通过后，长跑仍可能被 App crash、目标 runtime 丢失、网络红灯、bucket 串行阻塞、状态文件残留旧错误、服务端窗口和人类登录门打断；
  - dashboard 若只看历史 `lastErrorMessage`，会把正在推进的 worker 误报成失败；
  - 统一 `failed` 无法表达 1009、业务 not-found、transport error、环境红灯、等待人工等不同恢复动作。
- 最小 Green：
  - supervisor 常驻；
  - Xposed transport 请求池真实推进；
  - bucket quota 按接口独立；
  - 每实体 checkpoint；
  - runtime heartbeat、network health、business runtime、human gate 和 post-gate smoke 进入状态机；
  - dashboard 优先读取 worker 进程、DB 更新时间和 action health，再解释历史错误；
  - 新 Red 先写 TASK/log，再决定是否反哺 workflow。
- 影响位置：
  - `SKILL.md`：A5 P6 production long-run；
  - `skills/xposed-sekiro-runtime-dispatch/SKILL.md`：P6 生产长跑状态机；
  - `skills/xposed-sekiro-runtime-dispatch/references/xposed-sekiro-contract.md`：P6 Green 和 UAT。
- 证据角色：`field-primary / dialogue-insight / operational-safeguard / workflow-gap`。
- 清洗与泛化：
  - 不写入真实配额数字、业务数据或设备标识；
  - 泛化为“活体证据优先于历史错误”的 supervisor/dashboard 原则；
  - 保留 `current-case forward-test-green` 与 `new-case forward-test-pending` 的迁移边界。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：`current-case forward-test-green / new-case forward-test-pending`。

### TASK35 - 交互验证与 native 滑块处理

- 项目/案例：授权 Android 业务网络项目中的靶场附加“滑块校验”演练，以及 miku/Xposed 长跑采集中的交互验证恢复链路。
- 对应 TASK：`笔记包/Day 27及以后/网络与抓包专题/PROJECT-Android目标业务网络通道识别/tasks/TASK35-滑块校验演练`。
- 触发 Red：
  - 业务请求池长跑中可能遇到 `1009` / `interactive_verification_waiting`；
  - 验证页会以 App native UI 形式出现，不一定是 H5 DOM 滑块；
  - 旧逻辑遇到交互验证会暂停采集并等待人工；
  - 若只做一次 ADB 坐标滑动，无法沉淀为可迁移的恢复状态机；
  - 滑块处理结果需要通过通知、post-smoke 和请求池继续推进来验收。
- 最小 Green：
  - 先通过 UI dump、截图和运行态观察确认验证页类型；
  - 使用 ADB 输入证明最小可行动作；
  - 迁移为 Xposed App 内 ViewTree 检测和 `MotionEvent` 派发；
  - action server 暴露 `slider_status` 与 `solve_slider`；
  - miku wrapper 增加 slider guard：检测、通知、自动处理、处理结果通知；
  - `interactive_verification_waiting` 分支优先尝试自动处理，成功后清本地等待/冷却并继续采集，失败才暂停等待人工。
- 影响位置：
  - `SKILL.md`：新增“交互验证与滑块处理”专题；
  - `tests/unit/test_skill_contracts.py`：滑块专题契约测试；
  - miku `android-rpc-auto-recovery-wrapper.sh` 与相关 e2e 测试；
  - TASK35 子任务文档和 Xposed 模块实现。
- 证据角色：`field-primary / dialogue-insight / operational-safeguard / workflow-gap`。
- 清洗与泛化：
  - 不写入具体业务名、真实坐标、截图、资源路径、账号、设备 ID 或服务端响应；
  - 把个案动作泛化为“识别验证形态 -> 最小 Green -> 运行态自动处理 -> post-smoke -> 继续采集”的状态机；
  - 明确 H5/WebView/native/无可见 UI 四类验证形态和不同路线；
  - 把自动处理限定在授权靶场、课程练习或明确允许的测试环境内。
- 当前状态：`workflow-integrated / structural-green`。
- 迁移/回归状态：`current-case partial-forward-test-green / new-case forward-test-pending`。当前案例已完成 native 滑块识别、ADB 最小 Green、Xposed action 和 miku 接入；最新 wrapper 分支仍等待下一次真实滑块/交互验证触发后完成端到端 UAT。
