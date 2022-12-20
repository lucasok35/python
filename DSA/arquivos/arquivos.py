encoding='utf8'
#Abrindo o arquivo para leitura
arq1 = open('arquivos/arquivo1.txt', 'r')

#Lendo o arquivo
print(arq1.read())
print(arq1.tell())
print(arq1.seek(1,0))
print(arq1.read(10))

arq1.close()

#Abrindo o arquivo para gravação
arq2 = open('arquivos/arquivo1.txt', 'w')

#print(arq2.write('Isso sobrescreve o texto!!!'))
arq2.close()

#Abrindo arquivo para apend
arq2 = open('arquivos/arquivo1.txt', 'a')

print(arq2.write('Acrescentando conteúdo no arquivo'))
arq2.close()

#Abrindo novamente para leitura
arq1 = open('arquivos/arquivo1.txt', 'r')
arq1.seek(0,0)

print(arq1.read())


