ano = int(input('Escreva o ano que te direi se este é um ano Bissexto: '))

if ano % 4 == 0 and ano % 100!=0 or ano % 400 == 0:
    print('O ano {} é BISSEXT0!'.format(ano))

else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))
    
