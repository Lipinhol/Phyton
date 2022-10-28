
time = list()
jogador = dict()
partidas = list()
total = 0
while True:
    jogador.clear()
    nome = jogador['Nome'] = str(input('Nome do jogador: '))
    jogos = jogador['Partidas'] = int(input(f'Quantas partidas {nome.title()} jogou? '))
    partidas.clear()
    for a in range(1,jogos+1):
        partidas.append(int(input(f'Quantos gols na {a}ª partida? ')))
        
    jogador['Gols'] = partidas[:]
    jogador['Total_gols'] = sum(partidas)
    time.append(jogador.copy)

    while True:
        continuar = str(input('Quer continuar? [S/N]')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if continuar == 'N':
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
"""PAREI NO MINUTO 9,40' DO VIDEO DE CORREÇÃO!"""

'''for k, v in jogador.items():
    print(f'A chave: {k}, tem o valor: {v}')
print('=-' * 30)
print(f'O jogador {nome} jogou {jogos} partidas:')
for k, v in enumerate(jogador['Gols']):
    print(f'==> Na {k+1}ª partida fez {v} gols.')
print(f'O {nome} fez um total de {jogador["Total_gols"]} gols.')'''