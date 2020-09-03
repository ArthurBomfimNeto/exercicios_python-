'''Importando a biblioteca'''
from math import radians,cos,tan,sin
an = float(input('Digite o angulo :'))
seno = sin(radians(an))
print('O angulo de {} tem o seno de {:.2f}'.format(an , seno))
cosseno = cos(radians(an))
print('o angulu de {} tem o coseno de {:.2f} '.format(an,cosseno))
tangente= tan(radians(an))
print('o angulo {} tem a tengente de {:.2f} '.format(an,tangente))


