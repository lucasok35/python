encoding = 'utf8'

#Abrindo arquivo para leitura e escrita
arq1 = open('arquivos/arquivo1.txt', 'w')

#Realizando manipulações no arquivo com métodos
print(arq1.write('Python é uma linguagem poderosa'))
arq1.close()

arq1 = open('arquivos/arquivo1.txt', 'r')
print(arq1.read())
arq1.close()

arq1 = open('arquivos/arquivo1.txt', 'a')
print(arq1.write(' e eu irei dominá-la'))
arq1.close()

arq1 = open('arquivos/arquivo1.txt', 'r')
print(arq1.read())