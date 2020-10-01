listagem = ('Lapis',1.75,
            'Borracha',2.0,
            'Caderno',15.9,
            'Estojo',25,
            'Compasso',9.99)
print('--'*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--'*20)

for pos in range(0,len(listagem)):
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'{listagem[pos]:>7.2f}')