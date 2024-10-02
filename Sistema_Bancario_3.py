from abc import ABC, abstractmethod
from datetime import datetime

# Interface Transacao
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Deposito implementando Transacao
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(f"Depósito: R$ {self.valor:.2f}")
        print(f"Depósito de R$ {self.valor:.2f} realizado com sucesso!")

# Classe Saque implementando Transacao
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque: R$ {self.valor:.2f}")
            print(f"Saque de R$ {self.valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

# Classe Historico para manter registro de transações
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, descricao):
        data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.transacoes.append(f"{data_hora_atual} - {descricao}")

    def exibir_transacoes(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
        else:
            print("Histórico de Transações:")
            for transacao in self.transacoes:
                print(transacao)

# Classe Cliente (superclasse)
class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica, subclasse de Cliente
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# Classe Conta (superclasse)
class Conta:
    def __init__(self, cliente, numero_conta, agencia="0001"):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = 0
        self.historico = Historico()
        cliente.adicionar_conta(self)

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Classe ContaCorrente, herda de Conta
class ContaCorrente(Conta):
    def __init__(self, cliente, numero_conta, limite=500, limite_saques_diarios=3):
        super().__init__(cliente, numero_conta)
        self.limite = limite
        self.limite_saques_diarios = limite_saques_diarios
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques_diarios:
            print("Limite de saques diários atingido.")
        elif valor > self.limite:
            print(f"Não é possível sacar valores acima de R$ {self.limite:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            saque = Saque(valor)
            saque.registrar(self)
            self.numero_saques += 1

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

# Banco de Dados Simulado
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.numero_conta = 1

    def criar_cliente(self, nome, cpf, data_nascimento, endereco):
        cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
        self.clientes.append(cliente)
        print(f"Cliente {nome} criado com sucesso!")
        return cliente

    def criar_conta_corrente(self, cliente):
        conta_corrente = ContaCorrente(cliente, self.numero_conta)
        self.contas.append(conta_corrente)
        self.numero_conta += 1
        print(f"Conta corrente criada com sucesso para {cliente.nome}!")

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
        else:
            print("Contas cadastradas:")
            for conta in self.contas:
                print(f"Agência: {conta.agencia}, Conta: {conta.numero_conta}, Cliente: {conta.cliente.nome}")

# Função principal com menu
def main():
    banco = Banco()

    while True:
        print("\nBem-vindo ao Banco!")
        print("[1] Criar Cliente")
        print("[2] Criar Conta Corrente")
        print("[3] Depositar")
        print("[4] Sacar")
        print("[5] Exibir Saldo")
        print("[6] Exibir Histórico de Transações")
        print("[7] Listar Contas")
        print("[8] Sair")
        opcao = input("Escolha uma operação: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
            endereco = {
                'logradouro': input("Digite o logradouro: "),
                'numero': input("Digite o número: "),
                'bairro': input("Digite o bairro: "),
                'cidade': input("Digite a cidade: "),
                'estado': input("Digite o estado (sigla): ")
            }
            banco.criar_cliente(nome, cpf, data_nascimento, endereco)

        elif opcao == "2":
            cpf = input("Digite o CPF do cliente: ")
            cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
            if cliente:
                banco.criar_conta_corrente(cliente)
            else:
                print("Cliente não encontrado.")

        elif opcao == "3":
            cpf = input("Digite o CPF do cliente para depósito: ")
            conta = next((c for c in banco.contas if c.cliente.cpf == cpf), None)
            if conta:
                valor = float(input("Valor do depósito: R$ "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            cpf = input("Digite o CPF do cliente para saque: ")
            conta = next((c for c in banco.contas if c.cliente.cpf == cpf), None)
            if conta:
                valor = float(input("Valor do saque: R$ "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            cpf = input("Digite o CPF do cliente para exibir saldo: ")
            conta = next((c for c in banco.contas if c.cliente.cpf == cpf), None)
            if conta:
                conta.exibir_saldo()
            else:
                print("Conta não encontrada.")

        elif opcao == "6":
            cpf = input("Digite o CPF do cliente para exibir o histórico: ")
            conta = next((c for c in banco.contas if c.cliente.cpf == cpf), None)
            if conta:
                conta.historico.exibir_transacoes()
            else:
                print("Conta não encontrada.")

        elif opcao == "7":
            banco.listar_contas()

        elif opcao == "8":
            print("Obrigado por utilizar o banco. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
