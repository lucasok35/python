import random

#Jokenpô


print('Pedra, papel ou tesoura?: pedra (1), papel(2), tesoura(3)')
escolha = int(input())
computador = random.randrange(1,4)
print(escolha)
print(computador)

if (escolha == 1) and (computador == 1):
    print('empatou :/')
elif (escolha == 2) and (computador == 2):
    print('empatou :/')
elif (escolha == 3) and (computador == 3):
    print('empatou :/')
elif (escolha == 1) and (computador == 2):
    print('Você perdeu :(')
elif (escolha == 2) and (computador == 3):
    print('Você perdeu :)')
else:
    print('Você ganhou :)')               



