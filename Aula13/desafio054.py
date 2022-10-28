from datetime import date

atual = date.today().year
total_maior = 0
total_menor = 0

for pessoas in range(1, 8):
    ano_nascimento = int(input('Ano da {}ª Pessoa: '.format(pessoas)))
    idade = atual - ano_nascimento
    if idade >= 21: 
        total_maior = total_maior + 1
    else:
        total_menor = total_menor + 1
print('O total de pessoas maior de idade é {} e de menor é {}.'.format(total_maior,total_menor))