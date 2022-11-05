#Exercicio 1
""" dia_da_semana = input('Qual o dia da semana?')

if dia_da_semana == 'domingo' or dia_da_semana == 'sabado':
    print('Hoje é dia de descanso!')
else:
    print('Hoje é dia de trabalhar!')    """

#Exercicio 2
""" lista = ['morango', 'melão', 'goiaba', 'manga', 'laranja']

print('morango' in lista) """

#Exercicio 3
""" tp = (1, 2, 3, 4)
lista = []
i = 0
while i < len(tp):
    lista.append(tp[i]*2)
    i += 1

print(lista) """

#Exercicio 4
""" for i in range(102, 150, 2):   
    print(i)

 """

 #Exercicio 5
""" temperatura = 40

while temperatura > 35:
    print(temperatura)
    temperatura -= 1 """

#Exercicio 6

""" contador = 0

while contador < 100:
    print(contador)
    contador += 1

    if contador == 23:
        break """

#Exercicio 7
""" lista = []
varia = 4

while varia <= 20:
    if varia % 2 == 0:
        lista.append(varia)
        varia += 1
    else:
        varia += 1

print(lista) """

#Exercicio 8
""" nums = range(5, 45, 2)
lista = []

for i in nums:
    lista.append(i)

print(lista) """

#Exercicio 9 - corrigir erros
""" temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.') """

#Exercicio 10
""" frase = "É melhor, muito melhor, contentar-se com a realidade se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
j = 0

for i in frase:
    if i == "r":
        j += 1
print('A letra "r" aparece %s vezes na frase!' %(j)) """
