lista = []


while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)

    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
  
print(f'Foram digitados na lista um total de {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'A lista em sua forma decrescente é {lista}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não foi digitado, por isso não está na lista.')

