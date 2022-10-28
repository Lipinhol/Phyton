from random import randint
from time import sleep
from operator import itemgetter

resultados ={'Jogador 1' : randint(1,6),
            'Jogador 2' : randint(1,6),
            'Jogador 3' : randint(1,6),
            'Jogador 4' : randint(1,6)}
ranking = list()
print('  --- VALORES SORTEADOS: ---')
for k, v in resultados.items():
    print(f'{k} tirou o valor {v}')
    sleep(1)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('=-' * 20)
print('        ---  RANKING  ---')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)




