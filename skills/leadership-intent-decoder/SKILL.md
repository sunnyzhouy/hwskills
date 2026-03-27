---
name: leadership-intent-decoder
description: Huawei-style leadership-intent decoder for interpreting what a boss, CEO, founder, or business head really means from speeches, meeting notes, chats, comments, and product feedback. Use when Codex needs to extract strategic intent, management thinking, product direction, hidden priorities, and implied constraints, then route them into strategy, market, product, or transformation work. Typical triggers include 'interpret the boss's strategy', 'decode founder thinking', 'translate leadership direction into product actions', and 'what does the CEO actually want'.
---

# Leadership Intent Decoder

## Overview

Translate leadership expression into executable judgment. This skill is for extracting direction, boundaries, priorities, and operating implications from raw leadership communication instead of summarizing slogans.

## Classify The Input First

Start by identifying what kind of source you are reading:

- Speech or interview: look for repeated themes, wording, and warnings
- Meeting notes: look for decisions, vetoes, follow-up pressure, and resource tilt
- Chat, email, comments: look for repeated nudges, negative boundaries, and escalation signals
- Product feedback: identify whether the real issue is direction, pace, quality bar, or expression

For a stricter pass, read [signal-checklist.md](references/signal-checklist.md).

## Three Ways To Use It

- `Decode`: extract the real intent from a raw speech, note set, or comment trail
- `Translate`: turn leadership thinking into strategy, product, market, or org actions
- `Calibrate`: check whether the team's current interpretation is off and explain the misread

## Execution Workflow

1. Separate explicit statements, repeated emphasis, boundary-setting, and implied asks.
2. Distinguish what is explicit from what is only a strong inference.
3. Extract the true direction, pace expectation, resource focus, and control points.
4. State the strategic, market, product, and operating implications.
5. Mark what can already be executed and what should be confirmed with leadership.

## Keep It Abstract But Useful

Call out directly:

- what leadership is really protecting, cutting, or pushing
- which points are explicit instructions versus inference
- where the team may hear "work harder" but leadership actually means "change the operating model"
- which product comments are surface requests versus business-level demands

Do not:

- mistake tone for strategy
- turn one quote into a complete interpretation
- pretend uncertain inference is confirmed fact
- stop at summary instead of deriving action

## Common Output Shapes

- leadership intent brief
- product-direction translation memo
- management-thinking summary with organizational implications
- alignment memo for the team
- clarification questions to take back to leadership

## Clean Handoff

If the user wants artifacts beyond interpretation:

- strategy direction or annual priorities: switch to `huawei-strategy-principles` or `strategy-blm-dste-execution`
- market judgment and target choice: switch to `huawei-market-principles` or `market-management-execution`
- product direction, roadmap, or release planning: switch to `product-planning-execution`
- operating model, rollout, and organizational adoption: switch to `transformation-pmo-execution`
- a compressed executive-facing brief: switch to `byte-exec-brief-en`

## Resources

- Use [signal-checklist.md](references/signal-checklist.md) as the main decoding frame
- Use [common-misreads.md](references/common-misreads.md) to catch typical interpretation errors
