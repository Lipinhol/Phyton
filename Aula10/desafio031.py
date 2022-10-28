distancia = float(input('Diga a distância que será percorrida em sua viajem: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('A distância da sua viajem é {}Km, portanto o valor cobrado será R${}.'.format(distancia, valor))

else:
    valor = distancia * 0.45
    print('A distância da sua viajem é {}Km, portanto o valor cobrado será R${}.'.format(distancia, valor))