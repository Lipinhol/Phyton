co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))

'''Importando o método da hipotenusa do MATH (abaixo)'''

from math import hypot
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))