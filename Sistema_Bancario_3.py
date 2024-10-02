# Classe para representar um Usuário
class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"


# Classe para representar uma Conta Corrente
class ContaCorrente:
    agencia = "0001"  # Valor fixo para a agência

    def __init__(self, usuario, numero_conta):
        self.usuario = usuario
        self.numero_conta = numero_conta
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES_DIARIOS = 3
        self.limite_saque = 500

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if self.numero_saques >= self.LIMITE_SAQUES_DIARIOS:
            print("Limite de saques diários atingido.")
        elif valor > self.limite_saque:
            print(f"Não é possível sacar valores acima de R$ {self.limite_saque:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido.")

    def exibir_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("\nExtrato Bancário:")
            for movimento in self.extrato:
                print(movimento)
            print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")


# Banco de Dados Simulado
class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.numero_conta = 1

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print("CPF já cadastrado para outro usuário.")
                return
        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")

    def criar_conta(self, cpf_usuario):
        usuario = next((u for u in self.usuarios if u.cpf == cpf_usuario), None)
        if usuario:
            conta = ContaCorrente(usuario, self.numero_conta)
            self.contas.append(conta)
            self.numero_conta += 1
            print(f"Conta criada com sucesso para {usuario.nome}!")
        else:
            print("Usuário não encontrado.")

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
        else:
            print("\nListagem de Contas:")
            for conta in self.contas:
                print(f"Agência: {ContaCorrente.agencia}, Conta: {conta.numero_conta}, Usuário: {conta.usuario}")
            print("\n")


# Função principal com menu
def main():
    banco = Banco()

    while True:
        print("Bem-vindo ao Banco!")
        print("[1] Criar Usuário")
        print("[2] Criar Conta Corrente")
        print("[3] Depositar")
        print("[4] Sacar")
        print("[5] Extrato")
        print("[6] Listar Contas")
        print("[7] Sair")
        opcao = input("Escolha uma operação: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
            cpf = input("Digite o CPF do usuário: ")
            endereco = {
                'logradouro': input("Digite o logradouro: "),
                'numero': input("Digite o número: "),
                'bairro': input("Digite o bairro: "),
                'cidade': input("Digite a cidade: "),
                'estado': input("Digite o estado (sigla): ")
            }
            banco.criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "2":
            cpf_usuario = input("Digite o CPF do usuário para criar a conta: ")
            banco.criar_conta(cpf_usuario)

        elif opcao == "3":
            cpf_usuario = input("Digite o CPF do usuário para depósito: ")
            conta = next((c for c in banco.contas if c.usuario.cpf == cpf_usuario), None)
            if conta:
                valor = float(input("Digite o valor do depósito: R$ "))
                conta.deposito(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            cpf_usuario = input("Digite o CPF do usuário para saque: ")
            conta = next((c for c in banco.contas if c.usuario.cpf == cpf_usuario), None)
            if conta:
                valor = float(input("Digite o valor do saque: R$ "))
                conta.saque(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            cpf_usuario = input("Digite o CPF do usuário para extrato: ")
            conta = next((c for c in banco.contas if c.usuario.cpf == cpf_usuario), None)
            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "6":
            banco.listar_contas()

        elif opcao == "7":
            print("Obrigado por utilizar o banco. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
