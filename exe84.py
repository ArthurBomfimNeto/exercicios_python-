num = [[],[]]
for i in range(1,8):
    n = int(input(f'Digite um valor {i}: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
print(f'Numeros pares {num[0]}')
num[1].sort(reverse=True)
print(f'Numeros impares {num[1]}')

