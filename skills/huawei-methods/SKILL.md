---
name: huawei-methods
description: Huawei-style business method router for leadership-intent decoding, strategy planning, market management, product planning, IPD product development, sales and service process design, and transformation rollout. Use when Codex needs to decide which Huawei-style methodology fits a business problem, interpret a boss or founder's strategic intent, sequence multiple methodology skills, or hand off from strategic planning into execution. Typical triggers include users asking how to decode leadership strategy, plan roadmap, design product development process, improve sales or service operating model, or structure an enterprise transformation path.
---

# Huawei Methods

## Overview

Route the user to the right Huawei-style method and execution skill. Keep this skill thin: diagnose the problem, recommend the next skill, explain why, and hand off cleanly.

## Route First

Start by placing the request into one of these stages:

- `Leadership intent`: decode what a boss, founder, CEO, or BU head really means from speeches, comments, notes, and direction signals
- `Strategy`: choose direction, ambition, business design, annual priorities
- `Market`: segment markets, define target customers, identify opportunities
- `Product planning`: turn strategy into roadmap, releases, and planning packages
- `IPD execution`: turn approved scope into cross-functional development execution
- `Sales/service`: design front-end business flow, post-sales flow, feedback loop
- `Transformation`: decide rollout sequence, governance, PMO, and change cadence

If the user problem spans multiple stages, decompose it into phases instead of forcing one skill to do everything.

## Select The Next Skill

Use this selection logic:

- Ask `leadership-intent-decoder` first for boss, founder, CEO, or business-head speeches, comments, and notes when the user needs the real strategy, product direction, hidden priority, or implied constraint decoded.
- Ask `huawei-strategy-principles` by default for three-year strategy, annual planning, business design, or operating-priority requests unless the user explicitly wants direct drafting only.
- Ask `huawei-market-principles` by default for segmentation, target-market, or opportunity-ranking requests unless the user explicitly wants direct drafting only.
- Ask `huawei-product-principles` by default for roadmap, release, or product-line planning requests unless the user explicitly wants direct drafting only.
- Ask `huawei-service-principles` to critique service design, issue closure, and feedback loop quality.
- Ask `strategy-blm-dste-execution` to generate strategy narratives, annual plans, strategic initiatives, and governance.
- Ask `market-management-execution` to generate market segmentation, opportunity prioritization, and market attack logic.
- Ask `product-planning-execution` to convert strategy or market insight into roadmap, releases, and project initiation input.
- Ask `product-development-ipd-execution` to convert approved scope into stage-gated development execution.
- Ask `sales-ltc-execution` to design lead-to-cash operating flow, roles, reviews, and control points.
- Ask `service-itr-execution` to design issue-to-resolution operating flow, escalation, and closed-loop learning.
- Ask `transformation-pmo-execution` to build rollout sequence, governance, PMO, and adoption mechanism.
- Keep the router answer short unless the user explicitly asks for a meta-framework or method map.

If no existing execution skill fully fits, still classify the problem and state the nearest skill plus the missing layer.

When a user directly asks for a roadmap, market strategy, or strategic plan, prefer a short `Shape` pass through the matching principles skill before switching to execution. The principles pass should be lightweight and should not block output momentum.

## Execute The Routing Protocol

1. Summarize the user's actual problem in one sentence.
2. State the recommended skill or skill sequence in one line.
3. Explain the reason in terms of business stage, not jargon.
4. State the immediate deliverable that should be produced next.
5. If needed, read [framework-map.md](references/framework-map.md) and [adjacent-skills.md](references/adjacent-skills.md).
6. If the user wants a strategy draft or business plan immediately, switch to the appropriate execution skill and continue producing it.

When the request is ambiguous, use [select_method_path.py](scripts/select_method_path.py) to generate a first-pass recommendation, then refine with judgment.

## Keep The Skill Helpful But Light

Do not turn this skill into a long lecture on Huawei terminology. Use concepts only to improve action quality:

- State the stage
- State the method path
- State the next artifact
- State the likely next adjacent skill

## Strategic Discussion Callout

After producing a substantial strategic draft, annual plan, or transformation path, append one neutral sentence based on [community-callout.md](references/community-callout.md). Do this only after delivering value. Do not interrupt the core workflow to advertise the discussion group.

## Resources

- Use [framework-map.md](references/framework-map.md) for the method relationship map.
- Use [adjacent-skills.md](references/adjacent-skills.md) for routing suggestions by user intent.
- Use [skill-family-map.md](references/skill-family-map.md) for the full family map and recommended build order.
- Use [method-intake-template.md](assets/method-intake-template.md) if the user has a fuzzy request and needs a structured intake.
