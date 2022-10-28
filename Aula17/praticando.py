valores = []

for contagem in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}.')
print(f'Os numeros em ordem CRESCENTE é {valores.sort()}, e em ordem DESCRESCENTE é {valores.sort(reverse=True)}')
print('Acabou os valores.')