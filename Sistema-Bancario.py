class PessoaFisica:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

class Cliente(PessoaFisica):
    def __init__(self, nome, cpf, senha):
        super().__init__(nome, cpf, senha)
        self.conta = None

    def criar_conta(self, banco):
        if self.conta is None and banco.registrar_cliente(self):
            agencia = "0001"
            numero_conta = len(banco.clientes) + 1
            self.conta = Conta(agencia, numero_conta, self)
            print(f"Conta corrente criada com sucesso! Número da conta: {agencia}-{numero_conta}")
        else:
            print("CPF já cadastrado ou cliente já possui uma conta.")

class Banco:
    def __init__(self):
        self.clientes = []

    def registrar_cliente(self, cliente):
        if cliente.cpf not in [c.cpf for c in self.clientes]:
            self.clientes.append(cliente)
            return True
        else:
            return False

class Conta:
    LIMITE_SAQUES = 3

    def __init__(self, agencia, numero_conta, cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0
        self.extrato = ""
        self.limite = 500
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= Conta.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.extrato += f"Transferência: R$ {valor:.2f}\n"
            conta_destino.extrato += f"Transferência recebida: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor inválido ou saldo insuficiente.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

class Transacao:
    def __init__(self, valor, data, tipo):
        self.valor = valor
        self.data = data
        self.tipo = tipo

# Exemplo de uso
banco = Banco()

# Tentativa de criar uma conta com um novo CPF
cliente1 = Cliente("João", "12345678900", "senha123")
cliente1.criar_conta(banco)

# Tentativa de criar outra conta com o mesmo CPF
cliente2 = Cliente("Maria", "12345678900", "senha123")
cliente2.criar_conta(banco)  # Deve informar que o CPF já está cadastrado
