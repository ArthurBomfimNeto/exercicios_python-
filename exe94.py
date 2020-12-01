pessoa = dict()
galera =list()
mulher = []
idade =[]
soma = media = 0
while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Qual sexo : ').lower()[0]
        if pessoa['sexo'] in 'MmFf':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade : '))
    galera.append(pessoa.copy())
    while True :
        c = input('Desejar continuar? [S/N]').lower()[0]
        if c in 'sn':
            break
        print('ERRO! Digite apenas S ou N')
    if c in 'n':
       break
for i in galera:
    soma+= i['idade']
media = soma/ len(galera)
for i in galera:
    if i['sexo'] in 'Ff':
        mulher.append(i['nome'])
    if i['idade'] >= media:
        idade.append(i['nome'])
print(f'Cadastradas {len(galera)}')
print(f'A media das idade é {media:.2f}')
print('A lista de mulheres e :',end='')
for i in mulher:
    print(i,end=' ')
print()
print(f'a lista de idade acima da media e : ',end='')
for i in idade:
    print(i,end=' ')








