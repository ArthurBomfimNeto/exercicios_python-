lista = []
c='S'
while c in 'Ss' :
    n = (int(input('digite um numero ')))
    if n in lista :
        print('Numero ja existente .....')
    else:
        lista.append(n)
        print('Numero Adicionado com sucesso .....')
    c = input('Deseja continuar ? [S/N]')
lista.sort()
print(f'Os numeros add foi {lista}')
