from random import choice
from time import sleep
numeros = [0, 1, 2, 3, 4 ,5]
escolhido = choice(numeros)

jogador = int(input('Tente adivinhar o número sorteado de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if escolhido == jogador:
    print('PARABÉNS, você acertou o número!')
else:
    print('ERROU, eu escolhi o numero {} e não o {}, tente novamente.'.format(escolhido, jogador))
