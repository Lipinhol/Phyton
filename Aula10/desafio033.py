n1 = float(input('Digite um numero: '))
n2 = float(input('Outro numero: '))
n3 = float(input('Mais um: '))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1>n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('Dos numeros escolhidos o menor é {:.2f} e o maior é {:.2f}.'.format(menor, maior))


