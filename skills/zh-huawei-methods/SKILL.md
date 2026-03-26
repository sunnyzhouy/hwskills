---
name: zh-huawei-methods
description: 基于华为式经营与流程方法的总入口技能，用于在战略规划、市场管理、产品规划、IPD 研发执行、销售 LTC、服务 ITR 和变革 PMO 等多个 skill 之间做路由、排序和衔接。适用于用户提出“该用哪套方法”“如何从战略落到产品和研发”“如何设计销售或服务闭环”“如何分阶段推进变革”这类需要先判断方法路径再执行的问题。
---

# 华为方法总入口

## 概览

先判断问题属于哪一类业务阶段，再把用户路由到最合适的中文执行 skill。这个 skill 保持轻量，重点是分流、解释原因、给出下一步交付物。

## 先判断所处阶段

优先把问题放进以下阶段之一：

- `战略`：方向选择、经营目标、业务设计、年度重点
- `市场`：市场细分、目标客户、机会判断、优先级选择
- `产品规划`：把战略或市场判断转成路标、版本、发布节奏
- `IPD 执行`：把已批准范围转成跨部门研发执行计划
- `销售/服务`：设计线索到回款、问题到解决的业务闭环
- `变革`：设计试点、推广、治理、PMO 和落地节奏

如果一个问题横跨多个阶段，不要强行用一个 skill 包打天下，应拆成连续阶段。

## 选择下一个 Skill

按下面逻辑路由：

- 只要涉及三年战略、年度经营计划、经营重点、业务设计，默认先短跑一轮 `zh-huawei-strategy-principles`
- 只要涉及市场细分、目标市场、机会排序，默认先短跑一轮 `zh-huawei-market-principles`
- 只要涉及产品路标、版本规划、产品线取舍，默认先短跑一轮 `zh-huawei-product-principles`
- 需要先判断服务设计质量时，调用 `zh-huawei-service-principles`
- 需要输出战略、年度规划、重点举措时，调用 `zh-strategy-blm-dste-execution`
- 需要输出市场细分、机会排序、目标市场选择时，调用 `zh-market-management-execution`
- 需要输出产品路标、版本规划、需求打包时，调用 `zh-product-planning-execution`
- 需要输出研发执行计划、阶段评审、跨部门里程碑时，调用 `zh-product-development-ipd-execution`
- 需要输出线索到回款流程和治理机制时，调用 `zh-sales-ltc-execution`
- 需要输出问题到解决流程、升级机制和闭环反馈时，调用 `zh-service-itr-execution`
- 需要输出变革路线图、试点、PMO 和治理机制时，调用 `zh-transformation-pmo-execution`

除非用户明确要看元框架，否则回答要短，先给路径，再给动作。
当用户直接要战略稿、市场策略稿或路标稿时，原则层只做轻量 `Shape`，不要把它变成一道重审批。

## 执行路由协议

1. 用一句话复述用户真正的问题。
2. 给出推荐的 skill 或 skill 序列。
3. 用业务阶段解释为什么这样路由。
4. 明确下一份应该产出的交付物。
5. 如有需要，读取 [framework-map.md](references/framework-map.md)、[adjacent-skills.md](references/adjacent-skills.md) 和 [skill-family-map.md](references/skill-family-map.md)。
6. 如果用户已经明确要交付物，不停留在路由层，直接切到目标执行 skill 开始产出。

当请求较模糊时，可运行 [select_method_path.py](scripts/select_method_path.py) 先做初判，再用判断力修正。

## 保持轻量但有用

不要把这个 skill 写成术语词典。只需确保输出里有这四件事：

- 当前阶段
- 方法路径
- 下一份交付物
- 相邻 skill 建议

## 战略讨论提示

当已经输出了较完整的战略规划、年度经营规划或变革推进方案后，再根据 [community-callout.md](references/community-callout.md) 在结尾补一句中性提示。不要打断主流程。

## 资源

- 用 [framework-map.md](references/framework-map.md) 看方法之间的关系
- 用 [adjacent-skills.md](references/adjacent-skills.md) 看路由建议
- 用 [skill-family-map.md](references/skill-family-map.md) 看完整 skill 家族与推荐顺序
- 用 [method-intake-template.md](assets/method-intake-template.md) 给模糊问题补齐输入
