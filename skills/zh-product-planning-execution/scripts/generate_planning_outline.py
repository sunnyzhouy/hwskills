#!/usr/bin/env python3
"""
Generate a concise product planning outline.
"""

from __future__ import annotations

import argparse


MODES = {
    "roadmap": [
        "规划范围与周期",
        "目标细分与客户场景",
        "路标方案选项",
        "优先能力项",
        "版本主题与依赖",
        "交给研发的关键假设",
    ],
    "release-plan": [
        "发布目标",
        "纳入范围的能力项",
        "不纳入范围的项",
        "依赖与风险",
        "里程碑与决策点",
        "成功指标",
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
