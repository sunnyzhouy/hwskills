---
name: huawei-product-principles
description: Huawei-style product planning principles for product line strategy, roadmap decisions, release planning, requirement prioritization, and strategy-to-product translation. Use when Codex needs to critique or shape roadmap logic before detailed execution planning. Typical triggers include roadmap review, release planning critique, product line strategy refinement, and requirement package quality review.
---

# Huawei Product Principles

## Overview

Apply an abstract product planning quality layer before detailed release or execution planning. Use this skill to strengthen tradeoffs, roadmap logic, and value-to-scope translation.

## Apply Principle Checks First

Judge product planning against these questions:

- Does the roadmap reflect strategy and customer scenarios?
- Are priorities explicit instead of hidden in a backlog dump?
- Are release themes coherent and decision-ready?
- Are tradeoffs, dependencies, and constraints visible?
- Is the handoff to development concrete enough to operate?

Read [principle-checklist.md](references/principle-checklist.md) when a formal review is needed.

## Use The Skill In Three Modes

- `Critique`: review roadmap or release plans
- `Shape`: improve release logic and prioritization before drafting
- `Guardrail`: support `product-planning-execution` while it creates the actual plan

## Keep The Abstraction Useful

Explain weaknesses in plain product language:

- What release logic is missing
- What priority is unjustified
- What dependency is ignored
- What customer scenario is weakly represented

## Hand Off Cleanly

If the user needs the actual output package:

- Default to a short `Shape` pass first when the user asks directly for roadmap, release planning, or product line planning.
- Switch to `product-planning-execution` for roadmap or release deliverables
- Switch to `product-development-ipd-execution` once scope is stable and execution planning should start

## Resources

- Read [principle-checklist.md](references/principle-checklist.md) for the main evaluation rubric.
- Read [common-mistakes.md](references/common-mistakes.md) when the roadmap looks complete but is not decision-ready.
