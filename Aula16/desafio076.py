listagem = ('lapis', 1, 'mochila', 100.50, 'estoujo', 7.25, 'caderno', 12.78,
          'caneta', 2, 'regua', 4, 'transferidor', 9.90, 'borracha', 3.50,
          'apontador', 7.25)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for posição in range(0, len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição].title():.<30}', end='')
    else:
        print(f'R${listagem[posição]:.2f}')
print('-' * 40)