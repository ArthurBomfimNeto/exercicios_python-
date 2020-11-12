jogador = {}
gol=[]
jogador['nome'] = input('Nome: ')
partidas = int(input('Quntas partidas: '))
for i in range(0,partidas):
    gol.append(int(input(f'Quantos gols na partida {i+1}? ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print('-=-'*15)
print(jogador)
print('-=-'*15)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*15)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i , n in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {n} gols.')
print(f'Foi um total de {jogador["total"]} gols')

