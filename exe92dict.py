from datetime import date
pessoa = dict()
data = date.today()
pessoa['nome'] = input('Digite o nome: ')
ano = int(input('Ano de nascimento: '))
pessoa['carteira'] = int(input('Carteira de trabalho (0 se não tiver) : '))
pessoa['idade'] = data.year - ano
if pessoa['carteira'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('Salario: '))
    pessoa['aposentadoria'] = pessoa['idade']+(35 - ( data.year - pessoa['contratação'] ))
print('-=='*10)
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')

