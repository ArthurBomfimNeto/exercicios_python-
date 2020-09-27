import random
print('-=-'*20)
print('VAMOR JOGAR PAR OU IMPAR ')
print('-=-'*20)
n = int(input("Digite um valor:"))
computador = random.randint(0,20)
pi = input('Par ou Impar? [P/I] ').lower()
cont = acertou = 0
while True:
    if cont == 2 :
        break
    if (computador + n) % 2 == 0 and pi =='p':
        print('VOCE VENCEU !!')
        print(f'Voce jogou {n} e o cumputador {computador} somando {computador + n}')
        print('-=-' * 20)
        aacertou += 1
    elif (computador + n) % 2 == 1 and pi =='i':
        print('VOCE VENCEU !!')
        print(f'Voce jogou {n} e o cumputador {computador} somando {computador + n}')
        print('-=-' * 20)
        acertou += 1

    else:
        print('VOCE PERDEU ! :(')
        print(f'Voce jogou {n} e o cumputador {computador} somando {computador + n}')
    cont+=1
    n = int(input("Digite um valor:"))
    pi = input('Par ou Impar? [P/I] ').lower()
print('fim vc venceu {} vez'.format(acertou))




