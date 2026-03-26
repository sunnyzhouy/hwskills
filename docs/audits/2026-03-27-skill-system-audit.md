# Skill System Audit

Date: 2026-03-27

## Scope

This audit evaluates two skill systems:

1. The Huawei-oriented skill family in this repository
2. The gstack planning/review family used as the comparison baseline

The audit standard follows the `skill-creator` philosophy rather than a single-task outcome comparison. The question is not only "which one gives stronger output on a hard prompt", but "which one is designed as a better skill system for repeatable use by another Codex instance".

## Audit dimensions

The following dimensions were used:

1. Trigger precision
2. Layering and composability
3. Abstraction vs execution balance
4. Progressive disclosure quality
5. Resource leverage
6. Validation maturity
7. Operational friction
8. Accessibility to target users
9. Maintainability
10. Task-fit to claimed domain

## Summary scores

### Huawei skill family

Score: 8.4/10

Why it scores well:

- Thin router design
- Clear principles layer plus execution layer split
- Good fit for strategy -> market -> product -> development/service/transformation work
- Small, task-directed `SKILL.md` files that follow progressive disclosure well
- Real reusable resources in `scripts/`, `references/`, and `assets/`

Main weaknesses:

- English and Chinese families are duplicated, which creates drift risk
- Chinese family is partially localized at the entry layer but still shares deeper English resources in places
- Router fallback scripts remain heuristic rather than robust
- Validation exists, but not yet as a formal forward-test suite

### gstack planning/review family

Score: 7.3/10

Why it scores well:

- Very strong single-skill power
- Excellent rigor for plan review, edge cases, and challenge posture
- Strong operational conventions, telemetry, and protocol maturity

Main weaknesses:

- Very large `SKILL.md` bodies, which are expensive in context
- Significant repeated boilerplate across skills
- High operational friction before reaching useful work
- More like an operating system than a lean skill under `skill-creator` principles

## Key evidence

Representative `SKILL.md` sizes:

- `huawei-methods`: 75 lines
- `zh-huawei-methods`: 73 lines
- `gstack`: 667 lines
- `plan-ceo-review`: 1314 lines
- `plan-eng-review`: 882 lines

Structural observations:

- Huawei family keeps the router thin and pushes detail into references
- gstack keeps a large amount of common protocol directly in each skill body
- Huawei family is highly domain-fit
- gstack is highly powerful but more generalized and more ceremonious

## Findings by dimension

### 1. Trigger precision

Huawei family: strong

- Router descriptions closely match the real business tasks the family claims to solve
- Chinese and English entry skills are phrased in practical business language

gstack family: medium

- Triggering for plan review is clear once the user is already in planning mode
- The broader `gstack` entry point is optimized for stage suggestion, not domain-specialized triggering

### 2. Layering and composability

Huawei family: excellent

- Router -> principles -> execution is the correct architecture for methodology skills
- Adjacent handoffs are explicit

gstack family: strong but different

- Stage-specific skill map is broad and useful
- The family is composable, but not in a domain workflow sense

### 3. Abstraction vs execution balance

Huawei family: strong

- Principles skills provide abstraction
- Execution skills stay directly usable

gstack family: mixed

- Review skills are very strong at abstraction and challenge
- They are not meant to be primary execution artifacts for industry-method workflows

### 4. Progressive disclosure quality

Huawei family: strong

- Thin router
- Details pushed into references and templates

gstack family: weak against `skill-creator` standards

- Large inline instructions
- High body size before references become necessary

### 5. Resource leverage

Huawei family: strong

- Scripts produce reusable outlines and checklists
- Templates and references directly support repeat work

gstack family: medium

- The leverage is in protocol and system behavior more than in reusable task assets

### 6. Validation maturity

Huawei family: medium

- Quick validation and script spot checks were completed
- Forward testing exists but is not yet formalized as a suite

gstack family: strong

- Mature telemetry and protocol discipline
- Stronger runtime conventions

### 7. Operational friction

Huawei family: low friction

- Easier to trigger and stay on task
- Lower ceremony

gstack family: high friction

- Heavy preamble
- Many operational checks before substantive work

### 8. Accessibility

Huawei family: strong

- Chinese family lowers access cost for intended users
- Business-language entry points improve reach

gstack family: medium

- Extremely powerful for power users
- More intimidating for casual or business-facing usage

### 9. Maintainability

Huawei family: mixed

- Individual skills are maintainable
- Dual-language duplication is the main long-term risk

gstack family: mixed to weak

- Central conventions are powerful
- Repetition and body size raise maintenance cost

### 10. Task-fit

Huawei family: excellent for methodology work

- Purpose-built for strategic and operational methodology

gstack family: excellent for challenge/review, weaker for direct methodology execution

## Final judgment

If the question is "which system is better designed as a methodology skill family under `skill-creator` principles", the Huawei family is better.

If the question is "which system is better at high-pressure challenge and review on a plan", gstack remains better.

These are not contradictory results. They are different optimization targets.

## Priority recommendations

### P0

- Reduce drift risk between English and Chinese Huawei families
- Define which Chinese skills are fully localized versus entry-layer localized

### P1

- Create a formal forward-test suite for the Huawei family
- Improve router heuristics beyond keyword routing

### P2

- Refactor shared Huawei family guidance into fewer shared source artifacts
- Continue localizing deeper references and templates in the Chinese family
