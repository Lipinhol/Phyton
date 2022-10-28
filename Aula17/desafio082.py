lista = []
pares = []
impares = []

while True:
    numeros = (int(input('Digite um valor: ')))
    lista.append(numeros)
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista completa é {lista}')
print(f'Os numeros pares da lista são {pares}')
print(f'Os numeros impares da lista são {impares}')
