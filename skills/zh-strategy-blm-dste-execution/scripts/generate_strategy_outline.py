#!/usr/bin/env python3
"""
Generate a concise strategy or annual-plan outline.
"""

from __future__ import annotations

import argparse


MODES = {
    "strategy": [
        "业务范围与战略意图",
        "外部变化与内部差距",
        "关键战略选择",
        "能力含义与建设重点",
        "重大举措组合",
        "治理、风险与前提假设",
    ],
    "annual-plan": [
        "规划边界与前提假设",
        "年度目标",
        "重点举措与责任人",
        "季度里程碑",
        "指标与控制点",
        "主要风险与复盘节奏",
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
