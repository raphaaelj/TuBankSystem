"""1
----Criar um sistema bancário---
Operação de depósito: OK
    Apenas depositar valores positivos

Operação de saque: OK
    apenas 3 saques diarios
    limite de 500,00 por saque
    informar caso não possua saldo
    armazenar saques em uma var e exibir no extrato

Operação de extrato: OK
    Listar todos os depósitos e saques realizados na conta
    No fim exibir o saldo atual da conta
    Formato 'R$xxx.xx'

"""

"""2
Objetivo Geral Otimizando o Sistema Bancário

1 - Separar as funções existentes de saque, depósito e extrato em funções - OK
2 - Criar duas novas funções: OK
    . cadastrar usuário;
    . cadastrar conta bancária


Saque:
    argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
    retorno: saldo, extrato

Criar Usuario:
    armazenar os usuarios em lista
    Usuário - é composto po nome, data de nascimento, cpf e endereço
    Endereço - é composto por logradouro, nº - bairro - cidade/sigla estado
    Somente números no CPF
    Não podemos repetir CPF

Criar Conta:
    armazenar em uma lista
    Conta: composta por agência, número da conta e usuário
    Número da conta é sequencial, iniciando em 1
    O número da agência é fico: "0001"
    O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário


DICA: Para vincular uma conta a um usuário, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista
"""


login = 1  # IMPORTANTE: 1 - Programa ativo, 0 - Finaliza o programa

usuarios = {18851783799: {'Nome': 'Raphael José Silva de Oliveira', 'Data de Nascimento': '08-10-2000', 'endereco': {'logradouro': 'Rua Aracoia', 'Número': 489, 'Bairro': 'Bras de Pina', 'Cidade': 'Rio de Janeiro', 'Estado': 'RJ'}, 'Senha': '@Raphael08', 'isAdmin': True},
            18683026740: {'Nome': 'Raneli Rufino de Pontes', 'Data de Nascimento': '12-01-2001', 'endereco': {'logradouro': 'Rua Aracoia', 'Número': 489, 'Bairro': 'Bras de Pina', 'Cidade': 'Rio de Janeiro', 'Estado': 'RJ'}, 'Senha': '123456', 'isAdmin': False},
            }

contas = {}


def depositar(userCPF):  # func: Depositar dinheiro
    for conta in contas:
        if contas[conta]['Usuário'] == userCPF:
            contas_usuario = {}
            contas_usuario[conta] = conta
            print(f'Número de conta: {conta}')

    conta_a_depositar = int(input('\nEm qual conta deseja depositar?\n=> '))
    if not conta_a_depositar in contas_usuario:  # error: se conta não estiver na lista de contas do usuário
        print(f'\nValor de conta incorreto.\n')
        main(userCPF)
    else:
        valor_deposito = input('\nQuanto deseja depositar?\n=> ')
        if valor_deposito.isalpha():  # error: se o valor de entrada não for um número
            print('\nApenas números são permitidos.\n')
            main(userCPF)
        # info: transforma o valor de str para float
        valor_deposito = float(valor_deposito)

    if valor_deposito < 1:  # error: se tentar depositar menos que 1,00
        print('\nVocê não pode depositar menos que R$1,00.\n')
        depositar(userCPF)
    else:
        contas[conta_a_depositar]['Saldo'] += valor_deposito
        contas[conta_a_depositar]['Extrato'] += f'Deposito: R${valor_deposito:.2f}\n'
        print(f'\nDeposito de R${valor_deposito:.2f} realizado.\n')


def sacar(userCPF):  # func: Sacar dinheiro
    for conta in contas:
        if contas[conta]['Usuário'] == userCPF:
            contas_usuario = {}
            contas_usuario[conta] = conta
            print(f'Número de conta: {conta}')
    conta_a_sacar = int(input('\nDe qual conta gostaria de sacar?\n=> '))
    if not conta_a_sacar in contas_usuario:
        print(f'\nValor de conta incorreto.\n')
        main(userCPF)
    else:
        valor_saque = input('\nQuanto deseja sacar?\n=> ')
        if valor_saque.isalpha():
            print('\nApenas números são permitidos.\n')
            main(userCPF)
        valor_saque = float(valor_saque)

    LIMITE_SAQUE = 500

    excedeu_limite = contas[conta_a_sacar]['Limite diário'] == 0
    excedeu_saque = valor_saque > LIMITE_SAQUE
    execeu_saldo = valor_saque > contas[conta_a_sacar]['Saldo']

    if excedeu_limite:  # error: Já operou saque 3x no dia
        print('\nVocê realizou o máximo de operações possíveis hoje.\n')
        main(userCPF)

    elif excedeu_saque:  # error: Tentou sacar mais que R$500
        print(f'\nVocê não pode sacar mais que R${LIMITE_SAQUE:.2f}\n')
        main(userCPF)

    elif execeu_saldo:  # error: Não possui saldo
        print('\nValor em saldo insuficiente.\n')
        print(f'Seu saldo é de R${contas[conta_a_sacar]['Saldo']:.2f}\n')
        sacar(userCPF)

    elif valor_saque > 0:
        contas[conta_a_sacar]['Saldo'] -= valor_saque
        contas[conta_a_sacar]['Limite diário'] -= 1
        contas[conta_a_sacar]['Extrato'] += f"Saque: R${valor_saque:.2f}\n"
        print(f'{20*'='} TuBank {20*'='}')
        print(f'\nSaque de R${valor_saque:.2f} realizado.\n')
        print(f'\nSeu saldo atual é de R${contas[conta_a_sacar]['Saldo']:.2f}\n')
        print(f'{60*'='}')

    else:
        print('\nValor inválido.\n')


