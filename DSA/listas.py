lista1 = ["abacate", "limão", "pera", "laranja"]
lista2 = [["bitcoin", "ethereum", "bnb"], ["matic", "link", "aave"], ["gala", "usdt", "looksrare"]]



top6 = lista2[0][1]

lista1[0] = "banana"
fruta1 = lista1[0]

del lista1[1]

todas_listas = lista1 + lista2

#print(lista1)
#print(lista2)
#print(todas_listas)

#print("banana" in lista1)

# Função len() retorna o comprimento da lista
lista2.append(["sand"])
print(lista2)
print(len(lista2))
print(max(lista2))
print(min(lista2))
print(lista1.count("abacate"))