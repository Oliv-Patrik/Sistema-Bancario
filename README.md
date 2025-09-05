# Sistema Bancário Simples em Python

## 📜 Descrição

Este projeto é um sistema bancário simples desenvolvido em Python como um exercício de estudo. Ele simula as operações básicas de uma conta bancária, como depósitos, saques, transferências e a visualização de extratos. O sistema é construído utilizando os princípios de Programação Orientada a Objetos (POO).

## ✨ Funcionalidades

O sistema implementa as seguintes funcionalidades:

-   **Criação de Cliente e Conta:** Permite o cadastro de novos clientes (Pessoa Física) e a criação de uma conta corrente associada a eles.
-   **Validação de CPF:** Impede que o mesmo CPF seja cadastrado mais de uma vez.
-   **Operações Bancárias:**
    -   **Depósito:** Adicionar valores à conta.
    -   **Saque:** Retirar valores da conta, com um limite de 3 saques diários e um valor máximo de R$ 500,00 por saque.
    -   **Transferência:** Enviar valores de uma conta para outra.
-   **Extrato:** Exibe todas as transações realizadas na conta e o saldo atual.

## 🛠️ Estrutura do Código

O projeto é estruturado com as seguintes classes:

-   `PessoaFisica`: Classe base que representa uma pessoa física com atributos como nome, CPF e senha.
-   `Cliente`: Herda de `PessoaFisica` e representa um cliente do banco.
-   `Banco`: Classe que gerencia os clientes cadastrados.
-   `Conta`: Representa a conta bancária de um cliente, onde as operações são realizadas.
-   `Transacao`: Classe para registrar as transações (não totalmente implementada no exemplo).

## 🚀 Como Utilizar

Para testar o sistema, basta executar o arquivo `Sistema-Bancario.py`. O código de exemplo no final do arquivo demonstra como criar um banco, registrar um cliente e criar uma conta.

```python
# Exemplo de uso
banco = Banco()

# Tentativa de criar uma conta com um novo CPF
cliente1 = Cliente("João", "12345678900", "senha123")
cliente1.criar_conta(banco)

# Tentativa de criar outra conta com o mesmo CPF
cliente2 = Cliente("Maria", "12345678900", "senha123")
cliente2.criar_conta(banco)  # Deve informar que o CPF já está cadastrado

# Realizando operações na conta do cliente1
if cliente1.conta:
    cliente1.conta.depositar(1000)
    cliente1.conta.sacar(200)
    cliente1.conta.exibir_extrato()
