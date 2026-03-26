---
name: service-itr-execution
description: Huawei-style service execution workflow for issue intake, diagnosis, escalation, resolution, closure, complaint handling, and closed-loop feedback into product and management. Use when Codex needs to design or improve a service operating model that turns customer issues into timely resolution and organizational learning. Typical triggers include ticket process redesign, escalation mechanism design, complaint handling, service KPI setup, and service-to-product feedback loop planning.
---

# Service Itr Execution

## Overview

Turn service work into a real issue-to-resolution operating model. Focus on intake, classification, ownership, escalation, closure quality, and feedback into product or management systems.

## Gather The Right Inputs

Collect or infer:

- Service scope and issue types
- Current intake channels and ownership model
- Existing SLA, escalation pain points, or closure problems
- Required output: operating memo, workflow, KPI set, or role design

If the process is unclear, produce a draft operating model and mark assumptions.

## Execute The Workflow

1. Define issue classes and service boundary.
Clarify what issue types enter the flow and where resolution ends.

2. Design intake and triage.
Define channels, required fields, severity logic, and first ownership.

3. Define resolution and escalation.
Clarify who solves what, when escalation happens, and who decides exceptions.

4. Define closure.
State what evidence is required for resolution and what counts as real closure.

5. Build feedback loops.
Define what flows back to product, delivery, quality, or management.

6. Package the operating model.
Produce a service memo, workflow design, or KPI and review package.

If the user wants a first-pass checklist, run [generate_itr_checklist.py](scripts/generate_itr_checklist.py).

## Output Shapes

Common deliverables:

- Issue-to-resolution operating memo
- Escalation and closure checklist
- Service KPI and review cadence sheet
- Service-to-product feedback loop design

Use [itr-operating-template.md](assets/itr-operating-template.md) and [escalation-template.md](assets/escalation-template.md).

## Keep The Service Real

Reject these anti-patterns:

- Ticket closed internally but not resolved for the customer
- SLA metrics without severity and ownership logic
- Escalation path without decision owner
- No feedback loop to product or quality teams

Read [workflow.md](references/workflow.md) for the full flow and [metrics.md](references/metrics.md) when KPI design is weak.

## Hand Off Forward

This skill owns concrete service-process redesign, not organization-wide rollout governance.
Recommend `transformation-pmo-execution` when the goal is enterprise-wide adoption of the service operating model.
