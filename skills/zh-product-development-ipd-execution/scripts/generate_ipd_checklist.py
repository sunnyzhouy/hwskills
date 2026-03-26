#!/usr/bin/env python3
"""
Generate a concise IPD execution checklist.
"""

from __future__ import annotations

import argparse


CHECKLISTS = {
    "plan": [
        "确认已批准范围与排除项",
        "定义里程碑与工作流",
        "分配责任人",
        "设定阶段门标准",
        "列出主要风险与质量控制",
        "准备评审材料",
    ],
    "review": [
        "阶段目标清晰",
        "退出标准明确",
        "风险已命名且有人负责",
        "跨部门依赖可见",
        "质量证据已准备",
        "下一步决策与责任人清晰",
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
