dic_games = {'Batman':2011, 'GTA V':2013, 'GOW':2010, 'Spiderman':2015}
dic_games2 = {'Watch Dogs':2014, 'KOF 2002':2022}
print('*************************')
print(dic_games)
print(dic_games['Batman'])

#Adicionando chave e valor ao dicionario
dic_games['PES 2022'] = 2022
print('*************************')
print(dic_games['PES 2022'])
print(dic_games)

#Deletando dicionario
#del dic_games
print('*************************')
print(dic_games)
#tamanho do dicionario
print(len(dic_games))

#Imprimindo apenas as chaves
print(dic_games.keys())

#Imprimindo valores
print(dic_games.values())

#Imprimindo todos os itens
print(dic_games.items())

#Adicionando um dicionario a outro
dic_games.update(dic_games2)
print(dic_games)

#Criando um dicionario aninhado
dic_aninhado = {'Key1':{'Key2':{'Key3': 'dic aninhado em Python'}}}
#Imprimindo só o valor da primeira chave
print(dic_aninhado['Key1'])

#Tuplas são imutaveis, segue exemplo
tup1 = ('Lucas', 'Henrique', 'Teixeira', 'da', 'Silva')
print(tup1)

#Para converter uma tupla em lista usamos List()
#E tuple() para converter uma lista em tupla

