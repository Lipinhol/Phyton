temp = []
lista = []
pessoas = 0
mais_pesadas = 0
mais_leves = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
        
    if len(lista) == 0:
        mais_leves = temp [1]
        mais_pesadas = temp [1]
    else:
        if temp[1] > mais_pesadas:
            mais_pesadas = temp[1]
        if temp[1] < mais_leves:
            mais_leves = temp[1]
    lista.append(temp[:])
    temp.clear()
    pessoas += 1 
    continuar = input(str('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'Foi cadastrado um total de {pessoas} pesssoas na lista.')
print(f'O maior peso é {mais_pesadas}Kg e o menor é {mais_leves}Kg.')
