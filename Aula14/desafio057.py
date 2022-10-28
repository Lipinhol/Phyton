sexo = str(input('Digite seu sexo [M/F]: ')).title().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Favor digitar corretamente conforme solicitado. Informe seu sexo: '))

print('Muito bem, verificamos nos seus dados que seu sexo é {}.'.format(sexo))