def exibir_extrato(userCPF):  # func: Exibir extrato
    for conta in contas:
        if contas[conta]['Usuário'] == userCPF:
            contas_usuario = {}
            contas_usuario[conta] = conta
            print(f'Número de conta: {conta}')
    conta_a_exibir = int(input('\nDe qual conta quer ver o extrato?\n=> '))
    if conta_a_exibir not in contas_usuario:
        print(f'\nValor de conta incorreto.\n')
        main(userCPF)
    else:
        print('\n'+20*'='+" EXTRATO "+'='*20)
        if not contas[conta_a_exibir]['Extrato']:
            print('\nNão foi realizado nenhum tipo de movimento nesta conta.\n')
        else:
            print(contas[conta_a_exibir]['Extrato'], sep='\n')
            print(f'\nSaldo em conta: R${contas[conta_a_exibir]['Saldo']:.2f}\n')
        print(50*'='+'\n')


def criar_usuario():  # func: Cadastrar usuário
    cpf = input('\nCPF (apenas números): ')
    if usuarios.get(cpf):
        print('\nEste usuário já existe.\n')
        menu()
    elif cpf.isalpha():
        print('Insira apenas números!')
        menu()
    cpf = int(cpf)
    usuarios[cpf] = {'Nome':input('Nome completo: '),
                         'Data de Nascimento':input('Data de Nascimento (dd-mm-aa): '),
                         'endereco': {'logradouro':input('Nome da rua: '),
                                      'Número':input('Nº: '),
                                      'Bairro':input('Bairro: '),
                                      'Cidade':input('Cidade: '),
                                      'Estado':input('Sigla do Estado: ')},
                         'Senha':input('Digite uma senha: '),
                         'isAdmin':False}
    print(f'\nUsuário Criado!\n')
    menu()


def criar_conta(userCPF):  # func: Abrir conta
    agencia = '0001'
    quantidade_contas = len(contas)
    numero_conta = quantidade_contas + 1
    contas[numero_conta] = {'Agência': agencia, 'Usuário': userCPF,
                            'Saldo': 0, 'Extrato': "", 'Limite diário': 3}
    print(f'''\n{30*'='}
++ Sua conta foi criada com sucesso! ++

O TuBank agradece a preferência.
{30*'='}\n
''')


def listar_contas(userCPF):  # func: Mostra as contas, seus donos e saldos
    global quantidade_contas
    quantidade_contas = len(contas)
    if usuarios[userCPF]['isAdmin'] == True:
        for conta in contas:
            print(f'''{40*"="}
    C/C {conta} AG: {contas[conta]["Agência"]}:
        .Usuário: {contas[conta]["Usuário"]}
        .Saldo: {contas[conta]["Saldo"]}\n{40*"="}\n''')
        print('Quantidade de contas abertas: ', quantidade_contas)
    else:
        print('\nVocê não possui permissão.\n')


def menu():  # func: Fazer login ou Cadastrar usuário
    global login
    option = int(input(f'''{20*'='} TuBank {20*'='}

1. Sou correntista
2. Criar um usuário
3. Sair
=> '''))

    if option == 1:  # login: Sou correntista
        user = int(input('Digite seu cpf: '))
        pswd = input('Digite sua senha: ')
        # login: Usuário e Senha certos
        if user in usuarios and pswd == usuarios[user]['Senha']:
            while login:
                main(user)
        # erro: Senha incorreta
        elif user in usuarios and pswd != usuarios[user]['Senha']:
            print('\nSenha Incorreta!\n')
            menu()
        elif not user in usuarios:  # erro: Usuário não existe
            print('\nEste usuário não existe.\n')
            menu()
    elif option == 2:  # login: Cadastrar usuário
        criar_usuario()


def main(cpf):  # func: Main program
    global login

    if login:  # IF Login = True, abre as opções
        option = int(input(f"""\n{10*'='} TuBank {10*'='}
Olá {usuarios[cpf]["Nome"]}, qual operação deseja realizar hoje?

1. Criar Conta
2. Listar Contas
3. Depositar
4. Sacar
5. Extrato
6. Logout
7. Sair

=> """))

        if option == 1:  # func: Criar Conta
            criar_conta(cpf)

        elif option == 2:  # func: Listar Contas
            listar_contas(cpf)

        elif option == 3:  # func: Depositar
            depositar(cpf)

        elif option == 4:  # func: Sacar
            sacar(cpf)

        elif option == 5:  # func: Exibir extrato
            exibir_extrato(cpf)

        elif option == 6:  # func: Sair da conta
            menu()
        elif option == 7:  # func: Fechar programa
            login = 0

        else:  # error: Opção inválida
            print('\nOpção inválida.\n')
    else:  # Fechar
        login = 0


menu()