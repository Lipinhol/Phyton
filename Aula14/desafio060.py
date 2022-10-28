from math import factorial

numero = int(input('Digite um numero que lhe direi seu fatorial: '))
f = factorial(numero)

print('O fatorial de {} é {}.'.format(numero, f))