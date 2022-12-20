#Dividindo e contando numero de colunas
arquivo = open('arquivos/salarios.csv', 'r')

dados = arquivo.read()

rows = dados.split('\n')

dados_colunas = []

for row in rows:
    split_row = row.split(',')
    dados_colunas.append(split_row)
    first_row = dados_colunas[0]
count = 0
for dado in first_row:
    count += 1

print(count)