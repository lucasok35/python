#Abrindo um dataset e muma única linha
s = open('arquivos/salarios.csv', 'r')

#Colocando o conteúdo do arquivo em outra variável
data = s.read()

#Fazendo split dos dados
rows = data.split('\n')

#Criando lista vazia
contagem_linhas = []
for row in rows:
    split_row = row.split(',')
    contagem_linhas.append(split_row)
    count = 0
    for row in rows:
        count += 1

#Imprimindo o resultado e contando o numero de linhas
print(rows)
print('Total de linhas processadas: ', count)

    
