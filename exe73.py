time = ('corintians','palmeiras','santos','gremio','cruzeiro','flamengo','vasco','chapecoense',
    'atletico','botafogo','atletico-pr','bahia','sp','flunminense','sport','vitoria','coritiba','avai','ponte preta','atletico-go')
print('-=-'*20)
print(time)
print('-=-'*20)
print(f'Os primeiro 5 colocado {time[0:5]}')
print('-=-'*20)
print(f'Os ultimos 4 colocado {time[-4:]}')
print('-=-'*20)
print(f'Ordem alfabetica {sorted(time)}')
print('-=-'*20)
n = ''
for i in range(0,len(time)):
    if time[i]=='chapecoense':
        n = i
print(f'O chapecoense eta na posiçao{time.index("chapecoense")+1} ')

print(f'A posição do {time[n]} e {n+1}')





