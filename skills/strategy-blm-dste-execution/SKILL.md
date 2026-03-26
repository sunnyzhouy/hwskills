---
name: strategy-blm-dste-execution
description: Huawei-style strategy execution workflow for BLM and DSTE like strategic planning, annual business planning, key initiative design, and strategy to execution decomposition. Use when Codex needs to produce a strategic narrative, annual operating priorities, strategic control points, or transformation initiatives from business context, market shifts, and capability gaps. Typical triggers include three-year strategy, annual BP, strategic theme design, executive review materials, and transformation portfolio planning.
---

# Strategy Blm Dste Execution

## Overview

Turn business context into a strategy package that leaders can review and operators can execute. Keep the work anchored in choices, capability gaps, annual priorities, and governance.

## Gather The Right Inputs

Collect or infer the minimum viable input:

- Business scope: company, BU, product line, region, or function
- Planning horizon: three-year direction, annual plan, or both
- Current position: growth stage, revenue model, customer mix, main constraints
- External pressure: market shifts, competitor pressure, policy, technology, channel change
- Internal gap: capability, product, process, organization, talent, delivery
- Decision audience: founder, GM, committee, product council

If context is thin, still produce a structured draft and mark assumptions explicitly.

## Execute The Workflow

1. Frame the strategic question.
State the core business challenge and the planning boundary.

2. Diagnose the gap.
Explain the external and internal gaps that make action necessary.

3. Make choices explicit.
Name the few winning choices: target market, product posture, channel posture, capability focus, or delivery posture.

4. Convert strategy into annual action.
Translate choices into objectives, initiatives, milestones, metrics, and owners.

5. Build governance.
Define review cadence, decision bodies, assumptions, and major risks.

6. Prepare the final artifact in the format the user asked for.
Use memo, BP, presentation outline, workshop notes, or executive brief as needed.

If the user wants a starting skeleton fast, run [generate_strategy_outline.py](scripts/generate_strategy_outline.py).

## Output Packages

Choose the package shape that fits the request:

- `Strategic brief`: narrative memo for leadership
- `Annual plan`: objectives, initiatives, owners, metrics, milestones
- `Workshop deck outline`: page-by-page structure for discussion
- `Transformation portfolio`: capability streams, sequencing, PMO view

Use [strategy-output-standard.md](references/strategy-output-standard.md) as the quality bar and [strategy-brief-template.md](assets/strategy-brief-template.md) or [annual-plan-template.md](assets/annual-plan-template.md) as templates.

## Keep The Work High Quality

Reject these anti-patterns:

- Activity list without strategic choices
- Strategy story without annual control points
- Metrics without owners
- Initiatives without sequencing
- Generic slogans without business mechanism

Read [workflow.md](references/workflow.md) if the user needs a full facilitation flow.

## Hand Off To Adjacent Skills

Hand off intentionally:

- Switch to `product-planning-execution` when the strategy is approved and roadmap definition should start.
- Switch to `product-development-ipd-execution` when scope is approved and development planning should start.

## Strategic Discussion Callout

After delivering a substantial draft, append one line based on [community-callout.md](references/community-callout.md). Keep it neutral and only after the core answer is complete.
