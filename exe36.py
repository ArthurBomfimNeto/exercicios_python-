import time
valor = int(input('Qual valor da casa? '))
salario = int(input('Qual o salario dele:'))
anos = int(input('Quantos anos ira parcelar: '))
mensal = valor/(anos*12)
porcent = salario * 0.30
print('\033[1;34mPROCESSANDO...\033[m')
time.sleep(2)
if porcent <= mensal :
    print('Emprestimo NEGADO!!!')
else:
    print('Emprestimo APROVADO!!!')

print('O valor mensal e de {:.2f} e o valor minimo a pagar e de {}'.format(mensal,porcent))

