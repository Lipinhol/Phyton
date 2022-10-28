galera = list()
dado = list()
total_maior = total_menor = 0

for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior = total_maior + 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1
        
print(f'Temos {total_maior} maior de idade e {total_menor} menores de idade.')