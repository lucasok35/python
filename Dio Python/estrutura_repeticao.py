#Exemplos de estrutura de repetição

nome = 'Lucas Henrique Teixeira da Silva\n'

for letra in nome:
    print(letra.upper(), end='')    

for i in range(101):
    print(i,'\n', end='')
    while i == 10:
        print('Entrando no while\n')
        break             
      
   