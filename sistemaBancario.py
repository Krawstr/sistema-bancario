from datetime import datetime

saldo = 0
valores_transacoes = list()
transacoes_diarias = 0
LIMITE_TRANSACOES_DIARIAS = 10

def saque(valor_saque):
    global valores_transacoes, LIMITE_TRANSACOES_DIARIAS, transacoes_diarias
   
    if transacoes_diarias == LIMITE_TRANSACOES_DIARIAS:
        return "Limite diario de transaçoes atingido."
    
    if saldo >= valor_saque and valor_saque <= 500:
        saldo -= valor_saque
        transacoes_diarias += 1
        valores_transacoes.append(("saque", valor_saque, datetime.now()))
        return f"Você sacou R${valor_saque}."
    
    return f"Você não tem saldo suficiente para realizar o saque ou valor é maior que R$500. Seu saldo atual: R${saldo:.2f}"

def deposito(valor_deposito):
    global valores_transacoes, transacoes_diarias, LIMITE_TRANSACOES_DIARIAS

    if transacoes_diarias == LIMITE_TRANSACOES_DIARIAS:
        return "Limite diario de transaçoes atingido."

    if valor_deposito <= 0:
        return f"O valor depositado deve ser maior que zero. Seu saldo atual: R${saldo:.2f}"
    saldo += valor_deposito
    valores_transacoes.append(("deposito", valor_deposito, datetime.now()))

def extrato():
    global valores_depositos, valores_saques, saldo

    for tipo, valor, data_hora in valores_saques:
        print(f"{tipo.capitalize()}: R${valor:.2f} em {data_hora.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Seu saldo atual: R${saldo:.2f}")

while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 1:
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            armazenar_deposito = deposito(valor_deposito)
            print(armazenar_deposito)
            print("_____________________________")
        case 2:
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            armazenar_saque = saque(valor_saque)
            print(armazenar_saque)
            print("_____________________________")
        
        case 3:
            extrato()
            print("_____________________________")

        case 4:
            break

        case _:
            print("Opção inválida.")
