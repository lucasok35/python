import csv

with open('arquivos/numeros.csv', 'w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira','segunda','terceira'))
    writer.writerow((955,125,375))
    writer.writerow((223,788,954))

    
#Realizando a leitura do csv
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
"""     for x in leitor:
        print('Numero de colunas: ', len(x))
        print(x) """

#Gerando lista com dados do arquivo csv
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)   

#print(dados)

for linha in dados[1:]:
    print(linha)