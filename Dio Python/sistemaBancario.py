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
        deposito = int(input('Digite o valor que deseja depositar:'))
        saldo = saldo + deposito
        extrato.append(deposito)
    elif user_input == 's':
        saque = int(input('Digite o valor que deseja sacar:'))
        if confere_limite > limite_saques or saque > saldo:
            print('Não foi possível concluir o saque, verifique o saldo atual ou seu limite!!!')
        else:
            print('Saque concluído com sucesso!')
            confere_limite += 1
            saldo = saldo - saque
            saque = saque * (-1)
            str(saque)
            extrato.append(saque)
    elif user_input == 'e':
        print('Segue extrato da movimentação da conta!')
        print(extrato)          
        print(saldo)
    elif user_input == 'x':
        print('Obrigado pela preferência!')
        exit()
