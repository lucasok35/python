#Laboratorio 3
#Solicitando operação ao usuário
'********************************Calculadora*********************************'
print('Qual das operações abaixo deseja escolher?')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

operacao = int(input('Qual operação deseja escolher?'))

if operacao == 1:
    #Solicitando parametros da função para o usuario
    num1 = float(input('Digite o primeiro numero:'))
    num2 = float(input('Digite o segundo numero:'))
    #Declarando função que realiza a operação
    soma = lambda x, y: x + y
    #Imprimindo o resultado da operação chamando a função
    print(soma(num1, num2))

elif operacao == 2:
    #Solicitando parametros da função para o usuario
    num1 = float(input('Digite o primeiro numero:'))
    num2 = float(input('Digite o segundo numero:'))
    #Declarando função que realiza a operação
    soma = lambda x, y: x - y
    #Imprimindo o resultado da operação chamando a função
    print(soma(num1, num2))
elif operacao == 3:
    #Solicitando parametros da função para o usuario
    num1 = float(input('Digite o primeiro numero:'))
    num2 = float(input('Digite o segundo numero:'))
    #Declarando função que realiza a operação
    soma = lambda x, y: x * y
    #Imprimindo o resultado da operação chamando a função
    print(soma(num1, num2))
elif operacao == 4:
    #Solicitando parametros da função para o usuario
    num1 = float(input('Digite o primeiro numero:'))
    num2 = float(input('Digite o segundo numero:'))
    #Declarando função que realiza a operação
    soma = lambda x, y: x / y
    #Imprimindo o resultado da operação chamando a função
    print(soma(num1, num2))
else:
    print('Escolha uma opção válida')
