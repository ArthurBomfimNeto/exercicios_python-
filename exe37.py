import time
num = int(input('Digite um numero inteiro : '))
print('''Escolha umas da opções a baixo:
1 - converter para BINARIO
2 - converter para OCTAL
3 - converter para HEXADECIMAL ''')
opcao = int(input('Sua opção: '))
print('PROCESSANDO...')
time.sleep(2)
if opcao == 1 :
    print('O numero inteiro {} em BINARIO é {} '.format(num,bin(num)[2:]))
elif opcao == 2:
    print('O numero inteiro {} em BINARIO é {} '.format(num, oct(num)[2:]))
elif opcao == 3 :
    print('O numero inteiro {} em BINARIO é {} '.format(num,hex(num)[2:]))
else:
    print('Opção invalida')

