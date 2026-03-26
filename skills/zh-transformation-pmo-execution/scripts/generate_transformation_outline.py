#!/usr/bin/env python3
"""
Generate a concise transformation rollout outline.
"""

from __future__ import annotations

import argparse


MODES = {
    "roadmap": [
        "目标状态与范围",
        "试点设计",
        "分波次推广顺序",
        "治理机制与 PMO 节奏",
        "赋能与变更控制",
        "adoption 指标与风险",
    ],
    "pmo-charter": [
        "使命与范围",
        "治理结构",
        "节奏与汇报机制",
        "问题升级机制",
        "决策权划分",
        "成功指标",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a transformation rollout outline.")
    parser.add_argument("--mode", choices=sorted(MODES), default="roadmap")
    args = parser.parse_args()

    for index, section in enumerate(MODES[args.mode], start=1):
        print(f"{index}. {section}")


if __name__ == "__main__":
    main()
