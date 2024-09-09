"""
Fomos contratados por um banco para desenvolver um sistema com 3 operações: depósito, saque e extrato.

Deposito - Deve ser possivel depositar valores positivos para a minha conta bancaria, temos somente 1 usuario,
todos os depositos devem ser guardados em uma variavel e exibidos na operacao de extrato

Saques - O sistema deve permitir fazer 3 saques diários com limite de 500 reais por saque. Caso o usuário não tenhna
saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacaro dinheiro por falta de saldo.
Todos os saques devem ser guardados em uma variável e exibidos na operação de extrato

Extrato - Essa operação tem que listar todos os depósitos e saques feitos na conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores tem que ser exibidos usando o formato R$ xxx.xx, ex: 1500.45 -> R$ 1500.45

"""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d" or opcao == "D":
        valor_deposito = int(input("Informe a quantidade que deseja depositar: \n"))
        if valor_deposito < 0:
            print("Valor inválido! Repita a operação")
        saldo += valor_deposito
        extrato += f"Deposito: R$ {saldo:.2f}\n"
        
        
    elif opcao == "s" or opcao == "S":
        valor_saque = int(input("Entre com o valor para sacar: \n"))
        
        if valor_saque < 0:
            print("\nValor inválido!")
        
        elif valor_saque > saldo:
            print("\nNão há saldo disponível para fazer a operação")      
        
        elif numero_saques >= 3:
            print("\nNúmero máximo de saques atingido!")
            
        elif valor_saque < 500:
            numero_saques += 1
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            
        elif valor_saque > 500:
            print("O limite de valor do saque é de 500 R$")
                
    elif opcao == "e" or opcao == "E":
        if saldo == 0 and numero_saques == 0:
            print("\nNão foram feitas movimentações na conta.")
            
        else:
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
        
    elif opcao == "q" or opcao == "Q":
        break
    
    else:
        print("\nOperação inválida! Tente novamente outra operação!")
    
