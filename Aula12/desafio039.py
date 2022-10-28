ano = int(input('Digite seu ano de nascimento: '))
print('ANALISANDO...')
idade = 2022 - ano
print('Você possui {} anos. Portanto: '.format(idade))
if idade < 17:
    print('Você ainda não possui idade minima para o alistamento, volte no ano que completar 18 anos.')
elif idade == 17:
    print('Você está dentro dos parâmetros requeridos para o alistamento! Siga as intrunções do nosso site.')
elif idade > 17:
    print('Você já passou da idade requerida para o alistamento, favor nos contate para maiores informações.')