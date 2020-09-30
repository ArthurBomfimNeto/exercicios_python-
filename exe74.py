from random import randint
tup =(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores foram ', end='')
for n in tup:
    print(f'{n}',end=' ')
print(f'\nO maior {max(tup)} o menor {min(tup)}')





