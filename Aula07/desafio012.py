preço = int(input('Diga o valor do produto: '))
desconto = (preço*5) / 100
novo_valor = preço - desconto

print('O valor original do produto é {}, com a promoção de desconto ele ficará {}'.format(preço, novo_valor))