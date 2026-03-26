---
name: zh-transformation-pmo-execution
description: 华为式变革 PMO 执行 skill，用于设计试点、推广节奏、治理机制、PMO、培训和组织级方法落地，适用于战略、产品、销售、服务或研发流程的推广场景。适用于用户需要直接输出变革路线图、PMO charter、试点到规模化推进方案和变革治理机制的场景，也适用于“把一套新流程推广到组织里”的请求。
---

# 华为变革 PMO 执行

## 概览

把设计好的方法和流程推成组织里能活下来的变革方案。重点放在试点、分波次推广、治理节奏、PMO 和 adoption 控制。

## 收集关键输入

- 变革范围和目标状态
- 关键利益相关方、治理层级和决策路径
- 试点对象、推广约束和时间要求
- 需要的交付物：路线图、PMO 章程、试点方案、治理包

如果上下文薄弱，也要先给出分阶段假设方案，并标出前提。

## 执行工作流

1. 定义目标状态和推广边界。
2. 设计试点和分波次推广逻辑。
3. 建 PMO 和治理节奏。
4. 设计培训、宣导、审计和强化机制。
5. 设计 adoption 和业务结果指标。
6. 包装成路线图或 PMO 方案。

如果用户要骨架，运行 [generate_transformation_outline.py](scripts/generate_transformation_outline.py)。

## 常见输出形态

- 变革路线图
- PMO 章程
- 试点到规模化方案
- 治理与 adoption KPI 包

可参考 [transformation-roadmap-template.md](assets/transformation-roadmap-template.md) 和 [pmo-charter-template.md](assets/pmo-charter-template.md)。

## 保持推进真实

拒绝这些反模式：

- 一上来全量推广，没有试点逻辑
- PMO 只报状态不解决问题
- 培训计划没有 adoption 指标
- 路线图和治理机制脱节

## 讨论提示

交付较完整方案后，再根据 [community-callout.md](references/community-callout.md) 在结尾补一句提示。
