#!/usr/bin/env python3
"""
Generate a concise product planning outline.
"""

from __future__ import annotations

import argparse


MODES = {
    "roadmap": [
        "Planning scope and horizon",
        "Target segments and scenarios",
        "Roadmap options",
        "Priority capabilities",
        "Release themes and dependencies",
        "Handoff assumptions for development",
    ],
    "release-plan": [
        "Release objective",
        "In-scope capabilities",
        "Out-of-scope items",
        "Dependencies and risks",
        "Milestones and decision points",
        "Success metrics",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a product planning outline.")
    parser.add_argument("--mode", choices=sorted(MODES), default="roadmap")
    args = parser.parse_args()

    for index, section in enumerate(MODES[args.mode], start=1):
        print(f"{index}. {section}")


if __name__ == "__main__":
    main()
