---
name: extract-course-case-workflow
description: 将 Android 逆向课程案例、老师脚本和课堂笔记迁移为可复用 workflow/skills 能力。用于判断某个课程脚本在当前环境是否仍可运行、它依赖了哪些历史假设、哪些步骤应沉淀为通用 Skill/reference/assets/template，哪些只能保留为案例证据，并为总编排回写能力注册表、TASK 评测和后续补充计划。不得把失效脚本包装成已验证能力。
---

# 课程案例迁移评估

## 目标

把“老师脚本”拆成可验证假设和可迁移能力。课程脚本不是天然 workflow；只有经过当前环境预检、失败分层和泛化抽象后，才能进入 Skills。

## 工作流

1. 收集课程笔记、脚本、APK、工具包和原始运行前提。
2. 为每个脚本登记：目标、输入、输出、依赖环境、是否含账号/Token/时间/IP/服务端状态假设。
3. 低频预检脚本是否仍可运行；失败时记录 HTTP/异常/服务端页面，不强行修成 Green。
4. 判断失败原因：本地环境、App 版本、服务端变更、证书/代理、风控/WAF、授权边界。
5. 将脚本拆为三类：
   - `integrate-now`：抽象成通用 Skill/reference/assets；
   - `case-evidence`：保留在 TASK，作为历史案例和对照；
   - `defer`：需要后续真机/账号/环境或更明确边界。
6. 对 `integrate-now` 只迁移方法，不迁移案例常量、真实 Header、Cookie、Token 或过期请求。
7. 更新能力注册表、相关 Skill 的参考资料和测试；若能力未真机验证，状态写 `learning/experimental`。
8. 在课程 TASK 的 LOG 中写清：哪些老师脚本已转化、哪些未转化、为什么。

## 输出

- `course-script-migration.md`：脚本清单、当前预检、迁移分类和理由；
- 更新后的 Skill/reference/assets；
- 对应单元测试或 quick_validate 结果；
- 能力注册表状态变化；
- 下一轮要复现的最小 TASK。

## 完成标准

- A：至少一个课程脚本被抽象为通用模板，并通过 workflow 测试；
- B：脚本因服务端或环境变化不可复现，但已明确哪些知识可迁移；
- C：授权、账号、验证码或真实业务边界阻止继续，只保留案例证据。
