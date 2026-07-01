---
name: ths-drawline-annotation
description: ths-skill 的子 Skill。用于在授权环境内读取、生成、清理同花顺 K 线 DrawLine_New XML 标注/画线，支持文字工具、标注气泡、矩形、水平线、上涨箭头、下跌箭头，并保留 dry-run、备份、原生加载 UAT 与恢复规则。
---

# THS DrawLine Annotation

## 适用边界

使用本 Skill 处理：

```text
~/Library/Containers/cn.com.10jqka.macstock/Data/<accountDir>/DrawLine_New/<marketCode>_<stockCode>/<periodCode>_C09C8.xml
```

只处理本地画线/标注文件。不要修改交易、账户、登录、风控或服务端数据。

## 必读 Reference

执行前读取父目录：

```text
../../references/drawline-schema.md
../../references/source-provenance.md
```

## 脚本

```text
scripts/write_drawline_annotation.py
scripts/manage_drawline_annotations.py
```

默认行为：

```text
write_drawline_annotation.py 默认 dry-run，只有 --write 才写盘；
manage_drawline_annotations.py remove-text 默认 dry-run，只有 --write 才删除；
写盘前自动备份 .bak-YYYYMMDD-HHMMSS。
```

## 支持类型

| kind | LineName | LineType | 点数 | 状态 |
|---|---|---:|---:|---|
| `text` | `文字工具` | `67` | 2 | native load UAT confirmed |
| `note` | `标注` | `68` | 2 | dry-run structure confirmed |
| `hline` | `水平线` | `54` | 1 | dry-run structure confirmed |
| `rect` | `矩形` | `20` | 2 | dry-run structure confirmed |
| `up-arrow` | `上涨箭头` | `21` | 1 | dry-run structure confirmed |
| `down-arrow` | `下跌箭头` | `40` | 1 | dry-run structure confirmed |

## List

查看某支股票日 K 标注：

```bash
scripts/manage_drawline_annotations.py \
  list \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384
```

查看原始 KeyPoint：

```bash
scripts/manage_drawline_annotations.py \
  list \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --verbose
```

## Write

文字工具：

```bash
scripts/write_drawline_annotation.py \
  --kind text \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --date 20251028 \
  --price 40.22 \
  --open-price 31.20 \
  --text "脚本文字"
```

标注气泡：

```bash
scripts/write_drawline_annotation.py \
  --kind note \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --anchor-date 20260622 \
  --anchor-price 195.55 \
  --anchor-open-price 195.55 \
  --box-date 20260526 \
  --box-price 193.99 \
  --box-open-price 92.00 \
  --box-xdata -18 \
  --text "关键警讯"
```

矩形：

```bash
scripts/write_drawline_annotation.py \
  --kind rect \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --date 20260212 \
  --price 32.16 \
  --open-price 32.00 \
  --end-date 20260427 \
  --end-price 51.91 \
  --end-open-price 47.83 \
  --end-xdata 45
```

水平线：

```bash
scripts/write_drawline_annotation.py \
  --kind hline \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --date 20250825 \
  --price 36.38 \
  --open-price 34.58
```

上涨/下跌箭头：

```bash
scripts/write_drawline_annotation.py \
  --kind up-arrow \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --date 20250904 \
  --price 27.21 \
  --open-price 30.89
```

```bash
scripts/write_drawline_annotation.py \
  --kind down-arrow \
  --market-code 33 \
  --stock-code 301217 \
  --period-code 16384 \
  --date 20250825 \
  --price 37.03 \
  --open-price 34.58
```

## 二点图形规则

当前观察：

```text
P1: XData=YYYYMMDD, XTime=0
P2: XData=相对 offset/index, XTime=YYYYMMDD
```

因此 `note` / `rect` 如果第二点日期不同于第一点，必须显式传入：

```text
--second-xdata
--end-xdata
--box-xdata
```

脚本在缺少该字段时应拒绝执行，不要猜测。

## UAT

写入流程：

```text
dry-run -> 检查 entry -> 加 --write -> 重启 App -> 进入目标股票/周期 -> list 或 remove-text 验证/清理
```

当前已确认最小加载动作：

```text
restart app -> App native load DrawLine_New XML
```

若需要用户重启 App 或观察 UI，使用 `feishu-notify`。
