palavra = ('APRENDER','PROGRAMAR','LINGUAGEM','PHYTON','CURSO')

for p in palavra:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
