from __future__ import annotations

import argparse
from pathlib import Path

from privacy_sample_maker.core import generate_rows, load_schema, render_csv


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate privacy-safe synthetic CSV samples.")
    parser.add_argument("schema", type=Path)
    parser.add_argument("--rows", type=int, default=10)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--output", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    csv_text = render_csv(generate_rows(load_schema(args.schema), args.rows, args.seed))
    if args.output:
        args.output.write_text(csv_text, encoding="utf-8")
    else:
        print(csv_text, end="")
    return 0
