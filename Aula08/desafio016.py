from math import trunc
num = float(input('Digite um número com decimal: '))
num_inteiro = trunc(num)

print('A parte inteira do número {} é {}.'.format(num, num_inteiro))