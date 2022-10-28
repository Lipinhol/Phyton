num = [[], []]

for v in range(1,8):
    valor = int(input(f'Digite o {v}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()

print(f'Os numeros Pares em ordem crescente é: {num[0]}')
print(f'Os numeros Impares em ordem crescente é: {num[1]}')


