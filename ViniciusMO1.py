#Projeto Sistema Bancario

menu = '''

[1] = deposito
[2] = saque
[3] = extrato
[0] = sair

=> '''
saldo = 0
saque = 500
extrato = []
saque_total = 3
numero_saques = sum_saque = 0
saldo_final = 0
numero_depositos = 0

while True:

    opcao = input(menu)
#deposito    
    if opcao == "1":
        deposito = float(input('Quanto voce deseja depositar?'))
        numero_depositos += 1
        saldo_final+=deposito
        if deposito <= 0:
            print('Não é possível realizar um depósito com valor negativo')
            break

        print(f'Valor {deposito:.2f} R$, depositado com sucesso, algo mais? ')
#saque
    elif opcao == "2":
        saque = float(input('Quanto voce deseja sacar? Lembrando que o maximo de saque é de 500 R$'))
        sum_saque+=saque
        if saque > 500:
            print('Valor acima do limite, tente um valor menor que 500')
        else:
            if saque > deposito:
                print('Sem saldo suficiente para saque, tente novamente')
                break
            else:
                if numero_saques > saque_total:
                    print('O sistema não permite mais saques, comece novamente')            
                    break
        print(f'Saque de {saque} R$ realizado com sucesso')
        numero_saques += 1
    
#extrato        
    elif opcao == "3":
        tot= (saldo_final - sum_saque)
        if True:
            print('\n ==========EXTRATO=============')
            print(f'Voce depositou: R$ {saldo_final} e sacou: R${sum_saque}')
            print(f'Voce fez {numero_saques} saques e {numero_depositos} depósitos')
            print(f'Saldo final: R$ {tot}') 
            print('===============================')
        else:
            print("Não foram realizadas movimentações")
#fim              
    elif opcao == "0":
        if True:
            print(f'Voce está saindo do sistema, até logo.')
            break
        
        else:
            print('Opcao invalida, digite um valor valido')
