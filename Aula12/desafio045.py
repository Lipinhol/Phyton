from random import choice
from time import sleep

print('''Bem vindo ao desafio do JOKENPô!
Faça sua esolha e tente sua sorte...\n
PEDRA
PAPEL
TESOURA 
''')

escolha_jogador = input('Escreva sua escolha: ').title()
print("A escolha do jogador e: " + str(escolha_jogador))
print("==================================================")
sleep(1)
opcoes_computador = ['Pedra', 'Papel', 'Tesoura']
escolha_computador = choice(opcoes_computador).title()
print("A escolha do computador e: " + escolha_computador)
print("==================================================")


if escolha_computador == 'Pedra' and escolha_jogador == 'Pedra':
    print('A escolha do computador foi {} e sua escolha foi {}. EMPATE! Tente novamente...'.format(escolha_computador, escolha_jogador))
elif escolha_computador == 'Pedra' and escolha_jogador == 'Papel':
    print('A escolha do computador foi {} e sua esolha foi {}. GANHOU! PARABÉNS....'.format(escolha_computador, escolha_jogador))
elif escolha_computador == 'Pedra' and escolha_jogador == 'Tesoura':
    print('A escolha do computador foi {} e sua escolha foi {}. PERDEU! Tente novamente...'.format(escolha_computador, escolha_jogador))
elif escolha_computador == 'Papel' and escolha_jogador == 'Pedra':
    print('A escolha do computador foi {} e sua escolha foi {}. PERDEU! Tente novamente...'.format(escolha_computador, escolha_jogador))
elif escolha_computador == 'Papel' and escolha_jogador == 'Papel':
    print('A escolha do computador foi {} e sua escolha foi {}. EMPATE! Tente novamente...'.format(escolha_computador, escolha_jogador))
elif escolha_computador == 'Papel' and escolha_jogador == 'Tesoura':
    print('A escolha do computador foi {} e sua escolha foi {}. GANHOU! PARABÉNS...'.format(escolha_computador, escolha_jogador))
elif escolha_computador == 'Tesoura' and escolha_jogador == 'Pedra':
    print('A escolha do computador foi {} e sua escolha foi {}. GANHOU! PARABÉNS...'.format(escolha_computador, escolha_jogador))
elif escolha_computador == 'Tesoura' and escolha_jogador == 'Papel':
    print('A escolha do computador foi {} e sua escolha foi {}. PERDEU! Tente novamente...'.format(escolha_computador, escolha_jogador))
elif escolha_computador == 'Tesoura' and escolha_jogador == 'Tesoura':
    print('A escolha do computador foi {} e sua escolha foi {}. EMPATE! Tente novamente...'.format(escolha_computador, escolha_jogador))
else:
    print('Opção esolhida nao funciona. Por favor tente uma das opcoes acima corretamente.')







