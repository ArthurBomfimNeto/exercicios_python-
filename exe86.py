linha = coluna = []
soma = soma1 = maior =0
for i in range(0,3):
    linha =[]
    for j in range(0,3):
        linha.append(int(input(f'Digite um valor para [{i},{j}]')))
    coluna.append(linha)
for i in range(0, 3):
    soma1 += coluna[i][2]
    if maior < coluna[1][i]:
        maior = coluna[1][i]
    for j in range(0, 3):
       print(f'[{coluna[i][j]:^5}]', end='')
       if coluna[i][j] % 2 == 0:
          soma += coluna[i][j]
    print()
print('A soma dos pares: ' ,soma)
print('Soma da terceira coluna: ',soma1)
print('Maior numero da segunda linha: ',maior)

