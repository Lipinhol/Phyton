from random import randint
from time import sleep

lista = list()
jogos = list()

print('-' * 30)
print('     JOGOS PARA MEGA SENA     ')
print('-' * 30)

quantidade = int(input('Quantos jogos você deseja fazer? '))
total = 1

while total <= quantidade:
    cont = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total = total + 1
print('=-' * 3, f'SORTEANDO {quantidade} JOGOS', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-' * 5, 'BOA SORTE!', '=-' * 5)