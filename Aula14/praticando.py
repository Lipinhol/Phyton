quantidade = 0
maior = 0
menor = 0
soma = 0
media = soma / quantidade

valor = int(input('Digite um valor: '))
continuar = str(input('Quer continuar? [S/N]')).upper

while continuar == 'S':
    quantidade = quantidade + 1
    soma = soma + valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

