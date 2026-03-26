---
name: zh-product-development-ipd-execution
description: 华为式 IPD 研发执行 skill，用于把已批准的产品范围转成研发计划、阶段评审、跨部门执行、质量控制和风险管理。适用于用户需要直接输出研发执行计划、阶段门清单、里程碑安排或跨团队协同方案的场景。
---

# 华为 IPD 研发执行

## 概览

把已经批准的范围转成真正能执行的研发计划。重点放在跨部门协同、阶段门、质量、风险和里程碑。

## 收集关键输入

- 已批准范围或发布包
- 产品目标和成功标准
- 约束：架构、人力、依赖、合规、时间
- 需要的交付物：执行 memo、阶段评审、里程碑计划、风险控制表

如果批准状态不清楚，要明确标出假设和待决策项。
如果范围其实还没正式批准，先切回 `zh-product-planning-execution`，并把当前执行计划标成“待审批版本”。

## 执行工作流

1. 定义执行边界。
2. 把范围拆成能力、工作流和里程碑。
3. 设计阶段门目标和退出条件。
4. 建立跨部门协同关系。
5. 明确质量控制和风险管理。
6. 产出评审材料或执行计划。

如果用户要骨架，运行 [generate_ipd_checklist.py](scripts/generate_ipd_checklist.py)。

## 常见输出形态

- 研发执行计划
- 阶段评审清单
- 跨部门里程碑计划
- 质量与风险控制表

可参考 [ipd-plan-template.md](assets/ipd-plan-template.md) 和 [review-template.md](assets/review-template.md)。

## 保持计划可执行

拒绝这些反模式：

- 里程碑没有退出标准
- 只有任务没有 owner
- 只有评审 PPT 没有风险台账
- 研发计划忽略发布和服务准备

## 向前交接

如果后续问题变成服务闭环或组织推广，建议切到 `zh-service-itr-execution` 或 `zh-transformation-pmo-execution`。
