dados = dict()
idade = 0
aposentadoria = 0

while True:
    dados['Nome'] = str(input('Digite o nome: '))
    nascimento = dados['Nascimento'] = int(input('Ano de nascimento: '))
    dados['Idade'] = 2022 - nascimento
    
    trabalho = dados['Carteira de Trabalho'] = int(input('Carteira de trabalho (se não tiver digite 0): '))
    if trabalho == 0:
        break
    contratação = dados['Ano de contratação'] = int(input('Ano de contratação: '))
    if dados['Carteira de Trabalho'] != 0:
        dados['Aposentadoria'] = contratação + 35
    dados['Salário'] = float(input('Salário: R$'))
    break


print('*-*-*-* DADOS *-*-*-*')
for k, v in dados.items():
    print(f'{k} tem o valor {v}')

