from io import RawIOBase

num = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversão:
[1] converter para a base BINÁRIO 
[2] converter para a base OCTAL 
[3] converter para a base HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('O numero {} em BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O numero {} em OCTAL é {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O numero {} em HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
