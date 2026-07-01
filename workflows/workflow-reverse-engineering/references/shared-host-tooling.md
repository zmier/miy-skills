# Shared Host Tooling

## 目标

父 `workflow-reverse-engineering` 维护跨平台可复用的主机侧工具环境。平台子 workflow 只保留平台专属工具和设备端资产。

## 当前共享工具

| 工具 | 版本策略 | 作用域 |
|---|---|---|
| Frida Python/CLI | `frida==16.0.19`, `frida-tools==12.3.0` | Mac/iOS/Android 主机侧 attach、trace、RPC、process list |
| mitmproxy | `>=11,<13` | 跨平台代理和流量观察 |
| requests | `2.32.4` | 通用 HTTP smoke / helper |

## 与 Android 子 workflow 的边界

Android 子 workflow 仍管理：

- Android 设备端 `frida-server` 下载、安装、启动、停止；
- ADB、root、Magisk、systemless CA、SocksDroid 等 Android 专属路线；
- Android 子 workflow 自身测试。

父 workflow 管理：

- 主机侧 Frida CLI/Python 模块；
- 主机侧 mitmproxy；
- 可被 Mac、Android、JS、Windows 等 workflow 复用的工具版本和入口。

## 使用

```bash
cd "/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-reverse-engineering"
make init
make shared-tool-status
```

常用入口：

```text
.venv/bin/python
.venv/bin/frida
.venv/bin/frida-ps
.venv/bin/frida-trace
.venv/bin/mitmproxy
```

## 反哺来源

本规则来自授权 Mac App 靶场项目：

```text
/Users/narra/Documents/alib/Writer/03 Projects/冒险者工会/PROJECT-MacApp同花顺K线涨停紫色K
```

观察到 Android workflow 已有可用 Frida 主机侧依赖，但该能力不应只归 Android 项目所有；因此上提到父 workflow 共享层。

