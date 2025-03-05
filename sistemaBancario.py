import textwrap
from datetime import datetime

class ContaBancaria:
    def __init__(self, titular, limite=500, limite_saques=3):
        self.titular = titular
        self.saldo = 0
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.extrato = ""

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif self.numero_saques >= self.limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.numero_saques += 1
            self.extrato += f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:		R$ {self.saldo:.2f}")
        print("==========================================")


def menu():
    menu = """
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Sair
    => """
    return input(textwrap.dedent(menu))

def main():
    contas = []
    while True:
        opcao = menu()
        
        match opcao:
            case "1":
                nome = input("Digite o nome do titular: ")
                conta = next((c for c in contas if c.titular == nome), None)
                if conta:
                    valor = float(input("Informe o valor do depósito: "))
                    conta.depositar(valor)
                else:
                    print("Conta não encontrada!")
            
            case "2":
                nome = input("Digite o nome do titular: ")
                conta = next((c for c in contas if c.titular == nome), None)
                if conta:
                    valor = float(input("Informe o valor do saque: "))
                    conta.sacar(valor)
                else:
                    print("Conta não encontrada!")
            
            case "3":
                nome = input("Digite o nome do titular: ")
                conta = next((c for c in contas if c.titular == nome), None)
                if conta:
                    conta.exibir_extrato()
                else:
                    print("Conta não encontrada!")
            
            case "4":
                nome = input("Digite o nome do titular para a nova conta: ")
                contas.append(ContaBancaria(nome))
                print("Conta criada com sucesso!")
            
            case "5":
                print("\n===== Lista de Contas =====")
                for conta in contas:
                    print(f"Titular: {conta.titular}, Saldo: R$ {conta.saldo:.2f}")
                print("============================")
            
            case "6":
                print("Saindo...")
                break
            
            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
