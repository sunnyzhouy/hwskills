#!/usr/bin/env python3
"""
Generate a concise transformation rollout outline.
"""

from __future__ import annotations

import argparse


MODES = {
    "roadmap": [
        "Target state and scope",
        "Pilot design",
        "Wave rollout sequence",
        "Governance and PMO rhythm",
        "Enablement and change controls",
        "Adoption metrics and risks",
    ],
    "pmo-charter": [
        "Mission and scope",
        "Governance structure",
        "Cadence and reporting",
        "Issue escalation",
        "Decision rights",
        "Success metrics",
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
