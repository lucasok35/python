saldo = 0
limite_saques = 3
confere_limite = 0
extrato = []

def get_menu_option():
    menu = ['d', 's', 'e', 'x']
    while True:
        print('-----Menu-----\n'
        'D - Para depósito\n'
        'S - Para saque\n'
        'E - Para extrato\n'
        'X - Para sair\n')
        print('Saldo: ', saldo)

        user_input = input('Escolha uma das opções:\n')

        if user_input in menu:
            return user_input
        else:
            print('OPÇÃO INVÁLIDA!')

while True:

    user_input = get_menu_option()

    if user_input == 'd':
        deposito = float(input('Digite o valor que deseja depositar:'))
        if deposito >= 0:
            saldo = saldo + deposito
            extrato.append(f'Depósito de R$: {deposito}')
        else:
            print('Valor inválido!')    
    elif user_input == 's':
        saque = float(input('Digite o valor que deseja sacar:'))
        if saque <= 0:
            print('Valor inválido!')
        else:
            if confere_limite > limite_saques or saque > saldo:
                print('Não foi possível concluir o saque, verifique o saldo atual ou seu limite de saques!!!')
            else:
                print('Saque concluído com sucesso!')
                confere_limite += 1
                saldo = saldo - saque
                extrato.append(f'Saque de R$: -{saque}')
    elif user_input == 'e':
        print('-------------------extrato da movimentação da conta!---------------------')
        print(*extrato, sep='\n')
        print('-------------------------------------------------------------------------')          
        print(f'Saldo atual: {saldo}')
    elif user_input == 'x':
        print('Obrigado pela preferência!')
        exit()
