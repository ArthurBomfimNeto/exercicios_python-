from random import randint
from time import sleep
computador = randint(0,10)
print('-=-'*20)
print('\033[1;34m Vou pensar em um numero entre 0 e 10. Tente acertar\033[m...')
print('-=-'*20)
num = int(input('Que numero eu pensei: '))
print('''\033[4;35mPROCESSANDO...\033[m''')
sleep(2)
cont = 1
while num != computador:
    cont += 1
    if num < computador:
        print('Mais...Tente mais uma vez')
        num = int(input('Que numero eu pensei: '))
    else:
        print('Menos...Tente mais uma vez')
        num = int(input('Que numero eu pensei: '))
print('Acertou com {} tentativas. Parabéns'.format(cont))



