from __future__ import annotations

import csv
import io
import random
import uuid
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path


@dataclass(frozen=True)
class Column:
    name: str
    kind: str
    nullable: bool
    example: str


def load_schema(path: Path) -> list[Column]:
    rows = csv.DictReader(path.read_text(encoding="utf-8").splitlines())
    return [
        Column(
            name=str(row["column"]),
            kind=str(row["type"]),
            nullable=str(row.get("nullable", "false")).lower() == "true",
            example=str(row.get("example", "")),
        )
        for row in rows
    ]


def value_for(column: Column, index: int, rng: random.Random) -> str:
    if column.nullable and rng.random() < 0.2:
        return ""
    if column.kind == "email":
        return f"user{index}@example.test"
    if column.kind == "name":
        return f"Sample User {index}"
    if column.kind == "company":
        return f"Example Co {index}"
    if column.kind == "date":
        return (date(2026, 1, 1) + timedelta(days=index)).isoformat()
    if column.kind == "integer":
        return str(1000 + index)
    if column.kind == "category":
        choices = [item for item in column.example.split("|") if item]
        return rng.choice(choices or ["sample"])
    if column.kind == "uuid":
        return str(uuid.UUID(int=index))
    if column.kind == "text":
        return f"synthetic note {index}"
    raise ValueError(f"unsupported type: {column.kind}")


def generate_rows(columns: list[Column], rows: int, seed: int) -> list[dict[str, str]]:
    rng = random.Random(seed)
    output: list[dict[str, str]] = []
    for index in range(1, rows + 1):
        output.append({column.name: value_for(column, index, rng) for column in columns})
    return output


def render_csv(rows: list[dict[str, str]]) -> str:
    if not rows:
        return ""
    handle = io.StringIO()
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    return handle.getvalue()
