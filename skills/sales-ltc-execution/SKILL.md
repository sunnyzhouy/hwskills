---
name: sales-ltc-execution
description: Huawei-style sales execution workflow for lead to cash process design, opportunity governance, bidding and contract flow, delivery coordination, and revenue realization control points. Use when Codex needs to design or improve a sales operating model from lead generation through deal, delivery coordination, acceptance, and cash collection. Typical triggers include lead management, opportunity pipeline redesign, sales process design, contract-to-cash control, and business operating mechanism setup.
---

# Sales Ltc Execution

## Overview

Turn scattered sales activities into a controllable lead-to-cash operating model. Focus on stage definitions, governance, handoffs, and the control points that protect conversion and cash realization.

## Gather The Right Inputs

Collect or infer:

- Business model and average deal type
- Current lead sources and pipeline stages
- Major conversion or collection pain points
- Delivery and acceptance dependencies
- Required output: operating memo, stage design, or governance checklist

If current data is weak, still define the operating model and mark which metrics need validation.

## Execute The Workflow

1. Define the flow boundary.
State where the process starts and what counts as cash realization.

2. Define stages and exits.
Clarify lead, opportunity, proposal, contract, delivery, acceptance, and collection states.

3. Build governance and reviews.
Define forecast review, deal review, exception escalation, and contract control.

4. Map critical handoffs.
Clarify where sales, solution, delivery, finance, and service interact.

5. Set metrics and risk controls.
Include conversion, cycle time, win rate, backlog, acceptance, and collection metrics where relevant.

6. Package the design.
Produce a process memo, stage-gate table, or governance checklist.

If the user wants a first-pass checklist, run [generate_ltc_checklist.py](scripts/generate_ltc_checklist.py).

## Output Shapes

Common deliverables:

- Lead-to-cash operating memo
- Opportunity governance checklist
- Stage definition and exit criteria table
- Deal review cadence and KPI sheet

Use [ltc-operating-template.md](assets/ltc-operating-template.md) and [deal-review-template.md](assets/deal-review-template.md).

## Keep The Flow Controllable

Reject these anti-patterns:

- Pipeline stages without exit criteria
- Sales process that ignores delivery and acceptance
- Forecast review without real decision triggers
- Contract-to-cash design without finance control points

Read [workflow.md](references/workflow.md) for the full flow and [control-points.md](references/control-points.md) when governance is weak.

## Hand Off Forward

This skill does not own post-sales issue handling or ticket closure design.
Recommend `service-itr-execution` when post-sales issue handling or service closure should be integrated into the operating model.
