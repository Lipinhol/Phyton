velocidade = float(input('Diga a velocidade do carro: '))

if velocidade > 80:
    print('Você ultrapassou o limite de 80 km/h e será multado.\n')
    multa = (velocidade-80) * 7
    print('Você deverá pagar uma multa no valor de R${:.2f}!'.format(multa))

print('Dirija com segurança, boa viajem!')
