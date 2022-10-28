maior_18 = 0
homens = 0
mulheres_menos_18 = 0

while True:
    idade = int(input('Digite a idade desta pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior_18 = maior_18 + 1

    if sexo == 'M':
        homens = homens + 1

    if sexo == 'F' and idade < 18:
        mulheres_menos_18 = mulheres_menos_18 + 1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais pessoas? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'No cadastro há {maior_18} pessoas maior de 18 anos, {homens} homens e {mulheres_menos_18} mulheres menor de 18 anos.')

    


