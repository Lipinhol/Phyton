valor = float(input('Digite o valor do protudo: R$ '))

a_vista = valor - (valor * 10) / 100 
cartao = valor - (valor * 5) / 100
parcelado = valor + (valor * 20) / 100

print('''Selecio uma das opções de pagamentos abaixo:
[1]A VISTA
[2]A VISTA NO CARTAO
[3]EM ATÉ 2X NO CARTAO
[4]EM 3X OU MAIS
''')
opcao = int(input('Digite a opçao desejada: '))

if opcao == 1:
    print('Para pagamento a vista do valor de R${} tem um desconto de 10%. Valor a ser pago será R${}'.format(valor, a_vista)) 
elif opcao == 2:
    print('Para pagamento a vista no cartao do valor de R${} tem um desconto de 5%. Valor a ser pago será R${}'.format(valor, cartao))
elif opcao == 3:
    print('Para o pagamento em até 2x no cartão não temos desconto. Valor a ser pago será R${}'.format(valor))
elif opcao == 4:
    print('Para pagamento em 3x ou mais no cartao do valor de R${} temos um juros de 20%. O valor a ser pago será R${}'.format(valor, parcelado))
else:
    print('Algo deu errado. Digite uma opçao de 1 a 4 para continuarmos.')
