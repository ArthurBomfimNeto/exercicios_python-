from time import sleep
from random import randint
matriz = linha = []
print('-=-'*10)
print(F'{"JOGO NA MEGA SENA":^30}')
print('-=-'*10)
n = int(input('Quantos jogos deseja jogar: '))
print(f'{"-=-"*2}{f"SORTEANDO {n} NUMEROS":^22}{"-=-"*2}')
for i in range(0,n):
    linha = []
    for j in range(0,6):
        linha.append(randint(0,60))
    matriz.append(linha)
for i in range(0,n):
    sleep(1)
    print(f'Jogo {i+1}: {matriz[i]}')
print('-=-'*2, ' <BOA SORTE!> ','-=-'*2)

sala = []
c = 's'
while c in 'Ss':
    aluno = []
    for i in range[0,3]:
        aluno.append('Digite nome: ')
        aluno.append('Digite a primeira nota: ')
        aluno.append('Digite a segunda nota: ')
    sala.append(aluno)
    c = input('Deseja continuar? [S/N]')
for r in sala :
    print(r)




