#Exercicio 1
""" def numerospares():
    for i in range(2, 21, 2):
        print(i)
    
numerospares() """

#Exercicio 2
""" def maiusculas(x):
    print(x.upper())
    return
maiusculas('Eu sou invencivel')    
 """

#Exercicio 3
""" lista = ['Lucas', 'Determinado', 'Equilibrado', 'Objetivo']
lista2 = ['dinamico', 'arrojado']
def imprimelista(lista):
    lista.extend(lista2)
    return

imprimelista(lista)
print(lista) """

#Exercicio 4
""" def funcaodinamica(x, *vartuple):
    print(x)
    for item in vartuple:
        print(item)
    return

funcaodinamica(1)
funcaodinamica(1, 2, 3, 4) """

#Exercicio 5
""" soma = lambda num1, num2: num1 + num2

print(soma(2000000, 500000)) """

#Exercicio 6
""" total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total) """

#Exercício 7
#F = 37 x 1,8 + 32;

""" Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda f:f * float(9/5) + 32, Celsius)
print (list(Fahrenheit))
 """

 #Exercício 8
""" dic_met = {'met':1, 'met':2, 'met':3}
print(dir(dic_met)) """

#Exercicio 9
""" import pandas as pd
print(dir(pd))
 """

 #Exercicio 10
""" import pandas as pd
file_name = 'binary.csv'

def resEst(file_name):
    df = pd.read_csv(file_name)
    return df.describe()
print(resEst(file_name)) """