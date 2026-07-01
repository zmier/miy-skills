---
date: 2026-06-20
type: reference
status: structural-green
scope:
  - workflow-android-reverse
  - tdd
  - regression
---

# Android Reverse Workflow TDD 与回归体系

## 一句话

Android 逆向 workflow 的 TDD 不是只测 Python 函数，而是把“以终为始”的验收目标拆成可证伪的 Red，再用最小 Green 推进：

```text
目标接口/目标语料
-> 验收契约
-> 观察链 smoke
-> 参数/设备态/网络态 Red
-> 最小修复或替代路线
-> 回归测试
-> 反哺 Skill / reference / template
```

## 三圈测试

| 圈层 | 位置 | 责任 | 不负责 |
|---|---|---|---|
| Workflow | `workflow-android-reverse/tests` | Skill 契约、通用脚本、route ladder、能力边界 | 个案 raw 数据 |
| Miku | `00 信息/工具/alib-miku-sync/tests` | 菜单、runtime 软链、工作环境状态、通知入口 | 业务算法正确性 |
| TASK | 课程/项目 TASK 内 | 真实目标、SQLite 队列、业务 UAT、证据日志 | 通用规则本体 |

三圈之间按“证据上提”协作：

```text
TASK 发现真实 Red
-> TASK log 保存证据
-> Workflow 抽象规则
-> Miku 若涉及工具运行面板，则补状态/按钮/通知
-> 三圈各自补测试
```

## 测试分层

### Unit

目标：不需要真机、不请求服务端，验证稳定逻辑。

示例：

```text
crypto fixture
Skill 文本契约
route ladder 文案
mitm addon 过滤逻辑
gnirehtet/tun0 状态判断
SQLite schema / enqueue / assemble
窗口学习器纯函数
```

### E2E

目标：验证本机工具链和脚本入口，但不消耗业务接口。

示例：

```text
Frida 主机版本与 frida-compile
mitmproxy 脚本 status/start dry-run
JADX / IDA / Unidbg 工具链 smoke
miku runtime 软链入口
dashboard/status JSON 可读
```

### UAT

目标：验证真实 Android runtime 与授权业务动作。

示例：

```text
ADB 单设备
Root / Magisk / frida-server
目标 App 进程
目标小程序 XRiverActivity
App 内 RPC smoke
单条业务请求 smoke
小窗口采集 smoke
crash/network/env red light 恢复
```

UAT 可以写成半自动脚本，但必须明确：

```text
是否会重启 App；
是否会消耗服务端窗口；
是否需要人工登录/验证码/授权；
是否保存 raw 数据；
是否会修改设备态。
```

## Red 类型到测试

| Red | 最小测试 |
|---|---|
| 抓不到目标包 | capture readiness smoke + 网络通道候选树 |
| 系统代理不可见 | bridge/RPC/mobilegw/长连接识别 UAT |
| Frida attach 失败 | instrumentation smoke |
| App native crash | runtime crash sentinel UAT |
| 小程序白屏/加载不出 | runtime network smoke + gnirehtet log guard |
| 业务返回 1009 | 服务端窗口/设备态对照实验，禁止混进环境失败 |
| 评论树 partial | 分接口 SQLite 状态与 component_status 单元/fixture |
| 长跑不推进 | dashboard 状态、bucket quota、worker checkpoint 测试 |

## 默认命令

Workflow 自身：

```text
make test-unit
make test-e2e
make test
```

Miku 运行面板：

```text
make -C "<alib-miku-sync>" test-unit
make -C "<alib-miku-sync>" test-e2e
make -C "<alib-miku-sync>" test-uat
```

真实 TASK 工程：

```text
make test          # 不碰真机业务窗口的全部可自动测试
make test-unit     # 本地 fixture / SQLite / 纯函数
make test-e2e      # 脚本入口 / 汇总状态 / dashboard
make test-uat      # 需要真机或人工确认的 smoke，默认可只输出清单
```

## 反哺规则

当真实项目修复了一个红灯，要按这个格式上提：

```text
之前 workflow 缺什么：
本轮 TASK 观察到什么 Red：
最小 Green：
补到哪个 Skill/reference：
补了哪些测试：
哪些证据仍留在 TASK：
迁移状态：structural-green / forward-test-green
```

## 不允许的测试污染

```text
不把真实 raw 响应放进 workflow tests；
不让默认 make test 发送真实业务 RPC；
不把服务端 1009 归因到 Frida/网络，除非有证据；
不把 App crash 归因到业务参数，除非有 crash 证据；
不让 miku 测试依赖某个具体业务 ID；
不让 TASK 脚本写死个人机器路径，除非该 TASK 明确是本机探索证据。
```

## 完成标准

一次体系级改动完成时，至少要有：

```text
1. 对应圈层的测试文件或 Manual UAT 清单；
2. 可执行命令；
3. TASK log 中的 ReAct 记录；
4. workflow / miku / TASK 的边界说明；
5. 已运行测试结果；
6. 未运行测试的原因。
```
