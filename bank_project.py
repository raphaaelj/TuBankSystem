"""
----Criar um sistema bancário---
Operação de depósito:
    Apenas depositar valores positivos

Operação de saque:
    apenas 3 saques diarios
    limite de 500,00 por saque
    informar caso não possua saldo
    armazenar saques em uma var e exibir no extrato

Operação de extrato:
    Listar todos os depósitos e saques realizados na conta
    No fim exibir o saldo atual da conta
    Formato 'R$xxx.xx'

"""
saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3



while True:
    menu = int(input(f"""
{10*'='} TuBank {10*'='}
1. Depositar
2. Sacar
3. Extrato
4. Sair

=> """))
    if menu == 1:
        valor_deposito = float(input('Quanto deseja depositar?\n=> '))
        if valor_deposito < 1:
            print('Você não pode depositar menos que R$1,00.\n')
        
        else:
            saldo += valor_deposito
            extrato += f'Deposito: R${valor_deposito:.2f}\n'
            print(f'Deposito de R${valor_deposito:.2f} realizado.\n')
    
    elif menu == 2:
        valor_saque = float(input('Quanto deseja sacar?\n=> '))
        excedeu_limite = numero_saques >= LIMITE_SAQUE
        excedeu_saque = valor_saque > limite_diario
        execeu_saldo = valor_saque > saldo
        
        if excedeu_limite:
            print('Você realizou o máximo de operações possíveis hoje.\n')
            
        elif excedeu_saque:
            print(f'Você não pode sacar mais que R${limite_diario:.2f}\n')
            
        elif execeu_saldo:
            print('Valor em saldo insuficiente.\n')
            
        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R${valor_saque:.2f}\n"
            print(f'Saque de R${valor_saque:.2f} realizado.')
            print(f'Seu saldo atual é de R${saldo:.2f}\n')
            
        else:
            print('Valor inválido.\n')
        
    elif menu == 3:
        print(20*'='+" EXTRATO "+'='*20)
        if not extrato:
            print('Não foi realizado nenhum tipo de movimento nesta conta.')
        else:
            print(extrato, sep='\n')
            print(f'\nSaldo em conta: R${saldo:.2f}')
        print(50*'=')
    
    elif menu == 4:
        break
    
    else:
        print('Opção inválida.\n')