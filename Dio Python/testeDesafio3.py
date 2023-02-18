n = 3

for i in range(n):
    a = input().split()
    b = input().split()
    if a[-len(b):] == b:
        print('encaixa')
        print(len(a))
        print(len(b))
    else:
        print('nao encaixa')
        print(len(a))
        print(len(b))
        