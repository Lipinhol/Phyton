aproveitamento = dict()
partidas = list()
total = 0

nome = aproveitamento['Nome'] = str(input('Nome do jogador: '))
jogos = aproveitamento['Partidas'] = int(input(f'Quantas partidas {nome.title()} jogou? '))

for a in range(1,jogos+1):
    partidas.append(int(input(f'Quantos gols na {a}ª partida? ')))
    
aproveitamento['Gols'] = partidas[:]
aproveitamento['Total_gols'] = sum(partidas)
print(aproveitamento)
print('=-' * 30)
for k, v in aproveitamento.items():
    print(f'A chave: {k}, tem o valor: {v}')
print('=-' * 30)
print(f'O jogador {nome} jogou {jogos} partidas:')
for k, v in enumerate(aproveitamento['Gols']):
    print(f'==> Na {k+1}ª partida fez {v} gols.')
print(f'O {nome} fez um total de {aproveitamento["Total_gols"]} gols.')


