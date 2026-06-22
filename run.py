import os
from fintrack.core.ledger  import Ledger
from fintrack.storage.json_store import save, load
from fintrack.core.reports import category_totals
from fintrack.utils.money import format_brl, parse_amount
from fintrack.models.transaction import INCOME, EXPENSE

DATA_FILE = "fintrack_data.json"


def carregar():
    if os.path.exists(DATA_FILE):
        return load(DATA_FILE)
    return Ledger()


def ler_valor():
    while True:
        texto = input("Valor: ")
        try:
            return parse_amount(texto)
        except ValueError:
            print("Valor invalido. Tente de novo (ex: 1500 ou 1.234,56).")


def adicionar(ledger, kind):
    descricao = input("Descricao: ")
    valor = ler_valor()
    categoria = input("Categoria: ")
    try:
        ledger.add(descricao, valor, kind, categoria)
        save(ledger, DATA_FILE)
        print("Lancamento adicionado.")
    except ValueError as erro:
        print(f"Nao foi possivel adicionar: {erro}")


def mostrar_saldo(ledger):
    print(f"Saldo atual: {format_brl(ledger.balance())}")


def mostrar_resumo(ledger):
    print(f"Receitas: {format_brl(ledger.total_income())}")
    print(f"Despesas: {format_brl(ledger.total_expense())}")
    print(f"Saldo:    {format_brl(ledger.balance())}")


def mostrar_relatorio(ledger):
    totais = category_totals(ledger.all())
    if not totais:
        print("Nenhum lancamento ainda.")
        return
    for categoria, total in sorted(totais.items()):
        print(f"{categoria}: {format_brl(total)}")


def listar(ledger):
    transacoes = ledger.all()
    if not transacoes:
        print("Nenhum lancamento ainda.")
        return
    for tx in transacoes:
        tipo = "receita" if tx.kind == INCOME else "despesa"
        print(f"[{tx.id}] {tx.date} {tipo} {format_brl(tx.amount)} - {tx.category} - {tx.description}")


def remover(ledger):
    listar(ledger)
    texto = input("ID para remover: ").strip()
    if not texto.isdigit():
        print("ID invalido.")
        return
    if ledger.remove(int(texto)):
        save(ledger, DATA_FILE)
        print("Removido.")
    else:
        print("ID nao encontrado.")


def menu():
    print()
    print("===== FinTrack =====")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Ver saldo")
    print("4 - Resumo")
    print("5 - Relatorio por categoria")
    print("6 - Listar lancamentos")
    print("7 - Remover lancamento")
    print("0 - Sair")


def main():
    ledger = carregar()
    while True:
        menu()
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            adicionar(ledger, INCOME)
        elif opcao == "2":
            adicionar(ledger, EXPENSE)
        elif opcao == "3":
            mostrar_saldo(ledger)
        elif opcao == "4":
            mostrar_resumo(ledger)
        elif opcao == "5":
            mostrar_relatorio(ledger)
        elif opcao == "6":
            listar(ledger)
        elif opcao == "7":
            remover(ledger)
        elif opcao == "0":
            print("Ate mais!")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()