from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'*20)
print('\033[1;34m Vou pensar em um numero entre 0 e 5. Tente acertar\033[m...')
print('-=-'*20)
num = int(input('Que numero eu pensei: '))
print('''\033[4;35mPROCESSANDO...\033[m
''')
sleep(2)
if computador == num:
    print('Voce acerto!!!!')
    print()
else:
    print('--Voce errou eu pensei no {} e não no {} :('.format(computador,num))