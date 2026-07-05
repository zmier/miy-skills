# Table Visual QC

- date: 2026-06-20
- scope: 表 1 至表 18 的页面级视觉复核；跨页表做边界确认；关键风险表 11 做重点核验。
- limitation: 不是逐单元格人工录入式校对；复杂回归表的精确列对齐仍应回查 PDF page image。

| table | pdf pages | visual status | note |
|---|---:|---|---|
| 表 1 变量定义表 | 8 | page-level checked | page-level checked; existing Markdown table retained; cell-level PDF audit not repeated |
| 表 2 描述性统计结果 | 9 | page-level checked | page-level checked; table present on page 9; raw text matches visible table structure |
| 表 3 事前趋势检验结果 | 10 | page-level checked | page-level checked; table present on page 10; key event-study rows visible |
| 表 4 多元回归分析结果 | 11 | page-level checked | page-level checked; table present on page 11; main DID coefficient visible |
| 表 5 堆叠 DID 估计 | 12 | page-level checked | page-level checked; table present on page 12; stack DID coefficient visible |
| 表 6 匹配回归的结果 | 14, 15 | page-level checked | cross-page boundary checked on pages 14-15; table tail continues on page 15 |
| 表 7 排除共同决定因素干扰的检验 | 15, 16 | page-level checked | cross-page boundary checked on pages 15-16; table starts below table 6 tail |
| 表 8 Oster 检验结果 | 16 | page-level checked | page-level checked; compact Oster table visible on page 16 |
| 表 9 替换变量衡量方式的检验 | 17 | page-level checked | page-level checked; table present on page 17 |
| 表 10 事件公司主动披露违规的短期市场反应 | 18 | page-level checked | page-level checked; CAR table visible on page 18 |
| 表 11 基于声誉竞争机制的检验结果 | 19, 20 | page-level checked | cross-page visual checked on pages 19-20; PDF table shows PosCAR[-10,10] is -0.0028 and NegCAR[-10,10] is -0.0168***, which conflicts with author prose |
| 表 12 基于市场压力机制的检验结果 | 21 | page-level checked | page-level checked; market pressure table visible on page 21 |
| 表 13 基于信息传导机制的检验结果 | 22, 23 | page-level checked | cross-page/page-level checked on pages 22-23; table appears on page 23 after mechanism prose |
| 表 14 基于事件公司行业地位的检验结果 | 24, 25 | page-level checked | cross-page boundary checked on pages 24-25; table starts page 24 and continues page 25 |
| 表 15 基于事件公司披露违规主动性的检验结果 | 26 | page-level checked | page-level checked; table visible on page 26 |
| 表 16 基于事件公司违规严重程度的检验结果 | 27, 28 | page-level checked | cross-page boundary checked on pages 27-28; table starts page 27 and continues page 28 |
| 表 17 基于公司外部融资依赖度的检验结果 | 29 | page-level checked | page-level checked; table visible on page 29 |
| 表 18 基于行业竞争程度的检验结果 | 30, 31 | page-level checked | cross-page boundary checked on pages 30-31; table starts page 30 and continues page 31 |

## Key Finding

表 11 是本轮视觉复核发现的高价值问题：PDF 表格第三列显示 `Peerdumy_PosCAR[-10,10]×POST = -0.0028`，而 `Peerdumy_NegCAR[-10,10]×POST = -0.0168***`。这与作者正文声称 `PosCAR` 三组均显著、`NegCAR` 三组均不显著不一致。后续论证树与审稿 issue 应把它作为“机制证据与文字叙事不一致”的候选问题。
