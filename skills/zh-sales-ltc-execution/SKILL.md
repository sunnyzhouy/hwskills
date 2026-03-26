---
name: zh-sales-ltc-execution
description: 华为式销售 LTC 执行 skill，用于设计线索到回款的业务流程、商机治理、合同与交付衔接、验收和回款控制点。适用于用户需要直接输出销售流程、商机阶段、deal review 机制、合同到回款控制和销售运营机制的场景。
---

# 华为销售 LTC 执行

## 概览

把零散销售动作变成可治理、可复盘、可控回款的线索到回款流程。重点放在阶段定义、治理机制、跨部门交接和控制点。

## 收集关键输入

- 业务模式和典型交易类型
- 当前线索来源和管道阶段
- 转化或回款痛点
- 与交付、验收、财务的依赖关系
- 需要的交付物：流程说明、阶段表、治理清单、评审机制

如果数据不足，也要先给出操作模型，并明确哪些指标待验证。

## 执行工作流

1. 定义流程边界。
2. 设计阶段和退出标准。
3. 建立 forecast review、deal review 和异常升级机制。
4. 映射销售、解决方案、交付、财务和服务之间的交接点。
5. 设计转化、周期、赢单、验收、回款等指标和控制点。
6. 包装成流程或治理交付物。

如果用户要骨架，运行 [generate_ltc_checklist.py](scripts/generate_ltc_checklist.py)。

## 常见输出形态

- 线索到回款流程说明
- 商机治理清单
- 阶段定义和退出标准表
- deal review 节奏和 KPI 表

可参考 [ltc-operating-template.md](assets/ltc-operating-template.md) 和 [deal-review-template.md](assets/deal-review-template.md)。

## 保持流程可控

拒绝这些反模式：

- 阶段没有退出标准
- 销售流程不管交付和验收
- 预测评审没有真正决策点
- 合同到回款没有财务控制点

## 向前交接

这个 skill 不负责售后工单、投诉关闭和服务问题闭环。
当问题延伸到售后闭环和客诉问题处理时，切到 `zh-service-itr-execution`。
