salario = float(input('Digite o seu salario: R$'))

if salario > 1250:
    novo_salario = salario + (salario * 10) / 100
    print('Seu novo salário será {}'.format(novo_salario))

else:
    novo_salario = salario + (salario * 15) / 100
    print('Seu novo salário será {}'.format(novo_salario))
