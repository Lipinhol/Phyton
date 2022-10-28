pares = 0
terceira_coluna = 0
segunda_linha_maior = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
print('=-' * 30)    
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
        if matriz[l] [c] % 2 == 0:
            pares = pares + matriz[l] [c]
    print()

print('=-' * 30)
print(f'A soma dos numeros pares é {pares}.')
for l in range(0, 3):
    terceira_coluna = terceira_coluna + matriz[l] [2]
print(f'A soma da terceira coluna é {terceira_coluna}.')
for c in range(0, 3):
    if c == 0:
        segunda_linha_maior = matriz[1] [c]
    elif matriz [1] [c] > segunda_linha_maior:
        segunda_linha_maior = matriz[1] [c]
print(f'O maior numero da segunda linha da é {segunda_linha_maior}.')

