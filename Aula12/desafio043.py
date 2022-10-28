from time import sleep

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('CALCULANDO...')
sleep(2)

if imc < 18.5:
    print('Seu imc é {:.2f}. Você está ABAIXO do peso.'.format(imc))
elif imc >= 18.5 and imc < 25.0:
    print('Seu IMC é {:.2f}. Seu peso é o IDEAL!'.format(imc))
elif imc >= 25.0 and imc < 30.0:
    print('Seu IMC é {:.2f}. Você está com SOBREPESO.'.format(imc))
elif imc >= 30.0 and imc < 40.0:
    print('Seu IMC é {:.2f}. Você está com OBESIDADE.'.format(imc))
elif imc >= 40.0:
    print('Seu IMC é {:.2f}. Você está com OBESIDADE MÓRBIDA.'.format(imc))