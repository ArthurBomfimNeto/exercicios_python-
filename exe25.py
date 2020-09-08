nome = input('Digite o nome: ').strip().lower()
separado = nome.split()
a = 0
for i in range(0,len(separado)):
     if separado[i] == 'silva':
         a = 1
print('O nome tem silva ?')
print(a == 1)

nome = input('Digite o nome: ').strip().lower()
print('Seu nome tem silva ? {}'.format('silva' in nome))


