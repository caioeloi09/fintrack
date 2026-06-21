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


def test_cli_list_shows_transactions(tmp_path, capsys):
    path = str(tmp_path / "data.json")
    main(["--file", path, "add", "--description", "coffee",
          "--amount", "8", "--kind", "expense", "--category", "food"])
    capsys.readouterr()
    main(["--file", path, "list"])
    output = capsys.readouterr().out
    assert "coffee" in output


def test_cli_report_groups_by_category(tmp_path, capsys):
    path = str(tmp_path / "data.json")
    main(["--file", path, "add", "--description", "a",
          "--amount", "10", "--kind", "expense", "--category", "food"])
    main(["--file", path, "add", "--description", "b",
          "--amount", "20", "--kind", "expense", "--category", "food"])
    capsys.readouterr()
    main(["--file", path, "report"])
    output = capsys.readouterr().out
    assert "food" in output
    assert "30,00" in output


def test_cli_no_command_returns_error_code(capsys):
    code = main([])
    assert code == 1


def test_cli_end_to_end_subprocess(tmp_path):
    path = str(tmp_path / "data.json")
    subprocess.run(
        [sys.executable, "-m", "fintrack", "--file", path, "add",
         "--description", "salary", "--amount", "1500",
         "--kind", "income", "--category", "work"],
        check=True,
    )
    result = subprocess.run(
        [sys.executable, "-m", "fintrack", "--file", path, "balance"],
        capture_output=True, text=True, check=True,
    )
    assert "1.500,00" in result.stdout