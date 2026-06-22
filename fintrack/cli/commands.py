import argparse
import os

from ..core.ledger import Ledger
from ..core.reports import category_totals
from ..utils.money import format_brl
from ..storage.json_store import load, save

DEFAULT_FILE = "fintrack_data.json"


def get_ledger(path):
    if os.path.exists(path):
        return load(path)
    return Ledger()


def cmd_add(args):
    ledger = get_ledger(args.file)
    ledger.add(args.description, args.amount, args.kind, args.category)
    save(ledger, args.file)
    print(f"adicionado: {args.kind} {format_brl(args.amount)}")


def cmd_list(args):
    ledger = get_ledger(args.file)
    transactions = ledger.all()
    if not transactions:
        print("sem transacoes")
        return
    for tx in transactions:
        print(f"{tx.id} {tx.date} {tx.kind} {format_brl(tx.amount)} {tx.category} {tx.description}")


def cmd_balance(args):
    ledger = get_ledger(args.file)
    print(f"saldo: {format_brl(ledger.balance())}")


def cmd_summary(args):
    ledger = get_ledger(args.file)
    print(f"receita: {format_brl(ledger.total_income())}")
    print(f"despesa: {format_brl(ledger.total_expense())}")
    print(f"saldo: {format_brl(ledger.balance())}")


def cmd_report(args):
    ledger = get_ledger(args.file)
    totals = category_totals(ledger.all())
    if not totals:
        print("sem transacoes")
        return
    for category, total in sorted(totals.items()):
        print(f"{category}: {format_brl(total)}")


def build_parser():
    parser = argparse.ArgumentParser(prog="fintrack")
    parser.add_argument("--file", default=DEFAULT_FILE)
    sub = parser.add_subparsers(dest="command")

    add = sub.add_parser("add")
    add.add_argument("--description", required=True)
    add.add_argument("--amount", type=float, required=True)
    add.add_argument("--kind", choices=["income", "expense"], required=True)
    add.add_argument("--category", required=True)
    add.set_defaults(func=cmd_add)

    listing = sub.add_parser("list")
    listing.set_defaults(func=cmd_list)

    balance = sub.add_parser("balance")
    balance.set_defaults(func=cmd_balance)

    summary = sub.add_parser("summary")
    summary.set_defaults(func=cmd_summary)

    report = sub.add_parser("report")
    report.set_defaults(func=cmd_report)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return 1
    args.func(args)
    return 0
