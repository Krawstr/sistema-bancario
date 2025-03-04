saldo = 0
valores_depositos = list()
valores_saques = list()
saques_diario = 0

def saque(valor_saque):
    global saldo, valores_saques, saques_diario
   
    if saques_diario == 3:
        return "Limite diario de saques atingido."
    
    if saldo >= valor_saque and valor_saque <= 500:
        saldo -= valor_saque
        saques_diario += 1
        valores_saques.append(valor_saque)
        return f"Você sacou R${valor_saque}. Seu saldo atual: R${saldo:.2f}"
    
    return f"Você não tem saldo suficiente para realizar o saque ou está tentando sacar mais de R$500. Seu saldo atual: R${saldo:.2f}"

def deposito(valor_deposito):
    global valores_depositos, saldo

    if valor_deposito <= 0:
        return f"O valor depositado deve ser maior que zero. Seu saldo atual: R${saldo:.2f}"
    saldo += valor_deposito
    valores_depositos.append(valor_deposito)
    return f"Seu saldo atual: R${saldo:.2f}"

def extrato():
    global valores_depositos, valores_saques, saldo

    print(f"Depositos: {valores_depositos}")
    print(f"Saques: {valores_saques}")
    print(f"Seu saldo atual: R${saldo:.2f}")

while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    
try:
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
            
except ValueError:
    print("❌ Entrada inválida! Digite um número válido.")
