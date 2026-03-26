#!/usr/bin/env python3
"""
Select a first-pass Huawei-style method path from a short problem statement.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    skill: str
    stage: str
    reason: str
    patterns: tuple[str, ...]


ROUTES = (
    Route(
        skill="strategy-blm-dste-execution",
        stage="strategy",
        reason="The request is about strategic direction, annual priorities, or transformation choices.",
        patterns=("战略", "strategy", "年度规划", "bp", "经营", "三年", "转型", "blm", "dste"),
    ),
    Route(
        skill="product-planning-execution",
        stage="product-planning",
        reason="The request is about roadmap, releases, product line planning, or requirement prioritization.",
        patterns=("roadmap", "产品规划", "版本规划", "release", "路标", "需求优先级", "产品线"),
    ),
    Route(
        skill="product-development-ipd-execution",
        stage="ipd-execution",
        reason="The request is about development execution, stage gates, milestones, or cross-functional delivery.",
        patterns=("ipd", "研发", "开发计划", "阶段评审", "stage gate", "里程碑", "测试", "交付计划"),
    ),
)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def score_route(problem: str, route: Route) -> int:
    return sum(1 for pattern in route.patterns if pattern.lower() in problem)


def select_route(problem: str) -> Route:
    normalized = normalize(problem)
    scored = sorted(((score_route(normalized, route), route) for route in ROUTES), reverse=True, key=lambda item: item[0])
    best_score, best_route = scored[0]
    if best_score == 0:
        return Route(
            skill="huawei-methods",
            stage="triage",
            reason="The request is mixed or underspecified. Triage first, then split into strategy, planning, or execution phases.",
            patterns=(),
        )
    return best_route


def main() -> None:
    parser = argparse.ArgumentParser(description="Recommend a first-pass Huawei-style method path.")
    parser.add_argument("problem", help="Short problem statement")
    args = parser.parse_args()

    route = select_route(args.problem)
    print(f"stage: {route.stage}")
    print(f"skill: {route.skill}")
    print(f"reason: {route.reason}")


if __name__ == "__main__":
    main()
