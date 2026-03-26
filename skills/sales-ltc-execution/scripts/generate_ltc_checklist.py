#!/usr/bin/env python3
"""
Generate a concise LTC checklist.
"""

from __future__ import annotations

import argparse


CHECKLISTS = {
    "operating-model": [
        "Define stage entry and exit criteria",
        "Clarify forecast and deal-review cadence",
        "Map sales to delivery and finance handoffs",
        "List contract and acceptance controls",
        "Set conversion and cash metrics",
        "Name exception escalation owners",
    ],
    "deal-review": [
        "Opportunity stage is valid",
        "Decision makers and blockers are clear",
        "Commercial and delivery risks are visible",
        "Contract path is understood",
        "Next milestone and owner are clear",
        "Collection risks are known",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an LTC checklist.")
    parser.add_argument("--mode", choices=sorted(CHECKLISTS), default="operating-model")
    args = parser.parse_args()

    for index, item in enumerate(CHECKLISTS[args.mode], start=1):
        print(f"{index}. {item}")


if __name__ == "__main__":
    main()
