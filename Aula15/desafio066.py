quantidade = 0
soma = 0
numeros = 0

while numeros != 999:
    numeros = int(input('Digite um numero [Digite 999 para sair]: '))
    if numeros == 999:
        break
    soma = soma + numeros
    quantidade = quantidade + 1

print(f'A quantidade de numeros digitado foi {quantidade} e a soma deles é {soma}.')

