maior = 0
menor = 0

for pessoas in range(1, 6):
    pesos = float(input('Digite o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos
            
print('O maior peso lido foi {}Kg e o menor foi {}Kg.'.format(maior, menor))