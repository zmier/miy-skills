# 课程驱动 Skill 工程评测

```yaml
课程单元: 论证有效性分析 / 论效题子 workflow
案例: CASE-UAT-260619-论效新题
项目模式: course-case / forward-test
探索问题:
  - workflow-exam-argument-validity 是否能处理未参与提炼的新题
  - Mermaid 论证树与箭头断点表是否能稳定指导成文
阶段终点类型: capability / deliverable
blind阶段:
  独立性等级: limited-blind
  已暴露信息:
    - 已知本 case 存在 reference 解析和范文
    - 已知 final corpus 中包含同题完整资料
  冻结范围:
    - inputs/reference.md
    - inputs/final/2013-10-MBA-勤俭节约过时了.final.md 中的解析、范文、点评
    - inputs/final/FULL-CORPUS.final.md
  冻结的初始假设:
    - 不预设课程解析中的断点就是唯一答案
    - 不预设范文结构就是唯一写法
  是否提前解冻: no
  primary证据:
    - inputs/prompt.md
教师对照:
  解冻材料:
    - inputs/reference.md
  关键差异: pending
探索性反馈:
  field_primary: []
  field_limited: []
  field_hypothesis: []
  field_boundary:
    - 2011 与 2012 OCR 源缺主体内容，不能作为完整 UAT 样本
    - final-with-ocr-caveats 文件可用于 OCR 容错和写法参考，不宜作为题干真值
平行路线:
  决策: not-needed-before-forward-test
  角色: comparison-only
  证据: []
skill变更:
  updated:
    - tests/exam-fixtures.md
    - references/source-provenance.md
    - references/arrow-break-taxonomy.md
    - subworkflows/workflow-exam-argument-validity/references/exam-reading-rules.md
    - CASE-UAT-260619-论效新题/README.md
    - course-driven-skill-engineering/SKILL.md
  created:
    - case-charter.md
    - outputs/course-skill-evaluation.md
    - outputs/UAT.md
    - outputs/reference-comparison.md
    - outputs/skill-change-proposal-concept-relation.md
  rejected: []
可执行资产:
  upstream: []
  optimized: []
  task_only:
    - inputs/final/FULL-CORPUS.final.md
  rejected: []
操作护栏:
  限速: not-applicable
  断点续跑: outputs 四件套可分步生成
  脱敏保存: 本 case 不复制到通用 Skill 主流程
  停止条件: 生成四件套并完成 reference 对照；失败时记录首个失败层
结构回归:
  task_docs: pass
  skill_routes: pass
  provenance: pass
  registry: pass
  roadmap: not-applicable
  log: not-applicable
  skill_body_audit: pass
  cleanup_debt: []
回归:
  source_case: course-example-regression / pass
  existing_cases:
    CASE-J-260110-xinyuan-review: unaffected
迁移:
  target_case: inputs/prompt.md
  status: forward-test-pass
  evidence:
    - case-charter.md
    - inputs/final/README.md
  forward_test_required: true
覆盖率声明: 阶段性
未验证边界:
    - 后续仍需第二个新样本验证稳定性
状态: forward-test-pass
```

## 判断

本 case 已完成课程驱动 Skill 工程的结构准备、一次 blind-run、reference comparison 和轻量反哺：输入语料、冻结边界、评测标准、fixture、provenance、四个 workflow 输出、对照结果与概念关系审查规则均可追溯。

本轮已将 `workflow-exam-argument-validity` 推进为 `forward-test-green`，并把“概念关系审查”写入读题规则和父层断点分类。后续建议再用一道近年真题或模拟题做第二个迁移样本，检查稳定性。
