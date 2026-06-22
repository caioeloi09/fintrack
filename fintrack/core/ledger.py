from datetime import date
from ..models.transaction import Transaction, INCOME, EXPENSE


class Ledger:
    def __init__(self):
        self._transactions = []
        self._next_id = 1

    def add(self, description, amount, kind, category, on=None):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if kind not in (INCOME, EXPENSE):
            raise ValueError("invalid kind")
        if not description.strip():
            raise ValueError("description is required")
        if on is None:
            on = date.today()
        tx = Transaction(self._next_id, on, description, round(amount, 2), kind, category)
        self._transactions.append(tx)
        self._next_id += 1
        return tx

    def add_income(self, description, amount, category, on=None):
        return self.add(description, amount, INCOME, category, on)

    def add_expense(self, description, amount, category, on=None):
        return self.add(description, amount, EXPENSE, category, on)

    def add_transaction(self, tx):
        self._transactions.append(tx)
        self._next_id = max(self._next_id, tx.id + 1)

    def remove(self, tx_id):
        for tx in self._transactions:
            if tx.id == tx_id:
                self._transactions.remove(tx)
                return True
        return False

    def get(self, tx_id):
        for tx in self._transactions:
            if tx.id == tx_id:
                return tx
        return None

    def all(self):
        return list(self._transactions)

    def count(self):
        return len(self._transactions)

    def balance(self):
        return round(sum(tx.signed_amount() for tx in self._transactions), 2)

    def total_income(self):
        return round(sum(tx.amount for tx in self._transactions if tx.kind == INCOME), 2)

    def total_expense(self):
        return round(sum(tx.amount for tx in self._transactions if tx.kind == EXPENSE), 2)

    def filter_by_category(self, category):
        return [tx for tx in self._transactions if tx.category == category]

    def filter_by_kind(self, kind):
        return [tx for tx in self._transactions if tx.kind == kind]

    def filter_by_month(self, year, month):
        return [tx for tx in self._transactions if tx.date.year == year and tx.date.month == month]

    def categories(self):
        return sorted(set(tx.category for tx in self._transactions))
