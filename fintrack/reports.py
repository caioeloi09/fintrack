from .models import INCOME, EXPENSE


def category_totals(transactions):
    totals = {}
    for tx in transactions:
        totals[tx.category] = round(totals.get(tx.category, 0) + tx.amount, 2)
    return totals


def category_breakdown(transactions, kind=EXPENSE):
    selected = [tx for tx in transactions if tx.kind == kind]
    total = sum(tx.amount for tx in selected)
    if total == 0:
        return {}
    breakdown = {}
    for tx in selected:
        breakdown[tx.category] = breakdown.get(tx.category, 0) + tx.amount
    return {c: round(v / total * 100, 2) for c, v in breakdown.items()}


def top_expense(transactions):
    expenses = [tx for tx in transactions if tx.kind == EXPENSE]
    if not expenses:
        return None
    return max(expenses, key=lambda tx: tx.amount)


def monthly_summary(transactions, year, month):
    selected = [tx for tx in transactions if tx.date.year == year and tx.date.month == month]
    income = sum(tx.amount for tx in selected if tx.kind == INCOME)
    expense = sum(tx.amount for tx in selected if tx.kind == EXPENSE)
    return {
        "income": round(income, 2),
        "expense": round(expense, 2),
        "balance": round(income - expense, 2),
    }
