# Android Reverse Workflow Tests

## 分层

```text
tests/unit
  不连真机，不请求服务端。验证 Skill 契约、纯函数、fixture 和文档协议。

tests/e2e
  验证本机工具链和脚本入口。默认不发送真实业务请求。

Manual UAT
  放在具体 TASK 中。需要真机、登录、服务端窗口、App 页面或人工操作的验证不进入默认 make test。
```

## 常用命令

```bash
make test-unit
make test-e2e
make test
```

## 与真实 TASK 的关系

真实项目的业务验收留在项目 TASK，例如 TASK27 的：

```text
TASK27-回答详情请求池与采集调度/docs/TESTING_PROTOCOL.md
```

workflow tests 只保留可迁移的能力契约，不保存真实业务 raw、账号态、设备态、接口响应和长跑日志。
