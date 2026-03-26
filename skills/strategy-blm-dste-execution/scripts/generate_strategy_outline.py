#!/usr/bin/env python3
"""
Generate a concise strategy or annual-plan outline.
"""

from __future__ import annotations

import argparse


MODES = {
    "strategy": [
        "Business scope and ambition",
        "External change and internal gap",
        "Strategic choices",
        "Capability implications",
        "Major initiatives",
        "Governance, risks, and assumptions",
    ],
    "annual-plan": [
        "Planning boundary and assumptions",
        "Annual objectives",
        "Key initiatives and owners",
        "Quarterly milestones",
        "Metrics and control points",
        "Major risks and review cadence",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a strategy execution outline.")
    parser.add_argument("--mode", choices=sorted(MODES), default="strategy")
    args = parser.parse_args()

    for index, section in enumerate(MODES[args.mode], start=1):
        print(f"{index}. {section}")


if __name__ == "__main__":
    main()
