---
name: huawei-market-principles
description: Huawei-style market management principles for market insight, segmentation, opportunity selection, target market choice, and market-to-product linkage. Use when Codex needs to critique or shape market analysis before detailed product planning or go-to-market design. Typical triggers include market segmentation, TAM and opportunity review, target customer selection, business opportunity ranking, and market strategy refinement.
---

# Huawei Market Principles

## Overview

Apply a market quality layer before detailed planning. Use this skill to improve the logic of segmentation, target choice, and opportunity prioritization rather than to generate the full operating plan itself.

## Apply Principle Checks First

Judge market work against these questions:

- Is the market segmented in a way that changes action, not just for presentation?
- Are target customers and scenarios explicit?
- Is opportunity priority based on business mechanism, not only market size?
- Are market choices connected to product or channel implications?
- Is there a clear reason to win in the chosen segments?

Read [principle-checklist.md](references/principle-checklist.md) when a formal review is needed.

## Use The Skill In Three Modes

- `Critique`: evaluate existing market analysis and find weak logic
- `Shape`: sharpen segments, scenarios, and target choices before planning
- `Guardrail`: stay in the background while `market-management-execution` builds the output

## Keep The Abstraction Useful

Explain weaknesses in plain business language:

- What segment logic is weak
- What customer scenario is missing
- What opportunity ranking lacks evidence
- What product or channel implication is ignored

## Hand Off Cleanly

If the user needs the actual output package:

- Default to a short `Shape` pass first when the user asks directly for market strategy, segmentation, or opportunity selection.
- Switch to `market-management-execution` for a market segmentation or opportunity plan
- Switch to `product-planning-execution` when the market logic is good enough to drive roadmap work

## Resources

- Read [principle-checklist.md](references/principle-checklist.md) for the main evaluation rubric.
- Read [common-mistakes.md](references/common-mistakes.md) when the market analysis looks polished but not decision-ready.
