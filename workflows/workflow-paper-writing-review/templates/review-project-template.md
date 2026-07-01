---
type: template
name: review-project-template
status: draft
---

# Review Project Template

## 推荐目录

```text
review-project/
├── README.md
├── PROJECT_INDEX.md
├── sources/
├── manuscript/
├── notes/
├── review/
└── workflow-feedback/
```

## 目录职责

- `sources/`：邀请邮件、系统页面抓取、表单字段说明等来源材料。
- `manuscript/`：稿件 PDF/HTML/补充材料等本地阅读材料。
- `notes/`：人工审读笔记、问题清单、方法核查记录。
- `review/`：人工撰写的审稿意见草稿与最终提交前版本。
- `workflow-feedback/`：可回流 workflow 的抽象发现，不保存保密正文。

## README 必备字段

| 字段 | 内容 |
|---|---|
| journal |  |
| manuscript_id |  |
| title |  |
| deadline |  |
| editor |  |
| status |  |
| source_materials |  |
| submission_form |  |
| sensitive_boundaries |  |

## 边界规则

- 不公开 `sources/` 中的单次访问链接、登录链接、URL_MASK 或系统敏感参数。
- 不把稿件正文、作者身份或具体审稿意见正文写入 workflow 本体。
- workflow 只接收目录结构、台账字段、质量维度和通用流程规则。

