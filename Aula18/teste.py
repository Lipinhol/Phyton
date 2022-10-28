lista = []
pessoas = 0
mais_pesadas = 0
mais_leves = 0


while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    lista.append(nome)
    lista.append(peso)
    if len(lista) == 0:
        mais_leves = lista [1]
        mais_pesadas = lista [1]
    else:
        if peso > mais_pesadas:
            mais_pesadas = peso
        if peso < mais_leves:
            mais_leves = peso
    pessoas += 1 
    continuar = input(str('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'Foi cadastrado um total de {pessoas} pesssoas na lista.')
print(f'O maior peso é {mais_pesadas}Kg e o menor é {mais_leves}Kg.')