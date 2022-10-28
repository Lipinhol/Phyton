aluno = dict()

aluno['Nome'] = str(input('Nome do aluno(a): ')).title()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Media'] >= 7.0:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')