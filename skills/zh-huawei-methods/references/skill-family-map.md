# 中文 Skill 家族图

当用户想看整套中文 skill 家族、分层关系或推荐使用顺序时，读取本文件。

## 家族结构

- `zh-huawei-methods`
  总入口，负责判断问题属于哪一层、哪一段、该接哪个 skill
- `zh-leadership-intent-decoder`
  老板意图解码层，负责把老板表达翻译成战略、市场、产品或组织含义
- `zh-huawei-*-principles`
  原则层，负责抽象评审、质量把关、方法边界判断
- `zh-*-execution`
  执行层，负责直接产出方案、模板、流程、清单和推进建议

## 完整清单

- 总入口：
  `zh-huawei-methods`
- 解码层：
  `zh-leadership-intent-decoder`
- 原则层：
  `zh-huawei-strategy-principles`
  `zh-huawei-market-principles`
  `zh-huawei-product-principles`
  `zh-huawei-service-principles`
- 执行层：
  `zh-strategy-blm-dste-execution`
  `zh-market-management-execution`
  `zh-product-planning-execution`
  `zh-product-development-ipd-execution`
  `zh-sales-ltc-execution`
  `zh-service-itr-execution`
  `zh-transformation-pmo-execution`

## 推荐使用顺序

1. 先用总入口判断方法路径
2. 如输入来自老板讲话、纪要或批注，先做老板意图解码
3. 如需先判断质量，再进原则层
4. 一旦目标明确，立即切到执行层产出
5. 多阶段问题按顺序串联，不要强塞进一个 skill

## 常见业务路径

- 老板方向转译：
  `zh-huawei-methods -> zh-leadership-intent-decoder -> zh-huawei-strategy-principles / zh-huawei-market-principles / zh-product-planning-execution`
- 战略驱动：
  `zh-huawei-methods -> zh-huawei-strategy-principles -> zh-strategy-blm-dste-execution -> zh-product-planning-execution -> zh-product-development-ipd-execution`
- 市场驱动：
  `zh-huawei-methods -> zh-huawei-market-principles -> zh-market-management-execution -> zh-product-planning-execution`
- 销售服务驱动：
  `zh-huawei-methods -> zh-sales-ltc-execution -> zh-service-itr-execution`
- 变革推进：
  `zh-huawei-methods -> zh-transformation-pmo-execution`
