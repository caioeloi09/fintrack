import json
from datetime import date
from .ledger import Ledger
from .models import Transaction


def to_dict(tx):
    return {
        "id": tx.id,
        "date": tx.date.isoformat(),
        "description": tx.description,
        "amount": tx.amount,
        "kind": tx.kind,
        "category": tx.category,
    }


def from_dict(data):
    return Transaction(
        data["id"],
        date.fromisoformat(data["date"]),
        data["description"],
        data["amount"],
        data["kind"],
        data["category"],
    )


def save(ledger, path):
    data = [to_dict(tx) for tx in ledger.all()]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load(path):
    ledger = Ledger()
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        ledger.add_transaction(from_dict(item))
    return ledger
