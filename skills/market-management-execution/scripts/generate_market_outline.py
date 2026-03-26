#!/usr/bin/env python3
"""
Generate a concise market management outline.
"""

from __future__ import annotations

import argparse


MODES = {
    "market-analysis": [
        "Market boundary and segmentation logic",
        "Target segments and customer scenarios",
        "Competitive and channel context",
        "Opportunity ranking",
        "Implications for strategy or product",
        "Key assumptions and risks",
    ],
    "opportunity-ranking": [
        "Opportunity pool",
        "Value and attractiveness",
        "Strategic fit",
        "Execution burden and risk",
        "Recommended priority",
        "Next actions",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a market management outline.")
    parser.add_argument("--mode", choices=sorted(MODES), default="market-analysis")
    args = parser.parse_args()

    for index, section in enumerate(MODES[args.mode], start=1):
        print(f"{index}. {section}")


if __name__ == "__main__":
    main()
