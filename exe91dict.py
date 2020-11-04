from random import randint
from time import sleep
from operator import itemgetter
jogadores ={'jogador1': randint(1,6) , 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
ranking = {}
print('Valores sorteados:')
for k,v in jogadores.items():
    sleep(0.5)
    print(f'O {k} tirou {v}')
print('=-='*15)
print('Ranking dos jogadores:')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for n , i in enumerate(ranking):
    sleep(0.5)
    print(f'{n+1}° lugar: {i[0]} com {i[1]} ')



