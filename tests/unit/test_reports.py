from datetime import date
from fintrack.models.transaction import Transaction, INCOME, EXPENSE
from fintrack.core.reports import (
    category_totals,
    category_breakdown,
    top_expense,
    monthly_summary,
)


def expense(amount, category, day=1):
    return Transaction(1, date(2025, 1, day), "x", amount, EXPENSE, category)


def income(amount, category, day=1):
    return Transaction(1, date(2025, 1, day), "x", amount, INCOME, category)


def test_category_totals_sums_by_category():
    transactions = [expense(10, "food"), expense(20, "food"), expense(5, "home")]
    assert category_totals(transactions) == {"food": 30, "home": 5}


def test_category_totals_empty_is_empty_dict():
    assert category_totals([]) == {}


def test_category_breakdown_returns_percentages():
    transactions = [expense(75, "food"), expense(25, "home")]
    result = category_breakdown(transactions)
    assert result == {"food": 75.0, "home": 25.0}


def test_category_breakdown_ignores_income():
    transactions = [expense(100, "food"), income(500, "work")]
    result = category_breakdown(transactions)
    assert result == {"food": 100.0}


def test_category_breakdown_empty_returns_empty():
    assert category_breakdown([]) == {}


def test_top_expense_returns_largest():
    transactions = [expense(10, "food"), expense(90, "home"), expense(50, "fun")]
    assert top_expense(transactions).amount == 90
