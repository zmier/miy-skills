# TASK01 说明：RESSET Interface-First Replay

## 背景

在基金经理研究 TASK04 中，RESSET 下载技能暴露出一个可复用工程问题：是否能把当前的 “Playwright/CDP + 页面内 JS + UI 下载中心” 路线，扩展为 “接口优先，UI 兜底” 的 hybrid 模式。

这属于 `$resset-download` 的技能工程，不应长期留在单个研究项目中。

## 目标

建立 `$resset-download` 的 interface-first replay 证据链：

```text
1. read-only metadata replay: dataSearch.jsp
2. download center listing replay: downloadTaskUser.action
3. task creation replay: dataSearch.action direct POST
4. zip retrieval replay: /verifyDownload?token=<tid>
5. SKILL.md 反哺：仅在 Green 后写入默认或 experimental 路线
```

## 上游证据

- 基金经理研究 TASK04 的 RESSET 可行性初探。
- `$workflow-js-reverse` 的 request construction ledger 方法。
- `$handle-interactive-verification` 的验证码生命周期和超级鹰单次候选识别规则。

## 产物

- `outputs/resset_direct_interface_replay_feasibility.md`
- `acceptance-contract.md`
- `logs/log.md`
- 后续如果进入实现，可新增 `scripts/` 中的 preflight/replay 辅助脚本。

## Done 标准

- read-only GET replay 可稳定复现，且有登录失效/回退分类。
- direct POST 创建小样本任务通过 UAT，或明确记录红灯原因。
- zip retrieval 通过 `PK` magic 和 unzip 清单验证，或明确记录仍需 browser download event。
- `$resset-download/SKILL.md` 只接受已 Green 的规则；未 Green 的保留为 experimental / TODO。

## 人工关口

- CAPTCHA 自动识别前必须通过 `$handle-interactive-verification` preflight。
- 若超级鹰不可用，必须人工填写验证码后继续。
- 不允许循环刷新验证码、批量识别或绕过 RESSET 权限/下载中心。
