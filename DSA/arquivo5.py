text = 'Esse é meu texto\n'
text += 'E aqui eu estou adicionando conteúdo a ele\n'
text += 'Novamente mais conteúdo'

#print(text)

import os

""" #Outra forma de criar uma arquivo
arquivo = open(os.path.join('arquivos/arquivo_os.txt'), 'w')

#Gravando dados no arquivo
for palavra in text.split():
    arquivo.write(palavra+' ')

arquivo.close()

#lendo o arquivo após gravar o texto da variável text nele
arquivo = open('arquivos/arquivo_os.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo) """


#Com a expressão with o comando close é executado automaticamente
with open('arquivos/arquivo_os.txt', 'r') as arquivo:
    conteudo = arquivo.read()

#print(conteudo)

with open('arquivos/arquivo_os2', 'w') as arquivo2:
    arquivo2.write(conteudo)
    arquivo2.write(text[:21])
    arquivo2.write('\n')
    arquivo2.write(text[:35])

arquivo2 = open('arquivos/arquivo_os2', 'r')
conteudo2 = arquivo2.read()
arquivo2.close()

print(conteudo2)

