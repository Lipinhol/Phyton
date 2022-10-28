quantidade = 0
soma = 0
numeros = 0

numeros = int(input('Digite um numero inteiro [999 para parar]: '))
while numeros != 999:
    soma = soma + numeros
    quantidade = quantidade + 1
    numeros = int(input('Digite um numero inteiro [999 para parar]: '))
    
       
print('Voce digitou {} numeros e soma entre eles é {}.'.format(quantidade, soma))