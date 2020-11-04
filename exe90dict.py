aluno = dict()
aluno['nome'] = input('Digite o nome: ')
aluno['media'] = float(input('Digite a media: '))
if aluno['media'] >= 6:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Reprovado'
for i in aluno.values():
    print(i,end=' ')