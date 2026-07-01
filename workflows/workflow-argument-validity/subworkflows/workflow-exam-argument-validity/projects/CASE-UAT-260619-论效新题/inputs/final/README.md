# Final Cleaned Corpus

本目录是 `inputs/_ori` OCR 材料的人工精校/结构化最终版入口。

处理原则：

- 保留题干、解析、范文、习作点评、问题汇总、佳句集萃等对论效 workflow 有用的信息。
- 对源文件缺页的材料标为 `incomplete-source`，不补写不存在的内容。
- 对点评区 OCR 混排但主体可辨识的材料标为 `final-with-ocr-caveats`，后续只作为写法和失分点参考。
- `final-complete` 可直接进入论效 workflow 的 UAT 或集成测试。

## 文件索引

| 文件 | 状态 | 说明 |
|---|---|---|
| `2003-10-MBA-蜜蜂实验.final.md` | `final-with-ocr-caveats` | 主体完整；习作点评和问题汇总处混排明显，已保留原义并标注。 |
| `2004-10-MBA-企业竞争.final.md` | `final-complete` | 主体材料完整，可作为论效 workflow 输入。 |
| `2005-10-MBA-洋快餐.final.md` | `final-complete` | 主体材料完整，可作为论效 workflow 输入。 |
| `2006-10-MBA-企业丑闻.final.md` | `final-with-ocr-caveats` | 主体完整；习作点评区有少量 OCR 混排行，已尽量保留并标注。 |
| `2007-10-MBA-终身制和铁饭碗.final.md` | `final-with-ocr-caveats` | 主体完整；习作点评区有少量 OCR 混排行，已尽量保留并标注。 |
| `2008-10-MBA-孝不是选拔官员的标准.final.md` | `final-complete` | 主体材料完整，可作为论效 workflow 输入。 |
| `2009-10-MBA-民主集中制.final.md` | `final-complete` | 主体材料完整，可作为论效 workflow 输入。 |
| `2010-10-MBA-权威的影响.final.md` | `final-complete` | 主体材料完整，可作为论效 workflow 输入。 |
| `2011-10-MBA-降低个税起征点.incomplete.md` | `incomplete-source` | OCR 源仅含问题汇总和佳句集萃，缺题干、结构、解析、范文等主体内容。 |
| `2012-10-MBA-四不承诺.incomplete.md` | `incomplete-source` | OCR 源仅含题干审读和论证结构开头，缺解析、范文、点评等后续内容。 |
| `2013-10-MBA-勤俭节约过时了.final.md` | `final-complete` | 题干、论证结构、解析、范文、习作点评、问题汇总、佳句集萃均可用。 |

## 建议使用

1. 直接跑 workflow 时，优先使用 `final-complete`。
2. 检查 OCR 容错能力时，可使用 `final-with-ocr-caveats`。
3. `incomplete-source` 只用于提示材料缺失，不用于完整评测。

## 汇总文件

- `FULL-CORPUS.final.md`：按年份合并的完整语料入口。
