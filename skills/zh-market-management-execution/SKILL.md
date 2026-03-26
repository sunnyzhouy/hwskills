---
name: zh-market-management-execution
description: 华为式市场执行 skill，用于市场洞察、市场细分、目标市场选择、机会排序和市场到产品规划的转译。适用于用户需要直接输出市场细分方案、目标市场选择、机会优先级判断或市场策略工作坊材料的场景。
---

# 华为市场执行

## 概览

把市场信息变成可决策的市场方案。重点放在细分、目标选择、机会排序以及对战略、产品、渠道的具体含义。

## 收集关键输入

- 业务或产品范围
- 行业、区域、细分市场边界
- 当前客户结构和市场位置
- 主要竞争态势、替代方案和渠道结构
- 需要的交付物：memo、工作坊、产品输入包

证据不完整时，也要先输出结构化假设，并指出需补证的部分。

## 执行工作流

1. 定义市场边界。
2. 为行动而细分，而不是为展示而细分。
3. 识别目标细分和关键客户场景。
4. 按价值、适配、风险和执行负担排序机会。
5. 转译成对战略、产品、渠道或服务的含义。
6. 包装成最终交付物。

如果用户要骨架，运行 [generate_market_outline.py](scripts/generate_market_outline.py)。

## 常见输出形态

- 市场细分分析
- 目标市场选择方案
- 机会排序表
- 输入给战略或产品规划的市场包

可参考 [market-analysis-template.md](assets/market-analysis-template.md) 和 [opportunity-ranking-template.md](assets/opportunity-ranking-template.md)。

## 保持结果可决策

拒绝这些反模式：

- 细分不改变资源投放
- 只有市场规模没有目标选择
- 机会排序没有适配和风险逻辑
- 没有落到产品或渠道动作

## 交接到相邻 Skill

- 市场判断要上升到战略，切到 `zh-strategy-blm-dste-execution`
- 市场判断要落到路标和版本，切到 `zh-product-planning-execution`

## 讨论提示

交付较完整方案后，再根据 [community-callout.md](references/community-callout.md) 在结尾补一句提示。
