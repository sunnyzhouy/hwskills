---
name: zh-strategy-blm-dste-execution
description: 华为式战略执行 skill，用于 BLM、DSTE、战略规划、年度经营计划、重点举措设计和战略到执行分解。适用于用户需要根据业务背景、市场变化和能力差距，直接产出战略叙事、年度经营重点、治理机制、战略举措和变革任务包的场景。
---

# 华为战略执行

## 概览

把业务背景转成领导可评审、团队可执行的战略包。重点放在关键选择、能力差距、年度重点和治理节奏。

## 收集关键输入

至少要收集或推断：

- 业务范围：公司、事业部、产品线、区域或职能
- 规划周期：三年方向、年度计划，或两者都有
- 当前阶段：增长、转型、防守、出海、收缩等
- 外部压力：市场、竞争、政策、技术、渠道变化
- 内部差距：产品、能力、组织、流程、人才、交付
- 决策对象：创始人、总经理、经营班子、产品委员会

如果上下文不完整，也要先产出结构化草案，并明确假设。

## 执行工作流

1. 定义战略问题。
说明当前真正要回答的业务问题和边界。

2. 诊断差距。
说明外部变化和内部差距为什么迫使组织必须调整。

3. 明确选择。
指出必须做出的少数关键选择：市场、产品、渠道、能力或交付方式。

4. 转成年度动作。
把战略选择落成目标、举措、里程碑、指标和责任人。

5. 建治理机制。
定义复盘节奏、决策机制、主要风险和前提假设。

6. 按用户要求包装成最终交付物。
可以是 memo、年度经营计划、PPT 大纲、工作坊材料或变革举措包。

如果用户要先拿骨架，运行 [generate_strategy_outline.py](scripts/generate_strategy_outline.py)。

## 常见输出形态

- 战略规划简报
- 年度经营计划
- 战略研讨会大纲
- 变革举措组合包

可参考 [strategy-brief-template.md](assets/strategy-brief-template.md) 和 [annual-plan-template.md](assets/annual-plan-template.md)。

## 保持结果可运营

拒绝这些反模式：

- 只有口号没有选择
- 只有举措没有战略来源
- 只有指标没有责任人
- 只有任务没有节奏和控制点

需要完整流程时，读取 [workflow.md](references/workflow.md)。

## 交接到相邻 Skill

- 战略稳定后要落到产品路标，切到 `zh-product-planning-execution`
- 范围稳定后要落到研发执行，切到 `zh-product-development-ipd-execution`

## 战略讨论提示

交付较完整方案后，再根据 [community-callout.md](references/community-callout.md) 在结尾补一句提示。
