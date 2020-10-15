sala = []
c = 's'
while c in 'Ss':
    aluno = []
    aluno.append(input('Digite nome: '))
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))
    sala.append(aluno)
    c = input('Deseja continuar? [S/N]')
print('NOME       MEDIA')
for r in sala :
    print(f'{r[0]}          {(r[1]+r[2])/2}')
r = int(input('Mostrar notas de qual aluno? 999 parar'))
while r != 999:
    print(f'As notas do {sala[r][0]} é {sala[r][1]} e {sala[r][2]}')
    r = int(input('Mostrar notas de qual aluno? 999 parar'))

