from time import sleep 
ano = int(input('Digite seu ano de nascimento:'))
idade = 2022 - ano
print('Sua idade é {} anos.'.format(idade))
sleep(1)
print('ANALISANDO...')
sleep(3)
if idade <= 9:
    print('Seu ano de nascimento é {}, portanto sua categoria é MIRIM.'.format(ano))
elif idade > 9 and idade <= 14:
    print('Seu ano de nascimento é {}, portanto sua categoria é INFANTIL.'.format(ano))
elif idade > 14 and idade <= 19:
    print('Seu ano de nascimento é {}, portanto sua categoria é JUNIOR'.format(ano))
elif idade == 20:
    print('Seu ano de nascimento é {}, portanto sua categoria é SêNIOR.'.format(ano))
elif idade >= 21:
    print('Seu ano de nascimento é {}, portanto sua categoria é MASTER.'.format(ano))
