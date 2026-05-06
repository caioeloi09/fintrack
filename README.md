# FinTrack - Controle de Financas Pessoais

## 1. Membros do Grupo

- Caio Eloi Campos
- Thiago Silva Santos
- Victor Augusto Hon Fonseca

## 2. Explicacao do Sistema

O **FinTrack** e uma aplicacao web simples para controle de financas pessoais. O sistema permite que o usuario registre receitas e despesas, visualize seu saldo atual, filtre transacoes por categoria e periodo, e acompanhe um resumo financeiro mensal.

### Funcionalidades principais:
- Cadastro de transacoes (receita ou despesa) com valor, categoria, descricao e data
- Listagem e filtragem de transacoes por tipo, categoria e intervalo de datas
- Calculo automatico de saldo (total de receitas menos total de despesas)
- Resumo mensal com totais por categoria
- Edicao e exclusao de transacoes

O foco do projeto e demonstrar como testes de software (unitarios, de integracao e E2E) contribuem para a manutencao e confiabilidade de um sistema ao longo do tempo.

## 3. Tecnologias

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Backend | Python 3 + FastAPI | Simples, moderno, facil de testar e com excelente suporte a testes automatizados |
| Banco de dados | SQLite + SQLAlchemy | Leve, sem necessidade de servidor, ideal para projetos academicos |
| Frontend | HTML + CSS + JavaScript (Vanilla) | Sem complexidade de framework, foco nas funcionalidades |
| Testes unitarios | pytest + pytest-cov | Padrao da comunidade Python, cobertura de codigo integrada |
| Testes de integracao | pytest + httpx (TestClient do FastAPI) | Testa endpoints HTTP reais sem subir servidor externo |
| Testes E2E | Bruno | Ferramenta open source para testes de API, utilizada no seminario da disciplina |
| CI | GitHub Actions | Executa todos os testes automaticamente a cada push |
