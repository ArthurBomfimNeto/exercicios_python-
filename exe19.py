from random import choice
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno: ')
n3 = input('terceiro aluno ')
n4 = input('quarto aluno ')

lista=[n1,n2,n3,n4]
escolhido = choice(lista)
print('O alino escolhido foi {}'.format(escolhido))

'''importando a biblioteca toda '''
import random
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno: ')
n3 = input('terceiro aluno ')
n4 = input('quarto aluno ')

lista=[n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))