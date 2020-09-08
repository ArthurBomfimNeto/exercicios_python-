from random import shuffle
n1 = input('O primeiro aluno e: ')
n2 = input('O segundo aluno e :')
n3 = input('O terceiro aluno e: ')
n4 = input ('O quarto aluno e: ')
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem e de :')
print(lista)

'''importando toda a biblioteca '''
import random
n1 = input('O primeiro aluno e: ')
n2 = input('O segundo aluno e :')
n3 = input('O terceiro aluno e: ')
n4 = input ('O quarto aluno e: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem e de :')
print(lista)