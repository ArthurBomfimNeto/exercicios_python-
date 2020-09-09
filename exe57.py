sexo = str(input('Digite o sexo:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dados invalidos.Por favor digite o sexo:').strip().upper()[0]
print('Boa digito certo!!')


