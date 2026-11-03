# Financial System

Sistema de controle financeiro pessoal desenvolvido com FastAPI e SQLite.

## Contas do sistema

O sistema deverá reconhecer três tipos de conta:

1. **Conta principal:** dinheiro disponível em conta.
2. **Vale-refeição (VR):** saldo disponibilizado para alimentação.
3. **Vale-transporte (VT):** saldo disponibilizado para transporte.

### Regras de saldo

- A conta principal deverá considerar apenas o salário líquido, ou seja, o valor recebido após os descontos.
- O VR deverá considerar exclusivamente os valores depositados ou disponibilizados como benefício.
- O VT deverá considerar exclusivamente os valores depositados ou disponibilizados como benefício.
- Cada conta deverá possuir seu próprio saldo.
- Uma despesa deverá descontar o saldo da conta utilizada na transação.
- Os saldos dos benefícios não deverão ser somados ao saldo disponível da conta principal.