from random import randint
from time import sleep
lista = list()
jogos = list()
print('_' * 30)
print('MEGA DA VIRADA')
print('_' * 30)
quant = int(input ('escolha o numero de jogos que voce quer fazer:'))
tot = 1
while tot <= quant:    
    cont = 0
    while True:
        for i in range(50063860):
            num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
if quant == 1:
    print('$' * 3, f'Sorteando {quant} jogo:', '$' * 3)
else:
    print('$' * 3, f'Sorteando {quant} jogos:', '$' * 3)    
for i, l in enumerate(jogos):
    print(f'Jogo:{i+1}: {l}')
    sleep(1)