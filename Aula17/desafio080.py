lista = []

for n in range(1,6):
    numero = int(input(f'Digite o {n}º valor: '))
    if n == 1 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos = pos + 1

print(lista)

