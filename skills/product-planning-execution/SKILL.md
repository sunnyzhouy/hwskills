---
name: product-planning-execution
description: Product planning execution for turning strategy or market insight into product line strategy, roadmap, release themes, requirement package structure, and project initiation inputs. Use when Codex needs to define roadmap options, version objectives, release scope, or a bridge from strategic planning into IPD execution. Typical triggers include roadmap planning, release planning, product line strategy, requirement prioritization, and initiative to project conversion.
---

# Product Planning Execution

## Overview

Translate strategic direction into a product plan that can actually be executed. Focus on planning horizon, customer value, roadmap choices, release scope, and the handoff package for development.

## Build The Planning Context

Collect these inputs:

- Business strategy or market insight
- Product scope and portfolio boundary
- Target customers, scenarios, and value proposition
- Current product maturity and delivery constraints
- Required planning horizon: annual roadmap, half-year releases, or version package

If upstream strategy is weak, say so and narrow the planning assumptions instead of pretending certainty.

## Execute The Workflow

1. Define the planning horizon and product boundary.
State what product, market, release train, and time window are in scope.

2. Derive customer and business value.
Clarify customer scenarios, target segments, and expected business outcomes.

3. Generate roadmap options.
Compare scope choices by value, dependency, and delivery feasibility.

4. Prioritize capabilities and release themes.
Group requirements into coherent themes rather than a flat backlog dump.

5. Define release packages.
For each release, specify goals, headline scope, major dependencies, and tradeoffs.

6. Prepare the development handoff.
State what must be carried into IPD execution: scope, assumptions, owner, decision points, and unresolved risk.

If the user wants a skeleton first, run [generate_planning_outline.py](scripts/generate_planning_outline.py).

## Output Shapes

Common deliverables:

- Product roadmap memo
- Quarterly or half-year release plan
- Product line strategy note
- Project initiation package for development

Use [roadmap-template.md](assets/roadmap-template.md) and [release-plan-template.md](assets/release-plan-template.md) as starting points.

## Keep The Planning Honest

Reject these anti-patterns:

- Roadmap without segment or scenario logic
- Prioritization without explicit tradeoffs
- Release scope that ignores engineering capacity or dependency
- Huge feature laundry list with no release theme
- Handoff package missing assumptions or success criteria

Read [workflow.md](references/workflow.md) for the operating flow and [decision-questions.md](references/decision-questions.md) when prioritization is fuzzy.

## Hand Off Cleanly

When scope and release decisions are stable, switch to `product-development-ipd-execution` to build the actual execution plan.
