soma = 0
media_idade = 0
homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0

for p in range(1, 5):
    nome = str(input('Digite seu nome: ')).strip().title()
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    idade = int(input('Digite sua idade: '))
    soma = soma + idade

    if p == 1 and sexo in 'M':
        homem_mais_velho = idade
    if sexo in 'M' and idade > homem_mais_velho:
        homem_mais_velho = idade
    if sexo in 'F' and idade < 20:
        mulheres_menos_20 = mulheres_menos_20 + 1

nome_homem_mais_velho = nome
media_idade = soma / 4

print('A media de idade do grupo é {} anos.'.format(media_idade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nome_homem_mais_velho, homem_mais_velho))
print('O total de mulheres com menos de 20 anos é {}.'.format(mulheres_menos_20))