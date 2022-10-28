from random import randint

soma = 0
vitorias = 0

while True:
    numero = int(input('Escolha seu numero até 10: '))
    computador = randint(0, 10)
    soma = numero + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I]')).title().strip()
    print(f'Voce jogou {numero} e o computador {computador}. Total é {soma}.')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você GANHOU!')
            vitorias = vitorias + 1
        else:
            print('Voce PERDEU!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
                print('Você GANHOU!')
                vitorias = vitorias + 1
        else:
            print('Voce PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {vitorias} vezes!')
        






