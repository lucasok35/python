""" lista1 = ["laranja", "maca", "uva"]
print(lista1)

lista1 = []
print(lista1)

lista2 = list("python")
print(lista2)

numeros = list(range(10))
print(numeros)

carro = ["Civic", "LXR", 78000.000, 2016, 114000, "Boa Esperança do Sul", True]
print(carro)
#Acesso direto
print(carro[2])
print(carro[5])
#Indices negativos
print(carro[-1])
print(carro[-4]) """
#Como criar matrizes
""" matriz = [
["a", "b", "c"],
[1, 2, 3],
["d", 4, "4"]
]
#Imprimindo todos os elementos da matriz com o for
for linha in matriz:
    for elemento in linha:
        print(elemento) """

""" #Fatiamento
lista = list("python")
print(lista[2:])        
print(lista[:4])
print(lista[:]) """

#Iterando listas
""" carros = ["Civic", "New Civic", "Mustang"]

for carro in carros:
    print(carro)

#Imprimindo com indice
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

 """

#compreenssão de listas
""" numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
par = []

#Filtrar lista
for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
#Modificando valores
quadrado = [numero**2 for numero in numeros]
print(numeros)
print(par)
print(quadrado) """

#Append/clear
""" lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista)
lista.clear()

print(lista) """

#Copy/Id
""" lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista, lista2)  # [1, "Python", [40, 30, 20]]
print(id(lista), id(lista2)) """

#count/extended/index
""" games = ["Corrida", "Futebol", "RPG", "Luta", "Futebol"]

print(games.count("Fifa"))
print(games.count("Luta"))

games.extend(["Arcade", "Gore"])
print(games)

print(games.index("Futebol"))
 """

#Utilizando pop
""" linguagens = ["Python", "Progress", "SQL", "Java", "C#", "Javascript"]

print(linguagens.pop())
print(linguagens)
print(linguagens.pop(2))
print(linguagens) """

#Remove
""" linguagens = ["Python", "Progress", "SQL", "Java", "C#", "Javascript"]

linguagens.remove("Java")
print(linguagens) """

#Reverse
""" linguagens = ["Python", "Progress", "SQL", "Java", "C#", "Javascript"]
linguagens.reverse()
print(linguagens)
 """
#sort
""" linguagens = ["Python", "Progress", "SQL", "Java", "C#", "Javascript"]
linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens) """

#len
linguagens = ["Python", "Progress", "SQL", "Java", "C#", "Javascript"]
print(len(linguagens))

#sorted
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
print(sorted(linguagens))