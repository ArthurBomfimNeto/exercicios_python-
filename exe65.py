continuar = "s"
soma = maior = menor =cont = 0

while continuar in 'Ss':
    n = int(input('Digite um numero'))
    continuar = input('Deseja continuar? [S/N]').strip().lower()
    cont += 1
    soma += n
    if cont ==1:
        maior = menor = n
    else:
        if n > maior :
            maior = n
        if menor > n :
            menor = n
print(f'Voce digitou {cont} numeros e a media foi {soma/cont:.2f} ')
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))


