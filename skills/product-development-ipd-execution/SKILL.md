---
name: product-development-ipd-execution
description: Huawei-style IPD execution workflow for product development planning, stage gate preparation, cross functional execution, quality and risk management, and requirement to release decomposition. Use when Codex needs to convert approved roadmap or requirements into an executable product development plan with milestones, reviews, and ownership. Typical triggers include R and D planning, version execution planning, stage gate review prep, cross-functional coordination, and development risk management.
---

# Product Development Ipd Execution

## Overview

Turn approved roadmap or requirements into a product development execution package. Keep the work cross-functional, stage-gated, and explicit about quality, ownership, and risk.

## Confirm The Inputs

Collect or infer:

- Approved scope or release package
- Product goals and success criteria
- Constraints: architecture, staffing, dependency, compliance, delivery date
- Required review style: stage plan, project memo, gate checklist, steering material

If approval status is unclear, state assumptions and mark pending decisions.
If scope is not actually approved, route back to `product-planning-execution` first and label the execution plan as provisional only.

## Execute The Workflow

1. Define the execution boundary.
Clarify scope, exclusions, timing, and success criteria.

2. Decompose the work.
Break scope into workstreams, major capabilities, milestones, and review packages.

3. Plan stage gates and exits.
Set gate objectives, entry assumptions, and exit criteria.

4. Build cross-functional coordination.
Include development, test, product, operations, delivery, and support viewpoints where relevant.

5. Manage risk and quality explicitly.
List top risks, quality controls, change triggers, and escalation path.

6. Prepare the review artifact.
Produce a stage plan, review checklist, or project execution memo that leaders can inspect.

If the user needs a starting checklist, run [generate_ipd_checklist.py](scripts/generate_ipd_checklist.py).

## Output Shapes

Common deliverables:

- Development execution memo
- Stage gate review checklist
- Cross-functional milestone plan
- Quality and risk control sheet

Use [ipd-plan-template.md](assets/ipd-plan-template.md) and [review-template.md](assets/review-template.md) as templates.

## Keep The Plan Executable

Reject these anti-patterns:

- Milestones without exit criteria
- Scope list without workstream ownership
- Review deck without risk register
- Development plan that ignores downstream release or support readiness
- Planning output that cannot be used by a real project owner

Read [workflow.md](references/workflow.md) for the execution pattern and [stage-gates.md](references/stage-gates.md) for a reusable gate rubric.

## Hand Off Forward

If the user later needs service feedback loop or sales/service process design, recommend adding dedicated service or sales skills instead of stretching this one beyond development execution.
