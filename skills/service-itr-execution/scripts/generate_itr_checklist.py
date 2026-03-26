#!/usr/bin/env python3
"""
Generate a concise ITR checklist.
"""

from __future__ import annotations

import argparse


CHECKLISTS = {
    "operating-model": [
        "Define issue classes and severity logic",
        "Clarify intake channels and ownership",
        "Set escalation triggers and owners",
        "Define closure evidence",
        "Set service and resolution metrics",
        "Create product and quality feedback loops",
    ],
    "escalation": [
        "Issue severity is classified",
        "Current owner is explicit",
        "Escalation trigger is met",
        "Decision owner is named",
        "Customer communication plan exists",
        "Closure criteria are defined",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an ITR checklist.")
    parser.add_argument("--mode", choices=sorted(CHECKLISTS), default="operating-model")
    args = parser.parse_args()

    for index, item in enumerate(CHECKLISTS[args.mode], start=1):
        print(f"{index}. {item}")


if __name__ == "__main__":
    main()
