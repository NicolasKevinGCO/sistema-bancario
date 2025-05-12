# 💰 Sistema Bancário em Python

Este é um sistema bancário simples feito em Python, com um menu interativo para operações como depósito, saque, consulta de saldo e extrato. Ele funciona via terminal e foi desenvolvido com fins educacionais.

## 📌 Funcionalidades

- ✅ Depósito de valores
- ✅ Saques com limite por operação e limite diário
- ✅ Consulta de saldo atual
- ✅ Geração de extrato de movimentações
- ✅ Menu interativo até o usuário encerrar

## 📖 Regras do Sistema

- 💸 Saldo inicial: R$ 10.000.000,00
- 🏦 Limite por saque: R$ 500,00
- 🔁 Limite de 3 saques por execução
- ❌ Não são aceitos valores negativos ou inválidos

## ⚙️ Como funciona

- `menu()`: Exibe o menu de opções para o usuário.
- `saque()`: Permite saques dentro das regras de limite e saldo.
- `depositar()`: Realiza depósitos válidos no saldo.
- `main()`: Executa o programa em loop até o usuário sair.

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Salve o arquivo como `sistema_bancario.py`.
3. No terminal, execute:

```bash
python sistema_bancario.py
