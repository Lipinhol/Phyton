from random import randint

numeros = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Tente adivinhar o número sorteado de 0 a 10: '))
    palpites = palpites + 1
    if numeros == jogador:
        acertou = True
    else:
        if jogador > numeros:
            print('Menos...')
        elif jogador < numeros:
            print('Mais...')
        
print('Acertou o numero com {} tentativas.'.format(palpites))