import math

#definição da função

""" def soma(num1, num2):
    print('Primeiro numero: ' + str(num1))
    print('Segundo numero: ' + str(num2))
    print('Soma: ', (num1 + num2))

#Chamando a função e adicionando parâmetros
soma(500000, 500000) """

#Chamando função
   

#Verificando se um numero é primo com a biblioteca Math
def numPrimo(num):
    if (num % 2) == 0 and num > 2:
        return "Esse numero não é primo!"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Esse numero não é primo!"
    return "Esse numero é primo!"   

numPrimo(13)    