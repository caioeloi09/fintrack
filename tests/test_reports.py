from datetime import date
from fintrack.models import Transaction, INCOME, EXPENSE
from fintrack.reports import (
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
