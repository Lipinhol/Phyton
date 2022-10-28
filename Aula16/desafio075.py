numeros = (int(input('Digite um numero: ')), 
           int(input('Digite outro numero: ')),
           int(input('Mais um numero: ')),
           int(input('O ultimo numero: ')))
print(f'Os numeros digitados foram {numeros}')
print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O numero 3 apareceu na {numeros.index(3)+1}ª posicao.')
else:
    print('O valor 3 não foi digitado nenhuma vez.')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end = ' ')