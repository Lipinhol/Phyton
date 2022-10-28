quantidade = 0
maior = 0
menor = 0
soma = 0
resposta = 'S'

while resposta in 'Ss':
    num = int(input('Digite um valor: '))
    quantidade = quantidade + 1
    soma = soma + num
    if quantidade == 1:
        maior = num
        menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()

calculo_media = soma / quantidade
print('A media entre os valores digitados é {}.'.format(calculo_media))
print('O maior numero entre eles é {} e o menor é {}.'.format(maior, menor))
