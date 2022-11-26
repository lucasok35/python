import math

#definição da função

""" def soma(num1, num2):
    print('Primeiro numero: ' + str(num1))
    print('Segundo numero: ' + str(num2))
    print('Soma: ', (num1 + num2))

#Chamando a função e adicionando parâmetros
soma(500000, 500000) """

#Chamando função
   

#Verificando se um numero é primo com a biblioteca Math //Executado no jupyter notebook
""" def numPrimo(num):
    if (num % 2) == 0 and num > 2:
        return "Esse numero não é primo!"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Esse numero não é primo!"
    return "Esse numero é primo!"   

numPrimo(13)     """

#Função criada para fazer split dos dados
""" text = 'O impossível não existe para aquele que crê'

#Definindo a função
def split_string(text):
    return text.split(' ')

#print(split_string(text))

#Gravando o resultado da função em uma varíavel
palavras = split_string(text)
print(palavras) """

#Aderindo letras minusculas para todo o texto


""" letra_minuscula = 'Quero Tudo Minusculo Nesse Texto'

#Definindo função com parâmetro
def lowertext(letra_minuscula):
    return letra_minuscula.lower()

#Chamando função dentro da função print
print(lowertext(letra_minuscula)) """

#Como definir função com número de parâmetros indefinidos

def somaParam(par1, *vartuple):
    #imprime parâmetros
    soma = 0
    print('Parâmetro: ', par1)
    for item in vartuple:
        print('Parâmetro: ', item)
        soma = soma + item
    return print('Total da soma dos parâmetros: ', soma + par1)    
    
somaParam(10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)   