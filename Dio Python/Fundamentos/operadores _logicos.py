print(True and True)
print(True and False)
print(True or False)
print(True or True)

saldo = 1000
saque = 500
limite = 400
cheque_especial = True

saque_permitido = saque <= saldo and saque <= limite
saque_nao_permitido = saque > saldo or saque > limite

if saque_permitido:
    print('Saque realizado com sucesso!')
if saque_nao_permitido:
    print('Saldo insuficiente ou limite excedido!')
if cheque_especial == True and saque_nao_permitido:
    print('Gostaria de usar o cheque especial?')        