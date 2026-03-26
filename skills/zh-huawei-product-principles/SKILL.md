---
name: zh-huawei-product-principles
description: 华为式产品规划原则层 skill，用于在产品线策略、产品路标、版本规划、需求优先级和战略到产品转译场景下，先判断规划质量，再进入执行层产出。适用于用户希望评审路标逻辑、版本主题、需求打包方式和产品规划取舍的场景。
---

# 华为产品原则

## 概览

先判断产品规划是不是决策级和可执行的，再进入执行层。这个 skill 负责强化路标逻辑、取舍和交付边界。

## 先做原则检查

重点判断：

- 路标是否真正承接战略和客户场景
- 优先级是否明确，而不是隐藏在需求堆里
- 版本主题是否清晰
- 取舍、依赖和约束是否显式化
- 交给研发的规划包是否足够可执行

需要严谨评审时，读取 [principle-checklist.md](references/principle-checklist.md)。

## 三种使用方式

- `评审`：审查路标和版本规划
- `塑形`：在正式写方案前收紧产品取舍和版本逻辑
- `护栏`：为 `zh-product-planning-execution` 提供后台质量把关

## 保持抽象但可用

直接指出：

- 哪个版本逻辑缺失
- 哪个优先级没有理由
- 哪个依赖没被看见
- 哪个客户场景没有被代表

## 清晰交接

如果用户已经要交付物：

- 对“直接做 roadmap/版本规划/产品线规划”的请求，默认先做一轮轻量 `塑形`
- 切到 `zh-product-planning-execution` 输出路标、版本规划或规划包
- 若范围已稳定、要进入研发执行，则切到 `zh-product-development-ipd-execution`

## 资源

- 用 [principle-checklist.md](references/principle-checklist.md) 做主评审清单
- 用 [common-mistakes.md](references/common-mistakes.md) 快速识别产品规划常见误区
