# Inputs

本 TASK 不复制额外敏感正文，直接引用 case-local evidence bundle。

| 文件 | 相对路径 | 角色 |
|---|---|---|
| 稿件 Markdown | `../../../inputs/manuscript.md` | primary evidence，用于恢复作者贡献链 |
| 欣媛审稿意见 txt | `../../../inputs/xinyuan-review.txt` | primary evidence，用于识别 major concerns |
| 欣媛审稿意见 docx | `../../../inputs/xinyuan-review.docx` | source preservation |
| 源项目审稿笔记 | `../../../inputs/source-review-notes.md` | context |
| 既有 argument map | `../../../outputs/xinyuan-review-argument-map.md` | prior case output |
| 既有 skill gap | `../../../outputs/skill-gap-analysis.md` | prior case output |
| 对话洞见 001 | `../../../../references/dialogues/001-学术论文的双层论证与汇合箭头.md` | method source |
| 对话洞见 002 | `../../../../references/dialogues/002-论文的顶层发表正当性论证.md` | method source |
| 对话洞见 004 | `../../../../references/dialogues/004-论效题审稿与自下而上的论证树.md` | method source |

## 读取顺序

1. 先读 dialogue 001/002/004，固定 X1/X2/Y 论证树主轴；
2. 再读既有 `xinyuan-review-argument-map.md`，避免重复从零提炼；
3. 再回到稿件和欣媛意见，补证据和定位；
4. 最后产出 TASK-local outputs，不直接改父 workflow。
