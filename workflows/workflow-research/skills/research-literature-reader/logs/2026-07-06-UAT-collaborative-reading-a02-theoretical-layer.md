# 2026-07-06 UAT: collaborative-reading A02 theoretical layer

## UAT Setup

- UAT type: black-box
- Tested Skill: `/Users/narra/Documents/alib/Writer/00 信息/miy-skills/workflows/workflow-research/skills/research-literature-reader/skills/paper-reading/skills/collaborative-reading/SKILL.md`
- Raw material: `/Users/narra/Documents/alib/Writer/03 Projects/260521-基金经理研究/99-文献与项目管理/PDFs/基金经理/RFS-Does Media Coverage of Stocks Affect Mutual Funds Trading and Performance/tasks/TASK01-PDF转分章Markdown/outputs/manuscript_paragraphs.md`
- Simulated user request: “我们来用交互式阅读的方式读这篇论文吧。”
- SubAgent: `Kepler`
- Main Agent report time: 2026-07-06 16:38 CST

## UAT Prompt Integrity

Clean UAT.

The prompt only provided:

```text
被测 Skill 路径；
论文 Markdown 底稿；
真实用户请求；
输出外壳；
隔离规则；
只读要求。
```

The prompt did not leak:

```text
expected A01 wording；
P1/P2 expected structure；
A02 theoretical-layer expectation；
Pi-KB expectation；
proxy-ban-in-A02 rule；
expected PASS / FAIL criteria。
```

## SubAgent Raw Result

SubAgent reported:

```text
已完成黑盒 UAT 模拟：我只读取了被测 Skill、其模板和论文 Markdown 底稿；
没有读取隔离文件，也没有修改任何文件。
```

### Conversation Output: Key Raw Excerpts

A01:

```text
形式逻辑完整还原版：
专业基金经理也受有限注意力影响；
并且，基金经理受有限注意力影响越强，其未来投资表现越差。

这是一个联言 + 条件关系的复合命题：

P1：专业基金经理受有限注意力影响。
P2：如果基金经理受有限注意力影响越强，那么其未来投资表现越差。

这里我把“买入媒体报道股票的倾向”暂时不放进核心发现，
因为它更像作者用来观察“有限注意力”的 proxy，
而不是理论层 claim 本身。
```

A02-ish first-pass explanation:

```text
P1：基金经理存在有限注意力，并且这种注意力会影响其交易选择。
待证对象是：专业投资者并非完全不受注意力约束；
他们的交易会被注意力触发对象系统性影响。

P2：有限注意力越强，未来基金表现越差。
待证对象是：这种交易不是信息优势或技能的体现，
而更像搜索成本 / 认知资源不足导致的低质量交易。
```

Boundary / diagnostic handling:

```text
买入端强于卖出端，我目前先看作 P1/P2 的 diagnostic pattern 或边界支持，
而不是单独核心命题。
```

Proxy layer:

```text
P1 的 proxy bridge 可能是：股票是否被大众媒体覆盖、覆盖强度，
以及基金是否更倾向买入这些被覆盖股票。

P2 的 proxy bridge 可能是：基金层面的 PROPENSITY_BUY_MEDIA，
也就是某基金买入媒体覆盖股票的倾向；
结果变量是后续 alpha / manipulation-proof performance 等业绩指标。

这些是经验代理，不等于理论对象本身。
理论对象仍是“有限注意力”。
```

### Discussion Outline Draft: Key Raw Excerpts

Proposition Registry:

```text
P1 | core proposition |
专业基金经理受有限注意力影响，且这种注意力约束会影响其交易选择。 |
self | pending |
理论层命题；media coverage 是 proxy，不是 P1 本身。

P2 | core proposition |
基金经理受有限注意力影响越强，其未来投资表现越差。 |
self | pending |
理论层后果命题；PROPENSITY_BUY_MEDIA 是 proxy。

S-P1-1 | proxy |
媒体覆盖 / 覆盖强度代理 attention trigger。 |
P1 | pending |
需检查 proxy bridge warrant。

S-P1-2 | diagnostic / boundary |
媒体覆盖对买入影响强于卖出。 |
P1 | pending |
作者解释为买入搜索空间更大、卖出受持仓和卖空限制影响。
```

A02 details:

```text
### A02 Proof Structure / Argument Plan

- Status: pending
- Linked proposition IDs: P1, P2
- Current explanation:
  - P1-X = 有限注意力 / 注意力约束。
  - P1-Y = 基金经理交易行为 / 投资选择。
  - P1-R = 有限注意力会系统性影响基金经理交易行为。
  - P2-X = 有限注意力驱动交易倾向。
  - P2-Y = 未来基金表现。
  - P2-R = 有限注意力驱动交易倾向越强，未来表现越差。
- Open questions: Pi-KB 需要进一步从 introduction / literature paragraphs 中整理。
```

