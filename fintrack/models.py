from dataclasses import dataclass
from datetime import date

INCOME = "income"
EXPENSE = "expense"


@dataclass
class Transaction:
    id: int
    date: date
    description: str
    amount: float
    kind: str
    category: str

    def signed_amount(self):
        if self.kind == EXPENSE:
            return -self.amount
        return self.amount
