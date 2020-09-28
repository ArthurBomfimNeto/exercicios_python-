CPF = input("Digite o cpf (apenas numeros): ").strip()
cpf = []
teste1 = [10,9,8,7,6,5,4,3,2]
teste2 = [11,10,9,8,7,6,5,4,3,2]
soma1 = soma2 = resto = 0
for i in CPF:
    cpf.append(int(i))

for i in range(0,9):
    soma1 += cpf[i] * teste1[i]
resto = (soma1 * 10) % 11
if resto == 10:
    resto=0
if resto == cpf[9]:
    for i in range(0, 10):
        soma2 += cpf[i] * teste2[i]
    resto = (soma2 * 10) % 11
    if resto == 10:
        resto = 0
    if resto == cpf[10]:
        print('CPF valido ')
    else:
        print('ERRO !!!!! CPF invalido ')
else:
    print('ERRO !!!!! CPF invalido ')






