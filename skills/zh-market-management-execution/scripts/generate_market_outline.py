#!/usr/bin/env python3
"""
Generate a concise market management outline.
"""

from __future__ import annotations

import argparse


MODES = {
    "market-analysis": [
        "市场边界与细分逻辑",
        "目标细分与客户场景",
        "竞争与渠道格局",
        "机会排序",
        "对战略或产品的含义",
        "关键假设与风险",
    ],
    "opportunity-ranking": [
        "机会池",
        "价值与吸引力",
        "战略适配度",
        "执行负担与风险",
        "建议优先级",
        "下一步动作",
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
