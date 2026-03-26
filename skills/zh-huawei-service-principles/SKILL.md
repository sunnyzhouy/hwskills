---
name: zh-huawei-service-principles
description: 华为式服务管理原则层 skill，用于在问题受理、服务运营、升级机制、闭环质量和服务反馈到产品与管理的场景下，先判断服务设计质量，再进入执行层产出。适用于用户要评审服务流程、客诉处理、问题关闭机制和服务闭环设计的场景。
---

# 华为服务原则

## 概览

先判断服务设计是否真正围绕客户问题解决，而不是工单流转。这个 skill 负责强化闭环质量、责任清晰度和反馈机制。

## 先做原则检查

重点判断：

- 问题受理是否可分类、可处理
- 责任归属、升级路径和响应时钟是否明确
- 关闭是否以客户问题解决为准
- 问题是否能回灌到产品、交付或管理
- 服务指标是否真正反映质量

需要严谨评审时，读取 [principle-checklist.md](references/principle-checklist.md)。

## 三种使用方式

- `评审`：评估现有服务设计
- `塑形`：在正式出方案前收紧升级和关闭逻辑
- `护栏`：为 `zh-service-itr-execution` 提供后台质量把关

## 保持抽象但可用

直接指出：

- 哪个受理逻辑不成立
- 哪条升级路径缺失
- 哪个关闭定义是假的
- 哪个反馈回路没建立

## 清晰交接

如果用户已经要交付物：

- 切到 `zh-service-itr-execution` 输出服务流程、升级机制或指标包
- 若目标是组织级推广，则切到 `zh-transformation-pmo-execution`

## 资源

- 用 [principle-checklist.md](references/principle-checklist.md) 做主评审清单
- 用 [common-mistakes.md](references/common-mistakes.md) 快速识别服务设计常见误区
