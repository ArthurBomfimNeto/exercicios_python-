'''frase = "      Curso em video python     "'''
#print(frase.count('o')) conta quantas letras tem
#print(frase.find('deo')) procura se tem e volta a posição que começa.
#print('em' in frase) VE SE TEM NA FRASE E RETORNA Tru or False
#print(frase.replace('python','Android')) TROCA A FRASE
#print(frase.upper()) MUDA TUDO PARA MAIUSCULO.
#print(frase.lower()) MUDA TUDO PARA MINUSCULO.
#print(frase.capitalize())a frase fica minuscula apenas a primeira letra maiuscula
#print(frase.title()) coloca começo de frases com maiuscula
#print(frase.strip()) tira espaços no começo e final da frase
#print(frase.rstrip())tira espaços no começo da frase
#print(frase.lstrip()) tira espaços no final da frase
#len(fease) Ler o numero da lista ou vetor
#frase= frase.split() quebra a palvra no espaço e cada palavra fica em uma posição da lista
#frase = ''.join(frase)desfraciona a lista de acordo com o que vc por no parente

nome = input('nome:').strip()
print('Letras maiusculas {} :'.format(nome.upper()))
print('Letras minusculas {}'.format(nome.lower()))
nome = nome.split()
print('Tem {} letras o prieiro nome {}'.format(len(nome[0]),nome[0]))
nome = ' '.join(nome)
separa = nome.split()
print(nome)
print('Tem {} letras o prieiro nome {} '.format(nome.find(' '),separa[0]))
print('O nome te {} lestras no total sem contar os espaços'.format(len(nome) - nome.count(' ')))





