# FinTrack - Controle de Financas Pessoais

## 1. Membros do Grupo

- Caio Eloi Campos
- Thiago Silva Santos
- Victor Augusto Hon Fonseca

## 2. Explicacao do Sistema

O **FinTrack** e uma aplicacao de linha de comando (CLI) para controle de financas pessoais. O sistema permite que o usuario registre receitas e despesas, visualize seu saldo atual, filtre transacoes por categoria e acompanhe um resumo financeiro.

### Funcionalidades principais:
- Cadastro de transacoes (receita ou despesa) com valor, categoria, descricao e data
- Listagem de transacoes
- Calculo automatico de saldo (total de receitas menos total de despesas)
- Resumo financeiro com totais de receita, despesa e saldo
- Relatorio por categoria
- Remocao de transacoes

A interacao com o sistema e feita inteiramente via terminal, atraves de um menu interativo ou por comandos diretos.

O foco do projeto e demonstrar como testes de software (unitarios e de integracao) contribuem para a manutencao e confiabilidade de um sistema ao longo do tempo.

## 3. Tecnologias

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Linguagem | Python 3 | Simples, moderno, facil de testar e com excelente suporte a testes automatizados |
| Interface | CLI (argparse) | Leve, sem dependencias externas, interacao direta pelo terminal |
| Persistencia | JSON (arquivo local) | Sem necessidade de servidor de banco de dados, ideal para projetos academicos |
| Testes | pytest + pytest-cov | Padrao da comunidade Python, cobertura de codigo integrada |
| CI | GitHub Actions | Executa todos os testes automaticamente a cada push |
| Cobertura | Codecov | Monitoramento de cobertura de testes |

## 4. Como Executar

### Pre-requisitos
- Python 3.10+

### Instalacao
```bash
pip install -r requirements.txt
```

### Uso interativo (menu)
```bash
python run.py
```

### Uso por comandos diretos
```bash
# Adicionar transacao
python -m fintrack add --description "Salario" --amount 5000 --kind income --category trabalho

# Listar transacoes
python -m fintrack list

# Ver saldo
python -m fintrack balance

# Resumo financeiro
python -m fintrack summary

# Relatorio por categoria
python -m fintrack report
```

## 5. Como Executar os Testes

```bash
# Rodar todos os testes
pytest

# Rodar com cobertura
pytest --cov=fintrack --cov-report=term-missing
```
