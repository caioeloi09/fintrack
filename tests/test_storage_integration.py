from datetime import date
from fintrack.ledger import Ledger
from fintrack.storage import save, load


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "data.json"
    ledger = Ledger()
    ledger.add_income("salary", 1000, "work", on=date(2025, 1, 1))
    ledger.add_expense("rent", 400, "home", on=date(2025, 1, 2))
    save(ledger, str(path))

    loaded = load(str(path))
    assert loaded.count() == 2
    assert loaded.balance() == 600


def test_load_preserves_categories(tmp_path):
    path = tmp_path / "data.json"
    ledger = Ledger()
    ledger.add_expense("a", 10, "food")
    ledger.add_expense("b", 20, "home")
    save(ledger, str(path))

    loaded = load(str(path))
    assert loaded.categories() == ["food", "home"]


def test_load_continues_id_sequence(tmp_path):
    path = tmp_path / "data.json"
    ledger = Ledger()
    ledger.add_income("a", 10, "work")
    ledger.add_income("b", 20, "work")
    save(ledger, str(path))

    loaded = load(str(path))
    new_tx = loaded.add_expense("c", 5, "food")
    assert new_tx.id == 3
