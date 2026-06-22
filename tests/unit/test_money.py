from datetime import date
from fintrack.utils.money import format_brl, parse_amount
from fintrack.models.transaction import Transaction, INCOME, EXPENSE


def test_signed_amount_income_is_positive():
    tx = Transaction(1, date(2025, 1, 1), "x", 100, INCOME, "work")
    assert tx.signed_amount() == 100


def test_signed_amount_expense_is_negative():
    tx = Transaction(1, date(2025, 1, 1), "x", 100, EXPENSE, "food")
    assert tx.signed_amount() == -100


def test_format_brl_simple_value():
    assert format_brl(50) == "R$ 50,00"


def test_format_brl_with_thousands():
    assert format_brl(1234.56) == "R$ 1.234,56"


def test_format_brl_zero():
    assert format_brl(0) == "R$ 0,00"


def test_parse_amount_brazilian_format():
    assert parse_amount("1.234,56") == 1234.56


def test_parse_amount_simple_decimal():
    assert parse_amount("1234.56") == 1234.56


def test_parse_amount_integer():
    assert parse_amount("10") == 10.0


def test_parse_amount_with_currency_symbol():
    assert parse_amount("R$ 50,00") == 50.0
