import math 
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2}'.format(num, raiz))

'''Outra maneira de importar abaixo.'''

from math import sqrt,floor
num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

'''Abaixo exemplo de um numero aleatório'''

import random
num = random.randint(1, 10)
print (num)