## Main Agent Evaluation

### Expected Behavior

After the latest Skill revision, a clean first-round collaborative reading should:

```text
1. Keep A01 at claim level.
2. Identify P1 / P2 as stable proposition IDs.
3. Keep media coverage, PROPENSITY_BUY_MEDIA, alpha, and tables out of A01 core claim.
4. In A02, formulate each Pi at theoretical-object level:
   Pi-X / Pi-Y / Pi-R / Pi-KB.
5. Move concrete proxy choices to A03.
6. Move diagnostic patterns, statistical results, robustness, and exclusion tests to A07 or support branches.
7. Preserve Proposition Registry and Linked proposition IDs in the outline.
```

### Actual Behavior

Passed:

```text
1. A01 is cleanly stated as P1 且 P2.
2. The output explicitly says media coverage / PROPENSITY_BUY_MEDIA are proxies, not theory-level claims.
3. Proposition Registry is present.
4. A03-P1 and A03-P2 are separated.
5. Buy-side vs sell-side is treated as diagnostic / boundary, not as P3.
6. A02 includes Pi-X / Pi-Y / Pi-R for P1 and P2.
7. A01-A09 include linked proposition IDs or proposition-linked structure.
```

Partial:

```text
1. Pi-KB is recognized but not filled.
   The outline says: “Pi-KB 需要进一步从 introduction / literature paragraphs 中整理.”

2. The first conversation output still uses “注意力触发对象” in A02-ish wording.
   This is mostly theoretical, but it sits close to the later media-coverage proxy.

3. The Orientation Card's “可观察对象 / proxy” section is acceptable as A03 preview,
   but it could be visually separated more strongly from A02 to avoid the user reading it as proof structure.
```

Failed:

```text
No major structural failure.
```

## PASS / FAIL

Result: PASS with minor residual risk.

The key test passed: the subAgent did not put `media coverage` or `PROPENSITY_BUY_MEDIA` into the A01 core claim, and A02 details stayed mostly at the theoretical `Pi-X / Pi-Y / Pi-R` level.

The remaining issue is not a failure of the new rule, but a completeness gap:

```text
Pi-KB is now required by the Skill,
but the generated first-round outline only marks it as an open question.
```

## Leakage Assessment

No leakage found.

The UAT prompt did not reveal the target structure, but the subAgent naturally generated:

```text
P1 / P2；
Proposition Registry；
A03-P1 / A03-P2；
proxy-vs-claim distinction；
diagnostic / boundary classification；
A02 Pi-X / Pi-Y / Pi-R。
```

This indicates the tested Skill is shaping behavior rather than the UAT prompt teaching the answer.

## Patch Needed

Not urgent.

Recommended small follow-up patch:

```text
In the discussion-outline template, make Pi-KB an explicit field under A02,
not only a prompt question.

For each Pi:
  - Pi-X:
  - Pi-Y:
  - Pi-R:
  - Pi-KB:
```

Reason:

```text
The current output recognized that Pi-KB belongs to A02,
but treated it as an open question rather than a first-pass field to fill.
```

This patch would reduce the chance that future agents omit the literature-knowledge-base part of A02.

## Suggested Next Step

If we continue improving the Skill before returning to the paper:

```text
Patch discussion-outline-template.md:
  add an A02 Pi-X / Pi-Y / Pi-R / Pi-KB mini-table.
```

If we return to the paper now:

```text
Proceed to A02-P1 and A02-P2,
but explicitly fill Pi-KB from introduction / literature paragraphs before A03.
```

## Patch Applied After User Review

User confirmed that the UAT did not actually complete the A02 `Pi-KB` requirement; it only recognized it as an open question.

Applied patch:

```text
discussion-outline-template.md:
  Added an explicit A02 Proof Structure Table:
    Proposition ID | Pi-X | Pi-Y | Pi-R | Pi-KB | Needs Source Check

collaborative-reading/SKILL.md:
  Added rule that Pi-KB must not be only an open question.
  The first round must provide a first-pass knowledge-base judgment:
    what prior literature roughly knows;
    what remains unresolved;
    what relation the paper attempts to advance.
```

Expected effect:

```text
Future UAT should not merely say “Pi-KB needs source check.”
It should fill a first-pass Pi-KB field and mark needs-source-check only for uncertain details.
```
