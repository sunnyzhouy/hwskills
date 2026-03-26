---
name: zh-service-itr-execution
description: 华为式服务 ITR 执行 skill，用于设计问题受理、定位、升级、解决、关闭、投诉处理和服务到产品回灌的闭环机制。适用于用户需要直接输出服务流程、升级机制、关闭标准、服务 KPI 和问题闭环反馈机制的场景。
---

# 华为服务 ITR 执行

## 概览

把服务工作变成真正的问题到解决闭环。重点放在受理、分级、责任归属、升级、关闭质量和回灌机制。

## 收集关键输入

- 服务边界和问题类型
- 当前受理渠道和归属模型
- 现有 SLA、升级痛点、关闭问题
- 需要的交付物：流程、角色、KPI、升级机制、反馈闭环

如果上下文不清楚，也要先给出草案并标出假设。

## 执行工作流

1. 定义问题类型和服务边界。
2. 设计受理和分诊机制。
3. 设计解决和升级机制。
4. 设计真正的关闭标准。
5. 建立回灌到产品、交付、质量或管理的闭环。
6. 包装成服务运营设计。

如果用户要骨架，运行 [generate_itr_checklist.py](scripts/generate_itr_checklist.py)。

## 常见输出形态

- 问题到解决流程说明
- 升级与关闭清单
- 服务 KPI 与评审节奏
- 服务到产品反馈闭环方案

可参考 [itr-operating-template.md](assets/itr-operating-template.md) 和 [escalation-template.md](assets/escalation-template.md)。

## 保持服务真实

拒绝这些反模式：

- 工单内部关闭但客户问题没解决
- SLA 指标没有分级和 owner
- 升级路径没有决策 owner
- 没有回灌到产品和质量

## 向前交接

这个 skill 负责具体服务流程改造，不负责组织级 rollout 和 PMO 治理。
如果下一步变成组织级推广和治理，切到 `zh-transformation-pmo-execution`。
