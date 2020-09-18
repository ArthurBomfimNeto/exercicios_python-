n = int(input('Digite um numero'))
soma = cont = 0
while n != 999:
    if n != 999:
        soma += n
        cont +=1
        n = int(input('Digite um numero'))
print('Voce digitou {} numeros e a soma e {} '.format(cont,soma))



