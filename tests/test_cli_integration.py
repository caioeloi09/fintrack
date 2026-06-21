import subprocess
import sys
from fintrack.cli import main


def test_cli_add_then_balance(tmp_path, capsys):
    path = str(tmp_path / "data.json")
    main(["--file", path, "add", "--description", "salary",
          "--amount", "1000", "--kind", "income", "--category", "work"])
    main(["--file", path, "add", "--description", "rent",
          "--amount", "400", "--kind", "expense", "--category", "home"])
    capsys.readouterr()
    main(["--file", path, "balance"])
    output = capsys.readouterr().out
    assert "600,00" in output


def test_cli_summary(tmp_path, capsys):
    path = str(tmp_path / "data.json")
    main(["--file", path, "add", "--description", "salary",
          "--amount", "1000", "--kind", "income", "--category", "work"])
    capsys.readouterr()
    main(["--file", path, "summary"])
    output = capsys.readouterr().out
    assert "receita" in output
    assert "1.000,00" in output