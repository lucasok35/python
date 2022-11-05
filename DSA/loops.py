#trabalhando com loop (laços)

""" tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
liga = ['Batman', 'Ironman', 'Spiderman', 'Ichigo', 'Luffy', 'Natsu'] """

""" for i in tupla:
    print(i)
 """

""" for i in tupla:
    if i % 2 == 0:
        print(i) """

""" for heroi in liga:
    print(heroi)  """       

""" for contador in range(1,5): #(exclusive)
    print(contador)     """

""" for contador in range(0, 100, 5): #Incremento de 5
    print(contador) """

#Loop aninhado
""" for i in range(1, 10):
    for i in range(1, 10):
        if i % 2 == 0:
            print(i) """    

""" lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]            
soma = 0
for item in lista:
    soma += item
print(soma)     """

listas = [['catwomen', 'hawkwomen'], ['sheva', 'talia'], ['era', 'marvelwomen'], ['wonderwomen', 'arlequina']]
colunas = 0
linhas = 0
for item in listas:
    colunas += 1
    for item in listas[0]:
        linhas += 1
print(colunas, linhas)