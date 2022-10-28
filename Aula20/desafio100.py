from random import randint
from time import sleep

def sorteio(lista):
    print(f'Sorteando 5 números para a lista ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('<===== PRONTO!')

def par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'Somando os valores pares de {lista} temos {soma}')   
            
numeros = list()  
sorteio(numeros)
print(numeros)
par(numeros)