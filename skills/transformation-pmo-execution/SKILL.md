---
name: transformation-pmo-execution
description: Huawei-style transformation execution workflow for rollout sequencing, PMO design, governance, pilot planning, adoption management, and method deployment across strategy, product, sales, service, or development processes. Use when Codex needs to turn strategy or process design into a staged transformation plan with pilots, governance, cadence, and change control. Typical triggers include transformation roadmap, PMO setup, rollout design, pilot-to-scale planning, operating model adoption, and requests to push a new process or workflow across an organization.
---

# Transformation Pmo Execution

## Overview

Turn a designed method or operating model into a rollout plan that can survive contact with the organization. Focus on sequencing, pilot scope, governance, PMO rhythm, and adoption control.

## Gather The Right Inputs

Collect or infer:

- Transformation scope and target model
- Stakeholders, governance body, and decision hierarchy
- Pilot candidates, rollout constraints, and timeline
- Required output: roadmap, PMO charter, pilot plan, or governance package

If context is weak, produce a staged rollout hypothesis and mark assumptions.

## Execute The Workflow

1. Define the target state and rollout boundary.
State what is changing, for whom, and what is out of scope.

2. Sequence the rollout.
Choose pilot, wave, and scale logic based on risk and dependency.

3. Build PMO and governance.
Define cadence, review bodies, issue escalation, and reporting artifacts.

4. Define enablement and change controls.
Include training, communications, standards, audits, and reinforcement loops.

5. Define adoption metrics.
Track adoption, execution health, issue closure, and business outcomes.

6. Package the transformation plan.
Produce a roadmap, PMO charter, or pilot-to-scale plan.

If the user wants a first-pass rollout structure, run [generate_transformation_outline.py](scripts/generate_transformation_outline.py).

## Output Shapes

Common deliverables:

- Transformation roadmap
- PMO charter
- Pilot plan and scale criteria
- Governance and adoption KPI sheet

Use [transformation-roadmap-template.md](assets/transformation-roadmap-template.md) and [pmo-charter-template.md](assets/pmo-charter-template.md).

## Keep The Rollout Real

Reject these anti-patterns:

- Big-bang rollout with no pilot logic
- PMO that reports status but does not resolve issues
- Training plan with no adoption metrics
- Transformation roadmap disconnected from decision bodies and operating cadence

Read [workflow.md](references/workflow.md) for the rollout sequence and [governance-patterns.md](references/governance-patterns.md) when PMO design is weak.

## Strategic Discussion Callout

After delivering a substantial transformation plan, append one line based on [community-callout.md](references/community-callout.md).
