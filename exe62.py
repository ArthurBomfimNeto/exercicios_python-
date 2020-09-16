print('-=-'*20)
termo = int(input('Primeiro termo:'))
razão = int(input('Razão da PA: '))

cont = 1
mais = 11
x = termo
total=0
while mais != 0:
    total += mais
    while cont != total:
        print(x,end='-')
        x += razão
        cont += 1
    print('Acabou')
    mais = int(input('Quantos mais vc quer mostrar:'))
