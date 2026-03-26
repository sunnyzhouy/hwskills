#!/usr/bin/env python3
"""
Generate a concise LTC checklist.
"""

from __future__ import annotations

import argparse


CHECKLISTS = {
    "operating-model": [
        "定义阶段进入与退出标准",
        "明确预测与 deal review 节奏",
        "映射销售到交付与财务的交接",
        "列出合同与验收控制点",
        "设定转化与回款指标",
        "明确异常升级责任人",
    ],
    "deal-review": [
        "商机阶段判断有效",
        "决策人和阻碍项清晰",
        "商务与交付风险可见",
        "合同路径明确",
        "下一里程碑与责任人清晰",
        "回款风险已识别",
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
