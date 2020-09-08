frase = input('Digite uma frase: ').strip().lower()
print('A letra ´A´ aparece: {} vezes'.format(frase.count('a')))
print('Ela aparece a primeira vez na posição: {}'.format(frase.find('a')+1))
print('Ela aparece pela ultima vez na posição: {}'.format(frase.rfind('a')+1))

