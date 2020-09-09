'''for par in range(2,51,2):
    print(par, end=' - ')
    par += 2'''

'''num = int(input('Digite um numero: '))
for i in range(1,11):
    result = i*num
    print('{} x {:2} = {:2} '.format(num,i,result))'''

'''soma =0
cont = 0
for i in range(0,6):
   num = int(input('Digite um numero: '))
   if num % 2 == 0:
       soma += num
       cont += 1
print('Voce digitou {} pares e a soma e de {}'.format(cont,soma))'''


'''from time import sleep
n1 =int(input('Digite termo:'))
n2 =int(input('Razão:'))
x = n1
for i in range(0,10):
    print(x,end='-')
    x += n2
    sleep(0.1)
print('ABCABOU')'''

frase = input('Digite uma frase: ').strip().lower()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print(junto)
'''for letra in range(len(junto) -1, -1,-1):
    inverso += junto[letra]'''
print(inverso)
if inverso ==junto:
    print('Temos um palindromo')
else:
    print('Não é um palindromo ')

