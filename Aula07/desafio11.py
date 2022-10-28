a = int(input('Digite a altura da parede: '))
l = int(input('Digite a largura da parede: '))
area = a * l
litros = area / 2

print('A altura da parede é {} e sua largura {}. Logo temos {} m² de parede quais serão necessários {}L para pintar.'.format(a, l, area, litros))
