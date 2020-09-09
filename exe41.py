from datetime import date
data = int(input('Digite a data de nascimento: '))
atual = date.today().year

if atual - data <= 9 :
    print('Voce tem {} anos e e uma MIRIM!!'.format(atual - data))
elif atual - data <= 14:
    print('Voce tem {} anos e e uma INFANTIL!!'.format( atual - data))
elif atual - data <= 19:
    print('Voce tem {} anos e e uma JUNIOR!!'.format( atual - data))
elif atual - data <= 25:
    print('Voce tem {} anos e e uma SENIOR!!'.format(atual - data))
else:
    print('Voce tem {} anos e e uma MASTER!!'.format(atual - data))
