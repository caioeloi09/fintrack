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
