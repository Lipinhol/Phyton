from cgi import print_form


salário = int(input('Digite seu salário atual para saber quanto ele ficará com o aumento: '))
aumento = (salário*15) / 100
novo_salário = salário + aumento

print('Seu salário atual é R${}, mas logo após o aumento você passará a receber R${}'.format(salário, novo_salário))