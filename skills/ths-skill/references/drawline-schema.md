# THS DrawLine Schema

## 路径

```text
~/Library/Containers/cn.com.10jqka.macstock/Data/<accountDir>/DrawLine_New/<marketCode>_<stockCode>/<periodCode>_C09C8.xml
```

样本：

```text
Data/mx_184295493/DrawLine_New/33_301217/16384_C09C8.xml
```

## 编码

```text
GB2312
```

根节点：

```xml
<DrawLineData>
  <DrawLine ...>
    <KeyPoint ...></KeyPoint>
  </DrawLine>
</DrawLineData>
```

## DrawLine 字段

| 字段 | 说明 |
|---|---|
| `LineName` | UI 工具名 |
| `LineType` | 工具类型代码 |
| `Option` | 绘制选项 |
| `TextContent` | 文本内容，通常以 `\r\n\r\n` 结尾 |
| `Color` | 线/框颜色 |
| `WordClr` | 文字颜色 |
| `BKColor` | 背景色 |
| `Width` | 线宽 |
| `WordInfo` | 字体或文字布局信息 |
| `Show` | 是否显示，当前样本为 `1` |

## KeyPoint 字段

| 字段 | 说明 |
|---|---|
| `XData` | 第一通常为日期，后续点常为相对 offset/index |
| `XTime` | 第一通常为 `0`，后续点常为实际日期 |
| `YData` | 价格/纵轴坐标 |
| `OpenPrice` | 该点对应 K 线 open 或参考价格 |
| `YDataType` | 当前样本固定 `20480` |
| `Active` | 当前样本固定 `1` |

读取日期：

```text
if XTime != 0:
  date = XTime
else:
  date = XData
```

## 支持图形

| kind | LineName | LineType | Option | 点数 | 语义 |
|---|---|---:|---|---:|---|
| `text` | `文字工具` | `67` | `0010` | 2 | P1 文本锚点，P2 文本框点 |
| `note` | `标注` | `68` | `0010` | 2 | P1 被标注 K 线/价格，P2 标注框/引线位置 |
| `hline` | `水平线` | `54` | `0000` | 1 | P1 价格线锚点 |
| `rect` | `矩形` | `20` | `0010` | 2 | 两个对角点 |
| `up-arrow` | `上涨箭头` | `21` | `0000` | 1 | 单点箭头，方向由类型决定 |
| `down-arrow` | `下跌箭头` | `40` | `0000` | 1 | 单点箭头，方向由类型决定 |

## Market 映射

| marketCode | App Market | 样本 | 状态 |
|---:|---|---|---|
| `17` | `USHA` | `17_601991`、`17_688585` | confirmed |
| `33` | `USZA` | `33_301217`、`33_002594` | confirmed |
| `16` | 上证指数/沪市指数候选 | `16_1A0001` | candidate |
| `32` | 深市指数候选 | `32_399006` | candidate |
| `48` | 北交所/北证候选 | `48_883957` | candidate |
| `22` | 待确认 | `22_600745` | open |

## Period 映射

| periodCode | 样本 | 状态 |
|---:|---|---|
| `16384` | 多数股票日 K 样本，含 UAT | confirmed as current UAT period |
| `20481` | 多个股票另一周期样本 | candidate |
| `24577` | 指数周期样本 | candidate |
| `24579` | 指数周期样本 | candidate |
| `12293` | `688498` 样本 | candidate |

## 加载规则

当前最小 Green：

```text
脚本写入 XML -> 重启 App -> App 原生加载 DrawLine_New XML
```

待进一步验证：

```text
切股加载；
切周期加载；
当前页刷新；
文件变化自动刷新；
云同步覆盖风险。
```
