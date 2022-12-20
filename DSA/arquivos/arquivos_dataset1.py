#Automatizando a criação de arquivos com Python

criandoArquivo = input('Digite o nome do arquivo!')

#Atribuindo extensão do arquivo
criandoArquivo = criandoArquivo + '.txt'

#Abrindo arquivo criado para escrita
arq_dataset = open('criandoArquivo.txt', 'w')

arq_dataset.write('Adicionando texto ao arquivo criado')
arq_dataset.close()

#Abrindo arquivo criado para leitura
arq_dataset = open('criandoArquivo.txt', 'r')
print(arq_dataset.read())
arq_dataset.close()
