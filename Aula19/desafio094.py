cadastro = dict()
galera = list()
tot_pessoas = 0
soma = 0
media = 0
mulheres = 0

while True:
    cadastro.clear()
    nome = cadastro['Nome'] = str(input('Nome: '))
    while True:
        sexo = cadastro['Sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if sexo == 'F':
            mulheres = mulheres + 1
        if sexo in 'MF':
            break
        
        print('ERRO! Por favor digite apenas M ou F.')

    idade = cadastro['Idade'] = int(input('Idade: '))
    soma = soma + cadastro['Idade']
    galera.append(cadastro.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Favor digite apenas S ou N.')    
    tot_pessoas = tot_pessoas + 1
    if continuar == 'N':
        break
media = soma / tot_pessoas
print(galera)
print(f'Foram cadastradas um total de {tot_pessoas} pessoas.')
print(f'A médias das idades é {media} anos.')
print(f'Ao total temos {mulheres} mulheres na lista.')
print(f'As mulheres são: ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}, ', end='')
print()
print('Lista das pessoas que estão acima da média de idade: ')
for p in galera:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<<ENCERRADO>>>>')