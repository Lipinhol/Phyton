lista = []


while True:
    numeros = int(input('Digite um valor: '))
    if numeros not in lista:
        lista.append(numeros)
    else:
        print('Este numero ja foi informado, não será adicionado.')
    resp = str(input('Você deseja continuar? [S/N]'))
    if resp in 'Nn':
        break

lista.sort()

print(f'Os numeros digitados foram: {lista} ')


