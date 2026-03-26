#!/usr/bin/env python3
"""
Generate a concise ITR checklist.
"""

from __future__ import annotations

import argparse


CHECKLISTS = {
    "operating-model": [
        "定义问题分类与严重级别逻辑",
        "明确受理渠道与归属",
        "设定升级触发条件与责任人",
        "定义关闭证据",
        "设定服务与解决指标",
        "建立产品与质量反馈回路",
    ],
    "escalation": [
        "问题级别已分类",
        "当前责任人明确",
        "已达到升级触发条件",
        "决策 owner 已命名",
        "客户沟通方案存在",
        "关闭标准已定义",
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
