from datetime import date
from fintrack.money import format_brl, parse_amount
from fintrack.models import Transaction, INCOME, EXPENSE


def test_signed_amount_income_is_positive():
    tx = Transaction(1, date(2025, 1, 1), "x", 100, INCOME, "work")
    assert tx.signed_amount() == 100


def test_signed_amount_expense_is_negative():
    tx = Transaction(1, date(2025, 1, 1), "x", 100, EXPENSE, "food")
    assert tx.signed_amount() == -100
