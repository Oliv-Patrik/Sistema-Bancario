# Dicionário para armazenar os usuários
usuarios = {}

# Dicionário para armazenar as contas correntes
contas_correntes = []

# Função para registrar um novo usuário
def registrar_usuario():
    nome = input("Informe seu nome: ")
    cpf = input("Informe seu CPF: ")
    senha = input("Informe uma senha: ")

    if cpf in [u["cpf"] for u in usuarios.values()]:
        print("CPF já cadastrado!")
        return

    usuarios[nome] = {"cpf": cpf, "senha": senha, "saldo": 0, "extrato": "", "limite": 500, "numero_saques": 0, "LIMITE_SAQUES": 3}
    criar_conta_corrente(nome)

# Função para criar uma conta corrente
def criar_conta_corrente(nome):
    numero_conta = len(contas_correntes) + 1
    agencia = "0001"
    contas_correntes.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": nome})
    print(f"Conta corrente criada com sucesso! Número da conta: {agencia}-{numero_conta}")

# Função para realizar login
def login():
    nome = input("Informe seu nome: ")
    senha = input("Informe sua senha: ")

    if nome in usuarios and usuarios[nome]["senha"] == senha:
        return nome
    else:
        print("Login ou senha incorretos.")
        return None

# Função para realizar depósito
def depositar(nome, valor):
    if valor > 0:
        usuarios[nome]["saldo"] += valor
        usuarios[nome]["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para realizar saque
def sacar(nome, valor):
    excedeu_saldo = valor > usuarios[nome]["saldo"]
    excedeu_limite = valor > usuarios[nome]["limite"]
    excedeu_saques = usuarios[nome]["numero_saques"] >= usuarios[nome]["LIMITE_SAQUES"]

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        usuarios[nome]["saldo"] -= valor
        usuarios[nome]["extrato"] += f"Saque: R$ {valor:.2f}\n"
        usuarios[nome]["numero_saques"] += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para realizar transferência
def transferir(nome, valor, destino):
    if valor > 0 and valor <= usuarios[nome]["saldo"]:
        usuarios[nome]["saldo"] -= valor
        usuarios[destino]["saldo"] += valor
        usuarios[nome]["extrato"] += f"Transferência: R$ {valor:.2f}\n"
        usuarios[destino]["extrato"] += f"Transferência recebida: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! Valor inválido ou saldo insuficiente.")

# Função para bloquear conta
def bloquear_conta(nome):
    del usuarios[nome]

# Função para exibir extrato
def extrato(nome):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not usuarios[nome]["extrato"] else usuarios[nome]["extrato"])
    print(f"\nSaldo: R$ {usuarios[nome]['saldo']:.2f}")
    print("==========================================")

# Menu principal
menu = """\n
    ================ MENU ================
    [r]\tRegistrar
    [l]\tLogin
    [q]\tSair

    => """

while True:
    opcao = input(menu)

    if opcao == "r":
        registrar_usuario()

    elif opcao == "l":
        nome = login()

        if nome:
            while True:
                menu_interno = """\n
                ================ MENU ================
                [d]\tDepositar
                [s]\tSacar
                [t]\tTransferir
                [e]\tExtrato
                [b]\tBloquear conta
                [q]\tSair

                => """

                opcao_interna = input(menu_interno)

                if opcao_interna == "d":
                    valor = float(input("Informe o valor do depósito: "))
                    depositar(nome, valor)

                elif opcao_interna == "s":
                    valor = float(input("Informe o valor do saque: "))
                    sacar(nome, valor)

                elif opcao_interna == "t":
                    valor = float(input("Informe o valor da transferência: "))
                    destino = input("Informe o nome do destinatário: ")
                    transferir(nome, valor, destino)

                elif opcao_interna == "e":
                    extrato(nome)

                elif opcao_interna == "b":
                    bloquear_conta(nome)
                    break

                elif opcao_interna == "q":
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")