from __future__ import annotations

from privacy_sample_maker.cli import main
from privacy_sample_maker.core import Column, generate_rows, render_csv, value_for


def test_email_does_not_copy_example() -> None:
    column = Column("email", "email", False, "real@example.com")
    assert value_for(column, 1, __import__("random").Random(1)) != "real@example.com"


def test_category_uses_allowed_values() -> None:
    column = Column("plan", "category", False, "free|pro")
    assert value_for(column, 1, __import__("random").Random(1)) in {"free", "pro"}


def test_generation_is_deterministic() -> None:
    columns = [Column("id", "integer", False, "")]
    assert generate_rows(columns, 2, 5) == generate_rows(columns, 2, 5)


def test_nullable_can_emit_blank() -> None:
    column = Column("notes", "text", True, "")
    rows = generate_rows([column], 20, 1)
    assert any(row["notes"] == "" for row in rows)


def test_csv_render_has_header() -> None:
    assert render_csv([{"a": "1"}]).startswith("a")


def test_cli_writes_output(tmp_path) -> None:
    schema = tmp_path / "schema.csv"
    out = tmp_path / "sample.csv"
    schema.write_text("column,type,nullable,example\nemail,email,false,real@example.com\n", encoding="utf-8")
    assert main([str(schema), "--rows", "1", "--output", str(out)]) == 0
    assert "user1@example.test" in out.read_text(encoding="utf-8")


def test_cli_help(capsys) -> None:
    try:
        main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0
    assert "privacy" in capsys.readouterr().out.lower()
