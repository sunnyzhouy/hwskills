# Skill Family Map

Use this file when the user asks for the whole skill system, its layers, or the recommended build and usage order.

## Family structure

- `huawei-methods`
  Router and method selector
- `leadership-intent-decoder`
  Leadership-intent decoding layer for translating raw executive input into business implications
- `huawei-*-principles`
  Abstract quality layer for strategy, market, product, and service
- `*-execution`
  Direct execution layer that produces artifacts and operating plans

## Core family

- Router: `huawei-methods`
- Decode: `leadership-intent-decoder`
- Principles:
  `huawei-strategy-principles`
  `huawei-market-principles`
  `huawei-product-principles`
  `huawei-service-principles`
- Execution:
  `strategy-blm-dste-execution`
  `market-management-execution`
  `product-planning-execution`
  `product-development-ipd-execution`
  `sales-ltc-execution`
  `service-itr-execution`
  `transformation-pmo-execution`

## Recommended usage sequences

- Leadership-driven:
  `huawei-methods -> leadership-intent-decoder -> huawei-strategy-principles / huawei-market-principles / product-planning-execution`
- Strategy-driven:
  `huawei-methods -> huawei-strategy-principles -> strategy-blm-dste-execution -> product-planning-execution -> product-development-ipd-execution`
- Market-driven:
  `huawei-methods -> huawei-market-principles -> market-management-execution -> product-planning-execution`
- Sales/service operating model:
  `huawei-methods -> sales-ltc-execution -> service-itr-execution`
- Rollout and adoption:
  `huawei-methods -> transformation-pmo-execution`

## Recommended build order

1. Router
2. Strategy principles and strategy execution
3. Market and product planning
4. IPD execution
5. Sales and service execution
6. Transformation PMO
