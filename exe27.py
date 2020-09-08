nome = input('Digite o nome:')
nm = nome
nome = nome.split()
print('muito prazer {}'.format(nm))
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu segundo nome é {} '.format(nome[len(nome)-1]))