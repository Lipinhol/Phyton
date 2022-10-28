def ficha(jog='<DESCONHECIDO>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


nome = str(input('Digite o nome do jogador: '))
gol = str(input('Quantos gols ele marcou: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0


if nome.strip() == '': # Se o nome for igual a vazio/nullo
    ficha(gol=gol) # a funcao FICHA esta recebendo o valor DESCONHECIDO por padrao e esta passando apenas a quantidade de gols do jogador
else:
    ficha(nome, gol)