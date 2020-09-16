
import time
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
print('=-='*20)
print('''1 - somar
2 - multiplicar 
3 - maior 
4 - novos numeros
5 - sair''')
op = int(input('>>>>Qual sua opção: '))
maior = n1
while op != 5:
    if op ==1:
        print('A soma de {} + {} e {}'.format(n1,n2,n1+n2))
    elif op == 2:
        print('A multiplicação de {} x {} e {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 < n2:
            maior= n2
        print('entre {} e {} o maior e {}'.format(n1, n2, maior))
    elif op == 4:
        print('-------DIGITE NOVOS NUMERO------')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    else:
        print('!!!Digitos ivalidos!!!')
    print('')
    print('=-='*20)
    print('''
    1 - somar
    2 - multiplicar 
    3 - maior 
    4 novos numeros
    5 - sair''')
    op = int(input('>>>>Qual sua opção: '))
print('''finalizando...''')
time.sleep(2)
print('the end ')
