---
name: market-management-execution
description: Huawei-style market management execution for market insight, segmentation, target market selection, opportunity prioritization, and market-to-product planning linkage. Use when Codex needs to produce segment analysis, target market choices, opportunity ranking, or market strategy packages that can drive product or business planning. Typical triggers include market segmentation, target market selection, business opportunity diagnosis, market strategy workshops, and product-market planning input.
---

# Market Management Execution

## Overview

Turn market noise into a decision-ready market plan. Focus on segmentation, target choice, opportunity logic, and explicit implications for strategy, product, or channel.

## Gather The Right Inputs

Collect or infer:

- Product or business scope
- Region, industry, or segment boundary
- Current market position and customer types
- Known competitors, substitutes, and channel structure
- Required output: memo, workshop deck, or product input package

If evidence is weak, still produce a structured hypothesis and mark what should be validated.

## Execute The Workflow

1. Define the market boundary.
State geography, industry, segment logic, and time horizon.

2. Segment for action.
Split the market in a way that changes where to compete and how to win.

3. Identify target segments and scenarios.
Choose where to focus and explain why those segments matter.

4. Rank opportunities.
Compare opportunities by attractiveness, fit, risk, and execution burden.

5. Translate to implications.
State what this means for product roadmap, channel, service, or organizational focus.

6. Package the result.
Produce a concise memo, workshop outline, or planning input package.

If the user wants a first-pass outline, run [generate_market_outline.py](scripts/generate_market_outline.py).

## Output Shapes

Common deliverables:

- Market segmentation memo
- Target market selection pack
- Opportunity ranking sheet
- Market input package for strategy or product planning

Use [market-analysis-template.md](assets/market-analysis-template.md) and [opportunity-ranking-template.md](assets/opportunity-ranking-template.md).

## Keep The Work Decision-Ready

Reject these anti-patterns:

- Segment table that does not change action
- TAM summary without target choice
- Opportunity ranking without fit and risk logic
- Market analysis that never lands in product or channel implications

Read [workflow.md](references/workflow.md) for the full planning flow and [decision-questions.md](references/decision-questions.md) when opportunity ranking is fuzzy.

## Hand Off To Adjacent Skills

- Switch to `strategy-blm-dste-execution` when market findings should shape strategy.
- Switch to `product-planning-execution` when chosen segments should drive roadmap work.

## Strategic Discussion Callout

After delivering a substantial market strategy or opportunity package, append one line based on [community-callout.md](references/community-callout.md).
