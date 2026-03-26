#!/usr/bin/env python3
"""
Generate a concise IPD execution checklist.
"""

from __future__ import annotations

import argparse


CHECKLISTS = {
    "plan": [
        "Confirm approved scope and exclusions",
        "Define milestones and workstreams",
        "Assign owners",
        "Set stage-gate criteria",
        "List major risks and quality controls",
        "Prepare review package",
    ],
    "review": [
        "Gate objective is clear",
        "Exit criteria are explicit",
        "Risks are named and owned",
        "Cross-functional dependencies are visible",
        "Quality evidence is prepared",
        "Next decision and owner are clear",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an IPD execution checklist.")
    parser.add_argument("--mode", choices=sorted(CHECKLISTS), default="plan")
    args = parser.parse_args()

    for index, item in enumerate(CHECKLISTS[args.mode], start=1):
        print(f"{index}. {item}")


if __name__ == "__main__":
    main()
