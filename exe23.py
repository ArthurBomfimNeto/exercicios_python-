num = input( 'Digite um numero de 0 a 9999: ')
print('Analisando o numero {}'.format(num))
print('unidade: {}'.format(num[3]))
print('dezena: {}'.format(num[2]))
print('centena: {}'.format(num[1]))
print('milhar: {}'.format(num[0]))

num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))