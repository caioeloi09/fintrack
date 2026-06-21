from datetime import date
import pytest
from fintrack.ledger import Ledger


def test_add_income_increases_balance():
    ledger = Ledger()
    ledger.add_income("salary", 1000, "work")
    assert ledger.balance() == 1000


def test_add_expense_decreases_balance():
    ledger = Ledger()
    ledger.add_income("salary", 1000, "work")
    ledger.add_expense("rent", 400, "home")
    assert ledger.balance() == 600


def test_add_returns_created_transaction():
    ledger = Ledger()
    tx = ledger.add_expense("coffee", 8, "food")
    assert tx.description == "coffee"
    assert tx.amount == 8


def test_add_assigns_sequential_ids():
    ledger = Ledger()
    first = ledger.add_income("a", 10, "x")
    second = ledger.add_income("b", 20, "x")
    assert first.id == 1
    assert second.id == 2


def test_add_with_negative_amount_raises():
    ledger = Ledger()
    with pytest.raises(ValueError):
        ledger.add_expense("bad", -5, "food")


def test_add_with_zero_amount_raises():
    ledger = Ledger()
    with pytest.raises(ValueError):
        ledger.add_income("bad", 0, "work")


def test_add_with_invalid_kind_raises():
    ledger = Ledger()
    with pytest.raises(ValueError):
        ledger.add("bad", 10, "transfer", "food")


def test_add_with_empty_description_raises():
    ledger = Ledger()
    with pytest.raises(ValueError):
        ledger.add_expense("", 10, "food")


def test_add_with_whitespace_description_raises():
    ledger = Ledger()
    with pytest.raises(ValueError):
        ledger.add_expense("   ", 10, "food")


def test_balance_empty_ledger_is_zero():
    assert Ledger().balance() == 0


def test_total_income():
    ledger = Ledger()
    ledger.add_income("a", 100, "work")
    ledger.add_income("b", 50, "work")
    ledger.add_expense("c", 30, "food")
    assert ledger.total_income() == 150


def test_total_expense():
    ledger = Ledger()
    ledger.add_expense("a", 30, "food")
    ledger.add_expense("b", 20, "food")
    assert ledger.total_expense() == 50


def test_remove_existing_transaction():
    ledger = Ledger()
    tx = ledger.add_expense("a", 10, "food")
    assert ledger.remove(tx.id) is True
    assert ledger.count() == 0


def test_remove_nonexistent_returns_false():
    ledger = Ledger()
    assert ledger.remove(99) is False


def test_get_existing_transaction():
    ledger = Ledger()
    tx = ledger.add_income("a", 10, "work")
    assert ledger.get(tx.id) == tx


def test_get_nonexistent_returns_none():
    ledger = Ledger()
    assert ledger.get(99) is None
